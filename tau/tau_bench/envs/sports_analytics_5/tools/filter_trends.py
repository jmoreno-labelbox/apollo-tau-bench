# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables






def _require_tables(data: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [t for t in required if t not in data or data.get(t) is None]
    if missing:
        return f"Missing required table(s): {', '.join(missing)}"
    return None

def _check_required(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return f"Missing required argument(s): {', '.join(missing)}"
    return None

class FilterTrends(Tool):
    """Applies min samples + EB shrinkage + FDR to produce deterministic trend flags (stub persists parameters for verification)."""
    @staticmethod
    def invoke(data, fdr_threshold, min_bbe, min_pitches, min_swings)->str:
        err = _require_tables(data, ["pitches"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["min_pitches","min_swings","min_bbe","fdr_threshold"])
        if need:
            return json.dumps({"error": need}, indent=2)
        table_name = (f"trend_flags_p{min_pitches}_s{min_swings}"
                      f"_b{min_bbe}_fdr{fdr_threshold}")
        data.setdefault("trend_flags", []).append({"table_name": table_name})
        return json.dumps({"flags_table": table_name}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{
            "name":"filter_trends",
            "description":"Applies min samples + EB shrinkage + FDR to produce trend flags (deterministic).",
            "parameters":{"type":"object","properties":{
                "min_pitches":{"type":"integer"},
                "min_swings":{"type":"integer"},
                "min_bbe":{"type":"integer"},
                "fdr_threshold":{"type":"number"}}, "required":["min_pitches","min_swings","min_bbe","fdr_threshold"]}
        }}