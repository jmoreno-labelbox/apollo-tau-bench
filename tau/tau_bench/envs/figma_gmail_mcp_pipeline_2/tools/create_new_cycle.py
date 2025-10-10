# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewCycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("artifact_id") or not kwargs.get("sla_deadline_ts"):
            missing = []
            if not kwargs.get("artifact_id"):
                missing.append("artifact_id")
            if not kwargs.get("sla_deadline_ts"):
                missing.append("sla_deadline_ts")
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycles: List[Dict[str, Any]] = list(data.get("review_cycles", {}).values())
        cycle_id = get_next_cycle_id(data)
        created_ts = get_now_timestamp()
        thread_id: Optional[str] = kwargs.get("thread_id")
        sla_deadline_ts: str = kwargs.get("sla_deadline_ts")

        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": kwargs["artifact_id"],
            "thread_id_nullable": thread_id,
            "status": "IN_FLIGHT",
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None
        }

        cycles.append(new_cycle)
        data["review_cycles"] = cycles
        return json.dumps(new_cycle, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_cycle",
                "description": "Create a new review cycle with defaults: status=IN_FLIGHT, sla_breached_flag=False, escalated_ts_nullable=None. thread_id is optional. sla_deadline_ts is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                        "sla_deadline_ts": {"type": "string"}
                    },
                    "required": ["artifact_id", "sla_deadline_ts"]
                }
            }
        }
