from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class UpdateCandidateOnboardingStatusTool(Tool):
    """Refreshes status and associated timestamp fields for one or more candidates."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, candidate_ids: list = None, new_status: str = None) -> str:
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
            candidate = next(
                (c for c in candidates if str(c.get("candidate_id")) == str(cid)), None
            )

            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            candidate["onboarding_status"] = new_status
            updated_candidates.append(candidate)
        payload = updated_candidates
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCandidateOnboardingStatus",
                "description": "Updates status and related timestamp fields for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "A single target candidate identifier.",
                        },
                        "candidate_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of target candidate identifiers.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "Status from workflow analysis",
                        },
                    },
                    "required": ["new_status"],
                },
            },
        }
