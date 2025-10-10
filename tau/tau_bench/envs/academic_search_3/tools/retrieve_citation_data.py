# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveCitationData(Tool):
    """Tool to get the full details of a specific citation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citation_id = kwargs.get('citation_id')
        for citation in list(data.get('citations', {}).values()):
            if citation.get('citation_id') == citation_id:
                return json.dumps(citation, indent=2)
        return json.dumps({"error": f"Citation with ID {citation_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_citation_data", "description": "Retrieves the full details of a specific citation by its ID.", "parameters": {"type": "object", "properties": {
            "citation_id": {"type": "string", "description": "The unique ID of the citation."}
        }, "required": ["citation_id"]}}}
