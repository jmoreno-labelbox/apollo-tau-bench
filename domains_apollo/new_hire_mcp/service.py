import json
from pathlib import Path
from typing import List, Dict, Any
import copy
from domains.base import BaseDomain
from domains.dto import Tool


class NewHireMCPSystem(BaseDomain):
    """
    Domain service for new hire onboarding and management system.
    Handles candidate onboarding workflows, asset provisioning, access management,
    email communications, and checklist tracking.
    """

    def __init__(self, tools: List[Tool]):
        super().__init__(tools)
        self.master_database = self._load_data()
        # self.database = self.master_database.copy()
        self.database = copy.deepcopy(self.master_database)

    def reset_database(self):
        # self.database = self.master_database.copy()
        self.database = copy.deepcopy(self.master_database)
        return True

    def _load_data(self) -> Dict[str, Any]:
        """
        Loads all new hire MCP data tables from their JSON files.
        """
        db = {}
        data_path = Path(__file__).parent / "data"

        table_files = [
            "candidates",
            "asset_requests", 
            "inventory_assets",
            "access_checks",
            "checklist_items",
            "emails",
            "attachments",
            "email_labels",
            "onboarding_files"
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
                db[table_name] = []
            except json.JSONDecodeError:
                db[table_name] = []
        return db
