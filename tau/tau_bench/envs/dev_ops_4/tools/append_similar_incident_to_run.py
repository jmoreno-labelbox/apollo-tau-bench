# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendSimilarIncidentToRun(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "append_similar_incident_to_run",
                "description": "Appends a similar incident reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Current build run id"},
                        "incident_run_id": {"type": "string", "description": "Related incident run id"},
                        "similarity_score": {"type": "number", "description": "Similarity score 0..1"}
                    },
                    "required": ["run_id", "incident_run_id"]
                }
            }
        }

    @staticmethod
    def invoke(data, incident_run_id, run_id, similarity_score):
        score = similarity_score
        runs = list(data.get("build_runs", {}).values())
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        arr = meta.get("similar_incidents") or []
        arr.append({"incident_run_id": incident_run_id, "similarity_score": score})
        meta["similar_incidents"] = arr
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
