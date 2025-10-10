# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTranslationByKeyAndLocale(Tool):
    """Retrieves a translation by its string key and locale."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        key = kwargs.get("string_key")
        locale = kwargs.get("locale")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("string_key") == key and t.get("locale") == locale:
                return json.dumps(t)
        return json.dumps({"error": f"Translation for key '{key}' and locale '{locale}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_translation_by_key_and_locale",
                "description": "Retrieves a translation by its string key and locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"}
                    },
                    "required": ["string_key", "locale"],
                },
            },
        }
