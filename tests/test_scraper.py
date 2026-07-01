# tests/test_scraper.py

from app.services.scraper import extract_content


data = extract_content(
    "https://blog.python.org/2026/06/python-3150-beta-2/"
)

print("\ntitle:")
print(data["title"])

print("\ncontent:")
print(data["content"])
