from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSplitSummaryDefaults(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], path: str = None) -> str:
        if not path:
            payload = {"error": "Missing path"}
            out = json.dumps(payload)
            return out
        items = data.get("file_store", {}).values()
        for blob in items.values():
            if blob.get("paths") and path in blob.get("paths"):
                # This path would necessitate searching through arrays; not utilized here.
                break

        # Immediate retrieval from parsed data (processed file registry)
        texts = data.get("file_store", {}).values()
        for rec in texts.values():
            if rec.get("paths") and path in rec.get("paths"):
                try:
                    payload = json.loads(rec.get("file_contents_text")[0])
                    payload = {
                        "method": payload.get("method"),
                        "test_fraction": payload.get("test_fraction"),
                        "total_samples": payload.get("total_samples"),
                        "train_samples": payload.get("train_samples"),
                        "test_samples": payload.get("test_samples"),
                        "train_date_range": payload.get("train_date_range"),
                        "test_date_range": payload.get("test_date_range"),
                        "feature_columns": payload.get("feature_columns"),
                        "target_column": payload.get("target_column"),
                        "split_ts": payload.get("split_ts"),
                    }
                    out = json.dumps(payload)
                    return out
                except Exception:
                    payload = {"error": "Unable to parse JSON at given path"}
                    out = json.dumps(payload)
                    return out
        payload = {}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSplitSummaryDefaults",
                "description": "Returns defaults (incl. split_ts) from a known split summary JSON path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Absolute path to split summary JSON (e.g., /processed_data/split_summary.json).",
                        }
                    },
                    "required": ["path"],
                },
            },
        }
