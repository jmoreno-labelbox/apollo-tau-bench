from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SaveReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], save_data: list = None) -> str:
        if save_data is None:
            save_data = []

        if len(save_data) == 0:
            payload = {
                "status": "error",
                "description": "The save_data and file_path parameters are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_report = {
            "save_data": save_data,
            "file_path": "/IT/Reports/Backlog/Backlog_Status.pdf",
        }
        payload = new_report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveReport",
                "description": "Saves a report containing data called Backlog_Status.pdf",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "save_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "An array containing data to save",
                        },
                    },
                    "required": ["save_data"],
                },
            },
        }
