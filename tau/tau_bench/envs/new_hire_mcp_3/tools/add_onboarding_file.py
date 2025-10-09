from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file: dict = None, candidate_id: Any = None, file_name: str = None, file_path: str = None) -> str:
        new_file = file or {}
        files = data.get("onboarding_files", {}).values()
        data["onboarding_files"][new_file["onboarding_file_id"]] = new_file
        data["onboarding_files"] = files
        payload = {"added_file": new_file}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddOnboardingFile",
                "description": "Add a new onboarding file.",
                "parameters": {
                    "type": "object",
                    "properties": {"file": {"type": "object"}},
                    "required": ["file"],
                },
            },
        }
