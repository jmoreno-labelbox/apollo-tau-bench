from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_figma_comments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, resolved_flag: bool = None) -> str:
        p = _params(data, {"artifact_id": artifact_id, "resolved_flag": resolved_flag})
        rows = []
        for c in _ensure(data, "figma_comments", []):
            if p.get("artifact_id") and c.get("artifact_id") != p["artifact_id"]:
                continue
            if "resolved_flag" in p and bool(c.get("resolved_flag", False)) != bool(
                p["resolved_flag"]
            ):
                continue
            rows.append(c)
        return _ok({"rows": rows})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listFigmaComments",
                "description": "List comments for a Figma artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "resolved_flag": {"type": "boolean"},
                    },
                },
            },
        }
