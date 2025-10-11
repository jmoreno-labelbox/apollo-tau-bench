# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"projects": list(data.get("projects", {}).values())}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_projects",
            "description":"List all projects.",
            "parameters":{"type":"object","properties":{},"required":[]}
        }}
