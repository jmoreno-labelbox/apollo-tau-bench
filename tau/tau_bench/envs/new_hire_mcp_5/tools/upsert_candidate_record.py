# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_or_create_label_id(db: Dict[str, Any], name: str) -> str:
    """Return label_id for `name`; create next sequential id (label_1, label_2, ...) if missing."""
    labels = db.setdefault("email_labels", [])
    for lab in labels:
        if lab.get("name") == name:
            return lab["label_id"]
    max_n = 0
    for lab in labels:
        lid = lab.get("label_id") or ""
        m = re.match(r"^label_(\d+)$", lid)
        if m:
            n = int(m.group(1))
            if n > max_n: max_n = n
    new_id = f"label_{max_n + 1}"
    labels.append({"label_id": new_id, "name": name})
    return new_id

def _fixed_ts(ts: Optional[str]) -> str:
    return ts or "2025-09-01T00:00:00Z"

class UpsertCandidateRecord(Tool):
    """
    Idempotent create/update of candidate row keyed by (candidate_email, start_date).
    Deterministic candidate_id based on inputs.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_email, candidate_name, created_ts, manager_email, role_title, start_date, onboarding_status = "Created") -> str:
        email = candidate_email
        start = start_date
        name = candidate_name
        role = role_title
        created_ts = _fixed_ts(created_ts)

        candidates = data.setdefault("candidates", [])
        row = {}
        for _row in list(data.get("candidates", {}).values()):
            if _row.get("candidate_email") == email and _row.get("start_date") == start:
                row = _row
        if row:
            row["candidate_name"] = name
            if role is not None: row["role_title"] = role
            if manager_email is not None: row["manager_email_nullable"] = manager_email
            row["onboarding_status"] = onboarding_status
            return json.dumps({"candidate_id": row["candidate_id"], "status": "updated"}, indent=2)

        candidate_id = _get_or_create_label_id("cand", {"email": email, "start": start, "name": name})
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
            "welcome_email_message_id_nullable": None
        }
        candidates.append(new_row)
        return json.dumps({"candidate_id": candidate_id, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_candidate_record",
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
                        "created_ts": {"type": "string"}
                    },
                    "required": ["candidate_name", "start_date", "candidate_email"]
                }
            }
        }