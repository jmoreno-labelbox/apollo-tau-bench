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

class governance_update(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id: str, add_tags: List[str], remove_tags: List[str], timestamp: str, request_id: str) -> str:
        tbl = _table(data, "artifact_tags")
        day = _ymd(timestamp)
        row = next((r for r in tbl if isinstance(r, dict) and r.get("artifact_id") == artifact_id and r.get("day") == day), None)
        if not row:
            row = {"artifact_id": artifact_id, "day": day, "tags": []}
            tbl.append(row)
        current = set(row.get("tags", []))
        current |= set(add_tags or [])
        current -= set(remove_tags or [])
        row["tags"] = sorted(current)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"governance_update","description":"Apply deterministic tag updates for an artifact on the instruction day.","parameters":{"type":"object","properties":{"artifact_id":{"type":"string"},"add_tags":{"type":"array","items":{"type":"string"}},"remove_tags":{"type":"array","items":{"type":"string"}},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["artifact_id","add_tags","remove_tags","timestamp","request_id"]}}}