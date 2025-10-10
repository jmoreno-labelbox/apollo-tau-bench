# Copyright owned by Sierra

from .find_product_by_name import FindProductByName
from .get_product_details import GetProductDetails
from .find_warehouse_by_name import FindWarehouseByName
from .get_warehouse_details import GetWarehouseDetails
from .get_all_warehouses import GetAllWarehouses
from .get_inventory_details import GetInventoryDetails
from .find_carrier_by_method_of_transport import FindCarrierByMethodOfTransport
from .find_carrier_by_service import FindCarrierByService
from .calculate_expected_arrival_date import CalculateExpectedArrivalDate
from .find_supplier_by_name import FindSupplierByName
from .find_inventory_by_sku import FindInventoryBySku
from .find_inbound_shipments_by_warehouse import FindInboundShipmentsByWarehouse
from .get_supplier_details import GetSupplierDetails
from .find_inbound_shipments_by_supplier import FindInboundShipmentsBySupplier
from .find_cheapest_carrier_by_service import FindCheapestCarrierByService
from .find_outbound_order_by_so import FindOutboundOrderBySO
from .get_all_outbound_orders import GetAllOutboundOrders
from .get_carrier_details_by_name import GetCarrierDetailsByName
from .create_inbound_shipment import CreateInboundShipment
from .update_inventory_inbound_quantity import UpdateInventoryInboundQuantity
from .update_inventory_allocated_quantity import UpdateInventoryAllocatedQuantity
from .create_outbound_order import CreateOutboundOrder
from .update_shipment_notes import UpdateShipmentNotes
from .update_inventory_status import UpdateInventoryStatus
from .perform_inventory_adjustment import PerformInventoryAdjustment
from .update_outbound_order_details import UpdateOutboundOrderDetails
from .create_inventory_record import CreateInventoryRecord

ALL_TOOLS = [
    FindProductByName,
    GetProductDetails,
    FindWarehouseByName,
    GetWarehouseDetails,
    GetAllWarehouses,
    GetInventoryDetails,
    FindCarrierByMethodOfTransport,
    FindCarrierByService,
    CalculateExpectedArrivalDate,
    FindSupplierByName,
    FindInventoryBySku,
    FindInboundShipmentsByWarehouse,
    GetSupplierDetails,
    FindInboundShipmentsBySupplier,
    FindCheapestCarrierByService,
    FindOutboundOrderBySO,
    GetAllOutboundOrders,
    GetCarrierDetailsByName,
    CreateInboundShipment,
    UpdateInventoryInboundQuantity,
    UpdateInventoryAllocatedQuantity,
    CreateOutboundOrder,
    UpdateShipmentNotes,
    UpdateInventoryStatus,
    PerformInventoryAdjustment,
    UpdateOutboundOrderDetails,
    CreateInventoryRecord,
]
