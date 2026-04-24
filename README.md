# 🧠 my-second-brain

> Claude Code를 second brain으로 운영하는 워크스페이스 템플릿입니다.

Andrej Karpathy의 **LLM Wiki** 개념을 실무에 적용한 구조예요.
"사람은 업무를 하고, Claude가 기록을 유지한다"는 원칙으로 운영합니다.

---

## 이게 뭔가요?

Obsidian 같은 노트앱과 다릅니다. 내가 직접 찾아보는 게 아니라, **Claude가 알아서 꺼내옵니다.**

- 📓 **weekly log** — 업무 기억을 Claude가 쌓고 요약
- 🔧 **skills** — 반복 작업을 스킬로 만들어 자동 실행
- ⚡ **1회용 코딩** — 그때그때 필요한 스크립트를 같은 공간에서

기록, 자동화, 실행이 모두 한 레포 안에 있습니다.

---

## 빠른 시작

```bash
git clone https://github.com/tiger-dreams/my-second-brain
cd my-second-brain
# Claude Code로 열기
```

1. **`CLAUDE.md`** 를 내 업무 맥락에 맞게 수정하세요 → [수정 가이드](#claudemd-수정-가이드)
2. **첫 weekly log** 파일을 만드세요 → `docs/weekly-logs/weekly_log_YYYY-MM-DD.md`
3. Claude Code를 열고 대화를 시작하세요

---

## 폴더 구조

```
my-second-brain/
├── CLAUDE.md                        # ⭐ Claude에게 나를 설명하는 문서
├── MEMORY.md                        # 메모리 인덱스 (자동 관리)
├── docs/
│   ├── weekly-logs/                 # 주간 업무 로그
│   │   └── weekly_log_YYYY-MM-DD.md
│   └── skills-guide/
│       └── how-to-create-skills.md  # 내 스킬 만드는 법
└── .claude/
    ├── memory/                      # 대화 간 기억 저장소 (자동 관리)
    └── skills/
        ├── anyweb-reader/           # Selenium 기반 웹 리더
        └── pptx/                    # PPTX 생성 스킬
```

---

## CLAUDE.md 수정 가이드

`CLAUDE.md`는 **"새 직원 온보딩 문서"** 라고 생각하세요.
Claude에게 내가 누구인지, 어떤 업무를 하는지, 어떻게 도와주면 되는지 알려주는 파일입니다.

반드시 수정해야 할 항목:

```markdown
## 나에 대해
- 소속: [회사/팀 이름]
- 직무: [역할]
- 주요 업무: [무엇을 주로 하는지]

## 자주 쓰는 도구
- [Jira / Notion / Slack / 사내 Wiki 등]
```

---

## Weekly Log 사용법

파일을 직접 만들 필요 없습니다. Claude에게 말하면 됩니다.

```
"이번 주 로그 만들어줘"
→ Claude가 오늘 날짜 기준으로 weekly_log_2026-04-27.md 자동 생성
```

업무가 생길 때마다 Claude에게 알려주면 로그에 기록해줍니다:

```
"오늘 JIRA-123 처리했어"           → [JIRA-123] 항목 추가
"방금 팀 회의에서 릴리즈 D-7 확정됨" → [MEET] 항목 추가
"이번 주 뭐 했어?"                  → 로그 읽고 요약
"저번 주에 그 이슈 어떻게 됐더라?"    → 이전 주차 로그 거슬러 읽기
```

소스 태그는 나중에 "그게 어디서 나온 얘기야?"를 추적하기 위한 장치입니다:

| 태그 | 의미 |
|------|------|
| `[JIRA-123]` | JIRA 티켓 |
| `[SLACK]` | Slack 메시지 |
| `[MAIL]` | 이메일 |
| `[MEET]` | 회의 |
| `[TODO]` | 내부 작업 |

---

## 무엇이 어디에 쌓이나요?

Claude Code로 이 레포를 열고 대화를 나누면 두 곳에 기억이 쌓입니다.

### 1. Weekly Log — Active (내가 트리거)
```
docs/weekly-logs/weekly_log_2026-04-27.md
```
내가 Claude에게 업무를 말해줄 때 쌓입니다. Claude가 알아서 찾아오지 않습니다.

```
"오늘 이 이슈 처리했어"  →  로그에 기록
"이번 주 뭐 했어?"      →  로그 읽고 요약
```

### 2. Memory — Passive (Claude가 판단)
```
.claude/memory/user_profile.md
.claude/memory/project_xxx.md
```
내가 신경 쓰지 않아도 Claude가 대화 중에 "이건 다음에도 기억해야겠다" 싶으면 알아서 저장합니다. 내 역할, 선호하는 방식, 프로젝트 맥락 같은 것들.

| | Weekly Log | Memory |
|---|---|---|
| 방식 | Active — 내가 말해줘야 쌓임 | Passive — Claude가 알아서 저장 |
| 내용 | 이번 주 한 일 | 나라는 사람에 대한 맥락 |
| 단위 | 주차별 파일 | 주제별 파일 |

> 두 가지 모두 **Claude Code가 켜져 있는 동안**에만 동작합니다.

---

## 포함된 스킬

| 스킬 | 설명 | 쓰는 상황 |
|------|------|-----------|
| `anyweb-reader` | Selenium으로 웹 읽기 | 봇 차단된 페이지, Medium, 네이버 블로그 |
| `pptx` | pptxgenjs로 슬라이드 생성 | "PPTX 만들어줘" |

내 스킬 만드는 법 → [`docs/skills-guide/how-to-create-skills.md`](docs/skills-guide/how-to-create-skills.md)

---

## 사내 MCP가 있다면

회사에서 Slack, Jira, Wiki 등의 MCP를 제공한다면 `.mcp.json`에 추가하세요.
스킬과 MCP를 연결하면 훨씬 강력해집니다.

```json
{
  "mcpServers": {
    "your-company-slack": {
      "type": "stdio",
      "command": "npx",
      "args": ["your-mcp-connector", "https://your-slack-mcp-endpoint"]
    }
  }
}
```

---

## 참고

- [Andrej Karpathy - LLM Wiki (GitHub Gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Claude Code 공식 문서](https://docs.anthropic.com/claude-code)
