from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class CreateNewCandidateRecordTool(Tool):
    """Adds a candidate to the candidates table with validation, duplicate checking, and initial status assignment."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_name: str = None,
        role_title: str = None,
        start_date: str = None,
        candidate_email: str = None,
        manager_email: str = None
    ) -> str:
        if not all([candidate_name, role_title, start_date, candidate_email]):
            return _err(
                "candidate_name, role_title, start_date, and candidate_email are required"
            )

        candidates = data.setdefault("candidates", [])

        # Check for duplicates
        if any(c.get("candidate_email") == candidate_email for c in candidates):
            return _err(
                f"Candidate with email '{candidate_email}' already exists.",
                code="conflict",
            )

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
            "welcome_email_message_id_nullable": None,
        }

        candidates.append(new_candidate)
        payload = new_candidate
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewCandidateRecord",
                "description": "Inserts candidate into candidates table with validation, duplicate checking, and initial status setting.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_name": {
                            "type": "string",
                            "description": "Full name from user input",
                        },
                        "role_title": {
                            "type": "string",
                            "description": "Job position title",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Start date in YYYY-MM-DD format",
                        },
                        "candidate_email": {
                            "type": "string",
                            "description": "Company email address",
                        },
                        "manager_email": {
                            "type": "string",
                            "description": "Manager email if known",
                        },
                    },
                    "required": [
                        "candidate_name",
                        "role_title",
                        "start_date",
                        "candidate_email",
                    ],
                },
            },
        }
