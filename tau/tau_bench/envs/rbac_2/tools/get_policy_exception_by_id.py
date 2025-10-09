from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPolicyExceptionById(Tool):
    """Retrieve complete details of a specific policy exception by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", [])
        except:
            policy_exceptions = []

        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                payload = exc
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy exception with ID '{exception_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionById",
                "description": "Retrieves the full details of a specific policy exception using its unique ID (e.g., 'PE-010').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The unique ID of the policy exception to retrieve.",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }
