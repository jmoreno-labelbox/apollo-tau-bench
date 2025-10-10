# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSubmissionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], submission_id) -> str:
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        submissions = list(data.get('submissions', {}).values())
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                return json.dumps(sub, indent=2)

        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_submission_details",
                "description": "Retrieves the full details for a single submission by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The unique ID of the submission to retrieve."}
                    },
                    "required": ["submission_id"]
                }
            }
        }
