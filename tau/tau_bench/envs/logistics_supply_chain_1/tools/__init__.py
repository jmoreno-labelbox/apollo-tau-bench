# Copyright Sierra

from .get_product_details import GetProductDetails
from .list_warehouses_by_capability import ListWarehousesByCapability
from .get_inventory_by_sku import GetInventoryBySku
from .list_carriers_by_mode import ListCarriersByMode
from .create_outbound_order import CreateOutboundOrder
from .ship_outbound_order import ShipOutboundOrder
from .find_inbound_shipment import FindInboundShipment
from .update_shipment_status import UpdateShipmentStatus
from .log_supplier_performance_issue import LogSupplierPerformanceIssue
from .get_warehouse_details import GetWarehouseDetails
from .initiate_warehouse_transfer import InitiateWarehouseTransfer
from .update_warehouse_notes import UpdateWarehouseNotes
from .find_orders_by_carrier import FindOrdersByCarrier
from .reassign_order_carrier import ReassignOrderCarrier
from .log_audit_trail import LogAuditTrail
from .update_carrier_status import UpdateCarrierStatus
from .get_outbound_order_details import GetOutboundOrderDetails
from .get_inventory_details import GetInventoryDetails
from .get_carrier_details import GetCarrierDetails
from .update_inventory_damage_status import UpdateInventoryDamageStatus
from .create_purchase_order import CreatePurchaseOrder
from .get_purchase_order_details import GetPurchaseOrderDetails
from .get_outbound_order_details_by_so import GetOutboundOrderDetailsBySo
from .create_return_authorization import CreateReturnAuthorization
from .create_inbound_return_shipment import CreateInboundReturnShipment
from .update_outbound_order_status import UpdateOutboundOrderStatus
from .issue_customer_credit_memo import IssueCustomerCreditMemo
from .get_return_authorization_details import GetReturnAuthorizationDetails
from .get_credit_memo_details import GetCreditMemoDetails
from .get_kit_components import GetKitComponents

ALL_TOOLS = [
    GetProductDetails,
    ListWarehousesByCapability,
    GetInventoryBySku,
    ListCarriersByMode,
    CreateOutboundOrder,
    ShipOutboundOrder,
    FindInboundShipment,
    UpdateShipmentStatus,
    LogSupplierPerformanceIssue,
    GetWarehouseDetails,
    InitiateWarehouseTransfer,
    UpdateWarehouseNotes,
    FindOrdersByCarrier,
    ReassignOrderCarrier,
    LogAuditTrail,
    UpdateCarrierStatus,
    GetOutboundOrderDetails,
    GetInventoryDetails,
    GetCarrierDetails,
    UpdateInventoryDamageStatus,
    CreatePurchaseOrder,
    GetPurchaseOrderDetails,
    GetOutboundOrderDetailsBySo,
    CreateReturnAuthorization,
    CreateInboundReturnShipment,
    UpdateOutboundOrderStatus,
    IssueCustomerCreditMemo,
    GetReturnAuthorizationDetails,
    GetCreditMemoDetails,
    GetKitComponents,
]
