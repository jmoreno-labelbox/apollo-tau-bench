# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class UpsertOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_path = kwargs.get("file_path")
        content_text = kwargs.get("content_text", "")
        mime_type = kwargs.get("mime_type", "text/plain")
        candidate_id = kwargs.get("candidate_id")
        rows = _ensure_list(data, "onboarding_files")
        row = _find_by_key(rows, "file_path", file_path)
        created = False
        if row is None:
            row = {"file_path": file_path, "content_text": content_text, "mime_type": mime_type, "created_ts": NOW_TS,
                   "updated_ts": NOW_TS, "candidate_id": candidate_id}
            rows.append(row)
            created = True
        else:
            row["content_text"] = content_text
            row["mime_type"] = mime_type
            row["candidate_id"] = candidate_id
            row["updated_ts"] = NOW_TS
        return json.dumps({"file_path": file_path, "created": created}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "upsert_onboarding_file",
                                                 "description": "Create or update an onboarding_files row.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"file_path": {"type": "string"},
                                                                               "content_text": {"type": "string"},
                                                                               "mime_type": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["file_path", "content_text", "mime_type",
                                                                             "candidate_id"]}}}

class UpsertJsonArtifact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, file_path, content_obj = {}) -> str:
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