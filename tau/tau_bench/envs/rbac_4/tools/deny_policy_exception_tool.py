from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DenyPolicyExceptionTool(Tool):
    """Reject a policy exception request."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None, reviewed_on: str = None) -> str:
        for e in data.get("policy_exceptions", {}).values():
            if e["exception_id"] == exception_id:
                e["status"] = "DENIED"
                e["reviewed_by"] = reviewed_by
                e["reviewed_on"] = reviewed_on
                payload = {"success": f"Exception {exception_id} denied"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Exception {exception_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DenyPolicyException",
                "description": "Deny a pending policy exception request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reviewed_on": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewed_by", "reviewed_on"],
                },
            },
        }
