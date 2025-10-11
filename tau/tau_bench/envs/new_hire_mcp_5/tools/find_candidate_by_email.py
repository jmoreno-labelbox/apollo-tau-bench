# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCandidateByEmail(Tool):
    """
    Look up a candidate by (candidate_email, start_date).
    Returns: {"found": bool, "candidate_id": str|None, "candidate": dict|None}
    """

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_email, start_date) -> str:
        email = candidate_email
        start = start_date
        row = {}
        for _row in list(data.get("candidates", {}).values()):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row

        if row:
            return json.dumps({
                "found": True,
                "candidate_id": row["candidate_id"],
                "candidate": row
            }, indent=2)
        return json.dumps({"found": False, "candidate_id": None, "candidate": None}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_candidate_by_email",
                "description": "Find candidate by (candidate_email, start_date). Returns full candidate row too.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_email": {"type": "string"},
                        "start_date": {"type": "string"}
                    },
                    "required": ["candidate_email", "start_date"]
                }
            }
        }
