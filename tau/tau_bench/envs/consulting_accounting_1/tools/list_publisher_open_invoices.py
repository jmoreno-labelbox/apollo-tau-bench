# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPublisherOpenInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pub_id = kwargs.get("publisher_id")
        if not pub_id:
            return json.dumps({"error": "publisher_id is required"}, indent=2)
        invoices = list(data.get("invoices", {}).values())
        open_invs = [i for i in invoices if i.get("publisher_id") == pub_id and not i.get("paid_at")]
        return json.dumps({"publisher_id": pub_id,"invoice_ids": [i["invoice_id"] for i in open_invs]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "list_publisher_open_invoices","description": "Return unpaid invoice IDs for a publisher.","parameters": {"type": "object","properties": {"publisher_id": {"type": "string"}},"required": ["publisher_id"]}}}
