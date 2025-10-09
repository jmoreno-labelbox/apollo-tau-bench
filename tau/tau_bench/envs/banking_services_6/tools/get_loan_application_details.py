from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLoanApplicationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id: str = None) -> str:
        application = next((app for app in data.get('loan_applications', []) if app['application_id'] == application_id), None)
        if application:
            return json.dumps(application)
        return json.dumps({"error": "Loan application not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetLoanApplicationDetails",
                        "description": "Retrieves the full details of a single loan application.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."}
                                },
                                "required": ["application_id"]
                        }
                }
        }
