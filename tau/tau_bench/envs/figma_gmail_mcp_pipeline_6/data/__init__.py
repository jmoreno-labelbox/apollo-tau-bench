import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from the files located in data/
    tables = ['assets', 'audit_findings_a11y', 'audit_findings_ds', 'audits', 'figma_artifacts', 'figma_comments', 'fix_items', 'fix_plans', 'gmail_messages', 'gmail_threads', 'release_diffs', 'releases', 'review_approvals', 'review_cycles', 'system_config', 'terminal_logs']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

