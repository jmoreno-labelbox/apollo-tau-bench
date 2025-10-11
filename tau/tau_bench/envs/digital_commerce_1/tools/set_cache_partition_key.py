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

class SetCachePartitionKey(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], partition_key: str, version: str) -> str:
        settings = _ensure_table(data, "custom_settings")
        name = "CacheAPI.ExternalSystemPartitionKeyVersion"
        row = _find_one(settings, name=name)
        if row:
            row["value"] = version
            row["updated_at"] = FIXED_NOW
        else:
            settings.append(
                {
                    "setting_id": _stable_id("cs", name),
                    "name": name,
                    "value": version,
                    "updated_at": FIXED_NOW,
                }
            )
        return _json({"applied_version": version})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_cache_partition_key",
                "description": "Set the cache partition key version.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "partition_key": {"type": "string"},
                        "version": {"type": "string"},
                    },
                    "required": ["partition_key", "version"],
                },
            },
        }