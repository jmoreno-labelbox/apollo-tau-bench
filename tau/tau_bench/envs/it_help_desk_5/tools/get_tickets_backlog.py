from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetTicketsBacklog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None) -> str:
        snapshots = data.get("backlog_snapshot_open")

        if snapshot_id is None:
            if len(snapshots) > 0:
                target_snapshot = snapshots[-1]
            else:
                payload = {
                    "status": "error",
                    "description": "The snapshot could not be found.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            target_snapshot = None
            for snapshot in snapshots:
                if snapshot["snapshot_id"] == snapshot_id:
                    target_snapshot = snapshot
            if target_snapshot is None:
                payload = {
                    "status": "error",
                    "description": "The snapshot could not be found.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = target_snapshot["open_ticket_ids"]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTicketsBacklog",
                "description": "Gets a list of tickets from a snapshot, the default being the last snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {
                            "type": "string",
                            "description": "The id of the snapshot to look for.",
                        },
                    },
                },
            },
        }
