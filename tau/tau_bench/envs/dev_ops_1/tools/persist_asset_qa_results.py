# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _get_table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return data.setdefault(name, [])

class PersistAssetQaResults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, commit_sha: str, severity_max: str, errors_count: int, warnings_count: int, preview_uri: str, report_uri: str) -> str:
        qa = _get_table(data, "asset_qa_results")
        qa_id = f"QA-{asset_id}-{commit_sha}"
        existing = next((q for q in qa if q.get("qa_id") == qa_id), None)
        rec = {"qa_id": qa_id, "asset_id": asset_id, "commit_sha": commit_sha, "severity_max": severity_max, "errors_count": errors_count, "warnings_count": warnings_count, "preview_uri": preview_uri, "report_uri": report_uri}
        if existing:
            existing.update(rec)
        else:
            qa.append(rec)
        return json.dumps({"qa_id": qa_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "persist_asset_qa_results", "description": "Persists an asset QA results row keyed by (asset_id, commit_sha).", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "commit_sha": {"type": "string"}, "severity_max": {"type": "string"}, "errors_count": {"type": "integer"}, "warnings_count": {"type": "integer"}, "preview_uri": {"type": "string"}, "report_uri": {"type": "string"}}, "required": ["asset_id", "commit_sha", "severity_max", "errors_count", "warnings_count", "preview_uri", "report_uri"]}}}