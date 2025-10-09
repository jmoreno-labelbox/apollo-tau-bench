from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GuardAttachmentPolicyOnDraftTool(Tool):
    """Verify draft body length against release policy; returns OK/violation indicators (simplified guard)."""

    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None) -> str:
        message_id = _require_str(message_id, "message_id")
        if not message_id:
            payload = {"error": "message_id is required"}
            out = json.dumps(payload)
            return out

        messages = data.get("gmail_messages", [])
        target = None
        for m in messages:
            if m.get("message_id") == message_id:
                target = m
                break
        if not target:
            payload = {"error": f"message_id {message_id} not found"}
            out = json.dumps(payload)
            return out

        body = target.get("body", "")
        size = len(body.encode("utf-8"))
        policy = _get_config_json(data, "release_workflow_config").get(
            "attachment_policy", {}
        )
        max_total = int(policy.get("max_total_size", 10_000_000))
        ok = size <= max_total
        payload = {
            "message_id": message_id,
            "approx_body_bytes": size,
            "max_total_bytes": max_total,
            "ok": ok,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GuardAttachmentPolicyOnDraft",
                "description": "Approximate a policy check by comparing draft body bytes to max_total_size from config.",
                "parameters": {
                    "type": "object",
                    "properties": {"message_id": {"type": "string"}},
                    "required": ["message_id"],
                },
            },
        }
