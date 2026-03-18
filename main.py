import os
import pandas as pd
from src.parser import extract_text
from src.extractor import extract_resume_data
from src.matcher import calculate_ranking

# --- Data Gen Utils for Demo ---
def create_dummy_data():
    if not os.path.exists("data"):       os.makedirs("data")
    if not os.path.exists("data/resumes"): os.makedirs("data/resumes")
    if not os.path.exists("data/job_description"): os.makedirs("data/job_description")
    
    jd = """
    Job Title: Senior Data Scientist
    Responsibilities: Build ML models, NLP systems.
    Skills Required: Python, Machine Learning, NLP, Pandas, Scikit-learn, SQL, AWS, Docker.
    Experience: 5+ years.
    """
    with open("data/job_description/jd.txt", "w") as f: f.write(jd)
    
    resumes = {
        "candidate_A.txt": "Experienced Data Scientist with 6 years in Python, Machine Learning, and NLP. Skilled in Pandas, Scikit-learn. Contact: alice@example.com",
        "candidate_B.txt": "Junior Developer with knowledge of Java, C++, and some Python. Loves coding. Contact: bob@test.com",
        "candidate_C.txt": "Senior ML Engineer expert in Python, AWS, Docker, Kubernetes, and Deep Learning. Strong SQL skills. Contact: charlie@ml.org",
        "candidate_D.txt": "Marketing Manager with 10 years experience. Good communication skills. No coding. Contact: dave@marketing.com",
        "candidate_E.txt": "Fresh grad with Python, SQL, and Tableau skills. Eager to learn Machine Learning. Contact: eve@uni.edu"
    }
    
    for name, text in resumes.items():
        with open(f"data/resumes/{name}", "w") as f: f.write(text)

# --- Main Pipeline ---
def main():
    print("Initializing...")
    create_dummy_data()
    
    # 1. Load JD
    try:
        jd_path = "data/job_description/jd.txt"
        with open(jd_path, 'r') as f:
            jd_text = f.read()
    except:
        print("JD not found.")
        return

    # 2. Process Resumes
    resumes_dir = "data/resumes"
    processed_resumes = []
    
    print(f"Scanning {resumes_dir}...")
    for filename in os.listdir(resumes_dir):
        filepath = os.path.join(resumes_dir, filename)
        
        # Parse
        text = extract_text(filepath)
        if not text: continue
        
        # Extract Info
        data = extract_resume_data(text)
        data['filename'] = filename
        
        processed_resumes.append(data)
        
    print(f"Processed {len(processed_resumes)} resumes.")
    
    # 3. Rank
    print("Ranking candidates...")
    ranking_df = calculate_ranking(processed_resumes, jd_text)
    
    # 4. Output
    if not os.path.exists("output"): os.makedirs("output")
    output_path = "output/ranking_report.csv"
    ranking_df.to_csv(output_path, index=False)
    
    print("\nTop Candidates:")
    print(ranking_df[['Rank', 'Filename', 'Match_Score', 'Skills_Found']].head().to_string(index=False))
    print(f"\nReport saved to {output_path}")

if __name__ == "__main__":
    main()
