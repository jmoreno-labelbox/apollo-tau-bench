from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetBuildFailureCategorization(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetBuildFailureCategorization",
                "description": "Sets failure categorization for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "category": {
                            "type": "string",
                            "description": "Top-level category",
                        },
                        "subcategory": {
                            "type": "string",
                            "description": "Optional subcategory",
                        },
                    },
                    "required": ["run_id", "category"],
                },
            },
        }

    @staticmethod
    def invoke(data, run_id=None, category=None, subcategory=None):
        runs = data.get("build_runs", {}).values()
        run = next((r for r in runs.values() if r.get("id") == run_id), None)
        if not run:
            payload = {"error": "run_not_found", "run_id": run_id}
            out = json.dumps(payload)
            return out
        meta = run.get("metadata") or {}
        fc = meta.get("failure_category") or {}
        fc["category"] = category
        if subcategory is not None:
            fc["subcategory"] = subcategory
        meta["failure_category"] = fc
        run["metadata"] = meta
        payload = {"run": run}
        out = json.dumps(payload, indent=2)
        return out
