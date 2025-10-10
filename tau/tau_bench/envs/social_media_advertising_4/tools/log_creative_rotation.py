# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogCreativeRotation(Tool):
    """Adds an entry to the creative rotation log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rotations = data.get('creative_rotations', [])
        new_id = f"CR-{max((int(c['rotation_id'][3:]) for c in rotations), default=0) + 1}"
        new_log = {"rotation_id": new_id, "adset_id": kwargs.get("adset_id"), "old_ad_id": kwargs.get("old_ad_id"), "new_ad_id": kwargs.get("new_ad_id"), "rotated_at": "2025-08-15T03:00:00Z", "rationale": kwargs.get("rationale")}
        rotations.append(new_log)
        data['creative_rotations'] = rotations
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_creative_rotation", "description": "Writes an audit log entry for an ad creative rotation.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_ad_id": {"type": "string"}, "new_ad_id": {"type": "string"}, "rationale": {"type": "string"}}, "required": ["adset_id", "old_ad_id", "new_ad_id", "rationale"]}}}
