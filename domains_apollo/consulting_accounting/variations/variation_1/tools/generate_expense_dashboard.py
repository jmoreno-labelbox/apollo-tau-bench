from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateExpenseDashboard(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], quarter: str = None, included_expenses: list = None, as_of: str = None, artifact_name: str = None) -> str:
        if not quarter or not isinstance(included_expenses, list):
            payload = {"error": "quarter and included_expenses list are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        path = (
            f"/dashboards/ExpenseDashboards/{quarter}/expense_dashboard_{quarter}.pdf"
        )
        payload = {"quarter": quarter, "included_expenses": included_expenses, "pdf_path": path}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateExpenseDashboard",
                "description": "Generate an expense dashboard artifact for a given quarter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "quarter": {"type": "string"},
                        "included_expenses": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["quarter", "included_expenses"],
                },
            },
        }
