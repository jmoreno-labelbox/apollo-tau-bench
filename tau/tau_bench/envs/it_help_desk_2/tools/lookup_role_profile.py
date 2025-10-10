# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LookupRoleProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        job_title = kwargs.get("job_title")
        profiles = data.get("rbac_group_map", [])
        profile = next((p for p in profiles if p.get("department") == department and p.get("job_title") == job_title), None)
        if not profile:
            return json.dumps({"department": department, "job_title": job_title, "profile": None}, indent=2)
        return json.dumps(profile, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "lookup_role_profile", "description": "Look up the role profile for a given department and job title to get group IDs and license bundles.", "parameters": {"type": "object", "properties": {"department": {"type": "string"}, "job_title": {"type": "string"}}, "required": ["department", "job_title"]}}}
