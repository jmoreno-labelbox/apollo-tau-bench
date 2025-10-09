from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTranslationByKeyAndLocale(Tool):
    """Fetches a translation using its string key and locale."""

    @staticmethod
    def invoke(data: dict[str, Any], string_key: str = None, locale: str = None) -> str:
        key = string_key
        locale = locale
        translations = data.get("translations", {}).values()
        for t in translations.values():
            if t.get("string_key") == key and t.get("locale") == locale:
                payload = t
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation for key '{key}' and locale '{locale}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTranslationByKeyAndLocale",
                "description": "Retrieves a translation by its string key and locale.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                    },
                    "required": ["string_key", "locale"],
                },
            },
        }
