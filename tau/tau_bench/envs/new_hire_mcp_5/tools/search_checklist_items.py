# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchChecklistItems(Tool):
    """Filter checklist_items by candidate_id, optional status, optional due_date_lte."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cand_id = kwargs["candidate_id"]
        status = kwargs.get("status")
        due_lte = kwargs.get("due_date_lte")
        rows = []
        for it in list(data.get("checklist_items", {}).values()):
            if it.get("candidate_id") != cand_id:
                continue
            if status and it.get("status") != status:
                continue
            if due_lte and it.get("due_date") and it["due_date"] > due_lte:
                continue
            rows.append(it)
        return json.dumps({"items": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_checklist_items",
                "description": "Search checklist items for a candidate with simple filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "status": {"type": "string"},
                        "due_date_lte": {"type": "string"}
                    },
                    "required": ["candidate_id"]
                }
            }
        }
