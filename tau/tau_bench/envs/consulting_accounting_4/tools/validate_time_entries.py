# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateTimeEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], rows) -> str:
        rows = rows or []
        missing = [r for r in rows if not r.get("description") or r.get("isbn") in (None,"") or r.get("account_code") in (None,"")]
        return json.dumps({"valid": len(missing)==0, "missing_count": len(missing)}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"validate_time_entries",
            "description":"Validate that time entries have ISBN and account_code.",
            "parameters":{"type":"object","properties":{"rows":{"type":"array","items":{"type":"object"}}},"required":["rows"]}
        }}
