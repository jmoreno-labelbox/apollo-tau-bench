# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDraftEmailsRequiringActionTool(Tool):
    """Queries emails table for draft messages that need completion and sending, with aging analysis."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        draft_age_days = _as_int(kwargs.get("draft_age_days"))
        candidate_filter = kwargs.get("candidate_filter")

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
                if candidate_filter is None or str(draft.get("candidate_id_nullable")) == str(candidate_filter):
                    draft_copy = draft.copy()
                    draft_copy["age_days"] = age
                    results.append(draft_copy)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_draft_emails_requiring_action",
                "description": "Queries emails table for draft messages that need completion and sending, with aging analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_age_days": {"type": "integer", "description": "Minimum age of drafts to include"},
                        "candidate_filter": {"type": "string", "description": "Filter to specific candidate"}
                    },
                    "required": ["draft_age_days"],
                },
            },
        }
