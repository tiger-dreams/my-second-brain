# Start with your own work

[한국어](getting-started.md) · **English** · [日本語](getting-started.ja.md)

Start by recording one work item, without connecting services or installing video tools.

## 1. Prepare a workspace

You need Git and an AI tool that can read and edit a local folder. Use the Codex app or Code in Claude Desktop; VS Code and extensions are not required. Follow the app's instructions for accounts, plans, and installation.

```bash
git clone https://github.com/tiger-dreams/my-second-brain.git
cd my-second-brain
```

Use fictional material in this public repository. For real work, create a separate private repository and verify that the remote points to it. A public fork is also public.

### Codex app

Open the downloaded folder as a project and start a local conversation. Codex reads `AGENTS.md` and follows its instruction to read the profile and workspace guidance in `CLAUDE.md`.

### Code in Claude Desktop

Select the folder as your local Code workspace. `CLAUDE.md` imports shared rules from `AGENTS.md`. Use a Code session that can edit the repository, rather than attaching files to a regular chat.

## 2. Set up your profile

```text
Read AGENTS.md and CLAUDE.md and set this up as my first workspace.
Ask one question at a time and organize my work context from the answers.
Use English for replies and work logs.
```

Describe your team, role, recurring work, tools, and preferred language. A language already specified is not asked again. A company MCP is optional; setup does not automatically connect external accounts.

Skill sources live in `.claude/skills/`; relative symlinks in `.agents/skills/` expose them to Codex. If the list does not refresh, restart the app and check. If your checkout did not preserve symlinks, explicitly ask the agent to read the source:

```text
Read .claude/skills/walkthrough-video/SKILL.md.
First organize the inputs and narration draft needed for the video.
```

The links do not install production tools or voice models, or connect MCP servers.

## 3. Record a fictional work item

```text
This is a fictional exercise.
Today I drafted a customer notice, but it has not been reviewed.
If this week's log is missing, use docs/weekly-logs/weekly_log_YYYY-MM-DD.md
as the template and create a log named for this week's Monday.
Record the completed draft and pending review separately under today's date.
```

Open the file and check the date, completion state, and remaining action. Repeat the same update to check that it does not create duplicates. Routine entries use the result, remaining action or waiting party, and supporting links. Verify existing completion and approval evidence before adding a follow-up.

## 4. Adapt the workflow

- Shared rules and logging criteria: edit `AGENTS.md`; other documents link to it.
- Profile and tool-specific guidance: edit `CLAUDE.md`. Keep format examples in the weekly log template.
- Recurring tasks: see [Create a skill](skills-guide/how-to-create-skills.md).
- Deliverables: start with [PowerPoint generation](../.claude/skills/pptx/deck-generation.md) or [walkthrough videos](skills-guide/walkthrough-video.md).

Before using a skill, check its required inputs and outputs. Presentations and videos require additional libraries or tools. Linked specialist guides currently use Korean or English.

## 5. Connect and share when needed

Slack, email, and calendar access require separately configured MCP connections and permissions. Without those tools, work from the material you provide or local records.

Share generalized skills, guides, and fictional examples rather than private work history. Explain the problem they solve, how to start, and what another user needs to adapt.

[Back to README](../README.en.md)
