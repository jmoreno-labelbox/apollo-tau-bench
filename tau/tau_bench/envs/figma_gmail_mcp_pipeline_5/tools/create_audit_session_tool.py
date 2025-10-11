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

def _det_id(prefix: str, parts: List[str], length: int = 8) -> str:
    """
    Deterministic ID from input parts. Stable across runs.
    """
    m = hashlib.md5()
    m.update(("|".join(parts)).encode("utf-8"))
    return f"{prefix}_{m.hexdigest()[:length]}"

class CreateAuditSessionTool(Tool):
    """Create/upsert an audit session for an artifact (deterministic audit_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, audit_type, created_ts) -> str:
        artifact_id = _require_str(artifact_id, "artifact_id")
        created_ts = _require_str(created_ts, "created_ts")
        audit_type = audit_type or "COMBINED_DS_A11Y"
        if not (artifact_id and created_ts):
            return json.dumps({"error":"artifact_id and created_ts required"})

        audit_id = _det_id("audit", [artifact_id, created_ts, audit_type])
        audits = _safe_table(data, "audits")
        idx = _index_by(audits, "audit_id")
        row = {
            "audit_id": audit_id,
            "artifact_id": artifact_id,
            "audit_type": audit_type,
            "status": "IN_PROGRESS",
            "created_ts": created_ts
        }
        if audit_id in idx:
            audits[idx[audit_id]] = row
        else:
            audits.append(row)
        return json.dumps({"success": True, "audit_id": audit_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_audit_session",
            "description":"Create/update an audit session (deterministic id).",
            "parameters":{"type":"object","properties":{
                "artifact_id":{"type":"string"},
                "created_ts":{"type":"string"},
                "audit_type":{"type":"string"}
            },"required":["artifact_id","created_ts"]}
        }}