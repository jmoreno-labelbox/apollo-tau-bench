# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStores(Tool):
    """Return all stores."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return _json_dump(data.get("stores", []))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_stores",
            "description":"List available stores.",
            "parameters":{"type":"object","properties":{}}
        }}
