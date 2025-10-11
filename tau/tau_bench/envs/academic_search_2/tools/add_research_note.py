# Copyright Sierra

import uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddResearchNote(Tool):
    """Creates a new entry in the research_logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, log_id_override, notes, researcher_id, relevance = 'medium') -> str:
        researcher_id, article_id, notes = researcher_id, article_id, notes
        if not all([researcher_id, article_id, notes]):
            return json.dumps({"error": "researcher_id, article_id, and notes are required."})
        new_log = {
            "log_id": log_id_override if log_id_override else f"log_{uuid.uuid4().hex[:4]}",
            "researcher_id": researcher_id,
            "article_id": article_id,
            "entry_date": "2025-06-24",
            "notes": notes,
            "relevance": relevance
        }
        list(data.get('research_logs', {}).values()).append(new_log)
        return json.dumps({"success": True, "log_entry": new_log}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_research_note", "description": "Creates a new entry in the research_logs.", "parameters": {"type": "object", "properties": {"researcher_id": {"type": "string"}, "article_id": {"type": "string"}, "notes": {"type": "string"}, "relevance": {"type": "string"}, "log_id_override": {"type": "string"}}, "required": ["researcher_id", "article_id", "notes"]}}}
