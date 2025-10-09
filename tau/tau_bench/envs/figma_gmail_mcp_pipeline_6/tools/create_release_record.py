from tau_bench.envs.tool import Tool
import json
from typing import Any

class create_release_record(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], artifact_id: str, timestamp: str, request_id: str
    ) -> str:
        releases = data.setdefault("releases", [])
        day_iso = (timestamp or "").split("T")[0]
        day_compact = day_iso.replace("-", "")
        release_id = f"rel-{artifact_id}-{day_compact}-001"

        for r in releases:
            if isinstance(r, dict) and r.get("release_id") == release_id:
                payload = r
                out = json.dumps(payload, indent=2)
                return out

        row = {
            "release_id": release_id,
            "artifact_id": artifact_id,
            "day": day_iso,
            "request_id": request_id,
        }
        data["releases"][release_id] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReleaseRecord",
                "description": "Create/reuse a deterministic release row (rel-<artifact>-<YYYYMMDD>-001).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "artifact_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["artifact_id", "timestamp", "request_id"],
                },
            },
        }
