# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class ValidateSubtitleTiming(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], line_id: str, locale: str) -> str:
        timing = _get_table(data, "subtitle_timing")
        # Allow for record identification and nested timing status using either 'line_id' or 'id'.
        row = next((r for r in timing if (r.get("line_id") or r.get("id")) == line_id and r.get("locale") == locale), None)
        status = "unknown"
        if row:
            # Use 'validation_status' if available; else, access timing_validation.status from the nested structure.
            status = row.get("validation_status") or ((row.get("timing_validation") or {}).get("status") or "unknown")
        return json.dumps({"validation_status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_subtitle_timing", "description": "Returns stored validation status for a subtitle line and locale.", "parameters": {"type": "object", "properties": {"line_id": {"type": "string"}, "locale": {"type": "string"}}, "required": ["line_id", "locale"]}}}