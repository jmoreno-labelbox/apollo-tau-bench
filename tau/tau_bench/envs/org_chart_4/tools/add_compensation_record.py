from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_compensation_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensation_record: dict, position: Any = None) -> str:
        records = data.setdefault("compensation_records", [])
        records.append(compensation_record)
        payload = {
                "success": True,
                "compensation_id": compensation_record.get("compensation_id"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCompensationRecord",
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
