import json
import os
from typing import Any, Dict

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> Dict[str, Any]:
    with open(os.path.join(FOLDER_PATH, "articles.json")) as f:
        articles_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "users.json")) as f:
        users_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "research_logs.json")) as f:
        research_logs_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "citations.json")) as f:
        citations_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "submissions.json")) as f:
        submissions_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "reviews.json")) as f:
        reviews_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "projects.json")) as f:
        projects_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "funding_sources.json")) as f:
        funding_sources_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "notifications.json")) as f:
        notifications_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "subscriptions.json")) as f:
        subscriptions_data = json.load(f)
    with open(os.path.join(FOLDER_PATH, "user_preferences.json")) as f:
        user_preferences_data = json.load(f)
    return {
        "articles": articles_data,
        "users": users_data,
        "research_logs": research_logs_data,
        "citations": citations_data,
        "submissions": submissions_data,
        "reviews": reviews_data,
        "projects": projects_data,
        "funding_sources": funding_sources_data,
        "notifications": notifications_data,
        "subscriptions": subscriptions_data,
        "user_preferences": user_preferences_data
    }
