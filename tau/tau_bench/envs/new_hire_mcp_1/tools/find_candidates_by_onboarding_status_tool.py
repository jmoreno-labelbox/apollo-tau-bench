# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class FindCandidatesByOnboardingStatusTool(Tool):
    """Queries candidates table filtering by status, optionally including date ranges and related record counts."""

    @staticmethod
    def invoke(data: Dict[str, Any], onboarding_status, start_date_after, include_record_counts = False) -> str:
        status = onboarding_status
        include_counts = include_record_counts

        if not status:
            return _err("onboarding_status is required")

        valid_statuses = {"Started", "Packet Sent", "Access Issues", "Asset Pending", "Onboarded"}
        if status not in valid_statuses:
            return _err(f"Invalid onboarding_status '{status}'. Valid statuses are: {sorted(list(valid_statuses))}")

        candidates = data.get("candidates", [])

        # Filter based on status
        filtered_candidates = [c for c in candidates if c.get("onboarding_status") == status]

        # Apply filter based on the starting date.
        if start_date_after:
            try:
                # Check the format of the date.
                datetime.fromisoformat(start_date_after)
                filtered_candidates = [c for c in filtered_candidates if (c.get("start_date") or "0000-00-00") > start_date_after]
            except ValueError:
                return _err("Invalid start_date_after format. Please use YYYY-MM-DD.")

        results = []
        for candidate in filtered_candidates:
            candidate_id = candidate.get("candidate_id")
            if not candidate_id:
                continue

            result_candidate = candidate.copy()
            if include_counts:
                cid_str = str(candidate_id)
                result_candidate["record_counts"] = {
                    "emails": len([e for e in data.get("emails", []) if str(e.get("candidate_id_nullable")) == cid_str]),
                    "asset_requests": len([ar for ar in data.get("asset_requests", []) if str(ar.get("candidate_id")) == cid_str]),
                    "checklist_items": len([ci for ci in data.get("checklist_items", []) if str(ci.get("candidate_id")) == cid_str]),
                    "access_checks": len([ac for ac in data.get("access_checks", []) if str(ac.get("candidate_id")) == cid_str]),
                }
            results.append(result_candidate)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_candidates_by_onboarding_status",
                "description": "Queries candidates table filtering by status, optionally including date ranges and related record counts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "onboarding_status": {
                            "type": "string",
                            "description": "Status to filter ('Started', 'Packet Sent', 'Access Issues', 'Asset Pending', 'Onboarded')"
                        },
                        "start_date_after": {
                            "type": "string",
                            "description": "Filter candidates starting after date (YYYY-MM-DD)"
                        },
                        "include_record_counts": {
                            "type": "boolean",
                            "description": "Include counts of related emails/tasks/assets"
                        }
                    },
                    "required": ["onboarding_status"],
                },
            },
        }