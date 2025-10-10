# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReleaseDiffSummaryTool(Tool):
    """Summarize a release diff: counts of added/updated/removed frames."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        release_id = _require_str(kwargs.get("release_id"), "release_id")
        if not release_id:
            return json.dumps({"error":"release_id is required"})

        diffs = data.get("release_diffs", [])
        adds = updates = removes = 0
        for d in diffs:
            if d.get("release_id") != release_id:
                continue
            t = d.get("change_type")
            if t == "ADDED": adds += 1
            elif t == "UPDATED": updates += 1
            elif t == "REMOVED": removes += 1

        return json.dumps({"release_id": release_id, "added": adds, "updated": updates, "removed": removes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_release_diff_summary",
            "description":"Return counts of ADDED/UPDATED/REMOVED items for a release.",
            "parameters":{"type":"object","properties":{
                "release_id":{"type":"string"}
            },"required":["release_id"]}
        }}
