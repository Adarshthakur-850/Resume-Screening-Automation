# Resume Screening Automation

Automated screening tool that ranks resumes against a job description using NLP and Regex.

## Features
- **Parsing**: Extracts text from resume files.
- **Extraction**: Identifies contact info (Email, Phone) and technical skills.
- **Scoring**: Computes a match score based on content similarity (TF-IDF) and skill overlap.
- **Ranking**: Generates a CSV report of candidates sorted by relevance.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. (Optional) Download NLP model if using detailed extraction:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Usage
1. Place the Job Description in `data/job_description/jd.txt`.
2. Place Resumes in `data/resumes/` (.txt supported by default).
3. Run the pipeline:
   ```bash
   python main.py
   ```
4. Check `output/ranking_report.csv` for results.

*Note: The script automatically generates dummy data if folders are empty.*
