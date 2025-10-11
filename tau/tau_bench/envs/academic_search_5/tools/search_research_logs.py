# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchResearchLogs(Tool):
    """Tool to search research logs."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, researcher_id) -> str:

        if not researcher_id and not article_id:
            return json.dumps({"error": "Either researcher_id or article_id is required."})

        logs = list(data.get('research_logs', {}).values())
        results = [
            log for log in logs
            if (not researcher_id or log.get('researcher_id') == researcher_id)
            and (not article_id or log.get('article_id') == article_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_research_logs",
                "description": "Searches research logs by researcher or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {"type": "string", "description": "The user ID of the researcher."},
                        "article_id": {"type": "string", "description": "The ID of the article."}
                    }
                }
            }
        }
