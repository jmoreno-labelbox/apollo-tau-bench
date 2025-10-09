from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateSubnetGroupDescription(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], subnet_group_id: Any, name: Any, description: Any
    ) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        g = next(
            (x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        if not g:
            return _err("Subnet group not found.")
        g["name"] = str(name)
        g["description"] = str(description)
        payload = {
            "subnet_group_id": subnet_group_id,
            "name": g["name"],
            "description": g["description"],
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSubnetGroupDescription",
                "description": "Rename a subnet group and update its description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "name", "description"],
                },
            },
        }
