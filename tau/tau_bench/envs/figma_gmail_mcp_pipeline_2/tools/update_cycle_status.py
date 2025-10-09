from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateCycleStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        new_status: str,
        escalated_ts: str = None,
        thread_id: str = None
    ) -> str:
        required = ["cycle_id", "new_status"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                row["status"] = new_status
                if thread_id is not None:
                    row["thread_id_nullable"] = thread_id
                if escalated_ts is not None:
                    row["escalated_ts_nullable"] = escalated_ts
                    if escalated_ts is not None:
                        row["sla_breached_flag"] = True
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No cycle with id '{cycle_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCycleStatus",
                "description": "Update a review cycle status; optionally set thread_id and escalated_ts. If escalated_ts is not null, sla_breached_flag becomes True.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "escalated_ts": {"type": ["string", "null"]},
                        "thread_id": {"type": ["string", "null"]},
                    },
                    "required": ["cycle_id", "new_status"],
                },
            },
        }
