from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class GetIdleCpuCountTool(Tool):
    """Emulates the process of checking server CPU usage to determine the number of idle cores."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetIdleCpuCount",
                "description": "Gets the total number of idle CPU cores to use for parallel processing. Simulates using 'top' and 'awk'. Returns a fixed value for determinism.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }

    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {"idle_cpus": 6}
        out = json.dumps(payload)
        return out
