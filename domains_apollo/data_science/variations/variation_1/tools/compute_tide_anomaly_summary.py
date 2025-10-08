from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeTideAnomalySummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        station_id: str,
        water_level_series: list,
        tide_prediction_series: list,
        metrics_csv_path: str = None,
        generated_ts: str = "1970-01-01T00:00:00Z"
    ) -> str:
        req = ["station_id", "water_level_series", "tide_prediction_series"]
        err = _require(locals(), req)
        if err:
            return err
        wl = water_level_series
        tp = tide_prediction_series
        if len(wl) != len(tp):
            payload = {"error": "Series length mismatch"}
            out = json.dumps(payload, indent=2)
            return out
        max_abs = max(abs(float(a) - float(b)) for a, b in zip(wl, tp)) if wl else 0.0
        row = {
            "model_name": f"tide_anomaly_summary:{station_id}",
            "metrics_csv_path": metrics_csv_path or f"processed_data/anomaly_{station_id}.csv",
            "auc_nullable": None,
            "accuracy_nullable": None,
            "rmse_nullable": round(max_abs, 6),
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("metrics", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeTideAnomalySummary",
                "description": "Computes/records max absolute tide anomaly for a station.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "water_level_series": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "tide_prediction_series": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "metrics_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": [
                        "station_id",
                        "water_level_series",
                        "tide_prediction_series",
                    ],
                },
            },
        }
