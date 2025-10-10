import json
from typing import Any, Dict, List, Optional

from domains.dto import Tool


class GetProjectConfigByCity(Tool):
    """
    Retrieves a project_config entry by target_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], target_city: str) -> str:
        rows = data.get("project_config", [])
        for row in rows:
            if row.get("target_city") == target_city:
                return json.dumps(row)
        return json.dumps({"error": "project_config not found", "target_city": target_city})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_config_by_city",
                "description": "Retrieves a project_config entry by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {"type": "string", "description": "City name key in project_config."}
                    },
                    "required": ["target_city"]
                }
            }
        }


class GetFileTextByPath(Tool):
    """
    Returns file text and metadata from file_store by path.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], path: str) -> str:
        rows = data.get("file_store", [])
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                out = {
                    "path": path,
                    "file_contents_text": row.get("file_contents_text", [None]*len(paths))[i] if i < len(row.get("file_contents_text", [])) else None,
                    "file_mime_types": row.get("file_mime_types", [None]*len(paths))[i] if i < len(row.get("file_mime_types", [])) else None,
                    "char_counts": row.get("char_counts", [None]*len(paths))[i] if i < len(row.get("char_counts", [])) else None
                }
                return json.dumps(out)
        return json.dumps({"error": "file not found", "path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_file_text_by_path",
                "description": "Returns file text and metadata from file_store by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string", "description": "Exact file path stored in file_store.paths."}
                    },
                    "required": ["path"]
                }
            }
        }


class GetTerminalLogCommandResult(Tool):
    """
    Retrieves a terminal_log entry by exact command string.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], command: str) -> str:
        rows = data.get("terminal_log", [])
        for row in rows:
            cmds = row.get("commands", [])
            if command in cmds:
                i = cmds.index(command)
                out = {
                    "command": command,
                    "exit_code": row.get("exit_codes", [None]*len(cmds))[i] if i < len(row.get("exit_codes", [])) else None,
                    "stdout": row.get("stdouts", [None]*len(cmds))[i] if i < len(row.get("stdouts", [])) else None,
                    "stderr": row.get("stderrs", [None]*len(cmds))[i] if i < len(row.get("stderrs", [])) else None,
                    "printed_message": row.get("printed_messages", [None]*len(cmds))[i] if i < len(row.get("printed_messages", [])) else None,
                    "printed_ts": row.get("printed_ts", [None]*len(cmds))[i] if i < len(row.get("printed_ts", [])) else None
                }
                return json.dumps(out)
        return json.dumps({"error": "command not found", "command": command})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_log_command_result",
                "description": "Retrieves a terminal_log entry by exact command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Exact command string to look up."}
                    },
                    "required": ["command"]
                }
            }
        }


class GetGeocodingResultByCity(Tool):
    """
    Retrieves geocoding_results by query_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], query_city: str) -> str:
        rows = data.get("geocoding_results", [])
        for row in rows:
            if row.get("query_city") == query_city:
                return json.dumps(row)
        return json.dumps({"error": "geocoding result not found", "query_city": query_city})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_geocoding_result_by_city",
                "description": "Retrieves a geocoding result by query_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {"type": "string", "description": "City name used in geocoding query."}
                    },
                    "required": ["query_city"]
                }
            }
        }


class GetWeatherForecastByCity(Tool):
    """
    Retrieves a weather_forecasts record by city and horizon_days.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], city: str, horizon_days: int) -> str:
        rows = data.get("weather_forecasts", [])
        for row in rows:
            if row.get("city") == city and row.get("horizon_days") == horizon_days:
                return json.dumps(row)
        return json.dumps({"error": "weather forecast not found", "city": city, "horizon_days": horizon_days})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_weather_forecast_by_city",
                "description": "Retrieves weather_forecasts by city and exact horizon_days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "horizon_days": {"type": "integer"}
                    },
                    "required": ["city", "horizon_days"]
                }
            }
        }


class GetStationsByLocation(Tool):
    """
    Returns a noaa_station_searches record by exact latitude, longitude, and radius_km.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], query_latitude: float, query_longitude: float, radius_km: float) -> str:
        rows = data.get("noaa_station_searches", [])
        for row in rows:
            if row.get("query_latitude") == query_latitude and row.get("query_longitude") == query_longitude and row.get("radius_km") == radius_km:
                return json.dumps(row)
        return json.dumps({"error": "station search not found", "query_latitude": query_latitude, "query_longitude": query_longitude, "radius_km": radius_km})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_stations_by_location",
                "description": "Returns a noaa_station_searches record by exact query coordinates and radius.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"}
                    },
                    "required": ["query_latitude", "query_longitude", "radius_km"]
                }
            }
        }


class GetWaterLevelsWindow(Tool):
    """
    Returns a subset of water_levels for a station within [window_start_ts, window_end_ts].
    """
    @staticmethod
    def invoke(data: Dict[str, Any], station_id: str, window_start_ts: str, window_end_ts: str) -> str:
        rows = data.get("water_levels", [])
        for row in rows:
            if row.get("station_id") == station_id and row.get("start_ts") <= window_start_ts and row.get("end_ts") >= window_end_ts:
                ts = row.get("timestamps", [])
                wl = row.get("water_level_m", [])
                out_ts = []
                out_wl = []
                for t, v in zip(ts, wl):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_wl.append(v)
                return json.dumps({
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "water_level_m": out_wl,
                    "units": row.get("units"),
                    "datum_nullable": row.get("datum_nullable")
                })
        return json.dumps({"error": "window not covered", "station_id": station_id, "window_start_ts": window_start_ts, "window_end_ts": window_end_ts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_water_levels_window",
                "description": "Returns subset of water_levels for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"}
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"]
                }
            }
        }


class GetTidePredictionsWindow(Tool):
    """
    Returns a subset of tide_predictions for a station within [window_start_ts, window_end_ts].
    """
    @staticmethod
    def invoke(data: Dict[str, Any], station_id: str, window_start_ts: str, window_end_ts: str) -> str:
        rows = data.get("tide_predictions", [])
        for row in rows:
            if row.get("station_id") == station_id and row.get("start_ts") <= window_start_ts and row.get("end_ts") >= window_end_ts:
                ts = row.get("timestamps", [])
                tp = row.get("tide_pred_m", [])
                out_ts = []
                out_tp = []
                for t, v in zip(ts, tp):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_tp.append(v)
                return json.dumps({
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "tide_pred_m": out_tp,
                    "units": row.get("units"),
                    "method_nullable": row.get("method_nullable")
                })
        return json.dumps({"error": "window not covered", "station_id": station_id, "window_start_ts": window_start_ts, "window_end_ts": window_end_ts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_tide_predictions_window",
                "description": "Returns subset of tide_predictions for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"}
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"]
                }
            }
        }


class GetProcessedTimeseriesSummary(Tool):
    """
    Retrieves processed_timeseries by csv_path.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], csv_path: str) -> str:
        rows = data.get("processed_timeseries", [])
        for row in rows:
            if row.get("csv_path") == csv_path:
                return json.dumps(row)
        return json.dumps({"error": "processed_timeseries not found", "csv_path": csv_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_processed_timeseries_summary",
                "description": "Retrieves processed_timeseries record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"}
                    },
                    "required": ["csv_path"]
                }
            }
        }


class GetFeaturesByCsvPath(Tool):
    """
    Retrieves features record by csv_path.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], csv_path: str) -> str:
        rows = data.get("features", [])
        for row in rows:
            if row.get("csv_path") == csv_path:
                return json.dumps(row)
        return json.dumps({"error": "features not found", "csv_path": csv_path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_features_by_csv_path",
                "description": "Retrieves features record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "csv_path": {"type": "string"}
                    },
                    "required": ["csv_path"]
                }
            }
        }


class GetModelByName(Tool):
    """
    Retrieves models record by model_name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], model_name: str) -> str:
        rows = data.get("models", [])
        for row in rows:
            if row.get("model_name") == model_name:
                return json.dumps(row)
        return json.dumps({"error": "model not found", "model_name": model_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_model_by_name",
                "description": "Retrieves models record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }


class GetPredictionsByModelName(Tool):
    """
    Retrieves predictions record by model_name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], model_name: str) -> str:
        rows = data.get("predictions", [])
        for row in rows:
            if row.get("model_name") == model_name:
                return json.dumps(row)
        return json.dumps({"error": "predictions not found", "model_name": model_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_predictions_by_model_name",
                "description": "Retrieves predictions record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }


class GetMetricsByModelName(Tool):
    """
    Retrieves metrics record by model_name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], model_name: str) -> str:
        rows = data.get("metrics", [])
        for row in rows:
            if row.get("model_name") == model_name:
                return json.dumps(row)
        return json.dumps({"error": "metrics not found", "model_name": model_name})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_metrics_by_model_name",
                "description": "Retrieves metrics record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"}
                    },
                    "required": ["model_name"]
                }
            }
        }


class GetMcpToolCallsByServer(Tool):
    """
    Returns flattened MCP tool call entries filtered by server name.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], server_name: str) -> str:
        rows = data.get("mcp_tool_calls", [])
        out: List[Dict[str, Any]] = []
        for row in rows:
            servers = row.get("server_names", [])
            tools = row.get("tool_names", [])
            params = row.get("params_json", [])
            metas = row.get("response_meta_nullable", [])
            times = row.get("called_ts", [])
            for i, s in enumerate(servers):
                if s == server_name:
                    out.append({
                        "server_name": s,
                        "tool_name": tools[i] if i < len(tools) else None,
                        "params_json": params[i] if i < len(params) else None,
                        "response_meta_nullable": metas[i] if i < len(metas) else None,
                        "called_ts": times[i] if i < len(times) else None
                    })
        return json.dumps({"items": out})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mcp_tool_calls_by_server",
                "description": "Returns flattened MCP tool call entries filtered by server name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "server_name": {"type": "string"}
                    },
                    "required": ["server_name"]
                }
            }
        }


class GetGmailMessageBySubject(Tool):
    """
    Retrieves a gmail_messages record by exact subject.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], subject: str) -> str:
        rows = data.get("gmail_messages", [])
        for row in rows:
            if row.get("subject") == subject:
                return json.dumps(row)
        return json.dumps({"error": "gmail message not found", "subject": subject})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_message_by_subject",
                "description": "Retrieves a gmail_messages record by exact subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"}
                    },
                    "required": ["subject"]
                }
            }
        }


class UpsertProjectConfig(Tool):
    """
    Inserts or updates a project_config record by target_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        if "target_city" not in record:
            return json.dumps({"error": "missing target_city"})
        rows = data.setdefault("project_config", [])
        for row in rows:
            if row.get("target_city") == record["target_city"]:
                row.update(record)
                return json.dumps({"status": "updated", "record": row})
        rows.append(record)
        return json.dumps({"status": "inserted", "record": record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_project_config",
                "description": "Inserts or updates a project_config record by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object", "description": "Full project_config record with target_city as key."}
                    },
                    "required": ["record"]
                }
            }
        }


class AddFileDirectoryRecord(Tool):
    """
    Appends a new file_directory record with parallel arrays.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], paths: List[str], file_sizes_bytes: List[int], file_hashes_sha256: List[Optional[str]], file_mime_types: List[str], created_ts: List[str], updated_ts: List[str]) -> str:
        n = len(paths)
        if not all(len(lst) == n for lst in [file_sizes_bytes, file_hashes_sha256, file_mime_types, created_ts, updated_ts]):
            return json.dumps({"error": "all arrays must have the same length"})
        row = {
            "paths": paths,
            "file_sizes_bytes": file_sizes_bytes,
            "file_hashes_sha256": file_hashes_sha256,
            "file_mime_types": file_mime_types,
            "created_ts": created_ts,
            "updated_ts": updated_ts
        }
        data.setdefault("file_directory", []).append(row)
        return json.dumps({"status": "inserted", "record": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_file_directory_record",
                "description": "Appends a new file_directory record with parallel arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "paths": {"type": "array", "items": {"type": "string"}},
                        "file_sizes_bytes": {"type": "array", "items": {"type": "integer"}},
                        "file_hashes_sha256": {"type": "array", "items": {"type": ["string", "null"]}},
                        "file_mime_types": {"type": "array", "items": {"type": "string"}},
                        "created_ts": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["paths", "file_sizes_bytes", "file_hashes_sha256", "file_mime_types", "created_ts", "updated_ts"]
                }
            }
        }


class UpsertFileStoreText(Tool):
    """
    Inserts or updates a file_store path entry with text, mime, and char count.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], path: str, file_contents_text: str, file_mime_type: str) -> str:
        rows = data.setdefault("file_store", [])
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                while len(row.get("file_contents_text", [])) <= i:
                    row.setdefault("file_contents_text", []).append("")
                while len(row.get("file_mime_types", [])) <= i:
                    row.setdefault("file_mime_types", []).append("")
                while len(row.get("char_counts", [])) <= i:
                    row.setdefault("char_counts", []).append(0)
                row["file_contents_text"][i] = file_contents_text
                row["file_mime_types"][i] = file_mime_type
                row["char_counts"][i] = len(file_contents_text)
                return json.dumps({"status": "updated", "path": path})
        rows.append({
            "paths": [path],
            "file_contents_text": [file_contents_text],
            "file_mime_types": [file_mime_type],
            "char_counts": [len(file_contents_text)]
        })
        return json.dumps({"status": "inserted", "path": path})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_file_store_text",
                "description": "Inserts or updates a file_store path entry with text and metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "file_contents_text": {"type": "string"},
                        "file_mime_type": {"type": "string"}
                    },
                    "required": ["path", "file_contents_text", "file_mime_type"]
                }
            }
        }


class AppendTerminalLogEntry(Tool):
    """
    Appends a single entry to terminal_log arrays in the first record or creates one.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], command: str, exit_code: int, stdout: str, stderr: str, printed_message: str, printed_ts: str) -> str:
        rows = data.setdefault("terminal_log", [])
        if not rows:
            rows.append({"commands": [], "exit_codes": [], "stdouts": [], "stderrs": [], "printed_messages": [], "printed_ts": []})
        row = rows[0]
        row.setdefault("commands", []).append(command)
        row.setdefault("exit_codes", []).append(exit_code)
        row.setdefault("stdouts", []).append(stdout)
        row.setdefault("stderrs", []).append(stderr)
        row.setdefault("printed_messages", []).append(printed_message)
        row.setdefault("printed_ts", []).append(printed_ts)
        return json.dumps({"status": "appended", "index": len(row["commands"]) - 1})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_terminal_log_entry",
                "description": "Appends a single entry to terminal_log arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string"},
                        "exit_code": {"type": "integer"},
                        "stdout": {"type": "string"},
                        "stderr": {"type": "string"},
                        "printed_message": {"type": "string"},
                        "printed_ts": {"type": "string"}
                    },
                    "required": ["command", "exit_code", "stdout", "stderr", "printed_message", "printed_ts"]
                }
            }
        }


class RecordGeocodingResult(Tool):
    """
    Appends a geocoding_results record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        if not {"query_city", "latitude", "longitude", "canonical_name", "provider", "query_ts"}.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("geocoding_results", []).append(record)
        return json.dumps({"status": "inserted", "record": record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_geocoding_result",
                "description": "Appends a geocoding_results record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class InsertWeatherForecast(Tool):
    """
    Appends a weather_forecasts record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"city", "latitude", "longitude", "variables", "timezone", "horizon_days", "start_ts", "end_ts", "timestamps", "provider", "fetched_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        ts = record.get("timestamps", [])
        for k in ["precipitation_mm_hr_nullable", "temperature_2m_c_nullable", "wind_speed_10m_ms_nullable"]:
            if k in record and isinstance(record[k], list) and len(record[k]) != len(ts):
                return json.dumps({"error": "array length mismatch", "field": k})
        data.setdefault("weather_forecasts", []).append(record)
        return json.dumps({"status": "inserted", "record": {"city": record.get("city"), "horizon_days": record.get("horizon_days")}})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insert_weather_forecast",
                "description": "Appends a weather_forecasts record with required fields and aligned arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class RegisterEtlRun(Tool):
    """
    Appends an etl_runs record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"run_id", "input_paths", "output_paths", "status", "started_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("etl_runs", []).append(record)
        return json.dumps({"status": "inserted", "run_id": record.get("run_id")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_etl_run",
                "description": "Appends an etl_runs record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class RegisterProcessedTimeseries(Tool):
    """
    Appends a processed_timeseries record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"csv_path", "columns", "row_count", "min_timestamp", "max_timestamp", "file_hash_sha256", "created_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("processed_timeseries", []).append(record)
        return json.dumps({"status": "inserted", "csv_path": record.get("csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_processed_timeseries",
                "description": "Appends a processed_timeseries record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class GenerateFeaturesFromProcessed(Tool):
    """
    Generates a features record from an existing processed_timeseries csv_path using deterministic rules.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], processed_csv_path: str, features_csv_path: str, generated_ts: str) -> str:
        rows = data.get("processed_timeseries", [])
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


class SaveModelConfig(Tool):
    """
    Appends a model_config record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"saved_json_path", "created_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("model_config", []).append(record)
        return json.dumps({"status": "inserted", "saved_json_path": record.get("saved_json_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_model_config",
                "description": "Appends a model_config record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class CreateTimeBasedDatasetSplit(Tool):
    """
    Creates a dataset_split record from processed_timeseries row_count with a deterministic floor split.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], processed_csv_path: str, test_fraction: float, split_summary_json_path: str, split_ts: str) -> str:
        pts = data.get("processed_timeseries", [])
        row = None
        for r in pts:
            if r.get("csv_path") == processed_csv_path:
                row = r
                break
        if not row:
            return json.dumps({"error": "processed_timeseries not found", "csv_path": processed_csv_path})
        total = int(row.get("row_count", 0))
        if test_fraction < 0 or test_fraction > 1:
            return json.dumps({"error": "invalid test_fraction"})
        test_count = int(total * test_fraction)
        train_count = total - test_count
        rec = {
            "method": "time_based",
            "test_fraction": test_fraction,
            "train_index_count": train_count,
            "test_index_count": test_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts
        }
        data.setdefault("dataset_split", []).append(rec)
        return json.dumps({"status": "inserted", "record": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_time_based_dataset_split",
                "description": "Creates a dataset_split record from processed_timeseries row_count using floor(test_fraction*rows).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "processed_csv_path": {"type": "string"},
                        "test_fraction": {"type": "number"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"}
                    },
                    "required": ["processed_csv_path", "test_fraction", "split_summary_json_path", "split_ts"]
                }
            }
        }


class SaveModelRecord(Tool):
    """
    Appends a models record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "model_type", "training_ts", "model_path", "feature_names", "target_name"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("models", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_model_record",
                "description": "Appends a models record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class SavePredictionsRecord(Tool):
    """
    Appends a predictions record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "predictions_csv_path", "row_count", "columns", "generated_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("predictions", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name"), "predictions_csv_path": record.get("predictions_csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_predictions_record",
                "description": "Appends a predictions record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class SaveMetricsRecord(Tool):
    """
    Appends a metrics record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        req = {"model_name", "metrics_csv_path", "generated_ts"}
        if not req.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("metrics", []).append(record)
        return json.dumps({"status": "inserted", "model_name": record.get("model_name"), "metrics_csv_path": record.get("metrics_csv_path")})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "save_metrics_record",
                "description": "Appends a metrics record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }


class PublishStakeholderOutputs(Tool):
    """
    Creates a stakeholder_outputs record after verifying referenced predictions and metrics exist.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], predictions_final_csv_path: str, metrics_summary_csv_path: str, generated_ts: str) -> str:
        preds_ok = False
        for r in data.get("predictions", []):
            if r.get("predictions_csv_path") == predictions_final_csv_path:
                preds_ok = True
                break
        metrics_ok = False
        for r in data.get("metrics", []):
            if r.get("metrics_csv_path") == metrics_summary_csv_path:
                metrics_ok = True
                break
        if not preds_ok or not metrics_ok:
            return json.dumps({"error": "referenced artifacts not found", "predictions_ok": preds_ok, "metrics_ok": metrics_ok})
        rec = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts
        }
        data.setdefault("stakeholder_outputs", []).append(rec)
        return json.dumps({"status": "inserted", "record": rec})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "publish_stakeholder_outputs",
                "description": "Creates a stakeholder_outputs record after verifying predictions and metrics exist.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "predictions_final_csv_path": {"type": "string"},
                        "metrics_summary_csv_path": {"type": "string"},
                        "generated_ts": {"type": "string"}
                    },
                    "required": ["predictions_final_csv_path", "metrics_summary_csv_path", "generated_ts"]
                }
            }
        }

TOOLS = [
    GetProjectConfigByCity(),
    GetFileTextByPath(),
    GetTerminalLogCommandResult(),
    GetGeocodingResultByCity(),
    GetWeatherForecastByCity(),
    GetStationsByLocation(),
    GetWaterLevelsWindow(),
    GetTidePredictionsWindow(),
    GetProcessedTimeseriesSummary(),
    GetFeaturesByCsvPath(),
    GetModelByName(),
    GetPredictionsByModelName(),
    GetMetricsByModelName(),
    GetMcpToolCallsByServer(),
    GetGmailMessageBySubject(),
    UpsertProjectConfig(),
    AddFileDirectoryRecord(),
    UpsertFileStoreText(),
    AppendTerminalLogEntry(),
    RecordGeocodingResult(),
    InsertWeatherForecast(),
    RegisterEtlRun(),
    RegisterProcessedTimeseries(),
    GenerateFeaturesFromProcessed(),
    SaveModelConfig(),
    CreateTimeBasedDatasetSplit(),
    SaveModelRecord(),
    SavePredictionsRecord(),
    SaveMetricsRecord(),
    PublishStakeholderOutputs(),
]
