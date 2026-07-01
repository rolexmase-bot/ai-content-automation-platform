from app.database import SessionLocal
from app.models.article import Article


db = SessionLocal()

article = Article(

url="https://example.com",

title="AI Content",

content="hello",

summary="summary",

keywords="AI,Automation"

)

db.add(article)

db.commit()

db.refresh(article)

print(article.id)

db.close()
