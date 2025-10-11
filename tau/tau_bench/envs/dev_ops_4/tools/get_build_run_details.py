# Copyright Sierra
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool

# ---------- Determinism helpers ----------
FIXED_NOW = "2025-01-27T12:30:00Z"
DEFAULT_AUTOMATION_DURATION_MS = 5 * 60 * 1000  # 5 minutes
ID_PREFIX = "AUTO"


def _idx_by_id(rows: List[Dict[str, Any]], _id: str) -> Optional[int]:
    for i, r in enumerate(rows):
        if r.get("id") == _id:
            return i
    return None

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