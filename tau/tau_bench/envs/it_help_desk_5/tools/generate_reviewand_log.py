from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateReviewandLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], log_data: Any = None) -> str:
        if log_data is None:
            payload = {"status": "error", "description": "The log_data field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        formatted_date = FIXED_NOW.split("T")[0].replace("-", "_")
        new_report = {
            "run_id": f"rpt_{formatted_date}_0000",
            "report_type": "review_log",
            "started_at": FIXED_NOW,
            "completed_at": FIXED_NOW,
            "output_path_pdf": f"s3://reports/Report_{formatted_date}.pdf",
        }

        reports = data.get("validation_issues", {}).values()
        data["validation_issues"][new_report["validation_issue_id"]] = new_report
        payload = {
                "status": "ok",
                "description": "Successfully created pdf and added report to validation_issues.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateReviewAndLog",
                "description": "Generates a review packet pdf from input data and creates a log in validation_issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_data": {
                            "type": "string",
                            "description": "The data to log in the report.",
                        },
                    },
                    "required": ["log_data"],
                },
            },
        }
