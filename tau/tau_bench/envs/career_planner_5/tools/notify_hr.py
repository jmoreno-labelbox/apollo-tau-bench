# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class notify_hr(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message: str) -> str:
        data.setdefault("hr_notifications", []).append({"message": message})
        return json.dumps({"notified": "HR", "message": message})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "notify_hr",
                "description": "Send an informational notification to the HR team.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
