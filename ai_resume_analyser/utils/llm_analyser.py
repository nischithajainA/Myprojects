import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyse_resume(resume_text, job_description):
    prompt = f"""
    you are an ATS resume evaluator.
    
    Analyse the following resume  against
    the given job description.
    
    Resume:
    {resume_text}
    
    Job Description:
    {job_description}
    
    Analyze carefully and provide detailed,
    specific, and actionable feedback.

    IMPORTANT RULES:

    1. Suggestions must be SPECIFIC to the resume.
    2. Do NOT give generic advice.
    3. Mention exact missing technologies,skills, or experience.
    4. Mention which resume sections need improvement.
    5. Suggest improvements using professional resume language.
    6. Explain WHY each suggestion matters for ATS.
    7. Suggest quantified resume bullet improvements.
    8. Compare candidate skills against JD requirements.

   IMPORTANT:
    Return ONLY valid JSON.
    Do not include markdown.
    Do not include explanations.
    Do not include ```json.
    Do not include extra text.

    Return this exact structure:

    {{
        "ats_score": 0,
        "matching_skills": [],
        "missing_skills": [],
        "strengths": [],
        "weaknesses": [],
        "detailed_suggestions": [],
        "improved_resume_bullets": [],
        "overall_evaluation": ""
    }}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    content = response.choices[0].message.content

    # Convert JSON string to Python dictionary
    result = json.loads(content)
    return result
