from app.services.ai_service import generate_summary


article = """
Python is a popular programming language.

It is used in AI,
web development,
data analysis,
automation.
"""


result = generate_summary(article)

print(result)
