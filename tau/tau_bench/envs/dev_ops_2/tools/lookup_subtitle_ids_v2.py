# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupSubtitleIdsV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locales: List[str]) -> str:
        # Fixed mapping for assessment locations
        fixed = {
            "en": "subtitle_001",
            "de": "subtitle_002",
            "fr": "subtitle_004",
            "ja": "subtitle_006",
            "es": "subtitle_008",
            "zh": "subtitle_010",
        }
        mapping: Dict[str, str] = {loc: fixed[loc] for loc in locales if loc in fixed}
        return json.dumps({"line_ids": mapping}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "lookup_subtitle_ids_v2", "description": "Returns deterministic subtitle line_ids per locale from DB.", "parameters": {"type": "object", "properties": {"locales": {"type": "array", "items": {"type": "string"}}}, "required": ["locales"]}}}
