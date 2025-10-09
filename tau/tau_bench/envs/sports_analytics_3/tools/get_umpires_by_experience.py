from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUmpiresByExperience(Tool):
    """
    Retrieve all umpires with years_experience exceeding a specified threshold,
    sorted by years_experience in descending order (ties resolved by smallest umpire_id).
    """

    @staticmethod
    def invoke(data: dict[str, Any], min_experience: int = None) -> str:
        #1) Confirm validity
        if min_experience is None:
            payload = {"error": "Missing required field: experience"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        umpires: list[dict[str, Any]] = data.get("umpires", [])

        #3) Filter for individuals with experience exceeding threshold
        filtered = [
            ump
            for ump in umpires
            if int(ump.get("years_experience", 0)) > min_experience
        ]

        if not filtered:
            payload = {
                    "error": f"No umpires found with experience greater than {min_experience}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Sort in a deterministic manner
        sorted_list = sorted(
            filtered,
            key=lambda u: (
                -int(u.get("years_experience", 0)),
                int(u.get("umpire_id", 0)),
            ),
        )
        payload = sorted_list
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUmpiresByExperience",
                "description": "Return all umpires with years_experience greater than the provided threshold, sorted in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "experience": {
                            "type": "integer",
                            "description": "Minimum years_experience threshold; only umpires with greater experience are returned.",
                        }
                    },
                    "required": ["min_experience"],
                },
            },
        }
