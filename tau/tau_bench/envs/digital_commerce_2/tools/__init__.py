# Copyright Sierra


# Utility function
def _money(amount):
    """Format amount as money string."""
    return f"${amount:.2f}"


def _idstr(prefix, items, id_key='id'):
    """Generate next ID with prefix (e.g., 'USR-001', 'USR-002')."""
    max_num = 0
    for item in items:
        item_id = str(item.get(id_key, ''))
        if item_id.startswith(prefix + '-'):
            try:
                num = int(item_id.split('-')[-1])
                max_num = max(max_num, num)
            except (ValueError, IndexError):
                pass
    return f"{prefix}-{max_num + 1:03d}"


from .get_account_by_id import GetAccountById
from .get_account_by_name import GetAccountByName
from .update_street_address import UpdateStreetAddress
from .get_contact_by_name import GetContactByName
from .get_orders_by_contact_id import GetOrdersByContactId
from .add_stock_quantities import AddStockQuantities
from .get_price_of_product import GetPriceOfProduct
from .create_new_offer import CreateNewOffer
from .deactivate_offer import DeactivateOffer
from .get_offer_details import GetOfferDetails
from .get_cart_by_contact_id import GetCartByContactId
from .get_all_items_in_cart import GetAllItemsInCart
from .clear_cart import ClearCart
from .get_order_details_by_id import GetOrderDetailsById
from .update_order_status import UpdateOrderStatus
from .get_all_order_items_by_order_id import GetAllOrderItemsByOrderId
from .create_new_case import CreateNewCase
from .update_case_status import UpdateCaseStatus
from .calculate_sub_total_price import CalculateSubTotalPrice
from .calclulate_discount_flat import CalclulateDiscountFlat
from .calculate_discount_percent import CalculateDiscountPercent
from .get_products_by_names import GetProductsByNames
from .add_items_to_cart_batch import AddItemsToCartBatch
from .update_items_in_cart_batch import UpdateItemsInCartBatch
from .remove_items_from_cart_batch import RemoveItemsFromCartBatch
from .verify_order_from_stock import VerifyOrderFromStock
from .apply_offer_to_subtotal import ApplyOfferToSubtotal
from .get_or_create_cart import GetOrCreateCart
from .inventory_security_group_rules import InventorySecurityGroupRules
from .get_security_group_rule_by_id import GetSecurityGroupRuleById
from .update_subnet_group_description import UpdateSubnetGroupDescription
from .create_ingress_change_plan import CreateIngressChangePlan
from .apply_ingress_plan_step import ApplyIngressPlanStep
from .create_cluster_change_plan import CreateClusterChangePlan
from .apply_cluster_plan_step import ApplyClusterPlanStep
from .set_trace_flag import SetTraceFlag
from .run_cache_job import RunCacheJob
from .upsert_custom_setting import UpsertCustomSetting
from .build_bearer_for_connected_app import BuildBearerForConnectedApp
from .ensure_connected_app import EnsureConnectedApp
from .get_connected_app_by_name import GetConnectedAppByName
from .get_org_by_name import GetOrgByName
from .price_and_apply_offer_by_names import PriceAndApplyOfferByNames

ALL_TOOLS = [
    GetAccountById,
    GetAccountByName,
    UpdateStreetAddress,
    GetContactByName,
    GetOrdersByContactId,
    AddStockQuantities,
    GetPriceOfProduct,
    CreateNewOffer,
    DeactivateOffer,
    GetOfferDetails,
    GetCartByContactId,
    GetAllItemsInCart,
    ClearCart,
    GetOrderDetailsById,
    UpdateOrderStatus,
    GetAllOrderItemsByOrderId,
    CreateNewCase,
    UpdateCaseStatus,
    CalculateSubTotalPrice,
    CalclulateDiscountFlat,
    CalculateDiscountPercent,
    GetProductsByNames,
    AddItemsToCartBatch,
    UpdateItemsInCartBatch,
    RemoveItemsFromCartBatch,
    VerifyOrderFromStock,
    ApplyOfferToSubtotal,
    GetOrCreateCart,
    InventorySecurityGroupRules,
    GetSecurityGroupRuleById,
    UpdateSubnetGroupDescription,
    CreateIngressChangePlan,
    ApplyIngressPlanStep,
    CreateClusterChangePlan,
    ApplyClusterPlanStep,
    SetTraceFlag,
    RunCacheJob,
    UpsertCustomSetting,
    BuildBearerForConnectedApp,
    EnsureConnectedApp,
    GetConnectedAppByName,
    GetOrgByName,
    PriceAndApplyOfferByNames,
]
