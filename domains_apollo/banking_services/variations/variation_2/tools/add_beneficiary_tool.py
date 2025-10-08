from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class AddBeneficiaryTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None, 
               account_number: str = None, routing_number: str = None, bank_name: str = None, iban: str = None) -> str:
        beneficiaries = data.get('beneficiaries', [])

        beneficiary_id = f"ben_{generate_unique_id()}"

        new_beneficiary = {
            "beneficiary_id": beneficiary_id,
            "customer_id": customer_id,
            "beneficiary_name": beneficiary_name,
            "account_number": account_number,
            "routing_number": routing_number,
            "bank_name": bank_name,
            "status": "Active",
            "date_added": get_current_timestamp()
        }
        
        if iban:
            new_beneficiary["iban"] = iban

        beneficiaries.append(new_beneficiary)

        return json.dumps({
            "beneficiary_id": beneficiary_id,
            "beneficiary_name": beneficiary_name,
            "status": "Active",
            "date_added": new_beneficiary["date_added"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBeneficiary",
                "description": "Add a new payment beneficiary",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "beneficiary_name": {"type": "string", "description": "Name of beneficiary"},
                        "account_number": {"type": "string", "description": "Beneficiary account number"},
                        "routing_number": {"type": "string", "description": "Bank routing number"},
                        "iban": {"type": "string", "description": "Iban routing number"},
                        "bank_name": {"type": "string", "description": "Bank name"},
                        "sort_code": {"type": "string", "description": "Sort_code routing number"}
                    },
                    "required": ["customer_id", "beneficiary_name", "bank_name"]
                }
            }
        }
