# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCandidateDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                return json.dumps({"candidate": row}, indent=2)
        return json.dumps({"error": f"candidate_id {cand_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidate_details",
                "description": "Get candidate row by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }
