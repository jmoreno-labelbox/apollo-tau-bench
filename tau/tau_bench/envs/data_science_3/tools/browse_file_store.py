# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BrowseFileStore(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"files": data.get("file_store", [])}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_file_store",
            "description":"List all files in the file store.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}
