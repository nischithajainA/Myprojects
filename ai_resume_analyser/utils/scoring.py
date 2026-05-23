def score_resume(skills_found, required_skills, experience, education):
    skill_score = (len(skills_found) / len(required_skills)) * 60
    exp_score = min(experience, 5) / 5 * 20
    edu_score = 20 if "master" in education else 10

    total = skill_score + exp_score + edu_score
    return round(total, 2)
