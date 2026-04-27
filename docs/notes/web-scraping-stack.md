# 웹 스크래핑/검색 스택 비교

> Brave API · Hyperbrowser MCP · anyweb-reader 셋의 역할과 조합 패턴 정리

## 각 도구의 능력

### Hyperbrowser MCP
클라우드 헤드리스 브라우저를 MCP로 노출.

- **scrape_webpage**: 단일 URL → 마크다운/HTML (JS 렌더링, 봇 차단 우회)
- **crawl_webpages**: 시작 URL에서 링크 따라 다중 페이지 크롤
- **extract_structured_data**: 스키마 기반 구조화 추출
- **search_with_bing**: Bing 검색
- **browser_use_agent / claude_computer_use_agent**: 자연어 브라우저 자동화 (클릭, 폼 입력)
- 세션 유지, 프록시, stealth, CAPTCHA 우회 지원

### Brave Search API
Brave 자체 인덱스 기반 검색 API.

- Web / News / Image / Video / Local Search
- Suggest, Spellcheck, Summarizer (Pro)
- `site:` 필터, freshness, 언어/국가 필터
- **검색만 제공** — 본문 추출은 별도 fetch 필요

### anyweb-reader (자체 제작 스킬)
로컬 Selenium 기반 단일 URL 본문 리더.

- JS 렌더링 O
- 한국 사이트(Medium, 네이버 블로그, 브런치) 검증됨
- 로컬 실행 → **비용 0**, API 키 불필요

## 능력 매트릭스

| 항목 | Brave API | Hyperbrowser | anyweb-reader |
|---|---|---|---|
| 웹 검색 (쿼리 → URL) | ✅ 핵심 | ⚠️ Bing 경유 | ❌ |
| 단일 URL 본문 추출 | ❌ | ✅ | ✅ |
| JS 렌더링 | — | ✅ 클라우드 | ✅ 로컬 |
| 봇 차단 우회 | — | ✅ 강력 | ⚠️ 기본 |
| 멀티스텝 자동화 | ❌ | ✅ | ❌ |
| 비용 | 종량제 | 종량제 | **무료** |
| 한국 사이트 | △ | ✅ | ✅ 검증됨 |

## 조합 패턴

### 1. 대량 검색 워크플로우 (비용 최적화)
```
Brave API (검색·URL 수집)
    ↓
anyweb-reader (로컬 무료 본문 추출)
    ↓ 차단·실패 시
Hyperbrowser (유료 fallback)
```

### 2. 단건 페이지 (URL 이미 보유)
- **anyweb-reader 단독으로 충분**
- Hyperbrowser는 오버킬
- 현재 정책: `WebFetch 실패 시 anyweb-reader` 그대로 유지

### 3. 로그인·클릭 자동화 필요
- anyweb-reader 불가 → **Hyperbrowser 전용**
- 예: 비공개 페이지, SaaS 대시보드 캡처

## anyweb-reader의 고유 가치

세 도구가 다 있어도 버려지지 않는 이유:

1. **로컬 → 비용 0** (대량 처리 유리)
2. **한국 사이트 튜닝 검증** (Medium, 네이버, 브런치)
3. **인증·쿼터 의존성 없음** (오프라인이거나 API 키 만료돼도 동작)
4. **표준 fallback으로 워크플로우에 내장됨**

## 보강 아이디어

- **검색 모드**: Brave API 키 받아 `read.sh --search "쿼리"` → URL 목록 → 각 본문 자동 추출
- **fallback chain**: anyweb-reader 실패 시 Hyperbrowser 자동 호출 옵션
- **batch 모드**: URL 리스트 파일 받아 병렬 처리
