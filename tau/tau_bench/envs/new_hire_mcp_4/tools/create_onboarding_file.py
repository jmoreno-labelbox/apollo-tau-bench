# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateOnboardingFile(Tool):
    """Create or upsert an onboarding file for a candidate."""

    @staticmethod
    def invoke(data: Dict[str, Any], candidate_id, doc_type, file_id, uploaded_at, status = "pending") -> str:
        f = {
            "file_id": file_id,
            "candidate_id": candidate_id,
            "doc_type": doc_type,
            "status": status,
            "uploaded_at": uploaded_at,
        }
        if not f["file_id"] or not f["candidate_id"] or not f["doc_type"]:
            return json.dumps({"error": "missing_required_fields"}, indent=2)
        data.setdefault("onboarding_files", [])
        for i, existing in enumerate(data["onboarding_files"]):
            if existing.get("file_id") == f["file_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in f.items() if v is not None})
                data["onboarding_files"][i] = updated
                return json.dumps(updated, indent=2)
        data["onboarding_files"].append(f)
        return json.dumps(f, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_onboarding_file",
                "description": "Create or upsert an onboarding file for a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "candidate_id": {"type": "string"},
                        "doc_type": {"type": "string"},
                        "status": {"type": "string"},
                        "uploaded_at": {"type": "string"},
                    },
                    "required": ["file_id", "candidate_id", "doc_type"]
                }
            }
        }
