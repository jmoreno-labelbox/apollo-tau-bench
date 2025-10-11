# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

def _error(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

class SetAssetQaCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number: int, conclusion: str, details_uri: str) -> str:
        prs = _get_table(data, "pull_requests")
        pr = next((p for p in prs if p.get("pr_number") == pr_number), None)
        if not pr:
            return _error(f"PR '{pr_number}' not found.")
        checks = pr.setdefault("checks", [])
        checks.append({"name": "Asset QA", "conclusion": conclusion, "details_uri": details_uri})
        return json.dumps({"check_count": len(checks)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_asset_qa_check", "description": "Sets a deterministic PR check result named 'Asset QA'.", "parameters": {"type": "object", "properties": {"pr_number": {"type": "integer"}, "conclusion": {"type": "string"}, "details_uri": {"type": "string"}}, "required": ["pr_number", "conclusion", "details_uri"]}}}