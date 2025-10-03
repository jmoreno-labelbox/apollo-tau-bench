from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetConnectedAppSecurity(Tool):
    """Obtain security settings for connected apps using app_id."""

    @staticmethod
    def invoke(data: dict[str, Any], app_id: Any) -> str:
        app_id = _idstr(app_id)
        if not app_id:
            return _error("app_id is required.")
        apps = data.get("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            return _error(f"Connected app '{app_id}' not found.")
        payload = app
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetConnectedAppSecurity",
                "description": "Fetch connected app security configuration by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_id": {"type": "string"}},
                    "required": ["app_id"],
                },
            },
        }
