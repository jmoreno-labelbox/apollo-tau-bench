from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetFvpTimestamps(Tool):
    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {
            "started_ts": "2024-03-17T10:20:00Z",
            "finished_ts_nullable": "2024-03-17T10:25:00Z",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getFvpTimestamps",
                "description": "Returns canonical started_ts and finished_ts_nullable for FVP.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
