# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

class GuardAttachmentPolicyOnDraftTool(Tool):
    """Check draft body length against release policy; returns OK/violation flags (simplified guard)."""

    @staticmethod
    def invoke(data: Dict[str, Any], message_id) -> str:
        message_id = _require_str(message_id, "message_id")
        if not message_id:
            return json.dumps({"error":"message_id is required"})

        # Streamlined: verify body dimensions align with attachment issues
        messages = data.get("gmail_messages", [])
        target = None
        for m in messages:
            if m.get("message_id") == message_id:
                target = m
                break
        if not target:
            return json.dumps({"error": f"message_id {message_id} not found"})

        body = target.get("body","")
        size = len(body.encode("utf-8"))
        policy = _get_config_json(data, "release_workflow_config").get("attachment_policy", {})
        max_total = int(policy.get("max_total_size", 10_000_000))
        ok = size <= max_total
        return json.dumps({"message_id": message_id, "approx_body_bytes": size, "max_total_bytes": max_total, "ok": ok}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"guard_attachment_policy_on_draft",
            "description":"Approximate a policy check by comparing draft body bytes to max_total_size from config.",
            "parameters":{"type":"object","properties":{
                "message_id":{"type":"string"}
            },"required":["message_id"]}
        }}