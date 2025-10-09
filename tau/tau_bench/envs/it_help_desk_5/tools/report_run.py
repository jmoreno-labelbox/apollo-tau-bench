from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ReportRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_type: str = None, run_data: Any = None) -> str:
        if report_type is None or run_data is None:
            payload = {
                "status": "error",
                "description": "The report_type and data fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        run_date = FIXED_NOW.split("T")[0].replace("-", "_")
        new_report = {
            "run_id": f"rpt_{run_date}_0000",
            "report_type": report_type,
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/{report_type}_{run_date}.pdf",
        }

        reports = data.get("report_runs")
        reports.append(new_report)
        payload = {
            "status": "ok",
            "description": "Successfully created report pdf and saved a log in report_runs.",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reportRun",
                "description": "Creates a report log in report_runs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "description": "The type of the report to write.",
                        },
                        "run_data": {
                            "type": "array",
                            "items": {"type": "string"},
                            "item": {"type": "string"},
                            "description": "The data to include in the run.",
                        },
                    },
                    "required": ["report_type", "run_data"],
                },
            },
        }
