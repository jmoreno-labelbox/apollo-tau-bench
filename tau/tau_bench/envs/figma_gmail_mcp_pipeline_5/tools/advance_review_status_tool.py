from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class AdvanceReviewStatusTool(Tool):
    """Progress review cycle status with permitted transitions; deterministic (requires changed_ts)."""

    ALLOWED = {
        "IN_FLIGHT": {"NEEDS_REVIEW", "ESCALATED"},
        "NEEDS_REVIEW": {"APPROVED", "CHANGES_REQUESTED", "ESCALATED"},
        "CHANGES_REQUESTED": {"NEEDS_REVIEW", "ESCALATED"},
        "ESCALATED": {"NEEDS_REVIEW", "APPROVED", "CHANGES_REQUESTED"},
        "APPROVED": set(),
    }

    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, new_status: str = None, changed_ts: str = None, allow_override: bool = False) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        new_status = _require_str(new_status, "new_status")
        changed_ts = _require_str(changed_ts, "changed_ts")
        allow_override = bool(allow_override)
        if not (cycle_id and new_status and changed_ts):
            payload = {"error": "cycle_id, new_status, changed_ts required"}
            out = json.dumps(payload)
            return out

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            payload = {"error": f"cycle_id {cycle_id} not found"}
            out = json.dumps(payload)
            return out

        row = cycles[idx[cycle_id]]
        old = row.get("status")
        if (
            not allow_override
            and new_status not in AdvanceReviewStatusTool.ALLOWED.get(old, set())
        ):
            payload = {"error": f"transition {old} -> {new_status} not allowed"}
            out = json.dumps(
                payload)
            return out

        row["status"] = new_status
        row["last_updated"] = changed_ts
        payload = {"success": True, "cycle_id": cycle_id, "from": old, "to": new_status}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AdvanceReviewStatus",
                "description": "Advance review status with allowed transitions (override optional). Requires changed_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "changed_ts": {"type": "string"},
                        "allow_override": {"type": "boolean"},
                    },
                    "required": ["cycle_id", "new_status", "changed_ts"],
                },
            },
        }
