from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPolicyParameter(Tool):
    """Fetches the value associated with a specific business rule."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        for param in data.get("policy_params", []):
            if param.get("param_name") == param_name:
                payload = param
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy parameter '{param_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Retrieves the value of a specific business rule, like 'max_bid_amount'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {
                            "type": "string",
                            "description": "The name of the policy parameter to retrieve.",
                        }
                    },
                    "required": ["param_name"],
                },
            },
        }
