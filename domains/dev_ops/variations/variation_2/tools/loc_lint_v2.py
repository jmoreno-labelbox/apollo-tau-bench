from tau_bench.envs.tool import Tool
import json
from typing import Any

class LocLintV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], locale: str, keys: list[str], ui_px_limit: int
    ) -> str:
        pass
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
                "name": "LocLintV2",
                "description": "Checks translated texts against deterministic length budget.",
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
