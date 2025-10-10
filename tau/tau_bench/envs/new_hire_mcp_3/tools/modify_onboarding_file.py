# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], file_path, updates) -> str:
        updates = updates or {}
        files = list(data.get("onboarding_files", {}).values())
        for f in files:
            if f.get("file_path") == file_path:
                f.update(updates)
                f["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_file_path": file_path, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_onboarding_file",
            "description":"Update an onboarding file content or metadata.",
            "parameters":{"type":"object","properties":{"file_path":{"type":"string"},"updates":{"type":"object"}},"required":["file_path","updates"]}
        }}
