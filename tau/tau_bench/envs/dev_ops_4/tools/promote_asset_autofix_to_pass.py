# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PromoteAssetAutofixToPass(Tool):
    """Promote an autofixed QA record to 'passed' deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], qa_id) -> str:
        results = list(data.get("asset_qa_results", {}).values())
        idx = _idx_by_id(results, qa_id)
        if idx is None:
            return json.dumps({"asset_qa_result": None}, indent=2)
        rec = results[idx]
        if rec.get("autofix_applied"):
            rec["validation_status"] = "passed"
        results[idx] = rec
        return json.dumps({"asset_qa_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "promote_asset_autofix_to_pass",
                "description": "If autofix_applied is true, set validation_status='passed'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "qa_id": {"type": "string"}
                    },
                    "required": ["qa_id"]
                }
            }
        }
