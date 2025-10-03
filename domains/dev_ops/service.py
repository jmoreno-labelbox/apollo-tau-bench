import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool


class DevOpsSystem(BaseDomain):
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            # Core User Management
            "users",
            "teams",
            "team_members",
            "projects",

            # Source Code Management
            "repositories",
            "branches",
            "commits",
            "pull_requests",

            # Work Item Management
            "work_items",
            "work_item_links",
            "labels",
            "work_item_labels",

            # CI/CD Pipeline Management
            "environments",
            "pipelines",
            "pipeline_stages",
            "jobs",
            "runners",
            "artifacts",
            "test_runs",

            # Deployment Management
            "deployments",
            "releases",
            "rollbacks",

            # Security & Compliance
            "vulnerabilities",
            "policies",
            "approvals",
            "compliance",

            # Monitoring & Observability
            "alerts",
            "metrics",
            "logs",

            # Infrastructure & Configuration
            "configurations",
            "secret_management",
            "dependencies",
            "backups",

            # Shared Utilities
            "notifications",

            # Game Development Workflow Automation Tables
            "automation_runs",
            "ownership_map",
            "test_results",
            "build_runs",
            "source_changes",
            "bisect_results",
            "fix_proposals",
            "incident_history",
            "symbols",
            "asset_catalog",
            "asset_qa_results",
            "crash_events",
            "bug_deduplication",
            "bug_links",
            "loc_strings",
            "translations",
            "subtitle_timing",
            "localization_workflow",
            "tms_jobs",
        ]

        for table_name in table_files:
            file_path = data_path / f"{table_name}.json"
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        db[table_name] = json.loads(content)
                    else:
                        db[table_name] = []
            except FileNotFoundError:
                # Core tables that should always exist
                core_tables = [
                    "users", "teams", "projects", "repositories",
                    "environments", "pipelines", "deployments"
                ]
                if table_name in core_tables:
                    raise FileNotFoundError(f"Core data file not found: {file_path}")
                db[table_name] = []
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
                db[table_name] = []

        return db
