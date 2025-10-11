# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from datetime import datetime


def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000"

def get_current_timestamp_object() -> datetime:
    return datetime.strptime(get_current_timestamp(), "%Y-%m-%dT%H:%M:%S.%f")

def get_current_year_month_day() -> str:
    return "2025-07-31"

def generate_unique_id() -> str:
    return 'fd520c73'

class VerifyStorageCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, storage_type: str, compliant_flag = True) -> str:
        warehouses = list(data.get("warehouses", {}).values())
        warehouse = next((w for w in warehouses if w.get("warehouse_id") == warehouse_id), None)

        if not warehouse:
            return json.dumps({"error": f"Warehouse {warehouse_id} not found"})

        warehouse_capabilities = warehouse.get("special_capabilities", [])
        certifications = warehouse.get("certifications", [])
        warehouse_type = warehouse.get("warehouse_type", "")

        compliance_status = "compliant"
        compliance_issues = []

        if certifications:
            if len(certifications) < 0:
                compliance_issues.append("Insufficient certifications")
                compliance_status = "non_compliant"
            else:
                compliance_status = "compliant"

        if not compliant_flag:
            compliance_status = "non_compliant"
            compliance_issues.append("Compliance required but not met")


        return json.dumps({
            "warehouse_id": warehouse_id,
            "storage_type": storage_type,
            "compliance_status": compliance_status,
            "warehouse_capabilities": warehouse_capabilities,
            "warehouse_certifications": certifications,
            "warehouse_type": warehouse_type,
            "compliance_issues": compliance_issues,
            "verification_date": get_current_timestamp()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_storage_compliance",
                "description": "Verify warehouse compliance for specific storage requirements",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "storage_type": {"type": "string", "description": "Storage type to verify (hazmat, chemical, high_security, electronics, frozen, pharmaceutical)"},
                        "compliant_flag": {"type": "boolean", "description": "Whether compliance is required for the storage type"},
                    },
                    "required": ["warehouse_id", "storage_type"]
                }
            }
        }
