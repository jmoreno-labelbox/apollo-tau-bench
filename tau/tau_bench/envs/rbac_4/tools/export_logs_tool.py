# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportLogsTool(Tool):
    """Export logs in CSV or JSON format within given time range."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        fmt = kwargs.get("format")
        start = kwargs.get("start_time")
        end = kwargs.get("end_time")
        logs = [l for l in data.get("audit_logs", []) if start <= l["timestamp"] <= end]
        if not fmt or not isinstance(fmt, str) or fmt.upper() not in ["CSV", "JSON"]:
            return json.dumps({"error": "Invalid format"}, indent=2)
        return json.dumps({"format": fmt, "logs": logs}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "export_logs",
                "description": "Export logs to CSV or JSON format from given date range",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "format": {"type": "string", "enum": ["CSV", "JSON"]},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"}
                    },
                    "required": ["format", "start_time", "end_time"]
                }
            }
        }
