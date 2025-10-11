# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require




def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

class GmailSendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], draft_id, message_id = msg.get("message_id_nullable"), sent_ts = msg.get("sent_ts_nullable", "1970-01-01T00:00:00Z")) -> str:
        req = ["draft_id"]
        err = _require(kwargs, req)
        if err: return err
        msg = next((m for m in data.setdefault("gmail_messages", []) if m.get("draft_id_nullable") == draft_id), None)
        if not msg:
            return json.dumps({"error": f"draft_id '{draft_id}' not found"}, indent=2)
        msg["message_id_nullable"] = message_id
        msg["status"] = "sent"
        msg["sent_ts_nullable"] = sent_ts
        return json.dumps(msg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "gmail_send_email",
            "description": "Marks a drafted Gmail message as sent.",
            "parameters": {"type": "object", "properties": {
                "draft_id": {"type": "string"}, "message_id": {"type": "string"}, "sent_ts": {"type": "string"}},
                "required": ["draft_id"]}}}