# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class RegisterQcFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], created_ts, description, figure_path) -> str:
        err = _require(kwargs, ["figure_path"])
        if err: return err
        row = {"figure_path": figure_path, "description": description,
               "created_ts": created_ts}
        return json.dumps(_append(data.setdefault("qc_figures", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_qc_figure",
            "description": "Registers a QC figure path and description.",
            "parameters": {"type": "object", "properties": {
                "figure_path": {"type": "string"}, "description": {"type": "string"}, "created_ts": {"type": "string"}},
                "required": ["figure_path"]}}}