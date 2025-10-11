# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteAssetRequestFile(Tool):
    """Write /onboarding/<candidate>/asset_request.json into onboarding_files."""
    @staticmethod
    def invoke(db: Dict[str, Any], candidate_id, created_ts, file_path, updated_ts, payload = {}) -> str:
        cand_id = candidate_id
        file_path = file_path or f"/onboarding/{cand_id}/asset_request.json"
        return WriteOnboardingFile.invoke(
            db,
            candidate_id=cand_id,
            file_path=file_path,
            content_text=json.dumps(payload, sort_keys=True, indent=2),
            mime_type="application/json",
            created_ts=created_ts,
            updated_ts=updated_ts,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_asset_request_file",
                "description": "Store asset_request.json for the candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "file_path": {"type": "string"},
                        "payload": {"type": "object"},
                        "created_ts": {"type": "string"},
                        "updated_ts": {"type": "string"}
                    },
                    "required": ["candidate_id", "payload"]
                }
            }
        }
