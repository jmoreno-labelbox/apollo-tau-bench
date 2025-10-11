# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindGrants(Tool):
    """
    Tool to search for funding sources by various criteria, OR to get a single source's details by its ID.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], focus_area, funding_source_id, min_grant_amount, status) -> str:

        sources = list(data.get('funding_sources', {}).values())

        if funding_source_id:
            for source in sources:
                if source.get('funding_source_id') == funding_source_id:
                    return json.dumps(source, indent=2)
            return json.dumps({"error": f"Funding source with ID '{funding_source_id}' not found."})

        results = []
        for source in sources:
            area_match = not focus_area or focus_area.lower() in source.get('focus_area', '').lower()
            status_match = not status or status.lower() == source.get('status', '').lower()
            amount_match = not min_grant_amount or source.get('grant_amount', 0) >= int(min_grant_amount)

            if area_match and status_match and amount_match:
                results.append(source)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_grants",
                "description": "Searches for funding sources by criteria (focus area, status, amount), or retrieves a single source by its specific ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "funding_source_id": {"type": "string", "description": "The specific ID of the funding source to retrieve."},
                        "focus_area": {"type": "string", "description": "The research area the funding supports (e.g., 'AI')."},
                        "status": {"type": "string", "description": "The current status of the grant (e.g., 'available')."},
                        "min_grant_amount": {"type": "integer", "description": "The minimum amount of funding required."}
                    }
                }
            }
        }
