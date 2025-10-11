# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteOnboardingFile(Tool):
    """Insert/update onboarding_files entry for candidate_id + file_path."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, created_ts, file_path, updated_ts, content_text = "", mime_type = "text/markdown") -> str:
        cand_id = candidate_id
        created_ts = _fixed_ts(created_ts)
        updated_ts = _fixed_ts(updated_ts)

        files = data.setdefault("onboarding_files", [])
        for f in files:
            if f.get("file_path") == file_path and f.get("candidate_id") == cand_id:
                f["content_text"] = content_text
                f["mime_type"] = mime_type
                f["updated_ts"] = updated_ts
                return json.dumps({"file_path": file_path, "status": "updated"}, indent=2)

        files.append({
            "file_path": file_path,
            "content_text": content_text,
            "mime_type": mime_type,
            "created_ts": created_ts,
            "updated_ts": updated_ts,
            "candidate_id": cand_id
        })
        return json.dumps({"file_path": file_path, "status": "created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_onboarding_file",
                "description": "Create or update an onboarding file record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "content_text": {"type": "string"},
                        "mime_type": {"type": "string"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "file_path"]
                }
            }
        }
