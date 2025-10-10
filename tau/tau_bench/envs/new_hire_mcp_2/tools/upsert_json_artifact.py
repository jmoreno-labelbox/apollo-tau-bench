# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertJsonArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        content_obj = kwargs.get("content_obj", {})
        candidate_id = kwargs.get("candidate_id")
        text = json.dumps(content_obj, sort_keys=True)
        res = json.loads(
            UpsertOnboardingFile.invoke(data, file_path=file_path, content_text=text, mime_type="application/json",
                                        candidate_id=candidate_id))
        return json.dumps({"file_path": file_path, "created": res.get("created", False)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upsert_json_artifact",
                                                 "description": "Create or update a JSON artifact file under onboarding_files.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_obj": {"type": "object"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_obj",
                                                                             "candidate_id"]}}}
