from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class StartReviewCycleTool(Tool):
    """Generate or upsert a review cycle for an artifact (deterministic cycle_id based on inputs)."""

    @staticmethod
    def invoke(data: dict[str, Any], artifact_id: str = None, created_ts: str = None, status: str = "IN_FLIGHT") -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        created_ts = _require_str(created_ts, "created_ts")
        if not (artifact_id and created_ts):
            payload = {"error": "artifact_id and created_ts required"}
            out = json.dumps(payload)
            return out

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
            "sla_hours": _get_config_json(data, "sla_deadlines").get(
                "design_review", 72
            ),
        }
        if cycle_id in idx:
            existing = cycles[idx[cycle_id]]
            row["thread_id_nullable"] = existing.get("thread_id_nullable")
            cycles[idx[cycle_id]] = row
        else:
            cycles.append(row)
        payload = {"success": True, "cycle_id": cycle_id, "status": status}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StartReviewCycle",
                "description": "Create/update a review cycle for an artifact (deterministic id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "Default IN_FLIGHT.",
                        },
                    },
                    "required": ["artifact_id", "created_ts"],
                },
            },
        }
