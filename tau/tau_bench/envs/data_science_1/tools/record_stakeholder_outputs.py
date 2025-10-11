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

class RecordStakeholderOutputs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], generated_ts, metrics_summary_csv_path, predictions_final_csv_path) -> str:
        err = _require(kwargs, ["predictions_final_csv_path", "metrics_summary_csv_path"])
        if err: return err
        row = {"predictions_final_csv_path": predictions_final_csv_path,
               "metrics_summary_csv_path": metrics_summary_csv_path,
               "generated_ts": generated_ts}
        return json.dumps(_append(data.setdefault("stakeholder_outputs", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "record_stakeholder_outputs",
            "description": "Registers links to final predictions/metrics artifacts for stakeholders.",
            "parameters": {"type": "object", "properties": {
                "predictions_final_csv_path": {"type": "string"},
                "metrics_summary_csv_path": {"type": "string"}, "generated_ts": {"type": "string"}},
                "required": ["predictions_final_csv_path", "metrics_summary_csv_path"]}}}