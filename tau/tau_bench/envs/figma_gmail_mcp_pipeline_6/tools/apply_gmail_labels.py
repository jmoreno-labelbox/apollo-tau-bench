# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], thread_id: str, add_labels: List[str], remove_labels: List[str]) -> str:
        threads = data.get("gmail_threads", [])
        for thread in threads:
            if thread.get("thread_id") == thread_id:
                labels = set(thread.get("current_labels", []))
                labels.update(add_labels)
                labels.difference_update(remove_labels)
                thread["current_labels"] = list(labels)
                return json.dumps(thread, indent=2)
        return json.dumps({"error": f"Thread {thread_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "apply_gmail_labels",
            "description": "Apply or remove Gmail labels on a thread.",
            "parameters": {"type": "object","properties": {
                "thread_id": {"type": "string"},
                "add_labels": {"type": "array","items": {"type": "string"}},
                "remove_labels": {"type": "array","items": {"type": "string"}}
            },"required": ["thread_id"]}
        }}
