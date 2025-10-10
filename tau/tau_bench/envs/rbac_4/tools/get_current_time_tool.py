# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCurrentTimeTool(Tool):
    """
    Returns the fixed canonical current time used in evaluation.
    """

    @staticmethod
    def invoke(data: dict, **kwargs) -> str:
        # consistently provide the identical standard time
        return json.dumps({"current_time": "2025-08-17T00:00:00Z"})

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Return the canonical current time for use in audit logs and decisions.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
