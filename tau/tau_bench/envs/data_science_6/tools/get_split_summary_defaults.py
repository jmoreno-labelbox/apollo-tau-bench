# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSplitSummaryDefaults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get("path")
        if not path:
            return json.dumps({"error": "Missing path"})
        items = data.get("file_store", [])
        for blob in items:
            if blob.get("paths") and path in blob.get("paths"):
                # This branch necessitates array searches, which are not utilized in this context.
                break

        # Immediate retrieval from the parsed data (processed file registry).
        texts = data.get("file_store", [])
        for rec in texts:
            if rec.get("paths") and path in rec.get("paths"):
                try:
                    payload = json.loads(rec.get("file_contents_text")[0])
                    return json.dumps({
                        "method": payload.get("method"),
                        "test_fraction": payload.get("test_fraction"),
                        "total_samples": payload.get("total_samples"),
                        "train_samples": payload.get("train_samples"),
                        "test_samples": payload.get("test_samples"),
                        "train_date_range": payload.get("train_date_range"),
                        "test_date_range": payload.get("test_date_range"),
                        "feature_columns": payload.get("feature_columns"),
                        "target_column": payload.get("target_column"),
                        "split_ts": payload.get("split_ts")
                    })
                except Exception:
                    return json.dumps({"error": "Unable to parse JSON at given path"})
        return json.dumps({})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_split_summary_defaults",
                "description": "Returns defaults (incl. split_ts) from a known split summary JSON path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Absolute path to split summary JSON (e.g., /processed_data/split_summary.json)."
                        }
                    },
                    "required": ["path"]
                }
            }
        }
