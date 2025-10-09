from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindTestRunForBuildRun(Tool):
    """Locates the test run linked to a specific build run by aligning pipelines and timestamps."""

    @staticmethod
    def invoke(data: dict[str, Any], build_run_id: str = None) -> str:
        build_runs = data.get("build_runs", {}).values()
        test_runs = data.get("test_runs", {}).values()
        pipelines = data.get("pipelines", {}).values()

        build_run = next((b for b in build_runs.values() if b.get("id") == build_run_id), None)
        if not build_run:
            payload = {"error": f"Build run with ID '{build_run_id}' not found."}
            out = json.dumps(payload)
            return out

        pipeline = next(
            (p for p in pipelines.values() if p.get("name") == build_run.get("pipeline_name")),
            None,
        )
        if not pipeline:
            payload = {
                "error": f"Pipeline named '{build_run.get('pipeline_name')}' not found."
            }
            out = json.dumps(payload)
            return out

        build_start = build_run.get("started_at")
        build_end = build_run.get("ended_at")

        for test_run in test_runs.values():
            if test_run.get("pipeline_id") == pipeline.get("id"):
                test_time = test_run.get("created_at")
                if build_start <= test_time <= build_end:
                    payload = test_run
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"No matching test run found for build run '{build_run_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findTestRunForBuildRun",
                "description": "Finds the test run associated with a build run by matching pipeline and timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "build_run_id": {
                            "type": "string",
                            "description": "The ID of the build run.",
                        }
                    },
                    "required": ["build_run_id"],
                },
            },
        }
