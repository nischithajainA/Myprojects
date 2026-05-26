from sentence_transformers  import util
from models.embedding_model import model

def cal_similarity(resume_text, job_text):
    resume_emd = model.encode(
        resume_text,
        convert_to_tensor = True
    )
    job_emd = model.encode(
        job_text,
        convert_to_tensor = True
    )
    similarity = util.cos_sim(
        resume_emd,
        job_emd
    )
    return float(similarity[0][0])