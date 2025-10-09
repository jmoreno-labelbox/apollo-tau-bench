from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetMortgageRates(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], loan_type: str = "conventional", term_years: int = 30, document_id: Any = None) -> str:
        rates = data.get("mortgage_rates", {}).values()
        filtered_rates = []

        for rate in rates:
            if (
                rate.get("loan_type") == loan_type
                and rate.get("term_years") == term_years
            ):
                filtered_data["mortgage_rates"][rate["mortgage_rate_id"]] = rate
        payload = {
                "loan_type": loan_type,
                "term_years": term_years,
                "rate_count": len(filtered_rates),
                "rates": filtered_rates,
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
                "name": "getMortgageRates",
                "description": "Get current mortgage rates from available lenders",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_type": {
                            "type": "string",
                            "description": "Type of loan (conventional, fha, va, etc.)",
                        },
                        "term_years": {
                            "type": "integer",
                            "description": "Loan term in years (15, 30, etc.)",
                        },
                    },
                    "required": [],
                },
            },
        }
