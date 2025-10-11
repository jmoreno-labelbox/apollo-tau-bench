# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class IngestIssueWebhookV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event: str, payload: Dict[str, Any]) -> str:
        work_items = _get_table(data, "work_items")
        key = payload.get("ticket_key") or f"WB-{len(work_items)+1}"
        existing = next((w for w in work_items if w.get("ticket_key") == key), None)
        if existing:
            existing.update({"source": "webhook", "raw": payload})
        else:
            work_items.append({"ticket_key": key, "source": "webhook", "raw": payload, "state": payload.get("state") or "Open"})
        return json.dumps({"ticket_key": key}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "ingest_issue_webhook_v2", "description": "Stores/updates a work item from a webhook payload deterministically.", "parameters": {"type": "object", "properties": {"event": {"type": "string"}, "payload": {"type": "object"}}, "required": ["event", "payload"]}}}