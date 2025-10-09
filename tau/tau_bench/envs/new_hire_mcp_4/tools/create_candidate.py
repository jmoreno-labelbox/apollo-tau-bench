from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class CreateCandidate(Tool):
    """Establish or insert a candidate (predictable candidate_id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str = None,
        name: str = None,
        email: str = None,
        start_date: str = None,
        department: str = None,
        manager_email: str = None,
        status: str = "hired"
    ) -> str:
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
            payload = {"error": "missing_candidate_id"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("candidates", [])
        # insert or update using candidate_id
        for i, existing in enumerate(data["candidates"]):
            if existing.get("candidate_id") == c["candidate_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in c.items() if v is not None})
                data["candidates"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["candidates"][candidate_id] = c
        payload = c
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createCandidate",
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
                    "required": ["candidate_id"],
                },
            },
        }
