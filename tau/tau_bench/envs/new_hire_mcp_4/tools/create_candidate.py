# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCandidate(Tool):
    """Create or upsert a candidate (deterministic candidate_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, department, email, manager_email, name, start_date, status = "hired") -> str:
        c = {
            "candidate_id": candidate_id,
            "name": name,
            "email": email,
            "start_date": start_date,
            "department": department,
            "manager_email": manager_email,
            "status": status,
        }
        if not c["candidate_id"]:
            return json.dumps({"error": "missing_candidate_id"}, indent=2)
        data.setdefault("candidates", [])
        # insert or update based on candidate_id
        for i, existing in enumerate(data["candidates"]):
            if existing.get("candidate_id") == c["candidate_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in c.items() if v is not None})
                data["candidates"][i] = updated
                return json.dumps(updated, indent=2)
        data["candidates"].append(c)
        return json.dumps(c, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_candidate",
                "description": "Create or upsert a candidate by candidate_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "name": {"type": "string"},
                        "email": {"type": "string"},
                        "start_date": {"type": "string"},
                        "department": {"type": "string"},
                        "manager_email": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["candidate_id"]
                }
            }
        }
