# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveFundingInfo(Tool):
    """Searches for funding sources by source_name or funding_source_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_name, funding_source_id = kwargs.get('source_name'), kwargs.get('funding_source_id')
        if not source_name and not funding_source_id:
            return json.dumps(list(data.get('funding_sources', {}).values()), indent=2)

        funding_sources = list(data.get('funding_sources', {}).values())
        results = [
            fs for fs in funding_sources if
            (not source_name or source_name.lower() in fs.get('source_name', '').lower()) and
            (not funding_source_id or fs.get('funding_source_id') == funding_source_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_funding_info", "description": "Searches for funding sources by name or ID.", "parameters": {"type": "object", "properties": {"source_name": {"type": "string"}, "funding_source_id": {"type": "string"}}}}}
