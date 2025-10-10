# Copyright owned by Sierra.

from .find_product_by_name import FindProductByName
from .add_cart_item import AddCartItem
from .add_security_group_rule import AddSecurityGroupRule
from .update_cache_cluster_status import UpdateCacheClusterStatus
from .get_customer_profile import GetCustomerProfile
from .search_products_by_category import SearchProductsByCategory
from .create_shopping_cart import CreateShoppingCart
from .apply_discount_bundle import ApplyDiscountBundle
from .process_order_with_fulfillment import ProcessOrderWithFulfillment
from .configure_cache_integration import ConfigureCacheIntegration
from .manage_connected_app_security import ManageConnectedAppSecurity
from .optimize_security_group_rules import OptimizeSecurityGroupRules
from .get_audit_log import GetAuditLog
from .manage_inventory_levels import ManageInventoryLevels
from .generate_promotional_campaign import GeneratePromotionalCampaign
from .configure_payment_gateway import ConfigurePaymentGateway
from .manage_customer_segments import ManageCustomerSegments
from .process_bulk_product_update import ProcessBulkProductUpdate
from .analyze_customer_behavior import AnalyzeCustomerBehavior
from .manage_supplier_relationships import ManageSupplierRelationships
from .process_customer_feedback import ProcessCustomerFeedback
from .configure_shipping_rules import ConfigureShippingRules
from .manage_product_recommendations import ManageProductRecommendations
from .process_loyalty_program import ProcessLoyaltyProgram
from .configure_content_delivery_network import ConfigureContentDeliveryNetwork
from .manage_api_rate_limits import ManageApiRateLimits
from .process_data_backup import ProcessDataBackup
from .get_data_backup_info import GetDataBackupInfo
from .get_next_cart_id import GetNextCartId
from .get_next_order_id import GetNextOrderId
from .get_cache_cluster_info import GetCacheClusterInfo
from .get_api_rate_limit_config import GetApiRateLimitConfig
from .get_connected_app_security import GetConnectedAppSecurity

ALL_TOOLS = [
    FindProductByName,
    AddCartItem,
    AddSecurityGroupRule,
    UpdateCacheClusterStatus,
    GetCustomerProfile,
    SearchProductsByCategory,
    CreateShoppingCart,
    ApplyDiscountBundle,
    ProcessOrderWithFulfillment,
    ConfigureCacheIntegration,
    ManageConnectedAppSecurity,
    OptimizeSecurityGroupRules,
    GetAuditLog,
    ManageInventoryLevels,
    GeneratePromotionalCampaign,
    ConfigurePaymentGateway,
    ManageCustomerSegments,
    ProcessBulkProductUpdate,
    AnalyzeCustomerBehavior,
    ManageSupplierRelationships,
    ProcessCustomerFeedback,
    ConfigureShippingRules,
    ManageProductRecommendations,
    ProcessLoyaltyProgram,
    ConfigureContentDeliveryNetwork,
    ManageApiRateLimits,
    ProcessDataBackup,
    GetDataBackupInfo,
    GetNextCartId,
    GetNextOrderId,
    GetCacheClusterInfo,
    GetApiRateLimitConfig,
    GetConnectedAppSecurity,
]
