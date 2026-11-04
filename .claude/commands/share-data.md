---
allowed-tools: Bash, Read
description: Bundle your transcripts, logs, learner profile and lesson files into one archive to send back to Nadav. Shows you everything first. Usage: /share-data
---

Help the learner send their data back. Nothing leaves the machine: you build a local archive and
they send it themselves (DM or email).

1. Run `python3 tools/share_data.py --list` and show the learner the output: every file that would
   be included, grouped, with sizes. Say plainly that the **transcripts contain everything typed in
   these sessions**, so they should exclude any session they'd rather keep private.
2. Ask whether to exclude anything. Exclusions are glob patterns matched against the listed paths,
   for example `--exclude 'transcripts/abc123*'`.
3. Run `python3 tools/share_data.py --build [--exclude …]` and report the archive path it prints.
4. Tell them to send that file to Nadav by DM or email. The archive is git-ignored (`share/`), so
   it cannot be pushed by accident.
