from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckWorkflowExistsForChangeRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cr_id: str = None) -> str:
        if not cr_id:
            payload = {"error": "cr_id is required"}
            out = json.dumps(payload)
            return out

        approval_workflows = data.get("approval_workflows", {}).values()

        existing = next(
            (w for w in approval_workflows.values() if w.get("cr_id") == cr_id), None
        )
        if existing:
            payload = {"success": True, "exists": True}
            out = json.dumps(payload)
            return out
        payload = {"success": True, "exists": False}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckWorkflowExistsForChangeRequest",
                "description": "Check if a workflow exists for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                    },
                    "required": ["cr_id"],
                },
            },
        }
