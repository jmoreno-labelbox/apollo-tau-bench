# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _ymd(iso_ts: str) -> str:
    # '2024-08-23T10:00:00Z' -> '2024-08-23'
    return (iso_ts or "").split("T")[0]

def _table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    tbl = data.get(name)
    if not isinstance(tbl, list):
        tbl = []
        data[name] = tbl
    return tbl

def _id_from_request(prefix: str, request_id: str) -> str:
    rid = (request_id or "").strip()
    if not rid:
        return None
    return f"{prefix}_{rid}"

def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

class record_automation_run(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], task_name: str, status: str, started_at: str, ended_at: str, timestamp: str, request_id: str) -> str:
        runs = _table(data, "automation_runs")
        run_id = _id_from_request("run", request_id)
        if run_id:
            for r in runs:
                if isinstance(r, dict) and r.get("run_id") == run_id:
                    return json.dumps(r, indent=2)
        row = {
            "run_id": run_id or _get_next_id("run", [r.get("run_id", "") for r in runs if isinstance(r, dict)]),
            "task_name": task_name,
            "status": status,
            "started_at": started_at,
            "ended_at": ended_at,
            "day": _ymd(timestamp),
        }
        runs.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"record_automation_run","description":"Record/reuse a deterministic automation run row (run_<request_id>).","parameters":{"type":"object","properties":{"task_name":{"type":"string"},"status":{"type":"string"},"started_at":{"type":"string"},"ended_at":{"type":"string"},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["task_name","status","started_at","ended_at","timestamp","request_id"]}}}