# Sierra Copyright

import re
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

_ISO8601Z = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)

def _require_write(p: Dict[str, Any]):
    miss = _require(p, ["timestamp", "request_id"])
    if miss:
        return miss
    ts = p.get("timestamp")
    if not isinstance(ts, str) or not _ISO8601Z.match(ts):
        return _err("invalid_timestamp_format")
    rid = p.get("request_id")
    if not isinstance(rid, str) or not rid:
        return _err("invalid_request_id")
    return None

def _require(p: Dict[str, Any], req: List[str]):
    missing = [k for k in req if p.get(k) in (None, "")]
    if missing:
        return _err("missing_params", {"missing": missing})
    return None

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _err(code, extra=None):
    payload = {"error": code}
    if isinstance(extra, dict):
        payload.update(extra)
    return _j(payload)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class create_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)

        # mandatory fields
        miss = _require(p, ["cycle_id","artifact_id","started_at","timestamp","request_id"])
        if miss: return miss
        w = _require_write(p)
        if w: return w

        # ID_RULE: review_cycle_id — rev-<artifact_id>-<YYYYMMDD>-<sequence_number>
        m = re.match(r"^rev-(?P<art>[^-]+)-(?P<date>\d{8})-(?P<seq>\d+)$", p["cycle_id"])
        if not m:
            return _err("invalid_cycle_id_format")

        art_from_id = m.group("art")
        date_from_id = m.group("date")
        ts_date = p["timestamp"][0:10].replace("-", "")

        if art_from_id != p["artifact_id"]:
            return _err("cycle_id_artifact_mismatch")
        if date_from_id != ts_date:
            return _err("cycle_id_date_mismatch")

        # predictable output; no thread associated during initialization
        c= {
            "cycle_id": p["cycle_id"],
            "artifact_id": p["artifact_id"],
            "status": "IN_FLIGHT",
            "started_at": p["started_at"],
            "created_ts": p["timestamp"],
            "thread_id_nullable": None,
        }
        _ensure(data, "review_cycles", []).append(c)
        return _ok(c)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_review_cycle",
            "description":"Create a review cycle with deterministic ID validation per ID_RULE.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "artifact_id":{"type":"string"},
                "started_at":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"},
            },"required":["cycle_id","artifact_id","started_at","timestamp","request_id"]}
        }}