from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class UpdateCandidateInviteTimestamps(Tool):
    """Transfer invitation timestamps (orientation, manager introduction) into the candidate row."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        candidate_id: str, 
        orientation_invite_ts: str = None, 
        manager_intro_invite_ts: str = None
,
    message_id: Any = None,
    ) -> str:
        fields = {}
        if orientation_invite_ts is not None:
            fields["orientation_invite_ts_nullable"] = _fixed_ts(orientation_invite_ts)
        if manager_intro_invite_ts is not None:
            fields["manager_intro_invite_ts_nullable"] = _fixed_ts(manager_intro_invite_ts)
        return UpdateCandidateStatusFields.invoke(
            data, candidate_id=candidate_id, fields=fields
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidateInviteTimestamps",
                "description": "Set candidate invite timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "orientation_invite_ts": {"type": "string"},
                        "manager_intro_invite_ts": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
