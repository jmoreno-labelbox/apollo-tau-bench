# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StartReviewCycleTool(Tool):
    """Create or upsert a review cycle for an artifact (deterministic cycle_id from inputs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        artifact_id = _require_str(kwargs.get("artifact_id"), "artifact_id")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        status = kwargs.get("status") or "IN_FLIGHT"
        if not (artifact_id and created_ts):
            return json.dumps({"error":"artifact_id and created_ts required"})

        cycle_id = _det_id("cycle", [artifact_id, created_ts, status])
        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": status,
            "created_ts": created_ts,
            "last_updated": created_ts,
            "thread_id_nullable": None,
            "sla_hours": _get_config_json(data, "sla_deadlines").get("design_review", 72)
        }
        if cycle_id in idx:
            # maintain current thread connection
            existing = cycles[idx[cycle_id]]
            row["thread_id_nullable"] = existing.get("thread_id_nullable")
            cycles[idx[cycle_id]] = row
        else:
            cycles.append(row)

        return json.dumps({"success": True, "cycle_id": cycle_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"start_review_cycle",
            "description":"Create/update a review cycle for an artifact (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "created_ts":{"type":"string"},
                "status":{"type":"string","description":"Default IN_FLIGHT."}
            },"required":["artifact_id","created_ts"]}
        }}
