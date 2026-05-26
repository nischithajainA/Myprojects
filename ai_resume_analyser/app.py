from flask import render_template, Flask, request
from utils.extract import extract_text_from_docx,extract_text_from_pdf
from utils.similarity import cal_similarity
from utils.llm_analyser import analyse_resume

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
        
    #Similarity
    similarity_score = cal_similarity(
        resume_text,
        jd_text
    )
    # llmfeedback
    llm_feedback = analyse_resume(resume_text,jd_text)
    
    return render_template(
        "result.html",
        similarity_score=round(similarity_score * 100, 2),
        llm_feedback = llm_feedback
    )
    

if __name__ == "__main__":
    app.run(debug = True)
    
