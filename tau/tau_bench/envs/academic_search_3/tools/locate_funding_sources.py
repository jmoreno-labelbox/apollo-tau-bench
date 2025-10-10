# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LocateFundingSources(Tool):
    """Tool to locate funding sources by research area and availability status."""
    @staticmethod
    def invoke(data: Dict[str, Any], area = '', status = '') -> str:
        sources = list(data.get('funding_sources', {}).values())
        results = []
        area = area.lower()
        status = status.lower()

        for s in sources:
            match_area = area in s.get('focus_area', '').lower()
            match_status = True
            if status:
                match_status = status == s.get('status', '').lower()

            if match_area and match_status:
                results.append(s)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "locate_funding_sources", "description": "Locates funding sources by research area and availability.", "parameters": {"type": "object", "properties": {
            "area": {"type": "string", "description": "The research area (e.g., 'AI', 'Medical Research')."},
            "status": {"type": "string", "description": "The availability status of the grant (e.g., 'available')."}
        }, "required": []}}}
