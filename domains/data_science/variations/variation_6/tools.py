import json
from datetime import datetime
from typing import Any

from domains.dto import Tool


class GetWeatherForecast(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> datetime | None:
        pass
        try:
            #accepts "YYYY-MM-DDTHH:MM:SSZ" and "YYYY-MM-DDTHH:MM:SS"
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: dict[str, Any], city: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city or not start_ts or not end_ts:
            payload = {"error": "Missing required parameters: city, start_ts, end_ts"}
            out = json.dumps(payload)
            return out

        start_dt = GetWeatherForecast._parse_iso(start_ts)
        end_dt = GetWeatherForecast._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            payload = {"error": "Invalid time range. Use ISO 8601 and ensure start < end."}
            out = json.dumps(payload)
            return out

        items = data.get("weather_forecasts", [])
        for rec in items:
            if rec.get("city") != city:
                continue
            rec_start = GetWeatherForecast._parse_iso(rec.get("start_ts", ""))
            rec_end = GetWeatherForecast._parse_iso(rec.get("end_ts", ""))
            if not rec_start or not rec_end:
                continue
            # we require complete coverage of the requested range
            if rec_start <= start_dt and rec_end >= end_dt:
                ts_list = rec.get("timestamps") or []

                # sub-selects the range
                def in_range(ts):
                    dt = GetWeatherForecast._parse_iso(ts)
                    return dt is not None and (start_dt <= dt <= end_dt)

                out_ts = [t for t in ts_list if in_range(t)]
                # align series (nullable may exist)
                precip = rec.get("precipitation_mm_hr_nullable") or []
                temp = rec.get("temperature_2m_c_nullable") or []
                wind = rec.get("wind_speed_10m_ms_nullable") or []

                # cut by the same selected indices
                # (assumes position alignment with timestamps)
                idxs = [i for i, t in enumerate(ts_list) if t in out_ts]

                def sel(arr):
                    return [arr[i] for i in idxs if i < len(arr)]

                result = {
                    "city": city,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "temperature_c": sel(temp),
                    "precipitation_mm_hr": sel(precip),
                    "wind_speed_10m_ms": sel(wind),
                }
                payload = result
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetWeatherForecast",
                "description": "Returns hourly weather forecast series for a city within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City name exactly as stored in the database.",
                        },
                        "start_ts": {
                            "type": "string",
                            "description": "Start timestamp (ISO 8601).",
                        },
                        "end_ts": {
                            "type": "string",
                            "description": "End timestamp (ISO 8601).",
                        },
                    },
                    "required": ["city", "start_ts", "end_ts"],
                },
            },
        }


class GetTidePredictions(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        pass
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not station_id or not start_ts or not end_ts:
            payload = {"error": "Missing required parameters: station_id, start_ts, end_ts"}
            out = json.dumps(payload)
            return out

        start_dt = GetTidePredictions._parse_iso(start_ts)
        end_dt = GetTidePredictions._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            payload = {"error": "Invalid time range. Use ISO 8601 and ensure start < end."}
            out = json.dumps(payload)
            return out

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
                idxs = [
                    i
                    for i, t in enumerate(ts_list)
                    if (GetTidePredictions._parse_iso(t) or start_dt)
                    and (start_dt <= GetTidePredictions._parse_iso(t) <= end_dt)
                ]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                payload = {
                    "station_id": station_id,
                    "start_ts": start_ts,
                    "end_ts": end_ts,
                    "timestamps": out_ts,
                    "tide_pred_m": out_vals,
                    "units": rec.get("units", "meters"),
                }
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetTidePredictions",
                "description": "Returns tide prediction series for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "NOAA station id (e.g., '9414290').",
                        },
                        "start_ts": {
                            "type": "string",
                            "description": "Start timestamp (ISO 8601).",
                        },
                        "end_ts": {
                            "type": "string",
                            "description": "End timestamp (ISO 8601).",
                        },
                    },
                    "required": ["station_id", "start_ts", "end_ts"],
                },
            },
        }


class GetWaterLevels(Tool):
    @staticmethod
    def _parse_iso(ts: str):
        pass
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not station_id or not start_ts or not end_ts:
            payload = {"error": "Missing required parameters: station_id, start_ts, end_ts"}
            out = json.dumps(
                payload)
            return out

        start_dt = GetWaterLevels._parse_iso(start_ts)
        end_dt = GetWaterLevels._parse_iso(end_ts)
        if not start_dt or not end_dt or start_dt >= end_dt:
            payload = {"error": "Invalid time range. Use ISO 8601 and ensure start < end."}
            out = json.dumps(
                payload)
            return out

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
                idxs = [
                    i
                    for i, t in enumerate(ts_list)
                    if (GetWaterLevels._parse_iso(t) or start_dt)
                    and (start_dt <= GetWaterLevels._parse_iso(t) <= end_dt)
                ]
                out_ts = [ts_list[i] for i in idxs if i < len(ts_list)]
                out_vals = [vals[i] for i in idxs if i < len(vals)]
                payload = {
                        "station_id": station_id,
                        "start_ts": start_ts,
                        "end_ts": end_ts,
                        "timestamps": out_ts,
                        "water_level_m": out_vals,
                        "units": rec.get("units", "meters"),
                        "datum": rec.get("datum_nullable"),
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetWaterLevels",
                "description": "Returns observed water levels for a NOAA station within a given ISO-8601 time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {
                            "type": "string",
                            "description": "NOAA station id (e.g., '9414290').",
                        },
                        "start_ts": {
                            "type": "string",
                            "description": "Start timestamp (ISO 8601).",
                        },
                        "end_ts": {
                            "type": "string",
                            "description": "End timestamp (ISO 8601).",
                        },
                    },
                    "required": ["station_id", "start_ts", "end_ts"],
                },
            },
        }


class GetModelMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None) -> str:
        if not model_name:
            payload = {"error": "Missing model_name"}
            out = json.dumps(payload)
            return out
        for m in data.get("metrics", []):
            if m.get("model_name") == model_name:
                payload = {
                    "model_name": model_name,
                    "auc": m.get("auc_nullable"),
                    "accuracy": m.get("accuracy_nullable"),
                }
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetModelMetrics",
                "description": "Return stored AUC/accuracy for a given model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class CreateEtlRunRecord(Tool):
    @staticmethod
    def _parse_iso(ts: str) -> datetime | None:
        pass
        try:
            return datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            return None

    @staticmethod
    def invoke(
        data: dict[str, Any],
        finished_ts_nullable: str = None,
        input_paths: list = [],
        messages: list = [],
        output_paths: list = [],
        run_id: str = None,
        started_ts: str = None
    ) -> str:
        if (
            not run_id
            or not isinstance(input_paths, list)
            or not isinstance(output_paths, list)
        ):
            payload = {"error": "Missing or invalid: run_id, input_paths, output_paths."}
            out = json.dumps(payload)
            return out
        if not started_ts or not CreateEtlRunRecord._parse_iso(started_ts):
            payload = {"error": "Invalid started_ts (ISO 8601 UTC)."}
            out = json.dumps(payload)
            return out
        if finished_ts_nullable is not None and not CreateEtlRunRecord._parse_iso(
            finished_ts_nullable
        ):
            payload = {"error": "Invalid finished_ts_nullable (ISO 8601 UTC or null)."}
            out = json.dumps(payload)
            return out
        if not isinstance(messages, list):
            payload = {"error": "messages must be a list."}
            out = json.dumps(payload)
            return out

        etl_runs = data.get("etl_runs", [])
        for rec in etl_runs:
            if rec.get("run_id") == run_id:
                payload = rec
                out = json.dumps(payload)
                return out

        new_rec = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "started_ts": started_ts,
            "finished_ts_nullable": finished_ts_nullable,
            "messages": messages,
        }
        etl_runs.append(new_rec)
        data["etl_runs"] = etl_runs
        payload = new_rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateEtlRunRecord",
                "description": "Create an ETL run record with the canonical MWP fields only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "input_paths": {"type": "array", "items": {"type": "string"}},
                        "output_paths": {"type": "array", "items": {"type": "string"}},
                        "started_ts": {"type": "string"},
                        "finished_ts_nullable": {"type": ["string", "null"]},
                        "messages": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "run_id",
                        "input_paths",
                        "output_paths",
                        "started_ts",
                        "messages",
                    ],
                },
            },
        }


class GetProcessedTimeseriesMetadata(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], csv_path: str = None) -> str:
        if not csv_path:
            payload = {"error": "Missing csv_path"}
            out = json.dumps(payload)
            return out
        items = data.get("processed_timeseries", [])
        for rec in items:
            if rec.get("csv_path") == csv_path:
                payload = {
                        "csv_path": rec.get("csv_path"),
                        "row_count": rec.get("row_count"),
                        "min_timestamp": rec.get("min_timestamp"),
                        "max_timestamp": rec.get("max_timestamp"),
                        "columns": rec.get("columns"),
                    }
                out = json.dumps(
                    payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetProcessedTimeseriesMetadata",
                "description": "Returns row_count and metadata for a processed timeseries CSV path.",
                "parameters": {
                    "type": "object",
                    "properties": {"csv_path": {"type": "string"}},
                    "required": ["csv_path"],
                },
            },
        }


class CreateSplitSummaryRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        method: str = None,
        test_fraction: float = None,
        train_index_count: int = None,
        test_index_count: int = None,
        split_summary_json_path: str = None,
        split_ts: str = None
    ) -> str:
        if method != "time_based":
            payload = {"error": "Only 'time_based' method is supported."}
            out = json.dumps(payload)
            return out
        try:
            test_fraction = float(test_fraction)
            train_index_count = int(train_index_count)
            test_index_count = int(test_index_count)
        except Exception:
            payload = {"error": "Invalid numeric fields."}
            out = json.dumps(payload)
            return out
        if not split_summary_json_path or not isinstance(split_summary_json_path, str):
            payload = {"error": "split_summary_json_path is required."}
            out = json.dumps(payload)
            return out
        if not split_ts or not isinstance(split_ts, str):
            payload = {"error": "split_ts is required (ISO 8601)."}
            out = json.dumps(payload)
            return out

        ds = data.get("dataset_split", [])
        for rec in ds:
            if (
                rec.get("method") == method
                and rec.get("test_fraction") == test_fraction
                and rec.get("train_index_count") == train_index_count
                and rec.get("test_index_count") == test_index_count
                and rec.get("split_summary_json_path") == split_summary_json_path
                and rec.get("split_ts") == split_ts
            ):
                payload = rec
                out = json.dumps(payload)
                return out

        new_rec = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        ds.append(new_rec)
        data["dataset_split"] = ds
        payload = new_rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateSplitSummaryRecord",
                "description": "Creates a deterministic split summary record in dataset_split (no extra fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string", "enum": ["time_based"]},
                        "test_fraction": {"type": "number"},
                        "train_index_count": {"type": "integer"},
                        "test_index_count": {"type": "integer"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": [
                        "method",
                        "test_fraction",
                        "train_index_count",
                        "test_index_count",
                        "split_summary_json_path",
                        "split_ts",
                    ],
                },
            },
        }


class ResolveCitySlug(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city: str = None) -> str:
        if not city or not isinstance(city, str):
            payload = {"error": "Missing city"}
            out = json.dumps(payload)
            return out
        mapping = {
            "San Francisco": "sf",
            "Miami": "miami",
            "Boston": "boston",
            "Seattle": "seattle",
            "Charleston": "charleston",
            "New York": "new_york",
            "Los Angeles": "los_angeles",
        }
        slug = mapping.get(city, city.strip().lower().replace(" ", "_"))
        payload = {"city": city, "city_slug": slug}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ResolveCitySlug",
                "description": "Returns canonical city_slug used by file paths (e.g., 'San Francisco' -> 'sf').",
                "parameters": {
                    "type": "object",
                    "properties": {"city": {"type": "string"}},
                    "required": ["city"],
                },
            },
        }


class BuildProcessedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None) -> str:
        if not city_slug:
            payload = {"error": "Missing city_slug"}
            out = json.dumps(payload)
            return out
        path = f"/data/processed/timeseries_{city_slug}_weather.csv"
        payload = {"city_slug": city_slug, "csv_path": path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildProcessedTimeseriesPath",
                "description": "Builds canonical processed timeseries CSV path for a given city_slug.",
                "parameters": {
                    "type": "object",
                    "properties": {"city_slug": {"type": "string"}},
                    "required": ["city_slug"],
                },
            },
        }


class ComputeSplitCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], row_count: int = None, test_fraction: float = None) -> str:
        try:
            row_count = int(row_count)
            test_fraction = float(test_fraction)
        except Exception:
            payload = {"error": "row_count must be int and test_fraction must be float"}
            out = json.dumps(payload)
            return out
        if row_count < 0 or not (0 < test_fraction < 1):
            payload = {"error": "Invalid values for row_count or test_fraction"}
            out = json.dumps(payload)
            return out
        train_index_count = int(row_count * (1 - test_fraction))
        test_index_count = row_count - train_index_count
        payload = {
            "row_count": row_count,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeSplitCounts",
                "description": "Computes train/test counts given row_count and test_fraction (floor rule).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_count": {"type": "integer"},
                        "test_fraction": {"type": "number"},
                    },
                    "required": ["row_count", "test_fraction"],
                },
            },
        }


class GetModelConfigParam(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], saved_json_path: str = None) -> str:
        if not saved_json_path:
            payload = {"error": "Missing saved_json_path"}
            out = json.dumps(payload)
            return out
        for rec in data.get("model_config", []):
            if rec.get("saved_json_path") == saved_json_path:
                payload = {
                    "saved_json_path": saved_json_path,
                    "test_split_fraction": rec.get("test_split_fraction_nullable"),
                    "classification_threshold_m": rec.get(
                        "classification_threshold_m_nullable"
                    ),
                    "precip_24h_threshold_mm": rec.get(
                        "precip_24h_threshold_mm_nullable"
                    ),
                    "random_seed": rec.get("random_seed_nullable"),
                    "created_ts": rec.get("created_ts"),
                }
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetModelConfigParam",
                "description": "Returns parameters from a model_config record identified by saved_json_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"saved_json_path": {"type": "string"}},
                    "required": ["saved_json_path"],
                },
            },
        }


class GetSplitSummaryDefaults(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], path: str = None) -> str:
        if not path:
            payload = {"error": "Missing path"}
            out = json.dumps(payload)
            return out
        items = data.get("file_store", [])
        for blob in items:
            if blob.get("paths") and path in blob.get("paths"):
                # This path would necessitate searching through arrays; not utilized here.
                break

        # Immediate retrieval from parsed data (processed file registry)
        texts = data.get("file_store", [])
        for rec in texts:
            if rec.get("paths") and path in rec.get("paths"):
                try:
                    payload = json.loads(rec.get("file_contents_text")[0])
                    payload = {
                        "method": payload.get("method"),
                        "test_fraction": payload.get("test_fraction"),
                        "total_samples": payload.get("total_samples"),
                        "train_samples": payload.get("train_samples"),
                        "test_samples": payload.get("test_samples"),
                        "train_date_range": payload.get("train_date_range"),
                        "test_date_range": payload.get("test_date_range"),
                        "feature_columns": payload.get("feature_columns"),
                        "target_column": payload.get("target_column"),
                        "split_ts": payload.get("split_ts"),
                    }
                    out = json.dumps(payload)
                    return out
                except Exception:
                    payload = {"error": "Unable to parse JSON at given path"}
                    out = json.dumps(payload)
                    return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetSplitSummaryDefaults",
                "description": "Returns defaults (incl. split_ts) from a known split summary JSON path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Absolute path to split summary JSON (e.g., /processed_data/split_summary.json).",
                        }
                    },
                    "required": ["path"],
                },
            },
        }


class BuildSplitSummaryPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, method: str = None, split_ts: str = None) -> str:
        if not city_slug or not method or not split_ts:
            payload = {"error": "Missing city_slug, method, or split_ts"}
            out = json.dumps(payload)
            return out
        ymd = split_ts[:10].replace("-", "")
        path = f"/data/splits/{city_slug}_{method}_split_{ymd}.json"
        payload = {
            "city_slug": city_slug,
            "method": method,
            "split_ts": split_ts,
            "split_summary_json_path": path,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildSplitSummaryPath",
                "description": "Builds canonical split_summary_json_path from city_slug, method, and split_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "method": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "method", "split_ts"],
                },
            },
        }


class GetModelFeatures(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None) -> str:
        if not model_name:
            payload = {"error": "Missing model_name"}
            out = json.dumps(payload)
            return out
        for rec in data.get("models", []):
            if rec.get("model_name") == model_name:
                payload = {
                    "model_name": model_name,
                    "feature_names": rec.get("feature_names", []),
                }
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetModelFeatures",
                "description": "Returns required feature_names for a model_name from models.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class GetModelInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None) -> str:
        if not model_name:
            payload = {"error": "Missing model_name"}
            out = json.dumps(payload)
            return out
        for rec in data.get("models", []):
            if rec.get("model_name") == model_name:
                payload = {"model_name": model_name, "model_path": rec.get("model_path")}
                out = json.dumps(payload)
                return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetModelInfo",
                "description": "Returns model artifact info such as model_path for a model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class BuildFeaturesCsvPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None) -> str:
        if not city_slug:
            payload = {"error": "Missing city_slug"}
            out = json.dumps(payload)
            return out
        payload = {
            "city_slug": city_slug,
            "features_csv_path": "/processed_data/features.csv",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildFeaturesCsvPath",
                "description": "Returns canonical features CSV path for a city_slug.",
                "parameters": {
                    "type": "object",
                    "properties": {"city_slug": {"type": "string"}},
                    "required": ["city_slug"],
                },
            },
        }


class ComputeFeatureCoverage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], required_features: list = None, available_features: list = None) -> str:
        required = required_features or []
        available = available_features or []
        req = sorted([str(x) for x in required])
        ava = sorted([str(x) for x in available])
        present = [x for x in req if x in ava]
        missing = [x for x in req if x not in ava]
        present_count = len(present)
        required_count = len(req)
        missing_count = len(missing)
        coverage = 0.0 if required_count == 0 else present_count / float(required_count)
        payload = {
                "present_features": present,
                "missing_features": missing,
                "present_count": present_count,
                "required_count": required_count,
                "missing_count": missing_count,
                "coverage": coverage,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeFeatureCoverage",
                "description": "Computes present/missing features and coverage ratio given required and available feature lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "required_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "available_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["required_features", "available_features"],
                },
            },
        }


class BuildFeatureValidationPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, model_name: str = None, created_ts: str = None) -> str:
        if not city_slug or not model_name or not created_ts:
            payload = {"error": "Missing city_slug, model_name or created_ts"}
            out = json.dumps(payload)
            return out
        ymd = created_ts[:10].replace("-", "")
        path = f"/processed_data/feature_validation_{city_slug}_{model_name}_{ymd}.json"
        payload = {
                "city_slug": city_slug,
                "model_name": model_name,
                "ymd": ymd,
                "feature_validation_json_path": path,
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildFeatureValidationPath",
                "description": "Builds canonical feature validation JSON path from city_slug, model_name, and created_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "model_name": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "model_name", "created_ts"],
                },
            },
        }


class BuildFeatureValidationRunId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, model_name: str = None, created_ts: str = None) -> str:
        if not city_slug or not model_name or not created_ts:
            payload = {"error": "Missing city_slug, model_name or created_ts"}
            out = json.dumps(payload)
            return out
        ymd = created_ts[:10].replace("-", "")
        run_id = f"fv_{city_slug}_{model_name}_{ymd}_v1"
        payload = {"run_id": run_id, "ymd": ymd}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildFeatureValidationRunId",
                "description": "Builds canonical run_id for feature validation from city_slug, model_name, and created_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "model_name": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "model_name", "created_ts"],
                },
            },
        }


class BuildInputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], features_csv_path: str = None, model_path: str = None) -> str:
        if not features_csv_path or not model_path:
            payload = {"error": "Missing features_csv_path or model_path"}
            out = json.dumps(payload)
            return out
        payload = {"input_paths": [features_csv_path, model_path]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "buildInputPaths",
                "description": "Builds input_paths array for feature validation from features_csv_path and model_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "features_csv_path": {"type": "string"},
                        "model_path": {"type": "string"},
                    },
                    "required": ["features_csv_path", "model_path"],
                },
            },
        }


class BuildOutputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_validation_json_path: str = None) -> str:
        if not feature_validation_json_path:
            payload = {"error": "Missing feature_validation_json_path"}
            out = json.dumps(payload)
            return out
        payload = {"output_paths": [feature_validation_json_path]}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "buildOutputPaths",
                "description": "Wraps the feature_validation_json_path into the output_paths array.",
                "parameters": {
                    "type": "object",
                    "properties": {"feature_validation_json_path": {"type": "string"}},
                    "required": ["feature_validation_json_path"],
                },
            },
        }


class GetFvpTimestamps(Tool):
    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {
            "started_ts": "2024-03-17T10:20:00Z",
            "finished_ts_nullable": "2024-03-17T10:25:00Z",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getFvpTimestamps",
                "description": "Returns canonical started_ts and finished_ts_nullable for FVP.",
                "parameters": {"type": "object", "properties": {}},
            },
        }


class BuildFeatureValidationMessages(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_name: str = None,
        feature_validation_json_path: str = None,
        present_count: int = None,
        required_count: int = None,
        missing_features: list = None
    ) -> str:
        if missing_features is None:
            missing_features = []
        if (
            model_name is None
            or feature_validation_json_path is None
            or present_count is None
            or required_count is None
        ):
            payload = {"error": "Missing required fields"}
            out = json.dumps(payload)
            return out
        miss = sorted([str(x) for x in missing_features])
        miss_str = "none" if len(miss) == 0 else ", ".join(miss)
        messages = [
            f"Feature validation for {model_name}: {present_count}/{required_count} required features present.",
            f"Missing features: {miss_str}.",
            f"Validated file: {feature_validation_json_path}.",
        ]
        payload = {"messages": messages}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "buildFeatureValidationMessages",
                "description": "Builds deterministic FVP messages with sorted missing features and the validation artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "feature_validation_json_path": {"type": "string"},
                        "present_count": {"type": "integer"},
                        "required_count": {"type": "integer"},
                        "missing_features": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "model_name",
                        "feature_validation_json_path",
                        "present_count",
                        "required_count",
                    ],
                },
            },
        }


class BuildMergedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city_slug or not start_ts or not end_ts:
            payload = {"error": "Missing city_slug, start_ts, end_ts"}
            out = json.dumps(payload)
            return out
        y0 = start_ts[:10].replace("-", "")
        y1 = end_ts[:10].replace("-", "")
        payload = {
                "merged_timeseries_path": f"/processed_data/merged_timeseries_{city_slug}_{y0}_{y1}.csv"
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildMergedTimeseriesPath",
                "description": "Builds canonical merged timeseries path from city_slug and analysis window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "start_ts", "end_ts"],
                },
            },
        }


class BuildMetricsSummaryPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, end_ts: str = None) -> str:
        if not model_name or not end_ts:
            payload = {"error": "Missing model_name or end_ts"}
            out = json.dumps(payload)
            return out
        y1 = end_ts[:10].replace("-", "")
        payload = {
                "metrics_summary_path": f"/processed_data/metrics_summary_{model_name}_{y1}.csv"
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildMetricsSummaryPath",
                "description": "Builds canonical metrics summary CSV path from model_name and end_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["model_name", "end_ts"],
                },
            },
        }


class GetMtpTimestamps(Tool):
    def invoke(data: dict[str, Any], anything: Any = None) -> str:
        payload = {
            "started_ts": "2024-03-17T09:30:00Z",
            "finished_ts_nullable": "2024-03-17T11:15:00Z",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetMtpTimestamps",
                "description": "Returns canonical started_ts and finished_ts for MTP.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class BuildMtpMessages(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], train_samples: int = None, test_samples: int = None, model_path: str = None) -> str:
        if train_samples is None or test_samples is None or not model_path:
            payload = {"error": "Missing train_samples, test_samples, or model_path"}
            out = json.dumps(payload)
            return out
        messages = [
            f"Training samples: {int(train_samples)}",
            f"Test samples: {int(test_samples)}",
            f"Model saved to: {model_path}",
        ]
        payload = {"messages": messages}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpMessages",
                "description": "Builds deterministic MTP messages list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_samples": {"type": "integer"},
                        "test_samples": {"type": "integer"},
                        "model_path": {"type": "string"},
                    },
                    "required": ["train_samples", "test_samples", "model_path"],
                },
            },
        }


class BuildMtpInputPaths(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], merged_timeseries_path: str = None, features_csv_path: str = None, split_summary_json_path: str = None) -> str:
        if (
            not merged_timeseries_path
            or not features_csv_path
            or not split_summary_json_path
        ):
            payload = {
                    "error": "Missing merged_timeseries_path, features_csv_path, or split_summary_json_path"
                }
            out = json.dumps(
                payload)
            return out
        payload = {
                "input_paths": [
                    merged_timeseries_path,
                    features_csv_path,
                    split_summary_json_path,
                ]
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpInputPaths",
                "description": "Builds input_paths array for MTP.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "merged_timeseries_path": {"type": "string"},
                        "features_csv_path": {"type": "string"},
                        "split_summary_json_path": {"type": "string"},
                    },
                    "required": [
                        "merged_timeseries_path",
                        "features_csv_path",
                        "split_summary_json_path",
                    ],
                },
            },
        }


class BuildMtpRunId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, model_name: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city_slug or not model_name or not start_ts or not end_ts:
            payload = {"error": "Missing city_slug, model_name, start_ts, or end_ts"}
            out = json.dumps(payload)
            return out
        y0 = start_ts[:10].replace("-", "")
        y1 = end_ts[:10].replace("-", "")
        payload = {"run_id": f"mt_{city_slug}_{model_name}_{y0}_{y1}_v1"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpRunId",
                "description": "Builds canonical MTP run_id from city_slug, model_name, and analysis window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "model_name": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "model_name", "start_ts", "end_ts"],
                },
            },
        }


TOOLS = [
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
    GetModelInfo(),
]
