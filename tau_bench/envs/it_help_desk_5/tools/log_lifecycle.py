from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LogLifecycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, memo_id: str = None, event: str = None) -> str:
        if any([param is None for param in [employee_id, memo_id, event]]):
            payload = {
                    "status": "error",
                    "description": "The employee_id, memo_id, and event fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        lifecycle_items = data.get("lifecycle_queue")

        id = lifecycle_items[-1]["lifecycle_id"].split("_")
        new_lifecycle_id = f"{id[0]}_{str(int(id[1])+1).zfill(5)}"

        lifecycle = {
            "lifecycle_id": new_lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_id,
            "event": event,
            "status": "completed",
            "created_at": FIXED_NOW,
        }

        lifecycle_items.append(lifecycle)
        payload = {
                "status": "ok",
                "description": "Successfully added log to lifecycle_queue",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logLifecycle",
                "description": "Logs data to lifecycle_queue",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "memo_id": {
                            "type": "string",
                            "description": "The id of the memo referenced.",
                        },
                        "event": {
                            "type": "string",
                            "description": "The event type of the log",
                        },
                    },
                    "required": ["employee_id", "memo_id", "event"],
                },
            },
        }
