import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _index_by(items: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
    pass
    return {i.get(key): i for i in items or []}


def _fixed_now_iso() -> str:
    pass
    return "2025-08-20T00:00:00Z"


class FetchProjectConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], key: str = None) -> str:
        cfg = data.get("project_config", {}) or {}
        if key:
            payload = {key: cfg.get(key)}
            out = json.dumps(payload, indent=2)
            return out
        payload = cfg
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectConfig",
                "description": "Fetch project configuration (optionally a single key).",
                "parameters": {
                    "type": "object",
                    "properties": {"key": {"type": "string"}},
                    "required": [],
                },
            },
        }


class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None) -> str:
        if updates is None:
            updates = {}
        cfg = data.get("project_config", {})
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _fixed_now_iso()
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectConfig",
                "description": "Update project configuration with provided key/value pairs.",
                "parameters": {
                    "type": "object",
                    "properties": {"updates": {"type": "object"}},
                    "required": ["updates"],
                },
            },
        }


class FetchEnvironment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        env = data.get("environment", {}) or {}
        payload = env
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEnvironment",
                "description": "Read environment variables/secrets map.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class ModifyEnvironment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None) -> str:
        updates = updates or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _fixed_now_iso()
        payload = {"updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateEnvironment",
                "description": "Update environment variables/secrets.",
                "parameters": {
                    "type": "object",
                    "properties": {"updates": {"type": "object"}},
                    "required": ["updates"],
                },
            },
        }


class BrowseFileStore(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"files": data.get("file_store", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listFileStore",
                "description": "List all files in the file store.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class AddFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], path: str = None, mime_type: str = None, size: int = None) -> str:
        files = data.get("file_store", [])
        max_id = 0
        for f in files:
            try:
                fid = int(f.get("file_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "file_id": new_id,
            "path": path,
            "mime_type": mime_type,
            "size": size,
            "created_at": _fixed_now_iso(),
        }
        files.append(row)
        payload = {"file_id": new_id, "path": row["path"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertFile",
                "description": "Insert a file metadata row into the file store.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "size": {"type": ["integer", "null"]},
                    },
                    "required": ["path", "mime_type"],
                },
            },
        }


class RetrieveFile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, path: str = None) -> str:
        files = data.get("file_store", []) or []
        row = None
        if file_id is not None:
            row = next((f for f in files if str(f.get("file_id")) == str(file_id)), None)
        elif path:
            row = next((f for f in files if f.get("path") == path), None)
        payload = row or {"error": "File not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFile",
                "description": "Read a file store record by id or by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "path": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class LogETLRun(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_name: str = None,
        task: str = None,
        status: str = None,
        rows_processed: int = None
    ) -> str:
        runs = data.get("etl_runs", [])
        max_id = 0
        for r in runs:
            try:
                rid = int(r.get("run_id", 0))
                if rid > max_id:
                    max_id = rid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "run_id": new_id,
            "run_name": run_name,
            "task": task,
            "status": status,
            "rows_processed": rows_processed,
            "started_at": _fixed_now_iso(),
            "finished_at": _fixed_now_iso(),
        }
        runs.append(row)
        payload = {"run_id": new_id, "run_name": row["run_name"]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterEtlRun",
                "description": "Insert a new ETL run record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_name": {"type": "string"},
                        "task": {"type": "string"},
                        "status": {"type": "string"},
                        "rows_processed": {"type": ["integer", "null"]},
                    },
                    "required": ["run_name", "task", "status"],
                },
            },
        }


class FetchETLRunDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], run_id: str = None, run_name: str = None) -> str:
        runs = data.get("etl_runs", []) or []
        row = None
        if run_id is not None:
            row = next((r for r in runs if str(r.get("run_id")) == str(run_id)), None)
        elif run_name:
            row = next((r for r in runs if r.get("run_name") == run_name), None)
        payload = row or {"error": "ETL run not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEtlRunDetails",
                "description": "Read an ETL run by id or by run_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "run_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class RetrieveWaterLevels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], station_id: str = None, start: str = None, end: str = None) -> str:
        station = station_id
        rows = []
        for r in data.get("water_levels", []) or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            rows.append(r)
        payload = {"rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchWaterLevels",
                "description": "Fetch water level rows (optional station/time filters).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "station_id": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class StoreProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], series_name: str = None, items: list = None) -> str:
        table = data.get("processed_timeseries", [])
        items = items or []
        inserted = []
        max_id = 0
        for r in table:
            try:
                rid = int(r.get("row_id", 0))
                if rid > max_id:
                    max_id = rid
            except (ValueError, TypeError):
                continue
        for it in items:
            max_id += 1
            rid = max_id
            row = {
                "row_id": rid,
                "series_name": series_name,
                "timestamp": it.get("timestamp"),
                "value": it.get("value"),
                "source": it.get("source"),
            }
            table.append(row)
            inserted.append(rid)
        payload = {"series_name": series_name, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertProcessedTimeseries",
                "description": "Insert processed timeseries points for a named series.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "series_name": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["series_name", "items"],
                },
            },
        }


class FetchProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], series_name: str = None, start: str = None, end: str = None) -> str:
        rows = []
        for r in data.get("processed_timeseries", []) or []:
            if series_name and r.get("series_name") != series_name:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            rows.append(r)
        payload = {"series_name": series_name, "rows": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProcessedTimeseries",
                "description": "Read processed timeseries rows by series_name and optional time range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "series_name": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
                    },
                    "required": ["series_name"],
                },
            },
        }


class AddFeatureSet(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_set_name: str = None, version: str = None, columns: list = None) -> str:
        feats = data.get("features", [])
        max_id = 0
        for f in feats:
            try:
                fid = int(f.get("feature_set_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "feature_set_id": new_id,
            "feature_set_name": feature_set_name,
            "version": version,
            "columns": columns,
            "created_at": _fixed_now_iso(),
        }
        feats.append(row)
        payload = {"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertFeatureSet",
                "description": "Insert a new feature set descriptor.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "feature_set_name": {"type": "string"},
                        "version": {"type": "string"},
                        "columns": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["feature_set_name", "version", "columns"],
                },
            },
        }


class FetchFeatureSetDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], feature_set_id: str = None, feature_set_name: str = None) -> str:
        feats = data.get("features", []) or []
        row = None
        if feature_set_id is not None:
            row = next(
                (f for f in feats if str(f.get("feature_set_id")) == str(feature_set_id)), None
            )
        elif feature_set_name:
            row = next((f for f in feats if f.get("feature_set_name") == feature_set_name), None)
        payload = row or {"error": "Feature set not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFeatureSetDetails",
                "description": "Read a feature set by id or by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "feature_set_id": {"type": "string"},
                        "feature_set_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class AddModel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        model_name: str = None,
        model_type: str = None,
        framework: str = None,
        version: str = None,
        status: str = None
    ) -> str:
        models = data.get("models", [])
        max_id = 0
        for m in models:
            try:
                mid = int(m.get("model_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "model_id": new_id,
            "model_name": model_name,
            "model_type": model_type,
            "framework": framework,
            "version": version,
            "status": status,
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso(),
        }
        models.append(row)
        payload = {"model_id": new_id, "model_name": row["model_name"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertModel",
                "description": "Register a model in the model registry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "model_type": {"type": "string"},
                        "framework": {"type": "string"},
                        "version": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": [
                        "model_name",
                        "model_type",
                        "framework",
                        "version",
                        "status",
                    ],
                },
            },
        }


class FetchModelDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_id: str = None, model_name: str = None) -> str:
        models = data.get("models", []) or []
        row = None
        if model_id is not None:
            row = next((m for m in models if str(m.get("model_id")) == str(model_id)), None)
        elif model_name:
            row = next((m for m in models if m.get("model_name") == model_name), None)
        payload = row or {"error": "Model not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelDetails",
                "description": "Read a model by id or by model_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_id": {"type": "string"},
                        "model_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class SaveModelConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, config_name: str = None, params: dict = None) -> str:
        if params is None:
            params = {}
        cfgs = data.get("model_config", [])
        row = next(
            (
                c
                for c in cfgs
                if c.get("model_name") == model_name
                and c.get("config_name") == config_name
            ),
            None,
        )
        if row:
            row["params"] = params
            row["updated_at"] = _fixed_now_iso()
            out = {
                "model_name": model_name,
                "config_name": config_name,
                "action": "updated",
            }
        else:
            max_id = 0
            for c in cfgs:
                try:
                    cid = int(c.get("config_id", 0))
                    if cid > max_id:
                        max_id = cid
                except (ValueError, TypeError):
                    continue
            new_id = max_id + 1
            row = {
                "config_id": new_id,
                "model_name": model_name,
                "config_name": config_name,
                "params": params,
                "created_at": _fixed_now_iso(),
            }
            cfgs.append(row)
            out = {
                "config_id": new_id,
                "model_name": model_name,
                "config_name": config_name,
                "action": "inserted",
            }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertModelConfig",
                "description": "Insert or update a model configuration by (model_name, config_name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "config_name": {"type": "string"},
                        "params": {"type": "object"},
                    },
                    "required": ["model_name", "config_name", "params"],
                },
            },
        }


class FetchModelConfig(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, config_name: str = None) -> str:
        cfgs = data.get("model_config", []) or []
        rows = [
            c
            for c in cfgs
            if (not model_name or c.get("model_name") == model_name)
            and (not config_name or c.get("config_name") == config_name)
        ]
        payload = {"configs": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelConfig",
                "description": "List model configs (optionally filtered by model_name and/or config_name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "config_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class LogMetrics(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        model_name: str = None, 
        metric_name: str = None, 
        value: Any = None, 
        dataset_split: str = None
    ) -> str:
        metrics = data.get("metrics", [])
        max_id = 0
        for m in metrics:
            try:
                mid = int(m.get("metric_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "metric_id": new_id,
            "model_name": model_name,
            "metric_name": metric_name,
            "value": value,
            "dataset_split": dataset_split,
            "timestamp": _fixed_now_iso(),
        }
        metrics.append(row)
        payload = {
            "metric_id": new_id,
            "model_name": row["model_name"],
            "metric_name": row["metric_name"],
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertMetrics",
                "description": "Insert a metrics row for a model and split.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "value": {"type": "number"},
                        "dataset_split": {"type": "string"},
                    },
                    "required": ["model_name", "metric_name", "value", "dataset_split"],
                },
            },
        }


class RetrieveMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, metric_name: str = None, dataset_split: str = None) -> str:
        metrics = data.get("metrics", []) or []
        rows = [
            m
            for m in metrics
            if (not model_name or m.get("model_name") == model_name)
            and (not metric_name or m.get("metric_name") == metric_name)
            and (not dataset_split or m.get("dataset_split") == dataset_split)
        ]
        payload = {"metrics": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMetrics",
                "description": "List metrics (filter by model_name, metric_name, dataset_split).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "metric_name": {"type": "string"},
                        "dataset_split": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class AddPredictionBatch(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], batch_name: str = None, model_name: str = None, items: list = None) -> str:
        preds = data.get("predictions", [])
        max_id = 0
        for p in preds:
            try:
                pid = int(p.get("prediction_id", 0))
                if pid > max_id:
                    max_id = pid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "prediction_id": new_id,
            "batch_name": batch_name,
            "model_name": model_name,
            "items": items or [],
            "created_at": _fixed_now_iso(),
        }
        preds.append(row)
        payload = {"prediction_id": new_id, "batch_name": row["batch_name"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertPredictionBatch",
                "description": "Insert a batch of predictions for a model.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "batch_name": {"type": "string"},
                        "model_name": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["batch_name", "model_name", "items"],
                },
            },
        }


class RetrievePredictions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], batch_name: str = None, model_name: str = None) -> str:
        preds = data.get("predictions", []) or []
        rows = [
            p
            for p in preds
            if (not batch_name or p.get("batch_name") == batch_name)
            and (not model_name or p.get("model_name") == model_name)
        ]
        payload = {"predictions": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPredictions",
                "description": "Read prediction batches (filter by batch_name and/or model_name).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "batch_name": {"type": "string"},
                        "model_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GenerateQCFigure(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], figure_label: str = None) -> str:
        label = figure_label
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        payload = {"figure_path": pdf_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportQcFigure",
                "description": "Export a QC figure/report and return its deterministic pdf path.",
                "parameters": {
                    "type": "object",
                    "properties": {"figure_label": {"type": "string"}},
                    "required": ["figure_label"],
                },
            },
        }


class StoreQCFigure(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        figure_label: str = None, 
        figure_path: str = None, 
        artifact_type: str = None, 
        related_model_name: str = None
    ) -> str:
        figs = data.get("qc_figures", [])
        max_id = 0
        for f in figs:
            try:
                fid = int(f.get("figure_id", 0))
                if fid > max_id:
                    max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "figure_id": new_id,
            "figure_label": figure_label,
            "figure_path": figure_path,
            "artifact_type": artifact_type,
            "related_model_name": related_model_name,
            "created_at": _fixed_now_iso(),
        }
        figs.append(row)
        payload = {"figure_id": new_id, "figure_label": row["figure_label"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertQcFigure",
                "description": "Insert a QC figure record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_label": {"type": "string"},
                        "figure_path": {"type": "string"},
                        "artifact_type": {"type": "string"},
                        "related_model_name": {"type": ["string", "null"]},
                    },
                    "required": ["figure_label", "figure_path", "artifact_type"],
                },
            },
        }


class FetchQCFigure(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], figure_id: str = None, figure_label: str = None) -> str:
        figs = data.get("qc_figures", []) or []
        fid = figure_id
        label = figure_label
        row = None
        if fid is not None:
            row = next((f for f in figs if str(f.get("figure_id")) == str(fid)), None)
        elif label:
            row = next((f for f in figs if f.get("figure_label") == label), None)
        payload = row or {"error": "QC figure not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetQcFigure",
                "description": "Read a QC figure by id or label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "figure_id": {"type": "string"},
                        "figure_label": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class SaveStakeholderOutput(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_label: str = None, audience: str = None, artifact_path: str = None) -> str:
        outs = data.get("stakeholder_outputs", [])
        max_id = 0
        for o in outs:
            try:
                oid = int(o.get("output_id", 0))
                if oid > max_id:
                    max_id = oid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "output_id": new_id,
            "output_label": output_label,
            "audience": audience,
            "artifact_path": artifact_path,
            "created_at": _fixed_now_iso(),
        }
        outs.append(row)
        payload = {"output_id": new_id, "output_label": row["output_label"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InsertStakeholderOutput",
                "description": "Insert a stakeholder output record pointing to an artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_label": {"type": "string"},
                        "audience": {"type": "string"},
                        "artifact_path": {"type": "string"},
                    },
                    "required": ["output_label", "audience", "artifact_path"],
                },
            },
        }


class FetchStakeholderOutput(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], output_id: str = None, output_label: str = None) -> str:
        outs = data.get("stakeholder_outputs", []) or []
        row = None
        if output_id is not None:
            row = next((o for o in outs if str(o.get("output_id")) == str(output_id)), None)
        elif output_label:
            row = next((o for o in outs if o.get("output_label") == output_label), None)
        payload = row or {"error": "Stakeholder output not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStakeholderOutput",
                "description": "Read a stakeholder output by id or label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "output_id": {"type": "string"},
                        "output_label": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class DispatchResultsEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        to_address: str = None,
        subject: str = None,
        body_text: str = None,
        attachment: str = None,
        model_name: str = None,
        batch_name: str = None
    ) -> str:
        inbox = data.get("gmail_messages", [])
        max_id = 0
        for m in inbox:
            try:
                mid = int(m.get("message_id", 0))
                if mid > max_id:
                    max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "message_id": new_id,
            "to": to_address,
            "subject": subject,
            "body_text": body_text,
            "attachment": attachment,
            "model_name": model_name,
            "batch_name": batch_name,
            "sent_at": _fixed_now_iso(),
        }
        inbox.append(row)
        payload = {"status": "sent", "message_id": new_id, "to": row["to"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendResultsEmail",
                "description": "Send a results email with an attachment (deterministic parameters only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "to_address": {"type": "string"},
                        "subject": {"type": "string"},
                        "body_text": {"type": "string"},
                        "attachment": {"type": "string"},
                        "model_name": {"type": "string"},
                        "batch_name": {"type": "string"},
                    },
                    "required": ["to_address", "subject", "body_text", "attachment"],
                },
            },
        }


class WriteTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None, message: str = None) -> str:
        logs = data.get("terminal_log", [])
        max_id = 0
        for l in logs:
            try:
                lid = int(l.get("log_id", 0))
                if lid > max_id:
                    max_id = lid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "log_id": new_id,
            "event_type": event_type,
            "message": message,
            "created_at": _fixed_now_iso(),
        }
        logs.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordTerminalLog",
                "description": "Append a terminal log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["event_type", "message"],
                },
            },
        }


class BrowseTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None) -> str:
        logs = data.get("terminal_log", []) or []
        rows = [
            l for l in logs if (not event_type or l.get("event_type") == event_type)
        ]
        payload = {"logs": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTerminalLog",
                "description": "List terminal log entries (optionally filter by event_type).",
                "parameters": {
                    "type": "object",
                    "properties": {"event_type": {"type": "string"}},
                    "required": [],
                },
            },
        }


TOOLS = [
    FetchEnvironment(),
    ModifyEnvironment(),
    AddModel(),
    FetchModelDetails(),
    BrowseFileStore(),
    AddFile(),
    RetrieveFile(),
    LogETLRun(),
    FetchETLRunDetails(),
    FetchProjectConfig(),
    ModifyProjectConfig(),
    RetrieveWaterLevels(),
    StoreProcessedTimeseries(),
    FetchProcessedTimeseries(),
    AddFeatureSet(),
    FetchFeatureSetDetails(),
    SaveModelConfig(),
    FetchModelConfig(),
    LogMetrics(),
    RetrieveMetrics(),
    AddPredictionBatch(),
    RetrievePredictions(),
    GenerateQCFigure(),
    StoreQCFigure(),
    FetchQCFigure(),
    SaveStakeholderOutput(),
    FetchStakeholderOutput(),
    DispatchResultsEmail(),
    WriteTerminalLog(),
    BrowseTerminalLog(),
]
