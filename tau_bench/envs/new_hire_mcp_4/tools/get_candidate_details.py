from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class GetCandidateDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str) -> str:
        cand_id = candidate_id
        for row in data.get("candidates", []):
            if row.get("candidate_id") == cand_id:
                payload = {"candidate": row}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"candidate_id {cand_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCandidateDetails",
                "description": "Get candidate row by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
