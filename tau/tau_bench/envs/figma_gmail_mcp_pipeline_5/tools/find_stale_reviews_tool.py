from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindStaleReviewsTool(Tool):
    """Provide cycles that surpass SLA (status not APPROVED) by comparing last_updated with SLA hours."""

    @staticmethod
    def invoke(data: dict[str, Any], now_iso: str = None) -> str:
        now_iso = _require_str(now_iso, "now_iso")
        if not now_iso:
            payload = {"error": "now_iso is required (ISO timestamp baseline)"}
            out = json.dumps(payload)
            return out

        cycles = data.get("review_cycles", {}).values()
        sla_hours = _get_config_json(data, "sla_deadlines").get("design_review", 72)

        def overdue(c: dict[str, Any]) -> bool:
            return c.get("status") != "APPROVED" and c.get("last_updated", "") < now_iso

        out = []
        for c in cycles.values():
            if overdue(c):
                out.append(
                    _small_fields(
                        c, ["cycle_id", "artifact_id", "status", "last_updated"]
                    )
                )
        out.sort(key=lambda r: r.get("cycle_id", ""))
        payload = {"sla_hours": sla_hours, "stale_cycles": out}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindStaleReviews",
                "description": "Find review cycles not APPROVED and older than 'now_iso' (approximation for SLA breach).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "now_iso": {
                            "type": "string",
                            "description": "Current timestamp baseline (ISO).",
                        }
                    },
                    "required": ["now_iso"],
                },
            },
        }
