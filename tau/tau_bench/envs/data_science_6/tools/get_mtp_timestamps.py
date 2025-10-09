from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetMtpTimestamps(Tool):
    def invoke(data: dict[str, Any], anything: Any = None) -> str:
        payload = {
            "started_ts": "2024-03-17T09:30:00Z",
            "finished_ts_nullable": "2024-03-17T11:15:00Z",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMtpTimestamps",
                "description": "Returns canonical started_ts and finished_ts for MTP.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
