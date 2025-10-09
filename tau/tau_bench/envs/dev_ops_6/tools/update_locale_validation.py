from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateLocaleValidation(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        loc_string_id: str = None,
        string_key: str = None,
        locale: str = None,
        validation_status: str = None,
        validation_error: str = None,
        metadata: dict[str, Any] = None
    ) -> str:
        loc_rows = _loc_table(data)
        target_row: dict[str, Any] | None = None
        for row in loc_rows:
            if (
                loc_string_id
                and row.get("id") == loc_string_id
                or (string_key and row.get("string_key") == string_key)
            ):
                target_row = row
                break
        if not target_row:
            return _err("loc string not found")
        target_row.setdefault("translations", {})
        entry = target_row["translations"].setdefault(locale, {})
        if validation_status is not None:
            entry["validation_status"] = validation_status
        if validation_error is not None:
            entry["validation_error"] = validation_error
        if metadata is not None:
            entry["metadata"] = metadata
        return _ok(
            {
                "updated": {
                    "string_key": target_row.get("string_key"),
                    "locale": locale,
                    "validation_status": validation_status,
                    "validation_error": validation_error,
                }
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLocaleValidation",
                "description": "Update locale validation and mirror into translations. Optionally attach CI/linkage metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_string_id": {"type": "string"},
                        "string_key": {"type": "string"},
                        "locale": {"type": "string"},
                        "validation_status": {"type": "string"},
                        "validation_error": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["locale"],
                },
            },
        }
