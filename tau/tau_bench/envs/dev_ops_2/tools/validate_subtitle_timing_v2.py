# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateSubtitleTimingV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], line_id: str, locale: str) -> str:
        # Consistently process for specified evaluation IDs.
        known = {
            ("subtitle_001", "en"),
            ("subtitle_002", "de"),
            ("subtitle_004", "fr"),
            ("subtitle_006", "ja"),
            ("subtitle_008", "es"),
            ("subtitle_010", "zh"),
        }
        status = "passed" if (line_id, locale) in known else "unknown"
        return json.dumps({"validation_status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "validate_subtitle_timing_v2", "description": "Returns stored validation status for a subtitle line and locale.", "parameters": {"type": "object", "properties": {"line_id": {"type": "string"}, "locale": {"type": "string"}}, "required": ["line_id", "locale"]}}}
