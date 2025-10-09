from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSubnetGroupDescription(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, new_description: Any) -> str:
        subnet_group_id = _idstr(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        for g in groups:
            if g.get("subnet_group_id") == subnet_group_id:
                g["description"] = new_description
                payload = g
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No subnet group found with ID '{subnet_group_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubnetGroupDescription",
                "description": "Set the description field on an AWS subnet group record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "new_description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "new_description"],
                },
            },
        }
