from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CanonicalizePitchTypes(Tool):
    """Assign pitch_type_canonical for pitches missing it by utilizing PITCH_MAP."""

    @staticmethod
    def invoke(data: dict[str, Any], ingested_at_utc: Any = None, game_pk: Any = None, scope: str = None) -> str:
        if "pitches" not in data:
            payload = {"error": "Missing required table(s): pitches"}
            out = json.dumps(payload, indent=2)
            return out
        updated = 0
        for p in data["pitches"]:
            raw = p.get("pitch_type_raw")
            if raw and not p.get("pitch_type_canonical"):
                p["pitch_type_canonical"] = PITCH_MAP.get(raw, raw)
                updated += 1
        payload = {"updated_rows": updated}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "CanonicalizePitchTypes",
                "description": "Maps pitch_type_raw to canonical labels in pitches.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
