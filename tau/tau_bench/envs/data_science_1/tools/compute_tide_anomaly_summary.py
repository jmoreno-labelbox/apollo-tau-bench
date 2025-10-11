# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class ComputeTideAnomalySummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], station_id, tide_prediction_series, water_level_series, generated_ts = "1970-01-01T00:00:00Z", metrics_csv_path = f"processed_data/anomaly_{kwargs['station_id']}.csv") -> str:
        req = ["station_id", "water_level_series", "tide_prediction_series"]
        err = _require(kwargs, req)
        if err: return err
        wl = water_level_series
        tp = tide_prediction_series
        if len(wl) != len(tp):
            return json.dumps({"error": "Series length mismatch"}, indent=2)
        max_abs = max(abs(float(a) - float(b)) for a, b in zip(wl, tp)) if wl else 0.0
        row = {"model_name": f"tide_anomaly_summary:{station_id}",
               "metrics_csv_path": metrics_csv_path,
               "auc_nullable": None, "accuracy_nullable": None, "rmse_nullable": round(max_abs, 6),
               "generated_ts": generated_ts}
        return json.dumps(_append(data.setdefault("metrics", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "compute_tide_anomaly_summary",
            "description": "Computes/records max absolute tide anomaly for a station.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"},
                "water_level_series": {"type": "array", "items": {"type": "number"}},
                "tide_prediction_series": {"type": "array", "items": {"type": "number"}},
                "metrics_csv_path": {"type": "string"},
                "generated_ts": {"type": "string"}},
                "required": ["station_id", "water_level_series", "tide_prediction_series"]}}}
