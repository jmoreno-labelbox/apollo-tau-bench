# Copyright Sierra

tasks = [
    {
        "annotator": aws_v1,
        "user_id": "task_A01",
        "instruction": "You are Priya Shah from Platform. In UAT, aim to limit the Commerce API service to '10.0.0.0/16' on Redis 6379 while maintaining the existing cache cluster 'dcomm-uat-redis'. Ensure that AUTH/TLS are enabled and that Commerce is directed at that cache using the returned secret, with partition key 'dcomm-uat'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "cluster_id: dcomm-uat-redis",
                "endpoint_url: dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                "sg_id: sg-uat-commerce-api",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A02",
        "instruction": "You are Dana Brooks from API. In UAT, deploy 'Catalog v3' version '3.1.0' from 'blob_901' to 'catalog-v3' with baseline monitoring on the gateway and a sampling rate of 0.10, ensure offer discovery is accessible (GET /v3/offers), conduct 'Catalog-v3-SMOKE', and log the rollout for 'spec-catalog-v3-3-1-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.0",
                    "spec_blob_id": "blob_901"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "catalog-v3",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-catalog-v3-3-1-0",
                    "gateway_id": "dcg-catalog-v3-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "collection_name": "Catalog-v3-SMOKE",
                    "environment": "UAT"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "change_type": "rollout",
                    "target_id": "spec-catalog-v3-3-1-0",
                    "environment": "UAT"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-catalog-v3-3-1-0",
                "dcg_id: dcg-catalog-v3-uat",
                "run_id: run-catalog-v3-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A03",
        "instruction": "You are Rafael Kim from SRE. In UAT, you intend to keep the 'Commerce API' cache warm every 15 minutes and monitor it for any failures. Apply the bundle 'bundle_cachewarmer_v1' for a 'cache_warmer' function and set an alarm on the ARN 'arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat'. Incorporate a 'cache' dashboard, execute a 'SMOKE' test run, perform a quick metadata warm, and document the change for 'fn-commerce-api-cache_warmer-uat'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A04",
        "instruction": "You are Sam Lee from Commerce Ops. In UAT, ensure the 'Checkout Gateway' is secured to the UAT allowlist and process a cart for 'sam@example.com' for 'USB-C Hub'. Utilize the existing promotion 'WINTER20' and choose 'STANDARD' shipping.",
        "actions": [
            {
                "name": "GetEnvironmentNetworkDefaults",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "sam@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WINTER20",
                    "shipping_method": "STANDARD"
                }
            }
        ],
        "outputs": [
                "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A05",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, ensure 'david.c@email.com' is on the 'B2B Wholesale' tier and create a cart with 2\u00d7 'USB-C Hub' (AC-USBC-HUB) and 1\u00d7 'Thunderbolt Docking Station' (HW-TB-DOCK) using 'B2BVOLUME15' promotion and STANDARD shipping. Document the change for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 2
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-david-c-email-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A06",
        "instruction": "As Omar Kelly from Performance, in UAT you need to upgrade the cache partition for the UAT cache cluster 'dcomm-uat-redis' to 'v4' and remove outdated entries for 'offer:Crosstrek' and 'offer:Dock4K'. Schedule nightly cache maintenance, initiate a quick metadata warm, set sampling at 0.15, establish a 'cache' dashboard, and monitor for alerts if the cache hit rate falls below 75.0 in five-minute intervals.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm-uat-redis",
                    "version": "v4"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:Crosstrek",
                        "offer:Dock4K"
                    ]
                },
            },
            {
                "name": "ManageCacheMaintenance",
                "arguments": {
                    "environment": "UAT",
                    "action": "create"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.15
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 75.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                }
            }
        ],
        "outputs": [
                "applied_version: v4",
                "schedule_id: cm-uat",
                "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A07",
        "instruction": "As Luis Ortega from Identity, configure the 'Commerce API' connected app in UAT with scopes api, refresh_token, openid and callback https://acme.example/callback. Execute 'OAuth-Smoke', document it under 'oauth', and securely store the secret for 'OAUTH_CLIENT_SECRET'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Commerce API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://acme.example/callback"
                    ]
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "collection_name": "OAuth-Smoke",
                    "environment": "UAT"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "change_type": "oauth",
                    "target_id": "app-commerce-api",
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api"
                }
            }
        ],
        "outputs": [
                "app_id: app-commerce-api",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "secret_arn: arn:secret-secret-oauth_client_secret-uat-app-commerce-api-alias-dcomm-uat"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A08",
        "instruction": "As Dana Brooks, API Lead, deploy 'Checkout v2' version '2.0.0' from 'blob_checkout_v2', activate 'checkout-v2', register the necessary endpoints, perform 'Checkout-v2-SMOKE', develop an 'api' dashboard, and configure a '5xxErrorRate' alarm at 1.0 over 300 using 'GreaterThanOrEqualToThreshold' in UAT.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Checkout v2",
                    "spec_version": "2.0.0",
                    "spec_blob_id": "blob_checkout_v2"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "checkout-v2",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-checkout-v2-2-0-0",
                    "gateway_id": "dcg-checkout-v2-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "collection_name": "Checkout-v2-SMOKE",
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-checkout-v2-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-checkout-v2-2-0-0",
                "dcg_id: dcg-checkout-v2-uat",
                "run_id: run-checkout-v2-smoke-uat-2025-08-06t12-00-00z",
                "alarm_id: al-dcg-checkout-v2-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A09",
        "instruction": "As Amira Patel from Networking, ensure ElastiCache is accessible privately in VPC 'vpc-prod-0001' across the subnets 'subnet-prod-a' and 'subnet-prod-b' for the 'com.amazonaws.us-east-1.elasticache' service in PROD. Limit the 'Cache Integration' service to Redis 6379 from '10.0.0.0/16', establish a 'cache' dashboard, and document the modification for 'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-prod-a",
                        "subnet-prod-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                "sg_change_applied: True",
                "dashboard_name: dash-prod-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A10",
        "instruction": "As Raj Patel from Personalization, in UAT you require a 'Prefer-Standard-Shipping' rule for 'NewCustomers' that chooses STANDARD on PDP, ensuring it's respected with 'WELCOME5'. Validate using a quick cart for 'USB-C Hub' for 'newuser@example.com', and record it under 'personalization'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard-Shipping",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "collection_name": "Context-Rule-SMOKE",
                    "environment": "UAT"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "newuser@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "change_type": "personalization",
                    "target_id": "ctx-newcustomers-prefer-standard-shipping",
                    "environment": "UAT"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-newcustomers-prefer-standard-shipping",
                "cart_id: cart-cust-newuser-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A11",
        "instruction": "From API, you are Dana Brooks. Within UAT, you aim to activate the 'catalog-v3' gateway and enlist the 'Catalog v3' API version '3.1.0' from 'blob_901'. You plan to execute 'Catalog-v3-SMOKE', set up an 'api' dashboard, and document the rollout for 'spec-catalog-v3-3-1-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.0",
                    "spec_blob_id": "blob_901"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "catalog-v3",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-catalog-v3-3-1-0",
                    "gateway_id": "dcg-catalog-v3-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Catalog-v3-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-catalog-v3-3-1-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-catalog-v3-3-1-0",
                "dcg_id: dcg-catalog-v3-uat",
                "run_id: run-catalog-v3-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A12",
        "instruction": "From Platform, you are Priya Shah. In UAT, you need the Commerce API service limited to '10.0.0.0/16' on Redis 6379 while retaining usage of the existing cache cluster 'dcomm-uat-redis'. You plan a CacheHitRate alert at 75.0 over 300 with 'LessThanThreshold', intend to create a 'cache' dashboard, and wish to document the modification for 'dcomm-uat-redis'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 75.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "sg_id: sg-uat-commerce-api",
                "cluster_id: dcomm-uat-redis",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-75-0-300-lessthanthreshold",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A13",
        "instruction": "From Identity, you are Luis Ortega. In UAT, you want the 'Commerce API' connected app to permit api, refresh_token, and openid with callback https://acme.example/callback. You plan to store the 'OAUTH_CLIENT_SECRET', execute 'OAuth-Smoke', set up an 'api' dashboard, and desire the modification recorded.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Commerce API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://acme.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-commerce-api",
                "secret_arn: arn:secret-secret-oauth_client_secret-uat-app-commerce-api-alias-dcomm-uat",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A14",
        "instruction": "Working in Commerce Ops, you are Sam Lee. In UAT, you aim to update retail pricing in 'Standard Retail' to 59.99 for 'USB-C Hub' (AC-USBC-HUB) and 199.99 for 'Thunderbolt Docking Station' (HW-TB-DOCK). You plan to set up a quick cart for 'sam@example.com' with 'WINTER20' and STANDARD shipping, and wish to record the pricebook update for 'Standard Retail'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 59.99
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 199.99
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "sam@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WINTER20",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "Standard Retail",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A15",
        "instruction": "In Sales Ops, you are Kelly Nguyen. Within UAT, you need 'WINTER20' set active=False and 'WELCOME5' set active=True. You plan a quick cart for 'newuser2@example.com' for 'USB-C Hub' with 'WELCOME5' and STANDARD shipping, and you aim to document the change for 'WELCOME5' with change_type 'personalization'.",
        "actions": [
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "WINTER20",
                    "active": false
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "WELCOME5",
                    "active": true
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "newuser2@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "WELCOME5",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "promo_id: promo-welcome5",
                "cart_id: cart-cust-newuser2-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A16",
        "instruction": "Your name is Omar Kelly from Performance. Within UAT, ensure the Commerce cache partition key 'dcomm' for version 'v5', and invalidate 'offer:USB-C Hub' and 'offer:Thunderbolt Docking Station'. Require a 'cache' dashboard, a 'metadata' warm, set trace sampling at 0.20, and log the modification for 'dcomm-v5'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v5"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.2
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v5",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v5",
                "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A17",
        "instruction": "Your name is Raj Patel from Personalization. Within UAT, establish a rule dubbed 'Prefer-Ent-Support' for the 'B2B-Enterprise' segment with the attribute 'addon_priority' assigned as 'enterprise_support', connected to 'B2BVOLUME15'. Execute 'Context-Rule-SMOKE', implement 'B2BVOLUME15' in a quick cart for 'david.c@email.com' including 'Thunderbolt Docking Station' and STANDARD shipping, and ensure the adjustment is noted for 'ctx-b2b-enterprise-prefer-ent-support'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "B2B-Enterprise",
                    "rule_name_hint": "Prefer-Ent-Support",
                    "attributes": {
                        "addon_priority": "enterprise_support"
                    },
                    "bind_to_offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "Thunderbolt Docking Station"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "items": [
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-b2b-enterprise-prefer-ent-support",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-b2b-enterprise-prefer-ent-support",
                "cart_id: cart-cust-david-c-email-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A18",
        "instruction": "Your name is Amira Patel from Networking. Within UAT, make ElastiCache accessible privately in VPC 'vpc-resolved' throughout subnets 'subnet-a' and 'subnet-b' for the service 'com.amazonaws.us-east-1.elasticache'. Limit the 'Cache Integration' service to Redis 6379 from '10.0.0.0/16', request a 'cache' dashboard, and ensure the alteration is documented for 'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-a",
                        "subnet-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                "sg_change_applied: True",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A19",
        "instruction": "Your name is Kelly Nguyen from Sales Ops. Within UAT, include 'david.c@email.com' in the 'B2B Wholesale' tier while preparing a quick cart with 'USB-C Hub' and 'Thunderbolt Docking Station' utilizing 'B2BVOLUME15' and STANDARD shipping. Ensure the change is logged.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "Thunderbolt Docking Station"
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "cart-cust-david-c-email-com-2025-08-06t12-00-00z",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-david-c-email-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A20",
        "instruction": "Your name is Priya Shah from Platform. Within UAT, make Commerce employ a new API auth header secret for the UAT cache cluster and direct Commerce to the current cache endpoint. Conduct a quick metadata warm and document the change for 'CacheAPI.ExternalSystemURL'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemURL",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A21",
        "instruction": "You are Dana Brooks from API. Within UAT, manage the activation of the 'inventory-v1' gateway and the registration of the 'Inventory v1' API version '1.0.0' from 'blob_inventory_v1'. Proceed with executing 'Inventory-v1-SMOKE', establish an 'api' dashboard, and document the deployment for 'spec-inventory-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Inventory v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_inventory_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "inventory-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-inventory-v1-1-0-0",
                    "gateway_id": "dcg-inventory-v1-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Inventory-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-inventory-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-inventory-v1-1-0-0",
                "dcg_id: dcg-inventory-v1-uat",
                "run_id: run-inventory-v1-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A22",
        "instruction": "You are Luis Ortega from Identity. In UAT, ensure that the 'Commerce API' connected app is utilizing api, refresh_token, and openid with the callback https://acme.example/callback. Securely store the 'OAUTH_CLIENT_SECRET', execute 'OAuth-Smoke', set up an 'api' dashboard, and log the update for 'app-commerce-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Commerce API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://acme.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-commerce-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A23",
        "instruction": "You are Amira Patel from Networking. In UAT, ensure ElastiCache is accessible privately within VPC 'vpc-resolved' across subnets 'subnet-a' and 'subnet-b' (use these specified ids, not environment defaults) for service 'com.amazonaws.us-east-1.elasticache'. Constrain 'Cache Integration' to Redis 6379 from '10.0.5.0/24' and document the update for 'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-a",
                        "subnet-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.5.0/24"
                    ]
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                "sg_change_applied: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A24",
        "instruction": "You are Omar Kelly from Performance. In UAT, configure the Commerce cache partition key 'dcomm' on version 'v6' and be sure to invalidate 'offer:USB-C Hub' and 'offer:Thunderbolt Docking Station'. Set up a CacheHitRate alarm on 'dcomm-uat-redis' at 80.0 over 300 with 'LessThanThreshold', metadata warmed, trace sampling at 0.18, and ensure you record the modification for 'dcomm-v6'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v6"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 80.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.18
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v6",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v6",
                "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-80-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A25",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, update 'B2B Wholesale' to 57.00 for 'USB-C Hub' and 189.00 for 'Thunderbolt Docking Station'. Ensure 'alex.cho@example.com' is on 'B2B Wholesale', prepare a quick cart with both items using 'B2BVOLUME15' and STANDARD shipping, and document the change for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "Thunderbolt Docking Station"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 57.0
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 189.0
                        }
                    ]
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "alex.cho@example.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "alex.cho@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-alex-cho-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A26",
        "instruction": "You are Dana Brooks from API. In UAT, make sure to activate the 'payments-v1' gateway and register the 'Payments v1' API version '1.2.0' from 'blob_payments_120'. Ensure trace sampling is at 0.08, execute 'SMOKE', establish an 'api' dashboard, and document the rollout for 'spec-payments-v1-1-2-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Payments v1",
                    "spec_version": "1.2.0",
                    "spec_blob_id": "blob_payments_120"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "payments-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-payments-v1-1-2-0",
                    "gateway_id": "dcg-payments-v1-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.08
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-payments-v1-1-2-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-payments-v1-1-2-0",
                "dcg_id: dcg-payments-v1-uat",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A27",
        "instruction": "You are Priya Shah from Platform. In UAT, require Commerce to connect to the existing cache cluster 'dcomm-uat-redis' with a fresh API auth header secret using purpose 'API_AUTH_HEADER'. Warm the metadata and log the change for 'CacheAPI.ExternalSystemURL'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemURL",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A28",
        "instruction": "You are Raj Patel from Personalization. In UAT, establish a rule named 'Prefer-Express' for the 'VIP' segment with the attribute 'shipping_preference' set to 'EXPRESS', linked to 'WELCOME5'. Conduct 'Context-Rule-SMOKE', set up a quick cart for 'trialshopper@example.com' with 'USB-C Hub' and shipping EXPRESS, and document the change for 'ctx-vip-prefer-express'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {
                        "shipping_preference": "EXPRESS"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-vip-prefer-express",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A29",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, ensure the promotion 'B2BVOLUME15' is explicitly active and verify with a quick cart for 'USB-C Hub' for 'pat.jones@example.com' utilizing STANDARD shipping. Log the change for 'B2BVOLUME15'.",
        "actions": [
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "B2BVOLUME15",
                    "active": true
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "pat.jones@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2BVOLUME15",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "promo_id: promo-b2bvolume15",
                "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A30",
        "instruction": "You are Rafael Kim from SRE. In UAT, ensure Commerce API maintains its cache warmth routinely and is monitored for any failures. Deploy 'bundle_cachewarmer_v1' for a 'cache_warmer' function. Create a 'cache' dashboard, set an 'Errors' alarm at 1.0 over 300 with 'GreaterThanOrEqualToThreshold' on ARN 'arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat', conduct a 'SMOKE' test, warm the 'metadata' immediately, and document the change for 'fn-commerce-api-cache_warmer-uat'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A31",
        "instruction": "You are Dana Brooks from API. During UAT, aim to activate the 'inventory-v1' gateway and register the 'Inventory v1' API version '1.0.0' from 'blob_inventory_v1'. Run 'Inventory-v1-SMOKE', establish an 'api' dashboard, and log the rollout for 'spec-inventory-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Inventory v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_inventory_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "inventory-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-inventory-v1-1-0-0",
                    "gateway_id": "dcg-inventory-v1-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Inventory-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-inventory-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-inventory-v1-1-0-0",
                "dcg_id: dcg-inventory-v1-uat",
                "run_id: run-inventory-v1-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A32",
        "instruction": "You are Amira Patel from Networking. Within DEV, ensure ElastiCache is accessible privately in VPC 'vpc-dev-0001' across subnets 'subnet-dev-a' and 'subnet-dev-b' for service 'com.amazonaws.us-east-1.elasticache'. Restrict the 'Cache Integration' service to Redis 6379 from '10.2.0.0/16', and document the change for 'vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-dev-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-dev-a",
                        "subnet-dev-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "DEV",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-dev-cache-integration",
                    "environment": "DEV",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.2.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
                    "environment": "DEV",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
                "sg_change_applied: True",
                "dashboard_name: dash-dev-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A33",
        "instruction": "Your role as Sam Lee from Commerce Ops involves, in UAT, updating 'Standard Retail' to 62.50 for 'USB-C Hub' (AC-USBC-HUB) and 209.00 for 'Thunderbolt Docking Station' (HW-TB-DOCK). Ensure 'sam@example.com' confirms with a cart using 'WELCOME5' and STANDARD shipping, and document the pricebook change for 'Standard Retail'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 62.5
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 209.0
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "sam@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "Standard Retail",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A34",
        "instruction": "You are Omar Kelly from Performance. During UAT, establish the Commerce cache partition key 'dcomm' on version 'v7' and invalidate 'offer:USB-C Hub' and 'offer:Thunderbolt Docking Station'. Set up a CacheHitRate alarm on 'dcomm-uat-redis' at 70.0 over 300 with 'LessThanThreshold', initiate a 'populate' warm now, trace sampling at 0.12, and record the update for 'dcomm-v7'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v7"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 70.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.12
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v7",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v7",
                "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-70-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A35",
        "instruction": "You are Luis Ortega from Identity. In PROD, update the app titled 'Checkout API' with the necessary access and callback at https://checkout.example/callback, ensure validation, and monitor to baseline. Document the update for 'app-checkout-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Checkout API",
                    "scopes": [
                        "api",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://checkout.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-checkout-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "app-checkout-api",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-checkout-api",
                    "environment": "PROD",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-checkout-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-prod-app-checkout-api-alias-dcomm-prod",
                "run_id: run-oauth-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A36",
        "instruction": "As Raj Patel from Personalization, initiate in UAT a rule labeled 'Prefer-Overnight' for the 'VIP' segment, ensuring the attribute 'shipping_preference' is defined as 'OVERNIGHT', and link it to 'WELCOME5'. Proceed to execute 'Context-Rule-SMOKE', generate a quick cart for 'pat.jones@example.com' incorporating 'Thunderbolt Docking Station' with OVERNIGHT shipping, and log the modification for 'ctx-vip-prefer-overnight'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Overnight",
                    "attributes": {
                        "shipping_preference": "OVERNIGHT"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "Thunderbolt Docking Station"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "pat.jones@example.com",
                    "items": [
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "OVERNIGHT"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-vip-prefer-overnight",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-vip-prefer-overnight",
                "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A37",
        "instruction": "You are Priya Shah from Platform. Within UAT, coordinate Commerce to employ a fresh API auth header secret with the designated purpose 'API_AUTH_HEADER' for the active cluster 'dcomm-uat-redis'. Facilitate the warming of metadata and ensure to log the update for 'CacheAPI.ExternalSystemAuthHeader'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A38",
        "instruction": "Being Amira Patel from Networking, in PROD, impose a restriction on the 'Checkout Gateway' service to '10.0.0.0/16' using TLS 443. Develop an 'api' dashboard, and ensure you capture the update for 'sg-prod-checkout-gateway'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "change_set_id: chg-sg-sg-prod-checkout-gateway-prod-checkout-gateway-443-10-0-0-0-16",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A39",
        "instruction": "As Dana Brooks from API, in PROD, authorize the 'search-v1' gateway and register the 'Search v1' API, version '1.0.0', sourced from 'blob_search_v1_0_0'. Ensure trace sampling is set at 0.05, perform 'Search-v1-SMOKE', create an 'api' dashboard, and document the deployment for 'spec-search-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Search v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_search_v1_0_0"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "search-v1",
                    "environment": "PROD"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-search-v1-1-0-0",
                    "gateway_id": "dcg-search-v1-prod"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.05
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "Search-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-search-v1-1-0-0",
                    "environment": "PROD",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-search-v1-1-0-0",
                "dcg_id: dcg-search-v1-prod",
                "run_id: run-search-v1-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A40",
        "instruction": "Omar Kelly from Performance directs that in UAT, the Commerce cache partition key 'dcomm' reflects version 'v8', and trigger the invalidation of 'offer:WELCOME5' and 'offer:WINTER20'. Arrange for a 'metadata' warm now and configure a CacheHitRate alarm at 72.0 over 300 with 'LessThanThreshold', and ensure the record of the update for 'dcomm-v8'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v8"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:WELCOME5",
                        "offer:WINTER20"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 72.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v8",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v8",
                "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-72-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A41",
        "instruction": "Dana Brooks from API wants the 'orders-v1' gateway enabled in UAT, and to register the 'Orders v1' API version '1.0.0' using 'blob_orders_v1'. They intend to execute 'Orders-v1-SMOKE', establish an 'api' dashboard, and log the rollout for 'spec-orders-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Orders v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_orders_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "orders-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-orders-v1-1-0-0",
                    "gateway_id": "dcg-orders-v1-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Orders-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-orders-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-orders-v1-1-0-0",
                "dcg_id: dcg-orders-v1-uat",
                "run_id: run-orders-v1-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A42",
        "instruction": "Priya Shah from Platform will limit the Commerce API service to '10.0.5.0/24' on Redis 6379 in UAT while maintaining the 'dcomm-uat-redis' cache cluster. She requires a CacheHitRate alarm at 78.0, metric period 300, with 'LessThanThreshold', setting up a 'cache' dashboard, and documenting the change for 'dcomm-uat-redis'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.5.0/24"
                    ]
                },
            },
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 78.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "sg_id: sg-uat-commerce-api",
                "cluster_id: dcomm-uat-redis",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-78-0-300-lessthanthreshold",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A43",
        "instruction": "Luis Ortega from Identity needs in PROD the connected app titled 'Commerce API' to permit api and openid with callback https://commerce.example/callback. He aims to save the 'OAUTH_CLIENT_SECRET', proceed with 'OAuth-Smoke', set up an 'api' dashboard, and capture the change for 'app-commerce-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Commerce API",
                    "scopes": [
                        "api",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://commerce.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-commerce-api",
                    "environment": "PROD",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-commerce-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-prod-app-commerce-api-alias-dcomm-prod",
                "run_id: run-oauth-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A44",
        "instruction": "Kelly Nguyen from Sales Ops plans to adjust 'B2B Wholesale' pricing to 58.50 for 'USB-C Hub' and 185.00 for 'Thunderbolt Docking Station' in UAT. She wants 'sara.lee@example.com' associated with 'B2B Wholesale', creating a swift cart including both items with 'B2BVOLUME15' and STANDARD shipping, and ensuring the update is filed for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "Thunderbolt Docking Station"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 58.5
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 185.0
                        }
                    ]
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "sara.lee@example.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "sara.lee@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-sara-lee-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A45",
        "instruction": "Omar Kelly from Performance is setting up the Commerce cache with partition key 'dcomm' on version 'v9' in UAT, nullifying 'offer:USB-C Hub' and 'offer:WELCOME5'. He needs a 'metadata' warm, trace sampling set at 0.22, an organized 'cache' dashboard, and the modification recorded for 'dcomm-v9'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v9"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:WELCOME5"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.22
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v9",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v9",
                "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A46",
        "instruction": "You are Raj Patel from Personalization. Within UAT, you need a rule titled 'Prefer-Standard' for the 'Returning' segment with 'shipping_preference' set to 'STANDARD', associated with 'WELCOME5'. You should execute 'Context-Rule-SMOKE', assemble a quick cart for 'returning.buyer@example.com' featuring 'USB-C Hub' and STANDARD shipping, and document the adjustment for 'ctx-returning-prefer-standard'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "Returning",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "returning.buyer@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-returning-prefer-standard",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-returning-prefer-standard",
                "cart_id: cart-cust-returning-buyer-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A47",
        "instruction": "You are Amira Patel from Networking. In the DEV environment, arrange for ElastiCache to be privately accessible in VPC 'vpc-dev-0001' across 'subnet-dev-a' and 'subnet-dev-b' for service 'com.amazonaws.us-east-1.elasticache'. Limit access for the 'Cache Integration' service to Redis 6379 from '10.2.5.0/24', establish a 'cache' dashboard, and ensure the modification is documented for 'vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-dev-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-dev-a",
                        "subnet-dev-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "DEV",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-dev-cache-integration",
                    "environment": "DEV",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.2.5.0/24"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
                    "environment": "DEV",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
                "sg_change_applied: True",
                "dashboard_name: dash-dev-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A48",
        "instruction": "You are Dana Brooks from API. In the PROD environment, you need 'Billing v2' version '2.3.0' from 'blob_billing_230' accessible via 'billing-v2' with baseline monitoring and a sampling rate of 0.06. Proceed to 'Billing-v2-SMOKE' and log the deployment for 'spec-billing-v2-2-3-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Billing v2",
                    "spec_version": "2.3.0",
                    "spec_blob_id": "blob_billing_230"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "billing-v2",
                    "environment": "PROD"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-billing-v2-2-3-0",
                    "gateway_id": "dcg-billing-v2-prod"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.06
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "Billing-v2-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-billing-v2-prod",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-billing-v2-2-3-0",
                    "environment": "PROD",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-billing-v2-2-3-0",
                "dcg_id: dcg-billing-v2-prod",
                "run_id: run-billing-v2-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A49",
        "instruction": "You are Priya Shah from Platform. In the UAT setup, necessitate Commerce to implement a new API auth header secret for 'API_AUTH_HEADER' on the pre-existing cluster 'dcomm-uat-redis'. Make sure the metadata is warmed, and record the update for 'CacheAPI.ExternalSystemAuthHeader'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A30",
        "instruction": "You are Rafael Kim from SRE. In UAT, you want Commerce API to keep its cache warm on a recurring cadence and be monitored for failures. Use the bundle 'bundle_cachewarmer_v1' for a 'cache_warmer' function. You want a 'cache' dashboard, an 'Errors' alarm at 1.0 over 300 with 'GreaterThanOrEqualToThreshold' on the ARN 'arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat', a 'SMOKE' test run, a 'metadata' warm now, and you want to record the change for 'fn-commerce-api-cache_warmer-uat'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A51",
        "instruction": "As Rafael Kim from SRE, manage the 'Checkout API' in PROD to ensure its cache remains warm on a recurring basis and observe for any failures. Implement the 'cache_warmer' feature utilizing the bundle 'bundle_cachewarmer_v1'. Create a 'cache' dashboard, set up an 'Errors' alarm with a threshold of 1.0 over 300 using 'GreaterThanOrEqualToThreshold', execute a 'SMOKE' test, and document the update as 'fn-checkout-api-cache_warmer-prod'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Checkout API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-prod"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-prod",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-checkout-api-cache_warmer-prod",
                    "environment": "PROD",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-prod",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-checkout-api-cache_warmer-prod-rate-15-minutes",
                "dashboard_name: dash-prod-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-checkout-api-cache_warmer-prod-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A52",
        "instruction": "As Amira Patel from Networking, in UAT, restrict the 'Checkout Gateway' service to access only '10.0.5.0/24' over TLS on port 443. Develop an 'api' dashboard and document the alteration for 'sg-uat-checkout-gateway'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.5.0/24"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-5-0-24",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A53",
        "instruction": "Being Luis Ortega from Identity, in UAT, configure the 'Search API' connected app to permit api and refresh_token types with the callback URL as https://search.example/callback. Save the 'OAUTH_CLIENT_SECRET', perform 'OAuth-Smoke' testing, establish an 'api' dashboard, and log the change for 'app-search-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Search API",
                    "scopes": [
                        "api",
                        "refresh_token"
                    ],
                    "callback_urls": [
                        "https://search.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-search-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-search-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-search-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-search-api-alias-dcomm-uat",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A54",
        "instruction": "As Omar Kelly from Performance, in UAT, implement the partition key 'dcomm' of Commerce cache on version 'v10' and invalidate 'offer:WINTER20' alongside 'offer:Thunderbolt Docking Station'. Create a CacheHitRate alarm on 'dcomm-uat-redis' with a metric of 74.0 over 300 applying 'LessThanThreshold', perform a 'populate' warm, set trace sampling at 0.11, and record the modification as 'dcomm-v10'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v10"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:WINTER20",
                        "offer:Thunderbolt Docking Station"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 74.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.11
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v10",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v10",
                "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-74-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A55",
        "instruction": "As Kelly Nguyen from Sales Ops, make sure 'B2B Wholesale' is updated to 55.00 for 'USB-C Hub' in UAT. Add 'kelly.ross@example.com' on 'B2B Wholesale', prepare a quick cart with 3\u00d7 'USB-C Hub' applying 'B2BVOLUME15' and opting for STANDARD shipping, and ensure the update is logged for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 55.0
                        }
                    ]
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "kelly.ross@example.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "kelly.ross@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 3
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 1",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-kelly-ross-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A56",
        "instruction": "You are Raj Patel from Personalization. In UAT, a rule named 'Prefer-Ent-Addon' should be established for the 'B2B-Enterprise' segment with attribute 'addon_priority' assigned as 'enterprise_support', linked to 'B2BVOLUME15'. Proceed to execute 'Context-Rule-SMOKE', assemble a quick cart for 'alex.cho@example.com' with 'USB-C Hub' and STANDARD shipping using 'B2BVOLUME15', and document the modification for 'ctx-b2b-enterprise-prefer-ent-addon'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "B2B-Enterprise",
                    "rule_name_hint": "Prefer-Ent-Addon",
                    "attributes": {
                        "addon_priority": "enterprise_support"
                    },
                    "bind_to_offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "alex.cho@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-b2b-enterprise-prefer-ent-addon",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-b2b-enterprise-prefer-ent-addon",
                "cart_id: cart-cust-alex-cho-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A57",
        "instruction": "You are Dana Brooks from API. In UAT, the 'profiles-v1' gateway needs to be activated and the 'Profiles v1' API version '1.0.0' is to be registered from 'blob_profiles_v1'. Initiate 'Profiles-v1-SMOKE', set up an 'api' dashboard, and log the deployment for 'spec-profiles-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Profiles v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_profiles_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "profiles-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-profiles-v1-1-0-0",
                    "gateway_id": "dcg-profiles-v1-uat"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Profiles-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-profiles-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-profiles-v1-1-0-0",
                "dcg_id: dcg-profiles-v1-uat",
                "run_id: run-profiles-v1-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A58",
        "instruction": "You are Amira Patel from Networking. In PROD, ensure ElastiCache is accessible privately within VPC 'vpc-prod-0001' across subnets 'subnet-prod-a' and 'subnet-prod-b' for service 'com.amazonaws.us-east-1.elasticache'. Restrict the 'Cache Integration' service to Redis 6379 originating from '10.0.0.0/16', establish a 'cache' dashboard, and log the update for 'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-prod-a",
                        "subnet-prod-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                "sg_change_applied: True",
                "dashboard_name: dash-prod-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A59",
        "instruction": "You are Luis Ortega from Identity. In DEV, the 'Checkout API' connected app must authorize api and refresh_token with a callback to https://checkout.dev/callback. Secure the 'OAUTH_CLIENT_SECRET', commence 'OAuth-Smoke', configure an 'api' dashboard, and document the adjustment for 'app-checkout-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Checkout API",
                    "scopes": [
                        "api",
                        "refresh_token"
                    ],
                    "callback_urls": [
                        "https://checkout.dev/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-checkout-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "DEV",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-checkout-api",
                    "environment": "DEV",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-checkout-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-dev-app-checkout-api-alias-dcomm-dev",
                "run_id: run-oauth-smoke-dev-2025-08-06t12-00-00z",
                "dashboard_name: dash-dev-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A60",
        "instruction": "You are Sam Lee from Commerce Ops. In UAT, update 'Standard Retail' to 60.25 for 'USB-C Hub'. Create a quick cart for 'trialshopper@example.com' featuring 'USB-C Hub' and 'WELCOME5' using EXPRESS shipping, and ensure the pricebook amendment for 'Standard Retail' is recorded.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "GetProductByName",
                "arguments": {
                    "name": "USB-C Hub"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 60.25
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "Standard Retail",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 1",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A61",
        "instruction": "Assume the role of Dana Brooks from API. In the UAT environment, plan to implement the 'Catalog v4' edition '4.0.0' originating from 'blob_catalog_400' through the 'catalog-v4' gateway. Request trace sampling set to 0.09, register endpoints, execute 'Catalog-v4-SMOKE', form an 'api' dashboard, configure a '5xxErrorRate' alert at 1.0 over 300 with 'GreaterThanOrEqualToThreshold' on 'dcg-catalog-v4-uat', and chronicle the rollout for 'spec-catalog-v4-4-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Catalog v4",
                    "spec_version": "4.0.0",
                    "spec_blob_id": "blob_catalog_400"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "catalog-v4",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-catalog-v4-4-0-0",
                    "gateway_id": "dcg-catalog-v4-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.09
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Catalog-v4-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-catalog-v4-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-catalog-v4-4-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-catalog-v4-4-0-0",
                "dcg_id: dcg-catalog-v4-uat",
                "run_id: run-catalog-v4-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api",
                "alarm_id: al-dcg-catalog-v4-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A62",
        "instruction": "Identify as Priya Shah from Platform. Within the UAT, restrict the Commerce API to the standard internal network over TLS and Redis, continue utilizing the UAT cache cluster with AUTH/TLS, and privately unveil ElastiCache in VPC 'vpc-uat-0001' on 'subnet-uat-a' and 'subnet-uat-b'. Direct Commerce at dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com with the current secret, conduct a swift metadata warm, establish a 'cache' dashboard, and alert if the cache hit rate descends below 76.0 in five-minute blocks. Document the adjustment for 'dcomm-uat-redis'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        443,
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-uat-a",
                        "subnet-uat-b"
                    ]
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 76.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-76-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A63",
        "instruction": "Take the role of Luis Ortega from Identity. For UAT, ensure the 'Orders API' connected app permits api, refresh_token, and openid with callback at https://orders.example/callback. Preserve 'OAUTH_CLIENT_SECRET' and an 'API_AUTH_HEADER' secret for 'app-orders-api', conduct 'OAuth-Smoke', develop an 'api' dashboard, and document the modification for 'app-orders-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Orders API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://orders.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-orders-api"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-orders-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-orders-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-orders-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-orders-api-alias-dcomm-uat",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A64",
        "instruction": "Enact the responsibilities of Kelly Nguyen from Sales Ops. Within UAT, update 'Standard Retail' to 63.25 for 'USB-C Hub' (AC-USBC-HUB) and 212.00 for 'Thunderbolt Docking Station' (HW-TB-DOCK), and 'B2B Wholesale' to 56.75 for AC-USBC-HUB and 182.50 for HW-TB-DOCK. Include 'david.c@email.com' in 'B2B Wholesale', arrange a cart with 2\u00d7 AC-USBC-HUB and 1\u00d7 HW-TB-DOCK using 'B2BVOLUME15' and STANDARD shipping, and register the update for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 63.25
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 212.0
                        }
                    ]
                },
            },
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 56.75
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 182.5
                        }
                    ]
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 2
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-david-c-email-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A65",
        "instruction": "Act as Raj Patel from Personalization. In UAT, initiate a VIP policy named 'Prefer-Express' that selects EXPRESS and a NewCustomers policy named 'Prefer-Standard-New' that opts for STANDARD, both linked to WELCOME5. Conduct 'Context-Rule-SMOKE', then validate with a brief cart for 'USB-C Hub' (AC-USBC-HUB) using WELCOME5 and EXPRESS shipping, and document the alteration for 'ctx-vip-prefer-express'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {
                        "shipping_preference": "EXPRESS"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard-New",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-vip-prefer-express",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A66",
        "instruction": "Handle the task as Amira Patel from Networking. In PROD, ensure ElastiCache is accessible privately within VPC 'vpc-prod-0001' on subnets 'subnet-prod-a' and 'subnet-prod-b' for 'com.amazonaws.us-east-1.elasticache'. Restrict the 'Cache Integration' service to Redis 6379 from '10.0.0.0/16', execute 'Cache-Network-SMOKE', establish a 'cache' dashboard, and document the modification for 'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-prod-a",
                        "subnet-prod-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "Cache-Network-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "cache"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                "sg_change_applied: True",
                "dashboard_name: dash-prod-cache",
                "run_id: run-cache-network-smoke-prod-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A67",
        "instruction": "Coordinate activities as Omar Kelly from Performance. In UAT, assign the Commerce cache partition key 'dcomm' at 'v11' and invalidate 'offer:USB-C Hub' and 'offer:Thunderbolt Docking Station'. Set up nightly cache maintenance for UAT (action 'create'), conduct a 'metadata' warm followed by a 'populate' warm, adjust trace sampling to 0.13, develop a 'cache' dashboard, establish a 'CacheHitRate' alarm at 73.0 over 300 using 'LessThanThreshold' on 'dcomm-uat-redis', and log the adjustment for 'dcomm-v11'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v11"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station"
                    ]
                },
            },
            {
                "name": "ManageCacheMaintenance",
                "arguments": {
                    "environment": "UAT",
                    "action": "create"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.13
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 73.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v11",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v11",
                "schedule_id: cm-uat",
                "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-cachehitrate-73-0-300-lessthanthreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A68",
        "instruction": "Coordinate operations as Dana Brooks from API. In DEV, implement 'Checkout v3' version '3.0.0' from 'blob_checkout_300' via the 'checkout-v3' gateway. Set trace sampling to 0.07, register endpoints, perform 'Checkout-v3-SMOKE', create an 'api' dashboard, configure a '5xxErrorRate' alarm at 1.2 over 300 with 'GreaterThanOrEqualToThreshold' on 'dcg-checkout-v3-dev', and note the rollout for 'spec-checkout-v3-3-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Checkout v3",
                    "spec_version": "3.0.0",
                    "spec_blob_id": "blob_checkout_300"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "checkout-v3",
                    "environment": "DEV"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-checkout-v3-3-0-0",
                    "gateway_id": "dcg-checkout-v3-dev"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.07
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "DEV",
                    "collection_name": "Checkout-v3-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-checkout-v3-dev",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.2,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-checkout-v3-3-0-0",
                    "environment": "DEV",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-checkout-v3-3-0-0",
                "dcg_id: dcg-checkout-v3-dev",
                "run_id: run-checkout-v3-smoke-dev-2025-08-06t12-00-00z",
                "dashboard_name: dash-dev-api",
                "alarm_id: al-dcg-checkout-v3-dev-5xxerrorrate-1-2-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A69",
        "instruction": "Oversee the setup as Luis Ortega from Identity. In PROD, configure the 'Search API' connected app to enable api, refresh_token, and openid functions with callback https://search.example/callback. Store 'OAUTH_CLIENT_SECRET', execute 'OAuth-Smoke', develop an 'api' dashboard, and document the update for 'app-search-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Search API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://search.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-search-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-search-api",
                    "environment": "PROD",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-search-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-prod-app-search-api-alias-dcomm-prod",
                "run_id: run-oauth-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A70",
        "instruction": "Direct actions as Sam Lee from Commerce Ops. In UAT, establish 'Standard Retail' pricing at 65.00 for AC-USBC-HUB and 215.00 for HW-TB-DOCK. Instruct 'tasha.green@example.com' to place a quick order for AC-USBC-HUB using WINTER20 with OVERNIGHT shipping, verify that WINTER20 is active, create an 'api' dashboard for visibility, and record the price alteration for 'Standard Retail'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 65.0
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 215.0
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "WINTER20",
                    "active": true
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "tasha.green@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WINTER20",
                    "shipping_method": "OVERNIGHT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "Standard Retail",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "cart_id: cart-cust-tasha-green-example-com-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A71",
        "instruction": "You are Priya Shah from Platform. For UAT, handle the rotation of the API auth header secret for the UAT cache cluster, direct Commerce to the current cache endpoint, warm metadata, implement baseline sampling and a 'cache' dashboard, and document the change for 'CacheAPI.ExternalSystemAuthHeader'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "cache_integration_verified: True",
                "dashboard_name: dash-uat-cache"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A72",
        "instruction": "You are Amira Patel from Networking. In UAT, limit the Checkout Gateway to 10.0.5.0/24 on TLS 443 and ensure it is verified. Initiate 'Gateway-SMOKE', apply the API monitoring baseline, and record the change for 'sg-uat-checkout-gateway'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.5.0/24"
                    ]
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Gateway-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "sg-uat-checkout-gateway",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-5-0-24",
                "dashboard_name: dash-uat-api",
                "run_id: run-gateway-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A73",
        "instruction": "You are Rafael Kim from SRE. In PROD, ensure the cache of 'Search API' remains warm on a set schedule and is monitored for any failures. Utilize the package 'bundle_cachewarmer_v1' for a 'cache_warmer' function, and set an alarm on the ARN 'arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod'. Implement a 'cache' dashboard, conduct a 'SMOKE' test, do an immediate 'metadata' warm, and document the change for 'fn-search-api-cache_warmer-prod'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Search API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-search-api-cache_warmer-prod",
                    "environment": "PROD",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-search-api-cache_warmer-prod-rate-15-minutes",
                "dashboard_name: dash-prod-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-search-api-cache_warmer-prod-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-prod-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A74",
        "instruction": "You are Priya Shah from Platform. In UAT, ensure Commerce is using the UAT cache endpoint with AUTH/TLS, transfer the cache partition 'dcomm' to 'v12', restrict the Commerce API to 10.0.5.0/24 on Redis 6379, perform a quick metadata warm, apply the cache monitoring baseline (dashboard, Errors alarm, SMOKE), and document the change for 'CacheAPI.ExternalSystemURL'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v12"
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.5.0/24"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemURL",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v12",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A75",
        "instruction": "You are Dana Brooks from API. In UAT, initiate the rollout of 'Offers v1' version '1.0.0' using 'blob_offers_v1' through the 'offers-v1' gateway. Set trace sampling at 0.09, register endpoints, execute 'Offers-v1-SMOKE', create an 'api' dashboard, and record the rollout for 'spec-offers-v1-1-0-0'. Additionally, create a 'NewCustomers' context rule named 'Prefer-Standard' with 'shipping_preference'='STANDARD' linked to 'WELCOME5', and prepare a quick cart for 'trialshopper@example.com' for 'USB-C Hub' (AC-USBC-HUB) using 'WELCOME5' and STANDARD shipping.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Offers v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_offers_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "offers-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-offers-v1-1-0-0",
                    "gateway_id": "dcg-offers-v1-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.09
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Offers-v1-SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-offers-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                },
            },
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-offers-v1-1-0-0",
                "dcg_id: dcg-offers-v1-uat",
                "run_id: run-offers-v1-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api",
                "context_rule_id: ctx-newcustomers-prefer-standard",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A76",
        "instruction": "As Priya Shah from Platform, ensure that in UAT, the Commerce API is secured to the designated standard internal network, ElastiCache is exclusively accessible internally, and Commerce is integrated with the UAT cache cluster. Implement the cache monitoring baseline and document the modification for 'dcomm-uat-redis'.",
        "actions": [
            {
                "name": "GetEnvironmentNetworkDefaults",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-uat-a",
                        "subnet-uat-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        443,
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A77",
        "instruction": "Assuming the role of Dana Brooks from API, make sure that in UAT, the 'Pricing v1' of version '1.0.0' from 'blob_pricing_v1' is available via 'pricing-v1' and observe the baseline monitoring. Document the deployment for 'spec-pricing-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Pricing v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_pricing_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "pricing-v1",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-pricing-v1-1-0-0",
                    "gateway_id": "dcg-pricing-v1-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-pricing-v1-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-pricing-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-pricing-v1-1-0-0",
                "dcg_id: dcg-pricing-v1-uat",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api",
                "alarm_id: al-dcg-pricing-v1-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A78",
        "instruction": "As Luis Ortega from Identity, ensure that in UAT, the connected app named precisely 'Inventory API' is authorized with api and refresh_token, with the callback URL https://inventory.example/callback, and that its secrets are correctly configured. Apply the monitoring baseline and document the modification for 'app-inventory-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Inventory API",
                    "scopes": [
                        "api",
                        "refresh_token"
                    ],
                    "callback_urls": [
                        "https://inventory.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-inventory-api"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-inventory-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "app-inventory-api",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-inventory-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-inventory-api",
                "secret_arn_oauth: arn:secret-secret-oauth-client-secret-uat-app-inventory-api-alias-dcomm-uat",
                "secret_arn_api_auth: arn:secret-secret-api-auth-header-uat-app-inventory-api-alias-dcomm-uat",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api",
                "alarm_id: al-app-inventory-api-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A79",
        "instruction": "As Amira Patel from Networking, in a PROD environment, make ElastiCache accessible privately, ensuring both the Commerce API and Cache Integration services adhere to the standard internal network: the Commerce API should operate on ports 443 and 6379; Cache Integration should use port 6379 exclusively. Implement the cache monitoring baseline and document the change for 'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'.",
        "actions": [
            {
                "name": "GetEnvironmentNetworkDefaults",
                "arguments": {
                    "environment": "PROD"
                },
            },
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-prod-a",
                        "subnet-prod-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-commerce-api",
                    "environment": "PROD",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        443,
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "\"endpoint_id\": \"vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b\"",
                "\"dashboard_name\": \"dash-prod-cache\"",
                "\"alarm_id\": \"al-vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b-errors-1-0-300-greaterthanorequaltothreshold\""
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A80",
        "instruction": "Taking on the role of Kelly Nguyen from Sales Ops, in UAT, prepare wholesale pricing for 'B2B Wholesale', apply the 'B2B Wholesale' tier to 'alex.cho@example.com', and validate using a shopping cart containing 1\u00d7 AC-USBC-HUB and 1\u00d7 HW-TB-DOCK with B2BVOLUME15 and STANDARD shipping. Execute 'Pricing-SMOKE' and document the update for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 57.0
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 189.0
                        }
                    ]
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "alex.cho@example.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "alex.cho@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Pricing-SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-alex-cho-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A81",
        "instruction": "You are Raj Patel from Personalization. In UAT, adjust the experiences for VIP and NewCustomers\u2014apply 'Prefer-Express' for VIP and 'Prefer-Standard' for NewCustomers, link both to WELCOME5, confirm with a quick cart for 'trialshopper@example.com', and document the update for 'ctx-vip-prefer-express'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {
                        "shipping_preference": "EXPRESS"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-vip-prefer-express",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A82",
        "instruction": "You are Rafael Kim from SRE. In UAT, maintain the Commerce API in a warm state and actively monitor it. Utilize the bundle 'bundle_cachewarmer_v1' for a 'cache_warmer' function, implement the monitoring baseline, execute a metadata warm, and log the update for 'fn-commerce-api-cache_warmer-uat'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A83",
        "instruction": "You are Priya Shah from Platform. In UAT, optimize and confirm the Commerce cache partition 'dcomm': transition it to 'v13', deactivate keys 'offer:USB-C Hub', 'offer:Thunderbolt Docking Station', 'offer:WELCOME5', 'offer:WINTER20', initiate nightly maintenance, warm metadata and data, employ standard sampling, enact the cache monitoring baseline, and note the modification for 'dcomm-v13'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v13"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5",
                        "offer:WINTER20"
                    ]
                },
            },
            {
                "name": "ManageCacheMaintenance",
                "arguments": {
                    "environment": "UAT",
                    "action": "create"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v13",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v13",
                "schedule_id: cm-uat",
                "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A84",
        "instruction": "You are Dana Brooks from API. In DEV, deploy 'Recommendations v1' version '1.0.0' from 'blob_recs_v1' to 'recommendations-v1' complete with baseline monitoring on the gateway with a 5xxErrorRate alarm and a sampling of 0.10. Record the deployment for 'spec-recommendations-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Recommendations v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_recs_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "recommendations-v1",
                    "environment": "DEV"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-recommendations-v1-1-0-0",
                    "gateway_id": "dcg-recommendations-v1-dev"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "DEV"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-recommendations-v1-dev",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-recommendations-v1-1-0-0",
                    "environment": "DEV",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-recommendations-v1-1-0-0",
                "dcg_id: dcg-recommendations-v1-dev",
                "run_id: run-smoke-dev-2025-08-06t12-00-00z",
                "dashboard_name: dash-dev-api",
                "alarm_id: al-dcg-recommendations-v1-dev-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A85",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, refine and confirm retail and wholesale pricing with a cart for 'pat.jones@example.com'. Set 'Standard Retail' to 61.25 for 'AC-USBC-HUB' and 206.5 for 'HW-TB-DOCK'. Set 'B2B Wholesale' to 56.25 for 'AC-USBC-HUB' and 181.75 for 'HW-TB-DOCK'. Maintain promotion consistency and record the adjustment for 'Standard Retail'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 61.25
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 206.5
                        }
                    ]
                },
            },
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 56.25
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 181.75
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "pat.jones@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "Standard Retail",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A86",
        "instruction": "You are Amira Patel from Networking. In UAT, ensure the Checkout Gateway is secured to the standard internal network and verified. Implement the API monitoring baseline and document the change for 'sg-uat-checkout-gateway'.",
        "actions": [
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "sg-uat-checkout-gateway",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-0-0-16",
                "dashboard_name: dash-uat-api",
                "alarm_id: al-sg-uat-checkout-gateway-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A87",
        "instruction": "You are Rafael Kim from SRE. In DEV, maintain the Checkout API by keeping it warm every 15 minutes and monitoring at baseline (dashboard, Errors alarm, SMOKE). Utilize the bundle 'bundle_cachewarmer_v1' for a 'cache_warmer' function, perform a quick metadata warm, and log the change for 'fn-checkout-api-cache_warmer-dev'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "DEV",
                    "service_name": "Checkout API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "DEV"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-checkout-api-cache_warmer-dev",
                    "environment": "DEV",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-functi-rate-15-minutes",
                "dashboard_name: dash-dev-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-functi-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-dev-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A88",
        "instruction": "You are Dana Brooks from API. In PROD, make 'Orders v1' version '1.0.0' from 'blob_orders_v1' live on 'orders-v1' with baseline monitoring. Document the rollout for 'spec-orders-v1-1-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Orders v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_orders_v1"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "orders-v1",
                    "environment": "PROD"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-orders-v1-1-0-0",
                    "gateway_id": "dcg-orders-v1-prod"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "PROD"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-orders-v1-prod",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-orders-v1-1-0-0",
                    "environment": "PROD",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-orders-v1-1-0-0",
                "dcg_id: dcg-orders-v1-prod",
                "run_id: run-smoke-prod-2025-08-06t12-00-00z",
                "dashboard_name: dash-prod-api",
                "alarm_id: al-dcg-orders-v1-prod-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A89",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, suspend WINTER20 and specifically activate WELCOME5, check with a cart for 'newuser2@example.com', execute 'Promo-SMOKE', and note the change for 'WINTER20'.",
        "actions": [
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "WINTER20",
                    "active": false
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpsertPromotion",
                "arguments": {
                    "code": "WELCOME5",
                    "active": true
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "newuser2@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Promo-SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "WINTER20",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "promo_id: promo-winter20",
                "cart_id: cart-cust-newuser2-example-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A90",
        "instruction": "You are Priya Shah from Platform. In UAT, require Commerce to rotate its API auth header secret for the UAT cache cluster and verify end-to-end cache use. Implement the cache monitoring baseline and note the change for 'CacheAPI.ExternalSystemAuthHeader'.",
        "actions": [
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
                "cache_integration_verified: True"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A91",
        "instruction": "You are Priya Shah from Platform. While in UAT, strengthen Commerce to comply with the standard internal network, make ElastiCache private, activate AUTH and TLS on the UAT cache cluster without implementing new header secret rotation, transfer the cache partition 'dcomm' to 'v14', clear 'offer:USB-C Hub', 'offer:Thunderbolt Docking Station', and 'offer:WELCOME5', apply the baseline for cache monitoring (dashboard, Errors alarm, SMOKE), and document the modification for 'dcomm-v14'.",
        "actions": [
            {
                "name": "GetEnvironmentNetworkDefaults",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-uat-a",
                        "subnet-uat-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        443,
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetCacheCluster",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetRedisAuthAndTls",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v14"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v14",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                "applied_version: v14",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A92",
        "instruction": "You are Dana Brooks from API. In UAT, activate 'Catalog v5' version '5.0.0' from 'blob_catalog_500' on 'catalog-v5' ensuring baseline monitoring on the gateway and sampling set at 0.10; conduct 'SMOKE' and document the deployment for 'spec-catalog-v5-5-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Catalog v5",
                    "spec_version": "5.0.0",
                    "spec_blob_id": "blob_catalog_500"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "catalog-v5",
                    "environment": "UAT"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-catalog-v5-5-0-0",
                    "gateway_id": "dcg-catalog-v5-uat"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-catalog-v5-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-catalog-v5-5-0-0",
                    "environment": "UAT",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-catalog-v5-5-0-0",
                "dcg_id: dcg-catalog-v5-uat",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api",
                "alarm_id: al-dcg-catalog-v5-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A93",
        "instruction": "You are Luis Ortega from Identity. During UAT, update the connected app precisely named 'Commerce API' with the settings api, refresh_token, openid and callback https://acme.example/callback, and ensure it is validated and monitored at baseline. Document the update for 'app-commerce-api'.",
        "actions": [
            {
                "name": "ConfigureConnectedAppOauth",
                "arguments": {
                    "app_name_hint": "Commerce API",
                    "scopes": [
                        "api",
                        "refresh_token",
                        "openid"
                    ],
                    "callback_urls": [
                        "https://acme.example/callback"
                    ]
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api"
                },
            },
            {
                "name": "CreateSecretFor",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-commerce-api"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth"
                }
            }
        ],
        "outputs": [
                "app_id: app-commerce-api",
                "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
                "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A94",
        "instruction": "You are Amira Patel from Networking. In PROD, ensure that private ElastiCache access is available and both Checkout Gateway and Cache Integration are secured according to the standard internal network. Permit Checkout Gateway to allow 443 exclusively; ensure Cache Integration allows 6379 exclusively. Apply baseline cache monitoring and document the alteration for 'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-prod-a",
                        "subnet-prod-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Checkout Gateway"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [
                        443
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "PROD",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "PROD"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                "dashboard_name: dash-prod-cache",
                "alarm_id: al-vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A95",
        "instruction": "You are Kelly Nguyen from Sales Ops. In UAT, ensure the pricebooks are synchronized for retail and wholesale, assign the 'B2B Wholesale' tier to 'david.c@email.com', and validate using a cart containing 2\u00d7 AC-USBC-HUB and 1\u00d7 HW-TB-DOCK with B2BVOLUME15 and STANDARD shipping. Set 'Standard Retail' to 62.0 and 208.0; assign 'B2B Wholesale' to 56.0 and 182.0 (applicable for AC-USBC-HUB and HW-TB-DOCK). Conduct 'Pricing-SMOKE' and document the update for 'B2B Wholesale'.",
        "actions": [
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "Standard Retail"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 62.0
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 208.0
                        }
                    ]
                },
            },
            {
                "name": "GetPricebookByName",
                "arguments": {
                    "pricebook_name": "B2B Wholesale"
                },
            },
            {
                "name": "UpsertPricebookEntriesBatch",
                "arguments": {
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "unit_price": 56.0
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "unit_price": 182.0
                        }
                    ]
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "SetPricingTierForCustomer",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "pricing_tier_name": "B2B Wholesale"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "david.c@email.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 2
                        },
                        {
                            "product_code": "HW-TB-DOCK",
                            "qty": 1
                        }
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Pricing-SMOKE"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "upserted_count: 2",
                "applied_tier: B2B Wholesale",
                "cart_id: cart-cust-david-c-email-com-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A96",
        "instruction": "Assume the role of Raj Patel from Personalization. Within UAT, aim to modify the shipper for VIP to prefer EXPRESS. Ensure both VIP and new customers with WELCOME5 are given priority, followed by verification using a quick cart for 'trialshopper@example.com'. Keep the experience observable with an 'api' dashboard, and document the adjustment for 'ctx-vip-prefer-express'.",
        "actions": [
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {
                        "shipping_preference": "EXPRESS"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "UpsertContextRule",
                "arguments": {
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {
                        "shipping_preference": "STANDARD"
                    },
                    "bind_to_offer_code": "WELCOME5"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE"
                },
            },
            {
                "name": "GetOfferByCode",
                "arguments": {
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "CreateCartWithItems",
                "arguments": {
                    "customer_email": "trialshopper@example.com",
                    "items": [
                        {
                            "product_code": "AC-USBC-HUB",
                            "qty": 1
                        }
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "api"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization"
                }
            }
        ],
        "outputs": [
                "context_rule_id: ctx-vip-prefer-express",
                "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-api"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A97",
        "instruction": "Act as Rafael Kim from SRE. Within the UAT environment, ensure the Commerce API cache warmer operates every 15 minutes under baseline supervision. Implement the bundle 'bundle_cachewarmer_v1' to run a 'cache_warmer' function, perform a rapid metadata warm, apply a sampling rate of 0.10, and note the change for 'fn-commerce-api-cache_warmer-uat'.",
        "actions": [
            {
                "name": "DeployLambdaFunction",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer"
                },
            },
            {
                "name": "CreateLambdaSchedule",
                "arguments": {
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
                "run_id: run-smoke-uat-2025-08-06t12-00-00z"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A98",
        "instruction": "Take on the responsibilities of Dana Brooks from API. For DEV, deploy 'Payments v3' version '3.0.0' sourced from 'blob_payments_300' on 'payments-v3' with baseline observation. Log the deployment process under 'spec-payments-v3-3-0-0'.",
        "actions": [
            {
                "name": "PublishOpenapiSpec",
                "arguments": {
                    "spec_name": "Payments v3",
                    "spec_version": "3.0.0",
                    "spec_blob_id": "blob_payments_300"
                },
            },
            {
                "name": "EnableDigitalCommerceGateway",
                "arguments": {
                    "api_group_name": "payments-v3",
                    "environment": "DEV"
                },
            },
            {
                "name": "RegisterApiEndpoints",
                "arguments": {
                    "spec_id": "spec-payments-v3-3-0-0",
                    "gateway_id": "dcg-payments-v3-dev"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "DEV"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "DEV",
                    "purpose": "api"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcg-payments-v3-dev",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "spec-payments-v3-3-0-0",
                    "environment": "DEV",
                    "change_type": "rollout"
                }
            }
        ],
        "outputs": [
                "spec_id: spec-payments-v3-3-0-0",
                "dcg_id: dcg-payments-v3-dev",
                "run_id: run-smoke-dev-2025-08-06t12-00-00z",
                "dashboard_name: dash-dev-api",
                "alarm_id: al-dcg-payments-v3-dev-5xxerrorrate-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A99",
        "instruction": "Fulfill the duties of Priya Shah from Platform. In UAT, advance the cache partition, broadly invalidate keys for key offers ('offer:USB-C Hub', 'offer:Thunderbolt Docking Station', 'offer:WELCOME5', 'offer:WINTER20', 'offer:B2BVOLUME15'), establish nightly maintenance, execute both warms, set sampling at baseline, ensure cache monitoring is at baseline, and document the alteration for 'dcomm-v15'.",
        "actions": [
            {
                "name": "SetCachePartitionKey",
                "arguments": {
                    "partition_key": "dcomm",
                    "version": "v15"
                },
            },
            {
                "name": "InvalidateCacheByKeys",
                "arguments": {
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5",
                        "offer:WINTER20",
                        "offer:B2BVOLUME15"
                    ]
                },
            },
            {
                "name": "ManageCacheMaintenance",
                "arguments": {
                    "environment": "UAT",
                    "action": "create"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "populate"
                },
            },
            {
                "name": "ConfigureTraceSampling",
                "arguments": {
                    "sample_rate": 0.1
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "dcomm-v15",
                    "environment": "UAT",
                    "change_type": "ops"
                }
            }
        ],
        "outputs": [
                "applied_version: v15",
                "schedule_id: cm-uat",
                "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
    ,
    {
        "annotator": aws_v1,
        "user_id": "task_A100",
        "instruction": "Handle the tasks of Amira Patel from Networking. Within UAT, set up ElastiCache private access and verify compliance of both the Commerce API and Cache Integration services with the standard internal network. Apply the cache monitoring baseline and record the modification for 'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b'.",
        "actions": [
            {
                "name": "CreateInterfaceEndpoint",
                "arguments": {
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": [
                        "subnet-a",
                        "subnet-b"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Commerce API"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [
                        443,
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "GetServiceSecurityGroup",
                "arguments": {
                    "environment": "UAT",
                    "service_name": "Cache Integration"
                },
            },
            {
                "name": "UpdateSecurityGroupRuleset",
                "arguments": {
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [
                        6379
                    ],
                    "allowlist_cidrs": [
                        "10.0.0.0/16"
                    ]
                },
            },
            {
                "name": "RunCacheWarmJobs",
                "arguments": {
                    "mode": "metadata"
                },
            },
            {
                "name": "RunTestCollection",
                "arguments": {
                    "environment": "UAT",
                    "collection_name": "SMOKE"
                },
            },
            {
                "name": "CreateCloudwatchDashboard",
                "arguments": {
                    "environment": "UAT",
                    "purpose": "cache"
                },
            },
            {
                "name": "CreateCloudwatchAlarm",
                "arguments": {
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold"
                },
            },
            {
                "name": "RecordApiChangeLog",
                "arguments": {
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                    "environment": "UAT",
                    "change_type": "networking"
                }
            }
        ],
        "outputs": [
                "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                "dashboard_name: dash-uat-cache",
                "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold"
        ]
    }
]
