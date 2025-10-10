import json
from pathlib import Path
from typing import List, Dict, Any
import copy

from domains.base import BaseDomain
from domains.dto import Tool


class FileSystemDomain(BaseDomain):
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
            "user_preferences",
            "user_contacts",
            "file_check_db",
            "task_instructions",
            "file_check_logs",
            "directories",
            "file_lists",
            "archive_instructions",
            "remote_servers",
            "slack_channels",
            "slack_messages",
            "task_logs",
            "error_logs",
            "file_system",
            "tmux_sessions",
            "completion_messages",
            "error_messages",
            "ssh_keys",
            "system_resources",
            "security_policies"
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
                raise FileNotFoundError(f"Core data file not found: {file_path}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from {file_path}: {e}")
                db[table_name] = []

        return db
