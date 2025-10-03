from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeImpactV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], ticket_key: str, fingerprint: str | None = None
    ) -> str:
        pass
        work_items = _get_table(data, "work_items")
        crashes = _get_table(data, "crash_events")
        item = next((w for w in work_items if w.get("ticket_key") == ticket_key), None)
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        sev = (item.get("normalized") or {}).get("severity", "Medium")
        sev_weight = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}.get(sev, 2)
        crash_count = 0
        if fingerprint:
            crash_count = sum(
                1
                for c in crashes
                if c.get("crash_fingerprint") == fingerprint
                or c.get("fingerprint") == fingerprint
            )
        impact = sev_weight * (1 + crash_count)
        item["impact_score"] = impact
        payload = {"impact_score": impact}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeImpactV2",
                "description": "Deterministically computes an impact score from severity weight and optional crash fingerprint count.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_key": {"type": "string"},
                        "fingerprint": {"type": "string"},
                    },
                    "required": ["ticket_key"],
                },
            },
        }
