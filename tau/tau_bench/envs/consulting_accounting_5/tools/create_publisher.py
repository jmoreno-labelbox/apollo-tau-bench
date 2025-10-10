# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Creates a new publisher and adds it to the publishers.json data.
        """
        new_publisher = {
            "publisher_id": kwargs["publisher_id"],
            "name": kwargs["name"],
            "address": kwargs.get("address", ""),
            "contact_email": kwargs.get("contact_email", ""),
            "gst_number": kwargs.get("gst_number", ""),
            "created_at": "2024-08-08T12:00:00",
            "updated_at": "2024-08-08T12:00:00",
        }
        data["publishers"].append(new_publisher)
        return json.dumps(new_publisher["publisher_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "CreatePublisher",
                "description": "Create a new publisher record.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "Unique ID for the new publisher"},
                        "name": {"type": "string", "description": "Name of the new publisher"}
                    },
                    "required": ["publisher_id", "name"],
                },
            },
        }
