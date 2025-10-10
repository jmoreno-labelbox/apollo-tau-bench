# Copyright owned by Sierra

from .get_inventory_by_sku_warehouse import GetInventoryBySkuWarehouse
from .create_purchase_order import CreatePurchaseOrder
from .search_inbound_shipments import SearchInboundShipments
from .get_order_details import GetOrderDetails
from .verify_inventory_allocation import VerifyInventoryAllocation
from .select_optimal_carrier import SelectOptimalCarrier
from .generate_shipping_labels import GenerateShippingLabels
from .update_order_status import UpdateOrderStatus
from .get_shipment_details import GetShipmentDetails
from .verify_customs_documentation import VerifyCustomsDocumentation
from .calculate_customs_duty import CalculateCustomsDuty
from .process_duty_payment import ProcessDutyPayment
from .update_customs_status import UpdateCustomsStatus
from .update_shipment_status import UpdateShipmentStatus
from .get_supplier_performance import GetSupplierPerformance
from .create_supplier_improvement_plan import CreateSupplierImprovementPlan
from .search_purchase_orders import SearchPurchaseOrders
from .get_inventory_details import GetInventoryDetails
from .perform_physical_count import PerformPhysicalCount
from .calculate_inventory_variance import CalculateInventoryVariance
from .create_inventory_adjustment import CreateInventoryAdjustment
from .update_accuracy_metrics import UpdateAccuracyMetrics
from .get_carrier_performance import GetCarrierPerformance
from .request_shipping_quote import RequestShippingQuote
from .get_warehouse_capacity import GetWarehouseCapacity
from .calculate_utilization_percentage import CalculateUtilizationPercentage
from .analyze_inventory_by_category import AnalyzeInventoryByCategory
from .identify_overflow_options import IdentifyOverflowOptions
from .create_capacity_plan import CreateCapacityPlan
from .quarantine_inventory import QuarantineInventory
from .check_temperature_logs import CheckTemperatureLogs
from .verify_cold_chain_integrity import VerifyColdChainIntegrity
from .initiate_product_recall import InitiateProductRecall
from .create_incident_report import CreateIncidentReport
from .notify_supplier import NotifySupplier
from .get_approved_suppliers import GetApprovedSuppliers
from .calculate_financial_impact import CalculateFinancialImpact
from .escalate_to_quality_team import EscalateToQualityTeam
from .verify_storage_compliance import VerifyStorageCompliance

ALL_TOOLS = [
    GetInventoryBySkuWarehouse,
    CreatePurchaseOrder,
    SearchInboundShipments,
    GetOrderDetails,
    VerifyInventoryAllocation,
    SelectOptimalCarrier,
    GenerateShippingLabels,
    UpdateOrderStatus,
    GetShipmentDetails,
    VerifyCustomsDocumentation,
    CalculateCustomsDuty,
    ProcessDutyPayment,
    UpdateCustomsStatus,
    UpdateShipmentStatus,
    GetSupplierPerformance,
    CreateSupplierImprovementPlan,
    SearchPurchaseOrders,
    GetInventoryDetails,
    PerformPhysicalCount,
    CalculateInventoryVariance,
    CreateInventoryAdjustment,
    UpdateAccuracyMetrics,
    GetCarrierPerformance,
    RequestShippingQuote,
    GetWarehouseCapacity,
    CalculateUtilizationPercentage,
    AnalyzeInventoryByCategory,
    IdentifyOverflowOptions,
    CreateCapacityPlan,
    QuarantineInventory,
    CheckTemperatureLogs,
    VerifyColdChainIntegrity,
    InitiateProductRecall,
    CreateIncidentReport,
    NotifySupplier,
    GetApprovedSuppliers,
    CalculateFinancialImpact,
    EscalateToQualityTeam,
    VerifyStorageCompliance,
]
