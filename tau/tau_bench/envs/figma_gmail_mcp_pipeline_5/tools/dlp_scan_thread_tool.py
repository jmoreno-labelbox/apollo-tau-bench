from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DlpScanThreadTool(Tool):
    """Examine a thread's messages for DLP block patterns based on config; returns detected patterns."""

    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        if not thread_id:
            payload = {"error": "thread_id is required"}
            out = json.dumps(payload)
            return out

        dlp = _get_config_json(data, "dlp_config")
        patterns = dlp.get("block_patterns", []) if isinstance(dlp, dict) else []
        messages = data.get("gmail_messages", {}).values()
        found: set[str] = set()
        for m in messages.values():
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            for p in patterns:
                if isinstance(p, str) and p.lower() in body:
                    found.add(p)
        payload = {"thread_id": thread_id, "blocked_terms_found": sorted(found)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DlpScanThread",
                "description": "Scan thread messages for DLP block patterns from system config.",
                "parameters": {
                    "type": "object",
                    "properties": {"thread_id": {"type": "string"}},
                    "required": ["thread_id"],
                },
            },
        }
