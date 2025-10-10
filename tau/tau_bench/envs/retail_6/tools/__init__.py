# Copyright © Sierra

from .get_user_by_id import GetUserById
from .find_users_by_city import FindUsersByCity
from .update_user_address import UpdateUserAddress
from .add_payment_method import AddPaymentMethod
from .get_product_by_id import GetProductById
from .get_item_variant import GetItemVariant
from .set_variant_availability import SetVariantAvailability
from .set_variant_price import SetVariantPrice
from .search_products_by_name import SearchProductsByName
from .get_order_details import GetOrderDetails
from .update_order_status import UpdateOrderStatus
from .add_order_payment import AddOrderPayment
from .refund_order_payment import RefundOrderPayment
from .cancel_order_items import CancelOrderItems
from .update_item_option import UpdateItemOption
from .add_order_tag import AddOrderTag
from .compute_order_total import ComputeOrderTotal
from .get_tracking_info import GetTrackingInfo
from .append_tracking_event import AppendTrackingEvent
from .link_tracking_to_order import LinkTrackingToOrder
from .split_order_fulfillment import SplitOrderFulfillment
from .get_supplier_details import GetSupplierDetails
from .place_supply_order import PlaceSupplyOrder
from .update_supply_order_status import UpdateSupplyOrderStatus
from .get_courier_details import GetCourierDetails
from .reassign_courier_for_tracking import ReassignCourierForTracking
from .allocate_tracking_id import AllocateTrackingId
from .schedule_delivery import ScheduleDelivery
from .fraud_mark_order import FraudMarkOrder
from .compute_user_fill_rate import ComputeUserFillRate
from .upsert_tracking_address import UpsertTrackingAddress

ALL_TOOLS = [
    GetUserById,
    FindUsersByCity,
    UpdateUserAddress,
    AddPaymentMethod,
    GetProductById,
    GetItemVariant,
    SetVariantAvailability,
    SetVariantPrice,
    SearchProductsByName,
    GetOrderDetails,
    UpdateOrderStatus,
    AddOrderPayment,
    RefundOrderPayment,
    CancelOrderItems,
    UpdateItemOption,
    AddOrderTag,
    ComputeOrderTotal,
    GetTrackingInfo,
    AppendTrackingEvent,
    LinkTrackingToOrder,
    SplitOrderFulfillment,
    GetSupplierDetails,
    PlaceSupplyOrder,
    UpdateSupplyOrderStatus,
    GetCourierDetails,
    ReassignCourierForTracking,
    AllocateTrackingId,
    ScheduleDelivery,
    FraudMarkOrder,
    ComputeUserFillRate,
    UpsertTrackingAddress,
]
