# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCurrentTimestamp(Tool):
    """Returns a hardcoded current timestamp value."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"timestamp": "2025-08-13T01:01:01Z"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_timestamp",
                "description": "Returns a hardcoded current timestamp value (2025-08-13T01:01:01Z).",
                "parameters": {},
            },
        }
