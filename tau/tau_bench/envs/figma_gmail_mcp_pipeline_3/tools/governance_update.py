from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class governance_update(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, request_id: str = None, add_tags: list = None, remove_tags: list = None, timestamp: str = None) -> str:
        p = _params(data, {
            "artifact_id": artifact_id,
            "request_id": request_id,
            "add_tags": add_tags,
            "remove_tags": remove_tags
        })
        miss = _require(p, ["artifact_id", "request_id"])
        if miss:
            return miss
        add = p.get("add_tags", [])
        rem = p.get("remove_tags", [])
        for a in _ensure(data, "figma_artifacts", []):
            if a.get("artifact_id") == p["artifact_id"]:
                tags = set(a.get("current_tags", []))
                for t in add:
                    tags.add(t)
                for t in rem:
                    if t in tags:
                        tags.remove(t)
                a["current_tags"] = list(tags)
                return _ok({"artifact_id": a["artifact_id"], "tags": a["current_tags"]})
        return _err("artifact_not_found", {"artifact_id": p["artifact_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GovernanceUpdate",
                "description": "Add/remove tags on an artifact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "add_tags": {"type": "array", "items": {"type": "string"}},
                        "remove_tags": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["artifact_id", "request_id"],
                },
            },
        }
