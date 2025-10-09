from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], assignment_id: str = None) -> str:
        assignments = data.get("license_assignments", {}).values()
        assignment = next(
            (a for a in assignments.values() if a.get("assignment_id") == assignment_id), None
        )
        if not assignment:
            payload = {"error": f"Assignment {assignment_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        assignment["status"] = "revoked"
        assignment["revoked_at"] = FIXED_NOW
        payload = assignment
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeLicense",
                "description": "Revoke a user's license by updating its status. Does not check inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignment_id": {"type": "string"}},
                    "required": ["assignment_id"],
                },
            },
        }
