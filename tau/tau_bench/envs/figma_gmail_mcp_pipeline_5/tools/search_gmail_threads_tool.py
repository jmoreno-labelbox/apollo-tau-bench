from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchGmailThreadsTool(Tool):
    """Look for Gmail threads using label, participant, or topic keyword."""

    @staticmethod
    def invoke(data: dict[str, Any], label: str = None, participant: str = None, keyword: str = None) -> str:
        threads = data.get("gmail_threads", {}).values()
        out = []
        for t in threads:
            if label and label not in (t.get("current_labels") or []):
                continue
            if participant:
                ps = (t.get("participants") or []) + (t.get("recipients") or [])
                if participant not in ps:
                    continue
            if keyword and keyword.lower() not in (t.get("subject", "").lower()):
                continue
            out.append(
                _small_fields(
                    t, ["thread_id", "subject", "current_labels", "updated_ts"]
                )
            )
        out.sort(key=lambda r: r.get("thread_id", ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchGmailThreads",
                "description": "Search Gmail threads by label, participant, or subject keyword.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label": {"type": "string"},
                        "participant": {"type": "string"},
                        "keyword": {"type": "string"},
                    },
                },
            },
        }
