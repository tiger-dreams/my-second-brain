# anyweb-reader

Selenium 기반 웹페이지 리더 - WebFetch가 실패하는 사이트를 읽습니다.

## 용도

- 봇 차단 우회 (Medium, 네이버 블로그 등)
- JavaScript 렌더링이 필요한 페이지
- WebFetch 실패 시 대안

## 호환성

| 플랫폼 | 상태 | 품질 |
|--------|:----:|:----:|
| Medium | ✅ | ⭐⭐⭐ |
| 네이버 블로그 | ✅ | ⭐⭐ |
| 브런치 | ✅ | ⭐⭐ |

## 설치

### 의존성
```bash
pip3 install selenium
```

### 요구사항
- Python 3.9+
- Chrome 브라우저 (ChromeDriver는 Selenium이 자동 관리)

## 사용법

### 자연어 트리거
```
"이 글 읽어줘: https://medium.com/..."
"https://blog.naver.com/... 내용 보여줘"
"브런치 글 분석해줘: https://brunch.co.kr/..."
```

### 직접 실행
```bash
.claude/skills/anyweb-reader/scripts/read-medium.sh "<URL>"
```

## 작동 방식

1. Selenium으로 Chrome 브라우저 열기 (headless)
2. URL 접속 및 JavaScript 렌더링 대기
3. 본문 콘텐츠 추출 (제목, 본문, 헤딩, 리스트)
4. Markdown 형식으로 출력

## 제한사항

- 로그인이 필요한 콘텐츠는 접근 불가
- 이미지는 추출되지 않음 (텍스트만)
- 일부 사이트는 UI 요소가 함께 추출될 수 있음
