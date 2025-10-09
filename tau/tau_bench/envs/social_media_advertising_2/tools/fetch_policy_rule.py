from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchPolicyRule(Tool):
    """Retrieve a business rule parameter using its name (compatible with policy_params and policy_rules)."""

    @staticmethod
    def invoke(data: dict[str, Any], rule_name: str = None) -> str:
        target = rule_name
        sources = []
        if isinstance(data.get("policy_params"), list):
            sources.extend(data["policy_params"])
        if isinstance(data.get("policy_rules"), list):
            sources.extend(data["policy_rules"])

        for row in sources:
            key = row.get("param_name")
            if key == target:
                val = (
                    row.get("value") if "value" in row else row.get("param_value", None)
                )
                payload = {"name": key, "value": val}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy rule {target} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPolicyRule",
                "description": "Look up a business rule parameter by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                    },
                    "required": ["rule_name"],
                },
            },
        }
