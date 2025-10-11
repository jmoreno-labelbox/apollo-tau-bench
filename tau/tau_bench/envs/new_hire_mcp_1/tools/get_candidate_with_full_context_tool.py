# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCandidateWithFullContextTool(Tool):
    """Retrieves candidate record with all linked emails, asset requests, checklist items, and access checks for comprehensive view."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id) -> str:
        if not candidate_id:
            return _err("candidate_id is required")

        candidates = data.get("candidates", [])
        candidate = next((c for c in candidates if str(c.get("candidate_id")) == str(candidate_id)), None)

        if not candidate:
            return _err(f"Candidate with id '{candidate_id}' not found", code="not_found")

        result = {
            "candidate": candidate,
            "emails": [e for e in data.get("emails", []) if str(e.get("candidate_id_nullable")) == str(candidate_id)],
            "asset_requests": [ar for ar in data.get("asset_requests", []) if str(ar.get("candidate_id")) == str(candidate_id)],
            "checklist_items": [ci for ci in data.get("checklist_items", []) if str(ci.get("candidate_id")) == str(candidate_id)],
            "access_checks": [ac for ac in data.get("access_checks", []) if str(ac.get("candidate_id")) == str(candidate_id)],
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidate_with_full_context",
                "description": "Retrieves candidate record with all linked emails, asset requests, checklist items, and access checks for comprehensive view.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Target candidate identifier"}
                    },
                    "required": ["candidate_id"],
                },
            },
        }
