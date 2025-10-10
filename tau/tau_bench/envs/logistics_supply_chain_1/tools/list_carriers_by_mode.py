# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCarriersByMode(Tool):
    """A tool to find all active carriers that support a specific mode of transport."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        mode = kwargs.get('mode')
        if not mode:
            return json.dumps({"error": "mode is a required argument."}, indent=2)
        carriers = data.get('carriers', [])
        matching_carriers = [c for c in carriers if c.get('active_status') is True and mode.title() in c.get('supported_modes', [])]
        return json.dumps(matching_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_carriers_by_mode", "description": "Finds all active carriers for a given transportation mode.", "parameters": {"type": "object", "properties": {"mode": {"type": "string", "description": "The mode of transport to filter by (e.g., 'Air', 'Sea')."}}, "required": ["mode"]}}}
