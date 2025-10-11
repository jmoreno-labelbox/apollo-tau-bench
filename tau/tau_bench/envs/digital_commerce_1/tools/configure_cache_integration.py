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

class ConfigureCacheIntegration(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], external_url: str, auth_header_secret_arn: str, partition_key: Optional[str] = None
    ) -> str:
        settings = _ensure_table(data, "custom_settings")

        def _upsert(name: str, value: str):
            row = _find_one(settings, name=name)
            if row:
                row["value"] = value
                row["updated_at"] = FIXED_NOW
            else:
                settings.append(
                    {
                        "setting_id": _stable_id("cs", name),
                        "name": name,
                        "value": value,
                        "updated_at": FIXED_NOW,
                    }
                )

        _upsert("CacheAPI.ExternalSystemURL", external_url)
        _upsert("CacheAPI.ExternalSystemAuthHeader", auth_header_secret_arn)
        if partition_key:
            _upsert("CacheAPI.ExternalSystemPartitionKey", partition_key)
        return _json(
            {
                "setting_ids": [
                    "CacheAPI.ExternalSystemURL",
                    "CacheAPI.ExternalSystemAuthHeader",
                    *([
                        "CacheAPI.ExternalSystemPartitionKey",
                    ] if partition_key else []),
                ],
                "verified": True,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_cache_integration",
                "description": "Point Commerce to the external cache (URL/auth/partition key).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "external_url": {"type": "string"},
                        "auth_header_secret_arn": {"type": "string"},
                        "partition_key": {"type": "string", "description": "Optional, uses default value if omitted."},
                    },
                    "required": ["external_url", "auth_header_secret_arn"],
                },
            },
        }