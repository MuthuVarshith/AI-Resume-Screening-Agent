# AI Resume Screening Agent

[![Python 3](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI Agent Demo](https://img.shields.io/badge/Project-AI%20Agent%20Demo-orange.svg)](https://github.com/MuthuVarshith/AI-Resume-Screening-Agent)

Public GitHub repository: https://github.com/MuthuVarshith/AI-Resume-Screening-Agent

This project is a Resume Screening Agent, one of the AI agent challenge options. It reads a job description, evaluates a folder of resumes, and produces a ranked shortlist with explainable scoring.

## What This Agent Does

This agent is built to:
- parse resumes and extract skills, experience, and education,
- compare them against a job description,
- compute a relevance score using NLP similarity and structured heuristics,
- rank candidates and generate a shortlist,
- save the results as CSV and JSON for review.

### Expected Capabilities

- Parse 10+ resumes in a single run
- Score each resume against the job description
- Output an ordered shortlist with reasoning
- Provide a transparent, explainable ranking instead of a black-box result

## How the AI Agent Works

This agent follows a simple loop:
1. Read the job description.
2. Discover the resumes in the sample folder.
3. Extract candidate signals from each resume.
4. Score and rank the candidates.
5. Save the ranked results for human review.

This is the core Input → Think → Act → Output pattern of an AI agent.

## Project Structure

- `main.py` – CLI entry point
- `config.py` – scoring weights, model settings, and API key handling
- `jd_parser.py` – job description parsing
- `resume_parser.py` – resume parsing and extraction
- `scorer.py` – semantic and structured scoring
- `ranker.py` – candidate ranking and reasoning
- `utils.py` – file discovery, formatting, and output saving
- `sample_jd/jd.txt` – sample job description
- `sample_resumes/` – sample resumes used for the demo
- `output/` – generated ranked results
- `tests/` – unit tests for the scoring pipeline

## Setup Instructions

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Create an environment file (optional)

The project works without an API key. If you want optional Gemini-based reasoning, create a `.env` file from the example:

```bash
cp .env.example .env
```

Then add your key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## How to Run the Agent End to End

### Linux or macOS

```bash
python main.py --jd sample_jd/jd.txt --resumes sample_resumes --output output --no-llm
```

### Windows PowerShell

```powershell
py -3 main.py --jd sample_jd/jd.txt --resumes sample_resumes --output output --no-llm
```

### With optional LLM support

If you have a valid Google API key configured, run:

```bash
python main.py --jd sample_jd/jd.txt --resumes sample_resumes --output output
```

## Sample Inputs and Outputs

### Sample Input

- Job description: `sample_jd/jd.txt`
- Resume folder: `sample_resumes/`

### Sample Output

The agent writes:
- `output/ranked_results.json`
- `output/ranked_results.csv`

Example ranked output from the included sample data:

```text
1. Michael Chen — 73.7
2. Ananya Patel — 72.1
3. Sophia Nguyen — 67.8
```

## Agent-Specific Deliverables

This submission includes:
- a job description file,
- a folder of sample resumes,
- ranked output in CSV and JSON,
- a short explanation of the scoring method.

## Scoring Method

The ranking is built from a transparent multi-signal score:

- Semantic similarity (40%) – compares resume text and job description embeddings
- Skill match (30%) – checks required skills against extracted skills
- Experience (15%) – rewards candidates who meet the experience requirement
- Education (15%) – scores the highest qualification against the job requirement

## Testing

Run the tests with:

```bash
pytest
```

## Tradeoffs and Notes

- The agent is intentionally simple and easy to run locally.
- It focuses on transparency and reproducibility instead of a fully enterprise recruiting system.
- LLM support is optional; the default path works without external API access.
- The current implementation targets text-based resumes for a clean demo experience.

## Future Improvements

Possible next steps include:
- PDF and DOCX upload support for real resumes
- stronger skill extraction and entity recognition
- recruiter preference weighting and custom scoring rules
- a web UI or REST API for interactive use
