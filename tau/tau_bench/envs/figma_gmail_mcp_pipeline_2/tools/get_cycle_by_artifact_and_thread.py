from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetCycleByArtifactAndThread(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, artifact_id: str = None) -> str:
        if not thread_id:
            payload = {"error": "Missing required field: thread_id"}
            out = json.dumps(payload, indent=2)
            return out

        cycles: list[dict[str, Any]] = data.get("review_cycles", {}).values()
        results: list[dict[str, Any]] = []
        for row in cycles:
            if row.get("thread_id_nullable") != thread_id:
                continue
            if artifact_id and row.get("artifact_id") != artifact_id:
                continue
            results.append(row)

        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("cycle_id"))))
        if not results:
            if artifact_id:
                payload = {
                        "error": f"No cycles found for thread_id '{thread_id}' and artifact_id '{artifact_id}'"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            payload = {"error": f"No cycles found for thread_id '{thread_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"count": len(results), "cycles": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCycleByArtifactAndThread",
                "description": "Return review cycles for a thread, optionally filtered by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"},
                    },
                    "required": ["thread_id"],
                },
            },
        }
