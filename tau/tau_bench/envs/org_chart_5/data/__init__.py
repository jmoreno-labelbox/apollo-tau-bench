import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from files located in data/
    tables = ['benefits_plan', 'company_doc', 'compensation_records', 'departments', 'employee_doc', 'employees', 'ethnicity_codes', 'job_levels', 'leave_records', 'performance_reviews', 'positions']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

