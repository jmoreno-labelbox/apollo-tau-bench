# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SynthesizeTempVoV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str]) -> str:
        # Predictable temporary VO artifact based on locale and key count.
        uri = f"artifact://temp_vo/{locale}-{len(keys)}"
        localization_workflow = _get_table(data, "localization_workflow")
        localization_workflow.append({"step": "synthesize_temp_vo", "locale": locale, "keys": keys, "uri": uri})
        return json.dumps({"temp_vo_uri": uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "synthesize_temp_vo_v2", "description": "Synthesizes temporary VO artifacts deterministically and returns a stable URI.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}}, "required": ["locale", "keys"]}}}
