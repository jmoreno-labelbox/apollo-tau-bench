# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_releases(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        return _ok({"rows": list(_ensure(data, "releases", []))})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_releases",
            "description":"List releases.",
            "parameters":{"type":"object","properties":{}}
        }}
