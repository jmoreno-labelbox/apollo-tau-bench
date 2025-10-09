from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class FindCandidateByEmail(Tool):
    """
    Retrieve a candidate using (candidate_email, start_date).
    Returns: {"found": bool, "candidate_id": str|None, "candidate": dict|None}
    """

    @staticmethod
    def invoke(data: dict[str, Any], candidate_email: str, start_date: str) -> str:
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == candidate_email and _row.get("start_date") == start_date:
                row = _row

        if row:
            payload = {"found": True, "candidate_id": row["candidate_id"], "candidate": row}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"found": False, "candidate_id": None, "candidate": None}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCandidateByEmail",
                "description": "Find candidate by (candidate_email, start_date). Returns full candidate row too.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_email": {"type": "string"},
                        "start_date": {"type": "string"},
                    },
                    "required": ["candidate_email", "start_date"],
                },
            },
        }
