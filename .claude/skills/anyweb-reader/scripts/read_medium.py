#!/usr/bin/env python3
"""
Read Medium articles using Selenium to bypass bot detection.
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def read_medium_article(url):
    """
    Read a blog article using Selenium.

    Args:
        url: Blog article URL

    Returns:
        Article content as text
    """
    # Chrome options - advanced stealth settings
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')  # New headless mode (less detectable)
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')

    # Additional stealth settings
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Prefs to avoid detection
    prefs = {
        "profile.default_content_setting_values.notifications": 2,
        "profile.managed_default_content_settings.images": 2
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = None
    try:
        # Initialize driver (Selenium Manager will handle ChromeDriver automatically)
        driver = webdriver.Chrome(options=chrome_options)

        # Execute CDP commands to further hide automation
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {
            "userAgent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
        })
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # Load the page
        print(f"Loading: {url}", file=sys.stderr)
        driver.get(url)

        # Wait longer for dynamic content
        time.sleep(3)  # Let JavaScript fully load

        # Wait for article content to load
        wait = WebDriverWait(driver, 15)

        # Medium articles are typically in <article> tags
        try:
            article = wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "article"))
            )
            time.sleep(1)  # Wait for article to stabilize
        except:
            # Fallback: try to find main content
            print("Article tag not found, using body", file=sys.stderr)
            article = driver.find_element(By.TAG_NAME, "body")

        # Extract title
        try:
            title = driver.find_element(By.TAG_NAME, "h1").text
        except:
            title = driver.title

        # Extract article content
        # Medium uses various paragraph tags
        paragraphs = article.find_elements(By.TAG_NAME, "p")
        content_parts = [p.text for p in paragraphs if p.text.strip()]

        # Also get h2, h3 headings
        headings = article.find_elements(By.CSS_SELECTOR, "h2, h3, h4")

        # Combine all content
        full_content = f"# {title}\n\n"

        # Get all text content at once to avoid stale element issues
        # Use JavaScript to extract text content
        article_text = driver.execute_script("""
            const article = arguments[0];
            let content = '';

            // Get all text nodes recursively
            const elements = article.querySelectorAll('h1, h2, h3, h4, p, ul, ol, blockquote');

            elements.forEach(el => {
                const tagName = el.tagName.toLowerCase();
                const text = el.textContent.trim();

                if (!text) return;

                if (tagName === 'h1') {
                    content += '\\n# ' + text + '\\n\\n';
                } else if (tagName === 'h2') {
                    content += '\\n## ' + text + '\\n\\n';
                } else if (tagName === 'h3') {
                    content += '\\n### ' + text + '\\n\\n';
                } else if (tagName === 'h4') {
                    content += '\\n#### ' + text + '\\n\\n';
                } else if (tagName === 'blockquote') {
                    content += '\\n> ' + text + '\\n\\n';
                } else if (tagName === 'ul' || tagName === 'ol') {
                    const items = el.querySelectorAll('li');
                    items.forEach(item => {
                        content += '- ' + item.textContent.trim() + '\\n';
                    });
                    content += '\\n';
                } else {
                    content += text + '\\n\\n';
                }
            });

            return content;
        """, article)

        full_content += article_text

        return full_content.strip()

    except Exception as e:
        print(f"Error reading article: {str(e)}", file=sys.stderr)
        raise
    finally:
        if driver:
            driver.quit()

def main():
    if len(sys.argv) < 2:
        print("Usage: read_medium.py <blog_url>", file=sys.stderr)
        sys.exit(1)

    url = sys.argv[1]

    if not url.startswith(('http://', 'https://')):
        print(f"Error: URL must be a valid HTTP/HTTPS URL", file=sys.stderr)
        sys.exit(1)

    try:
        content = read_medium_article(url)
        print(content)
    except Exception as e:
        print(f"Failed to read article: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
