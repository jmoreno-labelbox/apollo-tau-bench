# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetThreadBySubject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("subject"):
            return json.dumps({"error": "Missing required field: subject"}, indent=2)

        subject = kwargs.get("subject")
        sender_id: Optional[str] = kwargs.get("sender_id")
        label: Optional[str] = kwargs.get("label")

        threads: List[Dict[str, Any]] = data.get("gmail_threads", [])
        results: List[Dict[str, Any]] = []
        for row in threads:
            if row.get("subject") != subject:
                continue
            if sender_id and row.get("sender_identity") != sender_id:
                continue
            if label and label not in (row.get("current_labels") or []):
                continue
            results.append(row)

        results.sort(key=lambda r: str(r.get("thread_id")))
        if not results:
            return json.dumps({"error": f"No thread found with subject '{subject}'"}, indent=2)
        return json.dumps({"count": len(results), "threads": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_thread_by_subject",
                "description": "Return Gmail threads matching a subject. Optional filters: sender_id and label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "label": {"type": "string"}
                    },
                    "required": ["subject"]
                }
            }
        }
