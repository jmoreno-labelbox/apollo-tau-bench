# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_str_id(rows: List[Dict[str, Any]], key: str, prefix: str) -> str:
    """Generates the next string ID in a sequence (e.g., CAND-001)."""
    if not rows:
        return f"{prefix}1"

    max_id = 0
    for r in rows:
        id_val = r.get(key)
        if id_val and isinstance(id_val, str) and id_val.startswith(prefix):
            try:
                num_part = int(id_val[len(prefix):])
                if num_part > max_id:
                    max_id = num_part
            except ValueError:
                continue

    return f"{prefix}{max_id + 1:03d}"

def _err(msg: str, code: str = "bad_request", ) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class CreateNewCandidateRecordTool(Tool):
    """Inserts candidate into candidates table with validation, duplicate checking, and initial status setting."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_email, candidate_name, manager_email, role_title, start_date) -> str:

        if not all([candidate_name, role_title, start_date, candidate_email]):
            return _err("candidate_name, role_title, start_date, and candidate_email are required")

        candidates = data.setdefault("candidates", [])

        # Redundancy verification
        if any(c.get("candidate_email") == candidate_email for c in candidates):
            return _err(f"Candidate with email '{candidate_email}' already exists.", code="conflict")

        new_candidate = {
            "candidate_id": _next_str_id(candidates, "candidate_id", "CAND-"),
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "role_title": role_title,
            "start_date": start_date,
            "manager_email_nullable": manager_email,
            "onboarding_status": "Started",
            "created_ts": HARD_TS,
            "asset_request_record_id_nullable": None,
            "checklist_follow_up_ts_nullable": None,
            "orientation_invite_ts_nullable": None,
            "manager_intro_invite_ts_nullable": None,
            "welcome_email_message_id_nullable": None
        }

        candidates.append(new_candidate)

        return json.dumps(new_candidate, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_candidate_record",
                "description": "Inserts candidate into candidates table with validation, duplicate checking, and initial status setting.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_name": {"type": "string", "description": "Full name from user input"},
                        "role_title": {"type": "string", "description": "Job position title"},
                        "start_date": {"type": "string", "description": "Start date in YYYY-MM-DD format"},
                        "candidate_email": {"type": "string", "description": "Company email address"},
                        "manager_email": {"type": "string", "description": "Manager email if known"}
                    },
                    "required": ["candidate_name", "role_title", "start_date", "candidate_email"],
                },
            },
        }