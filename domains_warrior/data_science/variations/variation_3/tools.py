from typing import Dict, Any, List, Optional
from domains.dto import Tool, Task, Action
import json
from datetime import datetime

def _fixed_now_iso() -> str:
    return "2025-08-20T00:00:00Z"

def _index_by(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in items or []}

class FetchProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfg = data.get("project_config", {}) or {}
        key = kwargs.get("key")
        if key:
            return json.dumps({key: cfg.get(key)}, indent=2)
        return json.dumps(cfg, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_project_config",
            "description":"Fetch project configuration (optionally a single key).",
            "parameters":{"type":"object","properties":{"key":{"type":"string"}},"required":[]}
        }}

class ModifyProjectConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        cfg = data.get("project_config", {})
        if cfg is None or isinstance(cfg, list):
            cfg = {}
            data["project_config"] = cfg
        cfg.update(updates)
        cfg["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_project_config",
            "description":"Update project configuration with provided key/value pairs.",
            "parameters":{"type":"object","properties":{"updates":{"type":"object"}},"required":["updates"]}
        }}

class FetchEnvironment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        env = data.get("environment", {}) or {}
        return json.dumps(env, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_environment",
            "description":"Read environment variables/secrets map.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}

class ModifyEnvironment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        env = data.get("environment", {})
        if env is None or isinstance(env, list):
            env = {}
            data["environment"] = env
        env.update(updates)
        env["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated": updates}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_environment",
            "description":"Update environment variables/secrets.",
            "parameters":{"type":"object","properties":{"updates":{"type":"object"}},"required":["updates"]}
        }}

class BrowseFileStore(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"files": data.get("file_store", [])}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_file_store",
            "description":"List all files in the file store.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}

class AddFile(Tool):
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
            "created_at": _fixed_now_iso()
        }
        files.append(row)
        return json.dumps({"file_id": new_id, "path": row["path"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"insert_file",
            "description":"Insert a file metadata row into the file store.",
            "parameters":{"type":"object","properties":{
                "path":{"type":"string"},
                "mime_type":{"type":"string"},
                "size":{"type":["integer","null"]}
            },"required":["path","mime_type"]}
        }}

class RetrieveFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        files = data.get("file_store", []) or []
        fid = kwargs.get("file_id")
        path = kwargs.get("path")
        row = None
        if fid is not None:
            row = next((f for f in files if str(f.get("file_id")) == str(fid)), None)
        elif path:
            row = next((f for f in files if f.get("path")==path), None)
        return json.dumps(row or {"error":"File not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_file",
            "description":"Read a file store record by id or by path.",
            "parameters":{"type":"object","properties":{
                "file_id":{"type":"string"},"path":{"type":"string"}
            },"required":[]}
        }}

class LogETLRun(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("etl_runs", [])
        max_id = 0
        for r in runs:
            try:
                rid = int(r.get("run_id", 0))
                if rid > max_id: max_id = rid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "run_id": new_id,
            "run_name": kwargs.get("run_name"),
            "task": kwargs.get("task"),
            "status": kwargs.get("status"),
            "rows_processed": kwargs.get("rows_processed"),
            "started_at": _fixed_now_iso(),
            "finished_at": _fixed_now_iso()
        }
        runs.append(row)
        return json.dumps({"run_id": new_id, "run_name": row["run_name"]}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"register_etl_run",
            "description":"Insert a new ETL run record.",
            "parameters":{"type":"object","properties":{
                "run_name":{"type":"string"},
                "task":{"type":"string"},
                "status":{"type":"string"},
                "rows_processed":{"type":["integer","null"]}
            },"required":["run_name","task","status"]}
        }}

class FetchETLRunDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        runs = data.get("etl_runs", []) or []
        rid = kwargs.get("run_id")
        rname = kwargs.get("run_name")
        row = None
        if rid is not None:
            row = next((r for r in runs if str(r.get("run_id"))==str(rid)), None)
        elif rname:
            row = next((r for r in runs if r.get("run_name")==rname), None)
        return json.dumps(row or {"error":"ETL run not found"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_etl_run_details",
            "description":"Read an ETL run by id or by run_name.",
            "parameters":{"type":"object","properties":{
                "run_id":{"type":"string"},"run_name":{"type":"string"}
            },"required":[]}
        }}

class RetrieveWaterLevels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        station = kwargs.get("station_id")
        start = kwargs.get("start")
        end = kwargs.get("end")
        rows = []
        for r in data.get("water_levels", []) or []:
            if station and r.get("station_id") != station:
                continue
            ts = r.get("timestamp","")
            if start and ts < start: continue
            if end and ts > end: continue
            rows.append(r)
        return json.dumps({"rows": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"fetch_water_levels",
            "description":"Fetch water level rows (optional station/time filters).",
            "parameters":{"type":"object","properties":{
                "station_id":{"type":"string"},
                "start":{"type":"string"},"end":{"type":"string"}
            },"required":[]}
        }}

class StoreProcessedTimeseries(Tool):
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
                if rid > max_id: max_id = rid
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
                "source": it.get("source")
            }
            table.append(row)
            inserted.append(rid)
        return json.dumps({"series_name": series_name, "inserted_row_ids": inserted}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_processed_timeseries",
            "description":"Insert processed timeseries points for a named series.",
            "parameters":{"type":"object","properties":{
                "series_name":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["series_name","items"]}
        }}

class FetchProcessedTimeseries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("series_name")
        start = kwargs.get("start")
        end = kwargs.get("end")
        rows = []
        for r in data.get("processed_timeseries", []) or []:
            if name and r.get("series_name") != name:
                continue
            ts = r.get("timestamp","")
            if start and ts < start: continue
            if end and ts > end: continue
            rows.append(r)
        return json.dumps({"series_name": name, "rows": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_processed_timeseries",
            "description":"Read processed timeseries rows by series_name and optional time range.",
            "parameters":{"type":"object","properties":{
                "series_name":{"type":"string"},
                "start":{"type":"string"},"end":{"type":"string"}
            },"required":["series_name"]}
        }}

class AddFeatureSet(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feats = data.get("features", [])
        max_id = 0
        for f in feats:
            try:
                fid = int(f.get("feature_set_id", 0))
                if fid > max_id: max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "feature_set_id": new_id,
            "feature_set_name": kwargs.get("feature_set_name"),
            "version": kwargs.get("version"),
            "columns": kwargs.get("columns"),
            "created_at": _fixed_now_iso()
        }
        feats.append(row)
        return json.dumps({"feature_set_id": new_id, "feature_set_name": row["feature_set_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_feature_set",
            "description":"Insert a new feature set descriptor.",
            "parameters":{"type":"object","properties":{
                "feature_set_name":{"type":"string"},
                "version":{"type":"string"},
                "columns":{"type":"array","items":{"type":"string"}}
            },"required":["feature_set_name","version","columns"]}
        }}

class FetchFeatureSetDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        feats = data.get("features", []) or []
        fid = kwargs.get("feature_set_id")
        fname = kwargs.get("feature_set_name")
        row = None
        if fid is not None:
            row = next((f for f in feats if str(f.get("feature_set_id"))==str(fid)), None)
        elif fname:
            row = next((f for f in feats if f.get("feature_set_name")==fname), None)
        return json.dumps(row or {"error":"Feature set not found"}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_feature_set_details",
            "description":"Read a feature set by id or by name.",
            "parameters":{"type":"object","properties":{
                "feature_set_id":{"type":"string"},"feature_set_name":{"type":"string"}
            },"required":[]}
        }}

class AddModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        models = data.get("models", [])
        max_id = 0
        for m in models:
            try:
                mid = int(m.get("model_id", 0))
                if mid > max_id: max_id = mid
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
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso()
        }
        models.append(row)
        return json.dumps({"model_id": new_id, "model_name": row["model_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_model",
            "description":"Register a model in the model registry.",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "model_type":{"type":"string"},
                "framework":{"type":"string"},
                "version":{"type":"string"},
                "status":{"type":"string"}
            },"required":["model_name","model_type","framework","version","status"]}
        }}

class FetchModelDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        models = data.get("models", []) or []
        mid = kwargs.get("model_id")
        mname = kwargs.get("model_name")
        row = None
        if mid is not None:
            row = next((m for m in models if str(m.get("model_id"))==str(mid)), None)
        elif mname:
            row = next((m for m in models if m.get("model_name")==mname), None)
        return json.dumps(row or {"error":"Model not found"}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_model_details",
            "description":"Read a model by id or by model_name.",
            "parameters":{"type":"object","properties":{
                "model_id":{"type":"string"},"model_name":{"type":"string"}
            },"required":[]}
        }}

class SaveModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = data.get("model_config", [])
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        params = kwargs.get("params") or {}
        row = next((c for c in cfgs if c.get("model_name")==model_name and c.get("config_name")==config_name), None)
        if row:
            row["params"] = params
            row["updated_at"] = _fixed_now_iso()
            out = {"model_name": model_name, "config_name": config_name, "action":"updated"}
        else:
            max_id = 0
            for c in cfgs:
                try:
                    cid = int(c.get("config_id", 0))
                    if cid > max_id: max_id = cid
                except (ValueError, TypeError):
                    continue
            new_id = max_id + 1
            row = {"config_id": new_id, "model_name": model_name, "config_name": config_name, "params": params, "created_at": _fixed_now_iso()}
            cfgs.append(row)
            out = {"config_id": new_id, "model_name": model_name, "config_name": config_name, "action":"inserted"}
        return json.dumps(out, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"upsert_model_config",
            "description":"Insert or update a model configuration by (model_name, config_name).",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "config_name":{"type":"string"},
                "params":{"type":"object"}
            },"required":["model_name","config_name","params"]}
        }}

class FetchModelConfig(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cfgs = data.get("model_config", []) or []
        model_name = kwargs.get("model_name")
        config_name = kwargs.get("config_name")
        rows = [c for c in cfgs if (not model_name or c.get("model_name")==model_name) and (not config_name or c.get("config_name")==config_name)]
        return json.dumps({"configs": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_model_config",
            "description":"List model configs (optionally filtered by model_name and/or config_name).",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},"config_name":{"type":"string"}
            },"required":[]}
        }}

class LogMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        metrics = data.get("metrics", [])
        max_id = 0
        for m in metrics:
            try:
                mid = int(m.get("metric_id", 0))
                if mid > max_id: max_id = mid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "metric_id": new_id,
            "model_name": kwargs.get("model_name"),
            "metric_name": kwargs.get("metric_name"),
            "value": kwargs.get("value"),
            "dataset_split": kwargs.get("dataset_split"),
            "timestamp": _fixed_now_iso()
        }
        metrics.append(row)
        return json.dumps({"metric_id": new_id, "model_name": row["model_name"], "metric_name": row["metric_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_metrics",
            "description":"Insert a metrics row for a model and split.",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "metric_name":{"type":"string"},
                "value":{"type":"number"},
                "dataset_split":{"type":"string"}
            },"required":["model_name","metric_name","value","dataset_split"]}
        }}

class RetrieveMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        metrics = data.get("metrics", []) or []
        model_name = kwargs.get("model_name")
        metric_name = kwargs.get("metric_name")
        dataset_split = kwargs.get("dataset_split")
        rows = [m for m in metrics if (not model_name or m.get("model_name")==model_name)
                and (not metric_name or m.get("metric_name")==metric_name)
                and (not dataset_split or m.get("dataset_split")==dataset_split)]
        return json.dumps({"metrics": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_metrics",
            "description":"List metrics (filter by model_name, metric_name, dataset_split).",
            "parameters":{"type":"object","properties":{
                "model_name":{"type":"string"},
                "metric_name":{"type":"string"},
                "dataset_split":{"type":"string"}
            },"required":[]}
        }}

class AddPredictionBatch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        preds = data.get("predictions", [])
        max_id = 0
        for p in preds:
            try:
                pid = int(p.get("prediction_id", 0))
                if pid > max_id: max_id = pid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "prediction_id": new_id,
            "batch_name": kwargs.get("batch_name"),
            "model_name": kwargs.get("model_name"),
            "items": kwargs.get("items") or [],
            "created_at": _fixed_now_iso()
        }
        preds.append(row)
        return json.dumps({"prediction_id": new_id, "batch_name": row["batch_name"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_prediction_batch",
            "description":"Insert a batch of predictions for a model.",
            "parameters":{"type":"object","properties":{
                "batch_name":{"type":"string"},
                "model_name":{"type":"string"},
                "items":{"type":"array","items":{"type":"object"}}
            },"required":["batch_name","model_name","items"]}
        }}

class RetrievePredictions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        preds = data.get("predictions", []) or []
        batch_name = kwargs.get("batch_name")
        model_name = kwargs.get("model_name")
        rows = [p for p in preds if (not batch_name or p.get("batch_name")==batch_name)
                and (not model_name or p.get("model_name")==model_name)]
        return json.dumps({"predictions": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_predictions",
            "description":"Read prediction batches (filter by batch_name and/or model_name).",
            "parameters":{"type":"object","properties":{
                "batch_name":{"type":"string"},
                "model_name":{"type":"string"}
            },"required":[]}
        }}

class GenerateQCFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        label = kwargs.get("figure_label")
        pdf_path = f"https://storage.example.com/reports/{label}.pdf"
        return json.dumps({"figure_path": pdf_path}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"export_qc_figure",
            "description":"Export a QC figure/report and return its deterministic pdf path.",
            "parameters":{"type":"object","properties":{"figure_label":{"type":"string"}},"required":["figure_label"]}
        }}

class StoreQCFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        figs = data.get("qc_figures", [])
        max_id = 0
        for f in figs:
            try:
                fid = int(f.get("figure_id", 0))
                if fid > max_id: max_id = fid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "figure_id": new_id,
            "figure_label": kwargs.get("figure_label"),
            "figure_path": kwargs.get("figure_path"),
            "artifact_type": kwargs.get("artifact_type"),
            "related_model_name": kwargs.get("related_model_name"),
            "created_at": _fixed_now_iso()
        }
        figs.append(row)
        return json.dumps({"figure_id": new_id, "figure_label": row["figure_label"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_qc_figure",
            "description":"Insert a QC figure record.",
            "parameters":{"type":"object","properties":{
                "figure_label":{"type":"string"},
                "figure_path":{"type":"string"},
                "artifact_type":{"type":"string"},
                "related_model_name":{"type":["string","null"]}
            },"required":["figure_label","figure_path","artifact_type"]}
        }}

class FetchQCFigure(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        figs = data.get("qc_figures", []) or []
        fid = kwargs.get("figure_id")
        label = kwargs.get("figure_label")
        row = None
        if fid is not None:
            row = next((f for f in figs if str(f.get("figure_id"))==str(fid)), None)
        elif label:
            row = next((f for f in figs if f.get("figure_label")==label), None)
        return json.dumps(row or {"error":"QC figure not found"}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_qc_figure",
            "description":"Read a QC figure by id or label.",
            "parameters":{"type":"object","properties":{
                "figure_id":{"type":"string"},"figure_label":{"type":"string"}
            },"required":[]}
        }}

class SaveStakeholderOutput(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outs = data.get("stakeholder_outputs", [])
        max_id = 0
        for o in outs:
            try:
                oid = int(o.get("output_id", 0))
                if oid > max_id: max_id = oid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "output_id": new_id,
            "output_label": kwargs.get("output_label"),
            "audience": kwargs.get("audience"),
            "artifact_path": kwargs.get("artifact_path"),
            "created_at": _fixed_now_iso()
        }
        outs.append(row)
        return json.dumps({"output_id": new_id, "output_label": row["output_label"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"insert_stakeholder_output",
            "description":"Insert a stakeholder output record pointing to an artifact path.",
            "parameters":{"type":"object","properties":{
                "output_label":{"type":"string"},
                "audience":{"type":"string"},
                "artifact_path":{"type":"string"}
            },"required":["output_label","audience","artifact_path"]}
        }}

class FetchStakeholderOutput(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        outs = data.get("stakeholder_outputs", []) or []
        oid = kwargs.get("output_id")
        label = kwargs.get("output_label")
        row = None
        if oid is not None:
            row = next((o for o in outs if str(o.get("output_id"))==str(oid)), None)
        elif label:
            row = next((o for o in outs if o.get("output_label")==label), None)
        return json.dumps(row or {"error":"Stakeholder output not found"}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_stakeholder_output",
            "description":"Read a stakeholder output by id or label.",
            "parameters":{"type":"object","properties":{
                "output_id":{"type":"string"},"output_label":{"type":"string"}
            },"required":[]}
        }}

class DispatchResultsEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inbox = data.get("gmail_messages", [])
        max_id = 0
        for m in inbox:
            try:
                mid = int(m.get("message_id", 0))
                if mid > max_id: max_id = mid
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
            "sent_at": _fixed_now_iso()
        }
        inbox.append(row)
        return json.dumps({"status":"sent","message_id": new_id, "to": row["to"]}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"send_results_email",
            "description":"Send a results email with an attachment (deterministic parameters only).",
            "parameters":{"type":"object","properties":{
                "to_address":{"type":"string"},
                "subject":{"type":"string"},
                "body_text":{"type":"string"},
                "attachment":{"type":"string"},
                "model_name":{"type":"string"},
                "batch_name":{"type":"string"}
            },"required":["to_address","subject","body_text","attachment"]}
        }}

class WriteTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get("terminal_log", [])
        max_id = 0
        for l in logs:
            try:
                lid = int(l.get("log_id", 0))
                if lid > max_id: max_id = lid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "log_id": new_id,
            "event_type": kwargs.get("event_type"),
            "message": kwargs.get("message"),
            "created_at": _fixed_now_iso()
        }
        logs.append(row)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"record_terminal_log",
            "description":"Append a terminal log entry.",
            "parameters":{"type":"object","properties":{
                "event_type":{"type":"string"},
                "message":{"type":"string"}
            },"required":["event_type","message"]}
        }}

class BrowseTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get("terminal_log", []) or []
        event_type = kwargs.get("event_type")
        rows = [l for l in logs if (not event_type or l.get("event_type")==event_type)]
        return json.dumps({"logs": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_terminal_log",
            "description":"List terminal log entries (optionally filter by event_type).",
            "parameters":{"type":"object","properties":{"event_type":{"type":"string"}},"required":[]}
        }}

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
    BrowseTerminalLog()
]
