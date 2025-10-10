# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCurrentTime(Tool):
    """ Returns a fixed current date and time formatted as "YYYY-MM-DD HH:MM:SS+00:00". e.g. "2025-08-09 10:00:00+00:00" """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Format the datetime as "YYYY-MM-DD HH:MM:SS+00:00"
        formatted_time = NOW.isoformat(timespec='seconds').replace("T", " ")
        return json.dumps({"current_time": formatted_time})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Returns the current date and time as YYYY-MM-DD HH:MM:SS+00:00",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }
