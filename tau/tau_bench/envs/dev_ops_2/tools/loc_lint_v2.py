# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LocLintV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str], ui_px_limit: int) -> str:
        translations = _get_table(data, "translations")
        issues = []
        for k in keys:
            row = next((t for t in translations if t.get("string_key") == k and t.get("locale") == locale), None)
            if row and len(row.get("target_text", "")) > ui_px_limit:
                issues.append({"string_key": k, "overflow": len(row.get("target_text")) - ui_px_limit})
        return json.dumps({"lint_report": issues}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "loc_lint_v2", "description": "Checks translated texts against deterministic length budget.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}, "ui_px_limit": {"type": "integer"}}, "required": ["locale", "keys", "ui_px_limit"]}}}
