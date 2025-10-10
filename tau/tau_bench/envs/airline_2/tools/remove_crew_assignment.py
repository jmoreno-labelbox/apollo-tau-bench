# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveCrewAssignment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], assignment_id: str) -> str:
        assignments = data.get("flight_crew_assignments", [])
        for i, a in enumerate(assignments):
            if a.get("assignment_id") == assignment_id:
                removed = assignments.pop(i)
                return _j({"assignment_id": assignment_id, "status": "removed", "removed": removed})
        return _j({"error": "assignment_not_found", "assignment_id": assignment_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "remove_crew_assignment",
            "description": "Remove a crew assignment record for a given flight deterministically.",
            "parameters": {"type": "object", "properties": {
                "assignment_id": {"type": "string"}
            }, "required": ["assignment_id"]}
        }}
