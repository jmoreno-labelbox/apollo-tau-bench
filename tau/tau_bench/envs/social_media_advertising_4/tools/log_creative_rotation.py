from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogCreativeRotation(Tool):
    """Records an entry in the creative rotation log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_ad_id: str = None,
        new_ad_id: str = None,
        rationale: str = None, change_id: Any = None) -> str:
        rotations = data.get("creative_rotations", {}).values()
        new_id = (
            f"CR-{max((int(c['rotation_id'][3:]) for c in rotations.values()), default=0) + 1}"
        )
        new_log = {
            "rotation_id": new_id,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,
            "rotated_at": "2025-08-15T03:00:00Z",
            "rationale": rationale,
        }
        data["creative_rotations"][new_log["creative_rotation_id"]] = new_log
        data["creative_rotations"] = rotations
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCreativeRotation",
                "description": "Writes an audit log entry for an ad creative rotation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_ad_id": {"type": "string"},
                        "new_ad_id": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["adset_id", "old_ad_id", "new_ad_id", "rationale"],
                },
            },
        }
