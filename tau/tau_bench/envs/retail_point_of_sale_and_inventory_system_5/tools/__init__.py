# Copyright Sierra

from .get_store_inventory import GetStoreInventory
from .get_physical_count import GetPhysicalCount
from .compare_inventory_counts import CompareInventoryCounts
from .trigger_recount_if_needed import TriggerRecountIfNeeded
from .log_audit_result import LogAuditResult
from .create_inventory_adjustment import CreateInventoryAdjustment
from .dual_approval import DualApproval
from .escalate_discrepancy import EscalateDiscrepancy
from .check_safety_stock import CheckSafetyStock
from .create_transfer_order import CreateTransferOrder
from .compliance_review import ComplianceReview
from .log_transfer import LogTransfer
from .update_transfer_compliance import UpdateTransferCompliance
from .compute_discrepancy_amount import ComputeDiscrepancyAmount
from .get_product_info import GetProductInfo
from .get_store_info import GetStoreInfo
from .get_employee_info import GetEmployeeInfo
from .list_store_sk_us import ListStoreSKUs
from .list_store_employees import ListStoreEmployees
from .get_promotion_info import GetPromotionInfo
from .list_active_promotions import ListActivePromotions
from .get_customer_info import GetCustomerInfo
from .list_store_transactions import ListStoreTransactions
from .get_transaction_details import GetTransactionDetails
from .flag_expired_products import FlagExpiredProducts
from .apply_bulk_discount import ApplyBulkDiscount
from .restock_low_inventory import RestockLowInventory

ALL_TOOLS = [
    GetStoreInventory,
    GetPhysicalCount,
    CompareInventoryCounts,
    TriggerRecountIfNeeded,
    LogAuditResult,
    CreateInventoryAdjustment,
    DualApproval,
    EscalateDiscrepancy,
    CheckSafetyStock,
    CreateTransferOrder,
    ComplianceReview,
    LogTransfer,
    UpdateTransferCompliance,
    ComputeDiscrepancyAmount,
    GetProductInfo,
    GetStoreInfo,
    GetEmployeeInfo,
    ListStoreSKUs,
    ListStoreEmployees,
    GetPromotionInfo,
    ListActivePromotions,
    GetCustomerInfo,
    ListStoreTransactions,
    GetTransactionDetails,
    FlagExpiredProducts,
    ApplyBulkDiscount,
    RestockLowInventory,
]
