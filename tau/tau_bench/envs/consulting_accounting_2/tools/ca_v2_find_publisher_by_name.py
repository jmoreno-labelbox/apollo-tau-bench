# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2FindPublisherByName(Tool):
    """Find publisher by name."""

    @staticmethod
    def invoke(data: Dict[str, Any], publisher_name) -> str:
        name = publisher_name
        if not name:
            return _error("publisher_name is required.")
        publishers = data.get("publishers", [])
        publisher = _find_one(publishers, "name", name)
        return json.dumps(publisher) if publisher else _error(f"Publisher '{name}' not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_find_publisher_by_name",
                "description": "Find a publisher by their name.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_name": {"type": "string"}},
                    "required": ["publisher_name"],
                },
            },
        }
