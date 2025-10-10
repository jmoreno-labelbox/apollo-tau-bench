# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchAdSetsByName(Tool):
    """Searches for ad sets with names containing the specified text."""

    @staticmethod
    def invoke(data: Dict[str, Any], name_query) -> str:
        adsets = list(data.get("adsets", {}).values())
        matching_adsets = []
        
        for adset in adsets:
            if name_query.lower() in adset.get("name", "").lower():
                matching_adsets.append(adset.get("adset_id"))
        
        return json.dumps({"adset_ids": matching_adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_adsets_by_name",
                "description": "Searches for ad sets with names containing the specified text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_query": {
                            "type": "string",
                            "description": "The text to search for in ad set names.",
                        }
                    },
                    "required": ["name_query"],
                },
            },
        }
