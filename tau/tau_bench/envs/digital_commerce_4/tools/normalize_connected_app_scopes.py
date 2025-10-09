from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class NormalizeConnectedAppScopes(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_id: str,
        connected_apps: list = None
    ) -> str:
        app_id = _sid(app_id)
        apps = connected_apps if connected_apps is not None else data.get("connected_apps", [])
        app = next((a for a in apps if a.get("app_id") == app_id), None)
        if not app:
            payload = {"error": f"app {app_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        scopes = app.get("oauth_scopes")
        if isinstance(scopes, str):
            vals = [s.strip() for s in scopes.split(",")]
            scopes_list = [v for v in vals if v]
        elif isinstance(scopes, list):
            scopes_list = scopes
        else:
            scopes_list = []
        for r in ["api", "refresh_token"]:
            if r not in scopes_list:
                scopes_list.append(r)
        app["oauth_scopes"] = scopes_list
        _ws_append(data, app_id, "NORMALIZE_APP_SCOPES", {"oauth_scopes": scopes_list})
        _append_audit(
            data, "NORMALIZE_APP_SCOPES", app_id, {"oauth_scopes": scopes_list}
        )
        payload = app
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeConnectedAppScopes",
                "description": "Normalize a connected app's oauth_scopes to a list and enforce required scopes.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_id": {"type": "string"}},
                    "required": ["app_id"],
                },
            },
        }
