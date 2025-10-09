from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddResearchNote(Tool):
    """Adds a new record in the research_logs."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: str = None, article_id: str = None, notes: str = None, relevance: str = "medium", log_id_override: Any = None) -> str:
        if not all([researcher_id, article_id, notes]):
            payload = {"error": "researcher_id, article_id, and notes are required."}
            out = json.dumps(payload)
            return out
        new_log = {
            "log_id": (
                log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
            ),
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": "2025-06-24",
            "notes": notes,
            "relevance": relevance,
        }
        data.get("research_logs", []).append(new_log)
        payload = {"success": True, "log_entry": new_log}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddResearchNote",
                "description": "Creates a new entry in the research_logs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "notes": {"type": "string"},
                        "relevance": {"type": "string"},
                        "log_id_override": {"type": "string"},
                    },
                    "required": ["researcher_id", "article_id", "notes"],
                },
            },
        }
