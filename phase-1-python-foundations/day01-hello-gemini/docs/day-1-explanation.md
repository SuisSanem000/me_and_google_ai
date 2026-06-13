Let me first see what's in the project directory and read the Day 1 tasks from the roadmap.

Listed directory me_and_google_ai
Viewed 30_day_ai_engineering_roadmap.md:168-225
Viewed 30_day_ai_engineering_roadmap.md:225-295

Good. I have everything I need. Now let me build the full folder structure and all Day 1 files.

Ran command: `mkdir _docs; mkdir phase-1-python-foundations; mkdir phase-1-python-foundations\day01-hello-gemini; mkdir phase-1-python-foundations\day02-embeddings; mkdir phase-1-python-foundations\day03-pandas-ml; mkdir phase-1-python-foundations\day04-prompt-engineering; mkdir phase-1-python-foundations\day05-llm-pipeline; mkdir phase-1-python-foundations\day06-huggingface; mkdir phase-2-langchain-rag; mkdir phase-2-langchain-rag\day07-langchain-intro; mkdir phase-2-langchain-rag\day08-langchain-classifier; mkdir phase-2-langchain-rag\day09-memory-chatbot; mkdir phase-2-langchain-rag\day10-rag-chunking; mkdir phase-2-langchain-rag\day11-rag-vectorstore; mkdir phase-2-langchain-rag\day12-rag-chatbot; mkdir phase-2-langchain-rag\day13-rag-evaluation; mkdir phase-2-langchain-rag\day14-advanced-rag; mkdir phase-2-langchain-rag\day15-16-rag-fastapi; mkdir phase-3-agents-google; mkdir phase-3-agents-google\day17-langgraph-basics; mkdir phase-3-agents-google\day18-19-research-agent; mkdir phase-3-agents-google\day20-langsmith; mkdir phase-3-agents-google\day21-multimodal; mkdir phase-3-agents-google\day22-firebase-genkit; mkdir phase-3-agents-google\day23-firestore-vector; mkdir phase-3-agents-google\day24-web-frontend; mkdir phase-4-deploy; mkdir phase-4-deploy\day25-docker-cloudrun`

Good. Now move the docs and create all the files simultaneously:

Ran command: `Move-Item "30_day_ai_engineering_roadmap.md" "_docs\"; Move-Item "daily_task_lists.md" "_docs\"`

Now create all the files — root README, .gitignore, Day 1 code:

Created README.md
Created .gitignore
Created .env.example

Now the Day 1 code files:

Created requirements.txt
Created hello_gemini.py
Created hello_openai.py
Created main.py
Created README.md

Now commit everything:

Ran command: `git add .; git commit -m "Day 1: scaffold full project structure, move docs to _docs/, add root README + .gitignore + .env.example, implement hello_gemini + hello_openai + comparison main.py"; git push`

All done and pushed. Here's the complete picture:

---

## Repository Structure

```
me_and_google_ai/
├── .env.example                          ← key template — commit this, never .env
├── .gitignore                            ← Python, venv, .env, ChromaDB, Node, Docker
├── README.md                             ← project index with progress tracker
├── _docs/
│   ├── 30_day_ai_engineering_roadmap.md
│   └── daily_task_lists.md
├── phase-1-python-foundations/
│   ├── day01-hello-gemini/               ← TODAY ✅
│   │   ├── hello_gemini.py
│   │   ├── hello_openai.py
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── README.md
│   ├── day02-embeddings/
│   ├── day03-pandas-ml/
│   ├── day04-prompt-engineering/
│   ├── day05-llm-pipeline/
│   └── day06-huggingface/
├── phase-2-langchain-rag/                ← Days 7–16
├── phase-3-agents-google/               ← Days 17–24
└── phase-4-deploy/                      ← Day 25
```

---

## Day 1 Implementation Notes

**3 files, each with a distinct purpose:**

- **`hello_gemini.py`** — raw Gemini SDK. Note `system_instruction` is set at model init (not per-call), and `usage_metadata` gives you token counts on every response
- **`hello_openai.py`** — OpenAI client. Uses the `messages` array pattern with explicit `system`/`user` roles. `temperature=0.3` keeps factual responses deterministic
- **`main.py`** — the interesting one. Wraps both in `time.perf_counter()` blocks to compare latency and token cost on the same prompt. This pattern scales into Day 14's Pinecone comparison and Day 13's RAGAS eval runs

**To run it, just do:**
```bash
cd phase-1-python-foundations/day01-hello-gemini
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
# Add your keys to root .env, then:
python main.py
```