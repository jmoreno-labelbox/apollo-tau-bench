from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class CreativeRotationRecorder(Tool):
    """Log a consistent creative rotation event and enforce a single-active rationale (for validation purposes only)."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str, from_creative: str, to_creative: str, rotation_date: str, rationale: str = "") -> str:
        base = json.dumps(
            {
                "ad_id": ad_id,
                "from_creative": from_creative,
                "to_creative": to_creative,
                "rotation_date": rotation_date,
                "rationale": rationale,
            },
            sort_keys=True,
        )
        rotation_id = "rot_" + current_date
        payload = {
                "success": True,
                "rotation_id": rotation_id,
                "ad_id": ad_id,
                "from_creative": from_creative,
                "to_creative": to_creative,
                "rotation_date": rotation_date,
                "rationale": rationale,
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
                "name": "CreativeRotationRecorder",
                "description": "Record a creative rotation event deterministically; returns rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "from_creative": {"type": "string"},
                        "to_creative": {"type": "string"},
                        "rotation_date": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "ad_id",
                        "from_creative",
                        "to_creative",
                        "rotation_date",
                    ],
                    "additionalProperties": False,
                },
            },
        }
