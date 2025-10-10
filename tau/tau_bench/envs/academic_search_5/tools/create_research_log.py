# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateResearchLog(Tool):
    """Tool to create a research log entry for a researcher about an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        researcher_id = kwargs.get('researcher_id')
        article_id = kwargs.get('article_id')
        notes = kwargs.get('notes')
        relevance = kwargs.get('relevance')
        log_id_override = kwargs.get('log_id_override')

        if not all([researcher_id, article_id, notes, relevance]):
            return json.dumps({"error": "researcher_id, article_id, notes, and relevance are required."})

        log_id = log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}"
        new_log = {
            "log_id": log_id,
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": datetime.now().strftime('%Y-%m-%d'),
            "notes": notes,
            "relevance": relevance
        }
        data['research_logs'].append(new_log)
        return json.dumps({"success": True, "log_entry": new_log})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_research_log",
                "description": "Creates a personal research log or note for a researcher about a specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string", "description": "The user ID of the researcher creating the log."},
                        "article_id": {"type": "string", "description": "The ID of the article the log is about."},
                        "notes": {"type": "string", "description": "The content of the research note."},
                        "relevance": {"type": "string", "description": "A relevance score (e.g., 'high', 'medium', 'low')."},
                        "log_id_override": {"type": "string", "description": "Optional specific ID for the log entry."}
                    },
                    "required": ["researcher_id", "article_id", "notes", "relevance"]
                }
            }
        }
