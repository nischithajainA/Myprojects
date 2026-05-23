import re
from utils.skills_list import SKILLS

def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS if skill.lower().strip() in text_lower]
def extract_experience(text):
    match = re.search(r'(\d+)\+?\s+years', text.lower())
    return int(match.group(1)) if match else 0

def extract_education(text):
    degrees = ["bachelor", "master", "phd", "diploma"]
    found = [d for d in degrees if d in text.lower()]
    return found
