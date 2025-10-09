from tau_bench.envs.tool import Tool
import json
from typing import Any

class PersistQaOutcomeV2(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        commit_sha: str,
        severity_max: str,
        errors_count: int,
        warnings_count: int,
        preview_uri: str,
        report_uri: str,
    ) -> str:
        pass
        qa = _get_table(data, "asset_qa_results")
        qa_id = f"QA-{asset_id}-{commit_sha}"
        existing = next((q for q in qa if q.get("qa_id") == qa_id), None)
        rec = {
            "qa_id": qa_id,
            "asset_id": asset_id,
            "commit_sha": commit_sha,
            "severity_max": severity_max,
            "errors_count": errors_count,
            "warnings_count": warnings_count,
            "preview_uri": preview_uri,
            "report_uri": report_uri,
        }
        if existing:
            existing.update(rec)
        else:
            qa.append(rec)
        payload = {"qa_id": qa_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PersistQaOutcomeV2",
                "description": "Persists asset QA results keyed by (asset_id, commit_sha).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "commit_sha": {"type": "string"},
                        "severity_max": {"type": "string"},
                        "errors_count": {"type": "integer"},
                        "warnings_count": {"type": "integer"},
                        "preview_uri": {"type": "string"},
                        "report_uri": {"type": "string"},
                    },
                    "required": [
                        "asset_id",
                        "commit_sha",
                        "severity_max",
                        "errors_count",
                        "warnings_count",
                        "preview_uri",
                        "report_uri",
                    ],
                },
            },
        }
