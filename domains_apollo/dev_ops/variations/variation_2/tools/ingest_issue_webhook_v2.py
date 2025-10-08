from tau_bench.envs.tool import Tool
import json
from typing import Any

class IngestIssueWebhookV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event: str, payload: dict[str, Any]) -> str:
        pass
        work_items = _get_table(data, "work_items")
        key = payload.get("ticket_key") or f"WB-{len(work_items)+1}"
        existing = next((w for w in work_items if w.get("ticket_key") == key), None)
        if existing:
            existing.update({"source": "webhook", "raw": payload})
        else:
            work_items.append(
                {
                    "ticket_key": key,
                    "source": "webhook",
                    "raw": payload,
                    "state": payload.get("state") or "Open",
                }
            )
        payload = {"ticket_key": key}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IngestIssueWebhookV2",
                "description": "Stores/updates a work item from a webhook payload deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event": {"type": "string"},
                        "payload": {"type": "object"},
                    },
                    "required": ["event", "payload"],
                },
            },
        }
