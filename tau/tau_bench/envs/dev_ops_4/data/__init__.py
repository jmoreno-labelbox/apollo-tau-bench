import json
import os
from typing import Any

FOLDER_PATH = os.path.dirname(__file__)

def load_data() -> dict[str, Any]:
    db: dict[str, Any] = {}
    # automatically created from files located in data/
    tables = ['alerts', 'approvals', 'artifacts', 'asset_catalog', 'asset_qa_results', 'automation_runs', 'backups', 'bisect_results', 'branches', 'bug_deduplication', 'bug_links', 'build_runs', 'commits', 'compliance', 'configurations', 'crash_events', 'dependencies', 'deployments', 'environments', 'fix_proposals', 'incident_history', 'jobs', 'labels', 'loc_strings', 'localization_workflow', 'logs', 'metrics', 'notifications', 'ownership_map', 'pipeline_stages', 'pipelines', 'policies', 'projects', 'pull_requests', 'releases', 'repositories', 'rollbacks', 'runners', 'secret_management', 'source_changes', 'subtitle_timing', 'symbols', 'team_members', 'teams', 'test_results', 'test_runs', 'tms_jobs', 'translations', 'users', 'vulnerabilities', 'work_item_labels', 'work_item_links', 'work_items']
    for name in tables:
        path = os.path.join(FOLDER_PATH, f"{name}.json")
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                db[name] = json.loads(content) if content else []
        except FileNotFoundError:
            db[name] = []
    return db

