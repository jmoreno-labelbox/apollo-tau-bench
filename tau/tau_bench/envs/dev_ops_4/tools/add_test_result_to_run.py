# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _sanitize(s: str) -> str:
    return (
        s.replace("/", "_")
         .replace(".", "_")
         .replace(":", "_")
         .replace(" ", "_")
    )

class AddTestResultToRun(Tool):
    """Append a test result to a test run deterministically."""
    @staticmethod
    def invoke(data: Dict[str, Any], duration_ms, failure_type, file_path, issue_code, issue_message, line_number, status, test_name, test_run_id) -> str:

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
            "metadata": {}
        }
        data.setdefault("test_results", []).append(rec)
        return json.dumps({"test_result": rec}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_test_result_to_run",
                "description": "Append a test result.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "test_run_id": {"type": "string"},
                        "test_name": {"type": "string"},
                        "status": {"type": "string", "enum": ["passed", "failed", "skipped"]},
                        "failure_type": {"type": "string"},
                        "issue_message": {"type": "string"},
                        "file_path": {"type": "string"},
                        "line_number": {"type": "integer"},
                        "issue_code": {"type": "string"},
                        "duration_ms": {"type": "integer"}
                    },
                    "required": ["test_run_id", "test_name", "status"]
                }
            }
        }