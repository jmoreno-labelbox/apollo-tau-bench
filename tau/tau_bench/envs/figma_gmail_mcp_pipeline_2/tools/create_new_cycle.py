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

class CreateNewCycle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, sla_deadline_ts: str = None, thread_id: str = None) -> str:
        if not artifact_id or not sla_deadline_ts:
            missing = []
            if not artifact_id:
                missing.append("artifact_id")
            if not sla_deadline_ts:
                missing.append("sla_deadline_ts")
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        cycle_id = get_next_cycle_id(data)
        created_ts = get_now_timestamp()

        new_cycle = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "thread_id_nullable": thread_id,
            "status": "IN_FLIGHT",
            "created_ts": created_ts,
            "sla_deadline_ts": sla_deadline_ts,
            "sla_breached_flag": False,
            "escalated_ts_nullable": None,
        }

        cycles.append(new_cycle)
        data["review_cycles"] = cycles
        payload = new_cycle
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewCycle",
                "description": "Create a new review cycle with defaults: status=IN_FLIGHT, sla_breached_flag=False, escalated_ts_nullable=None. thread_id is optional. sla_deadline_ts is required.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "thread_id": {"type": ["string", "null"]},
                        "sla_deadline_ts": {"type": "string"},
                    },
                    "required": ["artifact_id", "sla_deadline_ts"],
                },
            },
        }
