from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLocString(Tool):
    """Retrieve a localization string row using string_key; locale entry can be included optionally."""

    @staticmethod
    def invoke(data: dict[str, Any], string_key: str = None, locale: str = None) -> str:
        rows = _loc_table(data)
        for row in rows:
            if row.get("string_key") == string_key:
                if locale:
                    entry = (row.get("translations") or {}).get(locale)
                    payload = {"loc_string": row, "locale_entry": entry}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                payload = {"loc_string": row}
                out = json.dumps(payload, indent=2)
                return out
        return _err(f"string_key not found: {string_key}")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLocString",
                "description": "Fetch a loc string by string_key (optionally include a single-locale view).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                    },
                    "required": ["string_key"],
                },
            },
        }
