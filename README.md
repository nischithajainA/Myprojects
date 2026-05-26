# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer built using Flask, NLP embeddings, and Groq LLMs to evaluate resumes against job descriptions.

The application performs:

- Semantic similarity matching
- ATS resume scoring
- Skill gap analysis
- Resume improvement suggestions
- AI-generated resume bullet enhancements
- PDF report download

---

# 🚀 Features

## ✅ Resume Parsing
- Upload resume in PDF/DOCX format
- Extracts text automatically

## ✅ Job Description Matching
- Upload JD file OR paste JD text
- Compares resume with job description

## ✅ Semantic Similarity
Uses SentenceTransformers embeddings:
- `all-MiniLM-L6-v2`

Measures meaning-based similarity rather than simple keyword matching.

## ✅ AI ATS Analysis
Using Groq LLM:
- ATS score
- Matching skills
- Missing skills
- Strengths
- Weaknesses
- Detailed resume suggestions

## ✅ AI Resume Bullet Improvement
LLM rewrites weak resume bullets into stronger ATS-friendly bullets.

## ✅ Beautiful UI
- Bootstrap 5 dashboard
- Progress bars
- Responsive cards
- Loading spinner
- Download report feature

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Flask | Backend |
| Bootstrap 5 | Frontend UI |
| SentenceTransformers | Semantic embeddings |
| Groq API | LLM analysis |
| Python | Core programming |
| HTML/CSS/JS | Frontend |
| Jinja2 | Template rendering |

---

# 📂 Project Structure

```bash
ai_resume_analyser/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── utils/
│   ├── extract.py
│   ├── similarity.py
│   └── llm_analyser.py
│
├── models/
    ├─embedding_model.py
    
```

---

# 🔄 Application Flowchart

```text
                ┌────────────────────┐
                │   User Uploads     │
                │ Resume + JD        │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Flask Backend      │
                │ Receives Files     │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Resume/JD Parsing  │
                │ PDF/DOCX/Text      │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ SentenceTransformer│
                │ Embedding Creation │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Semantic Similarity│
                │ Cosine Similarity  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Groq LLM Analysis  │
                │ ATS + Suggestions  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Structured JSON    │
                │ Response           │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Bootstrap Dashboard│
                │ Result Visualization│
                └────────────────────┘
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️⃣ Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

# ☁️ Deployment

This project is deployable on:

- Render

---

# 🧠 AI Components Used

## Sentence Embeddings

```python
SentenceTransformer("all-MiniLM-L6-v2")
```

Used for semantic similarity matching.

---

## Groq LLM

Model used:

```python
llama-3.1-8b-instant
```

Used for:
- ATS scoring
- Resume evaluation
- Suggestions generation

---

# 📊 Sample Output

- Semantic Similarity Score
- ATS Resume Score
- Matching Skills
- Missing Skills
- Resume Strengths
- Resume Weaknesses
- Detailed Suggestions
- Improved Resume Bullets

---

# 📌 Future Improvements

- User authentication
- Resume history tracking
- Multiple resume comparison
- Interview question generation
- Cover letter generation
- Vector database integration
- RAG implementation
- Multi-language support

---

# 👨‍💻 Author

Developed as an AI Engineering portfolio project demonstrating:

- NLP
- Embeddings
- LLM Integration
- Flask Backend Development
- Prompt Engineering
- Responsive UI Design

---
