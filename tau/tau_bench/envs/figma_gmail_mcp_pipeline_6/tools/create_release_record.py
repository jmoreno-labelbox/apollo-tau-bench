# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_release_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], artifact_id: str, timestamp: str, request_id: str) -> str:
        releases = data.setdefault("releases", [])
        day_iso = (timestamp or "").split("T")[0]
        day_compact = day_iso.replace("-", "")
        release_id = f"rel-{artifact_id}-{day_compact}-001"

        for r in releases:
            if isinstance(r, dict) and r.get("release_id") == release_id:
                return json.dumps(r, indent=2)

        row = {
            "release_id": release_id,
            "artifact_id": artifact_id,
            "day": day_iso,
            "request_id": request_id,
        }
        releases.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"create_release_record","description":"Create/reuse a deterministic release row (rel-<artifact>-<YYYYMMDD>-001).","parameters":{"type":"object","properties":{"artifact_id":{"type":"string"},"timestamp":{"type":"string"},"request_id":{"type":"string"}},"required":["artifact_id","timestamp","request_id"]}}}
