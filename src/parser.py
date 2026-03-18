import os

def extract_text(filepath):
    """
    Extracts text from a file. 
    Currently supports .txt. 
    Can be extended for .pdf using pdfplumber or .docx using python-docx.
    """
    try:
        ext = os.path.splitext(filepath)[1].lower()
        
        if ext == '.txt':
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
                
        # Placeholder for PDF/DOCX (To keep dependencies minimal for this demo execution)
        # if ext == '.pdf': ...
        
        return ""
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return ""
