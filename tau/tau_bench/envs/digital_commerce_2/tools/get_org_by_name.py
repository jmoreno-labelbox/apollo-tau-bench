# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOrgByName(Tool):
    """Fetch a Salesforce org by exact org_name (e.g., 'UAT', 'Production')."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_name: Any) -> str:
        if not org_name:
            return json.dumps({"error": "Missing required field: org_name"}, indent=2)
        orgs = list(data.get("salesforce_orgs", {}).values())
        for org in orgs:
            if org.get("org_name") == org_name:
                return json.dumps(org, indent=2)
        return json.dumps({"error": f"Org not found: {org_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_org_by_name",
                "description": "Resolve a Salesforce org by org_name ('UAT', 'Production'). Returns the org record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_name": {"type": "string"},
                    },
                    "required": ["org_name"],
                },
            },
        }
