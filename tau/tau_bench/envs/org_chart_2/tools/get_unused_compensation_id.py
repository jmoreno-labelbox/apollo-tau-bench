# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_unused_compensation_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        compensations = data.get("compensations", [])
        prefix = "COMP"
        start_num = 10000

        if not compensations:
            return json.dumps(f"{prefix}{start_num}", indent=2)

        max_id_num = 0
        for comp in compensations:
            comp_id = comp.get("compensation_id", "")
            if comp_id.startswith(prefix):
                try:
                    num = int(comp_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        return json.dumps(next_id, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_unused_compensation_id",
                "description": "Return a compensation ID that is not currently in use.",
                "parameters": {},
            },
        }
