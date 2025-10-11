# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTransactionsInfoByParam(Tool): # READ DATA
    @staticmethod
    def invoke(data: Dict[str, Any], filter_params: Dict[str, Any], info_items: List[str] = None) -> str:
        db = list(data.get("transactions", {}).values())
        # Filter transactions by line_items that include the sku if it exists in filter_params.
        filter_params_no_sku = filter_params.copy()
        if "sku" in filter_params.keys():
            db = [transaction for transaction in db if any(item["sku"] in filter_params["sku"] for item in transaction.get("line_items", []))]
            del filter_params_no_sku["sku"]  # Eliminate sku from filter_params after it has been utilized.

        filtered_db = _filter_db(db, filter_params_no_sku)
        if not info_items:
            return json.dumps(filtered_db)
        return json.dumps([{info_item: row.get(info_item) for info_item in info_items} for row in filtered_db])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_transactions_info_by_param",
                "description": "Filter transactions by parameters and return specified fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {"type": "object", "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets"},
                        "info_items": {"type": "array", "items": {"type": "string"}, "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."}
                    },
                    "required": ["filter_params"]
                }
            }
        }
