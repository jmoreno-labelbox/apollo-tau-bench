import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['career_path_graph', 'course_catalog', 'goals', 'hr_workflows', 'industry_trends', 'job_applications', 'job_market_insights', 'job_postings', 'learning_providers', 'mentorship_strategies', 'role_skill_catalog', 'skill_gap_analysis', 'soft_skills', 'talent_network', 'team_training_log', 'teams', 'user_certification', 'user_course_progress', 'user_education', 'user_mentorship', 'user_mentorship_relationships', 'user_preferences', 'users']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

