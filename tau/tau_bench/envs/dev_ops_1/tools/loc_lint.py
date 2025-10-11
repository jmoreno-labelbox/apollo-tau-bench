# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class LocLint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], locale: str, keys: List[str], ui_px_limit: int) -> str:
        # Basic fixed-length verification against the threshold.
        translations = _get_table(data, "translations")
        issues = []
        for k in keys:
            row = next((t for t in translations if t.get("string_key") == k and t.get("locale") == locale), None)
            if row and len(row.get("target_text", "")) > ui_px_limit:
                issues.append({"string_key": k, "overflow": len(row.get("target_text")) - ui_px_limit})
        return json.dumps({"lint_report": issues}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "loc_lint", "description": "Checks translated texts against a deterministic pixel budget by length proxy.", "parameters": {"type": "object", "properties": {"locale": {"type": "string"}, "keys": {"type": "array", "items": {"type": "string"}}, "ui_px_limit": {"type": "integer"}}, "required": ["locale", "keys", "ui_px_limit"]}}}