# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool












def _safe_table(data: Dict[str, Any], table: str) -> List[Dict[str, Any]]:
    """Get or create a list table."""
    return data.setdefault(table, [])

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _index_by(table: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    """Build index map from key -> row_index (first occurrence)."""
    idx = {}
    for i, r in enumerate(table):
        k = r.get(key)
        if isinstance(k, str) and k not in idx:
            idx[k] = i
    return idx

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

def _det_id(prefix: str, parts: List[str], length: int = 8) -> str:
    """
    Deterministic ID from input parts. Stable across runs.
    """
    m = hashlib.md5()
    m.update(("|".join(parts)).encode("utf-8"))
    return f"{prefix}_{m.hexdigest()[:length]}"

class StartReviewCycleTool(Tool):
    """Create or upsert a review cycle for an artifact (deterministic cycle_id from inputs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, created_ts, status) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        created_ts = _require_str(created_ts, "created_ts")
        status = status or "IN_FLIGHT"
        if not (artifact_id and created_ts):
            return json.dumps({"error":"artifact_id and created_ts required"})

        cycle_id = _det_id("cycle", [artifact_id, created_ts, status])
        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        row = {
            "cycle_id": cycle_id,
            "artifact_id": artifact_id,
            "status": status,
            "created_ts": created_ts,
            "last_updated": created_ts,
            "thread_id_nullable": None,
            "sla_hours": _get_config_json(data, "sla_deadlines").get("design_review", 72)
        }
        if cycle_id in idx:
            # maintain current thread connection
            existing = cycles[idx[cycle_id]]
            row["thread_id_nullable"] = existing.get("thread_id_nullable")
            cycles[idx[cycle_id]] = row
        else:
            cycles.append(row)

        return json.dumps({"success": True, "cycle_id": cycle_id, "status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"start_review_cycle",
            "description":"Create/update a review cycle for an artifact (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "created_ts":{"type":"string"},
                "status":{"type":"string","description":"Default IN_FLIGHT."}
            },"required":["artifact_id","created_ts"]}
        }}