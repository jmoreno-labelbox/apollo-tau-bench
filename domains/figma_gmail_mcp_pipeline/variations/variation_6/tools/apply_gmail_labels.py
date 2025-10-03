from tau_bench.envs.tool import Tool
import json
from typing import Any

class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        thread_id: str,
        add_labels: list[str],
        remove_labels: list[str],
    ) -> str:
        threads = data.get("gmail_threads", [])
        for thread in threads:
            if thread.get("thread_id") == thread_id:
                labels = set(thread.get("current_labels", []))
                labels.update(add_labels)
                labels.difference_update(remove_labels)
                thread["current_labels"] = list(labels)
                payload = thread
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Thread {thread_id} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyGmailLabels",
                "description": "Apply or remove Gmail labels on a thread.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "add_labels": {"type": "array", "items": {"type": "string"}},
                        "remove_labels": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["thread_id"],
                },
            },
        }
