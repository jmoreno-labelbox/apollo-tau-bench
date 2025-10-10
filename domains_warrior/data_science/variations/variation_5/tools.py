from typing import Dict, Any, List, Optional
from domains.dto import Tool
import json


# --- deterministic clock for reproducibility ---
def _now_iso_fixed() -> str:
    return "2025-08-20T00:00:00Z"


def _by_key(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in (items or [])}


# ---------------- Project / Environment ----------------

class ReadProjectSettings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfg = data.get("project_config", {}) or {}
        key = kwargs.get("key")
        if key:
            return json.dumps({key: cfg.get(key)}, indent=2)
        return json.dumps(cfg, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_project_settings",
            "description": "Return full project settings or a single key.",
            "parameters": {"type": "object", "properties": {"key": {"type": "string"}}, "required": []}
        }}


class PatchProjectSettings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        cfg = data.get("project_config", {})
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _now_iso_fixed()
        return json.dumps({"updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "patch_project_settings",
            "description": "Apply key/value updates to project settings.",
            "parameters": {"type": "object", "properties": {"updates": {"type": "object"}}, "required": ["updates"]}
        }}


class ReadRuntimeEnv(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        env = data.get("environment", {}) or {}
        return json.dumps(env, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_runtime_env",
            "description": "Read the environment variables/secrets map.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}


class PatchRuntimeEnv(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _now_iso_fixed()
        return json.dumps({"updated": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "patch_runtime_env",
            "description": "Update environment variables/secrets.",
            "parameters": {"type": "object", "properties": {"updates": {"type": "object"}}, "required": ["updates"]}
        }}


# ---------------- File store ----------------

class BrowseFileIndex(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"files": data.get("file_store", [])}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "browse_file_index",
            "description": "List all file metadata rows.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}


class RegisterFileEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files = data.get("file_store", [])
        max_id = 0
        for f in files:
            try:
                fid = int(f.get("file_id", 0))
                if fid > max_id: max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "file_id": new_id,
            "path": kwargs.get("path"),
            "mime_type": kwargs.get("mime_type"),
            "size": kwargs.get("size"),
            "created_at": _now_iso_fixed()
        }
        files.append(row)
        return json.dumps({"file_id": new_id, "path": row["path"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_file_entry",
            "description": "Create a file metadata record.",
            "parameters": {"type": "object", "properties": {
                "path": {"type": "string"},
                "mime_type": {"type": "string"},
                "size": {"type": ["integer", "null"]}
            }, "required": ["path", "mime_type"]}
        }}


class RetrieveFileEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files = data.get("file_store", []) or []
        fid = kwargs.get("file_id")
        path = kwargs.get("path")
        row = None
        if fid is not None:
            row = next((f for f in files if str(f.get("file_id")) == str(fid)), None)
        elif path:
            row = next((f for f in files if f.get("path") == path), None)
        return json.dumps(row or {"error": "File not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "retrieve_file_entry",
            "description": "Read a file metadata record by id or path.",
            "parameters": {"type": "object", "properties": {
                "file_id": {"type": "string"},
                "path": {"type": "string"}
            }, "required": []}
        }}


# ---------------- NOAA / Weather ----------------

class ReadWeatherForecast(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get("city")
        rows = data.get("weather_forecasts", []) or []
        if city:
            rows = [r for r in rows if r.get("city") == city]
        return json.dumps({"rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_weather_forecast",
            "description": "Fetch Open-Meteo style forecast rows (optional city filter).",
            "parameters": {"type": "object", "properties": {"city": {"type": "string"}}, "required": []}
        }}


class ReadNoaaStationSearches(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("noaa_station_searches", []) or []
        return json.dumps({"rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_noaa_station_searches",
            "description": "List prior NOAA station discovery queries/results.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}


class QueryWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station = kwargs.get("station_id")
        start = kwargs.get("start")
        end = kwargs.get("end")
        out = []
        for r in data.get("water_levels", []) or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            out.append(r)
        return json.dumps({"rows": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "query_water_levels",
            "description": "Read observed water-level rows (optional station/time filters).",
            "parameters": {"type": "object", "properties": {
                "station_id": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Processed series ----------------

class WriteProcessedSeries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        table = data.get("processed_timeseries", [])
        series_name = kwargs.get("series_name")
        items = kwargs.get("items") or []
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
        return json.dumps({"series_name": series_name, "inserted_row_ids": inserted}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_processed_series",
            "description": "Insert derived/processed time-series points.",
            "parameters": {"type": "object", "properties": {
                "series_name": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["series_name", "items"]}
        }}


class ReadProcessedSeries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("series_name")
        start = kwargs.get("start")
        end = kwargs.get("end")
        rows = []
        for r in data.get("processed_timeseries", []) or []:
            if name and r.get("series_name") != name:
                continue
            ts = r.get("timestamp", "")
            if start and ts < start:
                continue
            if end and ts > end:
                continue
            rows.append(r)
        return json.dumps({"series_name": name, "rows": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_processed_series",
            "description": "Read processed series rows by name and optional range.",
            "parameters": {"type": "object", "properties": {
                "series_name": {"type": "string"},
                "start": {"type": "string"},
                "end": {"type": "string"}
            }, "required": ["series_name"]}
        }}


# ---------------- Feature registry ----------------

class RegisterFeatureBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "feature_set_name": kwargs.get("feature_set_name"),
            "version": kwargs.get("version"),
            "columns": kwargs.get("columns"),
            "created_at": _now_iso_fixed(),
        }
        feats.append(row)
        return json.dumps({"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "register_feature_bundle",
            "description": "Create a feature-set descriptor record.",
            "parameters": {"type": "object", "properties": {
                "feature_set_name": {"type": "string"},
                "version": {"type": "string"},
                "columns": {"type": "array", "items": {"type": "string"}}
            }, "required": ["feature_set_name", "version", "columns"]}
        }}


class ReadFeatureBundle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feats = data.get("features", []) or []
        fid = kwargs.get("feature_set_id")
        fname = kwargs.get("feature_set_name")
        row = None
        if fid is not None:
            row = next((f for f in feats if str(f.get("feature_set_id")) == str(fid)), None)
        elif fname:
            row = next((f for f in feats if f.get("feature_set_name") == fname), None)
        return json.dumps(row or {"error": "Feature set not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_feature_bundle",
            "description": "Fetch a feature-set by id or by name.",
            "parameters": {"type": "object", "properties": {
                "feature_set_id": {"type": "string"},
                "feature_set_name": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Model registry + configs ----------------

class StoreModelArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "model_name": kwargs.get("model_name"),
            "model_type": kwargs.get("model_type"),
            "framework": kwargs.get("framework"),
            "version": kwargs.get("version"),
            "status": kwargs.get("status"),
            "created_at": _now_iso_fixed(),
            "updated_at": _now_iso_fixed(),
        }
        models.append(row)
        return json.dumps({"model_id": new_id, "model_name": row["model_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_model_artifact",
            "description": "Register a model in the registry.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "model_type": {"type": "string"},
                "framework": {"type": "string"},
                "version": {"type": "string"},
                "status": {"type": "string"}
            }, "required": ["model_name", "model_type", "framework", "version", "status"]}
        }}


class FetchModelRecord(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        models = data.get("models", []) or []
        mid = kwargs.get("model_id")
        mname = kwargs.get("model_name")
        row = None
        if mid is not None:
            row = next((m for m in models if str(m.get("model_id")) == str(mid)), None)
        elif mname:
            row = next((m for m in models if m.get("model_name") == mname), None)
        return json.dumps(row or {"error": "Model not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_model_record",
            "description": "Read a model by id or by name.",
            "parameters": {"type": "object", "properties": {
                "model_id": {"type": "string"},
                "model_name": {"type": "string"}
            }, "required": []}
        }}


class UpsertModelProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = data.get("model_config", [])
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        params = kwargs.get("params") or {}
        row = next((c for c in cfgs if c.get("model_name") == model_name and c.get("config_name") == config_name), None)
        if row:
            row["params"] = params
            row["updated_at"] = _now_iso_fixed()
            out = {"model_name": model_name, "config_name": config_name, "action": "updated"}
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
                "created_at": _now_iso_fixed(),
            }
            cfgs.append(row)
            out = {"config_id": new_id, "model_name": model_name, "config_name": config_name, "action": "inserted"}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "upsert_model_profile",
            "description": "Insert or update a named configuration for a model.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "config_name": {"type": "string"},
                "params": {"type": "object"}
            }, "required": ["model_name", "config_name", "params"]}
        }}


class ReadModelProfiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = data.get("model_config", []) or []
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        rows = [
            c for c in cfgs
            if (not model_name or c.get("model_name") == model_name)
               and (not config_name or c.get("config_name") == config_name)
        ]
        return json.dumps({"configs": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_model_profiles",
            "description": "List model configs (filtered by model and/or config name).",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "config_name": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Metrics ----------------

class LogModelMetric(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "model_name": kwargs.get("model_name"),
            "metric_name": kwargs.get("metric_name"),
            "value": kwargs.get("value"),
            "dataset_split": kwargs.get("dataset_split"),
            "timestamp": _now_iso_fixed(),
        }
        metrics.append(row)
        return json.dumps({"metric_id": new_id, "model_name": row["model_name"], "metric_name": row["metric_name"]},
                          indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_model_metric",
            "description": "Insert a metric row for a model+split.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "metric_name": {"type": "string"},
                "value": {"type": "number"},
                "dataset_split": {"type": "string"}
            }, "required": ["model_name", "metric_name", "value", "dataset_split"]}
        }}


class ReadModelMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        metrics = data.get("metrics", []) or []
        model_name = kwargs.get("model_name")
        metric_name = kwargs.get("metric_name")
        dataset_split = kwargs.get("dataset_split")
        rows = [
            m for m in metrics
            if (not model_name or m.get("model_name") == model_name)
               and (not metric_name or m.get("metric_name") == metric_name)
               and (not dataset_split or m.get("dataset_split") == dataset_split)
        ]
        return json.dumps({"metrics": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_model_metrics",
            "description": "Read metrics filtered by model/metric/split.",
            "parameters": {"type": "object", "properties": {
                "model_name": {"type": "string"},
                "metric_name": {"type": "string"},
                "dataset_split": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Predictions ----------------

class WritePredictionLot(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "batch_name": kwargs.get("batch_name"),
            "model_name": kwargs.get("model_name"),
            "items": kwargs.get("items") or [],
            "created_at": _now_iso_fixed(),
        }
        preds.append(row)
        return json.dumps({"prediction_id": new_id, "batch_name": row["batch_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "write_prediction_lot",
            "description": "Insert a named prediction batch for a model.",
            "parameters": {"type": "object", "properties": {
                "batch_name": {"type": "string"},
                "model_name": {"type": "string"},
                "items": {"type": "array", "items": {"type": "object"}}
            }, "required": ["batch_name", "model_name", "items"]}
        }}


class ReadPredictionLots(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        preds = data.get("predictions", []) or []
        batch_name = kwargs.get("batch_name")
        model_name = kwargs.get("model_name")
        rows = [
            p for p in preds
            if (not batch_name or p.get("batch_name") == batch_name)
               and (not model_name or p.get("model_name") == model_name)
        ]
        return json.dumps({"predictions": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_prediction_lots",
            "description": "Read prediction batches (filter by batch or model).",
            "parameters": {"type": "object", "properties": {
                "batch_name": {"type": "string"},
                "model_name": {"type": "string"}
            }, "required": []}
        }}


# ---------------- QC artifacts ----------------

class RenderQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("figure_label")
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        return json.dumps({"figure_path": pdf_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "render_qc_report",
            "description": "Return deterministic PDF path for a QC report.",
            "parameters": {"type": "object", "properties": {"figure_label": {"type": "string"}},
                           "required": ["figure_label"]}
        }}


class RecordQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "figure_label": kwargs.get("figure_label"),
            "figure_path": kwargs.get("figure_path"),
            "artifact_type": kwargs.get("artifact_type"),
            "related_model_name": kwargs.get("related_model_name"),
            "created_at": _now_iso_fixed(),
        }
        figs.append(row)
        return json.dumps({"figure_id": new_id, "figure_label": row["figure_label"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "record_qc_report",
            "description": "Insert a QC report metadata row.",
            "parameters": {"type": "object", "properties": {
                "figure_label": {"type": "string"},
                "figure_path": {"type": "string"},
                "artifact_type": {"type": "string"},
                "related_model_name": {"type": ["string", "null"]}
            }, "required": ["figure_label", "figure_path", "artifact_type"]}
        }}


class ReadQcReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        figs = data.get("qc_figures", []) or []
        fid = kwargs.get("figure_id")
        label = kwargs.get("figure_label")
        row = None
        if fid is not None:
            row = next((f for f in figs if str(f.get("figure_id")) == str(fid)), None)
        elif label:
            row = next((f for f in figs if f.get("figure_label") == label), None)
        return json.dumps(row or {"error": "QC figure not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_qc_report",
            "description": "Read QC report metadata by id or label.",
            "parameters": {"type": "object", "properties": {
                "figure_id": {"type": "string"},
                "figure_label": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Stakeholder artifacts ----------------

class RecordStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "output_label": kwargs.get("output_label"),
            "audience": kwargs.get("audience"),
            "artifact_path": kwargs.get("artifact_path"),
            "created_at": _now_iso_fixed(),
        }
        outs.append(row)
        return json.dumps({"output_id": new_id, "output_label": row["output_label"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "record_stakeholder_artifact",
            "description": "Insert a stakeholder-visible artifact row.",
            "parameters": {"type": "object", "properties": {
                "output_label": {"type": "string"},
                "audience": {"type": "string"},
                "artifact_path": {"type": "string"}
            }, "required": ["output_label", "audience", "artifact_path"]}
        }}


class ReadStakeholderArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outs = data.get("stakeholder_outputs", []) or []
        oid = kwargs.get("output_id")
        label = kwargs.get("output_label")
        row = None
        if oid is not None:
            row = next((o for o in outs if str(o.get("output_id")) == str(oid)), None)
        elif label:
            row = next((o for o in outs if o.get("output_label") == label), None)
        return json.dumps(row or {"error": "Stakeholder output not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_stakeholder_artifact",
            "description": "Fetch a stakeholder artifact row by id or label.",
            "parameters": {"type": "object", "properties": {
                "output_id": {"type": "string"},
                "output_label": {"type": "string"}
            }, "required": []}
        }}


# ---------------- Email / Audit log ----------------

class DispatchResultsMail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "to": kwargs.get("to_address"),
            "subject": kwargs.get("subject"),
            "body_text": kwargs.get("body_text"),
            "attachment": kwargs.get("attachment"),
            "model_name": kwargs.get("model_name"),
            "batch_name": kwargs.get("batch_name"),
            "sent_at": _now_iso_fixed(),
        }
        inbox.append(row)
        return json.dumps({"status": "sent", "message_id": new_id, "to": row["to"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "dispatch_results_mail",
            "description": "Send a results email with a single attachment.",
            "parameters": {"type": "object", "properties": {
                "to_address": {"type": "string"},
                "subject": {"type": "string"},
                "body_text": {"type": "string"},
                "attachment": {"type": "string"},
                "model_name": {"type": "string"},
                "batch_name": {"type": "string"}
            }, "required": ["to_address", "subject", "body_text", "attachment"]}
        }}


class AppendAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "event_type": kwargs.get("event_type"),
            "message": kwargs.get("message"),
            "created_at": _now_iso_fixed(),
        }
        logs.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_audit_event",
            "description": "Append an audit/terminal log entry.",
            "parameters": {"type": "object", "properties": {
                "event_type": {"type": "string"},
                "message": {"type": "string"}
            }, "required": ["event_type", "message"]}
        }}


class ReadAuditEvents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get("terminal_log", []) or []
        event_type = kwargs.get("event_type")
        rows = [l for l in logs if (not event_type or l.get("event_type") == event_type)]
        return json.dumps({"logs": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_audit_events",
            "description": "List audit/terminal log entries (filter by event).",
            "parameters": {"type": "object", "properties": {
                "event_type": {"type": "string"}
            }, "required": []}
        }}


class LogEtlExecution(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
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
            "run_name": kwargs.get("run_name"),
            "task": kwargs.get("task"),
            "status": kwargs.get("status"),
            "rows_processed": kwargs.get("rows_processed"),
            "started_at": _now_iso_fixed(),
            "finished_at": _now_iso_fixed(),
        }
        runs.append(row)
        return json.dumps({"run_id": new_id, "run_name": row["run_name"]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "log_etl_execution",
            "description": "Record an ETL execution row.",
            "parameters": {"type": "object", "properties": {
                "run_name": {"type": "string"},
                "task": {"type": "string"},
                "status": {"type": "string"},
                "rows_processed": {"type": ["integer", "null"]}
            }, "required": ["run_name", "task", "status"]}
        }}


class FetchEtlExecution(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("etl_runs", []) or []
        rid = kwargs.get("run_id")
        rname = kwargs.get("run_name")
        row = None
        if rid is not None:
            row = next((r for r in runs if str(r.get("run_id")) == str(rid)), None)
        elif rname:
            row = next((r for r in runs if r.get("run_name") == rname), None)
        return json.dumps(row or {"error": "ETL run not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "fetch_etl_execution",
            "description": "Read an ETL execution by id or run_name.",
            "parameters": {"type": "object", "properties": {
                "run_id": {"type": "string"},
                "run_name": {"type": "string"}
            }, "required": []}
        }}


TOOLS = [
    # Project & env
    ReadRuntimeEnv(),
    PatchRuntimeEnv(),
    ReadProjectSettings(),
    PatchProjectSettings(),

    # Files
    BrowseFileIndex(),
    RegisterFileEntry(),
    RetrieveFileEntry(),

    # NOAA / Weather
    ReadNoaaStationSearches(),
    ReadWeatherForecast(),
    QueryWaterLevels(),

    # Processed series
    WriteProcessedSeries(),
    ReadProcessedSeries(),

    # Features
    RegisterFeatureBundle(),
    ReadFeatureBundle(),

    # Models & configs
    StoreModelArtifact(),
    FetchModelRecord(),
    UpsertModelProfile(),
    ReadModelProfiles(),

    # Metrics
    LogModelMetric(),
    ReadModelMetrics(),

    # Predictions
    WritePredictionLot(),
    ReadPredictionLots(),

    # QC
    RenderQcReport(),
    RecordQcReport(),
    ReadQcReport(),

    # Stakeholder
    RecordStakeholderArtifact(),
    ReadStakeholderArtifact(),

    # Email & audit
    DispatchResultsMail(),
    AppendAuditEvent(),
    ReadAuditEvents(),

    # ETL
    LogEtlExecution(),
    FetchEtlExecution(),
]
