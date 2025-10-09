from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class verify_single_thread_per_cycle(Tool):
    def invoke(data: dict[str, Any], cycle_id: str = None) -> str:
        p = _params(data, {"cycle_id": cycle_id})
        miss = _require(p, ["cycle_id"])
        if miss:
            return miss
        for c in _ensure(data, "review_cycles", []):
            if c.get("cycle_id") == p["cycle_id"]:
                ok = c.get("thread_id_nullable") is not None
                return _ok({"ok": ok, "cycle_id": c["cycle_id"]})
        return _ok({"ok": False, "cycle_id": p["cycle_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verifySingleThreadPerCycle",
                "description": "Verify each cycle has exactly one attached thread (simplified).",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
