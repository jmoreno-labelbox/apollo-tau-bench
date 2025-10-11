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

def _ensure_table(db: Dict[str, Any], name: str):
    if name not in db:
        db[name] = []
    return db[name]

class RecordApiChangeLog(Tool):
    @staticmethod
    def invoke(data, target_id: str, environment: str, change_type: str = "ops") -> str:
        cases = _ensure_table(data, "cases")
        change_log_id = _stable_id("chg", change_type, target_id, environment, FIXED_NOW)
        title = f"{change_type.capitalize()} – {target_id} [{environment}]"
        cases.append(
            {
                "case_id": change_log_id,
                "title": title,
                "status": "Recorded",
                "created_at": FIXED_NOW,
            }
        )
        return _json({"change_log_id": change_log_id, "title": title, "timestamp": FIXED_NOW})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "record_api_change_log",
                "description": "Record an API change event. Defaults change_type='ops'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {"type": "string"},
                        "environment": {"type": "string", "enum": ["DEV", "UAT", "PROD"]},
                        "change_type": {"type": "string"},
                    },
                    "required": ["target_id", "environment"],
                },
            },
        }