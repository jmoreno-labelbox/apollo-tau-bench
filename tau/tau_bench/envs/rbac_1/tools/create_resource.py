from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, owner_id: str = None, criticality: str = None, compliance_scope: str = None) -> str:
        resources = data.get("resources", {}).values()
        new_id_num = max((int(r["resource_id"][4:]) for r in resources.values()), default=0) + 1
        new_resource_id = f"RES-{new_id_num:03d}"
        new_resource = {
            "resource_id": new_resource_id,
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }
        data["resources"][resource_id] = new_resource
        data["resources"] = resources
        payload = new_resource
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResource",
                "description": "Creates a new resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner_id": {"type": "string"},
                        "criticality": {"type": "string"},
                        "compliance_scope": {"type": "string"},
                    },
                    "required": ["name", "owner_id", "criticality"],
                },
            },
        }
