from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MapFindingsToFramesSummaryTool(Tool):
    """Generate a per-frame summary of counts from DS and A11y findings for a specific audit."""

    @staticmethod
    def invoke(data: dict[str, Any], audit_id: str = None) -> str:
        audit_id = _require_str(audit_id, "audit_id")
        if not audit_id:
            payload = {"error": "audit_id is required"}
            out = json.dumps(payload)
            return out

        ds = [
            r
            for r in data.get("audit_findings_ds", {}).values()
            if r.get("audit_id") == audit_id
        ]
        a11y = [
            r
            for r in data.get("audit_findings_a11y", {}).values()
            if r.get("audit_id") == audit_id
        ]
        counts: dict[str, dict[str, int]] = {}
        for r in ds:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds": 0, "a11y": 0})
            bucket["ds"] += 1
        for r in a11y:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds": 0, "a11y": 0})
            bucket["a11y"] += 1

        out = [
            {"frame_id": k, "ds_count": v["ds"], "a11y_count": v["a11y"]}
            for k, v in sorted(counts.items())
        ]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapFindingsToFramesSummary",
                "description": "Return per-frame counts of DS and A11y findings for a given audit.",
                "parameters": {
                    "type": "object",
                    "properties": {"audit_id": {"type": "string"}},
                    "required": ["audit_id"],
                },
            },
        }
