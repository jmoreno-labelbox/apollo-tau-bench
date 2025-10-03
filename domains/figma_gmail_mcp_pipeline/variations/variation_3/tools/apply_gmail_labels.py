from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, add_labels: list = None, remove_labels: list = None, request_id: str = None, timestamp: str = None) -> str:
        p = _params(data, {"thread_id": thread_id, "add_labels": add_labels, "request_id": request_id})
        miss = _require(p, ["thread_id", "add_labels", "request_id"])
        if miss:
            return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                labels = set(t.get("labels", []))
                for lab in p.get("add_labels", []):
                    labels.add(lab)
                t["labels"] = list(labels)
                return _ok({"labels": t["labels"]})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyGmailLabels",
                "description": "Apply one or more labels to a Gmail thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "add_labels": {"type": "array", "items": {"type": "string"}},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["thread_id", "add_labels", "request_id"],
                },
            },
        }
