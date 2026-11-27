# 🧠 my-second-brain

**한국어** · [English](README.en.md) · [日本語](README.ja.md)

AI와 함께 업무를 기록하고, 필요한 맥락을 다시 찾고, 반복 업무를 스킬로 정리하는 워크스페이스 템플릿입니다. Codex 앱이나 Claude Desktop의 Code에서 폴더를 열어 사용합니다.

> 사람은 업무를 수행하고 판단하며, AI는 기록을 정리하고 유지합니다.

**처음이라면 [내 업무로 시작하기](docs/getting-started.md)에서 가상 업무 한 건을 기록해보세요.** 외부 서비스 연결 없이 시작할 수 있습니다.

## 할 수 있는 일

- **기록하기:** 완료한 작업·결정·후속 행동을 주간 로그에 남깁니다.
- **다시 찾기:** 지난 로그와 주제별 메모리에서 업무 맥락을 찾아 정리합니다.
- **반복하기:** 자주 하는 작업을 스킬로 정리해 재사용합니다.
- **만들기:** 문서·발표자료·스크립트 등 필요한 결과물을 같은 공간에서 만듭니다. 작업에 따라 추가 도구가 필요합니다.

## 시작하기

```bash
git clone https://github.com/tiger-dreams/my-second-brain.git
cd my-second-brain
```

이 공개 저장소에서는 가상 자료로 실습하세요. 실제 업무 기록은 별도 **비공개 저장소**에서 관리하고, 기록 전에 원격 주소를 확인하세요. 공개 Fork는 공개 상태를 유지합니다.

1. Codex 앱 또는 Claude Desktop의 Code에서 내려받은 폴더를 엽니다. VS Code나 확장 설치는 필요하지 않습니다.
2. AI에게 아래처럼 요청합니다.

```text
AGENTS.md와 CLAUDE.md를 읽고 처음 사용하는 업무 공간으로 설정해줘.
설정 질문은 한 번에 하나씩 해줘. 답변과 업무 기록은 한국어로 작성해줘.
```

3. 역할·반복 업무·사용 도구·MCP 유무·사용 언어에 답하면 AI가 프로필을 정리합니다. `[SETUP_REQUIRED]`는 초기 설정을 위한 표시입니다.
4. [시작 가이드](docs/getting-started.md)의 가상 업무로 로그를 확인합니다.

AI가 이 폴더를 읽고 수정할 수 있어야 합니다. 앱 설치·로그인·요금제와 실행 권한은 사용하는 도구의 안내를 따릅니다. 삭제·설치·공개·발송은 대상과 결과를 확인한 뒤 실행합니다.

## Codex와 Claude가 공유하는 규칙

Codex는 [`AGENTS.md`](AGENTS.md)에서 시작하고, Claude는 [`CLAUDE.md`](CLAUDE.md)의 `@AGENTS.md`로 공통 지침을 불러옵니다. Codex도 저장소 지침에 따라 `CLAUDE.md`의 프로필을 읽습니다.

| 기준 | 동작 |
|---|---|
| 대상 확인 | 파일 수정 전 저장소 경로·원격 호스트·소유자/저장소·브랜치를 확인합니다. |
| 공통 규칙 | `AGENTS.md`에서 관리하고 다른 문서는 참조합니다. |
| 메인·서브 채팅 | 각 대화에서 수행한 의미 있는 작업을 별도 기록 요청 없이 로그에 남깁니다. |
| 간결한 로그 | 결과 → 남은 행동·대기 상대 → 근거 링크 순서로 작성합니다. |
| 중복 방지 | 최신 로그를 읽고 같은 항목을 보완하며 다른 대화의 기록을 보존합니다. |
| 후속 업무 | 기존 완료·승인 근거부터 확인하고 실제로 남은 일만 추가합니다. |

이 규칙은 AI가 지침을 읽고 파일을 수정할 때 적용됩니다. 서브 채팅에서 로그 수정 권한이 없으면 저장하지 못한 내용을 알립니다. 로그 작성 권한이 메시지 발송이나 외부 도구 변경 권한을 부여하지는 않습니다.

## 무엇을 어디에 남기나요?

```text
my-second-brain/
├── AGENTS.md                       # 두 도구의 공통 운영 규칙
├── CLAUDE.md                       # 초기 설정·프로필·도구별 안내
├── MEMORY.md                       # 주제별 메모리 인덱스
├── docs/
│   ├── getting-started.md          # 한국어 시작 가이드
│   ├── getting-started.en.md       # 영어 시작 가이드
│   ├── getting-started.ja.md       # 일본어 시작 가이드
│   ├── weekly-logs/                # 월요일 날짜 기준 주간 로그
│   └── skills-guide/               # 스킬 제작·사용 가이드
├── .agents/skills/                 # Codex용 상대 심볼릭 링크
└── .claude/
    ├── memory/                     # 오래 유지할 선호·업무 맥락
    └── skills/                     # 스킬 원본
```

업무 사건은 `docs/weekly-logs/weekly_log_YYYY-MM-DD.md`, 장기 맥락은 `.claude/memory/`에 정리합니다. 스킬은 `.claude/skills/`에서 수정하며, Codex용 링크에 복사본을 만들지 않습니다.

## Weekly log 사용하기

대화 중 의미 있는 작업이 완료되거나 사용자가 수행 사실을 알려주면 기록합니다. 단순 질의응답과 결과가 남지 않은 탐색은 제외합니다. 초안 작성·실제 발송·회신 대기를 구분하고, 긴 조사 과정은 별도 자료에 연결합니다.

```text
오늘 안내문 초안을 작성했어. 아직 발송하지 않았고 검토를 기다리고 있어.
이번 주 로그에 초안 작성 완료와 검토 대기를 구분해서 기록해줘.
```

```markdown
- [x] [TODO] 안내문 초안 작성 완료. 검토 대기. [초안](상대경로)
```

소스 태그는 `[JIRA-123]`, `[SLACK]`, `[MAIL]`, `[MEET]`, `[TODO]`를 사용하고, 확인 가능한 식별자와 링크를 함께 남깁니다. 파일명은 해당 주 월요일 날짜를 쓰며, 기록에는 실제 작업 날짜를 씁니다. 이전 주 미완료 항목은 상태를 보존해 이월합니다.

사용자가 지정한 중앙 로그가 있으면 그곳에 기록합니다. AI가 연결하지 않은 외부 서비스의 업무를 자동 수집하거나 대화 종료 후 계속 기록하지는 않습니다. 상세 기준은 [공통 로그 지침](AGENTS.md#logging-strategy)을 참고하세요.

## 포함된 스킬

| 스킬 | 용도 | 시작 문서 |
|---|---|---|
| `anyweb-reader` | 일반 조회가 실패한 웹페이지 읽기 | [SKILL.md](.claude/skills/anyweb-reader/SKILL.md) |
| `pptx` | PowerPoint 생성·편집·원본 동기화 | [덱 제작 가이드](.claude/skills/pptx/deck-generation.md) |
| `walkthrough-video` | 화면 시연·나레이션·자막 영상 제작 | [사용 가이드](docs/skills-guide/walkthrough-video.md) |

스킬은 필요한 도구를 자동으로 설치하지 않습니다. 영상은 대상 서비스에 맞게 입력·화면 동작·제작 스크립트를 구성합니다. [내 스킬 만들기](docs/skills-guide/how-to-create-skills.md)에서 반복 업무를 추가할 수 있습니다.

## 언어와 문서 관리

한국어·영어·일본어 README와 시작 가이드를 제공합니다. 설정 시 선호하는 답변·기록 언어를 선택할 수 있으며, 개별 요청에서 언어를 지정하면 그 요청을 따릅니다. 그 밖의 문서와 스킬은 현재 한국어 또는 영어로 제공됩니다.

문서를 갱신할 때는 [다국어 문서 관리 기준](docs/i18n.md)에 따라 세 언어의 핵심 안내를 함께 맞춥니다. 공통 운영 규칙의 정본은 언어별 README가 아닌 `AGENTS.md`입니다.

## 외부 서비스 연결

Slack·메일·Jira·캘린더를 읽으려면 각 앱에서 사용할 수 있는 MCP와 권한을 별도로 연결합니다. 이 저장소만 내려받아 계정이 연결되지는 않습니다. Claude의 `.mcp.json`과 Codex의 설정 형식은 다르며, 인증 정보는 로컬에 보관합니다.

## 참고

- [LLM Wiki 원문 — Andrej Karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Codex 작업 지침](https://developers.openai.com/codex/guides/agents-md) · [스킬](https://developers.openai.com/codex/skills) · [MCP](https://developers.openai.com/codex/mcp)
- [Claude Code 문서](https://code.claude.com/docs/en/overview) · [Desktop의 Code 시작하기](https://code.claude.com/docs/en/desktop-quickstart)
