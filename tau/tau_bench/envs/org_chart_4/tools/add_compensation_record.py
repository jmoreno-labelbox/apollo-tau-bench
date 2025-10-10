# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_compensation_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], compensation_record: dict) -> str:
        records = data.setdefault("compensation_records", [])
        records.append(compensation_record)
        return json.dumps(
            {
                "success": True,
                "compensation_id": compensation_record.get("compensation_id"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_compensation_record",
                "description": "Add a new compensation record. The compensation_record object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "compensation_record": {
                            "type": "object",
                            "description": "Compensation record to add",
                        }
                    },
                    "required": ["compensation_record"],
                    "additionalProperties": False,
                },
            },
        }
