# Claude Code 행동 지침

## 나에 대해

> ✏️ 이 섹션을 본인 정보로 수정하세요.

- 소속: [회사/팀]
- 직무: [역할 — 예: Product Manager, 기획자, 마케터]
- 주요 업무: [예: 서비스 기획, 파트너 커뮤니케이션, 스펙 문서 작성]
- 자주 쓰는 도구: [예: Jira, Confluence, Slack, Google Workspace]

---

## 이 레포의 역할

**LLM Wiki** 패턴 기반의 second brain입니다.
사람은 업무를 하고, Claude가 기록을 유지합니다.

---

## Weekly Log 운영 규칙

- 주간 업무 로그 위치: `docs/weekly-logs/weekly_log_YYYY-MM-DD.md`
- 업무 이벤트 발생 시 즉시 해당 주차 로그 업데이트
- 업무 관련 질문 시 현재 주차 로그 먼저 확인 → 필요 시 이전 주차 거슬러 읽기
- 이전 주 미완료 `[ ]` 항목은 새 주차 파일에 이월

### 소스 태그 규칙

항목 기록 시 반드시 소스 태그를 붙여서 나중에 추적 가능하게 합니다.

| 태그 | 의미 |
|------|------|
| `[JIRA-123]` | JIRA 티켓 번호 |
| `[SLACK]` | Slack 메시지에서 온 정보 |
| `[MAIL]` | 이메일 |
| `[MEET]` | 회의에서 나온 내용 |
| `[TODO]` | 자동 추적 불필요한 내부 작업 |

---

## Available Skills

스킬 실행 전 반드시 해당 `.md` 파일을 읽어 파라미터 형식 확인.

### anyweb-reader
- **트리거**: "이 글 읽어줘", "URL 읽어줘", WebFetch 실패 시 자동 대안
- **위치**: `.claude/skills/anyweb-reader/`
- **설명**: Selenium 기반, 봇 차단 사이트 우회 가능 (Medium, 네이버 블로그 등)
- **스크립트**: `bash $SKILL_DIR/scripts/read-medium.sh "URL"`

### pptx
- **트리거**: "PPTX 만들어줘", "슬라이드 생성해줘", "덱 만들어줘"
- **위치**: `.claude/skills/pptx/`
- **설명**: pptxgenjs 기반 코드로 PPTX 생성, 또는 기존 파일 편집

---

## URL 자동 처리

사용자가 URL만 입력하면:
1. WebFetch로 읽기 시도
2. 실패 시 anyweb-reader 스킬 자동 사용

---

## 1회용 코딩

그때그때 필요한 스크립트는 루트에 바로 만들어도 됩니다.
결과물은 git history에 남아 나중에 참조 가능합니다.

---

## Memory 관리

- 위치: `.claude/memory/`
- 인덱스: `MEMORY.md`
- 대화에서 기억할 내용(선호, 피드백, 프로젝트 컨텍스트)이 생기면 즉시 저장

---

## 새 스킬 추가하기

반복되는 작업이 생기면 스킬로 만드세요.
가이드: `docs/skills-guide/how-to-create-skills.md`
