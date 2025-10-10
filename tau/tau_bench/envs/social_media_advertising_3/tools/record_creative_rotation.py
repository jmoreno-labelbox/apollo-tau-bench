# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordCreativeRotation(Tool):
    """Record a deterministic creative rotation event and enforce single-active rationale (validation only)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ad_id: str = kwargs["ad_id"]
        from_creative: str = kwargs["from_creative"]
        to_creative: str = kwargs["to_creative"]
        rationale: str = kwargs.get("rationale", "")
        rotation_date: str = kwargs["rotation_date"]

        base = json.dumps({
            "ad_id": ad_id, "from_creative": from_creative,
            "to_creative": to_creative, "rotation_date": rotation_date,
            "rationale": rationale
        }, sort_keys=True)
        rotation_id = "rot_" + current_date

        return json.dumps({
            "success": True,
            "rotation_id": rotation_id,
            "ad_id": ad_id,
            "from_creative": from_creative,
            "to_creative": to_creative,
            "rotation_date": rotation_date,
            "rationale": rationale
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_creative_rotation",
                "description": "Record a creative rotation event deterministically; returns rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "from_creative": {"type": "string"},
                        "to_creative": {"type": "string"},
                        "rotation_date": {"type": "string"},
                        "rationale": {"type": "string"}
                    },
                    "required": ["ad_id", "from_creative", "to_creative", "rotation_date"],
                    "additionalProperties": False
                }
            }
        }
