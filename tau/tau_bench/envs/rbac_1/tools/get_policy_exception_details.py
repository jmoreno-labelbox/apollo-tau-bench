from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetPolicyExceptionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        for ex in data.get("policy_exceptions", {}).values():
            if ex.get("exception_id") == exception_id:
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionDetails",
                "description": "Retrieves details for a specific policy exception.",
                "parameters": {
                    "type": "object",
                    "properties": {"exception_id": {"type": "string"}},
                    "required": ["exception_id"],
                },
            },
        }
