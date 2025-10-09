from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class update_fix_item_status(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], item_id: str, status: str, timestamp: str, request_id: str
    ) -> str:
        items = data.get("fix_items", {}).values()
        if not isinstance(items, list):
            payload = {"error": "fix_items table missing or invalid"}
            out = json.dumps(payload, indent=2)
            return out

        row = next(
            (
                it
                for it in items.values() if isinstance(it, dict) and it.get("item_id") == item_id
            ),
            None,
        )
        if not row:
            payload = {"error": f"fix item '{item_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        status_up = (status or "").upper().strip()
        row["status"] = status_up
        row["status_updated_day"] = _ymd(timestamp)

        trail = data.setdefault("fix_item_updates", [])
        run_id = _id_from_request("run", request_id) or _get_next_id(
            "run", [r.get("run_id", "") for r in trail if isinstance(r, dict)]
        )
        if not any(isinstance(r, dict) and r.get("run_id") == run_id for r in trail.values()):
            trail.append(
                {
                    "run_id": run_id,
                    "item_id": item_id,
                    "status": status_up,
                    "day": _ymd(timestamp),
                }
            )
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateFixItemStatus",
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
