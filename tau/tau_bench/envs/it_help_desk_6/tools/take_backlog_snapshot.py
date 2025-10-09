from tau_bench.envs.tool import Tool
import json
from typing import Any

class TakeBacklogSnapshot(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        snapshot_id: str,
        taken_at: str,
        statuses_in_scope: list[str],
    ) -> str:
        pass
        open_ids = [
            t["ticket_id"] for t in data["tickets"] if t["status"] in statuses_in_scope
        ]
        row = {
            "snapshot_id": snapshot_id,
            "taken_at": taken_at,
            "open_ticket_ids": open_ids,
        }
        _append_row(data["backlog_snapshot_open"], row)
        payload = {"status": "ok", "snapshot": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TakeBacklogSnapshot",
                "description": "Write a backlog snapshot of ticket IDs for the given statuses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "taken_at": {"type": "string"},
                        "statuses_in_scope": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["snapshot_id", "taken_at", "statuses_in_scope"],
                },
            },
        }
