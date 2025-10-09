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

class CreateAssetRequestWithNotificationTool(Tool):
    """Generates asset requests along with related IT notification emails for one or more candidates."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        candidate_id: str = None,
        candidate_ids: list[str] = None,
        asset_type: str = None,
        urgency_level: str = None,
        specifications: str = None
    ) -> str:
        ids_to_process = []
        if candidate_ids:
            ids_to_process.extend(candidate_ids)
        if candidate_id:
            ids_to_process.append(candidate_id)

        if not ids_to_process:
            return _err("candidate_id or candidate_ids is required.")

        candidates_map = {
            str(c.get("candidate_id")): c for c in data.get("candidates", {}).values()
        }
        asset_requests = data.setdefault("asset_requests", [])
        emails = data.setdefault("emails", [])
        all_results = []

        for cid in ids_to_process:
            candidate = candidates_map.get(cid)
            if not candidate:
                if len(ids_to_process) == 1:
                    return _err(f"Candidate '{cid}' not found.", code="not_found")
                continue

            role_title = candidate.get("role_title", "")
            defaults = ROLE_ASSET_DEFAULTS_MAP.get(
                role_title, ROLE_ASSET_DEFAULTS_MAP["Default"]
            )
            asset_type = asset_type or defaults["asset_type"]
            urgency = urgency_level or defaults["urgency_level"]
            specs = specifications or defaults["specifications"]

            context = {
                "candidate_name": candidate.get("candidate_name", ""),
                "urgency_level": urgency,
                "specifications": specs,
            }
            rendered = _get_hardcoded_template_and_render(
                "asset_request_notification", context
            )

            new_email_id = _next_str_id(emails, "message_id", "msg_")
            new_email = {
                "message_id": new_email_id,
                "subject": rendered["subject"],
                "body": rendered["body"],
                "from_email": "hr@company.com",
                "to_emails": ["it-assets@company.com"],
                "cc_emails": (
                    [candidate.get("manager_email_nullable")]
                    if candidate.get("manager_email_nullable")
                    else []
                ),
                "date_ts": HARD_TS,
                "labels_ids": ["label_1"],
                "attachments_ids": [],
                "draft_flag": False,
                "sent_flag": True,
                "candidate_id_nullable": cid,
                "thread_id_nullable": None,
                "in_reply_to_message_id_nullable": None,
            }
            data["emails"][new_email["email_id"]] = new_email

            new_request = {
                "request_id": _next_str_id(asset_requests, "request_id", "asset_req_"),
                "candidate_id": cid,
                "asset_type": asset_type,
                "status": "Pending",
                "email_message_id_nullable": new_email_id,
                "inventory_checked_flag": False,
                "asset_tag_nullable": None,
                "requested_ts": HARD_TS,
                "updated_ts": HARD_TS,
            }
            asset_requests.append(new_request)

            result = {
                "asset_request": new_request,
                "email": new_email,
                "results": {"system_name": "Email", "status": "Success"},
            }
            all_results.append(result)
        payload = all_results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAssetRequestWithNotification",
                "description": "Creates asset requests and corresponding IT notification emails for one or more candidates.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "A single target candidate identifier.",
                        },
                        "candidate_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of target candidate identifiers.",
                        },
                        "asset_type": {
                            "type": "string",
                            "description": "Optional: Defaults based on role.",
                        },
                        "urgency_level": {
                            "type": "string",
                            "description": "Optional: Defaults based on role.",
                        },
                        "specifications": {
                            "type": "string",
                            "description": "Optional: Defaults based on role.",
                        },
                    },
                },
            },
        }
