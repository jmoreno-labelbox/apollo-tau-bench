# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ymd(iso_ts: str) -> str:
    # '2024-08-23T10:00:00Z' -> '2024-08-23'
    return (iso_ts or "").split("T")[0]

def _id_from_request(prefix: str, request_id: str) -> str:
    rid = (request_id or "").strip()
    if not rid:
        return None
    return f"{prefix}_{rid}"

def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

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