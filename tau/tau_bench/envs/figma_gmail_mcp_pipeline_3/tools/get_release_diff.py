from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class get_release_diff(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], release_id: str = None) -> str:
        p = _params(data, {"release_id": release_id})
        miss = _require(p, ["release_id"])
        if miss:
            return miss
        for r in _ensure(data, "releases", []):
            if r.get("release_id") == p["release_id"]:
                return _ok({"release_id": r["release_id"], "diff": r.get("diff", {}).values()})
        return _err("release_not_found", {"release_id": p["release_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReleaseDiff",
                "description": "Fetch a release diff summary.",
                "parameters": {
                    "type": "object",
                    "properties": {"release_id": {"type": "string"}},
                    "required": ["release_id"],
                },
            },
        }
