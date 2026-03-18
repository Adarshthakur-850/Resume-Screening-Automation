import re
import spacy

# Load SpaCy model (ensure python -m spacy download en_core_web_sm is run)
# We handle the import error gracefully for the demo if model isn't present
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

SKILL_DB = [
    'Python', 'Java', 'C++', 'SQL', 'HTML', 'CSS', 'JavaScript', 
    'React', 'Node.js', 'Machine Learning', 'Deep Learning', 'NLP', 
    'Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'PyTorch', 
    'AWS', 'Azure', 'Docker', 'Kubernetes', 'Git', 'Agile'
]

def extract_contact_info(text):
    email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
    
    return {
        'email': email[0] if email else None,
        'phone': phone[0] if phone else None
    }

def extract_skills(text):
    found_skills = []
    text_lower = text.lower()
    
    # Simple dictionary matching
    for skill in SKILL_DB:
        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text_lower):
            found_skills.append(skill)
            
    # SpaCy Entity Extraction (Optional enhancement)
    if nlp:
        doc = nlp(text)
        # Could extract ORG, PERSON, etc.
        
    return list(set(found_skills))

def extract_resume_data(text):
    return {
        **extract_contact_info(text),
        'skills': extract_skills(text),
        'raw_text': text
    }
