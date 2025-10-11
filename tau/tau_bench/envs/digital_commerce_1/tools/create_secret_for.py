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

def _find_one(rows: List[Dict[str, Any]], **crit):
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

class CreateSecretFor(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], environment: str, purpose: str, value_source_id: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        key = f"secret:{purpose}:{environment}"
        kms_key_alias = f"alias/dcomm-{environment.lower()}"
        secret_arn = _stable_id("arn:secret", key, value_source_id, kms_key_alias)
        row = _find_one(settings, name=key)
        payload = {"source": value_source_id, "kms": kms_key_alias, "arn": secret_arn}
        if row:
            row.update({"value": json.dumps(payload), "updated_at": FIXED_NOW})
        else:
            settings.append(
                {
                    "setting_id": _stable_id("sec", key),
                    "name": key,
                    "value": json.dumps(payload),
                    "created_at": FIXED_NOW,
                }
            )
        return _json({"secret_arn": secret_arn})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "create_secret_for",
                "description": "Create/rotate a secret using deterministic naming by environment and purpose.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "purpose": {
                            "type": "string",
                            "enum": ["REDIS_AUTH_HEADER", "OAUTH_CLIENT_SECRET", "API_AUTH_HEADER"],
                        },
                        "value_source_id": {"type": "string"},
                    },
                    "required": ["environment", "purpose", "value_source_id"],
                },
            },
        }