def build_prompt(resume_context, jd_text, user_query):
    resume_text = "\n".join(resume_context)

    return f"""
You are an AI resume reviewer.

JOB DESCRIPTION:
{jd_text}

RESUME CONTENT:
{resume_text}

USER QUESTION:
{user_query}

TASK:
1. Identify missing skills
2. Suggest improvements
3. Rewrite weak resume bullet points
4. Keep feedback concise and actionable
"""
