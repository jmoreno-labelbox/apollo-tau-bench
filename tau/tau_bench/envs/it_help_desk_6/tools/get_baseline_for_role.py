# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], ) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class GetBaselineForRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department: str, job_title: str) -> str:
        row = _find_one(data["rbac_group_map"], department=department, job_title=job_title)
        if not row:
            return json.dumps({"status": "error", "reason": "rbac_baseline_not_found"})
        return json.dumps(
            {
                "status": "ok",
                "group_ids": row.get("group_ids", []),
                "default_license_bundle": row.get("default_license_bundle", []),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_baseline_for_role",
                "description": "Return RBAC baseline group_ids and default license bundle for department/job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {"department": {"type": "string"}, "job_title": {"type": "string"}},
                    "required": ["department", "job_title"],
                },
            },
        }