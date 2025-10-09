from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateFeaturesFromProcessed(Tool):
    """Creates a features record from an existing processed_timeseries csv_path following deterministic rules."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        processed_csv_path: str,
        features_csv_path: str,
        generated_ts: str,
    ) -> str:
        rows = data.get("processed_timeseries", {}).values()
        target = None
        for row in rows:
            if row.get("csv_path") == processed_csv_path:
                target = row
                break
        if not target:
            payload = {
                "error": "processed_timeseries not found",
                "csv_path": processed_csv_path,
            }
            out = json.dumps(payload)
            return out
        cols = target.get("columns", [])
        feature_names: list[str] = []
        definitions: list[str] = []
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
            "generated_ts": generated_ts,
        }
        data.setdefault("features", []).append(rec)
        payload = {"status": "inserted", "record": rec}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateFeaturesFromProcessed",
                "description": "Generates a features record from an existing processed_timeseries csv_path using deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "processed_csv_path": {"type": "string"},
                        "features_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": [
                        "processed_csv_path",
                        "features_csv_path",
                        "generated_ts",
                    ],
                },
            },
        }
