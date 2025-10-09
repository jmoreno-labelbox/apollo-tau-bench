from tau_bench.envs.tool import Tool
import json
from typing import Any

class create_review_cycle(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cycle_id: str,
        artifact_id: str,
        started_at: str,
        timestamp: str,
        request_id: str,
        recipients: list[str],
    ) -> str:
        cycles = data.setdefault("review_cycles", [])
        for c in cycles:
            if isinstance(c, dict) and c.get("cycle_id") == cycle_id:
                if not c.get("recipients"):
                    c["recipients"] = sorted(list(dict.fromkeys(recipients or [])))
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": "NEEDS_REVIEW",
            "started_at": started_at,
            "approvals_recorded": 0,
            "thread_id_nullable": None,
            "recipients": sorted(list(dict.fromkeys(recipients or []))),
            "sla_days": None,
            "day": (timestamp or "").split("T")[0],
        }
        cycles.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewCycle",
                "description": "Create or reuse a deterministic review cycle row; stores recipients.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                        "started_at": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "cycle_id",
                        "artifact_id",
                        "started_at",
                        "timestamp",
                        "request_id",
                        "recipients",
                    ],
                },
            },
        }
