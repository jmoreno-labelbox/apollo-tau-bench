from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindCandidatesByOnboardingStatusTool(Tool):
    """Searches the candidates table based on status, optionally incorporating date ranges and related record counts."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        onboarding_status: str, 
        start_date_after: str = None, 
        include_record_counts: bool = False
    ) -> str:
        if not onboarding_status:
            return _err("onboarding_status is required")

        valid_statuses = {
            "Started",
            "Packet Sent",
            "Access Issues",
            "Asset Pending",
            "Onboarded",
        }
        if onboarding_status not in valid_statuses:
            return _err(
                f"Invalid onboarding_status '{onboarding_status}'. Valid statuses are: {sorted(list(valid_statuses))}"
            )

        candidates = data.get("candidates", {}).values()

        # Filter based on status
        filtered_candidates = [
            c for c in candidates.values() if c.get("onboarding_status") == onboarding_status
        ]

        # Filter according to start date
        if start_date_after:
            try:
                # Check the format of the date
                datetime.fromisoformat(start_date_after)
                filtered_candidates = [
                    c
                    for c in filtered_candidates
                    if (c.get("start_date") or "0000-00-00") > start_date_after
                ]
            except ValueError:
                return _err("Invalid start_date_after format. Please use YYYY-MM-DD.")

        results = []
        for candidate in filtered_candidates:
            candidate_id = candidate.get("candidate_id")
            if not candidate_id:
                continue

            result_candidate = candidate.copy()
            if include_record_counts:
                cid_str = str(candidate_id)
                result_candidate["record_counts"] = {
                    "emails": len(
                        [
                            e
                            for e in data.get("emails", {}).values()
                            if str(e.get("candidate_id_nullable")) == cid_str
                        ]
                    ),
                    "asset_requests": len(
                        [
                            ar
                            for ar in data.get("asset_requests", {}).values()
                            if str(ar.get("candidate_id")) == cid_str
                        ]
                    ),
                    "checklist_items": len(
                        [
                            ci
                            for ci in data.get("checklist_items", {}).values()
                            if str(ci.get("candidate_id")) == cid_str
                        ]
                    ),
                    "access_checks": len(
                        [
                            ac
                            for ac in data.get("access_checks", {}).values()
                            if str(ac.get("candidate_id")) == cid_str
                        ]
                    ),
                }
            results.append(result_candidate)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCandidatesByOnboardingStatus",
                "description": "Queries candidates table filtering by status, optionally including date ranges and related record counts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "onboarding_status": {
                            "type": "string",
                            "description": "Status to filter ('Started', 'Packet Sent', 'Access Issues', 'Asset Pending', 'Onboarded')",
                        },
                        "start_date_after": {
                            "type": "string",
                            "description": "Filter candidates starting after date (YYYY-MM-DD)",
                        },
                        "include_record_counts": {
                            "type": "boolean",
                            "description": "Include counts of related emails/tasks/assets",
                        },
                    },
                    "required": ["onboarding_status"],
                },
            },
        }
