from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class GetDraftEmailsRequiringActionTool(Tool):
    """Searches the emails table for draft messages requiring completion and dispatch, along with aging analysis."""

    @staticmethod
    def invoke(data: dict[str, Any], draft_age_days: int = None, candidate_filter: str = None) -> str:
        pass
        draft_age_days = _as_int(draft_age_days)

        if draft_age_days is None:
            return _err("draft_age_days (integer) is required")

        emails = data.get("emails", [])
        drafts = [e for e in emails if e.get("draft_flag") == True]

        results = []
        for draft in drafts:
            created_at = draft.get("date_ts")
            if not created_at:
                continue

            age = _days_between(created_at, HARD_TS)
            if age >= draft_age_days:
                if candidate_filter is None or str(
                    draft.get("candidate_id_nullable")
                ) == str(candidate_filter):
                    draft_copy = draft.copy()
                    draft_copy["age_days"] = age
                    results.append(draft_copy)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDraftEmailsRequiringAction",
                "description": "Queries emails table for draft messages that need completion and sending, with aging analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_age_days": {
                            "type": "integer",
                            "description": "Minimum age of drafts to include",
                        },
                        "candidate_filter": {
                            "type": "string",
                            "description": "Filter to specific candidate",
                        },
                    },
                    "required": ["draft_age_days"],
                },
            },
        }
