from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class PromoteAssetAutofixToPass(Tool):
    """Upgrade an autofixed QA record to 'passed' in a deterministic way."""

    @staticmethod
    def invoke(data: dict[str, Any], qa_id: str = None) -> str:
        results = data.get("asset_qa_results", [])
        idx = _idx_by_id(results, qa_id)
        if idx is None:
            payload = {"asset_qa_result": None}
            out = json.dumps(payload, indent=2)
            return out
        rec = results[idx]
        if rec.get("autofix_applied"):
            rec["validation_status"] = "passed"
        results[idx] = rec
        payload = {"asset_qa_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PromoteAssetAutofixToPass",
                "description": "If autofix_applied is true, set validation_status='passed'.",
                "parameters": {
                    "type": "object",
                    "properties": {"qa_id": {"type": "string"}},
                    "required": ["qa_id"],
                },
            },
        }
