# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one


class GetConnectedAppSecurity(Tool):
    """Fetch connected app security configuration by app_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], app_id: Any) -> str:
        app_id = _idstr(app_id)
        if not app_id:
            return _error("app_id is required.")
        apps = data.get("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            return _error(f"Connected app '{app_id}' not found.")
        return json.dumps(app, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_connected_app_security",
                "description": "Fetch connected app security configuration by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_id": {"type": "string"}},
                    "required": ["app_id"],
                },
            },
        }
