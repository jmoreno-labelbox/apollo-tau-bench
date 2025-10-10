# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BrowseFileIndex(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"files": list(data.get("file_store", {}).values())}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "browse_file_index",
            "description": "List all file metadata rows.",
            "parameters": {"type": "object", "properties": {}, "required": []}
        }}
