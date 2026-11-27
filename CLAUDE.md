# Claude Code 행동 지침

@AGENTS.md

Codex와 Claude의 공통 운영 규칙은 `AGENTS.md`가 정본입니다. 이 파일에서는 초기 설정·사용자 프로필·도구별 안내를 관리하며, 공통 규칙은 아래 링크를 따라 수정합니다.

## [SETUP_REQUIRED]

공개 템플릿 자체의 검토·유지보수 요청이라면 인터뷰를 실행하지 않고 이 마커와 프로필 예시를 유지합니다. 아래 절차는 사용자가 자신의 업무 공간으로 사용하기 시작할 때 적용합니다.

이 마커가 보이면 사용자가 처음 대화를 시작한 것입니다.
**다른 어떤 작업보다 먼저** 아래 인터뷰를 진행하세요.

### 인터뷰 진행 방법

사용자에게 다음 질문을 순서대로 하나씩 물어보세요.
한꺼번에 묻지 말고, 답변을 받으면 다음 질문으로 넘어가세요.

1. "안녕하세요! 먼저 몇 가지 여쭤볼게요. 어떤 팀에서 어떤 일을 하세요?"
2. "주로 어떤 업무가 반복되나요? (회의록 작성, 문서 정리, 보고서 등)"
3. "매일 쓰는 도구가 뭔가요? (Jira, Notion, Slack, 사내 Wiki 등)"
4. "회사에서 MCP(AI 연동 도구)를 제공하고 있나요?"
5. "답변과 업무 기록에는 어떤 언어를 사용할까요?"

질문은 `AGENTS.md`의 언어 기준에 맞춰 번역합니다. 사용자가 이미 답변·기록 언어를 명시했다면 5번은 다시 묻지 않고 해당 설정을 반영합니다.

인터뷰가 끝나면:
1. 답변을 바탕으로 아래 `## 나에 대해` 섹션을 채워주세요
2. 이 파일 맨 위의 `## [SETUP_REQUIRED]` 섹션 전체를 삭제하세요
3. "설정 완료! 이제 업무 이야기를 나눠보세요." 라고 알려주세요

---

## 나에 대해

- 소속: [회사/팀]
- 직무: [역할]
- 주요 업무: [반복 업무]
- 자주 쓰는 도구: [도구 목록]
- 사내 MCP: [있음/없음]
- 답변·기록 언어: [한국어 / English / 日本語 / 기타]

---

## 이 레포의 역할

**LLM Wiki** 패턴 기반의 second brain입니다.
사람은 업무를 하고, Claude가 기록을 유지합니다.

---

## Weekly Log 운영 규칙

Codex와 Claude 모두 [AGENTS.md의 Logging Strategy](AGENTS.md#logging-strategy)를 따릅니다. 메인·서브 채팅의 기록 기준, 로그 작성에 대한 상시 승인, 중복 방지와 소스 태그는 해당 공통 지침에서 관리합니다.

---

## Available Skills

[AGENTS.md의 Skill Usage](AGENTS.md#skill-usage)에서 공통 목록과 원본 경로를 관리합니다. 각 스킬의 실행 절차는 해당 `SKILL.md`나 가이드를 따릅니다.

---

## URL 자동 처리

[AGENTS.md의 Web Fetching Strategy](AGENTS.md#web-fetching-strategy)를 따릅니다.

---

## 1회용 코딩

[AGENTS.md의 Editing Rules](AGENTS.md#editing-rules)와 [Generated Files And Assets](AGENTS.md#generated-files-and-assets)를 따릅니다.

---

## Memory 관리

[AGENTS.md의 Memory Management](AGENTS.md#memory-management)에서 공통 저장 위치와 운영 기준을 관리합니다.

---

## 새 스킬 추가하기

[AGENTS.md의 Skill Usage](AGENTS.md#skill-usage)에 연결된 스킬 제작 가이드를 따릅니다.
