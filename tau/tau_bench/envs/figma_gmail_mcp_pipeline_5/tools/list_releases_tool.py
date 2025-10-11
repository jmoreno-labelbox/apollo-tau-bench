# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}

class ListReleasesTool(Tool):
    """List releases filtered by version_tag prefix or artifact_id reference."""

    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id, version_prefix = "release/") -> str:
        prefix = version_prefix

        releases = data.get("releases", [])
        out = []
        for r in releases:
            if prefix and not str(r.get("version_tag","")).startswith(prefix):
                continue
            if artifact_id and r.get("artifact_id") != artifact_id:
                continue
            out.append(_small_fields(r, ["release_id","version_tag","artifact_id","created_ts","thread_id_nullable"]))
        out.sort(key=lambda r: r.get("version_tag",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_releases",
            "description":"List releases with optional version prefix and artifact filter.",
            "parameters":{"type":"object","properties":{
                "version_prefix":{"type":"string","description":"Default 'release/'."},
                "artifact_id":{"type":"string"}
            }}
        }}