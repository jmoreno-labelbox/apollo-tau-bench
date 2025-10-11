# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

class MapFindingsToFramesSummaryTool(Tool):
    """Produce a per-frame summary of counts from DS and A11y findings for a given audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], audit_id) -> str:
        audit_id = _require_str(audit_id, "audit_id")
        if not audit_id:
            return json.dumps({"error":"audit_id is required"})

        ds = [r for r in data.get("audit_findings_ds", []) if r.get("audit_id") == audit_id]
        a11y = [r for r in data.get("audit_findings_a11y", []) if r.get("audit_id") == audit_id]
        counts: Dict[str, Dict[str,int]] = {}
        for r in ds:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds":0,"a11y":0})
            bucket["ds"] += 1
        for r in a11y:
            fid = r.get("frame_id")
            bucket = counts.setdefault(fid, {"ds":0,"a11y":0})
            bucket["a11y"] += 1

        out = [{"frame_id": k, "ds_count": v["ds"], "a11y_count": v["a11y"]} for k,v in sorted(counts.items())]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"map_findings_to_frames_summary",
            "description":"Return per-frame counts of DS and A11y findings for a given audit.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"}
            },"required":["audit_id"]}
        }}