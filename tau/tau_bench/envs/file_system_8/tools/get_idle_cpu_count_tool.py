# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetIdleCpuCountTool(Tool):
    """Simulates checking server CPU usage to find the number of idle cores."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_idle_cpu_count",
                "description": "Gets the total number of idle CPU cores to use for parallel processing. Simulates using 'top' and 'awk'. Returns a fixed value for determinism.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Return a fixed number for deterministic behavior.
        return json.dumps({"idle_cpus": 6})
