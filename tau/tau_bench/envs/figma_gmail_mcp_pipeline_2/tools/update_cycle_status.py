# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["cycle_id", "new_status"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycle_id = kwargs.get("cycle_id")
        new_status = kwargs.get("new_status")
        escalated_ts: Optional[str] = kwargs.get("escalated_ts")
        thread_id: Optional[str] = kwargs.get("thread_id")

        cycles: List[Dict[str, Any]] = list(data.get("review_cycles", {}).values())
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                row["status"] = new_status
                if "thread_id" in kwargs:
                    row["thread_id_nullable"] = thread_id
                if "escalated_ts" in kwargs:
                    row["escalated_ts_nullable"] = escalated_ts
                    if escalated_ts is not None:
                        row["sla_breached_flag"] = True
                return json.dumps(row, indent=2)

        return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_cycle_status",
                "description": "Update a review cycle status; optionally set thread_id and escalated_ts. If escalated_ts is not null, sla_breached_flag becomes True.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "escalated_ts": {"type": ["string", "null"]},
                        "thread_id": {"type": ["string", "null"]}
                    },
                    "required": ["cycle_id", "new_status"]
                }
            }
        }
