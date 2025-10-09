from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReconcileTaxReserve(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        computed_tax_reserve_ref: dict[str, Any] = None, 
        snapshot_ref: dict[str, Any] = None, 
        threshold: float = 0.0
    ) -> str:
        if not computed_tax_reserve_ref or not snapshot_ref:
            payload = {"error": "computed_tax_reserve_ref and snapshot_ref are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        computed = float(
            computed_tax_reserve_ref.get("tax_reserve") or computed_tax_reserve_ref.get("ytd_tax_reserve") or 0.0
        )
        snap_val = float(snapshot_ref.get("ytd_tax_reserve") or 0.0)
        diff = round(computed - snap_val, 2)
        adj = diff if abs(diff) > threshold else 0.00
        payload = {"adjustment": round(adj, 2)}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReconcileTaxReserve",
                "description": "Compute adjustment needed between computed and snapshot tax reserve.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "computed_tax_reserve_ref": {"type": "object"},
                        "snapshot_ref": {"type": "object"},
                        "threshold": {"type": "number"},
                    },
                    "required": ["computed_tax_reserve_ref", "snapshot_ref"],
                },
            },
        }
