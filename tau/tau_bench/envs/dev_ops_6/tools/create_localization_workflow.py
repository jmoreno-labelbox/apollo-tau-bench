from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateLocalizationWorkflow(Tool):
    """Generate a localization_workflow record (deterministic; will error on duplicate id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str = None,
        pr_number: int = None,
        changed_keys: list = None,
        locales_processed: list = None,
        bundle_uris: dict = None,
        overflow_issues: int = 0,
        tms_job_id: str = None,
        status: str = "queued",
        timestamp: str = FIXED_TS,
        metadata: dict = None
    ) -> str:
        pass
        table = _table(data, "localization_workflow")
        wid = id
        #--- FIX: Create ID if it is not supplied ---
        if not wid:
            wid = f"loc_workflow_{len(table) + 1:04d}"

        if any(w.get("id") == wid for w in table.values()):
            return _err(f"localization_workflow id {wid} already exists")
        record = {
            "id": wid,
            "pr_number": pr_number,
            "changed_keys": changed_keys or [],
            "locales_processed": locales_processed or [],
            "bundle_uris": bundle_uris or {},
            "overflow_issues": overflow_issues,
            "tms_job_id": tms_job_id,
            "status": status,
            "timestamp": timestamp,
            "metadata": metadata or {},
        }
        table.append(record)
        return _ok({"localization_workflow": record})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createLocalizationWorkflow",
                "description": "Create a localization_workflow record (deterministic fields).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "changed_keys": {"type": "array", "items": {"type": "string"}},
                        "locales_processed": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "bundle_uris": {"type": "object"},
                        "overflow_issues": {"type": "integer"},
                        "tms_job_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "metadata": {"type": "object"},
                    },
                    "required": ["pr_number", "changed_keys"],
                },
            },
        }
