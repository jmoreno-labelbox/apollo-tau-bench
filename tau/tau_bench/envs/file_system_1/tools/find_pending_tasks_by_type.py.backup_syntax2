from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindPendingTasksByType(Tool):
    """Identifies all outstanding tasks of a given type (e.g., 'archive', 'file_check')."""

    @staticmethod
    def invoke(data: dict[str, Any], task_type: str = None) -> str:
        pending_tasks = []
        if task_type == "archive":
            db = _convert_db_to_list(data.get("archive_instructions", {}).values())
            pending_tasks = [t for t in db.values() if t.get("status") == "pending"]
        elif task_type == "file_check":
            db = _convert_db_to_list(data.get("file_check_db", {}).values()
            pending_tasks = [t for t in db.values() if not t.get("completed")]
        elif task_type == "file_organization":
            db = _convert_db_to_list(data.get("file_lists", {}).values()
            op_ids = {f["operation_id"] for f in db if f.get("status") == "pending"}
            all_ops = data.get("directories", {}).values()
            pending_tasks = [op for op in all_ops.values() if op["operation_id"] in op_ids]
        payload = {"pending_tasks": pending_tasks, "count": len(pending_tasks)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findPendingTasksByType",
                "description": "Scans the databases for all tasks of a specific type that are in a 'pending' state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_type": {
                            "type": "string",
                            "enum": ["archive", "file_check", "file_organization"],
                        }
                    },
                    "required": ["task_type"],
                },
            },
        }
