import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "role_skill_catalog.json")) as f:
        role_skill_catalog_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "skill_gap_analysis.json")) as f:
        skill_gap_analysis_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "goals.json")) as f:
        goals_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "soft_skills.json")) as f:
        soft_skills_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "industry_trends.json")) as f:
        industry_trends_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "talent_network.json")) as f:
        talent_network_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "hr_workflows.json")) as f:
        hr_workflows_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "job_applications.json")) as f:
        job_applications_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "job_postings.json")) as f:
        job_postings_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "career_path_graph.json")) as f:
        career_path_graph_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "team_training_log.json")) as f:
        team_training_log_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_mentorship_relationships.json")) as f:
        user_mentorship_relationships_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "users.json")) as f:
        users_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_course_progress.json")) as f:
        user_course_progress_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "teams.json")) as f:
        teams_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "mentorship_strategies.json")) as f:
        mentorship_strategies_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_preferences.json")) as f:
        user_preferences_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "job_market_insights.json")) as f:
        job_market_insights_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "learning_providers.json")) as f:
        learning_providers_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_mentorship.json")) as f:
        user_mentorship_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_certification.json")) as f:
        user_certification_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_education.json")) as f:
        user_education_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "course_catalog.json")) as f:
        course_catalog_data = json.load(f)

    return {
        "role_skill_catalog": role_skill_catalog_data,
        "skill_gap_analysis": skill_gap_analysis_data,
        "goals": goals_data,
        "soft_skills": soft_skills_data,
        "industry_trends": industry_trends_data,
        "talent_network": talent_network_data,
        "hr_workflows": hr_workflows_data,
        "job_applications": job_applications_data,
        "job_postings": job_postings_data,
        "career_path_graph": career_path_graph_data,
        "team_training_log": team_training_log_data,
        "user_mentorship_relationships": user_mentorship_relationships_data,
        "users": users_data,
        "user_course_progress": user_course_progress_data,
        "teams": teams_data,
        "mentorship_strategies": mentorship_strategies_data,
        "user_preferences": user_preferences_data,
        "job_market_insights": job_market_insights_data,
        "learning_providers": learning_providers_data,
        "user_mentorship": user_mentorship_data,
        "user_certification": user_certification_data,
        "user_education": user_education_data,
        "course_catalog": course_catalog_data
    }
