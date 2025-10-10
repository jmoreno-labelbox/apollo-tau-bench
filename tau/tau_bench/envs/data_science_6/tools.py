import json
from datetime import datetime
from typing import Dict, Any, List, Optional
from domains.dto import Tool

class GetWeatherForecast(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> Optional[datetime]:
        try:
            # aceita "YYYY-MM-DDTHH:MM:SSZ" e "YYYY-MM-DDTHH:MM:SS"
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")

        if not city or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: city, start_ts, end_ts"})

        start_dt = GetWeatherForecast._parse_iso(start_ts)
        end_dt = GetWeatherForecast._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("weather_forecasts", [])
        for rec in items:
            if rec.get("city") != city:
                continue
            rec_start = GetWeatherForecast._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWeatherForecast._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            # exigimos cobertura total do intervalo solicitado
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                # sub-seleciona o range
                def in_range(ts):
                    dt = GetWeatherForecast._parse_iso(ts)
                    return dt is not None and (start_dt <= dt <= end_dt)

                out_ts = [t for t in ts_list if in_range(t)]
                # alinhar séries (pode haver _nullable)
                precip = rec.get("precipitation_mm_hr_nullable") or []
                temp = rec.get("temperature_2m_c_nullable") or []
                wind = rec.get("wind_speed_10m_ms_nullable") or []

                # cortar pelos mesmos índices selecionados
                # (assume alinhamento por posição com timestamps)
                idxs = [i for i, t in enumerate(ts_list) if t in out_ts]
                def sel(arr): return [arr[i] for i in idxs if i < len(arr)]
                result = {
                    "city": city,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "temperature_c": sel(temp),
                    "precipitation_mm_hr": sel(precip),
                    "wind_speed_10m_ms": sel(wind)
                }
                return json.dumps(result)

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_weather_forecast",
                "description": "Returns hourly weather forecast series for a city within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City name exactly as stored in the database."},
                        "start_ts": {"type": "string", "description": "Start timestamp (ISO 8601)."},
                        "end_ts": {"type": "string", "description": "End timestamp (ISO 8601)."}
                    },
                    "required": ["city", "start_ts", "end_ts"]
                }
            }
        }

class GetTidePredictions(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")

        if not station_id or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: station_id, start_ts, end_ts"})

        start_dt = GetTidePredictions._parse_iso(start_ts)
        end_dt = GetTidePredictions._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("tide_predictions", [])
        for rec in items:
            if rec.get("station_id") != station_id:
                continue
            rec_start = GetTidePredictions._parse_iso(rec.get("start_ts", ""))
            rec_end = GetTidePredictions._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                vals = rec.get("tide_pred_m") or []
                idxs = [i for i, t in enumerate(ts_list)
                        if (GetTidePredictions._parse_iso(t) or start_dt) and (start_dt <= GetTidePredictions._parse_iso(t) <= end_dt)]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                return json.dumps({
                    "station_id": station_id,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "tide_pred_m": out_vals,
                    "units": rec.get("units", "meters")
                })

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tide_predictions",
                "description": "Returns tide prediction series for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string", "description": "NOAA station id (e.g., '9414290')."},
                        "start_ts": {"type": "string", "description": "Start timestamp (ISO 8601)."},
                        "end_ts": {"type": "string", "description": "End timestamp (ISO 8601)."}
                    },
                    "required": ["station_id", "start_ts", "end_ts"]
                }
            }
        }

class GetWaterLevels(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station_id = kwargs.get("station_id")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")

        if not station_id or not start_ts or not end_ts:
            return json.dumps({"error": "Missing required parameters: station_id, start_ts, end_ts"})

        start_dt = GetWaterLevels._parse_iso(start_ts)
        end_dt = GetWaterLevels._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            return json.dumps({"error": "Invalid time range. Use ISO 8601 and ensure start < end."})

        items = data.get("water_levels", [])
        for rec in items:
            if rec.get("station_id") != station_id:
                continue
            rec_start = GetWaterLevels._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWaterLevels._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []
                vals = rec.get("water_level_m") or []
                idxs = [i for i, t in enumerate(ts_list)
                        if (GetWaterLevels._parse_iso(t) or start_dt) and (start_dt <= GetWaterLevels._parse_iso(t) <= end_dt)]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                return json.dumps({
                    "station_id": station_id,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "water_level_m": out_vals,
                    "units": rec.get("units", "meters"),
                    "datum": rec.get("datum_nullable")
                })

        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_water_levels",
                "description": "Returns observed water levels for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string", "description": "NOAA station id (e.g., '9414290')."},
                        "start_ts": {"type": "string", "description": "Start timestamp (ISO 8601)."},
                        "end_ts": {"type": "string", "description": "End timestamp (ISO 8601)."}
                    },
                    "required": ["station_id", "start_ts", "end_ts"]
                }
            }
        }

class GetModelMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        if not model_name:
            return json.dumps({"error": "Missing model_name"})
        for m in data.get("metrics", []):
            if m.get("model_name") == model_name:
                return json.dumps({
                    "model_name": model_name,
                    "auc": m.get("auc_nullable"),
                    "accuracy": m.get("accuracy_nullable")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_model_metrics",
                "description": "Return stored AUC/accuracy for a given model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }

class CreateEtlRunRecord(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> Optional[datetime]:
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        run_id = kwargs.get("run_id")
        input_paths = kwargs.get("input_paths", [])
        output_paths = kwargs.get("output_paths", [])
        started_ts = kwargs.get("started_ts")
        finished_ts_nullable = kwargs.get("finished_ts_nullable")
        messages = kwargs.get("messages", [])

        if not run_id or not isinstance(input_paths, list) or not isinstance(output_paths, list):
            return json.dumps({"error": "Missing or invalid: run_id, input_paths, output_paths."})
        if not started_ts or not CreateEtlRunRecord._parse_iso(started_ts):
            return json.dumps({"error": "Invalid started_ts (ISO 8601 UTC)."})
        if finished_ts_nullable is not None and not CreateEtlRunRecord._parse_iso(finished_ts_nullable):
            return json.dumps({"error": "Invalid finished_ts_nullable (ISO 8601 UTC or null)."})
        if not isinstance(messages, list):
            return json.dumps({"error": "messages must be a list."})

        etl_runs = data.get("etl_runs", [])
        for rec in etl_runs:
            if rec.get("run_id") == run_id:
                return json.dumps(rec)

        new_rec = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "started_ts": started_ts,
            "finished_ts_nullable": finished_ts_nullable,
            "messages": messages
        }
        etl_runs.append(new_rec)
        data["etl_runs"] = etl_runs
        return json.dumps(new_rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"create_etl_run_record",
                "description":"Create an ETL run record with the canonical MWP fields only.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "run_id":{"type":"string"},
                        "input_paths":{"type":"array","items":{"type":"string"}},
                        "output_paths":{"type":"array","items":{"type":"string"}},
                        "started_ts":{"type":"string"},
                        "finished_ts_nullable":{"type":["string","null"]},
                        "messages":{"type":"array","items":{"type":"string"}}
                    },
                    "required":["run_id","input_paths","output_paths","started_ts","messages"]
                }
            }
        }

class GetProcessedTimeseriesMetadata(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        csv_path = kwargs.get("csv_path")
        if not csv_path:
            return json.dumps({"error": "Missing csv_path"})
        items = data.get("processed_timeseries", [])
        for rec in items:
            if rec.get("csv_path") == csv_path:
                return json.dumps({
                    "csv_path": rec.get("csv_path"),
                    "row_count": rec.get("row_count"),
                    "min_timestamp": rec.get("min_timestamp"),
                    "max_timestamp": rec.get("max_timestamp"),
                    "columns": rec.get("columns")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"get_processed_timeseries_metadata",
                "description":"Returns row_count and metadata for a processed timeseries CSV path.",
                "parameters":{"type":"object","properties":{"csv_path":{"type":"string"}},"required":["csv_path"]}
            }
        }

class CreateSplitSummaryRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        method = kwargs.get("method")
        test_fraction = kwargs.get("test_fraction")
        train_index_count = kwargs.get("train_index_count")
        test_index_count = kwargs.get("test_index_count")
        split_summary_json_path = kwargs.get("split_summary_json_path")
        split_ts = kwargs.get("split_ts")

        if method != "time_based":
            return json.dumps({"error": "Only 'time_based' method is supported."})
        try:
            test_fraction = float(test_fraction)
            train_index_count = int(train_index_count)
            test_index_count = int(test_index_count)
        except Exception:
            return json.dumps({"error":"Invalid numeric fields."})
        if not split_summary_json_path or not isinstance(split_summary_json_path, str):
            return json.dumps({"error": "split_summary_json_path is required."})
        if not split_ts or not isinstance(split_ts, str):
            return json.dumps({"error": "split_ts is required (ISO 8601)."})

        ds = data.get("dataset_split", [])
        for rec in ds:
            if (rec.get("method") == method and
                rec.get("test_fraction") == test_fraction and
                rec.get("train_index_count") == train_index_count and
                rec.get("test_index_count") == test_index_count and
                rec.get("split_summary_json_path") == split_summary_json_path and
                rec.get("split_ts") == split_ts):
                return json.dumps(rec)

        new_rec = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts
        }
        ds.append(new_rec)
        data["dataset_split"] = ds
        return json.dumps(new_rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"create_split_summary_record",
                "description":"Creates a deterministic split summary record in dataset_split (no extra fields).",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "method":{"type":"string","enum":["time_based"]},
                        "test_fraction":{"type":"number"},
                        "train_index_count":{"type":"integer"},
                        "test_index_count":{"type":"integer"},
                        "split_summary_json_path":{"type":"string"},
                        "split_ts":{"type":"string"}
                    },
                    "required":["method","test_fraction","train_index_count","test_index_count","split_summary_json_path","split_ts"]
                }
            }
        }

class ResolveCitySlug(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        if not city or not isinstance(city, str):
            return json.dumps({"error": "Missing city"})
        mapping = {"San Francisco": "sf", "Miami": "miami", "Boston": "boston", "Seattle": "seattle", "Charleston": "charleston", "New York": "new_york", "Los Angeles": "los_angeles"}
        slug = mapping.get(city, city.strip().lower().replace(" ", "_"))
        return json.dumps({"city": city, "city_slug": slug})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"resolve_city_slug","description":"Returns canonical city_slug used by file paths (e.g., 'San Francisco' -> 'sf').","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}

class BuildProcessedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        if not city_slug:
            return json.dumps({"error":"Missing city_slug"})
        path = f"/data/processed/timeseries_{city_slug}_weather.csv"
        return json.dumps({"city_slug": city_slug, "csv_path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_processed_timeseries_path",
                "description":"Builds canonical processed timeseries CSV path for a given city_slug.",
                "parameters":{"type":"object","properties":{"city_slug":{"type":"string"}},"required":["city_slug"]}
            }
        }

class ComputeSplitCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_count = kwargs.get("row_count")
        test_fraction = kwargs.get("test_fraction")
        try:
            row_count = int(row_count)
            test_fraction = float(test_fraction)
        except Exception:
            return json.dumps({"error":"row_count must be int and test_fraction must be float"})
        if row_count < 0 or not (0 < test_fraction < 1):
            return json.dumps({"error":"Invalid values for row_count or test_fraction"})
        train_index_count = int(row_count * (1 - test_fraction))
        test_index_count = row_count - train_index_count
        return json.dumps({
            "row_count": row_count,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"compute_split_counts",
                "description":"Computes train/test counts given row_count and test_fraction (floor rule).",
                "parameters":{"type":"object","properties":{"row_count":{"type":"integer"},"test_fraction":{"type":"number"}},"required":["row_count","test_fraction"]}
            }
        }

class GetModelConfigParam(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        saved_json_path = kwargs.get("saved_json_path")
        if not saved_json_path:
            return json.dumps({"error": "Missing saved_json_path"})
        for rec in data.get("model_config", []):
            if rec.get("saved_json_path") == saved_json_path:
                return json.dumps({
                    "saved_json_path": saved_json_path,
                    "test_split_fraction": rec.get("test_split_fraction_nullable"),
                    "classification_threshold_m": rec.get("classification_threshold_m_nullable"),
                    "precip_24h_threshold_mm": rec.get("precip_24h_threshold_mm_nullable"),
                    "random_seed": rec.get("random_seed_nullable"),
                    "created_ts": rec.get("created_ts")
                })
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"get_model_config_param",
                "description":"Returns parameters from a model_config record identified by saved_json_path.",
                "parameters":{"type":"object","properties":{"saved_json_path":{"type":"string"}},"required":["saved_json_path"]}
            }
        }

class GetSplitSummaryDefaults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get("path")
        if not path:
            return json.dumps({"error": "Missing path"})
        items = data.get("file_store", [])
        for blob in items:
            if blob.get("paths") and path in blob.get("paths"):
                # This branch would require searching in arrays; not used here.
                break

        # Direct lookup from parsed contents (processed file registry)
        texts = data.get("file_store", [])
        for rec in texts:
            if rec.get("paths") and path in rec.get("paths"):
                try:
                    payload = json.loads(rec.get("file_contents_text")[0])
                    return json.dumps({
                        "method": payload.get("method"),
                        "test_fraction": payload.get("test_fraction"),
                        "total_samples": payload.get("total_samples"),
                        "train_samples": payload.get("train_samples"),
                        "test_samples": payload.get("test_samples"),
                        "train_date_range": payload.get("train_date_range"),
                        "test_date_range": payload.get("test_date_range"),
                        "feature_columns": payload.get("feature_columns"),
                        "target_column": payload.get("target_column"),
                        "split_ts": payload.get("split_ts")
                    })
                except Exception:
                    return json.dumps({"error": "Unable to parse JSON at given path"})
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_split_summary_defaults",
                "description": "Returns defaults (incl. split_ts) from a known split summary JSON path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Absolute path to split summary JSON (e.g., /processed_data/split_summary.json)."
                        }
                    },
                    "required": ["path"]
                }
            }
        }

class BuildSplitSummaryPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        method = kwargs.get("method")
        split_ts = kwargs.get("split_ts")
        if not city_slug or not method or not split_ts:
            return json.dumps({"error":"Missing city_slug, method, or split_ts"})
        ymd = split_ts[:10].replace("-", "")
        path = f"/data/splits/{city_slug}_{method}_split_{ymd}.json"
        return json.dumps({"city_slug": city_slug, "method": method, "split_ts": split_ts, "split_summary_json_path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_split_summary_path",
                "description":"Builds canonical split_summary_json_path from city_slug, method, and split_ts.",
                "parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"method":{"type":"string"},"split_ts":{"type":"string"}},"required":["city_slug","method","split_ts"]}
            }
        }

class GetModelFeatures(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        if not model_name:
            return json.dumps({"error":"Missing model_name"})
        for rec in data.get("models", []):
            if rec.get("model_name") == model_name:
                return json.dumps({"model_name": model_name, "feature_names": rec.get("feature_names", [])})
        return json.dumps({})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_model_features","description":"Returns required feature_names for a model_name from models.","parameters":{"type":"object","properties":{"model_name":{"type":"string"}},"required":["model_name"]}}}

class GetModelInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        if not model_name:
            return json.dumps({"error":"Missing model_name"})
        for rec in data.get("models", []):
            if rec.get("model_name") == model_name:
                return json.dumps({"model_name": model_name, "model_path": rec.get("model_path")})
        return json.dumps({})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_model_info","description":"Returns model artifact info such as model_path for a model_name.","parameters":{"type":"object","properties":{"model_name":{"type":"string"}},"required":["model_name"]}}}

class BuildFeaturesCsvPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        if not city_slug:
            return json.dumps({"error":"Missing city_slug"})
        return json.dumps({"city_slug": city_slug, "features_csv_path": "/processed_data/features.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_features_csv_path","description":"Returns canonical features CSV path for a city_slug.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"}},"required":["city_slug"]}}}

class ComputeFeatureCoverage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = kwargs.get("required_features") or []
        available = kwargs.get("available_features") or []
        req = sorted([str(x) for x in required])
        ava = sorted([str(x) for x in available])
        present = [x for x in req if x in ava]
        missing = [x for x in req if x not in ava]
        present_count = len(present)
        required_count = len(req)
        missing_count = len(missing)
        coverage = 0.0 if required_count == 0 else present_count / float(required_count)
        return json.dumps({"present_features": present, "missing_features": missing, "present_count": present_count, "required_count": required_count, "missing_count": missing_count, "coverage": coverage})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"compute_feature_coverage","description":"Computes present/missing features and coverage ratio given required and available feature lists.","parameters":{"type":"object","properties":{"required_features":{"type":"array","items":{"type":"string"}},"available_features":{"type":"array","items":{"type":"string"}}},"required":["required_features","available_features"]}}}

class BuildFeatureValidationPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        model_name = kwargs.get("model_name")
        created_ts = kwargs.get("created_ts")
        if not city_slug or not model_name or not created_ts:
            return json.dumps({"error":"Missing city_slug, model_name or created_ts"})
        ymd = created_ts[:10].replace("-", "")
        path = f"/processed_data/feature_validation_{city_slug}_{model_name}_{ymd}.json"
        return json.dumps({"city_slug": city_slug, "model_name": model_name, "ymd": ymd, "feature_validation_json_path": path})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_feature_validation_path","description":"Builds canonical feature validation JSON path from city_slug, model_name, and created_ts.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"created_ts":{"type":"string"}},"required":["city_slug","model_name","created_ts"]}}}

class BuildFeatureValidationRunId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        model_name = kwargs.get("model_name")
        created_ts = kwargs.get("created_ts")
        if not city_slug or not model_name or not created_ts:
            return json.dumps({"error":"Missing city_slug, model_name or created_ts"})
        ymd = created_ts[:10].replace("-", "")
        run_id = f"fv_{city_slug}_{model_name}_{ymd}_v1"
        return json.dumps({"run_id": run_id, "ymd": ymd})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_feature_validation_run_id","description":"Builds canonical run_id for feature validation from city_slug, model_name, and created_ts.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"created_ts":{"type":"string"}},"required":["city_slug","model_name","created_ts"]}}}

class BuildInputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        features_csv_path = kwargs.get("features_csv_path")
        model_path = kwargs.get("model_path")
        if not features_csv_path or not model_path:
            return json.dumps({"error":"Missing features_csv_path or model_path"})
        return json.dumps({"input_paths": [features_csv_path, model_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_input_paths","description":"Builds input_paths array for feature validation from features_csv_path and model_path.","parameters":{"type":"object","properties":{"features_csv_path":{"type":"string"},"model_path":{"type":"string"}},"required":["features_csv_path","model_path"]}}}

class BuildOutputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feature_validation_json_path = kwargs.get("feature_validation_json_path")
        if not feature_validation_json_path:
            return json.dumps({"error":"Missing feature_validation_json_path"})
        return json.dumps({"output_paths": [feature_validation_json_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_output_paths","description":"Wraps the feature_validation_json_path into the output_paths array.","parameters":{"type":"object","properties":{"feature_validation_json_path":{"type":"string"}},"required":["feature_validation_json_path"]}}}

class GetFvpTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"started_ts": "2024-03-17T10:20:00Z", "finished_ts_nullable": "2024-03-17T10:25:00Z"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_fvp_timestamps","description":"Returns canonical started_ts and finished_ts_nullable for FVP.","parameters":{"type":"object","properties":{}}}}

class BuildFeatureValidationMessages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        feature_validation_json_path = kwargs.get("feature_validation_json_path")
        present_count = kwargs.get("present_count")
        required_count = kwargs.get("required_count")
        missing_features = kwargs.get("missing_features") or []
        if model_name is None or feature_validation_json_path is None or present_count is None or required_count is None:
            return json.dumps({"error":"Missing required fields"})
        miss = sorted([str(x) for x in missing_features])
        miss_str = "none" if len(miss) == 0 else ", ".join(miss)
        messages = [
            f"Feature validation for {model_name}: {present_count}/{required_count} required features present.",
            f"Missing features: {miss_str}.",
            f"Validated file: {feature_validation_json_path}."
        ]
        return json.dumps({"messages": messages})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type":"function",
            "function":{
                "name":"build_feature_validation_messages",
                "description":"Builds deterministic FVP messages with sorted missing features and the validation artifact path.",
                "parameters":{
                    "type":"object",
                    "properties":{
                        "model_name":{"type":"string"},
                        "feature_validation_json_path":{"type":"string"},
                        "present_count":{"type":"integer"},
                        "required_count":{"type":"integer"},
                        "missing_features":{"type":"array","items":{"type":"string"}}
                    },
                    "required":["model_name","feature_validation_json_path","present_count","required_count"]
                }
            }
        }

class BuildMergedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")
        if not city_slug or not start_ts or not end_ts:
            return json.dumps({"error":"Missing city_slug, start_ts, end_ts"})
        y0 = start_ts[:10].replace("-","")
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"merged_timeseries_path": f"/processed_data/merged_timeseries_{city_slug}_{y0}_{y1}.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_merged_timeseries_path","description":"Builds canonical merged timeseries path from city_slug and analysis window.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"start_ts":{"type":"string"},"end_ts":{"type":"string"}},"required":["city_slug","start_ts","end_ts"]}}}

class BuildMetricsSummaryPath(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        model_name = kwargs.get("model_name")
        end_ts = kwargs.get("end_ts")
        if not model_name or not end_ts:
            return json.dumps({"error":"Missing model_name or end_ts"})
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"metrics_summary_path": f"/processed_data/metrics_summary_{model_name}_{y1}.csv"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_metrics_summary_path","description":"Builds canonical metrics summary CSV path from model_name and end_ts.","parameters":{"type":"object","properties":{"model_name":{"type":"string"},"end_ts":{"type":"string"}},"required":["model_name","end_ts"]}}}

class GetMtpTimestamps(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"started_ts":"2024-03-17T09:30:00Z","finished_ts_nullable":"2024-03-17T11:15:00Z"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_mtp_timestamps","description":"Returns canonical started_ts and finished_ts for MTP.","parameters":{"type":"object","properties":{},"required":[]}}}

class BuildMtpMessages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        train_samples = kwargs.get("train_samples")
        test_samples = kwargs.get("test_samples")
        model_path = kwargs.get("model_path")
        if train_samples is None or test_samples is None or not model_path:
            return json.dumps({"error":"Missing train_samples, test_samples, or model_path"})
        messages = [
            f"Training samples: {int(train_samples)}",
            f"Test samples: {int(test_samples)}",
            f"Model saved to: {model_path}"
        ]
        return json.dumps({"messages": messages})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_messages","description":"Builds deterministic MTP messages list.","parameters":{"type":"object","properties":{"train_samples":{"type":"integer"},"test_samples":{"type":"integer"},"model_path":{"type":"string"}},"required":["train_samples","test_samples","model_path"]}}}

class BuildMtpInputPaths(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        merged_timeseries_path = kwargs.get("merged_timeseries_path")
        features_csv_path = kwargs.get("features_csv_path")
        split_summary_json_path = kwargs.get("split_summary_json_path")
        if not merged_timeseries_path or not features_csv_path or not split_summary_json_path:
            return json.dumps({"error":"Missing merged_timeseries_path, features_csv_path, or split_summary_json_path"})
        return json.dumps({"input_paths":[merged_timeseries_path, features_csv_path, split_summary_json_path]})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_input_paths","description":"Builds input_paths array for MTP.","parameters":{"type":"object","properties":{"merged_timeseries_path":{"type":"string"},"features_csv_path":{"type":"string"},"split_summary_json_path":{"type":"string"}},"required":["merged_timeseries_path","features_csv_path","split_summary_json_path"]}}}

class BuildMtpRunId(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_slug = kwargs.get("city_slug")
        model_name = kwargs.get("model_name")
        start_ts = kwargs.get("start_ts")
        end_ts = kwargs.get("end_ts")
        if not city_slug or not model_name or not start_ts or not end_ts:
            return json.dumps({"error":"Missing city_slug, model_name, start_ts, or end_ts"})
        y0 = start_ts[:10].replace("-","")
        y1 = end_ts[:10].replace("-","")
        return json.dumps({"run_id": f"mt_{city_slug}_{model_name}_{y0}_{y1}_v1"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"build_mtp_run_id","description":"Builds canonical MTP run_id from city_slug, model_name, and analysis window.","parameters":{"type":"object","properties":{"city_slug":{"type":"string"},"model_name":{"type":"string"},"start_ts":{"type":"string"},"end_ts":{"type":"string"}},"required":["city_slug","model_name","start_ts","end_ts"]}}}

TOOLS=[
    BuildMergedTimeseriesPath(),
    BuildMetricsSummaryPath(),
    GetMtpTimestamps(),
    BuildMtpInputPaths(),
    BuildMtpMessages(),
    BuildMtpRunId(),
    GetWeatherForecast(),
    GetTidePredictions(),
    GetWaterLevels(),
    GetModelMetrics(),
    CreateEtlRunRecord(),
    GetProcessedTimeseriesMetadata(),
    CreateSplitSummaryRecord(),
    ResolveCitySlug(),
    BuildProcessedTimeseriesPath(),
    ComputeSplitCounts(),
    GetModelConfigParam(),
    GetSplitSummaryDefaults(),
    BuildSplitSummaryPath(),
    GetModelFeatures(),
    BuildFeaturesCsvPath(),
    ComputeFeatureCoverage(),
    BuildFeatureValidationPath(),
    BuildFeatureValidationRunId(),
    BuildInputPaths(),
    BuildOutputPaths(),
    GetFvpTimestamps(),
    BuildFeatureValidationMessages(),
    GetModelInfo()
]
