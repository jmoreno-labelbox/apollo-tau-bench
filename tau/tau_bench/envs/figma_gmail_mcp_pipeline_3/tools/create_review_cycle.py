# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_review_cycle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)

        # required fields
        miss = _require(p, ["cycle_id","artifact_id","started_at","timestamp","request_id"])
        if miss: return miss
        w = _require_write(p)
        if w: return w

        # ID_RULE: review_cycle_id — rev-<artifact_id>-<YYYYMMDD>-<seq>
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

        # deterministic output; no thread attached at creation time
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
