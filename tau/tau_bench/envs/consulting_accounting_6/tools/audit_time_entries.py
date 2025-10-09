from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AuditTimeEntries(Tool):
    """Check for the existence of ISBN and account_code in billable entries."""

    @staticmethod
    def invoke(data: dict[str, Any], rows: list[dict[str, Any]] = None) -> str:
        rows = rows or []
        missing = [
            r
            for r in rows
            if not r.get("description")
            or not r.get("isbn")
            or not r.get("account_code")
        ]
        payload = {"valid": len(missing) == 0, "missing_count": len(missing)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AuditTimeEntries",
                "description": "Ensure time entries have ISBN and account_code.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rows": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["rows"],
                },
            },
        }
