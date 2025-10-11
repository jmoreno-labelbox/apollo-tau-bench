# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2ApproveTimeEntry(Tool):
    """Manually approve time entry for invoicing when synced_at is null."""

    @staticmethod
    def invoke(data: Dict[str, Any], approval_reason, approved_by, entry_id) -> str:

        if not all([entry_id, approved_by, approval_reason]):
            return _error("entry_id, approved_by, and approval_reason are required.")

        return _ok(
            entry_id=entry_id,
            approved_by=approved_by,
            approval_reason=approval_reason,
            approved_at="2024-12-16T15:00:00Z",
            status="approved_for_billing"
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_approve_time_entry",
                "description": "Manually approve time entry for invoicing when synced_at is null.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entry_id": {"type": "string"},
                        "approved_by": {"type": "string"},
                        "approval_reason": {"type": "string"}
                    },
                    "required": ["entry_id", "approved_by", "approval_reason"],
                },
            },
        }
