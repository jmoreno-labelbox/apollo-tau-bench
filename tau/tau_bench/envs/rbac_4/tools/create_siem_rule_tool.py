from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateSiemRuleTool(Tool):
    """Establish a new SIEM correlation rule."""

    @staticmethod
    def invoke(data: dict[str, Any], rule_name: str = None, conditions: Any = None, created_by: str = None,
    created_on: Any = None,
    notes: str = None
    ) -> str:
        rules = data.get("siem_rules", {}).values()
        new_id = f"RULE-{len(rules) + 1:03d}"
        rules.append(
            {
                "rule_id": new_id,
                "rule_name": rule_name,
                "conditions": conditions,
                "created_by": created_by,
            }
        )
        payload = {"success": f"SIEM rule {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemRule",
                "description": "Create and store a new rule in SIEM",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "conditions": {"type": "object"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["rule_name", "conditions", "created_by"],
                },
            },
        }
