# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetRequestStatus(Tool):
    @staticmethod
    def _find_email(db, candidate_id: str, subject: str, date_ts: str):
        emails = db.get("emails", [])
        matches = [e for e in emails
                   if e.get("candidate_id_nullable") == candidate_id
                   and e.get("subject") == subject
                   and e.get("date_ts") == date_ts]
        if not matches: return None
        def seq(e):
            m = re.match(r"^msg_(\d+)$", e.get("message_id",""))
            return int(m.group(1) or 0) if m else 0
        matches.sort(key=lambda e: (e.get("sent_flag") is True, seq(e)), reverse=True)
        return matches[0]

    @staticmethod
    def invoke(db, **kwargs) -> str:
        reqs = db.setdefault("asset_requests", [])
        row = None
        if "request_id" in kwargs:
            row = next((r for r in reqs if r.get("request_id") == kwargs["request_id"]), None)
        else:
            row = next((r for r in reqs if r.get("candidate_id") == kwargs["candidate_id"] and r.get("asset_type") == kwargs["asset_type"]), None)
        if not row:
            return json.dumps({"error": "asset request not found"}, indent=2)
        email_id = kwargs.get("email_message_id")
        if not email_id:
            cand_id = kwargs.get("candidate_id")
            subj    = kwargs.get("subject")
            dts     = _fixed_ts(kwargs.get("date_ts"))
            if cand_id and subj:
                em = UpdateAssetRequestStatus._find_email(db, cand_id, subj, dts)
                if em: email_id = em.get("message_id")
        row["status"] = kwargs.get("status", row.get("status"))
        if email_id is not None:
            row["email_message_id_nullable"] = email_id
        row["updated_ts"] = _fixed_ts(kwargs.get("updated_ts"))
        return json.dumps({"request_id": row["request_id"], "status": row["status"], "email_message_id": row.get("email_message_id_nullable")}, indent=2)


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_request_status",
                "description": "Update asset request status and optional email message id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "email_message_id": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "asset_type"]
                }
            }
        }
