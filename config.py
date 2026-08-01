"""Configuration and data models for the Resume Screening Agent."""
import os
from dataclasses import dataclass, field
from typing import List, Optional
from pathlib import Path

@dataclass
class ResumeProfile:
    """Structured representation of a parsed resume."""
    name: str = "Unknown"
    email: str = ""
    phone: str = ""
    skills: List[str] = field(default_factory=list)
    experience_years: float = 0.0
    education: List[dict] = field(default_factory=list)
    work_history: List[dict] = field(default_factory=list)
    raw_text: str = ""
    file_path: str = ""

@dataclass
class JobRequirements:
    """Structured representation of a job description."""
    title: str = ""
    required_skills: List[str] = field(default_factory=list)
    preferred_skills: List[str] = field(default_factory=list)
    min_experience_years: float = 0.0
    required_education: str = "Bachelor's"
    responsibilities: List[str] = field(default_factory=list)
    raw_text: str = ""

@dataclass
class CandidateScore:
    """Scoring result for a single candidate."""
    name: str = ""
    file_path: str = ""
    semantic_score: float = 0.0
    skill_match_score: float = 0.0
    experience_score: float = 0.0
    education_score: float = 0.0
    composite_score: float = 0.0
    matched_skills: List[str] = field(default_factory=list)
    missing_skills: List[str] = field(default_factory=list)
    reasoning: str = ""

# Scoring weights (must sum to 1.0)
WEIGHTS = {
    "semantic": 0.40,
    "skills": 0.30,
    "experience": 0.15,
    "education": 0.15,
}

# Model configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GEMINI_MODEL = "gemini-2.0-flash"

def get_api_key() -> Optional[str]:
    """Get Gemini API key from environment or .env file."""
    key = os.environ.get("GOOGLE_API_KEY")
    if key:
        return key
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GOOGLE_API_KEY=") and not line.endswith("your_api_key_here"):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
    return None
