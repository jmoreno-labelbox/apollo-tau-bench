# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarrierDetails(Tool):
    """Retrieves the full details for a single carrier by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get('carrier_name')
        if not carrier_name:
            return json.dumps({"error": "carrier_name is required."}, indent=2)
        carrier = next(
                (
                    c for c in data.get('carriers', [])
                    if carrier_name.lower() in c.get('carrier_name', '').lower()
                ),
                None
            )
        if not carrier:
            return json.dumps({"error": f"Carrier '{carrier_name}' not found."}, indent=2)
        return json.dumps(carrier, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_carrier_details", "description": "Retrieves the full details for a single carrier by its name.", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}}, "required": ["carrier_name"]}}}
