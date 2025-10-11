# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, updates) -> str:
        updates = updates or {}
        candidates = list(data.get("candidates", {}).values())

        # Locate the candidate in the list and modify accordingly.
        for c in candidates:
            if c.get("candidate_id") == candidate_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
                break
        else:
            return json.dumps({"error": f"Candidate {candidate_id} not found"}, indent=2)

        return json.dumps({"updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_candidate",
                "description": "Update candidate details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "updates": {"type": "object"}
                    },
                    "required": ["candidate_id", "updates"]
                }
            }
        }
