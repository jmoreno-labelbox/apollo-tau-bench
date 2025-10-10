# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupplierDetails(Tool):
    """Read supplier record by supplier_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        if not supplier_id:
            return json.dumps({"error":"supplier_id is required"}, indent=2)
        sup = next((s for s in data.get('suppliers', []) if s.get('supplier_id') == supplier_id), None)
        return json.dumps(sup or {"error": f"supplier_id {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_supplier_details","description":"Fetch supplier by ID.","parameters":{"type":"object","properties":{"supplier_id":{"type":"string"}},"required":["supplier_id"]}}}
