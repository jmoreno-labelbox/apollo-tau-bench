from tau_bench.envs.tool import Tool
import json
from typing import Any

class LocLint(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], locale: str, keys: list[str], ui_px_limit: int
    ) -> str:
        translations = _get_table(data, "translations")
        issues = []
        for k in keys:
            row = next(
                (
                    t
                    for t in translations
                    if t.get("string_key") == k and t.get("locale") == locale
                ),
                None,
            )
            if row and len(row.get("target_text", "")) > ui_px_limit:
                issues.append(
                    {
                        "string_key": k,
                        "overflow": len(row.get("target_text")) - ui_px_limit,
                    }
                )
        payload = {"lint_report": issues}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LocLint",
                "description": "Checks translated texts against a deterministic pixel budget by length proxy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "locale": {"type": "string"},
                        "keys": {"type": "array", "items": {"type": "string"}},
                        "ui_px_limit": {"type": "integer"},
                    },
                    "required": ["locale", "keys", "ui_px_limit"],
                },
            },
        }
