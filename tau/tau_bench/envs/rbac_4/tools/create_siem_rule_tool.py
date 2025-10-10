# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSiemRuleTool(Tool):
    """Create a new SIEM correlation rule."""

    @staticmethod
    def invoke(data: Dict[str, Any], conditions, created_by, rule_name) -> str:
        rules = data.get("siem_rules", [])
        new_id = f"RULE-{len(rules) + 1:03d}"
        rules.append({
            "rule_id": new_id,
            "rule_name": rule_name,
            "conditions": conditions,
            "created_by": created_by
        })
        return json.dumps({"success": f"SIEM rule {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_siem_rule",
                "description": "Create and store a new rule in SIEM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "conditions": {"type": "object"},
                        "created_by": {"type": "string"}
                    },
                    "required": ["rule_name", "conditions", "created_by"]
                }
            }
        }
