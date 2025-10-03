from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CreateResearchLog(Tool):
    """Utility for generating a research log entry for a researcher regarding an article."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: Any = None, article_id: Any = None, notes: Any = None, relevance: Any = None, log_id_override: Any = None) -> str:
        if not all([researcher_id, article_id, notes, relevance]):
            payload = {
                    "error": "researcher_id, article_id, notes, and relevance are required."
                }
            out = json.dumps(
                payload)
            return out

        log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        new_log = {
            "log_id": log_id,
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": datetime.now().strftime("%Y-%m-%d"),
            "notes": notes,
            "relevance": relevance,
        }
        data["research_logs"].append(new_log)
        payload = {"success": True, "log_entry": new_log}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResearchLog",
                "description": "Creates a personal research log or note for a researcher about a specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {
                            "type": "string",
                            "description": "The user ID of the researcher creating the log.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article the log is about.",
                        },
                        "notes": {
                            "type": "string",
                            "description": "The content of the research note.",
                        },
                        "relevance": {
                            "type": "string",
                            "description": "A relevance score (e.g., 'high', 'medium', 'low').",
                        },
                        "log_id_override": {
                            "type": "string",
                            "description": "Optional specific ID for the log entry.",
                        },
                    },
                    "required": ["researcher_id", "article_id", "notes", "relevance"],
                },
            },
        }
