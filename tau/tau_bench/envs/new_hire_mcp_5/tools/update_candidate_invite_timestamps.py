# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCandidateInviteTimestamps(Tool):
    """Copy invite timestamps (orientation, manager intro) into candidate row."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        fields = {}
        if "orientation_invite_ts" in kwargs:
            fields["orientation_invite_ts_nullable"] = _fixed_ts(kwargs["orientation_invite_ts"])
        if "manager_intro_invite_ts" in kwargs:
            fields["manager_intro_invite_ts_nullable"] = _fixed_ts(kwargs["manager_intro_invite_ts"])
        return UpdateCandidateStatusFields.invoke(data, candidate_id=cand_id, fields=fields)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_invite_timestamps",
                "description": "Set candidate invite timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "orientation_invite_ts": {"type": "string"},
                        "manager_intro_invite_ts": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }
