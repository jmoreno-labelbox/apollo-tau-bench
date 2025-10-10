# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class set_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], compensation: Dict[str, Any]) -> str:
        if not compensation:
            return json.dumps({"error": "compensation record required"}, indent=2)
        comp = data.get("compensation_records", [])
        comp = [
            c for c in comp if c["compensation_id"] != compensation["compensation_id"]
        ]
        comp.append(compensation)
        data["compensation_records"] = comp
        return json.dumps(
            {"success": f'compensation {compensation["compensation_id"]} recorded'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_compensation",
                "description": "Insert a new compensation record with all necessary fields (overwrites prior record if compensation_id already exists).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "compensation": {
                            "type": "object",
                            "description": "Full compensation object",
                        }
                    },
                    "required": ["compensation"],
                    "additionalProperties": False,
                },
            },
        }
