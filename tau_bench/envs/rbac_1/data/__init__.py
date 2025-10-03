import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # auto-generated from files present in data/
    tables = ['access_requests', 'audit_logs', 'certifications', 'emails', 'hubspot_tickets', 'permissions', 'policy_exceptions', 'resources', 'role_permissions', 'roles', 'sessions', 'siem_alerts', 'slack_messages', 'user_roles', 'users']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

