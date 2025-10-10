# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TakeBacklogSnapshot(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        snapshot_id: str,
        taken_at: str,
        statuses_in_scope: List[str],
    ) -> str:
        open_ids = [t["ticket_id"] for t in data["tickets"] if t["status"] in statuses_in_scope]
        row = {
            "snapshot_id": snapshot_id,
            "taken_at": taken_at,
            "open_ticket_ids": open_ids,
        }
        _append_row(data["backlog_snapshot_open"], row)
        return json.dumps({"status": "ok", "snapshot": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "take_backlog_snapshot",
                "description": "Write a backlog snapshot of ticket IDs for the given statuses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "taken_at": {"type": "string"},
                        "statuses_in_scope": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["snapshot_id", "taken_at", "statuses_in_scope"],
                },
            },
        }
