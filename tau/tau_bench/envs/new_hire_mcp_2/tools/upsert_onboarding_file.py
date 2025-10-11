# All rights reserved by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None

def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class UpsertOnboardingFile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, file_path, content_text = "", mime_type = "text/plain") -> str:
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