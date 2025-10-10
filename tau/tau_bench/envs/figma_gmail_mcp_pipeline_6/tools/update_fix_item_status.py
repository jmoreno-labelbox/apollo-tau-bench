# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_fix_item_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id: str, status: str, timestamp: str, request_id: str) -> str:
        items = data.get("fix_items", [])
        if not isinstance(items, list):
            return json.dumps({"error": "fix_items table missing or invalid"}, indent=2)

        row = next((it for it in items if isinstance(it, dict) and it.get("item_id") == item_id), None)
        if not row:
            return json.dumps({"error": f"fix item '{item_id}' not found"}, indent=2)

        status_up = (status or "").upper().strip()
        row["status"] = status_up
        row["status_updated_day"] = _ymd(timestamp)

        trail = data.setdefault("fix_item_updates", [])
        run_id = _id_from_request("run", request_id) or _get_next_id("run", [r.get("run_id", "") for r in trail if isinstance(r, dict)])
        if not any(isinstance(r, dict) and r.get("run_id") == run_id for r in trail):
            trail.append({
                "run_id": run_id,
                "item_id": item_id,
                "status": status_up,
                "day": _ymd(timestamp),
            })

        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_fix_item_status",
                "description": "Set the status for a fix item (e.g., PENDING, APPLIED) deterministically and record an audit trail.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["item_id", "status", "timestamp", "request_id"],
                },
            },
        }
