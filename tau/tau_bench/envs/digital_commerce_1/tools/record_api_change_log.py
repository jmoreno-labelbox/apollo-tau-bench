from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordApiChangeLog(Tool):
    @staticmethod
    def invoke(data, target_id: str, environment: str, change_type: str = "ops") -> str:
        cases = _ensure_table(data, "cases")
        change_log_id = _stable_id(
            "chg", change_type, target_id, environment, FIXED_NOW
        )
        title = f"{change_type.capitalize()} – {target_id} [{environment}]"
        cases.append(
            {
                "case_id": change_log_id,
                "title": title,
                "status": "Recorded",
                "created_at": FIXED_NOW,
            }
        )
        return _json(
            {"change_log_id": change_log_id, "title": title, "timestamp": FIXED_NOW}
        )
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RecordApiChangeLog",
                "description": "Record an API change event. Defaults change_type='ops'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_id": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "change_type": {"type": "string"},
                    },
                    "required": ["target_id", "environment"],
                },
            },
        }
