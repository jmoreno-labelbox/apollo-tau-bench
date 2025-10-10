# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BuildKpiReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        as_of = kwargs.get("as_of","2024-11-30")
        sections = kwargs.get("sections",[])
        name = kwargs.get("artifact_name","AR_KPI_Report")
        path = f"/reports/kpi/{name}.pdf"
        return json.dumps({"as_of": as_of, "sections": sections, "pdf_path": path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"build_kpi_report",
            "description":"Generate a KPI report artifact path.",
            "parameters":{"type":"object","properties":{
                "as_of":{"type":"string"},
                "sections":{"type":"array","items":{"type":"string"}},
                "artifact_name":{"type":"string"}
            },"required":["as_of","sections","artifact_name"]}
        }}
