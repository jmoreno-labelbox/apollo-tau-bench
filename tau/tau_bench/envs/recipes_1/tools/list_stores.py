# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump




def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class ListStores(Tool):
    """Return all stores."""
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return _json_dump(list(data.get("stores", {}).values()))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_stores",
            "description":"List available stores.",
            "parameters":{"type":"object","properties":{}}
        }}