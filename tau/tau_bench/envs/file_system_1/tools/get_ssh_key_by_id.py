# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSshKeyByID(Tool):
    """Fetches details for a specific SSH key, including which servers it is authorized on."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        key_id = kwargs.get("key_id")
        for key in data.get('ssh_keys', []):
            if key.get('key_id') == key_id:
                return json.dumps(key)
        return json.dumps({"error": f"SSH key with ID '{key_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_ssh_key_by_id", "description": "Retrieves details for a specific SSH key, including its list of authorized servers.", "parameters": {"type": "object", "properties": {"key_id": {"type": "string", "description": "The ID of the SSH key (e.g., 'alice_rsa_key')."}}, "required": ["key_id"]}}}
