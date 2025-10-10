# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetBuildFailureCategorization(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_build_failure_categorization",
                "description": "Sets failure categorization for a build run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string", "description": "Build run id"},
                        "category": {"type": "string", "description": "Top-level category"},
                        "subcategory": {"type": "string", "description": "Optional subcategory"}
                    },
                    "required": ["run_id", "category"]
                }
            }
        }

    @staticmethod
    def invoke(data, **kwargs):
        run_id = kwargs.get("run_id")
        category = kwargs.get("category")
        subcategory = kwargs.get("subcategory")
        runs = data.get("build_runs", [])
        run = next((r for r in runs if r.get("id") == run_id), None)
        if not run:
            return json.dumps({"error": "run_not_found", "run_id": run_id})
        meta = run.get("metadata") or {}
        fc = meta.get("failure_category") or {}
        fc["category"] = category
        if subcategory is not None:
            fc["subcategory"] = subcategory
        meta["failure_category"] = fc
        run["metadata"] = meta
        return json.dumps({"run": run}, indent=2)
