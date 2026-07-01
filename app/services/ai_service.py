import os
import json

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_summary(content):

    prompt = f"""
Summarize this article.

Return JSON:

{{
"summary":"...",
"keywords":[]
}}

Article:

{content}
"""


    response = client.chat.completions.create(

        model="gpt-5-mini",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        response_format={
            "type": "json_object"
        }
    )

    result = response.choices[0].message.content

    return json.loads(result)
