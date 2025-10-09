from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class find_translation_by_key_and_locale(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], string_key: str, locale: str) -> str:
        pass
        translations = data.get("translations", [])
        for t in translations:
            if t.get("string_key") == string_key and t.get("locale") == locale:
                payload = t
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": f"Translation for key '{string_key}' and locale '{locale}' not found"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTranslationByKeyAndLocale",
                "description": "Finds a translation record by its string key and locale.",
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
