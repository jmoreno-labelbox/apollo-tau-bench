# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs["file_path"]
        for f in list(data.get("onboarding_files", {}).values()):
            if f.get("file_path") == file_path:
                return json.dumps({"file": f}, indent=2)
        return json.dumps({"error": f"file_path {file_path} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "read_onboarding_file",
                "description": "Read an onboarding file by file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {"type": "string"}
                    },
                    "required": ["file_path"]
                }
            }
        }
