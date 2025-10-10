# Copyright owned by Sierra

from .get_contact_by_email import GetContactByEmail
from .get_product_by_name import GetProductByName
from .list_products_in_category import ListProductsInCategory
from .get_pricebook_by_name import GetPricebookByName
from .get_offer_by_code import GetOfferByCode
from .create_cart import CreateCart
from .add_item_to_cart import AddItemToCart
from .set_item_quantity import SetItemQuantity
from .remove_item_from_cart import RemoveItemFromCart
from .apply_offer_to_cart import ApplyOfferToCart
from .get_account_by_id import GetAccountById
from .preview_cart_totals import PreviewCartTotals
from .create_order import CreateOrder
from .list_order_items import ListOrderItems
from .set_order_shipping_address import SetOrderShippingAddress
from .cancel_order import CancelOrder
from .create_case import CreateCase
from .update_case_status import UpdateCaseStatus
from .refund_order_full import RefundOrderFull
from .refund_order_partial import RefundOrderPartial
from .list_elasti_cache_clusters import ListElastiCacheClusters
from .get_elasti_cache_cluster import GetElastiCacheCluster
from .provision_elasti_cache_cluster import ProvisionElastiCacheCluster
from .update_elasti_cache_instance_type import UpdateElastiCacheInstanceType
from .delete_elasti_cache_cluster import DeleteElastiCacheCluster
from .list_subnet_groups import ListSubnetGroups
from .create_subnet_group import CreateSubnetGroup
from .list_security_group_rules import ListSecurityGroupRules
from .add_security_group_rule import AddSecurityGroupRule
from .get_subnet_group import GetSubnetGroup
from .update_subnet_group_description import UpdateSubnetGroupDescription
from .update_elasti_cache_cluster_config import UpdateElastiCacheClusterConfig
from .get_contact_by_name import GetContactByName
from .list_orders_for_contact import ListOrdersForContact
from .list_active_offers import ListActiveOffers
from .get_default_pricebook_for_account import GetDefaultPricebookForAccount
from .validate_return_eligibility import ValidateReturnEligibility
from .list_carts_for_contact import ListCartsForContact
from .list_cart_items import ListCartItems
from .return_order import ReturnOrder

ALL_TOOLS = [
    GetContactByEmail,
    GetProductByName,
    ListProductsInCategory,
    GetPricebookByName,
    GetOfferByCode,
    CreateCart,
    AddItemToCart,
    SetItemQuantity,
    RemoveItemFromCart,
    ApplyOfferToCart,
    GetAccountById,
    PreviewCartTotals,
    CreateOrder,
    ListOrderItems,
    SetOrderShippingAddress,
    CancelOrder,
    CreateCase,
    UpdateCaseStatus,
    RefundOrderFull,
    RefundOrderPartial,
    ListElastiCacheClusters,
    GetElastiCacheCluster,
    ProvisionElastiCacheCluster,
    UpdateElastiCacheInstanceType,
    DeleteElastiCacheCluster,
    ListSubnetGroups,
    CreateSubnetGroup,
    ListSecurityGroupRules,
    AddSecurityGroupRule,
    GetSubnetGroup,
    UpdateSubnetGroupDescription,
    UpdateElastiCacheClusterConfig,
    GetContactByName,
    ListOrdersForContact,
    ListActiveOffers,
    GetDefaultPricebookForAccount,
    ValidateReturnEligibility,
    ListCartsForContact,
    ListCartItems,
    ReturnOrder,
]
