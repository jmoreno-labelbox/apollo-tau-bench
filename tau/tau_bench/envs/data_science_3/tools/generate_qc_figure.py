# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateQCFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], figure_label) -> str:
        label = figure_label
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        return json.dumps({"figure_path": pdf_path}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"export_qc_figure",
            "description":"Export a QC figure/report and return its deterministic pdf path.",
            "parameters":{"type":"object","properties":{"figure_label":{"type":"string"}},"required":["figure_label"]}
        }}
