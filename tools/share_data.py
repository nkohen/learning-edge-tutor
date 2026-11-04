#!/usr/bin/env python3
"""Bundle a learner's data from this project into one zip to send back by hand.

  python3 tools/share_data.py --list [--exclude GLOB ...]
  python3 tools/share_data.py --build [--exclude GLOB ...]

Collects:
  observe/*.jsonl            hook logs (friction, usage, tool outcomes, feedback)
  learners/*.md              the learner profile(s), minus TEMPLATE.md
  lessons/**                 lesson logs, question stacks, prep
  territories/*.md           territory maps built here (not the shipped ones)
  transcripts/**             Claude Code's transcripts for THIS project directory
                             (from ~/.claude/projects/, incl. subagent transcripts)

Writes share/learning-edge-data-<date>.zip. Nothing is sent anywhere. Stdlib only.
"""
import argparse
import datetime
import fnmatch
import json
import os
import re
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def claude_projects_dir() -> Path:
    base = os.environ.get("CLAUDE_CONFIG_DIR")
    return (Path(base) if base else Path.home() / ".claude") / "projects"


def _cwd_of(jsonl: Path):
    try:
        with jsonl.open(encoding="utf-8", errors="replace") as fh:
            for _, line in zip(range(50), fh):
                try:
                    cwd = json.loads(line).get("cwd")
                except (ValueError, AttributeError):
                    continue
                if cwd:
                    return cwd
    except OSError:
        pass
    return None


def transcript_files():
    """(archive_path, source_path) for every transcript belonging to ROOT."""
    projects = claude_projects_dir()
    if not projects.is_dir():
        return []
    root = str(ROOT)
    dirs = []
    guess = projects / re.sub(r"[^A-Za-z0-9]", "-", root)
    if guess.is_dir():
        dirs.append(guess)
    else:  # naming scheme changed or path normalized differently: match on recorded cwd
        for d in projects.iterdir():
            if d.is_dir() and any(_cwd_of(f) == root for f in d.glob("*.jsonl")):
                dirs.append(d)
    out = []
    for d in dirs:
        for f in sorted(d.rglob("*.jsonl")):
            out.append(("transcripts/" + f.relative_to(d).as_posix(), f))
    return out


def collect():
    items = []
    for f in sorted((ROOT / "observe").glob("*.jsonl")):
        items.append(("observe/" + f.name, f))
    for f in sorted((ROOT / "learners").glob("*.md")):
        if f.name != "TEMPLATE.md":
            items.append(("learners/" + f.name, f))
    lessons = ROOT / "lessons"
    if lessons.is_dir():
        for f in sorted(p for p in lessons.rglob("*") if p.is_file()):
            items.append(("lessons/" + f.relative_to(lessons).as_posix(), f))
    territories = ROOT / "territories"
    if territories.is_dir():
        try:
            shipped = set(subprocess.run(["git", "-C", str(ROOT), "ls-files", "territories"],
                                         capture_output=True, text=True, check=True).stdout.split())
        except (OSError, subprocess.CalledProcessError):
            shipped = set()
        for f in sorted(territories.glob("*.md")):
            if "territories/" + f.name not in shipped:
                items.append(("territories/" + f.name, f))
    items.extend(transcript_files())
    return items


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list", action="store_true", help="show what would be included")
    mode.add_argument("--build", action="store_true", help="write the zip")
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                    help="leave out archive paths matching GLOB (repeatable)")
    args = ap.parse_args()

    items = [(a, s) for a, s in collect()
             if not any(fnmatch.fnmatch(a, g) for g in args.exclude)]
    if not items:
        print("Nothing to share yet.")
        return 0

    if args.list:
        group = None
        total = 0
        for arc, src in items:
            g = arc.split("/", 1)[0]
            if g != group:
                group = g
                print(f"\n{g}/")
            size = src.stat().st_size
            total += size
            print(f"  {human(size):>9}  {arc}")
        print(f"\n{len(items)} files, {human(total)} total")
        if not any(a.startswith("transcripts/") for a, _ in items):
            print(f"(no transcripts found under {claude_projects_dir()} for {ROOT})")
        return 0

    out_dir = ROOT / "share"
    out_dir.mkdir(exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = out_dir / f"learning-edge-data-{stamp}.zip"
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for arc, src in items:
            zf.write(src, arc)
    print(f"{out}  ({len(items)} files, {human(out.stat().st_size)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
