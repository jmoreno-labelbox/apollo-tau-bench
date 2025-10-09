from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateArchiveStatusTool(Tool):
    """Modifies the status of a task in the archive_instructions database."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateArchiveStatus",
                "description": "Finds an archive instruction by its 'archive_id' and updates its 'status' field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {
                            "type": "string",
                            "description": "The ID of the archive task to update (e.g., 'arch_001').",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status to set (e.g., 'completed', 'failed').",
                        },
                    },
                    "required": ["archive_id", "status"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], archive_id: str = None, status: str = None) -> str:
        archive_task = next(
            (
                t
                for t in data.get("archive_instructions", [])
                if t.get("archive_id") == archive_id
            ),
            None,
        )
        if archive_task:
            archive_task["status"] = status
            payload = {"status": "success", "archive_id": archive_id, "new_status": status}
            out = json.dumps(payload)
            return out
        payload = {"error": f"Archive ID {archive_id} not found."}
        out = json.dumps(payload)
        return out
