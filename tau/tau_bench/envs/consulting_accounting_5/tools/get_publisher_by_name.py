# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPublisherByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_name) -> str:
        """
        Returns publisher_id for a given publisher name.
        """
        name = publisher_name
        pub = next((p for p in data["publishers"] if p["name"] == name), None)
        return json.dumps(pub["publisher_id"] if pub else None)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPublisherByName",
                "description": "Retrieve publisher_id for a given publisher name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_name": {"type": "string", "description": "Exact publisher name to look up"}
                    },
                    "required": ["publisher_name"],
                },
            },
        }
