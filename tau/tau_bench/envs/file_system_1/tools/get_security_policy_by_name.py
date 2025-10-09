from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetSecurityPolicyByName(Tool):
    """Fetches a particular security policy using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], policy_name: str = None) -> str:
        for policy in data.get("security_policies", []):
            if policy.get("name") == policy_name:
                payload = policy
                out = json.dumps(payload)
                return out
        payload = {"error": f"Security policy named '{policy_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSecurityPolicyByName",
                "description": "Fetches an entire security policy document by its name (e.g., 'SSH Access Policy').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "policy_name": {
                            "type": "string",
                            "description": "The name of the security policy.",
                        }
                    },
                    "required": ["policy_name"],
                },
            },
        }
