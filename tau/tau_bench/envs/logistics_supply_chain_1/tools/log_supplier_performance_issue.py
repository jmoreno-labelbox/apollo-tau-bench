# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogSupplierPerformanceIssue(Tool):
    """Logs a performance issue against a supplier's record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        issue_code = kwargs.get('issue_code')
        shipment_id = kwargs.get('shipment_id')
        if not all([supplier_id, issue_code]):
            return json.dumps({"error": "supplier_id and issue_code are required."}, indent=2)
        supplier_to_update = next((s for s in data.get('supplier_master', []) if s.get('supplier_id') == supplier_id), None)
        if not supplier_to_update:
            return json.dumps({"error": f"Supplier '{supplier_id}' not found."}, indent=2)
        if 'performance_logs' not in supplier_to_update:
            supplier_to_update['performance_logs'] = []
        log_entry = {"issue_code": issue_code, "related_shipment": shipment_id}
        supplier_to_update['performance_logs'].append(log_entry)
        return json.dumps(supplier_to_update, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_supplier_performance_issue", "description": "Logs a performance issue against a supplier's record.", "parameters": {"type": "object", "properties": {"supplier_id": {"type": "string"}, "issue_code": {"type": "string"}, "shipment_id": {"type": "string"}}, "required": ["supplier_id", "issue_code"]}}}
