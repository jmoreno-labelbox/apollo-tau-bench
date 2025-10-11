# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCurrentTimeTool(Tool):
    """get_current_time: returns deterministic timestamp used across writes."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"timestamp": _HARD_TS}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Return deterministic current time used for writes.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
