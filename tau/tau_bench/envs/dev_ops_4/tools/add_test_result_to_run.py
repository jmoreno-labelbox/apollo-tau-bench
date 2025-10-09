from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddTestResultToRun(Tool):
    """Add a test result to a test run in a deterministic manner."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        test_run_id: str = None,
        test_name: str = None,
        status: str = None,
        failure_type: str = None,
        issue_message: str = None,
        file_path: str = None,
        line_number: int = None,
        issue_code: str = None,
        duration_ms: int = None
    ) -> str:
        rec = {
            "id": f"{ID_PREFIX}::test_result::{_sanitize(test_run_id)}__{_sanitize(test_name)}::001",
            "test_run_id": test_run_id,
            "test_name": test_name,
            "status": status,
            "failure_type": failure_type,
            "issue_message": issue_message,
            "file_path": file_path,
            "line_number": line_number,
            "issue_code": issue_code,
            "stack_trace": None,
            "duration_ms": duration_ms,
            "timestamp": FIXED_NOW,
            "metadata": {},
        }
        data.setdefault("test_results", []).append(rec)
        payload = {"test_result": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddTestResultToRun",
                "description": "Append a test result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"},
                        "test_name": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["passed", "failed", "skipped"],
                        },
                        "failure_type": {"type": "string"},
                        "issue_message": {"type": "string"},
                        "file_path": {"type": "string"},
                        "line_number": {"type": "integer"},
                        "issue_code": {"type": "string"},
                        "duration_ms": {"type": "integer"},
                    },
                    "required": ["test_run_id", "test_name", "status"],
                },
            },
        }
