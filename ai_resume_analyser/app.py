from flask import render_template, Flask, request
from utils.extract import extract_text_from_docx,extract_text_from_pdf
from utils.nlp import extract_skills,extract_experience,extract_education
from utils.scoring import score_resume
from utils.skills_list import SKILLS

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods =["POST"])
def analyze():
    file = request.files["resume"]
    if file.filename.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file)
    elif file.filename.endswith(".docx"):
        resume_text = extract_text_from_docx(file)  
    else:
        return "Unsupported file type"    
     
    # Extract JD text (optional)
    jd_file = request.files.get("jd")
    jd_text_input = request.form.get("jd_text") 
     
    jd_text = ""
    if jd_file and jd_file.filename:
        if jd_file.filename.endswith(".pdf"):
            jd_text = extract_text_from_pdf(jd_file)
        elif jd_file.filename.endswith(".docx"):
            jd_text = extract_text_from_docx(jd_file)
    elif jd_text_input:
        jd_text = jd_text_input 
        
         
    resume_skills = extract_skills(resume_text)
    resume_experience = extract_experience(resume_text)
    resume_education = extract_education(resume_text)
    
    jd_skills = extract_skills(jd_text)
    jd_experience = extract_experience(jd_text)
    jd_education = extract_education(jd_text)

    resume_score = score_resume(resume_skills, SKILLS, resume_experience, resume_education)
    
    matched = set(resume_skills) & set(jd_skills)
    
    # resume_set = {s.lower().strip() for s in resume_skills}
    # jd_set = {s.lower().strip() for s in jd_skills}
    missing_skills = set(jd_skills) - set(resume_skills) 
    # missing_skills = [s for s in jd_skills if s.lower().strip() not in resume_skills]

    jd_match_percent = round((len(matched) / len(jd_skills)) * 100, 2) if jd_skills else 0


    return render_template(
        "result.html",
        skills=resume_skills,
        experience=resume_experience,
        education=resume_education,
        score=resume_score,
        jd_skills = jd_skills,
        jd_match_percent = jd_match_percent,
        missing_skills = missing_skills,
        matched =matched
    )


if __name__ == "__main__":
    app.run(debug = True)
    
