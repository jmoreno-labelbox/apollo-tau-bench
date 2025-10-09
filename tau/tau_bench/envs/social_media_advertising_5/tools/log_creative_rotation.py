from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogCreativeRotation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_ad_id: str = None,
        new_ad_id: str = None,
        rotated_at: str = None,
        rationale: str = None, change_id: Any = None) -> str:
        rows = data.get("creative_rotations", {}).values()
        nid = f"CR-{max((int(r['rotation_id'][3:]) for r in rows.values()), default=0) + 1}"
        rec = {
            "rotation_id": nid,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,
            "rotated_at": rotated_at,
            "rationale": rationale,
        }
        data["creative_rotations"][rec["creative_rotation_id"]] = rec
        data["creative_rotations"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCreativeRotation",
                "description": "Appends a creative rotation log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_ad_id": {"type": "string"},
                        "new_ad_id": {"type": "string"},
                        "rotated_at": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_ad_id",
                        "new_ad_id",
                        "rotated_at",
                        "rationale",
                    ],
                },
            },
        }
