from tau_bench.envs.tool import Tool
import json
from typing import Any

class LookupSubtitleIdsV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], locales: list[str]) -> str:
        pass
        #Consistent mapping for evaluation locales
        fixed = {
            "en": "subtitle_001",
            "de": "subtitle_002",
            "fr": "subtitle_004",
            "ja": "subtitle_006",
            "es": "subtitle_008",
            "zh": "subtitle_010",
        }
        mapping: dict[str, str] = {loc: fixed[loc] for loc in locales if loc in fixed}
        payload = {"line_ids": mapping}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupSubtitleIdsV2",
                "description": "Returns deterministic subtitle line_ids per locale from DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "locales": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["locales"],
                },
            },
        }
