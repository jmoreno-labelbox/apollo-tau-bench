# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteCitation(Tool):
    """Tool to delete a citation record."""
    @staticmethod
    def invoke(data: Dict[str, Any], citation_id) -> str:
        citations = list(data.get('citations', {}).values())
        original_count = len(citations)
        data['citations'] = [c for c in citations if c.get('citation_id') != citation_id]
        if len(data['citations']) < original_count:
            return json.dumps({"status": "success", "citation_id": citation_id, "message": "Citation deleted."})
        else:
            return json.dumps({"error": f"Citation with ID {citation_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_citation", "description": "Deletes a specific citation record by its ID.", "parameters": {"type": "object", "properties": {
            "citation_id": {"type": "string", "description": "The unique ID of the citation to delete."}
        }, "required": ["citation_id"]}}}
