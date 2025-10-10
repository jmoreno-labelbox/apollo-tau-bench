# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExportARAgingReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Simulates the export of an A/R aging report and returns the file path.
        """
        period_label = kwargs["period_label"]
        file_path = f"/reports/ar_aging/AR_Aging_Report_{period_label}.pdf"
        return json.dumps(file_path)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "ExportARAgingReport",
                "description": "Exports an Accounts Receivable (A/R) aging report for a given period.",
                "parameters": {
                    "type": "object", "properties": {
                        "period_label": {"type": "string",
                                         "description": "The period for the report, e.g., '2024-09'"}
                    },
                    "required": ["period_label"],
                },
            },
        }
