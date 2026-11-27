# Agent Instructions

This repository is a second-brain workspace template for the Codex app and Claude Code, including Code in Claude Desktop. VS Code is not required.

The main principle is simple:

> The user does the work. The agent keeps the memory, structure, and repeatable tools alive.

---

## Repository Role

This repo is not only a code repo. It is a working memory system.

- `CLAUDE.md`: how the agent should work with the user
- `AGENTS.md`: shared operating rules for Codex and Claude
- `MEMORY.md`: index of longer-term memory files
- `.claude/memory/`: persistent context and preferences
- `docs/weekly-logs/`: weekly work logs and accumulated wiki
- `.claude/skills/`: reusable workflows for repeated tasks

Keep these roles clear. Do not turn every task into code if a note, log, or skill update is the better artifact.

At the start of a task, also read `CLAUDE.md` for the shared user profile and workspace rules. Its filename is historical; the profile applies when using Codex as well. This is a repository convention, not a claim that Codex loads `CLAUDE.md` automatically. Claude Code imports this file through `CLAUDE.md`; do not recursively reload files already read.

### Shared Rule Ownership

Keep shared operating rules in `AGENTS.md`; keep setup, the user profile, and tool-specific instructions in `CLAUDE.md`. If a topic needs a separate guide, name that guide as the canonical source and link to it. Update the canonical rule and its references instead of maintaining separate copies for each tool. When existing instructions conflict and the intended rule is unclear, identify the conflict rather than silently choosing one.

### Confirm The Repository Before Editing

Before changing repository files, verify the checkout root, remote host, owner/repository, current branch, and existing changes. Match them against the user's requested target; a similar folder or repository name is insufficient. Briefly identify the target in the first progress update once verified. For a local folder without Git, state the folder and that it has no Git remote.

Repeat the check when switching repositories and before committing or pushing. Do not infer that GitHub and an internal Git host contain the same repository. Ask only when the available evidence cannot resolve the target. After pushing, compare the intended remote branch SHA with local HEAD before reporting remote completion.

---

## First-Time Setup

Distinguish using this template from maintaining it. When the user asks to review or update the public template, preserve `[SETUP_REQUIRED]` and the profile placeholders; do not run a personal setup interview or insert the maintainer's work history. The setup below applies when someone starts using their own workspace.

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

Use the tool’s normal file-access and execution approval settings. A permission bypass mode is not required to use this template. Confirm the target and expected result before deleting files, installing tools, publishing, sending messages, or deploying.

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

This section is the shared logging policy for Codex and Claude. Keep logging rules here; `CLAUDE.md` imports this file and links to this section.

Log when:

- the user explicitly asks to log something
- important work is completed
- a decision or insight should be remembered
- a repeatable workflow or skill is created
- a debugging or problem-solving journey may be useful later

Do not log simple Q&A, routine searches with no durable finding, hypothetical examples, or secrets. Respect an explicit request not to record something. When maintaining this public template, keep actual work history in the maintainer's private work log rather than adding it to the template.

### Main And Side Conversations

- Apply the same logging threshold to main and side conversations. These workspace instructions explicitly authorize ongoing weekly log updates for meaningful work performed in each conversation; do not ask for a separate logging request or renewed approval each time.
- Weekly log updates are an authorized exception to a side conversation's general restriction on file changes, subject to the tool's actual permissions and higher-priority instructions. This exception does not authorize edits to other files, external messages or Wiki updates, or execution or completion of the parent conversation's work.
- Record only work performed in the current conversation, including a user's report of completed work clearly attributed to the user. Inherited parent history alone is not a newly completed task.
- Reread the latest weekly log immediately before editing. Update the matching entry for the same work; preserve other conversations' entries and unfinished states. If the file changes before saving, reread it and reapply only the intended edit.
- Distinguish verified facts, user-provided information, proposals, and unresolved questions. Preparing a draft does not mean it was sent. Keep unfinished follow-ups separate from completed work; do not infer owners, deadlines, or agreements.
- If the log cannot be updated because of access or tool restrictions, report the pending entry and reason. Do not claim that it was saved.

### Weekly Log Operation

- Use `docs/weekly-logs/weekly_log_YYYY-MM-DD.md`, with the Monday of the relevant week in the filename and the actual work date inside. Use the configured central workspace if the user has designated one; do not create competing logs in each project.
- When the week's file is missing, create it using the repository's weekly log template. Carry over unresolved `[ ]` items from the previous week and preserve their status.
- For work-related questions, read the current weekly log first, then earlier weeks as needed.
- Mark completed work with `[x]` and unfinished work with `[ ]`. Include the result, a relevant source or artifact link, and any next action needed. Keep routine entries concise; use the expanded shape below when the background or investigation will be useful later.
- Write routine entries in this order: result, remaining action or waiting party when applicable, then source or artifact link. Keep them to one to three sentences. Store lengthy research, commands, and revision history in a linked supporting document; include a caveat in the log when it changes the reader's decision.
- Add source tags: `[JIRA-123]` for a Jira issue, `[SLACK]` for Slack, `[MAIL]` for email, `[MEET]` for a meeting, and `[TODO]` for internal work. Keep identifiers and links when available, subject to the workspace's privacy rules.

Expanded weekly log entry shape:

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

Preserve existing log history. Append new work and make focused updates to matching entries rather than replacing the whole log.

### Check Whether Follow-Up Work Remains

Before adding a follow-up or asking for another approval, check the current source, completion evidence, and any approval already given for the same action and target. Generic checklist wording, an old reminder, or an unverified possibility alone does not establish a new task. Do not reopen completed work without evidence that something remains.

Record an actual remaining action separately from a proposal or unresolved question. Preserve any confirmed owner, deadline, and waiting party; do not invent them. If evidence is unavailable, state what remains unknown rather than presenting the work as required or complete. Continue actions already authorized within their scope.

## Memory Management

Use `MEMORY.md` as the index for reusable context in `.claude/memory/`. Both Codex and Claude use these repository files. Keep lasting preferences, feedback, and project context here, and dated work events in the weekly log. Follow the user's explicit memory permissions and preserve existing entries. Do not copy the same operating rule into memory and multiple instruction files; link to its canonical location.

---

## Skill Usage

Before using a skill, read its `SKILL.md` or guide file enough to follow the expected workflow.

Skill sources live in `.claude/skills/`. Repository-local relative symlinks under `.agents/skills/` expose the same folders to Codex. Edit the source files rather than creating a second copy. If a checkout did not preserve symlinks, read the source `SKILL.md` explicitly and explain that automatic discovery has not been verified.

Available bundled skills in this template include:

- `anyweb-reader`: use when normal fetch cannot read an article or page
- `pptx`: use for PowerPoint creation, editing, reverse-sync, and generated deck maintenance
- `walkthrough-video`: create a narrated, subtitled walkthrough of a web service; read `.claude/skills/walkthrough-video/SKILL.md` first. This is a reusable production recipe, not a bundled one-command recorder.

For a new repeatable workflow, see `docs/skills-guide/how-to-create-skills.md`.

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
- One-off scripts may live at the repository root; keep reusable tools and their supporting files together when they grow.
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
