from tau_bench.envs.tool import Tool
import json
from typing import Any

class FetchBullpenSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        date_range = kwargs.get("date_range")
        kwargs.get("normalize_metrics", True)
        payload = {"bullpen_session_data": f"sessions_{date_range}"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchBullpenSessions",
                "description": "Fetches recent bullpen session data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date_range": {"type": "string"},
                        "normalize_metrics": {"type": "boolean"},
                    },
                    "required": ["date_range"],
                },
            },
        }
