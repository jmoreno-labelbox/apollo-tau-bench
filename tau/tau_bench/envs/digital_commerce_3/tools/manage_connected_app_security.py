# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one


class ManageConnectedAppSecurity(Tool):
    """Manage connected app security settings and OAuth scopes."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        app_id: Any,
        permissions: Any = ["read", "write"],
        oauth_scopes: Any = ["api", "refresh_token"],
    ) -> str:
        app_id = _idstr(app_id)
        permissions = list(permissions or [])
        oauth_scopes = list(oauth_scopes or [])

        if not app_id:
            return _error("app_id is required.")

        apps = data.setdefault("connected_apps", [])
        app = _find_one(apps, "app_id", app_id)
        if not app:
            app = {
                "app_id": app_id,
                "app_name": f"App_{app_id}",
                "client_secret_stored": True,
                "disabled": False,
                "oauth_scopes": [],
                "permissions": [],
            }
            apps.append(app)

        app["permissions"] = permissions
        app["oauth_scopes"] = oauth_scopes
        app["disabled"] = False
        app["client_secret_stored"] = True

        result = {
            "app_id": app_id,
            "app_name": app.get("app_name"),
            "permissions": permissions,
            "oauth_scopes": oauth_scopes,
            "disabled": app.get("disabled"),
            "client_secret_stored": app.get("client_secret_stored"),
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_connected_app_security",
                "description": "Manage connected app security settings, permissions and OAuth scopes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_id": {"type": "string"},
                        "permissions": {"type": "array", "items": {"type": "string"}},
                        "oauth_scopes": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["app_id"],
                },
            },
        }
