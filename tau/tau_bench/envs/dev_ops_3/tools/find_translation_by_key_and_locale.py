# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_translation_by_key_and_locale(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], string_key: str, locale: str) -> str:
        translations = data.get("translations", [])
        for t in translations:
            if t.get("string_key") == string_key and t.get("locale") == locale:
                return json.dumps(t, indent=2)
        return json.dumps({"error": f"Translation for key '{string_key}' and locale '{locale}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_translation_by_key_and_locale", "description": "Finds a translation record by its string key and locale.", "parameters": { "type": "object", "properties": { "string_key": { "type": "string" }, "locale": { "type": "string" } }, "required": ["string_key", "locale"] } } }
