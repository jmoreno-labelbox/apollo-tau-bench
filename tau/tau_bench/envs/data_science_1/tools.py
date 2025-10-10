import json
from typing import Any, Dict, List, Optional
from domains.dto import Tool


def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row


def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["target_city", "timezone_default"])
        if err: return err
        cfg = {
            "target_city": kwargs["target_city"],
            "forecast_horizon_days": kwargs.get("forecast_horizon_days"),
            "top_n_results": kwargs.get("top_n_results"),
            "timezone_default": kwargs["timezone_default"],
            "max_station_distance_km_nullable": kwargs.get("max_station_distance_km_nullable"),
            "created_ts": kwargs.get("created_ts"),
            "updated_ts": kwargs.get("updated_ts"),
            "primary_station_id_nullable": kwargs.get("primary_station_id_nullable"),
        }
        data["project_config"] = [cfg]  
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "set_project_config",
            "description": "Create/replace the single project config row deterministically.",
            "parameters": {"type": "object", "properties": {
                "target_city": {"type": "string"},
                "forecast_horizon_days": {"type": "integer"},
                "top_n_results": {"type": "integer"},
                "timezone_default": {"type": "string"},
                "max_station_distance_km_nullable": {"type": "number"},
                "created_ts": {"type": "string"},
                "updated_ts": {"type": "string"},
                "primary_station_id_nullable": {"type": "string"},
            }, "required": ["target_city", "timezone_default"]}}}


class CreateDirectory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["path"])
        if err: return err
        row = {"path": kwargs["path"], "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
        tbl = data.setdefault("file_directory", [])
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            return json.dumps(existing, indent=2)
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_directory",
            "description": "Registers a directory path in file_directory deterministically.",
            "parameters": {"type": "object", "properties": {
                "path": {"type": "string"},
                "created_ts": {"type": "string"},
                "updated_ts": {"type": "string"}
            }, "required": ["path"]}}}


class WriteFileText(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["path", "content"])
        if err: return err
        tbl = data.setdefault("file_store", [])
        row = {"path": kwargs["path"], "file_contents_text": kwargs["content"],
               "file_mime_types": kwargs.get("mime_type"),
               "char_counts": len(kwargs["content"]),
               "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            return json.dumps(existing, indent=2)
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_file_text",
            "description": "Stores or updates a text file into file_store deterministically.",
            "parameters": {"type": "object", "properties": {
                "path": {"type": "string"}, "content": {"type": "string"}, "mime_type": {"type": "string"},
                "created_ts": {"type": "string"}, "updated_ts": {"type": "string"}}, "required": ["path", "content"]}}}


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["command"])
        if err: return err
        tbl = data.setdefault("terminal_log", [])
        row = {
            "command": kwargs["command"], "exit_code": kwargs.get("exit_code", 0),
            "stdout": kwargs.get("stdout", ""), "stderr": kwargs.get("stderr", ""),
            "printed_message": kwargs.get("printed_message", ""),
            "printed_ts": kwargs.get("printed_ts", "1970-01-01T00:00:00Z")
        }
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_terminal_log",
            "description": "Appends a terminal log row (deterministic fields only).",
            "parameters": {"type": "object", "properties": {
                "command": {"type": "string"}, "exit_code": {"type": "integer"},
                "stdout": {"type": "string"}, "stderr": {"type": "string"},
                "printed_message": {"type": "string"}, "printed_ts": {"type": "string"}},
                "required": ["command"]}}}


class StoreGeocodingResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["query_city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "query_city": kwargs["query_city"],
            "latitude": kwargs["latitude"], "longitude": kwargs["longitude"],
            "canonical_name": kwargs.get("canonical_name"),
            "provider": "open-meteo",
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "query_ts": kwargs.get("query_ts")
        }
        return json.dumps(_append(data.setdefault("geocoding_results", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_geocoding_result",
            "description": "Adds a geocoding row for the target city.",
            "parameters": {"type": "object", "properties": {
                "query_city": {"type": "string"}, "latitude": {"type": "number"}, "longitude": {"type": "number"},
                "canonical_name": {"type": "string"}, "raw_json_path_nullable": {"type": "string"},
                "query_ts": {"type": "string"}}, "required": ["query_city", "latitude", "longitude"]}}}


class StoreWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "city": kwargs["city"], "latitude": kwargs["latitude"], "longitude": kwargs["longitude"],
            "variables": kwargs.get("variables"), "timezone": kwargs.get("timezone"),
            "horizon_days": kwargs.get("horizon_days"),
            "start_ts": kwargs.get("start_ts"), "end_ts": kwargs.get("end_ts"),
            "timestamps": kwargs.get("timestamps"),
            "precipitation_mm_hr_nullable": kwargs.get("precipitation_mm_hr_nullable"),
            "temperature_2m_c_nullable": kwargs.get("temperature_2m_c_nullable"),
            "wind_speed_10m_ms_nullable": kwargs.get("wind_speed_10m_ms_nullable"),
            "provider": "open-meteo",
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "fetched_ts": kwargs.get("fetched_ts")
        }
        return json.dumps(_append(data.setdefault("weather_forecasts", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_weather_forecast",
            "description": "Adds an hourly weather forecast record.",
            "parameters": {"type": "object", "properties": {
                "city": {"type": "string"}, "latitude": {"type": "number"}, "longitude": {"type": "number"},
                "variables": {"type": "array", "items": {"type": "string"}}, "timezone": {"type": "string"},
                "horizon_days": {"type": "integer"}, "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "precipitation_mm_hr_nullable": {"type": "array", "items": {"type": "number"}},
                "temperature_2m_c_nullable": {"type": "array", "items": {"type": "number"}},
                "wind_speed_10m_ms_nullable": {"type": "array", "items": {"type": "number"}},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["city", "latitude", "longitude"]}}}


class StoreNoaaStationSearch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["query_latitude", "query_longitude", "station_ids"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "query_latitude": kwargs["query_latitude"], "query_longitude": kwargs["query_longitude"],
            "radius_km": kwargs.get("radius_km"),
            "station_ids": kwargs["station_ids"],
            "station_names": kwargs.get("station_names"),
            "station_distances_km": kwargs.get("station_distances_km"),
            "station_latitudes": kwargs.get("station_latitudes"),
            "station_longitudes": kwargs.get("station_longitudes"),
            "station_types_nullable": kwargs.get("station_types_nullable"),
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "query_ts": kwargs.get("query_ts")
        }
        return json.dumps(_append(data.setdefault("noaa_station_searches", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_noaa_station_search",
            "description": "Stores results of a NOAA tide-station proximity search.",
            "parameters": {"type": "object", "properties": {
                "query_latitude": {"type": "number"}, "query_longitude": {"type": "number"},
                "radius_km": {"type": "number"},
                "station_ids": {"type": "array", "items": {"type": "string"}},
                "station_names": {"type": "array", "items": {"type": "string"}},
                "station_distances_km": {"type": "array", "items": {"type": "number"}},
                "station_latitudes": {"type": "array", "items": {"type": "number"}},
                "station_longitudes": {"type": "array", "items": {"type": "number"}},
                "station_types_nullable": {"type": "array", "items": {"type": "string"}},
                "raw_json_path_nullable": {"type": "string"}, "query_ts": {"type": "string"}},
                "required": ["query_latitude", "query_longitude", "station_ids"]}}}


class SetPrimaryStation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["station_id"])
        if err: return err
        cfg = (data.get("project_config") or [{}])[0] if data.get("project_config") else {}
        cfg["primary_station_id_nullable"] = kwargs["station_id"]
        data["project_config"] = [cfg] if data.get("project_config") else [cfg]
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "set_primary_station",
            "description": "Sets the chosen primary station_id on project_config.",
            "parameters": {"type": "object", "properties": {"station_id": {"type": "string"}}, "required": ["station_id"]}}}


class StoreWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "timestamps", "water_level_m", "units"]
        err = _require(kwargs, req)
        if err: return err
        row = {"station_id": kwargs["station_id"], "station_name_nullable": kwargs.get("station_name_nullable"),
               "start_ts": kwargs.get("start_ts"), "end_ts": kwargs.get("end_ts"),
               "timestamps": kwargs["timestamps"], "water_level_m": kwargs["water_level_m"],
               "units": kwargs["units"], "datum_nullable": kwargs.get("datum_nullable"),
               "provider": "noaa-tides-currents", "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
               "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("water_levels", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_water_levels",
            "description": "Stores observed water levels for a station and window.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"}, "station_name_nullable": {"type": "string"},
                "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "water_level_m": {"type": "array", "items": {"type": "number"}},
                "units": {"type": "string"}, "datum_nullable": {"type": "string"},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["station_id", "timestamps", "water_level_m", "units"]}}}


class StoreTidePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "timestamps", "tide_pred_m", "units"]
        err = _require(kwargs, req)
        if err: return err
        row = {"station_id": kwargs["station_id"], "station_name_nullable": kwargs.get("station_name_nullable"),
               "start_ts": kwargs.get("start_ts"), "end_ts": kwargs.get("end_ts"),
               "timestamps": kwargs["timestamps"], "tide_pred_m": kwargs["tide_pred_m"], "units": kwargs["units"],
               "method_nullable": kwargs.get("method_nullable"), "provider": "noaa-tides-currents",
               "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"), "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("tide_predictions", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_tide_predictions",
            "description": "Stores tide predictions for a station and window.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"}, "station_name_nullable": {"type": "string"},
                "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "tide_pred_m": {"type": "array", "items": {"type": "number"}},
                "units": {"type": "string"}, "method_nullable": {"type": "string"},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["station_id", "timestamps", "tide_pred_m", "units"]}}}


class StoreCoastalMeteorology(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "timestamps"]
        err = _require(kwargs, req)
        if err: return err
        row = {"station_id": kwargs["station_id"], "start_ts": kwargs.get("start_ts"),
               "end_ts": kwargs.get("end_ts"), "timestamps": kwargs["timestamps"],
               "wind_speed_ms_nullable": kwargs.get("wind_speed_ms_nullable"),
               "pressure_hpa_nullable": kwargs.get("pressure_hpa_nullable"),
               "temperature_c_nullable": kwargs.get("temperature_c_nullable"),
               "provider": "noaa-tides-currents", "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
               "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("coastal_meteorology", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_coastal_meteorology",
            "description": "Stores coastal meteorology (wind/pressure/temperature) by station.",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"}, "start_ts": {"type": "string"}, "end_ts": {"type": "string"},
                "timestamps": {"type": "array", "items": {"type": "string"}},
                "wind_speed_ms_nullable": {"type": "array", "items": {"type": "number"}},
                "pressure_hpa_nullable": {"type": "array", "items": {"type": "number"}},
                "temperature_c_nullable": {"type": "array", "items": {"type": "number"}},
                "raw_json_path_nullable": {"type": "string"}, "fetched_ts": {"type": "string"}},
                "required": ["station_id", "timestamps"]}}}


class ComputeAndStoreMergedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["csv_path"])
        if err: return err
        allowed = ["csv_path", "columns", "row_count", "min_timestamp", "max_timestamp", "file_hash_sha256", "created_ts"]
        row = {k: kwargs[k] for k in allowed if k in kwargs}
        return json.dumps(_append(data.setdefault("processed_timeseries", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "compute_and_store_merged_timeseries",
            "description": "Registers a merged timeseries CSV artifact and its metadata.",
            "parameters": {"type": "object", "properties": {
                "csv_path": {"type": "string"},
                "columns": {"type": "array", "items": {"type": "string"}},
                "row_count": {"type": "integer"},
                "min_timestamp": {"type": "string"}, "max_timestamp": {"type": "string"},
                "file_hash_sha256": {"type": "string"},
                "created_ts": {"type": "string"}}, "required": ["csv_path"]}}}


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


class StoreFeatures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["csv_path", "feature_names"])
        if err: return err
        row = {"csv_path": kwargs["csv_path"], "feature_names": kwargs["feature_names"],
               "definitions_nullable": kwargs.get("definitions_nullable"), "generated_ts": kwargs.get("generated_ts")}
        return json.dumps(_append(data.setdefault("features", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_features",
            "description": "Stores feature list metadata for a generated CSV.",
            "parameters": {"type": "object", "properties": {
                "csv_path": {"type": "string"}, "feature_names": {"type": "array", "items": {"type": "string"}},
                "definitions_nullable": {"type": "array", "items": {"type": "string"}},
                "generated_ts": {"type": "string"}}, "required": ["csv_path", "feature_names"]}}}


class WriteModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["saved_json_path"])
        if err: return err
        row = {
            "classification_threshold_m_nullable": kwargs.get("classification_threshold_m_nullable"),
            "precip_24h_threshold_mm_nullable": kwargs.get("precip_24h_threshold_mm_nullable"),
            "test_split_fraction_nullable": kwargs.get("test_split_fraction_nullable"),
            "random_seed_nullable": kwargs.get("random_seed_nullable"),
            "saved_json_path": kwargs["saved_json_path"], "created_ts": kwargs.get("created_ts")
        }
        return json.dumps(_append(data.setdefault("model_config", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_model_config",
            "description": "Stores modeling configuration (thresholds/split/seed).",
            "parameters": {"type": "object", "properties": {
                "classification_threshold_m_nullable": {"type": "number"},
                "precip_24h_threshold_mm_nullable": {"type": "number"},
                "test_split_fraction_nullable": {"type": "number"},
                "random_seed_nullable": {"type": "integer"},
                "saved_json_path": {"type": "string"},
                "created_ts": {"type": "string"}}, "required": ["saved_json_path"]}}}


class CreateTimeBasedSplit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["split_summary_json_path"])
        if err: return err
        row = {"method": kwargs.get("method"), "test_fraction": kwargs.get("test_fraction"),
               "train_index_count": kwargs.get("train_index_count"),
               "test_index_count": kwargs.get("test_index_count"),
               "split_summary_json_path": kwargs["split_summary_json_path"],
               "split_ts": kwargs.get("split_ts")}
        return json.dumps(_append(data.setdefault("dataset_split", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "create_time_based_split",
            "description": "Registers a time-based dataset split summary.",
            "parameters": {"type": "object", "properties": {
                "method": {"type": "string"}, "test_fraction": {"type": "number"},
                "train_index_count": {"type": "integer"}, "test_index_count": {"type": "integer"},
                "split_summary_json_path": {"type": "string"}, "split_ts": {"type": "string"}},
                "required": ["split_summary_json_path"]}}}


class RegisterModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["model_name", "model_path"])
        if err: return err
        row = {"model_name": kwargs["model_name"], "model_type": kwargs.get("model_type"),
               "training_ts": kwargs.get("training_ts"),
               "model_path": kwargs["model_path"], "feature_names": kwargs.get("feature_names"),
               "target_name": kwargs.get("target_name"),
               "train_metrics_json_path_nullable": kwargs.get("train_metrics_json_path_nullable")}
        return json.dumps(_append(data.setdefault("models", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_model",
            "description": "Registers a trained model artifact with metadata.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "model_type": {"type": "string"},
                "training_ts": {"type": "string"}, "model_path": {"type": "string"},
                "feature_names": {"type": "array", "items": {"type": "string"}},
                "target_name": {"type": "string"},
                "train_metrics_json_path_nullable": {"type": "string"}},
                "required": ["model_name", "model_path"]}}}


class StorePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["model_name", "predictions_csv_path"])
        if err: return err
        row = {"model_name": kwargs["model_name"], "predictions_csv_path": kwargs["predictions_csv_path"],
               "row_count": kwargs.get("row_count"), "columns": kwargs.get("columns"),
               "generated_ts": kwargs.get("generated_ts")}
        return json.dumps(_append(data.setdefault("predictions", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_predictions",
            "description": "Stores a predictions CSV artifact for a model.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "predictions_csv_path": {"type": "string"},
                "row_count": {"type": "integer"}, "columns": {"type": "array", "items": {"type": "string"}},
                "generated_ts": {"type": "string"}}, "required": ["model_name", "predictions_csv_path"]}}}


class StoreMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["model_name", "metrics_csv_path"])
        if err: return err
        row = {"model_name": kwargs["model_name"], "metrics_csv_path": kwargs["metrics_csv_path"],
               "auc_nullable": kwargs.get("auc_nullable"), "accuracy_nullable": kwargs.get("accuracy_nullable"),
               "rmse_nullable": kwargs.get("rmse_nullable"), "generated_ts": kwargs.get("generated_ts")}
        return json.dumps(_append(data.setdefault("metrics", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_metrics",
            "description": "Stores metrics for a model (AUC/accuracy/RMSE).",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"}, "metrics_csv_path": {"type": "string"},
                "auc_nullable": {"type": "number"}, "accuracy_nullable": {"type": "number"},
                "rmse_nullable": {"type": "number"}, "generated_ts": {"type": "string"}},
                "required": ["model_name", "metrics_csv_path"]}}}


class RecordStakeholderOutputs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["predictions_final_csv_path", "metrics_summary_csv_path"])
        if err: return err
        row = {"predictions_final_csv_path": kwargs["predictions_final_csv_path"],
               "metrics_summary_csv_path": kwargs["metrics_summary_csv_path"],
               "generated_ts": kwargs.get("generated_ts")}
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


class ZoteroSearchItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["query", "result_item_ids", "search_ts"]
        err = _require(kwargs, req)
        if err: return err
        row = {"query": kwargs["query"], "year_from": kwargs.get("year_from"), "year_to": kwargs.get("year_to"),
               "limit": kwargs.get("limit"), "result_item_ids": kwargs["result_item_ids"],
               "saved_path_nullable": kwargs.get("saved_path_nullable"), "search_ts": kwargs["search_ts"]}
        return json.dumps(_append(data.setdefault("zotero_searches", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_search_items",
            "description": "Stores results of a Zotero query (top-N IDs).",
            "parameters": {"type": "object", "properties": {
                "query": {"type": "string"}, "year_from": {"type": "integer"}, "year_to": {"type": "integer"},
                "limit": {"type": "integer"}, "result_item_ids": {"type": "array", "items": {"type": "string"}},
                "saved_path_nullable": {"type": "string"}, "search_ts": {"type": "string"}},
                "required": ["query", "result_item_ids", "search_ts"]}}}


class ZoteroItemMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["item_ids", "titles", "fetched_ts"]
        err = _require(kwargs, req)
        if err: return err
        row = {"item_ids": kwargs["item_ids"], "titles": kwargs["titles"], "authors": kwargs.get("authors"),
               "years": kwargs.get("years"), "venues_nullable": kwargs.get("venues_nullable"),
               "urls_nullable": kwargs.get("urls_nullable"), "abstracts_nullable": kwargs.get("abstracts_nullable"),
               "saved_path_nullable": kwargs.get("saved_path_nullable"), "fetched_ts": kwargs["fetched_ts"]}
        return json.dumps(_append(data.setdefault("zotero_metadata", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_item_metadata",
            "description": "Stores bibliographic metadata for Zotero items.",
            "parameters": {"type": "object", "properties": {
                "item_ids": {"type": "array", "items": {"type": "string"}},
                "titles": {"type": "array", "items": {"type": "string"}},
                "authors": {"type": "array", "items": {"type": "array", "items": {"type": "string"}}},
                "years": {"type": "array", "items": {"type": "integer"}},
                "venues_nullable": {"type": "array", "items": {"type": "string"}},
                "urls_nullable": {"type": "array", "items": {"type": "string"}},
                "abstracts_nullable": {"type": "array", "items": {"type": "string"}},
                "saved_path_nullable": {"type": "string"},
                "fetched_ts": {"type": "string"}}, "required": ["item_ids", "titles", "fetched_ts"]}}}


class ZoteroItemFulltext(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["item_ids", "file_paths"]
        err = _require(kwargs, req)
        if err: return err
        row = {"item_ids": kwargs["item_ids"], "file_paths": kwargs["file_paths"], "fetched_ts": kwargs.get("fetched_ts")}
        return json.dumps(_append(data.setdefault("zotero_fulltexts", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "zotero_item_fulltext",
            "description": "Stores file paths for fetched Zotero fulltexts.",
            "parameters": {"type": "object", "properties": {
                "item_ids": {"type": "array", "items": {"type": "string"}},
                "file_paths": {"type": "array", "items": {"type": "string"}},
                "fetched_ts": {"type": "string"}}, "required": ["item_ids", "file_paths"]}}}


class NotionCreatePage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["page_id", "title"]
        err = _require(kwargs, req)
        if err: return err
        row = {"page_id": kwargs["page_id"], "title": kwargs["title"], "url_nullable": kwargs.get("url_nullable"),
               "properties_json_nullable": kwargs.get("properties_json_nullable"),
               "sections_present": kwargs.get("sections_present", []),
               "created_ts": kwargs.get("created_ts"), "updated_ts": kwargs.get("updated_ts")}
        return json.dumps(_append(data.setdefault("notion_pages", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_create_page",
            "description": "Creates a Notion page record.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"}, "title": {"type": "string"},
                "url_nullable": {"type": "string"}, "properties_json_nullable": {"type": "string"},
                "sections_present": {"type": "array", "items": {"type": "string"}},
                "created_ts": {"type": "string"}, "updated_ts": {"type": "string"}},
                "required": ["page_id", "title"]}}}


class NotionAppendSections(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["page_id"]
        err = _require(kwargs, req)
        if err: return err
        page = next((p for p in data.setdefault("notion_pages", []) if p.get("page_id") == kwargs["page_id"]), None)
        if not page:
            return json.dumps({"error": f"page_id '{kwargs['page_id']}' not found"}, indent=2)
        sections = kwargs.get("sections", [])
        existing = set(page.get("sections_present", []))
        page["sections_present"] = list(existing.union(sections))
        page["updated_ts"] = kwargs.get("updated_ts", page.get("updated_ts"))
        return json.dumps(page, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_append_sections",
            "description": "Appends sections to a Notion page's sections_present.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"},
                "sections": {"type": "array", "items": {"type": "string"}},
                "updated_ts": {"type": "string"}}, "required": ["page_id"]}}}


class NotionUpdatePageProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["page_id", "properties_json"]
        err = _require(kwargs, req)
        if err: return err
        page = next((p for p in data.setdefault("notion_pages", []) if p.get("page_id") == kwargs["page_id"]), None)
        if not page:
            return json.dumps({"error": f"page_id '{kwargs['page_id']}' not found"}, indent=2)
        page["properties_json_nullable"] = kwargs["properties_json"]
        page["updated_ts"] = kwargs.get("updated_ts", page.get("updated_ts"))
        return json.dumps(page, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "notion_update_page_properties",
            "description": "Updates page properties JSON and updated_ts.",
            "parameters": {"type": "object", "properties": {
                "page_id": {"type": "string"}, "properties_json": {"type": "string"}, "updated_ts": {"type": "string"}},
                "required": ["page_id", "properties_json"]}}}


class GmailDraftEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["draft_id", "subject", "recipients"]
        err = _require(kwargs, req)
        if err: return err
        row = {"draft_id_nullable": kwargs["draft_id"], "message_id_nullable": None,
               "subject": kwargs["subject"], "recipients": kwargs["recipients"],
               "body_preview_nullable": kwargs.get("body_preview_nullable"),
               "attachments_paths": kwargs.get("attachments_paths", []),
               "status": "drafted", "created_ts": kwargs.get("created_ts"), "sent_ts_nullable": None}
        return json.dumps(_append(data.setdefault("gmail_messages", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "gmail_draft_email",
            "description": "Creates a drafted Gmail message entry.",
            "parameters": {"type": "object", "properties": {
                "draft_id": {"type": "string"}, "subject": {"type": "string"},
                "recipients": {"type": "array", "items": {"type": "string"}},
                "body_preview_nullable": {"type": "string"},
                "attachments_paths": {"type": "array", "items": {"type": "string"}},
                "created_ts": {"type": "string"}}, "required": ["draft_id", "subject", "recipients"]}}}


class GmailSendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["draft_id"]
        err = _require(kwargs, req)
        if err: return err
        msg = next((m for m in data.setdefault("gmail_messages", []) if m.get("draft_id_nullable") == kwargs["draft_id"]), None)
        if not msg:
            return json.dumps({"error": f"draft_id '{kwargs['draft_id']}' not found"}, indent=2)
        msg["message_id_nullable"] = kwargs.get("message_id", msg.get("message_id_nullable"))
        msg["status"] = "sent"
        msg["sent_ts_nullable"] = kwargs.get("sent_ts", msg.get("sent_ts_nullable", "1970-01-01T00:00:00Z"))
        return json.dumps(msg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "gmail_send_email",
            "description": "Marks a drafted Gmail message as sent.",
            "parameters": {"type": "object", "properties": {
                "draft_id": {"type": "string"}, "message_id": {"type": "string"}, "sent_ts": {"type": "string"}},
                "required": ["draft_id"]}}}


class LogMcpToolCall(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["server_names"]
        err = _require(kwargs, req)
        if err: return err
        row = {"server_names": kwargs["server_names"], "tool_names": kwargs.get("tool_names"),
               "params_json": kwargs.get("params_json"), "response_meta_nullable": kwargs.get("response_meta_nullable"),
               "called_ts": kwargs.get("called_ts")}
        return json.dumps(_append(data.setdefault("mcp_tool_calls", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_mcp_tool_call",
            "description": "Logs a synthetic MCP tool call for traceability.",
            "parameters": {"type": "object", "properties": {
                "server_names": {"type": "array", "items": {"type": "string"}},
                "tool_names": {"type": "array", "items": {"type": "string"}},
                "params_json": {"type": "string"},
                "response_meta_nullable": {"type": "string"},
                "called_ts": {"type": "string"}},
                "required": ["server_names"]}}}


class ComputeTideAnomalySummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["station_id", "water_level_series", "tide_prediction_series"]
        err = _require(kwargs, req)
        if err: return err
        wl = kwargs["water_level_series"]
        tp = kwargs["tide_prediction_series"]
        if len(wl) != len(tp):
            return json.dumps({"error": "Series length mismatch"}, indent=2)
        max_abs = max(abs(float(a) - float(b)) for a, b in zip(wl, tp)) if wl else 0.0
        row = {"model_name": f"tide_anomaly_summary:{kwargs['station_id']}",
               "metrics_csv_path": kwargs.get("metrics_csv_path", f"processed_data/anomaly_{kwargs['station_id']}.csv"),
               "auc_nullable": None, "accuracy_nullable": None, "rmse_nullable": round(max_abs, 6),
               "generated_ts": kwargs.get("generated_ts", "1970-01-01T00:00:00Z")}
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


TOOLS = [
    SetProjectConfig(),
    CreateDirectory(),
    WriteFileText(),
    AppendTerminalLog(),
    StoreGeocodingResult(),
    StoreWeatherForecast(),
    StoreNoaaStationSearch(),
    SetPrimaryStation(),
    StoreWaterLevels(),
    StoreTidePredictions(),
    StoreCoastalMeteorology(),
    ComputeAndStoreMergedTimeseries(),
    RegisterQcFigure(),
    StoreFeatures(),
    WriteModelConfig(),
    CreateTimeBasedSplit(),
    RegisterModel(),
    StorePredictions(),
    StoreMetrics(),
    RecordStakeholderOutputs(),
    ZoteroSearchItems(),
    ZoteroItemMetadata(),
    ZoteroItemFulltext(),
    NotionCreatePage(),
    NotionAppendSections(),
    NotionUpdatePageProperties(),
    GmailDraftEmail(),
    GmailSendEmail(),
    LogMcpToolCall(),
    ComputeTideAnomalySummary(),
]
