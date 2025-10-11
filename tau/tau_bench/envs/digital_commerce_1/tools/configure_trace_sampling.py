# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table










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

class ConfigureTraceSampling(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sample_rate: float) -> str:
        flags = _ensure_table(data, "trace_flags")
        policy_id = _stable_id("trace", f"{sample_rate:.2f}")
        row = _find_one(flags, policy_id=policy_id)
        if row:
            row["sample_rate"] = float(sample_rate)
            row["created_at"] = FIXED_NOW
        else:
            flags.append(
                {"policy_id": policy_id, "sample_rate": float(sample_rate), "created_at": FIXED_NOW}
            )
        return _json({"policy_id": policy_id, "effective_rate": float(sample_rate)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_trace_sampling",
                "description": "Configure API trace sampling rate globally.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sample_rate": {"type": "number", "minimum": 0.0, "maximum": 1.0}
                    },
                    "required": ["sample_rate"],
                },
            },
        }