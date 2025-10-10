# Intellectual property owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCitationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citation_id = kwargs.get('citation_id')
        if not citation_id:
            return json.dumps({"error": "citation_id is required."})

        for citation in list(data.get('citations', {}).values()):
            if citation.get('citation_id') == citation_id:
                return json.dumps(citation, indent=2)

        return json.dumps({"error": f"Citation with ID '{citation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_citation_details", "description": "Retrieves the full details for a single citation by its unique ID.", "parameters": {"type": "object", "properties": {"citation_id": {"type": "string", "description": "The unique ID of the citation to retrieve."}}, "required": ["citation_id"]}}}
