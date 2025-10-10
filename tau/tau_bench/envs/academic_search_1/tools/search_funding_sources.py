# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchFundingSources(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_name = kwargs.get('source_name')
        focus_area = kwargs.get('focus_area')
        status = kwargs.get('status')
        sources = list(data.get('funding_sources', {}).values())

        if not source_name and not focus_area and not status:
            return json.dumps(sources, indent=2)

        results = [
            s for s in sources
            if (not source_name or source_name.lower() in s.get('source_name', '').lower()) and
               (not focus_area or s.get('focus_area', '').lower() == focus_area.lower()) and
               (not status or s.get('status', '').lower() == status.lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_funding_sources",
                "description": "Searches for funding sources by name, focus area, or status. If no parameters are provided, it returns all sources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_name": {"type": "string", "description": "The name of the funding source to search for."},
                        "focus_area": {"type": "string", "description": "The focus area of the funding source (e.g., 'AI', 'Biomedicine')."},
                        "status": {"type": "string", "description": "The status of the funding source (e.g., 'available', 'depleted')."}
                    }
                }
            }
        }
