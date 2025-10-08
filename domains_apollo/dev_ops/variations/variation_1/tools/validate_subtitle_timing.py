from tau_bench.envs.tool import Tool
import json
from typing import Any

class ValidateSubtitleTiming(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], line_id: str, locale: str) -> str:
        timing = _get_table(data, "subtitle_timing")
        row = next(
            (
                r
                for r in timing
                if (r.get("line_id") or r.get("id")) == line_id
                and r.get("locale") == locale
            ),
            None,
        )
        status = "unknown"
        if row:
            status = row.get("validation_status") or (
                (row.get("timing_validation") or {}).get("status") or "unknown"
            )
        payload = {"validation_status": status}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateSubtitleTiming",
                "description": "Returns stored validation status for a subtitle line and locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "line_id": {"type": "string"},
                        "locale": {"type": "string"},
                    },
                    "required": ["line_id", "locale"],
                },
            },
        }
