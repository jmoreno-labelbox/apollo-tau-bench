# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetViewershipForCategory(Tool):
    """Retrieves user engagement data for a category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category, report_date = kwargs.get("category"), kwargs.get("date")
        for record in data.get('f_viewership', []):
            if record.get('category') == category and record.get('date') == report_date:
                return json.dumps(record)
        return json.dumps({"error": "Viewership data not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_viewership_for_category", "description": "Retrieves user session and engagement data for a category on a specific date.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}, "date": {"type": "string"}}, "required": ["category", "date"]}}}
