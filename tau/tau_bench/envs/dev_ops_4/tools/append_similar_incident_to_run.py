from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AppendSimilarIncidentToRun(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AppendSimilarIncidentToRun",
                "description": "Appends a similar incident reference to a run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {
                            "type": "string",
                            "description": "Current build run id",
                        },
                        "incident_run_id": {
                            "type": "string",
                            "description": "Related incident run id",
                        },
                        "similarity_score": {
                            "type": "number",
                            "description": "Similarity score 0..1",
                        },
                    },
                    "required": ["run_id", "incident_run_id"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, incident_run_id=None, similarity_score=None):
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        arr = meta.get("similar_incidents") or []
        arr.append({"incident_run_id": incident_run_id, "similarity_score": similarity_score})
        meta["similar_incidents"] = arr
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
