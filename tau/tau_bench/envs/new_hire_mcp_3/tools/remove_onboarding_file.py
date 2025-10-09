from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RemoveOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        files = data.get("onboarding_files", {}).values()
        data["onboarding_files"] = [f for f in files.values() if f.get("file_path") != file_path]
        payload = {"removed_file_path": file_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveOnboardingFile",
                "description": "Remove an onboarding file by file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }
