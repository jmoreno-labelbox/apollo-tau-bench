from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AssignRBACLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, job_title: str = None) -> str:
        if license_id is None or job_title is None:
            payload = {
                    "status": "error",
                    "description": "The license_id and job_title fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        group_map = data.get("rbac_group_map")

        for group in group_map:
            if group["job_title"] == job_title:
                group["default_license_bundle"].append(license_id)
                payload = group["default_license_bundle"]
                out = json.dumps(payload)
                return out
        payload = {
                "status": "error",
                "description": "The job title could not be found with an rbac group association.",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignRbacLicense",
                "description": "Assigns a license to be default in the rbac_group_map for a job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The id of the license to add.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to assign the license to.",
                        },
                    },
                    "required": ["license_id", "job_title"],
                },
            },
        }
