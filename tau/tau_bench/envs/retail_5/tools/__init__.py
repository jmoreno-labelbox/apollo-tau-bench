# Copyright owned by Sierra


# Utility function
import uuid

def generate_unique_id():
    """Generate a unique ID."""
    return uuid.uuid4().hex[:8]

from .search_products_by_category import SearchProductsByCategory
from .get_order_details import GetOrderDetails
from .get_user_orders import GetUserOrders
from .update_order_status import UpdateOrderStatus
from .check_product_availability import CheckProductAvailability
from .get_tracking_info import GetTrackingInfo
from .get_supplier_info import GetSupplierInfo
from .get_stock_levels import GetStockLevels
from .create_supply_order import CreateSupplyOrder
from .get_courier_info import GetCourierInfo
from .search_users import SearchUsers
from .process_return import ProcessReturn
from .update_inventory import UpdateInventory
from .get_orders_by_status import GetOrdersByStatus
from .get_pending_supply_orders import GetPendingSupplyOrders
from .update_supply_order_status import UpdateSupplyOrderStatus
from .get_top_selling_products import GetTopSellingProducts
from .update_tracking_status import UpdateTrackingStatus
from .get_revenue_summary import GetRevenueSummary
from .get_user_revenue_summary import GetUserRevenueSummary
from .validate_order_items import ValidateOrderItems
from .get_delivery_estimate import GetDeliveryEstimate
from .analyze_customer_purchase_history import AnalyzeCustomerPurchaseHistory
from .create_recommendations import CreateRecommendations
from .bulk_order_processing import BulkOrderProcessing
from .inventory_alert import InventoryAlert
from .create_promotional_campaign import CreatePromotionalCampaign
from .update_user_address import UpdateUserAddress
from .add_payment_method_to_user import AddPaymentMethodToUser
from .cancel_order_item import CancelOrderItem
from .update_order_item_price import UpdateOrderItemPrice
from .create_pending_order import CreatePendingOrder
from .apply_payment_to_order import ApplyPaymentToOrder
from .assign_fulfillment_to_order import AssignFulfillmentToOrder
from .adjust_order_payment import AdjustOrderPayment
from .get_product_details import GetProductDetails
from .update_product_price import UpdateProductPrice
from .list_products_by_supplier import ListProductsBySupplier
from .update_supplier_contact import UpdateSupplierContact
from .list_all_suppliers import ListAllSuppliers
from .get_product_by_item_id import GetProductByItemId
from .get_supply_order_details import GetSupplyOrderDetails
from .list_supply_orders_by_status import ListSupplyOrdersByStatus
from .update_supply_order_quantity import UpdateSupplyOrderQuantity
from .get_product_supplier_summary import GetProductSupplierSummary
from .get_supplier_order_history import GetSupplierOrderHistory

ALL_TOOLS = [
    SearchProductsByCategory,
    GetOrderDetails,
    GetUserOrders,
    UpdateOrderStatus,
    CheckProductAvailability,
    GetTrackingInfo,
    GetSupplierInfo,
    GetStockLevels,
    CreateSupplyOrder,
    GetCourierInfo,
    SearchUsers,
    ProcessReturn,
    UpdateInventory,
    GetOrdersByStatus,
    GetPendingSupplyOrders,
    UpdateSupplyOrderStatus,
    GetTopSellingProducts,
    UpdateTrackingStatus,
    GetRevenueSummary,
    GetUserRevenueSummary,
    ValidateOrderItems,
    GetDeliveryEstimate,
    AnalyzeCustomerPurchaseHistory,
    CreateRecommendations,
    BulkOrderProcessing,
    InventoryAlert,
    CreatePromotionalCampaign,
    UpdateUserAddress,
    AddPaymentMethodToUser,
    CancelOrderItem,
    UpdateOrderItemPrice,
    CreatePendingOrder,
    ApplyPaymentToOrder,
    AssignFulfillmentToOrder,
    AdjustOrderPayment,
    GetProductDetails,
    UpdateProductPrice,
    ListProductsBySupplier,
    UpdateSupplierContact,
    ListAllSuppliers,
    GetProductByItemId,
    GetSupplyOrderDetails,
    ListSupplyOrdersByStatus,
    UpdateSupplyOrderQuantity,
    GetProductSupplierSummary,
    GetSupplierOrderHistory,
]
