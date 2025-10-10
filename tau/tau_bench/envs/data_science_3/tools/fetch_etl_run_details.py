# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchETLRunDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("etl_runs", []) or []
        rid = kwargs.get("run_id")
        rname = kwargs.get("run_name")
        row = None
        if rid is not None:
            row = next((r for r in runs if str(r.get("run_id"))==str(rid)), None)
        elif rname:
            row = next((r for r in runs if r.get("run_name")==rname), None)
        return json.dumps(row or {"error":"ETL run not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_etl_run_details",
            "description":"Read an ETL run by id or by run_name.",
            "parameters":{"type":"object","properties":{
                "run_id":{"type":"string"},"run_name":{"type":"string"}
            },"required":[]}
        }}
