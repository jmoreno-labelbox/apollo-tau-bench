# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class RegisterQcFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["figure_path"])
        if err: return err
        row = {"figure_path": kwargs["figure_path"], "description": kwargs.get("description"),
               "created_ts": kwargs.get("created_ts")}
        return json.dumps(_append(data.setdefault("qc_figures", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_qc_figure",
            "description": "Registers a QC figure path and description.",
            "parameters": {"type": "object", "properties": {
                "figure_path": {"type": "string"}, "description": {"type": "string"}, "created_ts": {"type": "string"}},
                "required": ["figure_path"]}}}
