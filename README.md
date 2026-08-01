# Resume Screening Agent

A refreshed resume screening sample project that parses resumes, scores candidates against a job description, and generates a ranked shortlist with explainable reasoning.

**Fresh update** for the ROOMAN AI 24-Hour Agent Challenge (Resume Screening Agent - Intermediate)

> "This version uses a new AI Engineer-focused job description, a fresh set of sample resumes, and updated ranking output to showcase the workflow with a new scenario."

## Project Status

- ✅ Fully implemented CLI-based resume screening workflow
- ✅ Local scoring engine with semantic and rule-based matching
- ✅ Fresh sample resumes and updated output files included
- ✅ Ready for review, demo, and further extension

## Features

- **Multi-Signal Scoring**: Evaluates candidates across 4 weighted signals (semantic similarity, skill matching, experience, education)
- **Semantic NLP Analysis**: Uses `sentence-transformers` (`all-MiniLM-L6-v2`) for deep contextual matching beyond keyword search
- **LLM-Enhanced Extraction** (Optional): Google Gemini for structured resume/JD parsing and reasoning generation
- **Robust Fallback**: Works entirely locally without any API key using regex extraction + embedding scoring
- **Multi-Format Parsing**: Handles PDF, DOCX, and plain text resumes
- **Batch Processing**: Processes 10+ resumes in a single run
- **Dual Output**: Exports results to both JSON and CSV formats



## Quick Start

### 1. Clone the repository
```bash
git clone <repo_url>
cd resume_screening_agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Set up Gemini API key
Get a free key at https://aistudio.google.com/apikey

```bash
# Option A: Environment variable
export GOOGLE_API_KEY="your_api_key_here"

# Option B: Create a .env file
cp .env.example .env
# Edit .env and add your key
```

> **Note**: The agent works perfectly without an API key. It uses local embedding models for scoring and regex for extraction. The API key adds LLM-powered structured extraction and reasoning.

### 4. Run the agent
```bash
# With command-line arguments
python main.py --jd sample_jd/jd.txt --resumes sample_resumes/

# Disable LLM even if API key is available
python main.py --jd sample_jd/jd.txt --resumes sample_resumes/ --no-llm

# Interactive mode (will prompt for paths)
python main.py
```

### CLI Options
| Flag | Description | Default |
|------|------------|---------|
| `--jd` | Path to job description file | _(interactive prompt)_ |
| `--resumes` | Path to directory of resumes | _(interactive prompt)_ |
| `--output` | Output directory for results | `output` |
| `--top` | Show detailed view for top N candidates | `5` |
| `--no-llm` | Disable LLM even if API key is set | `False` |

## Sample Output

Running with the refreshed AI Engineer sample data:

```
RANKING RESULTS:
+--------+----------------+---------+-----------+
|   Rank | Name           |   Score | Matched   |
+========+================+=========+===========+
|      1 | Michael Chen   |    73.7 | 7 skills  |
|      2 | Ananya Patel   |    72.1 | 7 skills  |
|      3 | Sophia Nguyen  |    67.8 | 5 skills  |
|      4 | Priya Nair     |    66.9 | 6 skills  |
|      5 | Lina Fernandez |    65.9 | 5 skills  |
|      6 | Emma Thompson  |    65.9 | 6 skills  |
|      7 | Maya Chen      |    65.6 | 5 skills  |
|      8 | Javier Lopez   |    61.6 | 4 skills  |
|      9 | Daniel Rivera  |    61.1 | 4 skills  |
|     10 | Rahul Kumar    |    56.7 | 3 skills  |
|     11 | Tariq Hassan   |    55.0 | 5 skills  |
|     12 | Owen Brooks    |    48.6 | 4 skills  |
+--------+----------------+---------+-----------+

--- Candidate Detail: Michael Chen ---
Rank: 1
Composite Score: 73.7
Matched Skills: github, pandas, git, pytorch, tensorflow, numpy, python
Missing Skills: machine learning
Reasoning: Ranked #1 with a composite score of 73.7/100. Matched 7/8 required skills.
```

Results are saved to [output/ranked_results.json](output/ranked_results.json) and [output/ranked_results.csv](output/ranked_results.csv).

## Scoring Method

The agent uses a **4-signal weighted composite score** (detailed in [scoring_method.md](scoring_method.md)):

| Signal | Weight | Method |
|--------|--------|--------|
| Semantic Similarity | 40% | Cosine similarity between resume and JD embeddings (`all-MiniLM-L6-v2`) |
| Skill Match | 30% | Exact + semantic fuzzy matching of required skills |
| Experience | 15% | Years comparison (proportional if below, 100% if meets/exceeds) |
| Education | 15% | Degree hierarchy comparison (PhD > Master's > Bachelor's) |

**Composite Score** = (Semantic x 0.40) + (Skills x 0.30) + (Experience x 0.15) + (Education x 0.15)



## Design Choices & Tradeoffs

### Why `sentence-transformers` for semantic similarity?
Using a lightweight local embedding model (`all-MiniLM-L6-v2`, 22M params) provides fast, offline, and cost-free dense vector comparison. It captures contextual meaning that keyword matching misses (e.g., "built retrieval-augmented generation systems" is semantically relevant to an "AI engineer" JD even without exact keyword overlap).

### Why multi-signal scoring instead of a single LLM prompt?
A single LLM prompt asking "rate this candidate 0-100" is opaque, non-reproducible, and prone to hallucination. Our 4-signal deterministic approach is:
- **Explainable**: Each score dimension is transparent and auditable
- **Reproducible**: Same input always produces the same output
- **Debuggable**: Easy to diagnose why a candidate scored high or low

### Why Gemini with regex fallback?
Gemini excels at extracting nuanced skills and generating reasoning. However, a regex fallback ensures the agent **never fails** due to API rate limits, network issues, or missing API keys. This makes reviewer setup foolproof.

### What would improve with more time?
- **Fine-tuned extraction models**: Specialized NER models for resume parsing (e.g., SpaCy with custom entities)
- **Streamlit/Gradio UI**: Visual interface with drag-and-drop resume upload
- **Better skill taxonomy**: A curated skill ontology with synonyms (e.g., "React.js" = "ReactJS" = "React")
- **PDF OCR**: Support for image-based/scanned PDFs via Tesseract
- **Configurable weights**: Let users adjust scoring weights via CLI

## Running Tests

```bash
cd Resume-Screening-Agent
python -m pytest tests/test_agent.py -v
```

## Recent Update

This version includes a fresh set of sample resumes and refreshed output files so the project feels like a new, updated walkthrough rather than the original demo state.

All 19 tests cover: data model validation, scoring functions, file discovery, JSON/CSV output, and edge cases.

## Limitations

- PDF parsing quality depends on document structure (image-heavy PDFs need OCR, not included)
- Regex-based skill extraction may miss unconventional skill formats; LLM mode is more robust
- Semantic similarity scores tend to cluster in a narrow range for text documents (mitigated by the multi-signal approach)
- The `exit code 1` on Windows PowerShell is a false alarm caused by HuggingFace stderr warnings, not an actual failure

## License

MIT License
