# AI Resume Screening Agent

[![Python 3](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![AI Agent Demo](https://img.shields.io/badge/Project-AI%20Agent%20Demo-orange.svg)](https://github.com/MuthuVarshith/AI-Resume-Screening-Agent)

An AI-powered resume screening agent that parses resumes, matches them against a job description, and produces a ranked shortlist with explainable scoring. It is a practical demo of an AI agent that combines NLP, structured heuristics, and optional LLM reasoning for recruiting workflows.

## Why This Project

This project demonstrates a complete agent loop:
1. Read a job description.
2. Scan a folder of resumes.
3. Extract signals like skills, experience, and education.
4. Score and rank candidates.
5. Save the results as JSON and CSV.

The result is a lightweight, transparent screening workflow that can run locally without needing a paid API.

## Features

- Parses a job description and candidate resumes
- Uses semantic similarity via sentence-transformers
- Applies a transparent multi-signal scoring system
- Produces explainable output with matched and missing skills
- Saves ranked results to JSON and CSV
- Runs locally with the `--no-llm` flag
- Supports optional Gemini-based reasoning when an API key is present

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
- `tests/` – test suite for the scoring pipeline

## Quick Start

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Run the demo

```bash
python main.py --jd sample_jd/jd.txt --resumes sample_resumes --output output --no-llm
```

### Windows PowerShell

```powershell
py -3 main.py --jd sample_jd/jd.txt --resumes sample_resumes --output output --no-llm
```

### 3) View the results

The agent writes outputs to:
- `output/ranked_results.json`
- `output/ranked_results.csv`

## Optional LLM Setup

The project works without an API key. If you want optional Gemini-based reasoning, create a `.env` file from the example:

```bash
cp .env.example .env
```

Then add your key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## How the Scoring Works

The ranking is built from a transparent, explainable score:

- Semantic similarity (40%) – compares resume text and JD embeddings
- Skill match (30%) – checks required skills against extracted skills
- Experience (15%) – rewards candidates who meet the experience requirement
- Education (15%) – scores the highest qualification against the JD requirement

This makes the results easier to inspect than a fully opaque black-box ranking.

## Example Output

A sample run on the included dataset produces a ranked shortlist such as:

```text
1. Michael Chen — 73.7
2. Ananya Patel — 72.1
3. Sophia Nguyen — 67.8
```

## Testing

Run the tests with:

```bash
pytest
```

## Tradeoffs and Notes

- The agent is intentionally simple and easy to run locally.
- It focuses on transparency and reproducibility rather than a full enterprise recruiting system.
- LLM support is optional; the default path works without external API access.
- The current implementation targets text-based resumes for a clean demo experience.

## Future Improvements

Possible next steps include:
- PDF and DOCX upload support for real resumes
- stronger skill extraction and entity recognition
- recruiter preference weighting and custom scoring rules
- a web UI or REST API for interactive use
