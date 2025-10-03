from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FilterHRMemos(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        memo_type: str = None,
        type: Any = None
    ) -> str:
        memos = data.get("hr_memos")

        if first_name is None or last_name is None:
            if memo_type is not None:
                temp_memos = [memo for memo in memos if memo["type"] == memo_type]
            else:
                payload = {
                    "status": "error",
                    "reason": "Insufficient information to filter memos.",
                }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        else:
            temp_memos = [
                memo
                for memo in memos
                if memo["first_name"] == first_name and memo["last_name"] == last_name
            ]

        if len(temp_memos) == 0:
            payload = {"status": "error", "reason": "Unable to find specified memos"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = temp_memos
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterHrMemos",
                "description": "Filters HR memos for matching criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the person being searched for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the person being searched for.",
                        },
                        "type": {
                            "type": "string",
                            "description": "The type of memo being searched for.",
                        },
                    },
                },
            },
        }
