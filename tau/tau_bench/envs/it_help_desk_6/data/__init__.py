import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from files located in data/
    tables = ['app_accounts', 'backlog_snapshot_open', 'daily_metrics', 'data_archives', 'device_workflow', 'directory_accounts', 'employees', 'group_membership_audit', 'hr_memos', 'it_assets', 'jira_tickets', 'license_assignments', 'license_inventory', 'lifecycle_audit', 'lifecycle_queue', 'mailboxes', 'rbac_group_map', 'report_runs', 'tickets', 'validation_issues']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

