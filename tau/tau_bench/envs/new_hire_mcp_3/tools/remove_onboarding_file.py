# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], file_path) -> str:
        files = list(data.get("onboarding_files", {}).values())
        data["onboarding_files"] = [f for f in files if f.get("file_path") != file_path]
        return json.dumps({"removed_file_path": file_path}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_onboarding_file",
            "description":"Remove an onboarding file by file path.",
            "parameters":{"type":"object","properties":{"file_path":{"type":"string"}},"required":["file_path"]}
        }}
