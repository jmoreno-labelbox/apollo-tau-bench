# Copyright Sierra

from .find_user_id_by_name_zip import FindUserIdByNameZip
from .get_user_details import GetUserDetails
from .get_user_orders import GetUserOrders
from .update_user_address import UpdateUserAddress
from .get_user_payment_methods import GetUserPaymentMethods
from .get_order_details import GetOrderDetails
from .get_order_status import GetOrderStatus
from .update_order_status import UpdateOrderStatus
from .add_order_fulfillment import AddOrderFulfillment
from .get_order_payment_history import GetOrderPaymentHistory
from .get_product_details import GetProductDetails
from .get_variant_details import GetVariantDetails
from .list_available_variants import ListAvailableVariants
from .update_variant_availability import UpdateVariantAvailability
from .update_variant_price import UpdateVariantPrice
from .get_supplier_by_id import GetSupplierById
from .get_supplier_products import GetSupplierProducts
from .update_item_stock import UpdateItemStock
from .get_item_stock import GetItemStock
from .get_courier_by_id import GetCourierById
from .find_courier_by_tracking_id import FindCourierByTrackingId
from .assign_courier_to_order import AssignCourierToOrder
from .get_tracking_history import GetTrackingHistory
from .get_supply_order_details import GetSupplyOrderDetails
from .update_supply_order_status import UpdateSupplyOrderStatus
from .delete_supply_order import DeleteSupplyOrder

ALL_TOOLS = [
    FindUserIdByNameZip,
    GetUserDetails,
    GetUserOrders,
    UpdateUserAddress,
    GetUserPaymentMethods,
    GetOrderDetails,
    GetOrderStatus,
    UpdateOrderStatus,
    AddOrderFulfillment,
    GetOrderPaymentHistory,
    GetProductDetails,
    GetVariantDetails,
    ListAvailableVariants,
    UpdateVariantAvailability,
    UpdateVariantPrice,
    GetSupplierById,
    GetSupplierProducts,
    UpdateItemStock,
    GetItemStock,
    GetCourierById,
    FindCourierByTrackingId,
    AssignCourierToOrder,
    GetTrackingHistory,
    GetSupplyOrderDetails,
    UpdateSupplyOrderStatus,
    DeleteSupplyOrder,
]
