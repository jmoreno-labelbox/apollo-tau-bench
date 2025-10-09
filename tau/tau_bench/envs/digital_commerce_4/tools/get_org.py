from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOrg(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        orgs = data.get("salesforce_orgs", {}).values()
        org = next((o for o in orgs.values() if o.get("org_id") == org_id), None)
        payload = org or {"error": f"org {org_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getOrg",
                "description": "Retrieve Salesforce org metadata (including org_name) by org_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }
