# learning-edge

An inquiry-based tutor, mainly for mathematics. You tell it what you want to understand. It
interviews you to find what you already know, then teaches at the edge of it, by having you work
examples and discover the results yourself. It runs inside
[Claude Code](https://claude.com/claude-code).

It ships with one ready-made map, toward the isogeny-based signature scheme SQIsign. For any other
goal it builds the map with you during setup.

**This is an early test release.** Expect rough edges, and please report them.

## Start

```
git clone https://github.com/nkohen/learning-edge-tutor.git && cd learning-edge-tutor
claude
```

Then type `/setup`. Claude checks your install, asks what you want to learn, and interviews you,
which takes about 15 to 30 minutes, longer if your topic needs a new map. After that, type
`/lesson` whenever you want to learn something.

## Sending feedback

Your sessions and logs stay on your machine. When you want to send them back, type `/share-data`.
It shows you exactly what would be included, then builds one archive for you to send to Nadav by
DM or email. You can also type `/friction "what went wrong"` at any moment.

## License

MIT. See [LICENSE](LICENSE).
