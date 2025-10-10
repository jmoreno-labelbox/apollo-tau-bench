# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCandidateStatusFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, fields = {}) -> str:
        cand_id = candidate_id
        fields: Dict[str, Any] = fields
        for row in list(data.get("candidates", {}).values()):
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
