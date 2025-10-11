# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table
def _slugify(text: str, max_len: int = 40) -> str:
    s = str(text).lower()
    out = []
    prev_dash = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_dash = False
        else:
            if not prev_dash:
                out.append("-")
                prev_dash = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug[:max_len] if max_len > 0 else slug

def _stable_id(prefix: str, *parts: str) -> str:
    base = "-".join(_slugify(p) for p in parts if p is not None and str(p) != "")
    return f"{prefix}-{base}" if base else prefix

def _json(x: Any) -> str:
    return json.dumps(x, separators=(",", ":"))

def _find_one(rows: List[Dict[str, Any]], ):
    crit_items = sorted(crit.items(), key=lambda kv: kv[0])
    for r in rows:
        match = True
        for k, v in crit_items:
            if str(r.get(k)) != str(v):
                match = False
                break
        if match:
            return r
    return None

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class ConfigureConnectedAppOAuth(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], app_name_hint: str, scopes: List[str], callback_urls: List[str]
    ) -> str:
        apps = _ensure_table(data, "connected_apps")
        app_id = _stable_id("app", app_name_hint)
        row = _find_one(apps, app_id=app_id)
        client_id = _stable_id("client", app_name_hint)
        secret_arn = f"arn:aws:secretsmanager:local:000000000000:secret:{app_id}"
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
        return _json({"app_id": app_id, "client_id": client_id, "secret_arn": secret_arn})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_connected_app_oauth",
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