from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_review_cycles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        return _ok({"rows": list(_ensure(data, "review_cycles", []))})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListReviewCycles",
                "description": "List review cycles.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
