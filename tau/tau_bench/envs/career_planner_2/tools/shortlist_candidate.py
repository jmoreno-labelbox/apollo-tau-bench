# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ShortlistCandidate(Tool):
    """Add a candidate to a posting's shortlist."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        jid = kwargs.get("job_id")
        cid = kwargs.get("candidate_id")
        for p in data.get("job_postings", []):
            if p.get("job_id") == jid:
                sl = p.setdefault("shortlist", [])
                if cid not in sl:
                    sl.append(cid)
                return json.dumps({"success": f"{cid} shortlisted for {jid}"}, indent=2)
        return json.dumps({"error": "Job not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shortlist_candidate",
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
