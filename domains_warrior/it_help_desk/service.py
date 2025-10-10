import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool

class ITHelpDeskSystem(BaseDomain):
    """
    Domain service for an IT Help Desk system.
    Manages the state of employees, tickets, IT assets, and other related data.
    """
    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        """
        Loads all data tables from their JSON files.
        """
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "app_accounts",
            "backlog_snapshot_open",
            "daily_metrics",
            "data_archives",
            "device_workflow",
            "directory_accounts",
            "employees",
            "group_membership_audit",
            "hr_memos",
            "it_assets",
            "jira_tickets",
            "license_assignments",
            "license_inventory",
            "lifecycle_audit",
            "lifecycle_queue",
            "mailboxes",
            "rbac_group_map",
            "report_runs",
            "tickets",
            "validation_issues",
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
                if table_name in table_files:
                     raise FileNotFoundError(f"Core data file not found: {file_path}.")
                db[table_name] = []
            except json.JSONDecodeError:
                db[table_name] = []
        return db
