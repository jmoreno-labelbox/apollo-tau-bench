from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPolicyParameter(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        n = param_name
        for r in data.get("policy_params", []):
            if r.get("param_name") == n:
                payload = r
                out = json.dumps(payload)
                return out
        payload = {"error": f"policy {n} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Gets a single policy parameter.",
                "parameters": {
                    "type": "object",
                    "properties": {"param_name": {"type": "string"}},
                    "required": ["param_name"],
                },
            },
        }
