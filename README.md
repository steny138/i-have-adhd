<p align="center">
  <img src="./logo.png" alt="i-have-adhd" width="140" />
</p>
<p align="center">
  <strong align="center">ADHD-friendly outputs. No ADHD diagnosis needed!</strong>
</p>
<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/ayghri/i-have-adhd?style=flat" alt="License"></a>
</p>

<p align="center">
  <strong title="English" aria-label="English">🇬🇧</strong> ·
  <a href=".github/readme/README.zh-CN.md" title="简体中文" aria-label="简体中文">🇨🇳</a> ·
  <a href=".github/readme/README.pt-BR.md" title="Português (Brasil)" aria-label="Português (Brasil)">🇧🇷</a> ·
  <a href=".github/readme/README.ja.md" title="日本語" aria-label="日本語">🇯🇵</a> ·
  <a href=".github/readme/README.vi.md" title="Tiếng Việt" aria-label="Tiếng Việt">🇻🇳</a> ·
  <a href=".github/readme/README.ko.md" title="한국어" aria-label="한국어">🇰🇷</a>
</p>


## Install

Copy/paste into your CLI prompt:

```text
Install the i-have-adhd skill/plugin from https://github.com/steny138/i-have-adhd, refer to the repo's AGENTS.md for instructions.
```

Or 🔗 [check the installation instructions](INSTALL.md).

## What it does

A skill for your coding assistant that surfaces the verified outcome, decision, or next action without hiding evidence or safety constraints. No "Hope this helps!"


## What changes


<table>
<tr>
<td width="50%">

## Before

> Great question! Let me think about this. Your auth flow has a few moving pieces: the middleware, the token verification, and the cookie handling. Looking at `src/auth.ts`, the `verifyToken` function (around lines 42-58) seems to be using an older `jsonwebtoken` API. One approach would be to update the package and rewrite that function. After making the change, you'd want to run the auth tests to confirm nothing breaks. By the way, you might also want to look at your dependency versions overall. Hope this helps! Let me know if you want to dig deeper.

</td>

<td width="50%">

## After

> The auth failure is in `src/auth.ts:42`: `verifyToken` uses an older `jsonwebtoken` API. No change has been made yet.
>
> - Evidence: token verification fails at that call site.
> - Risk: the compatible target version is not yet verified.
>
> Next: confirm the supported `jsonwebtoken` version before updating the dependency and running `npm test -- auth.spec.ts`.

</td>
</tr>
</table>


## The rules

10 rules. Full text in [SKILL.md](./skills/i-have-adhd/SKILL.md).

1. Put the verified outcome, decision, or next action first.
2. Layer supporting evidence, unknowns, risks, and validation.
3. Number only ordered action sequences.
4. Keep material information complete and verify summary counts.
5. Restore state only when useful; omit next when nothing remains.
6. Estimate only from reliable evidence when timing matters.
7. Make completion and verification visible.
8. Report errors plainly and separate proven from unproven causes.
9. Control tangents without hiding material side issues.
10. Remove filler and end when the answer is complete.

## Tune it

Fork, edit `skills/i-have-adhd/SKILL.md`, then swap your copy in:

```bash
claude plugin uninstall i-have-adhd            # drop the upstream copy first:
claude plugin marketplace remove i-have-adhd   # fork and upstream share both names
claude plugin marketplace add <your-username>/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

Restart Claude Code, then re-invoke `/i-have-adhd`.

## Credits

Loosely based on *The Adult ADHD Tool Kit* by J. Russell Ramsay and Anthony L. Rostain. Adapted for how an LLM should respond, not how a human should organize their day.

## License

MIT.

Star ⭐ if it saved you one scroll past one "Great question!"
