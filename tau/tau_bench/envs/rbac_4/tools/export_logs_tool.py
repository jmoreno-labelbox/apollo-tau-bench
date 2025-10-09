from tau_bench.envs.tool import Tool
import json
from typing import Any

class ExportLogsTool(Tool):
    """Export logs in CSV or JSON format for the specified time range."""

    @staticmethod
    def invoke(data: dict[str, Any], format: str = None, start_time: Any = None, end_time: Any = None) -> str:
        logs = [l for l in data.get("audit_logs", []) if start_time <= l["timestamp"] <= end_time]
        if not format or not isinstance(format, str) or format.upper() not in ["CSV", "JSON"]:
            payload = {"error": "Invalid format"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"format": format, "logs": logs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportLogs",
                "description": "Export logs to CSV or JSON format from given date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "format": {"type": "string", "enum": ["CSV", "JSON"]},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                    },
                    "required": ["format", "start_time", "end_time"],
                },
            },
        }
