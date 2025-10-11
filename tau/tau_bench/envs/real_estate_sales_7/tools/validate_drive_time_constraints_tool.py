# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateDriveTimeConstraintsTool(Tool):
    """Validates that sequential hops between properties are within a max hop time."""

    @staticmethod
    def invoke(data: Dict[str, Any], max_hop_minutes, property_list) -> str:
        property_list = property_list or []
        max_hop_minutes = _as_int(max_hop_minutes)
        if (
            not isinstance(property_list, list)
            or not property_list
            or max_hop_minutes is None
        ):
            return _err("property_list (list) and max_hop_minutes are required")

        max_constraint = min(30, max_hop_minutes)
        segments = []
        if property_list:
            # Employ fixed mock times akin to the route optimizer.
            for a, b in zip(["start"] + property_list[:-1], property_list):
                travel = 18 if a == "start" else 15
                travel_minutes = min(travel, max_constraint)
                segments.append({"from": a, "to": b, "travel_minutes": travel_minutes})

        constraint_satisfied = all(
            s.get("travel_minutes", 999) <= max_constraint for s in segments
        )
        out = {
            "property_list": property_list,
            "max_hop_minutes": max_hop_minutes,
            "segments": segments,
            "constraint_satisfied": bool(constraint_satisfied),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_drive_time_constraints",
                "description": (
                    "Validate that a proposed property sequence meets hop-time limits."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_list": {"type": "array", "items": {"type": "string"}},
                        "max_hop_minutes": {"type": "integer"},
                    },
                    "required": ["property_list", "max_hop_minutes"],
                },
            },
        }
