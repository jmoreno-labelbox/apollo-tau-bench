from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2ApproveTimeEntry(Tool):
    """Approve time entry for invoicing manually when synced_at is not set."""

    @staticmethod
    def invoke(data: dict[str, Any], entry_id: str = None, approved_by: str = None, approval_reason: str = None) -> str:
        if not all([entry_id, approved_by, approval_reason]):
            return _error("entry_id, approved_by, and approval_reason are required.")

        return _ok(
            entry_id=entry_id,
            approved_by=approved_by,
            approval_reason=approval_reason,
            approved_at="2024-12-16T15:00:00Z",
            status="approved_for_billing",
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2ApproveTimeEntry",
                "description": "Manually approve time entry for invoicing when synced_at is null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "string"},
                        "approved_by": {"type": "string"},
                        "approval_reason": {"type": "string"},
                    },
                    "required": ["entry_id", "approved_by", "approval_reason"],
                },
            },
        }
