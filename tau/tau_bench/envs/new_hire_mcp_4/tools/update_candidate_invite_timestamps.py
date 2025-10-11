# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class UpdateCandidateStatusFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        fields: Dict[str, Any] = kwargs.get("fields", {})
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                for k, v in fields.items():
                    if v is None:
                        row[k] = None
                    else:
                        row[k] = v
                return json.dumps({"candidate_id": cand_id, "updated_fields": list(fields.keys())}, indent=2)
        return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_status_fields",
                "description": "Update selected candidate fields deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "fields": {"type": "object"}
                    },
                    "required": ["candidate_id", "fields"]
                }
            }
        }

class UpdateCandidateInviteTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, manager_intro_invite_ts, orientation_invite_ts) -> str:
        cand_id = candidate_id
        fields = {}
        if "orientation_invite_ts" in kwargs:
            fields["orientation_invite_ts_nullable"] = _fixed_ts(orientation_invite_ts)
        if "manager_intro_invite_ts" in kwargs:
            fields["manager_intro_invite_ts_nullable"] = _fixed_ts(manager_intro_invite_ts)
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