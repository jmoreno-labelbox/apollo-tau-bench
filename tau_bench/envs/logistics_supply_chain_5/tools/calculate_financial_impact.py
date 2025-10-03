from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class CalculateFinancialImpact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], product_value: float = 0, liability_estimate: float = 0) -> str:
        financial_impact = {
            "product_value_at_risk": product_value,
            "estimated_liability": liability_estimate,
            "total_financial_impact": product_value + liability_estimate,
            "insurance_coverage": min(product_value * 0.8, 100000),  # Basic coverage calculation
            "net_exposure": max(0, (product_value + liability_estimate) - min(product_value * 0.8, 100000)),
            "calculation_date": get_current_timestamp()
        }

        return json.dumps(financial_impact)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateFinancialImpact",
                "description": "Calculate financial impact of supply chain incidents",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_value": {"type": "number", "description": "Value of affected products"},
                        "liability_estimate": {"type": "number", "description": "Estimated liability amount"}
                    },
                    "required": ["product_value"]
                }
            }
        }
