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

## 시작하는 법

### 1. 레포 클론

```bash
git clone https://github.com/tiger-dreams/my-second-brain
```

### 2. VS Code로 열기

터미널보다 VS Code 확장을 추천합니다.
왼쪽 폴더 트리에서 weekly log와 memory 파일이 쌓이는 걸 눈으로 확인할 수 있습니다.

> VS Code → Extensions → "Claude Code" 검색 후 설치

### 3. 아무 말이나 한다

Claude가 `[SETUP_REQUIRED]` 마커를 감지하면 자동으로 인터뷰를 시작합니다.

```
Claude: "안녕하세요! 먼저 몇 가지 여쭤볼게요.
         어떤 팀에서 어떤 일을 하세요?"

나:     "XX팀 PM이고 파트너사 커뮤니케이션 주로 해요"

Claude: "주로 어떤 업무가 반복되나요?"
...
```

4~5개 질문에 답하면 Claude가 CLAUDE.md를 직접 채워줍니다.
**코드를 건드릴 필요 없습니다.**

### 4. 설정 완료

이제 업무 이야기를 나누면 됩니다. 나머지는 Claude가 합니다.

### 5. Permission 모드 설정 (VS Code 기준)

Claude Code는 도구를 실행할 때마다 승인 여부를 물어봅니다.
프롬프트 입력창 하단의 모드 버튼에서 `bypassPermissions`를 선택하면
반복 승인 없이 진행할 수 있습니다.

다만 코딩 작업처럼 소프트웨어 동작이 바뀌는 경우에는 신중하게 판단하세요.
파일 삭제, 패키지 설치, 배포, 권한 변경처럼 영향이 큰 작업은 승인 과정을
남겨두는 편이 안전합니다.

반대로 문서 정리, 회의록 요약, 리서치, weekly log 업데이트처럼
비개발 업무에서는 매번 결과물을 확인하고 승인하는 비용이 꽤 큽니다.
이런 작업은 `bypassPermissions`를 켜두면 흐름이 훨씬 자연스럽습니다.

---

## 폴더 구조

```
my-second-brain/
├── AGENTS.md                        # Codex/에이전트 작업 지침
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

Codex 같은 에이전트가 이 repo에서 작업할 때는 먼저
[`AGENTS.md`](AGENTS.md)를 읽고, Claude Code는 [`CLAUDE.md`](CLAUDE.md)를 따릅니다.

---

## 이런 게 가능합니다

말로 요청하면 Claude가 실행합니다. 코딩 지식 불필요.

**기록**
```
"오늘 파트너사 미팅에서 SDK 도입 검토하기로 했어"
→ 이번 주 weekly log에 [MEET] 항목 자동 추가

"저번 달에 그 이슈 어떻게 처리했더라?"
→ 지난 주차 로그 거슬러 읽고 요약
```

**문서 생성**
```
"다음 주 발표용 PPTX 만들어줘. 내용은 이거야: ..."
→ 슬라이드 파일 생성

"이번 주 한 일 정리해서 주간 보고서 초안 써줘"
→ weekly log 읽고 보고서 초안 작성
```

**정보 수집**
```
"이 Medium 글 읽고 요약해줘" (링크 붙여넣기)
→ 봇 차단 우회하고 내용 읽어서 요약

"이 경쟁사 3곳 비교 분석해줘" (URL 3개 붙여넣기)
→ 각 페이지 읽고 비교표 생성
```

**그때그때 필요한 것**
```
"이 CSV 파일에서 이번 달 수치만 뽑아서 정리해줘"
→ 스크립트 즉석에서 작성 후 실행

"이 내용으로 이메일 초안 3가지 버전 써줘"
→ 바로 작성
```

**사내 MCP 연결 시**
```
"오늘 나 멘션된 Slack 메시지 정리해줘"
→ Slack MCP로 읽어서 요약

"JIRA-123 내용 확인하고 weekly log에 추가해줘"
→ Jira MCP로 읽고 로그 업데이트
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

PPTX를 코드로 생성하고 유지하는 법은
[`deck-generation.md`](.claude/skills/pptx/deck-generation.md)를 참고하세요.

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
