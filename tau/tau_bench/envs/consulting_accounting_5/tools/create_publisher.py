from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str, name: str, address: str = "", contact_email: str = "", gst_number: str = "") -> str:
        """
        Creates a new publisher and adds it to the publishers.json data.
        """
        new_publisher = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": "2024-08-08T12:00:00",
            "updated_at": "2024-08-08T12:00:00",
        }
        data["publishers"][publisher_id] = new_publisher
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
