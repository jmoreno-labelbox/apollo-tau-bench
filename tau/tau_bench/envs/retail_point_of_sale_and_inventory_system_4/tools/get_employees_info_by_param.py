# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeesInfoByParam(Tool): # READ
    @staticmethod
    def invoke(data: Dict[str, Any], filter_params: Dict[str, Any], info_items: List[str] = None) -> str:
        db = list(data.get("employees", {}).values())
        filtered_db = _filter_db(db, filter_params)
        if not info_items:
            return json.dumps(filtered_db)
        return json.dumps([{info_item: row.get(info_item) for info_item in info_items} for row in filtered_db])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employees_info_by_param",
                "description": "Filter employees by any combination of fields. Returns all fields by default, or only those specified in 'fields' parameter if given.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filter_params": {"type": "object", "description": "Dictionary of ways to filter items in the database. To pass the filter an item must match one of the possible given values for all the filtering paramets"},
                        "info_items": {"type": "list", "items": {"type": "string"}, "description": "A list of all the keys of the infomation that should be returned by the function for the filtered database entries."}
                    },
                    "required": ["filter_params"]
                }
            }
        }
