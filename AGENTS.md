# Agent Instructions

This repository is a second-brain workspace template for Claude Code and other coding agents.

The main principle is simple:

> The user does the work. The agent keeps the memory, structure, and repeatable tools alive.

---

## Repository Role

This repo is not only a code repo. It is a working memory system.

- `CLAUDE.md`: how the agent should work with the user
- `MEMORY.md`: index of longer-term memory files
- `.claude/memory/`: persistent context and preferences
- `docs/weekly-logs/`: weekly work logs and accumulated wiki
- `.claude/skills/`: reusable workflows for repeated tasks

Keep these roles clear. Do not turn every task into code if a note, log, or skill update is the better artifact.

---

## First-Time Setup

If `CLAUDE.md` still contains `[SETUP_REQUIRED]`, handle setup before doing other work.

Ask the setup questions one at a time, then update:

1. `CLAUDE.md`
2. `MEMORY.md`
3. relevant `.claude/memory/` files if needed
4. today's weekly log, if the user asks to start logging work

Do not remove the setup marker until the user profile sections have been filled.

---

## Privacy And Safety

This workspace may contain meeting notes, business context, personal preferences, and internal work history.

- Prefer Private repositories for real workspaces.
- Do not paste secrets, tokens, private URLs, customer data, or internal documents into public outputs.
- If a task may expose private information, pause and ask before publishing, pushing, or sharing.
- Treat screenshots and exported files as potentially sensitive.

Permission bypass modes can be useful for non-development work such as summaries, document cleanup, research, and weekly log updates. For software-changing tasks such as deleting files, installing packages, changing permissions, or deploying, be more conservative and keep approval steps where appropriate.

---

## Web Fetching Strategy

When the user provides a URL directly:

1. First try the normal WebFetch/browser fetch available in the current agent environment.
2. If it fails because of a block, timeout, login wall, or incomplete content, use the repo's `anyweb-reader` skill or another available browser automation fallback.
3. If the fetch method matters for later reproducibility, record which method was used in the relevant log.

Do not spend heavy browser automation credits when a normal fetch is enough.

---

## Logging Strategy

Use Korean by default, matching the repository's existing documentation style.

Use `docs/weekly-logs/` for work memory that should become part of the user's second brain.

Log when:

- the user explicitly asks to log something
- important work is completed
- a decision or insight should be remembered
- a repeatable workflow or skill is created
- a debugging or problem-solving journey may be useful later

Recommended weekly log entry shape:

```markdown
### [Topic]
- **배경**: why this mattered
- **진행 과정**:
  - what was tried
  - what failed or changed
  - what finally worked
- **결과**: what changed
- **인사이트**: what should be remembered
```

For technical agent-work logs that are not part of weekly business memory, a `logs/YYYY/MM-month.md` structure is also acceptable if the workspace already uses it.

Never overwrite existing logs. Append and preserve history.

---

## Skill Usage

Before using a skill, read its `SKILL.md` or guide file enough to follow the expected workflow.

Available bundled skills in this template include:

- `anyweb-reader`: use when normal fetch cannot read an article or page
- `pptx`: use for PowerPoint creation, editing, reverse-sync, and generated deck maintenance

For PPTX generation, start with:

```text
.claude/skills/pptx/deck-generation.md
```

Use `pptxgenjs.md` for API details and `editing.md` when modifying an existing template.

---

## Generated Files And Assets

Keep generated work reproducible.

- Store deck/image/document assets in a local `assets/` folder near the generator.
- Use relative paths from the script location.
- Do not depend on `/Users/<name>/...` absolute paths.
- If a PPTX or document was edited manually, reverse-sync important changes back to the source script or notes.
- Keep source scripts, generated outputs, and assets together when handing off.

---

## Editing Rules

- Prefer small, focused changes.
- Preserve existing user-written notes and logs.
- Do not delete or rewrite memory unless the user explicitly asks.
- Do not commit secrets, local credentials, generated tokens, or private exports.
- When editing Markdown, keep headings and tables readable in plain text.
- When creating reusable instructions, avoid hardcoding one person's company, path, or tool setup unless the file is explicitly personal.

---

## Git Practices

Before committing:

1. Check `git status`.
2. Review the diff.
3. Stage only relevant files.
4. Use a concise commit message that describes the user-visible change.

Do not rewrite history or discard user changes unless explicitly asked.

For template repositories, prefer documentation and examples that work for a new user on a different machine.

---

## Blog Or Public Drafts

When drafting public-facing posts:

- Write in Korean unless the user asks otherwise.
- Do not insert local image paths as Markdown images.
- Use placeholders such as:

```markdown
**[사진: filename - what this image should show]**
```

This makes it easier for the user to add images manually in the final publishing platform.
