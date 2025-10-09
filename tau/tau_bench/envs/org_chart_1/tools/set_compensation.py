from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class set_compensation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensation: dict[str, Any]) -> str:
        if not compensation:
            payload = {"error": "compensation record required"}
            out = json.dumps(payload, indent=2)
            return out
        comp = data.get("compensation_records", [])
        comp = [
            c for c in comp if c["compensation_id"] != compensation["compensation_id"]
        ]
        comp.append(compensation)
        data["compensation_records"] = comp
        payload = {"success": f'compensation {compensation["compensation_id"]} recorded'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetCompensation",
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
