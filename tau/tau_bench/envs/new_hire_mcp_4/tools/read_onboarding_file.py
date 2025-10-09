from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReadOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_path: str) -> str:
        for f in data.get("onboarding_files", []):
            if f.get("file_path") == file_path:
                payload = {"file": f}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"file_path {file_path} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReadOnboardingFile",
                "description": "Read an onboarding file by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }
