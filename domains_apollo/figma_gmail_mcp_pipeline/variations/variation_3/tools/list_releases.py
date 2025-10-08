from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class list_releases(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        pass
        return _ok({"rows": list(_ensure(data, "releases", []))})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listReleases",
                "description": "List releases.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
