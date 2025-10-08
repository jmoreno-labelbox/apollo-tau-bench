from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetBaselineForRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str, job_title: str) -> str:
        pass
        row = _find_one(
            data["rbac_group_map"], department=department, job_title=job_title
        )
        if not row:
            payload = {"status": "error", "reason": "rbac_baseline_not_found"}
            out = json.dumps(payload)
            return out
        payload = {
                "status": "ok",
                "group_ids": row.get("group_ids", []),
                "default_license_bundle": row.get("default_license_bundle", []),
            }
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBaselineForRole",
                "description": "Return RBAC baseline group_ids and default license bundle for department/job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                    },
                    "required": ["department", "job_title"],
                },
            },
        }
