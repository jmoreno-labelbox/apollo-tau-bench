# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateFeaturesFromProcessed(Tool):
    """
    Generates a features record from an existing processed_timeseries csv_path using deterministic rules.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], processed_csv_path: str, features_csv_path: str, generated_ts: str) -> str:
        rows = list(data.get("processed_timeseries", {}).values())
        target = None
        for row in rows:
            if row.get("csv_path") == processed_csv_path:
                target = row
                break
        if not target:
            return json.dumps({"error": "processed_timeseries not found", "csv_path": processed_csv_path})
        cols = target.get("columns", [])
        feature_names: List[str] = []
        definitions: List[str] = []
        if "precipitation_mm_hr" in cols:
            feature_names.append("precip_24h_mm")
            definitions.append("24-hour rolling sum of precipitation in millimeters")
        if "tide_pred_m" in cols and "water_level_m" in cols:
            feature_names.append("tide_anomaly_6h_max_m")
            definitions.append("6-hour maximum tide anomaly in meters")
        if "pressure_hpa" in cols:
            feature_names.append("pressure_drop_6h_hpa")
            definitions.append("6-hour atmospheric pressure drop in hectopascals")
        if not feature_names:
            feature_names = ["timestamp"]
            definitions = ["ISO timestamp for temporal alignment"]
        rec = {
            "csv_path": features_csv_path,
            "feature_names": feature_names,
            "definitions_nullable": definitions,
            "generated_ts": generated_ts
        }
        data.setdefault("features", []).append(rec)
        return json.dumps({"status": "inserted", "record": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_features_from_processed",
                "description": "Generates a features record from an existing processed_timeseries csv_path using deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "processed_csv_path": {"type": "string"},
                        "features_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"}
                    },
                    "required": ["processed_csv_path", "features_csv_path", "generated_ts"]
                }
            }
        }
