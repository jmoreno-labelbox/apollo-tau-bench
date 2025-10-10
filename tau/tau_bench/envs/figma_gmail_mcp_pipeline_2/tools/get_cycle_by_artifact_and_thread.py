# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCycleByArtifactAndThread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("thread_id"):
            return json.dumps({"error": "Missing required field: thread_id"}, indent=2)

        thread_id = kwargs.get("thread_id")
        artifact_id: Optional[str] = kwargs.get("artifact_id")

        cycles: List[Dict[str, Any]] = list(data.get("review_cycles", {}).values())
        results: List[Dict[str, Any]] = []
        for row in cycles:
            if row.get("thread_id_nullable") != thread_id:
                continue
            if artifact_id and row.get("artifact_id") != artifact_id:
                continue
            results.append(row)

        results.sort(key=lambda r: (str(r.get("created_ts")), str(r.get("cycle_id"))))
        if not results:
            if artifact_id:
                return json.dumps({"error": f"No cycles found for thread_id '{thread_id}' and artifact_id '{artifact_id}'"}, indent=2)
            return json.dumps({"error": f"No cycles found for thread_id '{thread_id}'"}, indent=2)

        return json.dumps({"count": len(results), "cycles": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cycle_by_artifact_and_thread",
                "description": "Return review cycles for a thread, optionally filtered by artifact_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "artifact_id": {"type": "string"}
                    },
                    "required": ["thread_id"]
                }
            }
        }
