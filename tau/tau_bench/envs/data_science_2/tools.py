import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class GetProjectConfigByCity(Tool):
    """Fetches a project_config entry based on target_city."""

    @staticmethod
    def invoke(data: dict[str, Any], target_city: str) -> str:
        rows = data.get("project_config", [])
        for row in rows:
            if row.get("target_city") == target_city:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "project_config not found", "target_city": target_city}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectConfigByCity",
                "description": "Retrieves a project_config entry by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "target_city": {
                            "type": "string",
                            "description": "City name key in project_config.",
                        }
                    },
                    "required": ["target_city"],
                },
            },
        }


class GetFileTextByPath(Tool):
    """Provides file content and metadata from file_store using the specified path."""

    @staticmethod
    def invoke(data: dict[str, Any], path: str) -> str:
        rows = data.get("file_store", [])
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                out = {
                    "path": path,
                    "file_contents_text": (
                        row.get("file_contents_text", [None] * len(paths))[i]
                        if i < len(row.get("file_contents_text", []))
                        else None
                    ),
                    "file_mime_types": (
                        row.get("file_mime_types", [None] * len(paths))[i]
                        if i < len(row.get("file_mime_types", []))
                        else None
                    ),
                    "char_counts": (
                        row.get("char_counts", [None] * len(paths))[i]
                        if i < len(row.get("char_counts", []))
                        else None
                    ),
                }
                payload = out
                out = json.dumps(payload)
                return out
        payload = {"error": "file not found", "path": path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileTextByPath",
                "description": "Returns file text and metadata from file_store by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Exact file path stored in file_store.paths.",
                        }
                    },
                    "required": ["path"],
                },
            },
        }


class GetTerminalLogCommandResult(Tool):
    """Fetches a terminal_log entry using the precise command string."""

    @staticmethod
    def invoke(data: dict[str, Any], command: str, terminal_log: list[dict[str, Any]] = None) -> str:
        rows = terminal_log or []
        for row in rows:
            cmds = row.get("commands", [])
            if command in cmds:
                i = cmds.index(command)
                out = {
                    "command": command,
                    "exit_code": (
                        row.get("exit_codes", [None] * len(cmds))[i]
                        if i < len(row.get("exit_codes", []))
                        else None
                    ),
                    "stdout": (
                        row.get("stdouts", [None] * len(cmds))[i]
                        if i < len(row.get("stdouts", []))
                        else None
                    ),
                    "stderr": (
                        row.get("stderrs", [None] * len(cmds))[i]
                        if i < len(row.get("stderrs", []))
                        else None
                    ),
                    "printed_message": (
                        row.get("printed_messages", [None] * len(cmds))[i]
                        if i < len(row.get("printed_messages", []))
                        else None
                    ),
                    "printed_ts": (
                        row.get("printed_ts", [None] * len(cmds))[i]
                        if i < len(row.get("printed_ts", []))
                        else None
                    ),
                }
                payload = out
                out = json.dumps(payload)
                return out
        payload = {"error": "command not found", "command": command}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTerminalLogCommandResult",
                "description": "Retrieves a terminal_log entry by exact command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Exact command string to look up.",
                        }
                    },
                    "required": ["command"],
                },
            },
        }


class GetGeocodingResultByCity(Tool):
    """Fetches geocoding_results based on query_city."""

    @staticmethod
    def invoke(data: dict[str, Any], query_city: str) -> str:
        rows = data.get("geocoding_results", [])
        for row in rows:
            if row.get("query_city") == query_city:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "geocoding result not found", "query_city": query_city}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGeocodingResultByCity",
                "description": "Retrieves a geocoding result by query_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {
                            "type": "string",
                            "description": "City name used in geocoding query.",
                        }
                    },
                    "required": ["query_city"],
                },
            },
        }


class GetWeatherForecastByCity(Tool):
    """Fetches a weather_forecasts record using city and horizon_days."""

    @staticmethod
    def invoke(data: dict[str, Any], city: str, horizon_days: int) -> str:
        rows = data.get("weather_forecasts", [])
        for row in rows:
            if row.get("city") == city and row.get("horizon_days") == horizon_days:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {
            "error": "weather forecast not found",
            "city": city,
            "horizon_days": horizon_days,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWeatherForecastByCity",
                "description": "Retrieves weather_forecasts by city and exact horizon_days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string"},
                        "horizon_days": {"type": "integer"},
                    },
                    "required": ["city", "horizon_days"],
                },
            },
        }


class GetStationsByLocation(Tool):
    """Provides a noaa_station_searches record based on precise latitude, longitude, and radius_km."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_latitude: float,
        query_longitude: float,
        radius_km: float,
    ) -> str:
        rows = data.get("noaa_station_searches", [])
        for row in rows:
            if (
                row.get("query_latitude") == query_latitude
                and row.get("query_longitude") == query_longitude
                and row.get("radius_km") == radius_km
            ):
                payload = row
                out = json.dumps(payload)
                return out
        payload = {
            "error": "station search not found",
            "query_latitude": query_latitude,
            "query_longitude": query_longitude,
            "radius_km": radius_km,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStationsByLocation",
                "description": "Returns a noaa_station_searches record by exact query coordinates and radius.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"},
                    },
                    "required": ["query_latitude", "query_longitude", "radius_km"],
                },
            },
        }


class GetWaterLevelsWindow(Tool):
    """Provides a portion of water_levels for a station during [window_start_ts, window_end_ts]."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        station_id: str,
        window_start_ts: str,
        window_end_ts: str
    ) -> str:
        rows = data.get("water_levels", [])
        for row in rows:
            if (
                row.get("station_id") == station_id
                and row.get("start_ts") <= window_start_ts
                and row.get("end_ts") >= window_end_ts
            ):
                ts = row.get("timestamps", [])
                wl = row.get("water_level_m", [])
                out_ts = []
                out_wl = []
                for t, v in zip(ts, wl):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_wl.append(v)
                payload = {
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "water_level_m": out_wl,
                    "units": row.get("units"),
                    "datum_nullable": row.get("datum_nullable"),
                }
                out = json.dumps(payload)
                return out
        payload = {
            "error": "window not covered",
            "station_id": station_id,
            "window_start_ts": window_start_ts,
            "window_end_ts": window_end_ts,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetWaterLevelsWindow",
                "description": "Returns subset of water_levels for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"},
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"],
                },
            },
        }


class GetTidePredictionsWindow(Tool):
    """Provides a portion of tide_predictions for a station during [window_start_ts, window_end_ts]."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        station_id: str,
        window_start_ts: str,
        window_end_ts: str
    ) -> str:
        rows = data.get("tide_predictions", [])
        for row in rows:
            if (
                row.get("station_id") == station_id
                and row.get("start_ts") <= window_start_ts
                and row.get("end_ts") >= window_end_ts
            ):
                ts = row.get("timestamps", [])
                tp = row.get("tide_pred_m", [])
                out_ts = []
                out_tp = []
                for t, v in zip(ts, tp):
                    if window_start_ts <= t <= window_end_ts:
                        out_ts.append(t)
                        out_tp.append(v)
                payload = {
                    "station_id": station_id,
                    "timestamps": out_ts,
                    "tide_pred_m": out_tp,
                    "units": row.get("units"),
                    "method_nullable": row.get("method_nullable"),
                }
                out = json.dumps(payload)
                return out
        payload = {
            "error": "window not covered",
            "station_id": station_id,
            "window_start_ts": window_start_ts,
            "window_end_ts": window_end_ts,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTidePredictionsWindow",
                "description": "Returns subset of tide_predictions for a station and time window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "window_start_ts": {"type": "string"},
                        "window_end_ts": {"type": "string"},
                    },
                    "required": ["station_id", "window_start_ts", "window_end_ts"],
                },
            },
        }


class GetProcessedTimeseriesSummary(Tool):
    """Fetches processed_timeseries using csv_path."""

    @staticmethod
    def invoke(data: dict[str, Any], csv_path: str) -> str:
        rows = data.get("processed_timeseries", [])
        for row in rows:
            if row.get("csv_path") == csv_path:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "processed_timeseries not found", "csv_path": csv_path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProcessedTimeseriesSummary",
                "description": "Retrieves processed_timeseries record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"csv_path": {"type": "string"}},
                    "required": ["csv_path"],
                },
            },
        }


class GetFeaturesByCsvPath(Tool):
    """Fetches features record using csv_path."""

    @staticmethod
    def invoke(data: dict[str, Any], csv_path: str) -> str:
        rows = data.get("features", [])
        for row in rows:
            if row.get("csv_path") == csv_path:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "features not found", "csv_path": csv_path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFeaturesByCsvPath",
                "description": "Retrieves features record by csv_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"csv_path": {"type": "string"}},
                    "required": ["csv_path"],
                },
            },
        }


class GetModelByName(Tool):
    """Fetches models record based on model_name."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str) -> str:
        rows = data.get("models", [])
        for row in rows:
            if row.get("model_name") == model_name:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "model not found", "model_name": model_name}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelByName",
                "description": "Retrieves models record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class GetPredictionsByModelName(Tool):
    """Fetches predictions record using model_name."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str) -> str:
        rows = data.get("predictions", [])
        for row in rows:
            if row.get("model_name") == model_name:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "predictions not found", "model_name": model_name}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPredictionsByModelName",
                "description": "Retrieves predictions record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class GetMetricsByModelName(Tool):
    """Fetches metrics record based on model_name."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str) -> str:
        rows = data.get("metrics", [])
        for row in rows:
            if row.get("model_name") == model_name:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "metrics not found", "model_name": model_name}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMetricsByModelName",
                "description": "Retrieves metrics record by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {"model_name": {"type": "string"}},
                    "required": ["model_name"],
                },
            },
        }


class GetMcpToolCallsByServer(Tool):
    """Provides flattened MCP tool call entries filtered by the server name."""

    @staticmethod
    def invoke(data: dict[str, Any], server_name: str) -> str:
        rows = data.get("mcp_tool_calls", [])
        out: list[dict[str, Any]] = []
        for row in rows:
            servers = row.get("server_names", [])
            tools = row.get("tool_names", [])
            params = row.get("params_json", [])
            metas = row.get("response_meta_nullable", [])
            times = row.get("called_ts", [])
            for i, s in enumerate(servers):
                if s == server_name:
                    out.append(
                        {
                            "server_name": s,
                            "tool_name": tools[i] if i < len(tools) else None,
                            "params_json": params[i] if i < len(params) else None,
                            "response_meta_nullable": (
                                metas[i] if i < len(metas) else None
                            ),
                            "called_ts": times[i] if i < len(times) else None,
                        }
                    )
        payload = {"items": out}
        out_str = json.dumps(payload)
        return out_str

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMcpToolCallsByServer",
                "description": "Returns flattened MCP tool call entries filtered by server name.",
                "parameters": {
                    "type": "object",
                    "properties": {"server_name": {"type": "string"}},
                    "required": ["server_name"],
                },
            },
        }


class GetGmailMessageBySubject(Tool):
    """Fetches a gmail_messages record using the precise subject."""

    @staticmethod
    def invoke(data: dict[str, Any], subject: str) -> str:
        rows = data.get("gmail_messages", [])
        for row in rows:
            if row.get("subject") == subject:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "gmail message not found", "subject": subject}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailMessageBySubject",
                "description": "Retrieves a gmail_messages record by exact subject.",
                "parameters": {
                    "type": "object",
                    "properties": {"subject": {"type": "string"}},
                    "required": ["subject"],
                },
            },
        }


class UpsertProjectConfig(Tool):
    """Adds or modifies a project_config record based on target_city."""

    @staticmethod
    def invoke(data: dict[str, Any], record: dict[str, Any]) -> str:
        if "target_city" not in record:
            payload = {"error": "missing target_city"}
            out = json.dumps(payload)
            return out
        rows = data.setdefault("project_config", [])
        for row in rows:
            if row.get("target_city") == record["target_city"]:
                row.update(record)
                payload = {"status": "updated", "record": row}
                out = json.dumps(payload)
                return out
        rows.append(record)
        payload = {"status": "inserted", "record": record}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertProjectConfig",
                "description": "Inserts or updates a project_config record by target_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {
                            "type": "object",
                            "description": "Full project_config record with target_city as key.",
                        }
                    },
                    "required": ["record"],
                },
            },
        }


class AddFileDirectoryRecord(Tool):
    """Adds a new file_directory record using parallel arrays."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        paths: list[str],
        file_sizes_bytes: list[int],
        file_hashes_sha256: list[str | None],
        file_mime_types: list[str],
        created_ts: list[str],
        updated_ts: list[str],
    ) -> str:
        n = len(paths)
        if not all(
            len(lst) == n
            for lst in [
                file_sizes_bytes,
                file_hashes_sha256,
                file_mime_types,
                created_ts,
                updated_ts,
            ]
        ):
            payload = {"error": "all arrays must have the same length"}
            out = json.dumps(payload)
            return out
        row = {
            "paths": paths,
            "file_sizes_bytes": file_sizes_bytes,
            "file_hashes_sha256": file_hashes_sha256,
            "file_mime_types": file_mime_types,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
        }
        data.setdefault("file_directory", []).append(row)
        payload = {"status": "inserted", "record": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addFileDirectoryRecord",
                "description": "Appends a new file_directory record with parallel arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "paths": {"type": "array", "items": {"type": "string"}},
                        "file_sizes_bytes": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "file_hashes_sha256": {
                            "type": "array",
                            "items": {"type": ["string", "null"]},
                        },
                        "file_mime_types": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "created_ts": {"type": "array", "items": {"type": "string"}},
                        "updated_ts": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "paths",
                        "file_sizes_bytes",
                        "file_hashes_sha256",
                        "file_mime_types",
                        "created_ts",
                        "updated_ts",
                    ],
                },
            },
        }


class UpsertFileStoreText(Tool):
    """Adds or modifies a file_store path entry with text, mime type, and character count."""

    @staticmethod
    def invoke(
        data: dict[str, Any], path: str, file_contents_text: str, file_mime_type: str
    ) -> str:
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
                payload = {"status": "updated", "path": path}
                out = json.dumps(payload)
                return out
        rows.append(
            {
                "paths": [path],
                "file_contents_text": [file_contents_text],
                "file_mime_types": [file_mime_type],
                "char_counts": [len(file_contents_text)],
            }
        )
        payload = {"status": "inserted", "path": path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertFileStoreText",
                "description": "Inserts or updates a file_store path entry with text and metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "file_contents_text": {"type": "string"},
                        "file_mime_type": {"type": "string"},
                    },
                    "required": ["path", "file_contents_text", "file_mime_type"],
                },
            },
        }


class AppendTerminalLogEntry(Tool):
    """Adds a single entry to terminal_log arrays in the first record or initializes a new one."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        command: str,
        exit_code: int,
        stdout: str,
        stderr: str,
        printed_message: str,
        printed_ts: str,
    ) -> str:
        rows = data.setdefault("terminal_log", [])
        if not rows:
            rows.append(
                {
                    "commands": [],
                    "exit_codes": [],
                    "stdouts": [],
                    "stderrs": [],
                    "printed_messages": [],
                    "printed_ts": [],
                }
            )
        row = rows[0]
        row.setdefault("commands", []).append(command)
        row.setdefault("exit_codes", []).append(exit_code)
        row.setdefault("stdouts", []).append(stdout)
        row.setdefault("stderrs", []).append(stderr)
        row.setdefault("printed_messages", []).append(printed_message)
        row.setdefault("printed_ts", []).append(printed_ts)
        payload = {"status": "appended", "index": len(row["commands"]) - 1}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLogEntry",
                "description": "Appends a single entry to terminal_log arrays.",
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
                    "required": [
                        "command",
                        "exit_code",
                        "stdout",
                        "stderr",
                        "printed_message",
                        "printed_ts",
                    ],
                },
            },
        }


class RecordGeocodingResult(Tool):
    """Adds a geocoding_results record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_city: str,
        latitude: float,
        longitude: float,
        canonical_name: str,
        provider: str,
        query_ts: str
    ) -> str:
        record = {
            "query_city": query_city,
            "latitude": latitude,
            "longitude": longitude,
            "canonical_name": canonical_name,
            "provider": provider,
            "query_ts": query_ts
        }
        if not {
            "query_city",
            "latitude",
            "longitude",
            "canonical_name",
            "provider",
            "query_ts",
        }.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("geocoding_results", []).append(record)
        payload = {"status": "inserted", "record": record}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recordGeocodingResult",
                "description": "Appends a geocoding_results record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class InsertWeatherForecast(Tool):
    """Adds a weather_forecasts record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        city: str,
        latitude: float,
        longitude: float,
        variables: list[str],
        timezone: str,
        horizon_days: int,
        start_ts: str,
        end_ts: str,
        timestamps: list[str],
        provider: str,
        fetched_ts: str,
        precipitation_mm_hr_nullable: list[float] = None,
        temperature_2m_c_nullable: list[float] = None,
        wind_speed_10m_ms_nullable: list[float] = None,
    ) -> str:
        req = {
            "city",
            "latitude",
            "longitude",
            "variables",
            "timezone",
            "horizon_days",
            "start_ts",
            "end_ts",
            "timestamps",
            "provider",
            "fetched_ts",
        }
        record = {
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
            "variables": variables,
            "timezone": timezone,
            "horizon_days": horizon_days,
            "start_ts": start_ts,
            "end_ts": end_ts,
            "timestamps": timestamps,
            "provider": provider,
            "fetched_ts": fetched_ts,
            "precipitation_mm_hr_nullable": precipitation_mm_hr_nullable,
            "temperature_2m_c_nullable": temperature_2m_c_nullable,
            "wind_speed_10m_ms_nullable": wind_speed_10m_ms_nullable,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        ts = record.get("timestamps", [])
        for k in [
            "precipitation_mm_hr_nullable",
            "temperature_2m_c_nullable",
            "wind_speed_10m_ms_nullable",
        ]:
            if (
                k in record
                and isinstance(record[k], list)
                and len(record[k]) != len(ts)
            ):
                payload = {"error": "array length mismatch", "field": k}
                out = json.dumps(payload)
                return out
        data.setdefault("weather_forecasts", []).append(record)
        payload = {
            "status": "inserted",
            "record": {
                "city": record.get("city"),
                "horizon_days": record.get("horizon_days"),
            },
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "insertWeatherForecast",
                "description": "Appends a weather_forecasts record with required fields and aligned arrays.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class RegisterEtlRun(Tool):
    """Adds an etl_runs record."""

    @staticmethod
    def invoke(data: dict[str, Any], run_id: str, input_paths: Any, output_paths: Any, status: str, started_ts: Any) -> str:
        req = {"run_id", "input_paths", "output_paths", "status", "started_ts"}
        record = {
            "run_id": run_id,
            "input_paths": input_paths,
            "output_paths": output_paths,
            "status": status,
            "started_ts": started_ts
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("etl_runs", []).append(record)
        payload = {"status": "inserted", "run_id": record.get("run_id")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "registerEtlRun",
                "description": "Appends an etl_runs record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class RegisterProcessedTimeseries(Tool):
    """Adds a processed_timeseries record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        csv_path: str = None,
        columns: list[str] = None,
        row_count: int = None,
        min_timestamp: str = None,
        max_timestamp: str = None,
        file_hash_sha256: str = None,
        created_ts: str = None
    ) -> str:
        req = {
            "csv_path",
            "columns",
            "row_count",
            "min_timestamp",
            "max_timestamp",
            "file_hash_sha256",
            "created_ts",
        }
        record = {
            "csv_path": csv_path,
            "columns": columns,
            "row_count": row_count,
            "min_timestamp": min_timestamp,
            "max_timestamp": max_timestamp,
            "file_hash_sha256": file_hash_sha256,
            "created_ts": created_ts,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("processed_timeseries", []).append(record)
        payload = {"status": "inserted", "csv_path": csv_path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "registerProcessedTimeseries",
                "description": "Appends a processed_timeseries record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class GenerateFeaturesFromProcessed(Tool):
    """Creates a features record from an existing processed_timeseries csv_path following deterministic rules."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        processed_csv_path: str,
        features_csv_path: str,
        generated_ts: str,
    ) -> str:
        rows = data.get("processed_timeseries", [])
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


class SaveModelConfig(Tool):
    """Adds a model_config record."""

    @staticmethod
    def invoke(data: dict[str, Any], saved_json_path: str = None, created_ts: str = None) -> str:
        record = {"saved_json_path": saved_json_path, "created_ts": created_ts}
        req = {"saved_json_path", "created_ts"}
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("model_config", []).append(record)
        payload = {"status": "inserted", "saved_json_path": record.get("saved_json_path")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveModelConfig",
                "description": "Appends a model_config record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class CreateTimeBasedDatasetSplit(Tool):
    """Generates a dataset_split record from processed_timeseries row_count using a deterministic floor split."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        processed_csv_path: str,
        test_fraction: float,
        split_summary_json_path: str,
        split_ts: str,
    ) -> str:
        pts = data.get("processed_timeseries", [])
        row = None
        for r in pts:
            if r.get("csv_path") == processed_csv_path:
                row = r
                break
        if not row:
            payload = {
                "error": "processed_timeseries not found",
                "csv_path": processed_csv_path,
            }
            out = json.dumps(payload)
            return out
        total = int(row.get("row_count", 0))
        if test_fraction < 0 or test_fraction > 1:
            payload = {"error": "invalid test_fraction"}
            out = json.dumps(payload)
            return out
        test_count = int(total * test_fraction)
        train_count = total - test_count
        rec = {
            "method": "time_based",
            "test_fraction": test_fraction,
            "train_index_count": train_count,
            "test_index_count": test_count,
            "split_summary_json_path": split_summary_json_path,
            "split_ts": split_ts,
        }
        data.setdefault("dataset_split", []).append(rec)
        payload = {"status": "inserted", "record": rec}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTimeBasedDatasetSplit",
                "description": "Creates a dataset_split record from processed_timeseries row_count using floor(test_fraction*rows).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "processed_csv_path": {"type": "string"},
                        "test_fraction": {"type": "number"},
                        "split_summary_json_path": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": [
                        "processed_csv_path",
                        "test_fraction",
                        "split_summary_json_path",
                        "split_ts",
                    ],
                },
            },
        }


class SaveModelRecord(Tool):
    """Adds a models record."""

    @staticmethod
    def invoke(data: dict[str, Any], record: dict[str, Any]) -> str:
        req = {
            "model_name",
            "model_type",
            "training_ts",
            "model_path",
            "feature_names",
            "target_name",
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("models", []).append(record)
        payload = {"status": "inserted", "model_name": record.get("model_name")}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveModelRecord",
                "description": "Appends a models record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class SavePredictionsRecord(Tool):
    """Adds a predictions record."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str, predictions_csv_path: str, row_count: int, columns: list, generated_ts: str) -> str:
        req = {
            "model_name",
            "predictions_csv_path",
            "row_count",
            "columns",
            "generated_ts",
        }
        record = {
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
            "row_count": row_count,
            "columns": columns,
            "generated_ts": generated_ts,
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("predictions", []).append(record)
        payload = {
            "status": "inserted",
            "model_name": model_name,
            "predictions_csv_path": predictions_csv_path,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "savePredictionsRecord",
                "description": "Appends a predictions record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class SaveMetricsRecord(Tool):
    """Adds a metrics record."""

    @staticmethod
    def invoke(data: dict[str, Any], model_name: str, metrics_csv_path: str, generated_ts: str) -> str:
        req = {"model_name", "metrics_csv_path", "generated_ts"}
        record = {
            "model_name": model_name,
            "metrics_csv_path": metrics_csv_path,
            "generated_ts": generated_ts
        }
        if not req.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("metrics", []).append(record)
        payload = {
            "status": "inserted",
            "model_name": record.get("model_name"),
            "metrics_csv_path": record.get("metrics_csv_path"),
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveMetricsRecord",
                "description": "Appends a metrics record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }


class PublishStakeholderOutputs(Tool):
    """Generates a stakeholder_outputs record after confirming that referenced predictions and metrics are present."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        predictions_final_csv_path: str,
        metrics_summary_csv_path: str,
        generated_ts: str,
    ) -> str:
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
            payload = {
                "error": "referenced artifacts not found",
                "predictions_ok": preds_ok,
                "metrics_ok": metrics_ok,
            }
            out = json.dumps(payload)
            return out
        rec = {
            "predictions_final_csv_path": predictions_final_csv_path,
            "metrics_summary_csv_path": metrics_summary_csv_path,
            "generated_ts": generated_ts,
        }
        data.setdefault("stakeholder_outputs", []).append(rec)
        payload = {"status": "inserted", "record": rec}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PublishStakeholderOutputs",
                "description": "Creates a stakeholder_outputs record after verifying predictions and metrics exist.",
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
                        "generated_ts",
                    ],
                },
            },
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