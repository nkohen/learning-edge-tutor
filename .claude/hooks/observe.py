#!/usr/bin/env python3
"""
Passive observe hook — portable observe-loop component.

Fires on: Stop, PostToolUse (Edit|Write).
Appends structured JSONL entries to observe/observe-log.jsonl.

Passive entries are marked decision_grade: false.
Decision-grade signal comes from explicit /friction invocations only.

This hook does NOT depend on almanac being installed — it is a standalone
passive logger for the observe loop.

Path resolution: the log path is derived from THIS script's location
(.claude/hooks/ -> project root), NEVER from the process cwd. A drifted cwd
(e.g. after a `cd` into a subdir in a prior Bash call) must not be able to
misroute the append-only audit trail. Mirrors friction_log.py's project-root
derivation. (2026-07-18: fixed — passive file_write entries had been misrouted
into a subdir's stray observe/observe-log.jsonl when cwd drifted.)
"""
import fcntl
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


def _project_root() -> Path:
    # .claude/hooks/observe.py -> .claude/hooks -> .claude -> project root
    return Path(__file__).resolve().parent.parent.parent


def get_log_path() -> Path:
    return _project_root() / "observe" / "observe-log.jsonl"


def append_entry(entry: dict) -> None:
    log_path = get_log_path()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(entry) + "\n"
    with open(log_path, "a", encoding="utf-8") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            f.write(line)
            f.flush()
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)


def handle_stop(session_id: str, ts: str) -> None:
    append_entry({
        "ts": ts,
        "type": "observe",
        "signal": "session_end",
        "decision_grade": False,
        "dimension": None,
        "step": None,
        "note": None,
        "source": "hook:Stop",
        "session_id": session_id,
    })


def handle_post_tool_use(payload: dict, session_id: str, ts: str) -> None:
    tool_name = payload.get("tool_name", "")
    if tool_name not in ("Edit", "Write"):
        return
    tool_input = payload.get("tool_input", {})
    file_path = tool_input.get("file_path", tool_input.get("path", ""))
    # Render the note as a repo-relative path (relative to project root, NOT
    # cwd) so it stays stable/meaningful regardless of the process cwd.
    rel_path = os.path.relpath(file_path, _project_root()) if file_path else ""
    append_entry({
        "ts": ts,
        "type": "observe",
        "signal": "file_write",
        "decision_grade": False,
        "dimension": None,
        "step": f"tool:{tool_name}",
        "note": f"wrote {rel_path}",
        "source": "hook:PostToolUse",
        "session_id": session_id,
    })


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    event = payload.get("hook_event_name", "")
    session_id = payload.get("session_id", "")
    ts = datetime.now(timezone.utc).isoformat()

    if event == "Stop":
        handle_stop(session_id, ts)
    elif event == "PostToolUse":
        handle_post_tool_use(payload, session_id, ts)


if __name__ == "__main__":
    main()
