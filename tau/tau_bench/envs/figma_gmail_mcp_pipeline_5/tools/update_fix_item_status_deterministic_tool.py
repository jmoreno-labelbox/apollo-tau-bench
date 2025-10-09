from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class UpdateFixItemStatusDeterministicTool(Tool):
    """Modify a fix item status in a deterministic manner (requires explicit changed_ts)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        changed_ts: str = None,
        item_id: str = None,
        new_status: str = None,
        note: str = ""
    ) -> str:
        item_id = _require_str(item_id, "item_id")
        new_status = _require_str(new_status, "new_status")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not all([item_id, new_status, changed_ts]):
            payload = {"error": "item_id, new_status, changed_ts required"}
            out = json.dumps(payload)
            return out

        items = _safe_table(data, "fix_items")
        idx = _index_by(items, "item_id")
        if item_id not in idx:
            payload = {"error": f"item_id {item_id} not found"}
            out = json.dumps(payload)
            return out

        row = items[idx[item_id]]
        old = row.get("status")
        row["status"] = new_status
        row["last_updated"] = changed_ts
        hist = row.setdefault("status_history", [])
        hist.append(
            {"from": old, "to": new_status, "changed_ts": changed_ts, "note": note}
        )
        payload = {"success": True, "item_id": item_id, "from": old, "to": new_status}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemStatusDeterministic",
                "description": "Update fix item status (deterministic; requires changed_ts).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "changed_ts": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["item_id", "new_status", "changed_ts"],
                },
            },
        }
