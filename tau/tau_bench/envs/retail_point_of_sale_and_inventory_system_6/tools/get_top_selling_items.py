from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class get_top_selling_items(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], n_values: int = None, store_id: str = None, payment_method: str = None, customer_id: str = None) -> str:
        transactions = data.get("transactions", [])

        filter_cols = ["store_id", "payment_method", "customer_id"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        filter_values = {k: params_dict.get(k) for k in filter_cols if params_dict.get(k) is not None}

        item_tracker = defaultdict(int)
        for transaction in transactions:
            # Apply filters based on any provided values
            if all([filter_values[k] == transaction[k] for k in filter_values.keys()]):
                line_items = transaction["line_items"]
                for item in line_items:
                    item_tracker[item["sku"]] += item["quantity"]

        out = OrderedDict()

        # Arrange the values by total and retrieve the top n items
        sort = sorted(item_tracker, key=item_tracker.get, reverse=True)
        if n_values is not None:
            sort = sort[:n_values]
        for sku in sort:
            out[sku] = item_tracker[sku]
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopSellingItems",
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
