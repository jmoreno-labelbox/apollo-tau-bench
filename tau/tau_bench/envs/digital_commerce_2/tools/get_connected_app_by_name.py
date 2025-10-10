# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetConnectedAppByName(Tool):
    """Fetch a connected app by exact app_name within a given org_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], org_id: Any, app_name: Any) -> str:
        if not org_id or not app_name:
            return json.dumps({"error": "Missing required field: org_id and/or app_name"}, indent=2)
        apps = list(data.get("connected_apps", {}).values())
        for app in apps:
            if app.get("org_id") == org_id and app.get("app_name") == app_name:
                return json.dumps(app, indent=2)
        return json.dumps(
            {"error": f"Connected app not found for org_id={org_id}, app_name={app_name}"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_connected_app_by_name",
                "description": "Resolve a connected app by app_name within the specified org_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "app_name": {"type": "string"},
                    },
                    "required": ["org_id", "app_name"],
                },
            },
        }
