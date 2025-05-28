from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def parse_question(question: str) -> str:
    prompt = f"""
    Ты — помощник, который превращает вопрос на естественном языке в SQL-запрос.
    Работай с таблицей freelancer_data со следующими полями:

    - job_category (TEXT)
    - platform (TEXT)
    - experience_level (TEXT)
    - client_region (TEXT)
    - payment_method (TEXT) — примеры значений: 'Crypto', 'Bank Transfer', 'PayPal'
    - job_completed (INTEGER)
    - earnings_usd (NUMERIC)
    - hourly_rate (NUMERIC)
    - job_success_rate (NUMERIC)
    - client_rating (NUMERIC)
    - job_duration_days (INTEGER)
    - project_type (TEXT)
    - rehire_rate (NUMERIC)
    - marketing_spend (NUMERIC)

    Пример запроса: SELECT AVG(earnings_usd) FROM freelancer_data WHERE payment_method = 'Crypto';

    Вопрос: {question}
    SQL-запрос:
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()
