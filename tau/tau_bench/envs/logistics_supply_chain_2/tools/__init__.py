# Copyright Sierra

from .get_carrier_by_scac import GetCarrierBySCAC
from .get_active_carriers import GetActiveCarriers
from .get_carriers_by_region import GetCarriersByRegion
from .get_carriers_by_mode import GetCarriersByMode
from .get_top_rated_carriers import GetTopRatedCarriers
from .get_on_time_delivery_stats import GetOnTimeDeliveryStats
from .update_carrier import UpdateCarrier
from .get_shipment_by_id import GetShipmentById
from .get_shipments_by_status import GetShipmentsByStatus
from .get_delayed_shipments import GetDelayedShipments
from .filter_inbound_shipments import FilterInboundShipments
from .update_inbound_shipment import UpdateInboundShipment
from .get_inventory_by_id import GetInventoryById
from .get_inventory_below_reorder_point import GetInventoryBelowReorderPoint
from .get_inventory_by_warehouse import GetInventoryByWarehouse
from .get_expired_inventory import GetExpiredInventory
from .get_inventory_with_damage import GetInventoryWithDamage
from .filter_inventory import FilterInventory
from .update_inventory import UpdateInventory
from .get_outbound_order_by_id import GetOutboundOrderById
from .get_orders_by_status import GetOrdersByStatus
from .get_high_value_outbound_orders import GetHighValueOutboundOrders
from .get_orders_requiring_temperature_control import GetOrdersRequiringTemperatureControl
from .update_outbound_order import UpdateOutboundOrder
from .get_product_by_sku import GetProductBySKU
from .get_hazmat_products import GetHazmatProducts
from .get_products_by_category import GetProductsByCategory
from .get_products_by_storage_requirement import GetProductsByStorageRequirement
from .update_product import UpdateProduct
from .get_supplier_by_id import GetSupplierByID
from .get_preferred_suppliers import GetPreferredSuppliers
from .get_certified_suppliers import GetCertifiedSuppliers
from .update_supplier import UpdateSupplier
from .get_warehouse_by_id import GetWarehouseByID
from .get_warehouses_by_ownership_status import GetWarehousesByOwnershipStatus
from .update_warehouse import UpdateWarehouse
from .calculate_total import CalculateTotal
from .calculate_aggregate import CalculateAggregate
from .return_ids import ReturnIds

ALL_TOOLS = [
    GetCarrierBySCAC,
    GetActiveCarriers,
    GetCarriersByRegion,
    GetCarriersByMode,
    GetTopRatedCarriers,
    GetOnTimeDeliveryStats,
    UpdateCarrier,
    GetShipmentById,
    GetShipmentsByStatus,
    GetDelayedShipments,
    FilterInboundShipments,
    UpdateInboundShipment,
    GetInventoryById,
    GetInventoryBelowReorderPoint,
    GetInventoryByWarehouse,
    GetExpiredInventory,
    GetInventoryWithDamage,
    FilterInventory,
    UpdateInventory,
    GetOutboundOrderById,
    GetOrdersByStatus,
    GetHighValueOutboundOrders,
    GetOrdersRequiringTemperatureControl,
    UpdateOutboundOrder,
    GetProductBySKU,
    GetHazmatProducts,
    GetProductsByCategory,
    GetProductsByStorageRequirement,
    UpdateProduct,
    GetSupplierByID,
    GetPreferredSuppliers,
    GetCertifiedSuppliers,
    UpdateSupplier,
    GetWarehouseByID,
    GetWarehousesByOwnershipStatus,
    UpdateWarehouse,
    CalculateTotal,
    CalculateAggregate,
    ReturnIds,
]
