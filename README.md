# 📄 Resume Screening Automation

Automated system to screen and rank resumes using Natural Language Processing (NLP) and Machine Learning (ML), saving time and improving recruitment efficiency.

---

## 🚀 Project Overview

Resume Screening Automation is a tool designed to automatically evaluate, score, and rank resumes based on specified job requirements. It uses NLP techniques and similarity scoring to compare candidate profiles with job descriptions and provide a ranked shortlist of the best matches.

This project aims to improve hiring workflows by:
- Reducing manual screening time
- Providing objective and consistent resume evaluations
- Supporting recruiters in high-volume hiring

---

## 🧠 Features

✔ Parse and extract key information from resumes  
✔ Transform text into embeddings for semantic comparison  
✔ Compare resumes with job descriptions  
✔ Generate similarity scores and rank candidates  
✔ Save results in structured formats (CSV/JSON)

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| NLP | spaCy, NLTK, Transformer Embeddings |
| ML | Cosine Similarity, Vectorization |
| UI | Streamlit (optional) |
| Deployment | N/A |

---

## 📁 Project Structure

```

Resume-Screening-Automation/
├── data/
│   ├── resumes/
│   └── job_descriptions/
├── src/
│   ├── preprocessing.py
│   ├── vectorizer.py
│   ├── similarity.py
│   └── ranking.py
├── requirements.txt
├── LICENSE
└── README.md

````

---

## 💡 How It Works

1. **Resume Ingestion**  
   Load candidate resumes from a folder (PDF/DOCX/TXT).

2. **Text Extraction & Preprocessing**  
   Convert resume content to plain text and clean for processing.

3. **Job Requirement Input**  
   Provide the job description or criteria for role.

4. **Embedding & Vectorization**  
   Transform both resumes and job description into numerical vectors.

5. **Similarity Scoring**  
   Compute similarity scores between job requirement and each resume.

6. **Ranking & Output**  
   Rank candidates based on scores and export results.

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/Adarshthakur-850/Resume-Screening-Automation.git
cd Resume-Screening-Automation
````

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

## ▶ Usage

1. Place resumes in `data/resumes/`
2. Edit the job description in the script or supply dynamically
3. Run the resume screening script:

```bash
python main.py
```

For interactive UI (if included):

```bash
streamlit run app.py
```

---

## 📊 Output

The tool generates:

* Ranked list of candidates
* Similarity scores for each resume
* Exportable results (CSV/JSON)

---

## 🧪 Sample Results

| Candidate       | Score |
| --------------- | ----- |
| John_Doe.pdf    | 0.87  |
| Jane_Smith.docx | 0.76  |
| Alex_Kumar.pdf  | 0.68  |

---

## 🧩 Customizing

You can extend this project by:

* Adding transformer-based embeddings (BERT / Sentence-BERT)
* Building a web UI
* Integrating with ATS systems
* Adding database storage for persistent candidate data

---

## ▶ Deployment Tips

* Use Docker for environment reproducibility
* Deploy UI using Streamlit Cloud or Heroku
* Schedule batch resume tests

---

## 📝 License

This project is released under the **MIT License**.

---

## 🙌 Acknowledgements

Thanks to open-source NLP libraries and community contributions.

---

### ✨ Made with ❤️ by **Adarsh Thakur**


📍 LinkedIn: [https://www.linkedin.com/in/adarsh-thakur-8368](https://www.linkedin.com/in/adarsh-thakur-8368)

📍 GitHub: [https://github.com/Adarshthakur-850](https://github.com/Adarshthakur-850)
