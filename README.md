# 🧠 my-second-brain

> AI 에이전트와 함께 업무를 기록하고, 반복하는 방식을 스킬로 정리하는 워크스페이스 템플릿입니다.

**처음 오셨다면 [내 업무로 시작하는 가이드](docs/getting-started.md)부터 읽어보세요.**
외부 서비스 연결 없이 가상 업무 한 건을 기록해볼 수 있습니다. Codex 앱 또는 Claude Desktop의 Code에서 폴더를 열고 시작합니다. VS Code나 확장 설치는 필요하지 않습니다.

이 저장소는 다른 사람의 방식을 배우고, 내 업무에 맞게 바꾸고, 다시 공유하는 출발점입니다. 실제 개인 업무 기록은 자신의 **비공개 저장소**에서 관리하세요. 공개 Fork는 원본처럼 공개되므로, 비공개 업무 공간이 필요하면 별도의 Private 저장소를 만드세요.

Andrej Karpathy의 **LLM Wiki** 개념을 실무에 적용한 구조예요.
"사람은 업무를 하고, AI가 기록을 유지한다"는 원칙으로 운영합니다.

---

## 이게 뭔가요?

업무 기록과 규칙을 파일로 남기고, AI에게 필요한 내용을 찾아 정리하도록 요청하는 구조입니다.

- 📓 **weekly log** — 업무 기억을 AI가 쌓고 요약
- 🔧 **skills** — 반복 작업을 스킬로 만들어 자동 실행
- ⚡ **1회용 코딩** — 그때그때 필요한 스크립트를 같은 공간에서

기록, 자동화, 실행이 모두 한 레포 안에 있습니다.

---

## 시작하는 법

### 1. 레포 클론

```bash
git clone https://github.com/tiger-dreams/my-second-brain
cd my-second-brain
```

### 2. 데스크톱 앱에서 폴더 열기

| 사용하는 앱 | 시작 방법 |
|---|---|
| Codex 앱 | 내려받은 `my-second-brain` 폴더를 프로젝트로 열고 로컬에서 새 대화를 시작합니다. |
| Claude Desktop의 Code | Code에서 로컬 작업 폴더로 `my-second-brain`을 선택하고 대화를 시작합니다. |

AI가 이 폴더의 파일을 읽고 수정할 수 있어야 합니다. 앱 설치·로그인과 이용 가능한 요금제는 각 앱의 안내를 따릅니다.

### 3. 아무 말이나 한다

처음에는 아래처럼 시작하면 됩니다. 사용하는 도구의 파일 접근·지침 자동 로딩 설정에 따라 시작 동작이 다를 수 있습니다.

```text
AGENTS.md와 CLAUDE.md를 읽고, 처음 사용하는 업무 공간으로 설정해줘.
설정 질문은 한 번에 하나씩 해줘.
```

AI는 `[SETUP_REQUIRED]` 마커에 따라 인터뷰를 진행합니다. `CLAUDE.md`라는 파일명은 기존 구조를 유지한 것이며, Codex도 `AGENTS.md`의 지시에 따라 이 파일의 프로필과 업무 규칙을 읽습니다.

```
Claude: "안녕하세요! 먼저 몇 가지 여쭤볼게요.
         어떤 팀에서 어떤 일을 하세요?"

나:     "XX팀 PM이고 파트너사 커뮤니케이션 주로 해요"

Claude: "주로 어떤 업무가 반복되나요?"
...
```

질문에 답하면 AI가 `CLAUDE.md`의 프로필을 채워줍니다.
**코드를 건드릴 필요 없습니다.**

### 4. 설정 완료

이제 업무 이야기를 나누고, 생성한 기록과 결과를 확인합니다. 외부 서비스는 해당 MCP를 연결하기 전까지 자동으로 읽을 수 없습니다.

### 5. 작업 범위와 승인 설정

사용하는 AI 도구에서 접근할 폴더와 실행 권한을 확인하세요.
문서 정리와 로컬 기록부터 시작하고, 삭제·설치·공개·발송은 대상과 결과를 확인한 뒤 실행합니다.
권한 확인을 한꺼번에 생략하는 모드는 시작에 필요하지 않습니다.

---

## 폴더 구조

```
my-second-brain/
├── AGENTS.md                        # Codex/에이전트 작업 지침
├── CLAUDE.md                        # ⭐ Claude에게 나를 설명하는 문서
├── MEMORY.md                        # 메모리 인덱스 (자동 관리)
├── docs/
│   ├── getting-started.md            # 첫 가상 업무 실습
│   ├── weekly-logs/                 # 주간 업무 로그
│   │   └── weekly_log_YYYY-MM-DD.md
│   └── skills-guide/
│       └── how-to-create-skills.md  # 내 스킬 만드는 법
├── .agents/skills/                  # Codex용 스킬 연결 (원본은 아래)
└── .claude/
    ├── memory/                      # 대화 간 기억 저장소 (자동 관리)
    └── skills/
        ├── anyweb-reader/           # Selenium 기반 웹 리더
        ├── pptx/                    # PPTX 생성 스킬
        └── walkthrough-video/       # 화면 시연 + 나레이션 + 자막
```

Codex는 [`AGENTS.md`](AGENTS.md), Claude Code는 [`CLAUDE.md`](CLAUDE.md)에서 시작하며 두 파일은 공통 규칙과 프로필을 연결합니다. 스킬의 원본은 `.claude/skills/`에 있고, `.agents/skills/`에는 같은 스킬을 가리키는 상대 심볼릭 링크가 있어 Codex도 발견할 수 있습니다. 홈 폴더에 별도로 복사할 필요는 없습니다. 자세한 사용법은 [시작 가이드](docs/getting-started.md)를 참고하세요.

---

## 이런 게 가능합니다

다음은 AI에게 요청할 수 있는 예시입니다. 파일을 만드는 작업은 실행 환경과 필요한 도구를 갖춘 뒤 결과를 확인합니다.

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
사용하는 AI에게 내가 누구인지, 어떤 업무를 하는지, 어떻게 도와주면 되는지 알려주는 파일입니다. Codex도 이 프로필을 함께 사용합니다.

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

파일을 직접 만들 필요 없습니다. 사용하는 AI에게 말하면 됩니다.

```
"이번 주 로그 만들어줘"
→ AI가 해당 주 월요일 날짜로 주간 로그 생성
```

업무가 생길 때마다 AI에게 알려주면 로그에 기록해줍니다:

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

이 저장소는 업무 로그와 주제별 메모리를 파일로 관리하도록 안내합니다. 실제 저장은 AI 도구가 지침을 읽고 파일을 수정할 수 있을 때 이루어집니다.

### 1. Weekly Log — Active (내가 트리거)
```
docs/weekly-logs/weekly_log_2026-04-27.md
```
내가 AI에게 업무를 말해줄 때 쌓입니다. 연결하지 않은 외부 서비스에서 업무를 자동으로 가져오지는 않습니다.

```
"오늘 이 이슈 처리했어"  →  로그에 기록
"이번 주 뭐 했어?"      →  로그 읽고 요약
```

### 2. Memory — Passive (Claude가 판단)
```
.claude/memory/user_profile.md
.claude/memory/project_xxx.md
```
이 저장소의 지침에 따라 AI가 역할, 선호하는 방식, 프로젝트 맥락을 주제별 파일로 정리할 수 있습니다. 도구 자체의 메모리 기능과는 별개이므로, 저장된 파일을 직접 확인하세요.

| | Weekly Log | Memory |
|---|---|---|
| 방식 | Active — 내가 알려준 업무를 기록 | Passive — AI가 지침에 따라 정리 |
| 내용 | 이번 주 한 일 | 나라는 사람에 대한 맥락 |
| 단위 | 주차별 파일 | 주제별 파일 |

> 파일은 대화가 끝나도 남습니다. AI가 파일을 읽거나 갱신하는 작업은 해당 폴더에 접근할 수 있는 대화가 실행 중일 때 이루어집니다.

---

## 포함된 스킬

| 스킬 | 설명 | 쓰는 상황 |
|------|------|-----------|
| `anyweb-reader` | Selenium으로 웹 읽기 | 봇 차단된 페이지, Medium, 네이버 블로그 |
| `pptx` | pptxgenjs로 슬라이드 생성 | "PPTX 만들어줘" |
| `walkthrough-video` | 화면 시연·나레이션·자막이 있는 안내 영상 제작 절차 | "릴리즈 안내 영상 만들어줘" |

영상 제작은 [스킬](.claude/skills/walkthrough-video/SKILL.md)과 [사용 가이드](docs/skills-guide/walkthrough-video.md)를 참고하세요. 서비스마다 로그인·화면 동작·안내 내용이 달라, 이 저장소만 내려받아 바로 녹화하는 실행기는 아닙니다. AI와 함께 대상에 맞는 제작 스크립트를 구성합니다.

PPTX를 코드로 생성하고 유지하는 법은
[`deck-generation.md`](.claude/skills/pptx/deck-generation.md)를 참고하세요.

내 스킬 만드는 법 → [`docs/skills-guide/how-to-create-skills.md`](docs/skills-guide/how-to-create-skills.md)

---

## 사내 MCP가 있다면

회사에서 Slack, Jira, Wiki 등의 MCP를 제공한다면 사용하는 앱에 별도로 연결합니다. 이 템플릿을 내려받는 것만으로 계정이나 서버가 연결되지는 않습니다.

- Codex: 앱의 MCP 설정을 사용하거나 `~/.codex/config.toml`에 설정합니다. 신뢰한 프로젝트에서는 `.codex/config.toml`로 범위를 제한할 수도 있습니다.
- Claude Desktop의 Code: Code 세션에서 사용할 수 있는 MCP 연결 방법을 따릅니다. 일반 Chat에 연결한 도구가 Code에도 자동으로 연결된다고 가정하지 않습니다.

아래는 Claude Code용 프로젝트 `.mcp.json`의 구조 예시입니다. Codex 설정 형식과는 다릅니다. 서버 주소·인증 정보는 각자의 로컬 설정으로 관리하세요.

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
- [Claude Desktop의 Code 시작하기](https://code.claude.com/docs/en/desktop-quickstart)
- [Codex 작업 지침](https://developers.openai.com/codex/guides/agents-md)
- [Codex 스킬](https://developers.openai.com/codex/skills)
- [Codex MCP 설정](https://developers.openai.com/codex/mcp)
- [내 업무로 시작하는 가이드](docs/getting-started.md)
- [영상 제작 스킬 사용 가이드](docs/skills-guide/walkthrough-video.md)
