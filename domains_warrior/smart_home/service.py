import json
from pathlib import Path
from typing import List, Dict, Any

from domains.base import BaseDomain
from domains.dto import Tool

import copy

class SmartHomeSystem(BaseDomain):
    """
    Domain service for a smart home.
    Manages the state of devices, users, and home settings.
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
            "custom_lists", "devices", "rooms", "scenes", "reminders", "members", "sensors",
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
