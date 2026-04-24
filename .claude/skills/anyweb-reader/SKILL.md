# anyweb-reader

Selenium 기반 웹페이지 리더 - WebFetch 실패 시 대안

## Trigger Keywords
- "이 글 읽어줘"
- "블로그 글 읽어줘"
- "웹페이지 내용 보여줘"
- "URL 읽어줘"
- "Medium 글 읽어줘"
- "네이버 블로그 읽어줘"
- "브런치 글 읽어줘"

## Usage
WebFetch로 읽히지 않는 URL이 있을 때 이 스킬을 사용합니다:
1. Selenium으로 headless Chrome 브라우저 실행
2. 페이지 로드 및 JavaScript 렌더링 대기
3. 본문 콘텐츠 추출
4. Markdown 형식으로 반환

## Supported Sites
- Medium (봇 차단 우회)
- 네이버 블로그 (iframe 구조 처리)
- 브런치 (카카오)
- 기타 JavaScript 렌더링 필요 사이트

## Example
```bash
bash $SKILL_DIR/scripts/read-medium.sh "https://medium.com/@user/article"
bash $SKILL_DIR/scripts/read-medium.sh "https://blog.naver.com/user/12345"
bash $SKILL_DIR/scripts/read-medium.sh "https://brunch.co.kr/@user/123"
```

## Dependencies
- `pip3 install selenium`
- Chrome browser
