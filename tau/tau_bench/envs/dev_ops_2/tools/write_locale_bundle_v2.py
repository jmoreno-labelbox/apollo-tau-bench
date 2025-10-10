# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteLocaleBundleV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str]) -> str:
        localization_workflow = _get_table(data, "localization_workflow")
        bundle_name = f"bundle-{locale}-{len(keys)}"
        entry = {"bundle": bundle_name, "locale": locale, "keys": keys}
        localization_workflow.append(entry)
        return json.dumps({"bundle_uri": f"artifact://bundle/{bundle_name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_locale_bundle_v2", "description": "Writes deterministic locale bundle record and returns bundle URI.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}}, "required": ["locale", "keys"]}}}
