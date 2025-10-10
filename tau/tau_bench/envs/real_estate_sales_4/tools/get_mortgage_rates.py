# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMortgageRates(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_type = 'conventional', term_years = 30) -> str:
        
        rates = list(data.get('mortgage_rates', {}).values())
        filtered_rates = []
        
        for rate in rates:
            if (rate.get('loan_type') == loan_type and 
                rate.get('term_years') == term_years):
                filtered_rates.append(rate)
        
        return json.dumps({
            "loan_type": loan_type,
            "term_years": term_years,
            "rate_count": len(filtered_rates),
            "rates": filtered_rates
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mortgage_rates",
                "description": "Get current mortgage rates from available lenders",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_type": {
                            "type": "string",
                            "description": "Type of loan (conventional, fha, va, etc.)"
                        },
                        "term_years": {
                            "type": "integer",
                            "description": "Loan term in years (15, 30, etc.)"
                        }
                    },
                    "required": []
                }
            }
        }
