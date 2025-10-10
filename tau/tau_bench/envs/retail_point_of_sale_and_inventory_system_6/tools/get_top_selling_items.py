# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_top_selling_items(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transactions = list(data.get("transactions", {}).values())

        n_values = kwargs.get("n_values")

        filter_cols = ["store_id", "payment_method", "customer_id"]
        filter_values = {k: kwargs.get(k) for k in filter_cols if k in kwargs}

        item_tracker = defaultdict(int)
        for transaction in transactions:
            # Filter on any sent values
            if all([filter_values[k] == transaction[k] for k in filter_values.keys()]):
                line_items = transaction["line_items"]
                for item in line_items:
                    item_tracker[item["sku"]] += item["quantity"]

        out = OrderedDict()

        # Sort the values by total and get the top n items
        sort = sorted(item_tracker, key=item_tracker.get, reverse=True)
        if n_values is not None:
            sort = sort[:n_values]
        for sku in sorted(item_tracker, key=item_tracker.get, reverse=True)[:n_values]:
            out[sku] = item_tracker[sku]

        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_selling_items",
                "description": "Gets top selling items. Can filter values to narrow the scope",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the store id",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the payment method",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "OPTIONAL. Filters on the customer id",
                        },
                    },
                },
            },
        }
