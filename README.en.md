# 🧠 my-second-brain

[한국어](README.md) · **English** · [日本語](README.ja.md)

A workspace template for recording work with AI, retrieving useful context, and turning repeated tasks into reusable skills. Open the folder in the Codex app or Code in Claude Desktop.

> The user does the work and makes decisions. AI organizes and maintains the records.

**New here? [Start with one fictional work item](docs/getting-started.en.md).** No external service connection is needed.

## What you can do

- **Record:** keep completed work, decisions, and next actions in weekly logs.
- **Retrieve:** recover context from earlier logs and topic-specific memory.
- **Repeat:** turn recurring tasks into reusable skills.
- **Create:** keep documents, presentations, and scripts in the same workspace. Some tasks require additional tools.

## Get started

```bash
git clone https://github.com/tiger-dreams/my-second-brain.git
cd my-second-brain
```

Use fictional material in this public repository. Keep real work in a separate **private repository**, and check the remote before recording it. A public fork remains public.

1. Open the downloaded folder in the Codex app or Code in Claude Desktop. VS Code and extensions are not required.
2. Ask the agent:

```text
Read AGENTS.md and CLAUDE.md and set this up as my first workspace.
Ask setup questions one at a time. Use English for replies and work logs.
```

3. Answer questions about your role, recurring work, tools, MCP availability, and preferred language. The agent fills in your profile. `[SETUP_REQUIRED]` marks first-time setup.
4. Follow the [getting-started guide](docs/getting-started.en.md) to record a fictional work item.

The agent needs access to read and edit the folder. Follow your tool's instructions for installation, login, plans, and execution permissions. Confirm the target and expected result before deleting, installing, publishing, or sending.

## Rules shared by Codex and Claude

Codex starts with [`AGENTS.md`](AGENTS.md). Claude imports the shared rules through `@AGENTS.md` in [`CLAUDE.md`](CLAUDE.md). Repository instructions also direct Codex to read the profile in `CLAUDE.md`.

| Principle | Behavior |
|---|---|
| Verify the target | Check the checkout path, remote host, owner/repository, and branch before editing. |
| One source for shared rules | Maintain them in `AGENTS.md`; other documents link to them. |
| Main and side chats | Record meaningful work performed in each conversation without a separate logging request. |
| Concise logs | Write the result, remaining action or waiting party, then supporting links. |
| Avoid duplicates | Reread the latest log, update the matching entry, and preserve other chats' records. |
| Verify follow-ups | Check completion and approval evidence before adding work that actually remains. |

These rules apply when the agent reads the instructions and can edit files. If a side chat lacks log access, it reports the unsaved entry. Permission to write a log does not authorize external messages or changes to external tools.

## Where things live

```text
my-second-brain/
├── AGENTS.md                       # Shared operating rules
├── CLAUDE.md                       # Setup, profile, tool-specific guidance
├── MEMORY.md                       # Topic memory index
├── docs/
│   ├── getting-started.md          # Korean guide
│   ├── getting-started.en.md       # English guide
│   ├── getting-started.ja.md       # Japanese guide
│   ├── weekly-logs/                # Weekly logs dated by Monday
│   └── skills-guide/               # Skill authoring and usage guides
├── .agents/skills/                 # Relative symlinks for Codex
└── .claude/
    ├── memory/                     # Lasting preferences and context
    └── skills/                     # Skill source files
```

Work events go in `docs/weekly-logs/weekly_log_YYYY-MM-DD.md`; lasting context goes in `.claude/memory/`. Edit skills in `.claude/skills/`, without creating separate copies for Codex.

## Use weekly logs

Record meaningful work completed in a conversation or reported by the user. Skip simple Q&A and searches with no durable result. Distinguish drafts, sent messages, and pending replies; link lengthy investigations separately.

```text
I finished drafting the notice. It has not been sent and is awaiting review.
Record the completed draft and pending review separately in this week's log.
```

```markdown
- [x] [TODO] Notice draft completed. Awaiting review. [Draft](relative-path)
```

Use source tags `[JIRA-123]`, `[SLACK]`, `[MAIL]`, `[MEET]`, and `[TODO]`, with available identifiers and links. Date the filename by the week's Monday and entries by the actual work date. Carry unfinished items forward while preserving their status.

If the user designates a central log, use it. The agent does not automatically collect work from unconnected services or keep logging after the conversation ends. See the [shared logging policy](AGENTS.md#logging-strategy).

## Included skills

| Skill | Purpose | Starting document |
|---|---|---|
| `anyweb-reader` | Read pages when normal fetching fails | [SKILL.md](.claude/skills/anyweb-reader/SKILL.md) |
| `pptx` | Create, edit, and synchronize PowerPoint sources | [Deck generation guide](.claude/skills/pptx/deck-generation.md) |
| `walkthrough-video` | Produce screen walkthroughs with narration and captions | [Usage guide](docs/skills-guide/walkthrough-video.md) |

Skills do not automatically install their dependencies. Video production requires inputs, screen interactions, and scripts adapted to the service. See [Create your own skill](docs/skills-guide/how-to-create-skills.md) to add a recurring workflow.

## Languages and documentation

READMEs and getting-started guides are available in Korean, English, and Japanese. Choose a preferred reply and logging language during setup; a language explicitly requested for a task takes precedence. Other documents and skills currently use Korean or English.

Keep key guidance aligned across all three languages using the [translation maintenance guide](docs/i18n.md). `AGENTS.md` remains the canonical source for shared operating rules.

## Connect external services

Slack, email, Jira, and calendar access require separately configured MCP connections and permissions in your app. Cloning this repository does not connect accounts. Claude's `.mcp.json` and Codex configuration use different formats; keep credentials local.

## References

- [LLM Wiki — Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Codex instructions](https://developers.openai.com/codex/guides/agents-md) · [Skills](https://developers.openai.com/codex/skills) · [MCP](https://developers.openai.com/codex/mcp)
- [Claude Code documentation](https://code.claude.com/docs/en/overview) · [Code in Claude Desktop](https://code.claude.com/docs/en/desktop-quickstart)
