from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTestResult(Tool):
    """Retrieve a test result using id."""

    @staticmethod
    def invoke(data: dict[str, Any], id: Any = None) -> str:
        tid = id
        rows = _table(data, "test_results")
        row = next((r for r in rows if r.get("id") == tid), None)
        return _ok({"test_result": row}) if row else _err("test_result not found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTestResult",
                "description": "Fetch a test result by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
