# Security Rules

<!-- [Conv #2: regex-blocking PreToolUse rung]
     These constraints are mechanically enforced by .claude/hooks/guard.py
     (the regex-blocking PreToolUse rung of the Guardrails trust ladder). -->

## Secrets and credentials

Never read, write, echo, or log `.env`, `.env.*`, or files under `secrets/`.
Never hardcode API keys, tokens, or passwords in source files.

## Destructive commands

Never run `rm -rf`, `rm -r`, or any recursive delete.
Never run `sudo` or privilege escalation.
Never pipe `curl`/`wget` output directly to `bash` or `sh`.

Mechanically enforced by the PreToolUse guard hook (`.claude/hooks/guard.py`),
which blocks recursive `rm` in any flag spelling, `find ... -delete`, curl/wget
piped or chained into a shell, `sudo`, and `chmod 777`.

## Observe log hygiene

Never modify or delete entries in `observe/observe-log.jsonl` — it is append-only.
Never write fake or backdated friction entries.

Mechanically enforced: the guard hook denies Write/Edit tools on `observe-log.jsonl`.
Appends (`>>`) and the python append-hooks remain allowed.
