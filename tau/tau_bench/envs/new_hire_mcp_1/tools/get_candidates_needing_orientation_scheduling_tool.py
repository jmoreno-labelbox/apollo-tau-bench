# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCandidatesNeedingOrientationSchedulingTool(Tool):
    """Identifies candidates ready for orientation based on status, access checks, and missing invitation timestamps."""

    @staticmethod
    def invoke(data: Dict[str, Any], days_until_start) -> str:
        days_until_start = _as_int(days_until_start)
        if days_until_start is None:
            return _err("days_until_start (integer) is required")

        candidates = data.get("candidates", [])
        access_checks = data.get("access_checks", [])
        emails = data.get("emails", [])

        ready_candidates = []
        for candidate in candidates:
            start_date = candidate.get("start_date")
            cid = str(candidate.get("candidate_id"))

            if not start_date:
                continue

            # Verify days remaining until the start.
            if _days_between(HARD_TS.split('T')[0], start_date) > days_until_start:
                continue

            # Verify status (considering 'Asset Pending' or 'Packet Sent' as acceptable states)
            if candidate.get("onboarding_status") not in ["Asset Pending", "Packet Sent", "Started"]:
                 continue

            # Verify access permissions
            candidate_access_checks = [ac for ac in access_checks if str(ac.get("candidate_id")) == cid]
            if not candidate_access_checks or any(ac.get("status") == "Failed" for ac in candidate_access_checks):
                continue

            # Verify for a pre-existing orientation invitation by examining the subject line.
            has_invitation = any(
                "orientation invitation" in str(e.get("subject", "")).lower()
                for e in emails
                if str(e.get("candidate_id_nullable")) == cid
            )
            if has_invitation:
                continue

            candidate_copy = candidate.copy()
            # Basic priority assessment
            priority_score = 100 - _days_between(HARD_TS.split('T')[0], start_date)
            candidate_copy["scheduling_priority_score"] = priority_score
            ready_candidates.append(candidate_copy)

        ready_candidates.sort(key=lambda x: x["scheduling_priority_score"], reverse=True)

        return json.dumps(ready_candidates, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_candidates_needing_orientation_scheduling",
                "description": "Identifies candidates ready for orientation based on status, access checks, and missing invitation timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "days_until_start": {"type": "integer", "description": "How many days before start date to schedule"}
                    },
                    "required": ["days_until_start"],
                },
            },
        }
