# Copyright © Sierra

from .get_contact_by_email import GetContactByEmail
from .get_product_by_name import GetProductByName
from .list_products_in_category import ListProductsInCategory
from .get_offer_by_code import GetOfferByCode
from .create_cart import CreateCart
from .add_item_to_cart import AddItemToCart
from .set_item_quantity import SetItemQuantity
from .remove_item_from_cart import RemoveItemFromCart
from .apply_offer_to_cart import ApplyOfferToCart
from .switch_cart_pricebook import SwitchCartPricebook
from .preview_cart_totals import PreviewCartTotals
from .create_order import CreateOrder
from .list_order_items import ListOrderItems
from .set_order_shipping_address import SetOrderShippingAddress
from .cancel_order import CancelOrder
from .return_order import ReturnOrder
from .create_case import CreateCase
from .update_case_status import UpdateCaseStatus
from .refund_order_full import RefundOrderFull
from .refund_order_partial import RefundOrderPartial
from .list_elasti_cache_clusters import ListElastiCacheClusters
from .get_elasti_cache_cluster import GetElastiCacheCluster
from .provision_elasti_cache_cluster import ProvisionElastiCacheCluster
from .update_elasti_cache_cluster_status import UpdateElastiCacheClusterStatus
from .list_subnet_groups import ListSubnetGroups
from .create_subnet_group import CreateSubnetGroup
from .create_account import CreateAccount
from .list_security_group_rules import ListSecurityGroupRules
from .add_security_group_rule import AddSecurityGroupRule
from .get_subnet_group import GetSubnetGroup
from .update_elasti_cache_cluster_config import UpdateElastiCacheClusterConfig
from .get_account_by_id import GetAccountById

ALL_TOOLS = [
    GetContactByEmail,
    GetProductByName,
    ListProductsInCategory,
    GetOfferByCode,
    CreateCart,
    AddItemToCart,
    SetItemQuantity,
    RemoveItemFromCart,
    ApplyOfferToCart,
    SwitchCartPricebook,
    PreviewCartTotals,
    CreateOrder,
    ListOrderItems,
    SetOrderShippingAddress,
    CancelOrder,
    ReturnOrder,
    CreateCase,
    UpdateCaseStatus,
    RefundOrderFull,
    RefundOrderPartial,
    ListElastiCacheClusters,
    GetElastiCacheCluster,
    ProvisionElastiCacheCluster,
    UpdateElastiCacheClusterStatus,
    ListSubnetGroups,
    CreateSubnetGroup,
    CreateAccount,
    ListSecurityGroupRules,
    AddSecurityGroupRule,
    GetSubnetGroup,
    UpdateElastiCacheClusterConfig,
    GetAccountById,
]
