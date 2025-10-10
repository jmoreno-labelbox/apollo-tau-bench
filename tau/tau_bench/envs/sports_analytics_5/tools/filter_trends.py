# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class FilterTrends(Tool):
    """Applies min samples + EB shrinkage + FDR to produce deterministic trend flags (stub persists parameters for verification)."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["pitches"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["min_pitches","min_swings","min_bbe","fdr_threshold"])
        if need:
            return json.dumps({"error": need}, indent=2)
        table_name = (f"trend_flags_p{kwargs['min_pitches']}_s{kwargs['min_swings']}"
                      f"_b{kwargs['min_bbe']}_fdr{kwargs['fdr_threshold']}")
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
