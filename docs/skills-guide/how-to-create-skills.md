# 나만의 스킬 만드는 법

Claude Code에서 반복되는 작업이 생기면 스킬로 만드세요.
한 번 만들면 자연어로 "~해줘" 라고만 해도 자동 실행됩니다.

---

## 스킬의 구조

```
.claude/skills/
└── my-skill/
    ├── SKILL.md        # 스킬 설명 + 트리거 키워드
    └── scripts/
        ├── common.sh   # 공통 함수 (환경변수 로딩 등)
        └── run.sh      # 실제 실행 스크립트
```

---

## Step 1: SKILL.md 작성

Claude가 이 파일을 읽고 언제 스킬을 실행할지 판단합니다.

```markdown
# 스킬 이름

한 줄 설명

## Trigger Keywords
- "이렇게 말하면 실행"
- "이런 요청이 오면 실행"

## Usage
스킬이 하는 일 설명

## Script
\`\`\`bash
bash $SKILL_DIR/scripts/run.sh "파라미터"
\`\`\`

## Parameters
- **PARAM** (필수): 설명
```

---

## Step 2: scripts/common.sh 작성

환경변수, 공통 함수를 여기에 정의합니다.

```bash
#!/bin/bash

# 환경변수 로딩
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/../../../../.env"

if [ -f "$ENV_FILE" ]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
fi

# 공통 로그 함수
log_info()  { echo -e "\033[0;32m[INFO]\033[0m $1"; }
log_error() { echo -e "\033[0;31m[ERROR]\033[0m $1"; }
```

---

## Step 3: scripts/run.sh 작성

실제 작업을 수행하는 스크립트입니다.

```bash
#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

PARAM="$1"

if [ -z "$PARAM" ]; then
  log_error "파라미터가 필요합니다"
  exit 1
fi

log_info "실행 중: $PARAM"
# 여기에 실제 로직 작성
```

---

## Step 4: CLAUDE.md에 등록

`CLAUDE.md`의 `Available Skills` 섹션에 추가합니다:

```markdown
### my-skill
- **트리거**: "이렇게 말하면"
- **위치**: `.claude/skills/my-skill/`
- **스크립트**: `bash $SKILL_DIR/scripts/run.sh "파라미터"`
```

---

## 실전 예시: 날씨 스킬

```
.claude/skills/weather/
├── SKILL.md
└── scripts/
    └── get.sh
```

**SKILL.md:**
```markdown
# weather

현재 날씨를 조회합니다.

## Trigger Keywords
- "날씨 알려줘"
- "오늘 날씨"

## Script
\`\`\`bash
bash $SKILL_DIR/scripts/get.sh "서울"
\`\`\`
```

**scripts/get.sh:**
```bash
#!/bin/bash
CITY="${1:-서울}"
curl -s "wttr.in/${CITY}?format=3"
```

---

## 사내 MCP가 있다면?

스킬 안에서 MCP 도구를 직접 호출할 수 없지만,
MCP와 스킬을 조합해서 쓸 수 있습니다:

1. 스킬이 데이터를 수집/가공
2. Claude가 MCP 도구로 결과를 전달

예: "이번 주 작업 내용을 Confluence에 올려줘"
→ weekly log 스킬로 내용 정리 → Wiki MCP로 업로드

---

## 팁

- 스킬 이름은 짧고 동사형으로: `fetch`, `create`, `search`
- 스크립트는 단독 실행 가능하게 만들기 (테스트 편의)
- 에러 메시지를 명확하게 — Claude가 에러를 보고 다음 행동을 판단함
- 필요한 환경변수는 `.env` 파일에 모아두기
