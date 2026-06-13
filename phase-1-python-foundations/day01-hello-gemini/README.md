# Day 1 — Hello Gemini & OpenAI

First project in the 30-day AI Engineering journey.
Establishes the baseline: calling two LLM APIs with the same prompt and comparing
their output, latency, and token usage side by side.

## What This Covers

- Google Gemini API via `google-generativeai` SDK
- OpenAI API via the official `openai` Python client
- `.env`-based secret management with `python-dotenv`
- Token usage logging (critical for cost awareness from day one)

## Architecture Note

Both SDKs are called directly here — no orchestration layer yet.
From Day 7 onward, LangChain's `ChatGoogleGenerativeAI` and `ChatOpenAI`
wrap these same HTTP calls, letting you swap models with a single string change.
Knowing the raw API first means you're never blindly trusting the abstraction.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Side-by-side comparison runner |
| `hello_gemini.py` | Gemini-only script |
| `hello_openai.py` | OpenAI-only script |
| `requirements.txt` | Dependencies |

## Setup

```bash
# From repo root — copy template and fill in your keys
cp .env.example .env

# Create venv and install
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

# Run the comparison
python main.py

# Or run individually
python hello_gemini.py
python hello_openai.py
```

## Expected Output

```
Prompt: What is an LLM? Explain in exactly 3 bullet points.
────────────────────────────────────────────────
🔵 Gemini 2.0 Flash  [0.82s | 147 tokens]
────────────────────────────────────────────────
• LLMs are neural networks trained on massive text datasets...
...

🟢 GPT-4o-mini       [1.1s | 132 tokens]
────────────────────────────────────────────────
• Large Language Models (LLMs) are AI systems...
...

📊 Comparison
   Latency  — Gemini: 0.82s | OpenAI: 1.1s
   Tokens   — Gemini: 147   | OpenAI: 132
```

## What I Learned

- Gemini uses `generate_content()` with `system_instruction` at model init
- OpenAI uses `chat.completions.create()` with a `messages` array
- Both converge on the same conceptual interface — LangChain unifies them
- Token counts differ because tokenizers differ between providers
