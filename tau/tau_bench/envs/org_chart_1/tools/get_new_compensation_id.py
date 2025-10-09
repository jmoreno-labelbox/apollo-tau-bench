from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_new_compensation_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], compensations: list[dict[str, Any]] = None) -> str:
        compensations = compensations if compensations is not None else []
        prefix = "COMP"
        start_num = 10000

        if not compensations:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for comp in compensations:
            comp_id = comp.get("compensation_id", "")
            if comp_id.startswith(prefix):
                try:
                    num = int(comp_id[len(prefix):])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id = f"{prefix}{max(start_num, max_id_num) + 1}"
        payload = next_id
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewCompensationId",
                "description": "Return a compensation ID that is not currently in use.",
                "parameters": {},
            },
        }
