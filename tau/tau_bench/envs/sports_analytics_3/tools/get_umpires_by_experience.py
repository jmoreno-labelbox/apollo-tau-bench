# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUmpiresByExperience(Tool):
    """
    Return all umpires with years_experience greater than a given threshold,
    sorted by years_experience in descending order (ties broken by smallest umpire_id).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], min_experience) -> str:
        exp_threshold = min_experience

        # 1) Confirm validity
        if exp_threshold is None:
            return json.dumps({"error": "Missing required field: experience"}, indent=2)

        # Retrieve database
        umpires: List[Dict[str, Any]] = list(data.get("umpires", {}).values())

        # 3) Select entries with experience exceeding the threshold.
        filtered = [
            ump for ump in umpires
            if int(ump.get("years_experience", 0)) > exp_threshold
        ]

        if not filtered:
            return json.dumps({"error": f"No umpires found with experience greater than {exp_threshold}"}, indent=2)

        # 4) Ensure sorting is deterministic.
        sorted_list = sorted(
            filtered,
            key=lambda u: (-int(u.get("years_experience", 0)), int(u.get("umpire_id", 0)))
        )

        return json.dumps(sorted_list, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_umpires_by_experience",
                "description": "Return all umpires with years_experience greater than the provided threshold, sorted in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "experience": {
                            "type": "integer",
                            "description": "Minimum years_experience threshold; only umpires with greater experience are returned."
                        }
                    },
                    "required": ["min_experience"]
                }
            }
        }
