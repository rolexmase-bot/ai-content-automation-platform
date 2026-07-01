# AI Content Automation Platform

This project is a FastAPI-based backend system that processes articles from URLs, extracts content, generates AI summaries and keywords, and stores results into a PostgreSQL database.

The system is fully containerized using Docker and supports optional integration with n8n for workflow automation.

---

# Project Structure

app/

├── api/
│   ├── content.py → article processing API
│   ├── history.py → article history API
│   ├── n8n.py → webhook endpoints for external automation (n8n)
│   ├── web.py → web interface routes
│   └── __init__.py

├── services/
│   ├── scraper.py → extracts title and content from URL
│   ├── ai_service.py → generates summary and keywords using OpenAI
│   ├── content_service.py → coordinates scraping and AI processing
│   └── __init__.py

├── crud/
│   ├── article_crud.py → database CRUD operations for articles
│   └── article_history.py → database operations for article history

├── models/
│   ├── article.py → SQLAlchemy database model
│   └── __init__.py

├── database/
│   ├── db.py → database engine and session configuration
│   └── __init__.py

├── schemas/
│   └── article.py → Pydantic request and response schemas

├── workflows/
│   └── process_article.py → processing workflow (scrape → AI → save)

├── templates/
│   └── index.html → web interface page

├── static/
│   └── static assets (CSS, JavaScript, images)

├── config.py → application configuration

├── init_db.py → initializes database tables

├── main.py → FastAPI application entry point

└── __init__.py

---

# System Flow

URL input → scraper.py → ai_service.py → article_crud.py → PostgreSQL → API response

n8n webhook → api/n8n.py → process_article.py → database storage

---

# Tech Stack

FastAPI  
PostgreSQL  
OpenAI API  
Docker / Docker Compose  
SQLAlchemy  
n8n (optional automation layer)

---

# Environment Variables

You must create a `.env` file manually in the project root before running the system.

Example:

OPENAI_API_KEY=your_openai_key  
DATABASE_URL=postgresql://postgres:123456@postgres:5432/ai_content  

---

# Run with Docker

This project is fully containerized.

## Start all services

docker-compose up -d --build

---

## Check running containers

docker ps

---

## Access services

FastAPI API:
http://localhost:8000/docs

n8n Dashboard:
http://localhost:5678

PostgreSQL:
localhost:5432

---

# API Example
## Summarize Article

```bash
curl -X POST "http://localhost:8000/summarize" \
-H "Content-Type: application/json" \
-d '{
  "url": "https://blog.python.org/"
}'
```

### Request

```json
{
  "url": "https://blog.python.org/"
}
```

### Response

```json
{
  "title": "...",
  "summary": "...",
  "keywords": "..."
}
```
# Core Workflow (process_article.py)

This is the main pipeline of the system.

It performs the following steps:

1. Receive URL input
2. Call scraper.py to extract article content
3. Call ai_service.py to generate summary and keywords
4. Call article_crud.py to save results into PostgreSQL
5. Return structured response

---

# Database Layer

db.py → manages database connection  
article.py → defines database table structure  
article_crud.py → handles database insert/query operations  

---

# AI Module

ai_service.py receives article content and returns:

- summary
- keywords

It uses OpenAI API for text generation.

---

# Scraper Module

scraper.py is responsible for:

- Fetching HTML from URL
- Extracting article title
- Extracting main content

---

# Testing

Run automated tests:

pytest tests/

Run manual scripts:

python test_ai.py  
python test_insert.py  

---

# Important Notes

- .env file must be created manually
- credentials.json must NOT be committed
- process_article.py contains core pipeline logic
- Docker is the recommended way to run this project
- Do not expose API keys in source code

---

# Docker Services Included

- FastAPI backend service
- PostgreSQL database
- n8n workflow engine (optional)

---

# Run Project (One Command)

docker-compose up -d
