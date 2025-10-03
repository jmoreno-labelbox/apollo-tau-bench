from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class Think(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], thought: str) -> str:
        pass
        return ""
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "think",
                "description": "Allows the agent to think and document its reasoning process without altering data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thought": {
                            "type": "string",
                            "description": "The thought process to be logged.",
                        }
                    },
                    "required": ["thought"],
                },
            },
        }
