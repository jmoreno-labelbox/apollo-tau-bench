# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTimeEntryDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves the full details for a given time_entry_id.
        """
        time_entry_id = kwargs["time_entry_id"]
        entry = next((t for t in data["time_entries"] if t["time_entry_id"] == time_entry_id), None)
        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTimeEntryDetails",
                "description": "Retrieve the full details for a given time entry ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_entry_id": {"type": "string", "description": "The ID of the time entry to retrieve"}
                    },
                    "required": ["time_entry_id"],
                },
            },
        }
