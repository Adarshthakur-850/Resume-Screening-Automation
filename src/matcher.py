from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def calculate_ranking(resumes_data, jd_text):
    """
    resumes_data: List of dicts [{'filename', 'raw_text', 'skills'}]
    jd_text: String
    """
    documents = [jd_text] + [r['raw_text'] for r in resumes_data]
    
    # TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Cosine Similarity (First doc is JD)
    # Compare JD (index 0) with all resumes (indices 1 to N)
    cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    results = []
    
    # JD Skills
    from src.extractor import extract_skills
    jd_skills = set(extract_skills(jd_text))
    
    for i, score in enumerate(cosine_sim):
        resume = resumes_data[i]
        res_skills = set(resume['skills'])
        
        # Skill Match Score
        if len(jd_skills) > 0:
            skill_match = len(jd_skills.intersection(res_skills)) / len(jd_skills)
        else:
            skill_match = 0
            
        # Weighted Final Score (70% Content Sim, 30% Skill Match)
        final_score = (score * 0.7) + (skill_match * 0.3)
        
        results.append({
            'Rank': 0, # Placeholder
            'Filename': resume['filename'],
            'Email': resume['email'],
            'Match_Score': round(final_score * 100, 2),
            'Cosine_Sim': round(score, 4),
            'Skill_Match': round(skill_match, 4),
            'Skills_Found': ", ".join(resume['skills'])
        })
        
    df = pd.DataFrame(results)
    df.sort_values(by='Match_Score', ascending=False, inplace=True)
    df['Rank'] = range(1, len(df) + 1)
    
    return df
