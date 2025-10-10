# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_file = kwargs.get("file") or {}
        files = list(data.get("onboarding_files", {}).values())
        files.append(new_file)
        data["onboarding_files"] = files
        return json.dumps({"added_file": new_file}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_onboarding_file",
            "description":"Add a new onboarding file.",
            "parameters":{"type":"object","properties":{"file":{"type":"object"}},"required":["file"]}
        }}
