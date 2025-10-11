# Copyright Sierra

from .get_product_by_sku import GetProductBySku
from .find_products import FindProducts
from .get_inventory_by_sku import GetInventoryBySku
from .get_inventory_in_warehouse import GetInventoryInWarehouse
from .adjust_inventory import AdjustInventory
from .create_outbound_order import CreateOutboundOrder
from .get_outbound_order_status import GetOutboundOrderStatus
from .update_outbound_order_status import UpdateOutboundOrderStatus
from .cancel_outbound_order import CancelOutboundOrder
from .get_inbound_shipment_details import GetInboundShipmentDetails
from .find_inbound_shipments import FindInboundShipments
from .create_inbound_shipment import CreateInboundShipment
from .receive_inbound_shipment import ReceiveInboundShipment
from .get_carrier_details import GetCarrierDetails
from .find_carriers import FindCarriers
from .get_supplier_info import GetSupplierInfo
from .find_suppliers import FindSuppliers
from .get_warehouse_info import GetWarehouseInfo
from .find_warehouses import FindWarehouses
from .update_outbound_order_items import UpdateOutboundOrderItems
from .update_inbound_shipment import UpdateInboundShipment

ALL_TOOLS = [
    GetProductBySku,
    FindProducts,
    GetInventoryBySku,
    GetInventoryInWarehouse,
    AdjustInventory,
    CreateOutboundOrder,
    GetOutboundOrderStatus,
    UpdateOutboundOrderStatus,
    CancelOutboundOrder,
    GetInboundShipmentDetails,
    FindInboundShipments,
    CreateInboundShipment,
    ReceiveInboundShipment,
    GetCarrierDetails,
    FindCarriers,
    GetSupplierInfo,
    FindSuppliers,
    GetWarehouseInfo,
    FindWarehouses,
    UpdateOutboundOrderItems,
    UpdateInboundShipment,
]
