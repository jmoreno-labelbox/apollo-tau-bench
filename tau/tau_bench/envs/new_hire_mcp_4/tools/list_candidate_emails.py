# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCandidateEmails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id) -> str:
        cand_id = candidate_id
        rows = [e for e in list(data.get("emails", {}).values()) if e.get("candidate_id_nullable") == cand_id]
        return json.dumps({"emails": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_candidate_emails",
                "description": "List emails for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"]
                }
            }
        }
