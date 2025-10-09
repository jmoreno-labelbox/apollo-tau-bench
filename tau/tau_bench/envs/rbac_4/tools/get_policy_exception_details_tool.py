from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPolicyExceptionDetailsTool(Tool):
    """Provide the complete stored record for a specified policy exception (excluding error payloads)."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        pass
        eid = exception_id
        for e in data.get("policy_exceptions", []) or []:
            if e.get("exception_id") == eid:
                payload = e
                out = json.dumps(payload, indent=2)
                return out
        #Not located → return empty object to prevent '"error":' keys from triggering validators
        return "{}"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionDetails",
                "description": "Return the full stored policy-exception record for the given ID.",
                "parameters": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "e.g., PE-007",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }
