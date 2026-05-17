# 📄 Resume Analyzer

An AI-powered desktop application that parses resumes (PDF/DOCX), extracts key information, scores candidates, and generates career insights using OpenAI's GPT-4.

---

## 🧠 How It Works

The project is split into four core modules:

### 1. `file_handling.py` — File Parsing
Handles reading resume files. Supports `.pdf` and `.docx` formats.
- Extracts raw text using `pdfplumber` (for PDFs) and `python-docx` (for DOCX)
- Also counts the number of pages in a file

### 2. `resume_analysis.py` — NLP & Scoring
Two classes power the analysis:
- **`TextExtractor`** — Uses `spaCy` (NER) and regex to extract:
  - Candidate name (via Named Entity Recognition)
  - Email address
  - Mobile number
  - Academic degrees (Bachelor's, Master's, PhD, etc.)
- **`ResumeAnalyzer`** — Matches resume text against a predefined skills dictionary to:
  - Identify which domain (e.g., Software Development, Data Analysis) and sub-domain (e.g., Web Development, Data Science) best fits the candidate
  - Score the resume out of 100 based on presence of name, email, phone, degrees, and relevant skills

### 3. `GenAI_module.py` — AI Insights via GPT-4
Uses LangChain + OpenAI GPT-4 to generate a deep-dive career analysis of the resume:
- Evaluates educational and professional history
- Identifies key skills and achievements
- Recommends career pathways and growth strategies

### 4. `ui_manager.py` — Desktop GUI (Tkinter)
The main entry point. Provides a two-panel interface:
- **Left panel** — Displays the raw resume text after upload
- **Right panel** — Shows extracted info (name, email, domain, score) and AI-generated insights

---

## 🗂️ Project Structure

```
resume-analyzer/
│
├── resume_analysis.py      # NLP extraction + scoring logic
├── file_handling.py        # PDF and DOCX text extraction
├── GenAI_module.py         # LangChain + GPT-4 integration
├── ui_manager.py           # Tkinter GUI (main entry point)
└── requirements.txt        # All Python dependencies
```

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.9 or higher
- An OpenAI API key

### Step 1 — Clone the repository
```bash
git clone https://github.com/venkat-pavan-bandaru/resume-analyzer.git
cd resume-analyzer
```

### Step 2 — Create a virtual environment (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Download the spaCy language model
```bash
python -m spacy download en_core_web_sm
```

### Step 5 — Add your OpenAI API key
Open `GenAI_module.py` and replace the placeholder with your actual key:
```python
self.llm = ChatOpenAI(model_name='gpt-4', temperature=0.5, openai_api_key="YOUR_API_KEY_HERE")
```

> ⚠️ **Security Note:** Never commit your API key to version control. Use environment variables or a `.env` file instead (see below).

#### Recommended: Use a `.env` file
```bash
# .env
OPENAI_API_KEY=your_key_here
```
Then in `GenAI_module.py`:
```python
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
```

---

## 🚀 Running the App

```bash
python ui_manager.py
```

A desktop window will open. Click **"Open File"** to upload a `.pdf` or `.docx` resume. The app will:
1. Display the resume text on the left
2. Show extracted details and score on the right
3. Generate AI career insights below the results

---

## 🎯 Supported Domains & Skills

| Domain | Sub-Domain | Key Skills Tracked |
|---|---|---|
| Software Development | Embedded Systems | Embedded C, RTOS, AUTOSAR, Microcontrollers |
| Software Development | ADAS | Sensor Fusion, MATLAB/Simulink, AUTOSAR |
| Software Development | Software Engineering | Python, C++, Agile, Model-Based Design |
| Software Development | Web Development | JavaScript, React, Angular, Node.js, HTML5 |
| Data Analysis | Data Science | Machine Learning, Deep Learning, Python, R |
| Data Analysis | Data Engineering | Hadoop, Spark, SQL, ETL, Data Warehousing |

---

## 📊 Scoring System

The resume is scored out of **100 points**, divided equally across five criteria:

| Criteria | Points |
|---|---|
| Name detected | 20 |
| Email detected | 20 |
| Mobile number detected | 20 |
| Degree detected | 20 |
| Relevant domain skills found | 20 |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| GUI | Tkinter |
| NLP | spaCy (`en_core_web_sm`) |
| PDF Parsing | pdfplumber |
| DOCX Parsing | python-docx |
| AI / LLM | LangChain + OpenAI GPT-4 |
| Pattern Matching | Python `re` (regex) |

---

## 🔒 .gitignore Recommendation

Add this `.gitignore` to avoid committing sensitive files:

```gitignore
# Python
__pycache__/
*.pyc
venv/
.env

# OS
.DS_Store
Thumbs.db
```

---

## 📌 Known Limitations

- Phone number extraction supports international format (`+XX XXXXX XXXXX`) only
- AI insights require a valid OpenAI API key with GPT-4 access
- The GUI is built with Tkinter and is platform-dependent (works on Windows, macOS, Linux)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source. Add your preferred license here (e.g., MIT).
