from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetPublisherInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Retrieves the full details for a given publisher_id.
        """
        publisher = next((p for p in data["publishers"].values() if p["publisher_id"] == publisher_id), None)
        return json.dumps(publisher)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetPublisherInfo",
                "description": "Retrieve full details for a given publisher ID.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "The ID of the publisher to retrieve"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }
