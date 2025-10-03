from tau_bench.envs.tool import Tool
import json
from typing import Any

class BuildKpiReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], as_of: str = "2024-11-30", sections: list = None, artifact_name: str = "AR_KPI_Report") -> str:
        if sections is None:
            sections = []
        path = f"/reports/kpi/{artifact_name}.pdf"
        payload = {"as_of": as_of, "sections": sections, "pdf_path": path}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildKpiReport",
                "description": "Generate a KPI report artifact path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "as_of": {"type": "string"},
                        "sections": {"type": "array", "items": {"type": "string"}},
                        "artifact_name": {"type": "string"},
                    },
                    "required": ["as_of", "sections", "artifact_name"],
                },
            },
        }
