import requests
from bs4 import BeautifulSoup
from readability import Document


def extract_content(url):
    try:
        if not url:
            return {"title": "", "content": ""}

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 Chrome/125 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        html = response.text


        doc = Document(html)

        title = doc.short_title()

        summary_html = doc.summary()

        soup = BeautifulSoup(
            summary_html,
            "html.parser"
        )

        content = soup.get_text(
            separator="\n",
            strip=True
        )


        if len(content) < 300:

            soup = BeautifulSoup(
                html,
                "html.parser"
            )

            for tag in soup(
                [
                    "script",
                    "style",
                    "nav",
                    "footer",
                    "header"
                ]
            ):
                tag.decompose()

            content = soup.get_text(
                separator="\n",
                strip=True
            )

        content = "\n".join(
            line.strip()
            for line in content.splitlines()
            if line.strip()
        )

        return {
            "title": title,
            "content": content[:15000]
        }

    except Exception as e:

        print("SCRAPER ERROR:", e)

        return {
            "title": "",
            "content": "",
            "error": str(e)
        }
