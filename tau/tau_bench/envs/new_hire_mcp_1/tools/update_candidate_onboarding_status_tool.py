# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCandidateOnboardingStatusTool(Tool):
    """Updates status and related timestamp fields for one or more candidates."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        candidate_ids = kwargs.get("candidate_ids")
        new_status = kwargs.get("new_status")

        if not new_status:
            return _err("new_status is required.")

        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates = data.get("candidates", [])
        updated_candidates = []

        for cid in ids_to_process:
            candidate = next((c for c in candidates if str(c.get("candidate_id")) == str(cid)), None)

            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            candidate["onboarding_status"] = new_status
            updated_candidates.append(candidate)

        return json.dumps(updated_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate_onboarding_status",
                "description": "Updates status and related timestamp fields for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "A single target candidate identifier."},
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "A list of target candidate identifiers."},
                        "new_status": {"type": "string", "description": "Status from workflow analysis"},
                    },
                    "required": ["new_status"],
                },
            },
        }
