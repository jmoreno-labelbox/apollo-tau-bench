from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ShortlistCandidate(Tool):
    """Include a candidate in the shortlist for a job posting."""

    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None, candidate_id: str = None) -> str:
        jid = job_id
        cid = candidate_id
        for p in data.get("job_postings", []):
            if p.get("job_id") == jid:
                sl = p.setdefault("shortlist", [])
                if cid not in sl:
                    sl.append(cid)
                payload = {"success": f"{cid} shortlisted for {jid}"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Job not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistCandidate",
                "description": "Shortlist candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["job_id", "candidate_id"],
                },
            },
        }
