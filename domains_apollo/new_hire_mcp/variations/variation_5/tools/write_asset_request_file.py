from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class WriteAssetRequestFile(Tool):
    """Save /onboarding/<candidate>/asset_request.json to onboarding_files."""

    @staticmethod
    def invoke(
        db: dict[str, Any],
        candidate_id: str,
        file_path: str = None,
        payload: dict = None,
        created_ts: str = None,
        updated_ts: str = None
    ) -> str:
        file_path = file_path or f"/onboarding/{candidate_id}/asset_request.json"
        payload = payload or {}
        return WriteOnboardingFile.invoke(
            db,
            candidate_id=candidate_id,
            file_path=file_path,
            content_text=json.dumps(payload, sort_keys=True, indent=2),
            mime_type="application/json",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteAssetRequestFile",
                "description": "Store asset_request.json for the candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "payload": {"type": "object"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"},
                    },
                    "required": ["candidate_id", "payload"],
                },
            },
        }
