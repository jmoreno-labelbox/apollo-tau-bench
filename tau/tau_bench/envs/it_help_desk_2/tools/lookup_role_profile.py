from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LookupRoleProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, job_title: str = None) -> str:
        profiles = data.get("rbac_group_map", [])
        profile = next(
            (
                p
                for p in profiles
                if p.get("department") == department and p.get("job_title") == job_title
            ),
            None,
        )
        if not profile:
            payload = {"department": department, "job_title": job_title, "profile": None}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = profile
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupRoleProfile",
                "description": "Look up the role profile for a given department and job title to get group IDs and license bundles.",
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
