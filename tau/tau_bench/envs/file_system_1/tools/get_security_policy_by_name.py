# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSecurityPolicyByName(Tool):
    """Retrieves a specific security policy by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], policy_name) -> str:
        for policy in data.get('security_policies', []):
            if policy.get('name') == policy_name:
                return json.dumps(policy)
        return json.dumps({"error": f"Security policy named '{policy_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_security_policy_by_name", "description": "Fetches an entire security policy document by its name (e.g., 'SSH Access Policy').", "parameters": {"type": "object", "properties": {"policy_name": {"type": "string", "description": "The name of the security policy."}}, "required": ["policy_name"]}}}
