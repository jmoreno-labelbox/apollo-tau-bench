# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListClientEmails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cid = kwargs.get("client_id")
        rows = [e for e in (data.get("emails") or []) if e.get("client_id") == cid]
        return json.dumps({"client_id": cid, "emails": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_client_emails",
                "description": "List all emails for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
