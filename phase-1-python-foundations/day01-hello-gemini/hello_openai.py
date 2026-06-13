"""
Day 1 — hello_openai.py

Calls the OpenAI API using the official Python client.
Note the structural difference vs Gemini:
  - OpenAI uses a chat completions interface (messages array) as its primary API.
  - Gemini uses generate_content() with an optional system_instruction kwarg.
Both converge on the same LangChain abstraction (ChatOpenAI / ChatGoogleGenerativeAI)
from Day 7 onward — which is the whole point of an orchestration layer.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = "What is an LLM? Explain in exactly 3 bullet points."

response = client.chat.completions.create(
    model="gpt-4o-mini",   # cheapest capable OpenAI model — fine for all exercises
    messages=[
        {
            "role": "system",
            "content": (
                "You are a concise technical explainer. "
                "Use bullet points and plain language. Avoid padding."
            ),
        },
        {"role": "user", "content": PROMPT},
    ],
    temperature=0.3,        # low temp = more deterministic, better for factual tasks
    max_tokens=300,
)

print("=" * 50)
print("Model : gpt-4o-mini")
print("Prompt:", PROMPT)
print("=" * 50)
print(response.choices[0].message.content)
print()
# Usage — OpenAI charges per token; always log this in dev
usage = response.usage
print(f"[Token usage] prompt={usage.prompt_tokens} "
      f"| output={usage.completion_tokens} "
      f"| total={usage.total_tokens}")
