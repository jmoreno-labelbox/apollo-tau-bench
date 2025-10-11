# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadOnboardingFile(Tool):
    """Read a file from onboarding_files by file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], file_path) -> str:
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
