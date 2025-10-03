from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class CreateOnboardingFile(Tool):
    """Establish or insert an onboarding document for a candidate."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str, candidate_id: str, doc_type: str, status: str = "pending", uploaded_at: str = None) -> str:
        f = {
            "file_id": file_id,
            "candidate_id": candidate_id,
            "doc_type": doc_type,
            "status": status,
            "uploaded_at": uploaded_at,
        }
        if not f["file_id"] or not f["candidate_id"] or not f["doc_type"]:
            payload = {"error": "missing_required_fields"}
            out = json.dumps(payload, indent=2)
            return out
        data.setdefault("onboarding_files", [])
        for i, existing in enumerate(data["onboarding_files"]):
            if existing.get("file_id") == f["file_id"]:
                updated = dict(existing)
                updated.update({k: v for k, v in f.items() if v is not None})
                data["onboarding_files"][i] = updated
                payload = updated
                out = json.dumps(payload, indent=2)
                return out
        data["onboarding_files"].append(f)
        payload = f
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createOnboardingFile",
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
                    "required": ["file_id", "candidate_id", "doc_type"],
                },
            },
        }
