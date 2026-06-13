"""
Day 1 — main.py

Runs both APIs with the same prompt and prints a side-by-side comparison.
This is the pattern you'll use throughout the roadmap: same input, different
models, compare output quality and token cost. By Day 14 you'll be doing
this programmatically with RAGAS metrics.
"""

import os
import time
import google.generativeai as genai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ── Clients ────────────────────────────────────────────────────────────────────
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="You are a concise technical explainer. Use bullet points.",
)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM = "You are a concise technical explainer. Use bullet points."
PROMPT = "What is an LLM? Explain in exactly 3 bullet points."

DIVIDER = "─" * 60


def call_gemini(prompt: str) -> dict:
    t0 = time.perf_counter()
    resp = gemini_model.generate_content(prompt)
    latency = time.perf_counter() - t0
    return {
        "text": resp.text,
        "latency_s": round(latency, 2),
        "tokens": resp.usage_metadata.total_token_count,
    }


def call_openai(prompt: str) -> dict:
    t0 = time.perf_counter()
    resp = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=300,
    )
    latency = time.perf_counter() - t0
    return {
        "text": resp.choices[0].message.content,
        "latency_s": round(latency, 2),
        "tokens": resp.usage.total_tokens,
    }


if __name__ == "__main__":
    print(f"\nPrompt: {PROMPT}\n")
    print(DIVIDER)

    gemini = call_gemini(PROMPT)
    print(f"🔵 Gemini 2.0 Flash  [{gemini['latency_s']}s | {gemini['tokens']} tokens]")
    print(DIVIDER)
    print(gemini["text"])

    print(DIVIDER)

    gpt = call_openai(PROMPT)
    print(f"🟢 GPT-4o-mini       [{gpt['latency_s']}s | {gpt['tokens']} tokens]")
    print(DIVIDER)
    print(gpt["text"])

    print(DIVIDER)
    print(f"\n📊 Comparison")
    print(f"   Latency  — Gemini: {gemini['latency_s']}s | OpenAI: {gpt['latency_s']}s")
    print(f"   Tokens   — Gemini: {gemini['tokens']} | OpenAI: {gpt['tokens']}")
