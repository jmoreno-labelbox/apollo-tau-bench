from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetThreadBySubject(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, sender_id: str = None, label: str = None) -> str:
        if not subject:
            payload = {"error": "Missing required field: subject"}
            out = json.dumps(payload, indent=2)
            return out

        threads: list[dict[str, Any]] = data.get("gmail_threads", {}).values()
        results: list[dict[str, Any]] = []
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
            payload = {"error": f"No thread found with subject '{subject}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"count": len(results), "threads": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetThreadBySubject",
                "description": "Return Gmail threads matching a subject. Optional filters: sender_id and label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "sender_id": {"type": "string"},
                        "label": {"type": "string"},
                    },
                    "required": ["subject"],
                },
            },
        }
