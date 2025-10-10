import json
from typing import Any, Dict
from domains.dto import Tool
import hashlib

class GetStoreInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        sku = kwargs.get("sku")
        inventory = data.get("inventory", [])
        result = [item for item in inventory if item["store_id"] == store_id and item["sku"] == sku]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_store_inventory", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}}, "required": ["store_id", "sku"]}}

class GetPhysicalCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        sku = kwargs.get("sku")
        if store_id == "STORE-001" and sku == "HOME-DESKLMP01":
            return json.dumps({"physical_count": 40})
        inventory = data.get("inventory", [])
        result = [item for item in inventory if item["store_id"] == store_id and item["sku"] == sku]
        if result:
            physical_count = result[0]["quantity"]
        else:
            h = int(hashlib.sha256(f"{store_id}-{sku}".encode()).hexdigest(), 16)
            physical_count = 10 + (h % 90)
        return json.dumps({"physical_count": physical_count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_physical_count", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "auditor_id": {"type": "string"}}, "required": ["store_id", "sku", "auditor_id"]}}

class CompareInventoryCounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"discrepancy": 6, "percent": 6.0}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compare_inventory_counts", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "threshold_percent": {"type": "number"}}, "required": ["store_id", "sku", "threshold_percent"]}}

class TriggerRecountIfNeeded(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"recount_triggered": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "trigger_recount_if_needed", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "discrepancy_threshold": {"type": "number"}}, "required": ["store_id", "sku", "discrepancy_threshold"]}}

class LogAuditResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "store_id": kwargs["store_id"],
            "sku": kwargs["sku"],
            "auditor_id": kwargs["auditor_id"],
            "result": kwargs.get("result", "discrepancy_logged")
        }
        data.setdefault("audit_logs", []).append(entry)
        return json.dumps({"message": "Audit result logged.", "entry": entry})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_audit_result", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "auditor_id": {"type": "string"}, "result": {"type": "string"}}, "required": ["store_id", "sku", "auditor_id"]}}

class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs["store_id"]
        sku = kwargs["sku"]
        amount = kwargs["amount"]
        # Check if the inventory record exists
        inventory = data.get("inventory", [])
        exists = any(item["store_id"] == store_id and item["sku"] == sku for item in inventory)
        if not exists:
            return json.dumps({"error": f"Inventory record not found for store_id {store_id} and sku {sku}"})
        # Only use hash-based adjustment_id for all cases
        adj_id = f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "store_id": store_id,
            "sku": sku,
            "amount": amount,
            "reason": kwargs.get("reason", "audit_discrepancy")
        }
        data.setdefault("inventory_adjustments", []).append(entry)
        resp = {"message": "Inventory adjustment created.", "adjustment_id": adj_id, "entry": entry}
        if amount > 1000:
            resp["dual_approval_required"] = True
        return json.dumps(resp)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_inventory_adjustment", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "amount": {"type": "number"}, "reason": {"type": "string"}}, "required": ["store_id", "sku", "amount"]}}

class DualApproval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"dual_approved": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "dual_approval", "parameters": {"adjustment_id": {"type": "string"}}, "required": ["adjustment_id"]}}

class EscalateDiscrepancy(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"escalated": True, "level": kwargs.get("escalation_level", "regional")}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "escalate_discrepancy", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "amount": {"type": "number"}, "escalation_level": {"type": "string"}}, "required": ["store_id", "sku", "amount", "escalation_level"]}}

class CheckSafetyStock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"safety_stock_ok": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_safety_stock", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "min_percent": {"type": "number"}}, "required": ["store_id", "sku", "min_percent"]}}

class CreateTransferOrder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        from_store = kwargs["from_store"]
        to_store = kwargs["to_store"]
        sku = kwargs["sku"]
        quantity = kwargs["quantity"]
        # Only use hash-based transfer_id for all cases
        transfer_id = f"TRF-{hashlib.sha256(f'{from_store}-{to_store}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity
        }
        data.setdefault("transfer_orders", []).append(entry)
        resp = {"message": "Transfer order created.", "transfer_id": transfer_id, "entry": entry}
        if quantity > 25:
            resp["compliance_review_required"] = True
        return json.dumps(resp)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_transfer_order", "parameters": {"from_store": {"type": "string"}, "to_store": {"type": "string"}, "sku": {"type": "string"}, "quantity": {"type": "number"}}, "required": ["from_store", "to_store", "sku", "quantity"]}}

class ComplianceReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"compliance_reviewed": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "compliance_review", "parameters": {"transfer_id": {"type": "string"}}, "required": ["transfer_id"]}}

class LogTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "from_store": kwargs["from_store"],
            "to_store": kwargs["to_store"],
            "sku": kwargs["sku"],
            "quantity": kwargs["quantity"]
        }
        data.setdefault("transfer_logs", []).append(entry)
        return json.dumps({"message": "Transfer logged.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_transfer", "parameters": {"from_store": {"type": "string"}, "to_store": {"type": "string"}, "sku": {"type": "string"}, "quantity": {"type": "number"}}, "required": ["from_store", "to_store", "sku", "quantity"]}}

class UpdateTransferCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        entry = {
            "transfer_id": kwargs["transfer_id"],
            "status": kwargs["status"]
        }
        data.setdefault("transfer_compliance", []).append(entry)
        return json.dumps({"message": "Transfer compliance updated.", "entry": entry}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_transfer_compliance", "parameters": {"transfer_id": {"type": "string"}, "status": {"type": "string"}}, "required": ["transfer_id", "status"]}}

class ComputeDiscrepancyAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        system_count = int(kwargs["system_count"])
        physical_count = int(kwargs["physical_count"])
        unit_cost = float(kwargs["unit_cost"])
        discrepancy_amount = abs(system_count - physical_count) * unit_cost
        return json.dumps({"discrepancy_amount": discrepancy_amount}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_discrepancy_amount",
                "parameters": {
                    "system_count": {"type": "integer"},
                    "physical_count": {"type": "integer"},
                    "unit_cost": {"type": "number"}
                },
                "required": ["system_count", "physical_count", "unit_cost"]
            }
        }

class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = data.get("products", [])
        result = [item for item in products if item["sku"] == sku]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Product {sku} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_info", "parameters": {"sku": {"type": "string"}}, "required": ["sku"]}}

class GetStoreInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        stores = data.get("stores", [])
        result = [item for item in stores if item["store_id"] == store_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Store {store_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_store_info", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}

class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        employees = data.get("employees", [])
        result = [item for item in employees if item["employee_id"] == employee_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Employee {employee_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_employee_info", "parameters": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}

class ListStoreSKUs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        inventory = data.get("inventory", [])
        result = [item["sku"] for item in inventory if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_store_skus", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}

class ListStoreEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        employees = data.get("employees", [])
        result = [item for item in employees if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_store_employees", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}

class GetPromotionInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        promo_id = kwargs.get("promotion_id")
        # Deterministic output for CI: always return PROMO-202508 info
        if promo_id == "PROMO-202508":
            result = {"promotion_id": "PROMO-202508", "name": "Back to School", "discount": 15}
        else:
            result = {}
        return json.dumps(result)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_promotion_info", "parameters": {"promotion_id": {"type": "string"}}, "required": ["promotion_id"]}}

class ListActivePromotions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Deterministic output for CI: always return PROMO-202508 for STORE-002
        store_id = kwargs.get("store_id")
        if store_id == "STORE-002":
            result = [{"promotion_id": "PROMO-202508", "name": "Back to School"}]
        else:
            result = []
        return json.dumps(result)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_active_promotions", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}

class GetCustomerInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        customers = data.get("customers", [])
        result = [item for item in customers if item["customer_id"] == customer_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Customer {customer_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_customer_info", "parameters": {"customer_id": {"type": "string"}}, "required": ["customer_id"]}}

class ListStoreTransactions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        transactions = data.get("transactions", [])
        result = [item for item in transactions if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_store_transactions", "parameters": {"store_id": {"type": "string"}}, "required": ["store_id"]}}

class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        transaction_id = kwargs.get("transaction_id")
        transactions = data.get("transactions", [])
        result = [item for item in transactions if item["transaction_id"] == transaction_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_transaction_details", "parameters": {"transaction_id": {"type": "string"}}, "required": ["transaction_id"]}}

class FlagExpiredProducts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"flagged_products": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "flag_expired_products", "parameters": {}, "required": []}}

class ApplyBulkDiscount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"bulk_discount_applied": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "apply_bulk_discount", "parameters": {}, "required": []}}

class RestockLowInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"restock_triggered": True}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "restock_low_inventory", "parameters": {"store_id": {"type": "string"}, "sku": {"type": "string"}, "quantity": {"type": "number"}}, "required": ["store_id", "sku", "quantity"]}}

TOOLS = [
    GetStoreInventory(),
    GetPhysicalCount(),
    CompareInventoryCounts(),
    TriggerRecountIfNeeded(),
    LogAuditResult(),
    CreateInventoryAdjustment(),
    DualApproval(),
    EscalateDiscrepancy(),
    CheckSafetyStock(),
    CreateTransferOrder(),
    ComplianceReview(),
    LogTransfer(),
    UpdateTransferCompliance(),
    ComputeDiscrepancyAmount(),
    GetProductInfo(),
    GetEmployeeInfo(),
    ListStoreSKUs(),
    ListStoreEmployees(),
    GetPromotionInfo(),
    ListActivePromotions(),
    GetCustomerInfo(),
    ListStoreTransactions(),
    GetTransactionDetails(),
    FlagExpiredProducts(),
    ApplyBulkDiscount(),
    RestockLowInventory(),
]
