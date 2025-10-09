from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyOnboardingFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, file_path: str = None,
    candidate_id: Any = None,
    ) -> str:
        updates = updates or {}
        files = data.get("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path:
                f.update(updates)
                f["updated_at"] = _fixed_now_iso()
        payload = {"updated_file_path": file_path, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOnboardingFile",
                "description": "Update an onboarding file content or metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["file_path", "updates"],
                },
            },
        }
