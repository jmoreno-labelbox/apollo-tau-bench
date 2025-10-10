# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AuditTimeEntries(Tool):
    """Validate the presence of ISBN and account_code for billable entries."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = kwargs.get("rows") or []
        missing = [r for r in rows
                   if not r.get("description") or not r.get("isbn") or not r.get("account_code")]
        return json.dumps({"valid": len(missing) == 0, "missing_count": len(missing)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "audit_time_entries",
            "description": "Ensure time entries have ISBN and account_code.",
            "parameters": {"type": "object", "properties": {
                "rows": {"type": "array", "items": {"type": "object"}}
            }, "required": ["rows"]}
        }}
