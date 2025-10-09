from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigureConnectedAppOAuth(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_name_hint: str,
        scopes: list[str],
        callback_urls: list[str]
    ) -> str:
        apps = _ensure_table(data, "connected_apps")
        app_id = _stable_id("app", app_name_hint)
        row = _find_one(apps, app_id=app_id)
        client_id = _stable_id("client", app_name_hint)
        secret_arn = f"arn:aws:secretsmanager:local:000000000000:secret:{app_id}"
        payload = {
            "name": app_name_hint,
            "scopes": list(scopes),
            "callbacks": list(callback_urls),
        }
        if row:
            row.update(
                {
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            apps.append(
                {
                    "app_id": app_id,
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "created_at": FIXED_NOW,
                }
            )
        return _json(
            {"app_id": app_id, "client_id": client_id, "secret_arn": secret_arn}
        )
        pass
        apps = _ensure_table(data, "connected_apps")
        app_id = _stable_id("app", app_name_hint)
        row = _find_one(apps, app_id=app_id)
        client_id = _stable_id("client", app_name_hint)
        secret_arn = f"arn:aws:secretsmanager:local:000000000000:secret:{app_id}"
        payload = {
            "name": app_name_hint,
            "scopes": list(scopes),
            "callbacks": list(callback_urls),
        }
        if row:
            row.update(
                {
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "updated_at": FIXED_NOW,
                }
            )
        else:
            apps.append(
                {
                    "app_id": app_id,
                    "name": app_name_hint,
                    "scopes": list(scopes),
                    "callback_urls": list(callback_urls),
                    "client_id": client_id,
                    "secret_arn": secret_arn,
                    "created_at": FIXED_NOW,
                }
            )
        return _json(
            {"app_id": app_id, "client_id": client_id, "secret_arn": secret_arn}
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureConnectedAppOauth",
                "description": "Configure connected app OAuth scopes and callbacks.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_name_hint": {"type": "string"},
                        "scopes": {"type": "array", "items": {"type": "string"}},
                        "callback_urls": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["app_name_hint", "scopes", "callback_urls"],
                },
            },
        }
