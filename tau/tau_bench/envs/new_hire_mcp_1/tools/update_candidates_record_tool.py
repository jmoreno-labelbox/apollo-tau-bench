# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class UpdateCandidatesRecordTool(Tool):
    """Updates one or more fields for a list of candidate records."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_ids, fields_to_update) -> str:

        if not candidate_ids or not isinstance(candidate_ids, list):
            return _err("candidate_ids (array) is required")
        if not fields_to_update or not isinstance(fields_to_update, dict):
            return _err("fields_to_update (object) is required")

        candidates = data.get("candidates", [])
        updated_candidates = []

        for candidate in candidates:
            if candidate.get("candidate_id") in candidate_ids:
                for field, value in fields_to_update.items():
                    if field in candidate:
                        candidate[field] = value
                updated_candidates.append(candidate)

        return json.dumps(updated_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidates_record",
                "description": "Updates one or more fields for a list of candidate records. Useful for setting timestamps or notes after an action has been performed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_ids": {"type": "array", "items": {"type": "string"}, "description": "List of candidate IDs to update."},
                        "fields_to_update": {"type": "object", "description": "A dictionary of fields to update. e.g., {\"checklist_follow_up_ts_nullable\": \"2024-08-15T12:00:00Z\"}"}
                    },
                    "required": ["candidate_ids", "fields_to_update"],
                },
            },
        }