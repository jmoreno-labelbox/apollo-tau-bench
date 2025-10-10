# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindTestRunForBuildRun(Tool):
    """Finds the test run associated with a specific build run by matching pipelines and timestamps."""
    @staticmethod
    def invoke(data: Dict[str, Any], build_run_id) -> str:
        build_runs = data.get("build_runs", [])
        test_runs = data.get("test_runs", [])
        pipelines = list(data.get("pipelines", {}).values())

        build_run = next((b for b in build_runs if b.get("id") == build_run_id), None)
        if not build_run:
            return json.dumps({"error": f"Build run with ID '{build_run_id}' not found."})

        pipeline = next((p for p in pipelines if p.get("name") == build_run.get("pipeline_name")), None)
        if not pipeline:
            return json.dumps({"error": f"Pipeline named '{build_run.get('pipeline_name')}' not found."})

        build_start = build_run.get("started_at")
        build_end = build_run.get("ended_at")

        for test_run in test_runs:
            if test_run.get("pipeline_id") == pipeline.get("id"):
                test_time = test_run.get("created_at")
                if build_start <= test_time <= build_end:
                    return json.dumps(test_run)
        
        return json.dumps({"error": f"No matching test run found for build run '{build_run_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_test_run_for_build_run",
                "description": "Finds the test run associated with a build run by matching pipeline and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {"type": "string", "description": "The ID of the build run."}
                    },
                    "required": ["build_run_id"]
                }
            }
        }
