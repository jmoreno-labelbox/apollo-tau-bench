# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class SetAssetQaCheckV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, conclusion: str, details_uri: str) -> str:
        checks = _get_table(data, "test_results")
        check_id = f"check-{len(checks)+1}"
        checks.append({"id": check_id, "pr_number": pr_number, "name": "Asset QA", "conclusion": conclusion, "details_uri": details_uri})
        return json.dumps({"check_id": check_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_asset_qa_check_v2", "description": "Set the PR check for Asset QA deterministically.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "conclusion": {"type": "string"}, "details_uri": {"type": "string"}}, "required": ["pr_number", "conclusion", "details_uri"]}}}