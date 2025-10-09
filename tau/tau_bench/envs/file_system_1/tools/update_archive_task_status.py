from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateArchiveTaskStatus(Tool):
    """Modifies the status of an archival task within the instructions database."""

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None, status: str = None) -> str:
        for instruction in data.get("archive_instructions", []):
            if instruction.get("archive_id") == archive_id:
                instruction["status"] = status
                payload = {"status": "success", "updated_task": instruction}
                out = json.dumps(payload)
                return out
        payload = {"status": "failure", "error": f"Archive ID '{archive_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArchiveTaskStatus",
                "description": "Updates the status of an archive task (e.g., 'in_progress', 'completed', 'failed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["in_progress", "completed", "failed", "verified"],
                        },
                    },
                    "required": ["archive_id", "status"],
                },
            },
        }
