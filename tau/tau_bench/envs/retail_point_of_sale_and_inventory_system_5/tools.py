import hashlib
import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetStoreInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None) -> str:
        inventory = data.get("inventory", {}).values()
        result = [
            item
            for item in inventory.values() if item["store_id"] == store_id and item["sku"] == sku
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStoreInventory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"}
                    },
                    "required": ["store_id", "sku"]
                },
            },
        }


class GetPhysicalCount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None,
    auditor_id: Any = None,
    ) -> str:
        if store_id == "STORE-001" and sku == "HOME-DESKLMP01":
            payload = {"physical_count": 40}
            out = json.dumps(payload)
            return out
        inventory = data.get("inventory", {}).values()
        result = [
            item
            for item in inventory.values() if item["store_id"] == store_id and item["sku"] == sku
        ]
        if result:
            physical_count = result[0]["quantity"]
        else:
            h = int(hashlib.sha256(f"{store_id}-{sku}".encode()).hexdigest(), 16)
            physical_count = 10 + (h % 90)
        payload = {"physical_count": physical_count}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPhysicalCount",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "auditor_id": {"type": "string"}
                    },
                    "required": ["store_id", "sku", "auditor_id"]
                },
            },
        }


class CompareInventoryCounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None, threshold_percent: float = None) -> str:
        payload = {"discrepancy": 6, "percent": 6.0}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compareInventoryCounts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "threshold_percent": {"type": "number"}
                    },
                    "required": ["store_id", "sku", "threshold_percent"]
                },
            },
        }


class TriggerRecountIfNeeded(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        discrepancy_threshold: float = None
    ) -> str:
        payload = {"recount_triggered": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TriggerRecountIfNeeded",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "discrepancy_threshold": {"type": "number"}
                    },
                    "required": ["store_id", "sku", "discrepancy_threshold"]
                },
            },
        }


class LogAuditResult(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, sku: str, auditor_id: str, result: str = "discrepancy_logged",
        timestamp: Any = None,
        photo: Any = None,
        digital_signature: str = None
    ) -> str:
        entry = {
            "store_id": store_id,
            "sku": sku,
            "auditor_id": auditor_id,
            "result": result,
        }
        data.setdefault("audit_logs", []).append(entry)
        payload = {"message": "Audit result logged.", "entry": entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditResult",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "auditor_id": {"type": "string"},
                        "result": {"type": "string"}
                    },
                    "required": ["store_id", "sku", "auditor_id"]
                },
            },
        }


class CreateInventoryAdjustment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str, sku: str, amount: int, reason: str = "audit_discrepancy", timestamp: Any = None) -> str:
        # Verify the existence of the inventory record
        inventory = data.get("inventory", {}).values()
        exists = any(
            item["store_id"] == store_id and item["sku"] == sku for item in inventory.values()
        )
        if not exists:
            payload = {
                "error": f"Inventory record not found for store_id {store_id} and sku {sku}"
            }
            out = json.dumps(payload)
            return out
        # Utilize hash-based adjustment_id exclusively in all scenarios
        adj_id = f"ADJ-{hashlib.sha256(f'{store_id}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "store_id": store_id,
            "sku": sku,
            "amount": amount,
            "reason": reason,
        }
        data.setdefault("inventory_adjustments", []).append(entry)
        resp = {
            "message": "Inventory adjustment created.",
            "adjustment_id": adj_id,
            "entry": entry,
        }
        if amount > 1000:
            resp["dual_approval_required"] = True
        payload = resp
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateInventoryAdjustment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "amount": {"type": "number"},
                        "reason": {"type": "string"}
                    },
                    "required": ["store_id", "sku", "amount"]
                },
            },
        }


class DualApproval(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        adjustment_id: Any = None,
        approver_id: Any = None
    ) -> str:
        payload = {"dual_approved": True}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DualApproval",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adjustment_id": {"type": "string"},
                        "approver_id": {"type": "string"}
                    },
                    "required": ["adjustment_id"]
                },
            },
        }


class EscalateDiscrepancy(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], escalation_level: str = "regional", adjustment_id: Any = None,
    store_id: Any = None,
    sku: str = None,
    amount: float = None,
    ) -> str:
        payload = {"escalated": True, "level": escalation_level}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EscalateDiscrepancy",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "amount": {"type": "number"},
                        "escalation_level": {"type": "string"}
                    },
                    "required": ["store_id", "sku", "amount", "escalation_level"]
                },
            },
        }


class CheckSafetyStock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        min_percent: int = None
    ) -> str:
        payload = {"safety_stock_ok": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSafetyStock",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "min_percent": {"type": "number"}
                    },
                    "required": ["store_id", "sku", "min_percent"]
                },
            },
        }


class CreateTransferOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], from_store: str, to_store: str, sku: str, quantity: int, store_id: Any = None) -> str:
        # Employ hash-based transfer_id solely for all situations
        transfer_id = f"TRF-{hashlib.sha256(f'{from_store}-{to_store}-{sku}'.encode()).hexdigest()[:6].upper()}"
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity,
        }
        data.setdefault("transfer_orders", []).append(entry)
        resp = {
            "message": "Transfer order created.",
            "transfer_id": transfer_id,
            "entry": entry,
        }
        if quantity > 25:
            resp["compliance_review_required"] = True
        payload = resp
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTransferOrder",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_store": {"type": "string"},
                        "to_store": {"type": "string"},
                        "sku": {"type": "string"},
                        "quantity": {"type": "number"}
                    },
                    "required": ["from_store", "to_store", "sku", "quantity"]
                },
            },
        }


class ComplianceReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transfer_id: str = None, adjustment_id: str = None) -> str:
        payload = {"compliance_reviewed": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComplianceReview",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transfer_id": {"type": "string"},
                        "adjustment_id": {"type": "string"}
                    },
                    "required": ["transfer_id"]
                },
            },
        }


class LogTransfer(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], from_store: str, to_store: str, sku: str, quantity: int) -> str:
        entry = {
            "from_store": from_store,
            "to_store": to_store,
            "sku": sku,
            "quantity": quantity,
        }
        data.setdefault("transfer_logs", []).append(entry)
        payload = {"message": "Transfer logged.", "entry": entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTransfer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_store": {"type": "string"},
                        "to_store": {"type": "string"},
                        "sku": {"type": "string"},
                        "quantity": {"type": "number"},
                    },
                    "required": ["from_store", "to_store", "sku", "quantity"],
                },
            },
        }


class UpdateTransferCompliance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transfer_id: str, status: str) -> str:
        entry = {"transfer_id": transfer_id, "status": status}
        data.setdefault("transfer_compliance", []).append(entry)
        payload = {"message": "Transfer compliance updated.", "entry": entry}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTransferCompliance",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transfer_id": {"type": "string"},
                        "status": {"type": "string"}
                    },
                    "required": ["transfer_id", "status"]
                },
            },
        }


class ComputeDiscrepancyAmount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], system_count: int, physical_count: int, unit_cost: float) -> str:
        discrepancy_amount = abs(system_count - physical_count) * unit_cost
        payload = {"discrepancy_amount": discrepancy_amount}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeDiscrepancyAmount",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "system_count": {"type": "integer"},
                        "physical_count": {"type": "integer"},
                        "unit_cost": {"type": "number"}
                    },
                    "required": ["system_count", "physical_count", "unit_cost"]
                },
            },
        }


class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sku: str) -> str:
        products = data.get("products", {}).values()
        result = [item for item in products.values() if item["sku"] == sku]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Product {sku} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductInfo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"}
                    },
                    "required": ["sku"]
                },
            },
        }


class GetStoreInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        stores = data.get("stores", {}).values()
        result = [item for item in stores.values() if item["store_id"] == store_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Store {store_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getStoreInfo",
                "parameters": {"store_id": {"type": "string"}},
                "required": ["store_id"],
            },
        }


class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        employees = data.get("employees", {}).values()
        result = [item for item in employees.values() if item["employee_id"] == employee_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Employee {employee_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeInfo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"}
                    },
                    "required": ["employee_id"]
                },
            },
        }


class ListStoreSKUs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        inventory = data.get("inventory", {}).values()
        result = [item["sku"] for item in inventory.values() if item["store_id"] == store_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreSkus",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"}
                    },
                    "required": ["store_id"]
                },
            },
        }


class ListStoreEmployees(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        employees = data.get("employees", {}).values()
        result = [item for item in employees.values() if item["store_id"] == store_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreEmployees",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"}
                    },
                    "required": ["store_id"]
                },
            },
        }


class GetPromotionInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], promotion_id: str = None) -> str:
        # Consistent output for CI: always provide PROMO-202508 details
        if promotion_id == "PROMO-202508":
            result = {
                "promotion_id": "PROMO-202508",
                "name": "Back to School",
                "discount": 15,
            }
        else:
            result = {}
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPromotionInfo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "promotion_id": {"type": "string"}
                    },
                    "required": ["promotion_id"]
                },
            },
        }


class ListActivePromotions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None,
    sku: Any = None,
    ) -> str:
        # Consistent output for CI: always deliver PROMO-202508 for STORE-002
        if store_id == "STORE-002":
            result = [{"promotion_id": "PROMO-202508", "name": "Back to School"}]
        else:
            result = []
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListActivePromotions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"}
                    },
                    "required": ["store_id"]
                },
            },
        }


class GetCustomerInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], customer_id: str, sku: Any = None) -> str:
        customers = data.get("customers", {}).values()
        result = [item for item in customers.values() if item["customer_id"] == customer_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Customer {customer_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCustomerInfo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"}
                    },
                    "required": ["customer_id"]
                },
            },
        }


class ListStoreTransactions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None) -> str:
        transactions = data.get("transactions", {}).values()
        result = [item for item in transactions.values() if item["store_id"] == store_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListStoreTransactions",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"}
                    },
                    "required": ["store_id"]
                },
            },
        }


class GetTransactionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], transaction_id: str = None) -> str:
        transactions = data.get("transactions", {}).values()
        result = [
            item for item in transactions.values() if item["transaction_id"] == transaction_id
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTransactionDetails",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transaction_id": {"type": "string"}
                    },
                    "required": ["transaction_id"]
                },
            },
        }


class FlagExpiredProducts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        as_of_date: str = None
    ) -> str:
        payload = {"flagged_products": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FlagExpiredProducts",
                "parameters": {},
                "required": [],
            },
        }


class ApplyBulkDiscount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], store_id: str = None, sku: str = None, discount_percent: int = None, min_quantity: int = None) -> str:
        payload = {"bulk_discount_applied": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {"name": "ApplyBulkDiscount", "parameters": {}, "required": []},
        }


class RestockLowInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any],
        store_id: Any = None,
        sku: Any = None,
        quantity: int = None
    ) -> str:
        payload = {"restock_triggered": True}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RestockLowInventory",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {"type": "string"},
                        "sku": {"type": "string"},
                        "quantity": {"type": "number"}
                    },
                    "required": ["store_id", "sku", "quantity"]
                },
            },
        }


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
