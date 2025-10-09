from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class UpsertCandidateRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_email: str,
        start_date: str,
        candidate_name: str,
        role_title: str = None,
        manager_email: str = None,
        onboarding_status: str = "Created",
        created_ts: Any = None, due_date_lte: Any = None) -> str:
        pass
        email = candidate_email
        start = start_date
        name = candidate_name
        role = role_title
        manager_email = manager_email
        onboarding_status = onboarding_status
        created_ts = _fixed_ts(created_ts)

        candidates = data.setdefault("candidates", [])
        row = {}
        for _row in data.get("candidates", []):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row
        if row:
            row["candidate_name"] = name
            if role is not None:
                row["role_title"] = role
            if manager_email is not None:
                row["manager_email_nullable"] = manager_email
            row["onboarding_status"] = onboarding_status
            payload = {"candidate_id": row["candidate_id"], "status": "updated"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        candidate_id = _get_or_create_label_id(
            "cand", {"email": email, "start": start, "name": name}
        )
        new_row = {
            "candidate_id": candidate_id,
            "candidate_name": name,
            "role_title": role,
            "start_date": start,
            "candidate_email": email,
            "onboarding_status": onboarding_status,
            "asset_request_record_id_nullable": None,
            "checklist_follow_up_ts_nullable": None,
            "created_ts": created_ts,
            "manager_email_nullable": manager_email,
            "orientation_invite_ts_nullable": None,
            "manager_intro_invite_ts_nullable": None,
            "welcome_email_message_id_nullable": None,
        }
        candidates.append(new_row)
        payload = {"candidate_id": candidate_id, "status": "created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertCandidateRecord",
                "description": "Create/update candidate keyed by (candidate_email, start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_name": {"type": "string"},
                        "role_title": {"type": "string"},
                        "start_date": {"type": "string"},
                        "candidate_email": {"type": "string"},
                        "manager_email": {"type": "string"},
                        "onboarding_status": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["candidate_name", "start_date", "candidate_email"],
                },
            },
        }
