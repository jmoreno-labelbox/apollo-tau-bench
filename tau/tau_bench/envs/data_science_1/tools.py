import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _require(kwargs: dict[str, Any], required: list[str]) -> str | None:
    pass
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        payload = {"error": f"Missing required arguments: {', '.join(missing)}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    return None


def _append(table: list[dict[str, Any]], row: dict[str, Any]) -> dict[str, Any]:
    pass
    table.append(row)
    return row


class SetProjectConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        forecast_horizon_days: int = None,
        max_station_distance_km_nullable: float = None,
        primary_station_id_nullable: str = None,
        target_city: str = None,
        timezone_default: str = None,
        top_n_results: int = None,
        updated_ts: str = None
    ) -> str:
        err = _require({"target_city": target_city, "timezone_default": timezone_default}, ["target_city", "timezone_default"])
        if err:
            return err
        cfg = {
            "target_city": target_city,
            "forecast_horizon_days": forecast_horizon_days,
            "top_n_results": top_n_results,
            "timezone_default": timezone_default,
            "max_station_distance_km_nullable": max_station_distance_km_nullable,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
            "primary_station_id_nullable": primary_station_id_nullable,
        }
        data["project_config"] = [cfg]
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetProjectConfig",
                "description": "Create/replace the single project config row deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {"type": "string"},
                        "forecast_horizon_days": {"type": "integer"},
                        "top_n_results": {"type": "integer"},
                        "timezone_default": {"type": "string"},
                        "max_station_distance_km_nullable": {"type": "number"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                        "primary_station_id_nullable": {"type": "string"},
                    },
                    "required": ["target_city", "timezone_default"],
                },
            },
        }


class CreateDirectory(Tool):
    def invoke(
        data: dict[str, Any],
        created_ts: Any = None,
        path: str = None,
        updated_ts: Any = None
    ) -> str:
        err = _require({"path": path}, ["path"])
        if err:
            return err
        row = {
            "path": path,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        tbl = data.setdefault("file_directory", [])
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDirectory",
                "description": "Registers a directory path in file_directory deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["path"],
                },
            },
        }


class WriteFileText(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        content: str = None,
        created_ts: str = None,
        mime_type: str = None,
        path: str = None,
        updated_ts: str = None
    ) -> str:
        err = _require({"path": path, "content": content}, ["path", "content"])
        if err:
            return err
        tbl = data.setdefault("file_store", [])
        row = {
            "path": path,
            "file_contents_text": content,
            "file_mime_types": mime_type,
            "char_counts": len(content),
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        existing = next((r for r in tbl if r.get("path") == row["path"]), None)
        if existing:
            existing.update(row)
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteFileText",
                "description": "Stores or updates a text file into file_store deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["path", "content"],
                },
            },
        }


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        command: str = None,
        exit_code: int = 0,
        printed_message: str = "",
        printed_ts: str = "1970-01-01T00:00:00Z",
        stderr: str = "",
        stdout: str = ""
    ) -> str:
        err = _require({"command": command}, ["command"])
        if err:
            return err
        tbl = data.setdefault("terminal_log", [])
        row = {
            "command": command,
            "exit_code": exit_code,
            "stdout": stdout,
            "stderr": stderr,
            "printed_message": printed_message,
            "printed_ts": printed_ts,
        }
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLog",
                "description": "Appends a terminal log row (deterministic fields only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string"},
                        "exit_code": {"type": "integer"},
                        "stdout": {"type": "string"},
                        "stderr": {"type": "string"},
                        "printed_message": {"type": "string"},
                        "printed_ts": {"type": "string"},
                    },
                    "required": ["command"],
                },
            },
        }


class StoreGeocodingResult(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        canonical_name: str = None,
        latitude: float = None,
        longitude: float = None,
        query_city: str = None,
        query_ts: str = None,
        raw_json_path_nullable: str = None
    ) -> str:
        req = ["query_city", "latitude", "longitude"]
        err = _require({"query_city": query_city, "latitude": latitude, "longitude": longitude}, req)
        if err:
            return err
        row = {
            "query_city": query_city,
            "latitude": latitude,
            "longitude": longitude,
            "canonical_name": canonical_name,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "query_ts": query_ts,
        }
        payload = _append(data.setdefault("geocoding_results", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreGeocodingResult",
                "description": "Adds a geocoding row for the target city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {"type": "string"},
                        "latitude": {"type": "number"},
                        "longitude": {"type": "number"},
                        "canonical_name": {"type": "string"},
                        "raw_json_path_nullable": {"type": "string"},
                        "query_ts": {"type": "string"},
                    },
                    "required": ["query_city", "latitude", "longitude"],
                },
            },
        }


class StoreWeatherForecast(Tool):
    def invoke(
        data: dict[str, Any],
        city: str = None,
        end_ts: str = None,
        fetched_ts: str = None,
        horizon_days: int = None,
        latitude: float = None,
        longitude: float = None,
        precipitation_mm_hr_nullable: float = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        temperature_2m_c_nullable: float = None,
        timestamps: list = None,
        timezone: str = None,
        variables: Any = None,
        wind_speed_10m_ms_nullable: float = None
    ) -> str:
        req = ["city", "latitude", "longitude"]
        err = _require({"city": city, "latitude": latitude, "longitude": longitude}, req)
        if err:
            return err
        row = {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "variables": variables,
            "timezone": timezone,
            "horizon_days": horizon_days,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "precipitation_mm_hr_nullable": precipitation_mm_hr_nullable,
            "temperature_2m_c_nullable": temperature_2m_c_nullable,
            "wind_speed_10m_ms_nullable": wind_speed_10m_ms_nullable,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("weather_forecasts", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "storeWeatherForecast",
                "description": "Adds an hourly weather forecast record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "latitude": {"type": "number"},
                        "longitude": {"type": "number"},
                        "variables": {"type": "array", "items": {"type": "string"}},
                        "timezone": {"type": "string"},
                        "horizon_days": {"type": "integer"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "precipitation_mm_hr_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "temperature_2m_c_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "wind_speed_10m_ms_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["city", "latitude", "longitude"],
                },
            },
        }


class StoreNoaaStationSearch(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_latitude: float = None,
        query_longitude: float = None,
        query_ts: str = None,
        radius_km: float = None,
        raw_json_path_nullable: str = None,
        station_distances_km: list[float] = None,
        station_ids: list[str] = None,
        station_latitudes: list[float] = None,
        station_longitudes: list[float] = None,
        station_names: list[str] = None,
        station_types_nullable: list[str] = None
    ) -> str:
        req = ["query_latitude", "query_longitude", "station_ids"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "query_latitude": query_latitude,
            "query_longitude": query_longitude,
            "radius_km": radius_km,
            "station_ids": station_ids,
            "station_names": station_names,
            "station_distances_km": station_distances_km,
            "station_latitudes": station_latitudes,
            "station_longitudes": station_longitudes,
            "station_types_nullable": station_types_nullable,
            "raw_json_path_nullable": raw_json_path_nullable,
            "query_ts": query_ts,
        }
        payload = _append(data.setdefault("noaa_station_searches", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreNoaaStationSearch",
                "description": "Stores results of a NOAA tide-station proximity search.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"},
                        "station_ids": {"type": "array", "items": {"type": "string"}},
                        "station_names": {"type": "array", "items": {"type": "string"}},
                        "station_distances_km": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_latitudes": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_longitudes": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_types_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "query_ts": {"type": "string"},
                    },
                    "required": ["query_latitude", "query_longitude", "station_ids"],
                },
            },
        }


class SetPrimaryStation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None) -> str:
        err = _require({"station_id": station_id}, ["station_id"])
        if err:
            return err
        cfg = (
            (data.get("project_config") or [{}])[0]
            if data.get("project_config")
            else {}
        )
        cfg["primary_station_id_nullable"] = station_id
        data["project_config"] = [cfg] if data.get("project_config") else [cfg]
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetPrimaryStation",
                "description": "Sets the chosen primary station_id on project_config.",
                "parameters": {
                    "type": "object",
                    "properties": {"station_id": {"type": "string"}},
                    "required": ["station_id"],
                },
            },
        }


class StoreWaterLevels(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        datum_nullable: str = None,
        end_ts: str = None,
        fetched_ts: str = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        station_id: str = None,
        station_name_nullable: str = None,
        timestamps: list = None,
        units: str = None,
        water_level_m: float = None
    ) -> str:
        req = ["station_id", "timestamps", "water_level_m", "units"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "station_id": station_id,
            "station_name_nullable": station_name_nullable,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "water_level_m": water_level_m,
            "units": units,
            "datum_nullable": datum_nullable,
            "provider": "noaa-tides-currents",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("water_levels", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreWaterLevels",
                "description": "Stores observed water levels for a station and window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "station_name_nullable": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "water_level_m": {"type": "array", "items": {"type": "number"}},
                        "units": {"type": "string"},
                        "datum_nullable": {"type": "string"},
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["station_id", "timestamps", "water_level_m", "units"],
                },
            },
        }


class StoreTidePredictions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        end_ts: str = None,
        fetched_ts: str = None,
        method_nullable: str = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        station_id: str = None,
        station_name_nullable: str = None,
        tide_pred_m: float = None,
        timestamps: list = None,
        units: str = None
    ) -> str:
        req = ["station_id", "timestamps", "tide_pred_m", "units"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "station_id": station_id,
            "station_name_nullable": station_name_nullable,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "tide_pred_m": tide_pred_m,
            "units": units,
            "method_nullable": method_nullable,
            "provider": "noaa-tides-currents",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("tide_predictions", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreTidePredictions",
                "description": "Stores tide predictions for a station and window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "station_name_nullable": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "tide_pred_m": {"type": "array", "items": {"type": "number"}},
                        "units": {"type": "string"},
                        "method_nullable": {"type": "string"},
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["station_id", "timestamps", "tide_pred_m", "units"],
                },
            },
        }


class StoreCoastalMeteorology(Tool):
    def invoke(
        data: dict[str, Any],
        end_ts: str = None,
        fetched_ts: str = None,
        pressure_hpa_nullable: float = None,
        raw_json_path_nullable: str = None,
        start_ts: str = None,
        station_id: str = None,
        temperature_c_nullable: float = None,
        timestamps: list = None,
        wind_speed_ms_nullable: float = None
    ) -> str:
        req = ["station_id", "timestamps"]
        err = _require({"station_id": station_id, "timestamps": timestamps}, req)
        if err:
            return err
        row = {
            "station_id": station_id,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "wind_speed_ms_nullable": wind_speed_ms_nullable,
            "pressure_hpa_nullable": pressure_hpa_nullable,
            "temperature_c_nullable": temperature_c_nullable,
            "provider": "noaa-tides-currents",
            "raw_json_path_nullable": raw_json_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("coastal_meteorology", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "storeCoastalMeteorology",
                "description": "Stores coastal meteorology (wind/pressure/temperature) by station.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                        "timestamps": {"type": "array", "items": {"type": "string"}},
                        "wind_speed_ms_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "pressure_hpa_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "temperature_c_nullable": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["station_id", "timestamps"],
                },
            },
        }


class ComputeAndStoreMergedTimeseries(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        columns: list[str] = None,
        created_ts: str = None,
        csv_path: str = None,
        file_hash_sha256: str = None,
        max_timestamp: str = None,
        min_timestamp: str = None,
        row_count: int = None
    ) -> str:
        err = _require({"csv_path": csv_path}, ["csv_path"])
        if err:
            return err
        allowed = [
            "csv_path",
            "columns",
            "row_count",
            "min_timestamp",
            "max_timestamp",
            "file_hash_sha256",
            "created_ts",
        ]
        row = {k: v for k, v in locals().items() if k in allowed and v is not None}
        payload = _append(data.setdefault("processed_timeseries", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeAndStoreMergedTimeseries",
                "description": "Registers a merged timeseries CSV artifact and its metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                        "row_count": {"type": "integer"},
                        "min_timestamp": {"type": "string"},
                        "max_timestamp": {"type": "string"},
                        "file_hash_sha256": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["csv_path"],
                },
            },
        }


class RegisterQcFigure(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        description: str = None,
        figure_path: str = None
    ) -> str:
        err = _require({"figure_path": figure_path}, ["figure_path"])
        if err:
            return err
        row = {
            "figure_path": figure_path,
            "description": description,
            "created_ts": created_ts,
        }
        payload = _append(data.setdefault("qc_figures", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterQcFigure",
                "description": "Registers a QC figure path and description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_path": {"type": "string"},
                        "description": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["figure_path"],
                },
            },
        }


class StoreFeatures(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        csv_path: str = None,
        definitions_nullable: Any = None,
        feature_names: list[str] = None,
        generated_ts: Any = None
    ) -> str:
        err = _require({"csv_path": csv_path, "feature_names": feature_names}, ["csv_path", "feature_names"])
        if err:
            return err
        row = {
            "csv_path": csv_path,
            "feature_names": feature_names,
            "definitions_nullable": definitions_nullable,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("features", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreFeatures",
                "description": "Stores feature list metadata for a generated CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"},
                        "feature_names": {"type": "array", "items": {"type": "string"}},
                        "definitions_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["csv_path", "feature_names"],
                },
            },
        }


class WriteModelConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        classification_threshold_m_nullable: float = None,
        precip_24h_threshold_mm_nullable: float = None,
        test_split_fraction_nullable: float = None,
        random_seed_nullable: int = None,
        saved_json_path: str = None,
        created_ts: str = None
    ) -> str:
        err = _require({"saved_json_path": saved_json_path}, ["saved_json_path"])
        if err:
            return err
        row = {
            "classification_threshold_m_nullable": classification_threshold_m_nullable,
            "precip_24h_threshold_mm_nullable": precip_24h_threshold_mm_nullable,
            "test_split_fraction_nullable": test_split_fraction_nullable,
            "random_seed_nullable": random_seed_nullable,
            "saved_json_path": saved_json_path,
            "created_ts": created_ts,
        }
        payload = _append(data.setdefault("model_config", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteModelConfig",
                "description": "Stores modeling configuration (thresholds/split/seed).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "classification_threshold_m_nullable": {"type": "number"},
                        "precip_24h_threshold_mm_nullable": {"type": "number"},
                        "test_split_fraction_nullable": {"type": "number"},
                        "random_seed_nullable": {"type": "integer"},
                        "saved_json_path": {"type": "string"},
                        "created_ts": {"type": "string"},
                    },
                    "required": ["saved_json_path"],
                },
            },
        }


class CreateTimeBasedSplit(Tool):
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
        err = _require({"split_summary_json_path": split_summary_json_path}, ["split_summary_json_path"])
        if err:
            return err
        row = {
            "method": method,
            "test_fraction": test_fraction,
            "train_index_count": train_index_count,
            "test_index_count": test_index_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        payload = _append(data.setdefault("dataset_split", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTimeBasedSplit",
                "description": "Registers a time-based dataset split summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "method": {"type": "string"},
                        "test_fraction": {"type": "number"},
                        "train_index_count": {"type": "integer"},
                        "test_index_count": {"type": "integer"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": ["split_summary_json_path"],
                },
            },
        }


class RegisterModel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        feature_names: list[str] = None,
        model_name: str = None,
        model_path: str = None,
        model_type: str = None,
        target_name: str = None,
        train_metrics_json_path_nullable: str = None,
        training_ts: str = None
    ) -> str:
        err = _require({"model_name": model_name, "model_path": model_path}, ["model_name", "model_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "model_type": model_type,
            "training_ts": training_ts,
            "model_path": model_path,
            "feature_names": feature_names,
            "target_name": target_name,
            "train_metrics_json_path_nullable": train_metrics_json_path_nullable,
        }
        payload = _append(data.setdefault("models", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterModel",
                "description": "Registers a trained model artifact with metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "model_type": {"type": "string"},
                        "training_ts": {"type": "string"},
                        "model_path": {"type": "string"},
                        "feature_names": {"type": "array", "items": {"type": "string"}},
                        "target_name": {"type": "string"},
                        "train_metrics_json_path_nullable": {"type": "string"},
                    },
                    "required": ["model_name", "model_path"],
                },
            },
        }


class StorePredictions(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        columns: list = None,
        generated_ts: str = None,
        model_name: str = None,
        predictions_csv_path: str = None,
        row_count: int = None
    ) -> str:
        err = _require({"model_name": model_name, "predictions_csv_path": predictions_csv_path}, ["model_name", "predictions_csv_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
            "row_count": row_count,
            "columns": columns,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("predictions", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StorePredictions",
                "description": "Stores a predictions CSV artifact for a model.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "predictions_csv_path": {"type": "string"},
                        "row_count": {"type": "integer"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["model_name", "predictions_csv_path"],
                },
            },
        }


class StoreMetrics(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        accuracy_nullable: float = None,
        auc_nullable: float = None,
        generated_ts: str = None,
        metrics_csv_path: str = None,
        model_name: str = None,
        rmse_nullable: float = None
    ) -> str:
        err = _require({"model_name": model_name, "metrics_csv_path": metrics_csv_path}, ["model_name", "metrics_csv_path"])
        if err:
            return err
        row = {
            "model_name": model_name,
            "metrics_csv_path": metrics_csv_path,
            "auc_nullable": auc_nullable,
            "accuracy_nullable": accuracy_nullable,
            "rmse_nullable": rmse_nullable,
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
                "name": "StoreMetrics",
                "description": "Stores metrics for a model (AUC/accuracy/RMSE).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metrics_csv_path": {"type": "string"},
                        "auc_nullable": {"type": "number"},
                        "accuracy_nullable": {"type": "number"},
                        "rmse_nullable": {"type": "number"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": ["model_name", "metrics_csv_path"],
                },
            },
        }


class RecordStakeholderOutputs(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        generated_ts: str = None,
        metrics_summary_csv_path: str = None,
        predictions_final_csv_path: str = None
    ) -> str:
        err = _require(
            {"predictions_final_csv_path": predictions_final_csv_path, "metrics_summary_csv_path": metrics_summary_csv_path}, 
            ["predictions_final_csv_path", "metrics_summary_csv_path"]
        )
        if err:
            return err
        row = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts,
        }
        payload = _append(data.setdefault("stakeholder_outputs", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordStakeholderOutputs",
                "description": "Registers links to final predictions/metrics artifacts for stakeholders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_final_csv_path": {"type": "string"},
                        "metrics_summary_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"},
                    },
                    "required": [
                        "predictions_final_csv_path",
                        "metrics_summary_csv_path",
                    ],
                },
            },
        }


class ZoteroSearchItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        limit: int = None,
        query: str = None,
        result_item_ids: list = None,
        saved_path_nullable: str = None,
        search_ts: str = None,
        year_from: int = None,
        year_to: int = None
    ) -> str:
        req = ["query", "result_item_ids", "search_ts"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "query": query,
            "year_from": year_from,
            "year_to": year_to,
            "limit": limit,
            "result_item_ids": result_item_ids,
            "saved_path_nullable": saved_path_nullable,
            "search_ts": search_ts,
        }
        payload = _append(data.setdefault("zotero_searches", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroSearchItems",
                "description": "Stores results of a Zotero query (top-N IDs).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "year_from": {"type": "integer"},
                        "year_to": {"type": "integer"},
                        "limit": {"type": "integer"},
                        "result_item_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "saved_path_nullable": {"type": "string"},
                        "search_ts": {"type": "string"},
                    },
                    "required": ["query", "result_item_ids", "search_ts"],
                },
            },
        }


class ZoteroItemMetadata(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        abstracts_nullable: Any = None,
        authors: Any = None,
        fetched_ts: Any = None,
        item_ids: Any = None,
        saved_path_nullable: Any = None,
        titles: Any = None,
        urls_nullable: Any = None,
        venues_nullable: Any = None,
        years: Any = None
    ) -> str:
        req = ["item_ids", "titles", "fetched_ts"]
        kwargs = {
            "item_ids": item_ids,
            "titles": titles,
            "fetched_ts": fetched_ts
        }
        err = _require(kwargs, req)
        if err:
            return err
        row = {
            "item_ids": item_ids,
            "titles": titles,
            "authors": authors,
            "years": years,
            "venues_nullable": venues_nullable,
            "urls_nullable": urls_nullable,
            "abstracts_nullable": abstracts_nullable,
            "saved_path_nullable": saved_path_nullable,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("zotero_metadata", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroItemMetadata",
                "description": "Stores bibliographic metadata for Zotero items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "titles": {"type": "array", "items": {"type": "string"}},
                        "authors": {
                            "type": "array",
                            "items": {"type": "array", "items": {"type": "string"}},
                        },
                        "years": {"type": "array", "items": {"type": "integer"}},
                        "venues_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "urls_nullable": {"type": "array", "items": {"type": "string"}},
                        "abstracts_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "saved_path_nullable": {"type": "string"},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["item_ids", "titles", "fetched_ts"],
                },
            },
        }


class ZoteroItemFulltext(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        fetched_ts: Any = None,
        file_paths: Any = None,
        item_ids: Any = None
    ) -> str:
        req = ["item_ids", "file_paths"]
        err = _require({"item_ids": item_ids, "file_paths": file_paths}, req)
        if err:
            return err
        row = {
            "item_ids": item_ids,
            "file_paths": file_paths,
            "fetched_ts": fetched_ts,
        }
        payload = _append(data.setdefault("zotero_fulltexts", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ZoteroItemFulltext",
                "description": "Stores file paths for fetched Zotero fulltexts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "item_ids": {"type": "array", "items": {"type": "string"}},
                        "file_paths": {"type": "array", "items": {"type": "string"}},
                        "fetched_ts": {"type": "string"},
                    },
                    "required": ["item_ids", "file_paths"],
                },
            },
        }


class NotionCreatePage(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        created_ts: str = None,
        page_id: str = None,
        properties_json_nullable: str = None,
        sections_present: list = None,
        title: str = None,
        updated_ts: str = None,
        url_nullable: str = None
    ) -> str:
        if sections_present is None:
            sections_present = []
        req = ["page_id", "title"]
        err = _require({"page_id": page_id, "title": title}, req)
        if err:
            return err
        row = {
            "page_id": page_id,
            "title": title,
            "url_nullable": url_nullable,
            "properties_json_nullable": properties_json_nullable,
            "sections_present": sections_present,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        payload = _append(data.setdefault("notion_pages", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionCreatePage",
                "description": "Creates a Notion page record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "title": {"type": "string"},
                        "url_nullable": {"type": "string"},
                        "properties_json_nullable": {"type": "string"},
                        "sections_present": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id", "title"],
                },
            },
        }


class NotionAppendSections(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], page_id: str, sections: list = None, updated_ts: str = None) -> str:
        if sections is None:
            sections = []
        req = ["page_id"]
        err = _require({"page_id": page_id}, req)
        if err:
            return err
        page = next(
            (
                p
                for p in data.setdefault("notion_pages", [])
                if p.get("page_id") == page_id
            ),
            None,
        )
        if not page:
            payload = {"error": f"page_id '{page_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        existing = set(page.get("sections_present", []))
        page["sections_present"] = list(existing.union(sections))
        page["updated_ts"] = updated_ts if updated_ts is not None else page.get("updated_ts")
        payload = page
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionAppendSections",
                "description": "Appends sections to a Notion page's sections_present.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "sections": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id"],
                },
            },
        }


class NotionUpdatePageProperties(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        page_id: str = None,
        properties_json: str = None,
        updated_ts: str = None
    ) -> str:
        req = ["page_id", "properties_json"]
        err = _require({"page_id": page_id, "properties_json": properties_json}, req)
        if err:
            return err
        page = next(
            (
                p
                for p in data.setdefault("notion_pages", [])
                if p.get("page_id") == page_id
            ),
            None,
        )
        if not page:
            payload = {"error": f"page_id '{page_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        page["properties_json_nullable"] = properties_json
        page["updated_ts"] = updated_ts if updated_ts is not None else page.get("updated_ts")
        payload = page
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotionUpdatePageProperties",
                "description": "Updates page properties JSON and updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "page_id": {"type": "string"},
                        "properties_json": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["page_id", "properties_json"],
                },
            },
        }


class GmailDraftEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        attachments_paths: list[str] = [],
        body_preview_nullable: str = None,
        created_ts: str = None,
        draft_id: str = None,
        recipients: list[str] = None,
        subject: str = None
    ) -> str:
        req = ["draft_id", "subject", "recipients"]
        err = _require({"draft_id": draft_id, "subject": subject, "recipients": recipients}, req)
        if err:
            return err
        row = {
            "draft_id_nullable": draft_id,
            "message_id_nullable": None,
            "subject": subject,
            "recipients": recipients,
            "body_preview_nullable": body_preview_nullable,
            "attachments_paths": attachments_paths,
            "status": "drafted",
            "created_ts": created_ts,
            "sent_ts_nullable": None,
        }
        payload = _append(data.setdefault("gmail_messages", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GmailDraftEmail",
                "description": "Creates a drafted Gmail message entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "recipients": {"type": "array", "items": {"type": "string"}},
                        "body_preview_nullable": {"type": "string"},
                        "attachments_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "string"},
                    },
                    "required": ["draft_id", "subject", "recipients"],
                },
            },
        }


class GmailSendEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        draft_id: str = None,
        message_id: str = None,
        sent_ts: str = "1970-01-01T00:00:00Z"
    ) -> str:
        req = ["draft_id"]
        err = _require({"draft_id": draft_id}, req)
        if err:
            return err
        msg = next(
            (
                m
                for m in data.setdefault("gmail_messages", [])
                if m.get("draft_id_nullable") == draft_id
            ),
            None,
        )
        if not msg:
            payload = {"error": f"draft_id '{draft_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        msg["message_id_nullable"] = message_id if message_id is not None else msg.get("message_id_nullable")
        msg["status"] = "sent"
        msg["sent_ts_nullable"] = sent_ts if sent_ts is not None else msg.get("sent_ts_nullable", "1970-01-01T00:00:00Z")
        payload = msg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GmailSendEmail",
                "description": "Marks a drafted Gmail message as sent.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "draft_id": {"type": "string"},
                        "message_id": {"type": "string"},
                        "sent_ts": {"type": "string"},
                    },
                    "required": ["draft_id"],
                },
            },
        }


class LogMcpToolCall(Tool):
    def invoke(
        data: dict[str, Any],
        called_ts: str = None,
        params_json: str = None,
        response_meta_nullable: str = None,
        server_names: str = None,
        tool_names: str = None
    ) -> str:
        req = ["server_names"]
        err = _require({"server_names": server_names}, req)
        if err:
            return err
        row = {
            "server_names": server_names,
            "tool_names": tool_names,
            "params_json": params_json,
            "response_meta_nullable": response_meta_nullable,
            "called_ts": called_ts,
        }
        payload = _append(data.setdefault("mcp_tool_calls", []), row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logMcpToolCall",
                "description": "Logs a synthetic MCP tool call for traceability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_names": {"type": "array", "items": {"type": "string"}},
                        "tool_names": {"type": "array", "items": {"type": "string"}},
                        "params_json": {"type": "string"},
                        "response_meta_nullable": {"type": "string"},
                        "called_ts": {"type": "string"},
                    },
                    "required": ["server_names"],
                },
            },
        }


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
