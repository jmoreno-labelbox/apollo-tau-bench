# Copyright Sierra

from .create_order_tool import CreateOrderTool
from .append_payment_tool import AppendPaymentTool
from .assign_courier_and_create_tracking_tool import AssignCourierAndCreateTrackingTool
from .advance_tracking_status_tool import AdvanceTrackingStatusTool
from .cancel_order_and_refund_tool import CancelOrderAndRefundTool
from .add_items_to_order_tool import AddItemsToOrderTool
from .remove_items_by_index_tool import RemoveItemsByIndexTool
from .set_order_status_tool import SetOrderStatusTool
from .link_existing_tracking_to_order_tool import LinkExistingTrackingToOrderTool
from .create_supply_order_tool import CreateSupplyOrderTool
from .set_supply_order_status_tool import SetSupplyOrderStatusTool
from .append_supply_order_event_tool import AppendSupplyOrderEventTool
from .get_order_financials_tool import GetOrderFinancialsTool
from .find_orders_by_user_and_status_tool import FindOrdersByUserAndStatusTool
from .attach_courier_by_name_tool import AttachCourierByNameTool
from .update_tracking_courier_tool import UpdateTrackingCourierTool
from .add_tracking_custom_event_tool import AddTrackingCustomEventTool
from .find_tracking_by_order_tool import FindTrackingByOrderTool
from .find_supply_orders_tool import FindSupplyOrdersTool
from .split_order_into_shipments_tool import SplitOrderIntoShipmentsTool
from .merge_orders_for_same_user_tool import MergeOrdersForSameUserTool
from .reopen_cancelled_order_tool import ReopenCancelledOrderTool
from .replace_item_variant_in_order_tool import ReplaceItemVariantInOrderTool
from .auto_approve_supply_order_tool import AutoApproveSupplyOrderTool
from .duplicate_order_tool import DuplicateOrderTool
from .remove_payment_by_index_tool import RemovePaymentByIndexTool
from .append_alternate_tracking_id_tool import AppendAlternateTrackingIdTool
from .reassign_tracking_to_new_courier_tool import ReassignTrackingToNewCourierTool
from .receive_supply_order_and_close_tool import ReceiveSupplyOrderAndCloseTool
from .update_product_variant_price_tool import UpdateProductVariantPriceTool

ALL_TOOLS = [
    CreateOrderTool,
    AppendPaymentTool,
    AssignCourierAndCreateTrackingTool,
    AdvanceTrackingStatusTool,
    CancelOrderAndRefundTool,
    AddItemsToOrderTool,
    RemoveItemsByIndexTool,
    SetOrderStatusTool,
    LinkExistingTrackingToOrderTool,
    CreateSupplyOrderTool,
    SetSupplyOrderStatusTool,
    AppendSupplyOrderEventTool,
    GetOrderFinancialsTool,
    FindOrdersByUserAndStatusTool,
    AttachCourierByNameTool,
    UpdateTrackingCourierTool,
    AddTrackingCustomEventTool,
    FindTrackingByOrderTool,
    FindSupplyOrdersTool,
    SplitOrderIntoShipmentsTool,
    MergeOrdersForSameUserTool,
    ReopenCancelledOrderTool,
    ReplaceItemVariantInOrderTool,
    AutoApproveSupplyOrderTool,
    DuplicateOrderTool,
    RemovePaymentByIndexTool,
    AppendAlternateTrackingIdTool,
    ReassignTrackingToNewCourierTool,
    ReceiveSupplyOrderAndCloseTool,
    UpdateProductVariantPriceTool,
]
