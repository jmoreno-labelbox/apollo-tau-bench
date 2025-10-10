import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from files located in data/
    tables = ['audit_events', 'brokers', 'calendar_events', 'campaigns', 'client_preferences', 'comp_reports', 'comparables', 'documents', 'emails', 'lenders', 'listings', 'mortage_profiles', 'mortgage_rates', 'neighborhoods', 'open_houses', 'routes', 'sales']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

