# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[Dict[str, Any]]:
    idx = _idx_by_id(rows, _id)
    return rows[idx] if idx is not None else None

class GetBuildRunDetails(Tool):
    """Return full details for a build run by its id."""
    @staticmethod
    def invoke(data: Dict[str, Any], run_id) -> str:
        runs = list(data.get("build_runs", {}).values())
        run = _find_by_id(runs, run_id)
        return json.dumps({"run": run}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_build_run_details",
                "description": "Fetch a single build run by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"}
                    },
                    "required": ["run_id"]
                }
            }
        }