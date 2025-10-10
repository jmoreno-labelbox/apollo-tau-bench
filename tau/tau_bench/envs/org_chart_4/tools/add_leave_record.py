# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave_record: dict) -> str:
        records = data.setdefault("leave_records", [])
        records.append(leave_record)
        return json.dumps(
            {"success": True, "leave_id": leave_record.get("leave_id")}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_leave_record",
                "description": "Add a new leave record. The leave_record object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_record": {
                            "type": "object",
                            "description": "Leave record to add",
                        }
                    },
                    "required": ["leave_record"],
                    "additionalProperties": False,
                },
            },
        }
