# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _err(msg: str, code: str = "bad_request", **extra) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _days_between(d1_str: str, d2_str: str) -> int:
    """A deterministic way to calculate days between two ISO date strings."""
    try:
        # Assumes ISO format with 'Z' for UTC
        d1 = datetime.fromisoformat(d1_str.replace("Z", "+00:00"))
        d2 = datetime.fromisoformat(d2_str.replace("Z", "+00:00"))
        return abs((d2 - d1).days)
    except (ValueError, TypeError):
        return 9999  # Return a large number for invalid formats

def _as_int(x: Any) -> Optional[int]:
    """Safely converts a value to an integer."""
    try:
        return int(x)
    except (ValueError, TypeError):
        return None

class GetDraftEmailsRequiringActionTool(Tool):
    """Queries emails table for draft messages that need completion and sending, with aging analysis."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_filter, draft_age_days) -> str:
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