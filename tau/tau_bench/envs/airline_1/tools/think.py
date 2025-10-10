# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Think(Tool):
    """
    A tool for the agent to log its reasoning process without taking an action.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], thought: str) -> str:
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
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
                            "description": "The thought process to be logged."
                        }
                    },
                    "required": ["thought"]
                }
            }
        }
