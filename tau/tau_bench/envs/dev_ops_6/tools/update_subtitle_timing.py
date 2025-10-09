from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateSubtitleTiming(Tool):
    """Modify subtitle_timing row fields (e.g., subtitle_start/end/text) with basic safeguards."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        sub_id: str = None,
        updates: dict[str, Any] = None
    ) -> str:
        if updates is None:
            updates = {}
        table = _table(data, "subtitle_timing")
        row = next((r for r in table if r.get("id") == sub_id), None)
        if not row:
            return _err(f"subtitle_timing id not found: {sub_id}")
        if "subtitle_start" in updates and "subtitle_end" in updates:
            s, e = (updates["subtitle_start"], updates["subtitle_end"])
            if not (isinstance(s, (int, float)) and isinstance(e, (int, float))):
                return _err("subtitle_start/subtitle_end must be numeric")
            if not 0 <= s < e:
                return _err("subtitle_start must be >= 0 and < subtitle_end")
        row.update(updates)
        return _ok({"updated_subtitle": {"id": sub_id, "applied_updates": updates}})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSubtitleTiming",
                "description": "Update a subtitle_timing record with basic timing guards.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["id", "updates"],
                },
            },
        }
