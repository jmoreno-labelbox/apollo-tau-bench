# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class GmailDraftEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], body_preview_nullable, created_ts, draft_id, recipients, subject, attachments_paths = []) -> str:
        req = ["draft_id", "subject", "recipients"]
        err = _require(kwargs, req)
        if err: return err
        row = {"draft_id_nullable": draft_id, "message_id_nullable": None,
               "subject": subject, "recipients": recipients,
               "body_preview_nullable": body_preview_nullable,
               "attachments_paths": attachments_paths,
               "status": "drafted", "created_ts": created_ts, "sent_ts_nullable": None}
        return json.dumps(_append(data.setdefault("gmail_messages", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "gmail_draft_email",
            "description": "Creates a drafted Gmail message entry.",
            "parameters": {"type": "object", "properties": {
                "draft_id": {"type": "string"}, "subject": {"type": "string"},
                "recipients": {"type": "array", "items": {"type": "string"}},
                "body_preview_nullable": {"type": "string"},
                "attachments_paths": {"type": "array", "items": {"type": "string"}},
                "created_ts": {"type": "string"}}, "required": ["draft_id", "subject", "recipients"]}}}
