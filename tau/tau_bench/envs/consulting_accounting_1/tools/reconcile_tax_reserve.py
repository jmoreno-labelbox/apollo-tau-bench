# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReconcileTaxReserve(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], computed_tax_reserve_ref, snapshot_ref, threshold = 0.0) -> str:
        comp_ref = computed_tax_reserve_ref
        snap_ref = snapshot_ref
        threshold = float(threshold)
        if not comp_ref or not snap_ref:
            return json.dumps({"error":"computed_tax_reserve_ref and snapshot_ref are required"}, indent=2)
        computed = float(comp_ref.get("tax_reserve") or comp_ref.get("ytd_tax_reserve") or 0.0)
        snap_val = float(snap_ref.get("ytd_tax_reserve") or 0.0)
        diff = round(computed - snap_val, 2)
        adj = diff if abs(diff) > threshold else 0.00
        return json.dumps({"adjustment": round(adj,2)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"reconcile_tax_reserve",
            "description":"Compute adjustment needed between computed and snapshot tax reserve.",
            "parameters":{"type":"object","properties":{
                "computed_tax_reserve_ref":{"type":"object"},
                "snapshot_ref":{"type":"object"},
                "threshold":{"type":"number"}
            },"required":["computed_tax_reserve_ref","snapshot_ref"]}
        }}
