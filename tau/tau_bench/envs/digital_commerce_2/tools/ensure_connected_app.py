# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnsureConnectedApp(Tool):
    """Ensure a connected app exists for an org; create if missing, upsert scopes deterministically."""

    @staticmethod
    def invoke(
        data: Dict[str, Any], org_id: Any, app_name: Any, client_id: Any, oauth_scopes: Any
    ) -> str:
        if not org_id or not app_name or not client_id or oauth_scopes is None:
            return json.dumps(
                {"error": "Missing required fields: org_id, app_name, client_id, oauth_scopes"},
                indent=2,
            )
        if not isinstance(oauth_scopes, list):
            return json.dumps({"error": "oauth_scopes must be a list"}, indent=2)

        apps = data.setdefault("connected_apps", [])
        for app in apps:
            if app.get("org_id") == org_id and app.get("app_name") == app_name:
                merged = sorted(set(app.get("oauth_scopes", []) + oauth_scopes))
                app["client_id"] = client_id
                app["client_secret_stored"] = True
                app["oauth_scopes"] = merged
                return json.dumps(app, indent=2)

        next_id = str(max([int(a.get("app_id")) for a in apps] + [200]) + 1)
        record = {
            "app_id": next_id,
            "org_id": org_id,
            "app_name": app_name,
            "client_id": client_id,
            "client_secret_stored": True,
            "oauth_scopes": sorted(set(oauth_scopes)),
        }
        apps.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_connected_app",
                "description": "Ensure a connected app exists with given client_id and scopes; create if missing; returns the app record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "org_id": {"type": "string"},
                        "app_name": {"type": "string"},
                        "client_id": {"type": "string"},
                        "oauth_scopes": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["org_id", "app_name", "client_id", "oauth_scopes"],
                },
            },
        }
