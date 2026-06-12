# all roadmaps

# Week 1 — Python for AI + ML Literacy

[Untitled](Untitled%203791f4e20c6a818ca8c2c260f001b731.csv)

# Week 2 — LangChain Core + RAG

[Untitled](Untitled%203791f4e20c6a81cb9d9ee15b5b79250b.csv)

# Week 3 — Agents, Tools, and LLMOps

[Untitled](Untitled%203791f4e20c6a8185ab21ff8fa8eb6b7b.csv)

# Week 4 — Portfolio Polish + Interview Prep

[Untitled](Untitled%203791f4e20c6a812cb10fd881a9542944.csv)

# Reference: Key Links

[Untitled](Untitled%203791f4e20c6a818fbeabd7d4b288aba1.csv)

# ai_engineering_30day_plan

# 30-Day Junior AI Engineer Study Plan

**For: Simin Shoeibi — Experienced Backend Engineer transitioning to AI Engineering Timeline: 4 hours/day max | Goal: Interview-ready in 1 month**

---

## Your Unfair Advantages (Use These)

Before diving in: you already have production LLM experience (Claude Opus/Sonnet at QueryLaw, OpenAI GPT-4 at Parsaiane), NestJS/FastAPI-compatible backend knowledge, Docker/CI-CD, PostgreSQL, and pgvector is just a Postgres extension — you’ve been half an AI engineer for years. The plan below closes the gaps fast.

**What you’re actually missing vs. a typical junior AI candidate:**
- Formal Python AI tooling vocabulary (LangChain, LangGraph, embeddings APIs)
- RAG architecture end-to-end in Python (you’ve done it in TS)
- ML fundamentals literacy (enough to not blank in interviews)
- A Python-based public portfolio

---

## Week 1 — Python for AI + ML Literacy (Days 1–7)

**Theme: Close the Python-for-AI gap and learn just enough ML to speak fluently Daily target: ~4 hours**

### Day 1–2: NumPy + Pandas for AI (8 hrs total)

These are not general data science tools — they’re the substrate everything in the Python AI stack runs on.

**Course:**
- [Kaggle — Pandas](https://www.kaggle.com/learn/pandas) (~4 hrs, free certificate)
- [Kaggle — Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) (~3 hrs, free certificate)

**What to focus on:** DataFrames for loading/inspecting datasets, vectorized operations (NumPy arrays underlie tensors), train/test splits. Skip visualisation deeply.

**Mini-exercise:** Load a CSV dataset (e.g., from Kaggle), clean it with Pandas, split it, and run a basic scikit-learn model. Push to GitHub as `day1-pandas-ml-basics`.

---

### Day 3–4: Embeddings, Vectors, and Semantic Search (8 hrs)

This is where your backend instincts connect to AI. Embeddings are just arrays of floats — you already know arrays.

**Courses:**
- [DeepLearning.AI — Understanding and Applying Text Embeddings](https://learn.deeplearning.ai/courses/google-cloud-vertex-ai) (~1.5 hrs, free)
- [DeepLearning.AI — Building Applications with Vector Databases](https://learn.deeplearning.ai/courses/building-applications-vector-databases) (~2 hrs, free)

**Key concepts to internalize:**
- What an embedding is (dense vector representation)
- Cosine similarity/dot product distance
- How vector search (ANN) differs from SQL LIKE queries
- Why pgvector exists and when to use it vs. Pinecone vs. ChromaDB

**Mini-exercise:** Use OpenAI’s `text-embedding-3-small` or a HuggingFace model to embed 20 sentences, compute cosine similarity manually in NumPy, and visualise with a simple script. Push as `day3-embeddings-from-scratch`.

---

### Day 5–6: LLM Fundamentals + Prompt Engineering (8 hrs)

You’ve done production prompt engineering. Now formalize the vocabulary.

**Courses:**
- [DeepLearning.AI — ChatGPT Prompt Engineering for Developers](https://learn.deeplearning.ai/courses/chatgpt-prompt-eng) (~1.5 hrs, free, certificate)
- [DeepLearning.AI — Building Systems with the ChatGPT API](https://learn.deeplearning.ai/courses/chatgpt-building-system) (~2 hrs, free, certificate)

**Key concepts:**
- System/user/assistant message roles
- Few-shot, chain-of-thought, structured output
- Classification chains, routing, multi-step pipelines
- Moderation and guardrails (you already built this — connect the vocabulary)

**Mini-exercise:** Build a Python CLI tool that takes a user question, routes it to one of two prompt templates based on topic classification, and returns a structured JSON response. Push as `day5-llm-pipeline-cli`.

---

### Day 7: Review + GitHub Cleanup

- Write README files for all projects pushed this week
- Commit the Kaggle certificates to a `/certificates` folder in your repo or link them on LinkedIn
- Review your own QueryLaw/Parsaiane work mentally through the new vocabulary — you’ll articulate it better in interviews now

---

## Week 2 — LangChain Core + RAG (Days 8–16)

**Theme: The framework interviewers ask about most. Build one real RAG system.**

### Day 8–9: LangChain Foundations (8 hrs)

**Primary resource:**
- [LangChain Academy — Introduction to LangChain](https://academy.langchain.com/courses/intro-to-langchain) (free, certificate)

**What to cover:**
- Runnables and LCEL (LangChain Expression Language) — the modern API
- Chat models, prompt templates, output parsers
- Memory and conversation history management
- LangChain’s tool/function calling integration

**Key mental model:** LangChain is a composable pipeline builder. `prompt | model | parser` is like Express middleware — you already think this way.

**Mini-exercise:** Recreate your QueryLaw validation pipeline concept in LangChain — a chain that takes a legal clause as input, classifies its risk level, and returns structured JSON with reasoning. Push as `day8-langchain-document-classifier`.

---

### Day 10–11: LangGraph — Agents and Stateful Workflows (8 hrs)

LangGraph is increasingly what interviewers mean when they say “agents.” It’s the graph-based orchestration layer on top of LangChain.

**Course:**
- [LangChain Academy — Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) (free, certificate)

**Key concepts:**
- Nodes, edges, conditional routing in a state graph
- ReAct agent pattern
- Human-in-the-loop checkpointing (maps directly to your reviewer workflow at QueryLaw)
- Tool use within agents

**Mini-exercise:** Build a simple research agent that: (1) takes a question, (2) decides whether to search or answer directly, (3) uses a tool (e.g., DuckDuckGo search via `langchain_community`), (4) synthesizes a final answer. Push as `day10-langgraph-research-agent`.

---

### Day 12–14: RAG — Full Pipeline (12 hrs)

This is your week’s centrepiece. RAG is the #1 thing junior AI engineers are asked to build.

**Courses:**
- [DeepLearning.AI — LangChain: Chat with Your Data](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data) (~2.5 hrs, free, certificate)
- [DeepLearning.AI — Building and Evaluating Advanced RAG](https://learn.deeplearning.ai/courses/building-evaluating-advanced-rag) (~2 hrs, free, certificate)

**RAG pipeline you must be able to build from scratch:**

```
Documents → Chunking → Embedding → Vector Store → Retriever
    ↓
User Query → Embed Query → Similarity Search → Retrieved Chunks
    ↓
Context + Query → LLM → Answer
```

**Tools to use:**
- `langchain`, `langchain_openai` or `langchain_anthropic`
- `chromadb` or `pgvector` (see below) as vector store
- `RecursiveCharacterTextSplitter` for chunking
- `RAGAS` for evaluation (covered in the advanced RAG course)

**pgvector specifically:** Since you know PostgreSQL deeply, use pgvector as your vector store backend instead of ChromaDB. This gives you a stronger talking point.

```python
from langchain_community.vectorstores import PGVector
CONNECTION_STRING = "postgresql+psycopg2://user:pass@localhost/mydb"
vectorstore = PGVector.from_documents(docs, embeddings, connection_string=CONNECTION_STRING)
```

**Portfolio Project (main deliverable of Week 2):**
Build a full RAG application:
- PDF ingestion → chunking → embedding → stored in pgvector (local Postgres + pgvector Docker)
- Query interface (FastAPI endpoint is ideal given your backend experience)
- Basic evaluation: retrieval precision, answer faithfulness with RAGAS
- Push as `rag-document-qa-pgvector` — this is your primary portfolio piece

---

### Day 15–16: Advanced RAG Patterns + Evaluation (8 hrs)

**Course:**
- [DeepLearning.AI — Advanced Retrieval for AI with Chroma](https://learn.deeplearning.ai/courses/advanced-retrieval-for-ai) (~2 hrs, free)

**Patterns to know:**
- HyDE (Hypothetical Document Embeddings) — generate a hypothetical answer, embed it, retrieve
- Multi-query retrieval — generate multiple query variants, merge results
- Contextual compression — extract only relevant sentences from retrieved chunks
- Reranking with a cross-encoder

Add at least one of these patterns to your RAG project and document the tradeoffs in the README.

---

## Week 3 — Agents, Tools, and LLMOps (Days 17–22)

**Theme: Move from “I can call an LLM” to “I can build production AI systems”**

### Day 17–18: LLM Application Architecture + LLMOps (8 hrs)

**Courses:**
- [DeepLearning.AI — LLMOps](https://learn.deeplearning.ai/courses/llmops) (~2 hrs, free)
- [DeepLearning.AI — Evaluating and Debugging Generative AI](https://learn.deeplearning.ai/courses/evaluating-debugging-generative-ai) (~2 hrs, free)

**Key concepts:**
- Prompt versioning and A/B testing pipelines
- LLM evaluation: automated metrics vs. LLM-as-judge
- Tracing and observability (LangSmith — get a free account)
- Guardrails, input/output validation

**Action:** Set up LangSmith tracing on your RAG project. Add structured logging. This makes your GitHub project look production-grade.

---

### Day 19–20: Tool Use + Function Calling (8 hrs)

**Course:**
- [DeepLearning.AI — Functions, Tools and Agents with LangChain](https://learn.deeplearning.ai/courses/functions-tools-agents-langchain) (~3 hrs, free, certificate)

**Key concepts:**
- OpenAI/Anthropic function calling schemas
- Building and registering custom tools
- Tool selection and agent decision loops
- Handling tool errors gracefully

**Mini-exercise:** Extend your research agent to use 2–3 tools: a calculator, a web search tool, and a database lookup. Implement proper error handling and fallback. Push update to existing agent repo.

---

### Day 21–22: FastAPI + Deployment for AI Apps (8 hrs)

You know backend. This maps directly.

**Resource:**
- [FastAPI official docs — Tutorial](https://fastapi.tiangolo.com/tutorial/) (free, ~4 hrs for AI-relevant parts)
- Focus on: async endpoints, background tasks, file upload, streaming responses (`StreamingResponse` for LLM token streaming)

**Key additions for AI apps:**

```python
# Streaming LLM responses via FastAPI
from fastapi.responses import StreamingResponse

async def stream_llm(query: str):
    async for token in llm.astream(query):
        yield token

@app.get("/chat")
async def chat(query: str):
    return StreamingResponse(stream_llm(query), media_type="text/plain")
```

**Action:** Wrap your RAG pipeline in a FastAPI app with:
- `POST /ingest` — upload and index a PDF
- `POST /query` — ask a question, get a streamed answer
- Dockerize it (you already know Docker)
- Push as update to your RAG project or as a standalone `rag-fastapi-service`

---

## Week 4 — Portfolio Polish + Interview Prep (Days 23–30)

**Theme: Stop learning, start presenting**

### Day 23–24: Build One More Targeted Project (8 hrs)

Choose based on the job descriptions you’re targeting:

**Option A (most hirable):** Agentic system

Build a multi-agent workflow using LangGraph: one agent researches, one summarizes, one formats output. Demonstrates LangGraph mastery.

**Option B (if targeting enterprise/legal/fintech):** Structured data extraction pipeline

Take unstructured documents, extract structured JSON using an LLM with schema validation (Pydantic + `instructor` library), store to PostgreSQL. Maps directly to your QueryLaw experience.

**Option C (if targeting AI product companies):** Chatbot with memory + tools

Persistent conversation history with Redis, tool use, multi-turn context management. Demonstrates production thinking.

---

### Day 25–26: LinkedIn + GitHub Optimization (8 hrs)

**GitHub — for each project, the README must include:**
- Problem statement (1 paragraph)
- Architecture diagram (a simple ASCII or Mermaid diagram)
- Tech stack badges
- How to run it locally (Docker Compose preferred)
- Key technical decisions and tradeoffs
- What you’d do differently / next steps

**LinkedIn updates:**
- Add “AI Engineering” to headline alongside “Backend Engineer”
- Add certificates: Kaggle (Python, Pandas, ML), DeepLearning.AI courses (multiple), LangChain Academy (LangChain + LangGraph)
- Update QueryLaw description to explicitly name: LangChain patterns, structured outputs, prompt engineering, validation pipelines, Claude Opus/Sonnet
- Add a featured post: write 300 words about one technical decision you made in your RAG project

**Your LinkedIn pitch (have this ready):**
> “I’m a backend engineer with 6 years of production experience who’s been building LLM-powered systems in production for the past year — AI-driven legal automation at QueryLaw achieving 95%+ accuracy, and an LLM semantic news pipeline at Parsaiane serving 60K users. I’ve spent the last month going deep on the Python AI stack: LangChain, LangGraph, RAG with pgvector, agent orchestration, and LLM evaluation. I’m looking for a junior-to-mid AI engineering role where I can own the backend of AI-powered products.”

---

### Day 27–28: Interview Prep — Technical (8 hrs)

**Topics you must be able to explain and discuss with code:**

**LLM Fundamentals:**
- What is a transformer at a high level? (attention mechanism, tokens, context window)
- Difference between fine-tuning and RAG — when do you choose each?
- What are hallucinations and how do you mitigate them?
- What is temperature, top-p, top-k?
- Explain structured outputs / JSON mode

**RAG:**
- Walk me through a RAG pipeline end-to-end
- What is chunking strategy and why does it matter?
- How do you evaluate a RAG system? (RAGAS: faithfulness, relevancy, context precision/recall)
- HyDE — what is it and when would you use it?
- What’s the difference between a vector store and a relational DB? When do you use pgvector?

**LangChain / LangGraph:**
- What is LCEL? How does `|` chaining work?
- What is a Runnable? What is a chain vs. an agent?
- How does LangGraph differ from a simple LangChain chain?
- What is a checkpointer in LangGraph?

**Agents:**
- What is the ReAct pattern?
- How does function/tool calling work at the API level?
- How do you handle agent loops / infinite loops?

**MLOps / Production:**
- How do you trace/observe LLM calls in production?
- What is LangSmith and why would you use it?
- How do you version prompts?
- How do you A/B test prompt changes?

**Your existing experience translated:**
- At QueryLaw: “I built antifragile AI reasoning cores with failure-feedback loops” = “production agent with error recovery and adaptive prompting”
- At Parsaiane: “LLM-powered semantic news feed” = “LLM pipeline with scoring, classification, and personalization at scale”

---

### Day 29: Interview Prep — Behavioral + System Design (4 hrs)

**System design questions you should be able to answer:**

1. “Design a document Q&A system for 10,000 users” — answer: ingestion pipeline, chunking strategy, vector DB with metadata filtering, caching frequent queries with Redis (you’ve done this), async query processing, streaming responses
2. “How would you evaluate whether your RAG system is working?” — RAGAS metrics, LLM-as-judge, user feedback loops, retrieval analytics
3. “How do you handle prompt injection attacks?” — input sanitization, system prompt isolation, output validation, you built guardrails at QueryLaw
4. “Walk me through a production AI system you built” — QueryLaw, in full technical detail

**Behavioral (your strongest cards):**
- Production at scale (60K users, sub-100ms p95 latency)
- 95%+ accuracy on a hard legal AI task — quantify how you got there
- Failure handling and antifragility — your QueryLaw work is genuinely impressive, use it
- Technical writing that reached 120K developers — demonstrates communication

---

### Day 30: Final Review + Job Applications (4 hrs)

- Final pass on all GitHub READMEs
- Apply to 10–15 roles: target “AI Engineer,” “LLM Engineer,” “ML Engineer,” “Backend AI Engineer”
- Good targets: companies building AI features (not AI research labs), AI startups, enterprise software adding AI layers, legal tech, fintech, developer tooling
- Geographic targets based on your profile: Germany (Berlin), Netherlands (Amsterdam), Switzerland (Zurich/Basel), Sweden (Stockholm), remote EU

---

## Full Course List + Certificates

| Course | Platform | Hours | Certificate | Cost |
| --- | --- | --- | --- | --- |
| Pandas | Kaggle | 4 | Yes | Free |
| Intro to Machine Learning | Kaggle | 3 | Yes | Free |
| Prompt Engineering for Developers | DeepLearning.AI | 1.5 | Yes | Free |
| Building Systems with the ChatGPT API | DeepLearning.AI | 2 | Yes | Free |
| Chat with Your Data | DeepLearning.AI | 2.5 | Yes | Free |
| Building and Evaluating Advanced RAG | DeepLearning.AI | 2 | Yes | Free |
| Functions, Tools and Agents with LangChain | DeepLearning.AI | 3 | Yes | Free |
| Introduction to LangChain | LangChain Academy | 6 | Yes | Free |
| Introduction to LangGraph | LangChain Academy | 6 | Yes | Free |
| Understanding Text Embeddings | DeepLearning.AI | 1.5 | No | Free |
| Building Applications with Vector DBs | DeepLearning.AI | 2 | No | Free |
| LLMOps | DeepLearning.AI | 2 | No | Free |
| Evaluating and Debugging Generative AI | DeepLearning.AI | 2 | No | Free |
| Advanced Retrieval for AI | DeepLearning.AI | 2 | No | Free |

**Certificates by end of month: ~9 (Kaggle x2, DeepLearning.AI x5, LangChain Academy x2)**

---

## Portfolio Projects (GitHub)

| Project | Stack | Demonstrates |
| --- | --- | --- |
| `day1-pandas-ml-basics` | Python, Pandas, scikit-learn | ML literacy |
| `day3-embeddings-from-scratch` | Python, NumPy, OpenAI API | Embeddings understanding |
| `day5-llm-pipeline-cli` | Python, LangChain, Anthropic/OpenAI API | Pipeline thinking |
| `day8-langchain-document-classifier` | LangChain, Pydantic | LangChain proficiency |
| `day10-langgraph-research-agent` | LangGraph, LangChain, tools | Agent orchestration |
| `rag-document-qa-pgvector` ⭐ | Python, LangChain, pgvector, FastAPI, Docker | Full RAG system — your flagship |
| `week3-project` (agent or extractor) | LangGraph or Pydantic+instructor | Depth in chosen direction |

**The `rag-document-qa-pgvector` The project is your anchor.** Every other project supports it. In interviews, you lead with this.

---

## What You Can Honestly Claim After 30 Days

- Built production RAG systems using LangChain, pgvector, and FastAPI
- Designed and implemented agentic workflows with LangGraph (ReAct pattern, tool use, stateful graphs)
- Experience with LLM evaluation using RAGAS (faithfulness, context precision/recall)
- Structured output engineering with Pydantic and function calling
- LLM observability and tracing with LangSmith
- Prior production experience: Claude Opus/Sonnet at QueryLaw (95%+ accuracy), GPT-4 at Parsaiane (60K users)
- Deployment: Dockerized AI services, async FastAPI with streaming LLM responses

**What to not overclaim:** Deep ML research, model training from scratch, fine-tuning (you can say “familiar with the concepts but haven’t done hands-on fine-tuning yet” — that’s honest and fine for junior roles).

---

## Key Links

- LangChain Academy: https://academy.langchain.com
- DeepLearning.AI short courses: https://learn.deeplearning.ai
- Kaggle Learn: https://www.kaggle.com/learn
- LangSmith (free tier): https://smith.langchain.com
- pgvector: https://github.com/pgvector/pgvector
- RAGAS: https://docs.ragas.io
- Instructor (structured outputs): https://python.useinstructor.com
- LangChain docs: https://python.langchain.com/docs/introduction
- LangGraph docs: https://langchain-ai.github.io/langgraph/

# roadmap

Now I have the skill info. Let me create the comprehensive markdown file directly since it's more appropriate than a docx for this content type.Here's the full plan. A few things worth flagging about how it's structured for your specific situation:

**Why this differs from the previous notes you gathered:** The old plan was written for a beginner — 6 months, Python syntax from scratch, basic ML certs. You don't need any of that. I cut Week 1 down to the two gaps that actually matter (embeddings + ML vocabulary) and front-loaded LangChain Academy, which has proper certificates and is far more relevant than the AWS/Google cloud badges.

**The anchor project is `rag-document-qa-pgvector`.** Everything else in the plan exists to support it or extend it. You already have PostgreSQL experience and you already built something like this at QueryLaw in TypeScript — rebuilding it in Python with LangChain gives you a direct story: "I've done this in production, here's the Python equivalent."

**LangChain Academy is the most important resource in this plan** — it's free, has verifiable certificates, and interviewers specifically recognize it. Start the LangChain course on Day 8, not after finishing everything else.

**Your QueryLaw experience is more valuable than a month of courses.** The plan ends with explicit framing on how to translate that work into AI engineering vocabulary. Don't undersell it — 95%+ accuracy on automated legislative analysis with failure-feedback loops is genuinely impressive and you built the system, not just called an API.