from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateLoanApplicationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id: str = None, new_status: str = None) -> str:
        application = next((app for app in data.get('loan_applications', {}).values() if app['application_id'] == application_id), None)
        if not application:
            return json.dumps({"error": "Loan application not found."})

        application['application_status'] = new_status
        if new_status.lower() == "withdrawn":
            application['decision'] = None

        return json.dumps(application)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "UpdateLoanApplicationStatus",
                        "description": "Updates the status of a loan application (e.g., Under Review, Withdrawn).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."},
                                        "new_status": {"type": "string", "description": "The new status for the application."}
                                },
                                "required": ["application_id", "new_status"]
                        }
                }
        }
