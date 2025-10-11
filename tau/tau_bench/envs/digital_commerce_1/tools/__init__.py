# Copyright Sierra



# Utility function
def _ensure_table(data, table_name):
    """Ensure table exists in data, create if missing."""
    if table_name not in data:
        data[table_name] = {}
    return data[table_name]



# Utility function
def _get_network_defaults():
    """Get default network configuration."""
    return {
        "cidr_block": "10.0.0.0/16",
        "availability_zone": "us-east-1a",
        "enable_dns_support": True,
        "enable_dns_hostnames": True
    }


def _find_all(items, **filters):
    """Find all items matching filters."""
    if not filters:
        return items
    
    results = []
    for item in items:
        match = True
        for key, value in filters.items():
            if item.get(key) != value:
                match = False
                break
        if match:
            results.append(item)
    return results


from .get_environment_network_defaults import GetEnvironmentNetworkDefaults
from .get_service_security_group import GetServiceSecurityGroup
from .update_security_group_ruleset import UpdateSecurityGroupRuleset
from .provision_or_update_redis_cluster import ProvisionOrUpdateRedisCluster
from .set_redis_auth_and_tls import SetRedisAuthAndTLS
from .create_interface_endpoint import CreateInterfaceEndpoint
from .create_secret_for import CreateSecretFor
from .configure_cache_integration import ConfigureCacheIntegration
from .run_cache_warm_jobs import RunCacheWarmJobs
from .set_cache_partition_key import SetCachePartitionKey
from .manage_cache_maintenance import ManageCacheMaintenance
from .configure_trace_sampling import ConfigureTraceSampling
from .enable_digital_commerce_gateway import EnableDigitalCommerceGateway
from .configure_connected_app_o_auth import ConfigureConnectedAppOAuth
from .publish_open_api_spec import PublishOpenAPISpec
from .register_api_endpoints import RegisterApiEndpoints
from .run_test_collection import RunTestCollection
from .record_api_change_log import RecordApiChangeLog
from .deploy_lambda_function import DeployLambdaFunction
from .create_lambda_schedule import CreateLambdaSchedule
from .create_cloud_watch_alarm import CreateCloudWatchAlarm
from .create_cloud_watch_dashboard import CreateCloudWatchDashboard
from .invalidate_cache_by_keys import InvalidateCacheByKeys
from .resolve_catalog_entities import ResolveCatalogEntities
from .upsert_pricebook_entries_batch import UpsertPricebookEntriesBatch
from .upsert_offer import UpsertOffer
from .set_pricing_tier_for_customer import SetPricingTierForCustomer
from .create_cart_with_items import CreateCartWithItems
from .upsert_promotion import UpsertPromotion
from .upsert_context_rule import UpsertContextRule
from .get_cache_cluster import GetCacheCluster
from .get_offer_by_code import GetOfferByCode
from .get_pricebook_by_name import GetPricebookByName
from .get_product_by_name import GetProductByName
from .get_security_group_rules import GetSecurityGroupRules
from .verify_o_auth_redirect_domain import VerifyOAuthRedirectDomain
from .register_o_auth_trusted_audience import RegisterOAuthTrustedAudience

ALL_TOOLS = [
    GetEnvironmentNetworkDefaults,
    GetServiceSecurityGroup,
    UpdateSecurityGroupRuleset,
    ProvisionOrUpdateRedisCluster,
    SetRedisAuthAndTLS,
    CreateInterfaceEndpoint,
    CreateSecretFor,
    ConfigureCacheIntegration,
    RunCacheWarmJobs,
    SetCachePartitionKey,
    ManageCacheMaintenance,
    ConfigureTraceSampling,
    EnableDigitalCommerceGateway,
    ConfigureConnectedAppOAuth,
    PublishOpenAPISpec,
    RegisterApiEndpoints,
    RunTestCollection,
    RecordApiChangeLog,
    DeployLambdaFunction,
    CreateLambdaSchedule,
    CreateCloudWatchAlarm,
    CreateCloudWatchDashboard,
    InvalidateCacheByKeys,
    ResolveCatalogEntities,
    UpsertPricebookEntriesBatch,
    UpsertOffer,
    SetPricingTierForCustomer,
    CreateCartWithItems,
    UpsertPromotion,
    UpsertContextRule,
    GetCacheCluster,
    GetOfferByCode,
    GetPricebookByName,
    GetProductByName,
    GetSecurityGroupRules,
    VerifyOAuthRedirectDomain,
    RegisterOAuthTrustedAudience,
]
