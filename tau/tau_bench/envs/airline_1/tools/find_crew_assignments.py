# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCrewAssignments(Tool):
    """
    A tool to find flight assignments for a specific crew member.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], crew_member_id: str, flight_number:Optional[str] = None) -> str:
        assignments = data.get("flight_crew_assignments", [])
        results = [a for a in assignments if a["crew_member"]["crew_member_id"] == crew_member_id]
        if flight_number:
            results = [a for a in results if a["flight"]["flight_number"] == flight_number]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_crew_assignments",
                "description": "Finds all flight assignments for a given crew member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "crew_member_id": {
                            "type": "string",
                            "description": "The unique ID of the crew member."
                        },
                        "flight_number": {
                            "type": "string",
                            "description": "Optional: Filter assignments by a specific flight number."
                        }
                    },
                    "required": ["crew_member_id"]
                }
            }
        }
