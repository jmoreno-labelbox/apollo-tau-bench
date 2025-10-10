# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPitchDetailsById(Tool):
    """Fetch a single pitch by its pitch_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_id = kwargs.get("pitch_id")

        # 1) Validate
        if pitch_id is None:
            return json.dumps({"error": "Missing required field: pitch_id"}, indent=2)

        # 2) Get DB
        pitches: List[Dict[str, Any]] = list(data.get("pitches", {}).values())

        # 3) Exact match
        for p in pitches:
            if p.get("pitch_id") == pitch_id:
                return json.dumps(p, indent=2)

        return json.dumps({"error": f"No pitch found with pitch_id {pitch_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pitch_details_by_id",
                "description": "Fetch a single pitch's full details by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {"type": "integer", "description": "Exact pitch ID to retrieve."}
                    },
                    "required": ["pitch_id"]
                }
            }
        }
