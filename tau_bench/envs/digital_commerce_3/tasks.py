
tasks = [
    {
        "annotator": v3,
        "user_id": "task_001",
        "instruction": "With 'david.c@email.com', ensure Stripe is active for 'MERCH_001', limit checkout traffic to 50 rpm, establish a CDN in US East, and identify similar products for your profile. Provide a straightforward confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_001",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/checkout",
                    "rate_limit": 50
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/checkout"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories",
                    "account_id": "107"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "208",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_002",
        "instruction": "With 'maria.garcia@globaltech.com', initiate the 'High-Value-90d' segment (min_orders=5, period_days=90) and trigger 'HV-10'. Provide a straightforward confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "High-Value-90d",
                    "criteria": {
                        "min_orders": 5,
                        "period_days": 90
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "HV-10",
                    "target_segment": "High-Value-90d",
                    "discount_percentage": 10
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_003",
        "instruction": "Utilizing 'david.c@email.com', incorporate supplier 'ProMouse Co' (support@promouse.example), replenish 'Pro Gaming Mouse' by 25, adjust its list price to 89.99, deploy Akamai in 'us-west-2', and confirm the inventory update through the audit log. Provide a straightforward confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "support@promouse.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1013",
                    "quantity_adjustment": 25,
                    "movement_type": "restock"
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1013"
                    ],
                    "update_data": {
                        "list_price": 89.99
                    }
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "inventory_updated",
                    "resource_id": "1013"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Akamai",
                    "region": "us-west-2"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_004",
        "instruction": "With 'emily.w@email.com', have the 'dcomm-dev-redis' cache set up and assured to be ready, then purchase 1 'USB-C Hub' using WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_005",
        "instruction": "With 'kevin.lee@starlight.net', activate connected app 'APP900' with permissions ['read','write'] and scopes ['api','refresh_token'], and apply a 600 rpm restriction on '/oauth/token' with confirmation. Provide a straightforward confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP900",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "refresh_token"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP900"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/oauth/token",
                    "rate_limit": 600
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/oauth/token"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_006",
        "instruction": "Handle the activation of Adyen for merchant 'MERCH_002' using 'david.chen@quantum.co', then assign the EU\u2011Std shipping rule (using the exact rule name) to your profile without enabling tracking. Confirm the shipping-rule update in the audit log and request recommendations for similar_products for your profile. Provide a simple confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.chen@quantum.co"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_002",
                    "supported_currencies": [
                        "USD",
                        "EUR"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": false,
                    "customer_id": "206"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "shipping_rule_configured"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "206",
                    "recommendation_type": "similar_products"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_007",
        "instruction": "Coordinate the full backup processing with storage_location 's3' using 'david.c@email.com', retrieve its backup information, and verify 'backup_processed' event in the audit log; subsequently, add supplier 'USB Hub Works' (hello@usbhub.example), allocate 1 'Pro Gaming Mouse' by reducing the on\u2011hand quantity by 1 using movement_type 'reserve', and finally purchase 1 'Pro Gaming Mouse' from the Computer Accessories catalog with WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "full",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "USB Hub Works",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "hello@usbhub.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1013",
                    "quantity_adjustment": -1,
                    "movement_type": "reserve"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "backup_processed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_008",
        "instruction": "Handle feedback recording ('Order arrived early', rating 5), award 50 loyalty points, then make a purchase of 1 'Ergo Laptop Stand' using WELCOME5 with 'tom.j@email.com'. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "208",
                    "feedback_text": "Order arrived early",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "208",
                    "action": "add",
                    "points": 50
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_009",
        "instruction": "Coordinate the preparation of 'dcomm-uat-redis' cache for production using 'david.c@email.com' by initially establishing a security\u2011group rule allowing Redis traffic (port 6379/TCP from 10.0.0.0/16) on the authorized security group, then optimize/reconcile the group according to policy. Update the cache status, verify readiness, and proceed to buy 1 'USB\u2011C Hub' from the Computer Accessories catalog with B2BVOLUME15. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "allowed_cidr": "10.0.0.0/16",
                    "target_port": 6379
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "endpoint_url": "redis://dcomm-uat-redis.cache.amazonaws.com:6379"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_010",
        "instruction": "Arrange to launch the 'RECS-7' promotion (7% to all), configure '/products' to 200 rpm, and view bought_together recommendations for your profile using 'kevin.lee@starlight.net'. Return a simple confirmation.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RECS-7",
                    "target_segment": "all",
                    "discount_percentage": 7
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "210",
                    "recommendation_type": "bought_together"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/products",
                    "rate_limit": 200
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/products"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "recommendations_generated"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": []
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_011",
        "instruction": "As Nora Patel at Digital Solutions, utilize 'chloe.davis@email.com' to purchase 1 \u2018Mechanical Keyboard\u2019 from the Computer Accessories category (in stock), apply the WELCOME5 discount code, and confirm the order through the order_created audit. Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.davis@email.com"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "211",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "order_created",
                    "resource_id": "9017"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_012",
        "instruction": "With 's.adams@pioneercorp.com', ensure Adyen is activated for 'MERCH_002', implement the EU-Std shipping rule on your profile with tracking disabled, then purchase 1 'USB-C Hub' using WELCOME5; validate the gateway setup in the audit log (event 'payment_gateway_configured'). Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_002",
                    "supported_currencies": [
                        "USD",
                        "EUR"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": false,
                    "customer_id": "213"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_013",
        "instruction": "Employ 't.jenkins@pioneercorp.com' to make the 'dcomm-uat-redis' cache ready for production by configuring the cluster, setting up a security\u2011group rule for Redis (6379/TCP from 10.0.0.0/16), optimizing the security group, updating the cache cluster status, and obtaining the cache cluster details. Subsequently, locate the product via the Computer Accessories catalog (not by name) and purchase 1 'USB\u2011C Hub' using the WINTER20 discount. Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "t.jenkins@pioneercorp.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "214",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_014",
        "instruction": "Utilize 'kevin.lee@starlight.net', to enable the connected app 'APP901' with permissions ['read'] and scopes ['api'], then proceed to purchase 1 'Wireless Mouse' and 1 'USB-C Hub' using WELCOME5.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP901",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        },
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_015",
        "instruction": "With 'chloe.d@email.com', secure the 'dcomm-dev-redis' cache according to policy, activate the connected app 'APP901' with permissions ['read'] and scopes ['api'], set '/search' to 150 rpm and confirm, then proceed to purchase 1 'Pro Gaming Mouse' using WELCOME5. Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP901",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/search",
                    "rate_limit": 150
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/search"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "212",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_016",
        "instruction": "With 'john.doe@globaltech.com', ensure '/auth' is set to 300 rpm and confirmed (event 'rate_limit_configured'), use an incremental backup stored at 's3', then purchase 1 '4K Webcam' with WELCOME5. Confirm with an audit log tagged rate_limit_configured.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/auth",
                    "rate_limit": 300
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/auth"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "rate_limit_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_017",
        "instruction": "Employing 'maria.garcia@globaltech.com', define a customer segment labeled 'VIP' for customers whose lifetime_spend_usd exceeds 1000. Roll out the campaign 'VIP-15' targeting the 'VIP' segment, then acquire 1 'Pro Gaming Mouse' from the Computer Accessories catalog using the WINTER20 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "VIP",
                    "criteria": {
                        "lifetime_spend_usd": 1000
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "VIP-15",
                    "target_segment": "VIP",
                    "discount_percentage": 15
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_018",
        "instruction": "With 'emily.white@innovate.com', document feedback ('Hub arrived fast', rating 5), make an adjustment to the loyalty program by adding 40 points (action 'adjust_points'), examine customer behavior over the recent 30 days (analysis_period '30d'), and then purchase 1 'USB\u2011C Hub' from the Computer Accessories catalog with the WELCOME5 discount. Lastly, affirm the feedback activity in the audit log. Give back the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "203",
                    "feedback_text": "Hub arrived fast",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "203",
                    "action": "adjust_points",
                    "points": 40
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "203",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "feedback_processed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_019",
        "instruction": "With 'emily.w@email.com', establish Braintree for 'MERCH_003', implement the 'US-Priority' shipping rule with tracking for your profile, configure '/returns' to 20 rpm and confirm, then obtain 1 'Wireless Mouse' and 1 'USB-C Hub' with WINTER20. Supply the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Braintree",
                    "merchant_id": "MERCH_003",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "204"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/returns",
                    "rate_limit": 20
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/returns"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        },
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_020",
        "instruction": "Using 'tom.j@email.com', set up Cloudflare in 'us-east-1' and activate the connected app 'APP902' with permissions ['read','write'] and scopes ['api','openid']; identify the product through the Computer Accessories catalog (not by name), then purchase 1 'Pro Gaming Mouse' with WELCOME5; validate the CDN configuration in the audit log (event 'cdn_configured'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Cloudflare",
                    "region": "us-east-1"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "205",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_021",
        "instruction": "Handle 'john.doe@globaltech.com', ensure Stripe is activated for 'MERCH_010', adjust '/checkout' to 80 rpm, verify the setup, and purchase 1 'USB-C Hub' using WELCOME5; verify the payment-gateway configuration in the audit log. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_010",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/checkout",
                    "rate_limit": 80
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/checkout"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_022",
        "instruction": "Coordinate via 'maria.garcia@globaltech.com', configure CloudFront in 'us-east-1', proceeding to buy 2 'Wireless Mouse' from the Computer Accessories catalog using WINTER20. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_023",
        "instruction": "You are Maria Garcia at Innovate Corp. With 'emily.white@innovate.com', assess your last '30d' activity, initiate campaign 'SPRING9' (9% to 'all'), then purchase 1 Ergo Laptop Stand with the welcome discount, utilizing the next order id and document the promotion audit. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "203",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "SPRING9",
                    "target_segment": "all",
                    "discount_percentage": 9
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_024",
        "instruction": "Through 'emily.w@email.com', establish the 'High-Value-90d' segment (min_orders=5, period_days=90), apply the 'US-Std' shipping rule to your profile, then proceed to purchase 1 'Pro Gaming Mouse' with B2BVOLUME15. Use only the new order and cart numbers for the purchase without including additional order parameters. Document the shipping-rule audit. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "High-Value-90d",
                    "criteria": {
                        "min_orders": 5,
                        "period_days": 90
                    }
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "204"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "shipping_rule_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_025",
        "instruction": "Utilizing 'tom.j@email.com', incorporate supplier 'ProMouse Co' (support@promouse.example), replenish 'Pro Gaming Mouse' by 20, and purchase 2 'Pro Gaming Mouse' with WELCOME5; log the inventory update in the audit log (event 'inventory_updated'). Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "support@promouse.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1013",
                    "quantity_adjustment": 20,
                    "movement_type": "restock"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "inventory_updated"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_026",
        "instruction": "With 'david.chen@quantum.co', ensure the 'dcomm-dev-redis' cache is configured for internal-only access by adding a security-group rule for Redis (6379/TCP from 10.0.0.0/16) and optimizing the security group as per policy. Make sure to verify the security setup via the audit log (event 'security_group_optimized') prior to purchasing. Afterwards, buy 2 'Wireless Mouse' from the Computer Accessories category using the WINTER20 discount if applicable. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.chen@quantum.co"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "security_group_optimized",
                    "resource_id": "sg-0123456789abcdef0"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_027",
        "instruction": "Using 'emily.w@email.com', make sure the connected app 'APP900' is enabled with permissions ['read','write'] and scopes ['api','refresh_token'], and then purchase 3 'Wireless Mouse' with B2BVOLUME15; ",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP900",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "refresh_token"
                    ]
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 3
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_028",
        "instruction": "With 'tom.j@email.com', proceed to execute an incremental backup with storage_location 's3', gather backup data, confirm the backup in the audit log (event 'backup_processed'), and then buy 1 'Ergo Laptop Stand' from the Computer Accessories catalog using WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "backup_processed"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_029",
        "instruction": "Employ 'david.c@email.com' to set '/products' to 220 rpm, configure Fastly in 'us-east-1', and then purchase 2 'Wireless Mouse' with B2BVOLUME15. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/products",
                    "rate_limit": 220
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/products"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Fastly",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                {}
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_030",
        "instruction": "Utilize 'kevin.lee@starlight.net' to find the '4K Webcam' in the Computer Accessories catalog, review bought_together recommendations, and then purchase 1 unit with WINTER20; verify recommendations in the audit log. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "4K Webcam"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "210",
                    "recommendation_type": "bought_together"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "recommendations_generated"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_031",
        "instruction": "Employ 'tom.j@email.com' to characterize the customer segment 'Returning-30d' (customers with at least 2 orders in the last 30 days), examine 30\u2011day behavior, initiate the 'RET-10' promotion (10% discount) aimed at this segment, and set the US\u2011Std shipping rule (exact name) with tracking for your profile. Next, acquire one Wireless Mouse through the Computer Accessories catalog by applying the WELCOME5 discount. Confirm the promotion via the audit log. Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-30d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 30
                    }
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "205",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-10",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 10
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "205"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_032",
        "instruction": "As Mike Rivera representing Frontier Industries and using 's.adams@pioneercorp.com', initially create or update the 'Returning-30d' customer segment (customers with at least 2 orders in the last 30 days). Then, initiate the 'RET-8' campaign (8% discount) focusing on this segment. Afterwards, buy 1 USB\u2011C Hub through the Computer Accessories catalog applying the WELCOME5 discount, and confirm the promotion via the audit log. Provide the order id in return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-30d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 30
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-8",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 8
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_033",
        "instruction": "With 't.jenkins@pioneercorp.com', arrange for payments through Adyen for 'MERCH_011' for the US including loyalty enrollment, then proceed to purchase 1 'USB-C Hub' with WELCOME5. Submit the order id as the return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "t.jenkins@pioneercorp.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_011",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "214",
                    "action": "enroll",
                    "points": 0
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "214",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_034",
        "instruction": "Utilizing 'kevin.lee@starlight.net', aim to add supplier 'USB Hub Works' (hello@usbhub.example), align the 'USB-C Hub' list price to 149.00 utilizing the price update, then purchase 2 'USB-C Hub' with B2BVOLUME15; log the bulk update in the audit log (event 'bulk_product_update'). Provide the order id as the return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "USB Hub Works",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "hello@usbhub.example"
                    }
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1002"
                    ],
                    "update_data": {
                        "list_price": 149.0
                    }
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "bulk_product_update"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_035",
        "instruction": "With 'chloe.d@email.com', establish the US\u2011Std shipping rule for your profile with tracking disabled, configure Akamai in 'us-west-2', then purchase 1 'Mechanical Keyboard' from the Computer Accessories catalog using WELCOME5. Record the shipping-rule audit (event 'shipping_rule_configured'). Provide the order id as the return.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": false,
                    "customer_id": "212"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Akamai",
                    "region": "us-west-2"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "212",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_036",
        "instruction": "As Maria Garcia at GlobalTech, manage the 'dcomm-uat-redis' cache preparation for production by setting it up and modifying its network settings to comply with internal access standards. After confirming the cache readiness, procure a USB\u2011C Hub from the Computer Accessories catalog applying the WINTER20 discount. Provide the order id obtained.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "endpoint_url": "redis://dcomm-uat-redis.cache.amazonaws.com:6379"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_037",
        "instruction": "Through 'maria.garcia@globaltech.com', initiate a swift retention strategy: define or renew the 'Returning-30d' customer segment (customers with \u22652 orders in the past 30 days), examine 30\u2011day activity, roll out the 'RET-7' promotion (7% discount) for that group, establish the US\u2011Std shipping rule with tracking for your profile, arrange CloudFront in 'us-east-1', impose an API rate limit of 300 rpm for the '/auth' endpoint and verify it, process an incremental backup to s3 and gather its details, and log the promotion via the audit log. No need to make a purchase.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-30d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 30
                    }
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "202",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-7",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 7
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "202"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/auth",
                    "rate_limit": 300
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/auth"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_038",
        "instruction": "With 'emily.white@innovate.com', proceed to activate the connected app 'APP901' with read\u2011only access and then validate the setup by fetching the app's security information. Thereafter, impose a 500 rpm rate limit on '/oauth/token' and confirm the implementation, and ultimately purchase 1 'USB\u2011C Hub' from the Computer Accessories catalog. Provide the order id obtained.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP901",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP901"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/oauth/token",
                    "rate_limit": 500
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/oauth/token"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_039",
        "instruction": "Utilizing 'emily.w@email.com', log feedback ('Site loads fast', rating 5), adjust 30 loyalty points, then order 1 'Wireless Mouse' using WELCOME5; record the loyalty update in the audit log (event 'loyalty_program_activity'). Provide the order id obtained.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "204",
                    "feedback_text": "Site loads fast",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "204",
                    "action": "adjust_points",
                    "points": 30
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "loyalty_program_activity"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_040",
        "instruction": "With 'emily.w@email.com', ensure 'dcomm-dev-redis' cache access is limited to internal traffic per policy, then place an order for 1 'Pro Gaming Mouse' from the Computer Accessories catalog with WELCOME5. Provide the order id obtained.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_041",
        "instruction": "Handle the configuration for 'john.doe@globaltech.com' by setting '/pricing' to 140 rpm, enabling and securing the connected app 'APP902', and selecting US-Std shipping for your profile. Then purchase 1 'Wireless Mouse' using WELCOME5. Provide the order id upon completion.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "201"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/pricing",
                    "rate_limit": 140
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/pricing"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "201",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "app_security_updated",
                    "resource_id": "APP902"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_042",
        "instruction": "For 'maria.garcia@globaltech.com', coordinate the configuration of Adyen payments for merchant 'MERCH_020' with currencies ['USD','EUR'], and adjust the 'Ergo Laptop Stand' list price to 56.25. Following this, acquire 1 'Ergo Laptop Stand' utilizing the WINTER20 discount. Return the order id when done.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_020",
                    "supported_currencies": [
                        "USD",
                        "EUR"
                    ]
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1010"
                    ],
                    "update_data": {
                        "list_price": 56.25
                    }
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_043",
        "instruction": "With 'john.doe@globaltech.com', prepare the 'dcomm-dev-redis' cache in accordance with production policy, confirming it afterwards. Place an order for 1 'USB-C Hub' and 1 'Wireless Mouse' from the Computer Accessories catalog using WELCOME5. Provide the order id after ordering.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_044",
        "instruction": "Manage the addition of supplier 'KeyWorks' (contact 'keys@keyworks.example') for 'emily.w@email.com', restock 8 units of 'Mechanical Keyboard', set and affirm the API rate limit on '/payments' at 120 rpm, then execute a full backup to storage_location 's3', noting its metadata. Afterwards, purchase 1 'Mechanical Keyboard' via Computer Accessories catalog with WELCOME5, and log the inventory change as 'inventory_updated' in the audit log. Provide the order id upon completion.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "KeyWorks",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "keys@keyworks.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1017",
                    "quantity_adjustment": 8,
                    "movement_type": "restock"
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "Mechanical Keyboard"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/payments",
                    "rate_limit": 120
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/payments"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "full",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "inventory_updated"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_045",
        "instruction": "For 'tom.j@email.com', reference an incremental s3 backup, define the 'Returning-30d' segment, execute 'RET-12', and buy 1 'Wireless Mouse' using WELCOME5. Provide the order id when done.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-30d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 30
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-12",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 12
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_046",
        "instruction": "Utilizing 'david.chen@quantum.co', ensure the app 'APP903' is activated with permissions ['read','write'] and scopes ['api','openid']. Set '/oauth/token' to 450 rpm and confirm. Afterward, purchase 2 'USB-C Hub' using B2BVOLUME15. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.chen@quantum.co"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP903",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP903"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/oauth/token",
                    "rate_limit": 450
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/oauth/token"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_047",
        "instruction": "With 'emily.w@email.com', establish the EU-Express shipping rule with tracking enabled for your profile, then obtain bought_together recommendations. Next, purchase 1 'USB-C Hub' with WELCOME5. Securely log the shipping-rule audit (event 'shipping_rule_configured'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "EU-Express",
                    "shipping_zone": "EU",
                    "tracking_enabled": true,
                    "customer_id": "207"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "207",
                    "recommendation_type": "bought_together"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "shipping_rule_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_048",
        "instruction": "From 'tom.j@email.com', examine 60-day behavior, initiate 'LAPS-10' for everyone, and configure Akamai in 'us-west-2'. Next, acquire 1 'Ergo Laptop Stand' using WELCOME5 and document the promotion audit. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "208",
                    "analysis_period": "60d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "LAPS-10",
                    "target_segment": "all",
                    "discount_percentage": 10
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Akamai",
                    "region": "us-west-2"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_049",
        "instruction": "By using 'david.c@email.com', prepare the 'dcomm-uat-redis' cache for exclusive internal access by configuring the cluster. Add a security-group rule for Redis (6379/TCP from 10.0.0.0/16), reconcile and optimize the group, set the endpoint URL to redis://dcomm-uat-redis.cache.amazonaws.com:6379, and confirm through cluster info and an audit log entry (event 'cache_configured'). Then, procure 2 'USB-C Hub' via the Computer Accessories catalog, utilizing the B2BVOLUME15 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "allowed_cidr": "10.0.0.0/16",
                    "target_port": 6379
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "endpoint_url": "redis://dcomm-uat-redis.cache.amazonaws.com:6379"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cache_configured",
                    "resource_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_050",
        "instruction": "Employ 'kevin.lee@starlight.net' to add supplier 'CamVision' (sales@camvision.example), standardize the '4K Webcam' list price to 179.00 (product_id '1018'). Then, purchase 1 '4K Webcam' with WELCOME5 and record the bulk update in the audit log (event 'bulk_product_update'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "CamVision",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "sales@camvision.example"
                    }
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1018"
                    ],
                    "update_data": {
                        "list_price": 179.0
                    }
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "4K Webcam"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "bulk_product_update"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_051",
        "instruction": "Utilize 'emily.w@email.com' to incorporate supplier 'KeyWorks' (keys@keyworks.example), replenish 'Mechanical Keyboard' with 8 units, harmonize its list price to 169.00, then purchase 1 'Mechanical Keyboard' using WELCOME5. Document the bulk update in the audit log (event 'bulk_product_update'). Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "KeyWorks",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "keys@keyworks.example"
                    }
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1017",
                    "quantity_adjustment": 8,
                    "movement_type": "restock"
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1017"
                    ],
                    "update_data": {
                        "list_price": 169.0
                    }
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "bulk_product_update"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_052",
        "instruction": "Employ 'john.doe@globaltech.com' to ensure Redis access security following policy on cluster 'dcomm-dev-redis', then order 1 'USB-C Hub' with WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "status": "available",
                    "endpoint_url": "redis://dcomm-dev-redis.cache.amazonaws.com:6379",
                    "security_group_id": "sg-0123456789abcdef0"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_053",
        "instruction": "Engage 't.jenkins@pioneercorp.com' to carry out an incremental backup with storage_location 's3' noted, set '/search' to 190 rpm, then acquire 1 'Pro Gaming Mouse' utilizing WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "t.jenkins@pioneercorp.com"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/search",
                    "rate_limit": 190
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/search"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "214",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "rate_limit_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_054",
        "instruction": "As a lifecycle marketer, with 'john.doe@globaltech.com', establish a customer segment named 'VIP' for those with a lifetime spend of $1,000 or more. Initiate the 'VIP-15' campaign aimed at the 'VIP' segment, assess similar product suggestions for your profile, and place a test order for one Pro Gaming Mouse with the WINTER20 discount. Verify via the audit log that the promotion was noted. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "VIP",
                    "criteria": {
                        "lifetime_spend_usd": 1000
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "VIP-15",
                    "target_segment": "VIP",
                    "discount_percentage": 15
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "201",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_055",
        "instruction": "With 'john.doe@globaltech.com', ensure the 'dcomm-dev-redis' cache is secure following policy by initially permitting temporary TLS on port 6380/TCP from 10.0.0.0/16 on the approved security group, then restoring regular Redis access on port 6379/TCP for 10.0.0.0/16. Complete the remaining purchase as outlined (via the Computer Accessories catalog with WELCOME5) and check the security enhancement via the audit log. Then, buy one product, 1013, from Computer Accessories using WELCOME5.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6380,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "security_group_optimized",
                    "resource_id": "sg-0123456789abcdef0"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_056",
        "instruction": "As Mike Rivera from WorldWide Systems, utilize 'maria.garcia@globaltech.com' to set up CDN 'Fastly' in 'us-east-1'; activate the connected app 'APP904' granting permissions ['read'] and scopes ['api'] and ensure its security; afterward, order 1 Ergo Laptop Stand applying the WELCOME5 discount using the platform's upcoming IDs, and inspect the CDN set-up through an audit. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Fastly",
                    "region": "us-east-1"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP904",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP904"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_057",
        "instruction": "By way of 'emily.white@innovate.com', initiate adding supplier 'HubWorld' (with supplier_data.contact_email 'hi@hubworld.example'), allocate 2 units of 'USB\u2011C Hub' (product_id '1002', movement_type 'reserve') to reduce on\u2011hand stock, request similar_products recommendations tailored to your profile, and subsequently purchase 2 'USB\u2011C Hub' from the Computer Accessories catalog using the B2BVOLUME15 discount. Conclude by confirming the supplier management through an audit log. Deliver the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "HubWorld",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "hi@hubworld.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1002",
                    "quantity_adjustment": -2,
                    "movement_type": "reserve"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "203",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "supplier_managed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_058",
        "instruction": "Employ 'emily.w@email.com' to assess the preceding 30 days and initiate 'MOUSE-5' (5% universally), subsequently obtain 1 'Wireless Mouse' from the Computer Accessories catalog using WELCOME5. Submit the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "204",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "MOUSE-5",
                    "target_segment": "all",
                    "discount_percentage": 5
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_059",
        "instruction": "With 'tom.j@email.com', configure '/returns' to maintain 30 rpm, document feedback ('Return experience was smooth', rating 5), sign up for the loyalty program, afterward purchase 1 'Wireless Mouse' with WELCOME5 and authenticate the feedback through an audit. Deliver the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/returns",
                    "rate_limit": 30
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/returns"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "205",
                    "feedback_text": "Return experience was smooth",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "205",
                    "action": "enroll"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "feedback_processed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_060",
        "instruction": "Under 'david.chen@quantum.co', arrange the 'dcomm-dev-redis' cache, provisionally permit 6379/TCP from 0.0.0.0/0, then restrict access to 10.0.0.0/16 according to policy, subsequently procure 1 'Wireless Mouse' from the Computer Accessories catalog with WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.chen@quantum.co"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "0.0.0.0/0"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "security_group_optimized",
                    "resource_id": "sg-0123456789abcdef0"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_061",
        "instruction": "With 'john.doe@globaltech.com', configure Braintree for 'MERCH_030', establish 'US-Priority' shipping with tracking for your profile, then purchase 1 'USB-C Hub' and 1 'Pro Gaming Mouse' using WELCOME5; confirm the gateway setup in the audit log (event 'payment_gateway_configured'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Braintree",
                    "merchant_id": "MERCH_030",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "201"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_062",
        "instruction": "Utilizing 'maria.garcia@globaltech.com', configure '/search' for 180 rpm, and acquire 2 'Wireless Mouse' using WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/search",
                    "rate_limit": 180
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/search"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_063",
        "instruction": "With 'emily.white@innovate.com', ready the 'dcomm-uat-redis' cache environment for production by setting up the cluster (node_type cache.r5.large, num_cache_nodes 3), adding a security-group rule for Redis (6379/TCP from 10.0.0.0/16) and optimizing it, updating the cache cluster status and endpoint URL (redis://dcomm-uat-redis.cache.amazonaws.com:6379), obtaining the cache cluster information, and verifying the security optimization in the audit log. Then, purchase 1 'USB-C Hub' from the Computer Accessories catalog with the WELCOME5 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "status": "available",
                    "endpoint_url": "redis://dcomm-uat-redis.cache.amazonaws.com:6379",
                    "security_group_id": "sg-0123456789abcdef0"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "security_group_optimized",
                    "resource_id": "sg-0123456789abcdef0"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_064",
        "instruction": "Using 'emily.w@email.com', initiate the onboarding for ErgoWorks, adjust the Ergo Laptop Stand to the corrected list price of 189.99, and buy one Ergo Laptop Stand with WELCOME5 employing the upcoming IDs, logging the bulk-update audit. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "ErgoWorks",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "ops@ergoworks.example"
                    }
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1010"
                    ],
                    "update_data": {
                        "list_price": 189.99
                    }
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "Ergo Laptop Stand"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "bulk_product_update"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_065",
        "instruction": "With 'tom.j@email.com', implement an incremental backup process referencing storage_location 's3', adjust '/auth' to 320 rpm and confirm, configure CloudFront in 'us-east-1', set the 'US-Std' shipping rule for your profile with tracking turned on.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ProcessDataBackup",
                "arguments": {
                    "backup_type": "incremental",
                    "storage_location": "s3"
                },
            },
            {
                "name": "GetDataBackupInfo",
                "arguments": {
                {}
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/auth",
                    "rate_limit": 320
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/auth"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "205"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "backup_processed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_066",
        "instruction": "Handle the enabling process for the connected app 'APP905' with read and write permissions and OAuth scopes ['api','refresh_token'] using 'david.chen@quantum.co'. Confirm its security configuration by checking the connected app security details. After that, request similar product recommendations for your profile, and proceed to purchase 2 'USB\u2011C Hub' items from the Computer Accessories catalog applying the B2BVOLUME15 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.chen@quantum.co"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP905",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "refresh_token"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP905"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "206",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_067",
        "instruction": "With 'emily.w@email.com', arrange for the EU\u2011Std shipping rule (exact name) to be set for your profile with tracking disabled. Replenish 30 units of the 'USB\u2011C Hub' inventory, and then buy three 'USB\u2011C Hub' units from the Computer Accessories catalog using the B2BVOLUME15 discount. Check the shipping\u2011rule arrangement via the audit log and deliver the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": false,
                    "customer_id": "207"
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1002",
                    "quantity_adjustment": 30,
                    "movement_type": "restock"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 3
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "shipping_rule_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_068",
        "instruction": "You, David Chen at Summit Shipping, should utilize 'tom.j@email.com' to establish the segment 'High-Value' (>=5 orders/90d), review '30d' behavior for contact_id='208', initiate campaign 'HV-12' (12%), then purchase 1 Ergo Laptop Stand employing the welcome discount using the next id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "High-Value",
                    "criteria": {
                        "min_orders": 5,
                        "period_days": 90
                    }
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "208",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "HV-12",
                    "target_segment": "High-Value",
                    "discount_percentage": 12
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_069",
        "instruction": "Using 'david.c@email.com', manage the preparation of the 'dcomm-dev-redis' cache for production by setting up the cluster, allowing Redis traffic on 6379/TCP from 10.0.0.0/16 via an add_security_group_rule call, followed by optimizing the security group. Set the endpoint URL to 'redis://dcomm-dev-redis.cache.amazonaws.com:6379', and verify readiness by reviewing both the cache cluster info and the audit log (event 'cache_configured'). Next, purchase 1 'Pro Gaming Mouse' from the Computer Accessories catalog with the WELCOME5 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "endpoint_url": "redis://dcomm-dev-redis.cache.amazonaws.com:6379"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cache_configured",
                    "resource_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_070",
        "instruction": "For 'kevin.lee@starlight.net', coordinate the configuration of Stripe for 'MERCH_031'. Obtain similar products for your profile, then proceed to purchase 1 '4K Webcam' using the WELCOME5 discount; validate the gateway configuration in the audit log. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_031",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "210",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "4K Webcam"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_071",
        "instruction": "Utilize 'chloe.davis@email.com' to gather feedback ('Keys feel solid', rating 5), allocate 20 loyalty points, then purchase 1 'Mechanical Keyboard' using WELCOME5; verify the loyalty activity in the audit log. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.davis@email.com"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "211",
                    "feedback_text": "Keys feel solid",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "211",
                    "action": "add",
                    "points": 20
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "211",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "loyalty_program_activity"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_072",
        "instruction": "With 's.adams@pioneercorp.com', proceed to add supplier 'MousePad Ltd' (hello@mousepad.example), reserve 1 'Mechanical Keyboard' (reduce on-hand by 1), set up CloudFront in 'us-east-1', then acquire 1 'Mechanical Keyboard' from the Computer Accessories catalog using WELCOME5; ensure to log the supplier audit (event 'supplier_managed'). Supply the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "MousePad Ltd",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "hello@mousepad.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1017",
                    "quantity_adjustment": -1,
                    "movement_type": "reserve"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_073",
        "instruction": "Using 't.jenkins@pioneercorp.com', have the checkout rate limit configured at 85 rpm and confirmed, adjust the Pro Gaming Mouse list price to 70.00 (product found via the Computer Accessories catalog), then procure 1 'Pro Gaming Mouse' using WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "t.jenkins@pioneercorp.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/checkout",
                    "rate_limit": 85
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/checkout"
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1013"
                    ],
                    "update_data": {
                        "list_price": 70.0
                    }
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "214",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "rate_limit_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_074",
        "instruction": "Employ 'chloe.d@email.com' to enable and secure the connected app 'APP906'; confirm by reviewing the app's security details and the audit log (event 'app_security_updated'); establish the 'US-Std' shipping rule for your profile (contact-level, tracking enabled), then acquire 1 'USB-C Hub' and 1 'Wireless Mouse' using WELCOME5. Supply the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP906",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP906"
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "215"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "215",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "app_security_updated",
                    "resource_id": "APP906"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_075",
        "instruction": "Utilize 'chloe.d@email.com' to enable and secure the connected app 'APP906' (with read and write permissions and OAuth scopes ['api','openid']), confirming its security settings by accessing the app details. Set the US-Std shipping rule for your profile (contact_id 215) with tracking enabled, then purchase 1 'USB-C Hub' and 1 'Wireless Mouse' from the Computer Accessories catalog using the WELCOME5 discount. Verify the app-security update in the audit log (event 'app_security_updated'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP906",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "215"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "215",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        },
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "app_security_updated",
                    "resource_id": "APP906"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_076",
        "instruction": "With 'maria.garcia@globaltech.com', handle the security of the 'dcomm-uat-redis' cache according to policy and confirm this in the cluster details. Next, coordinate the purchase of 2 'USB-C Hub' from the 'Computer Accessories' category using B2BVOLUME15. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories",
                    "account_id": "101"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_077",
        "instruction": "Using 'emily.white@innovate.com', initiate the 'CLEAR-7' campaign (providing a 7% discount to all customers) and configure the 'EU-Express' shipping rule in your profile with tracking activated. Then, conduct a purchase of 1 'Wireless Mouse' from the Computer Accessories catalog using the WELCOME5 discount and finding the product through category search. Ensure verification of the promotion in the audit log under the event 'promotion_created'. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "CLEAR-7",
                    "target_segment": "all",
                    "discount_percentage": 7
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "EU-Express",
                    "shipping_zone": "EU",
                    "tracking_enabled": true,
                    "customer_id": "203"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_078",
        "instruction": "Using 'emily.white@innovate.com', implement internal-only access enforcement on the 'dcomm-dev-redis' cache and confirm its readiness. Subsequently, manage the purchase of 1 'Pro Gaming Mouse' from the Computer Accessories catalog utilizing the WELCOME5 discount. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "status": "available",
                    "endpoint_url": "redis://dcomm-dev-redis.cache.amazonaws.com:6379",
                    "security_group_id": "sg-0123456789abcdef0"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_079",
        "instruction": "Your name is Mike Rivera. Update your VIP customer segment (those with a lifetime spend of at least $1,000), and follow with a purchase of a Pro Gaming Mouse from the Computer Accessories category by applying any suitable discount, like WELCOME5. Return the resulting order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "VIP",
                    "criteria": {
                        "lifetime_spend_usd": 1000
                    }
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "205",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_080",
        "instruction": "You are Mike Rivera at Tech Solutions. Using 'tom.j@email.com', arrange for your dev Redis cluster 'dcomm-dev-redis' to operate as cache.r5.large with three nodes, ensuring access is only from 10.0.0.0/16 on TCP 6379 through 'sg-0123456789abcdef0', culminating in a single ingress and any redundant rules should be consolidated. Afterward, proceed to a swift checkout for one Pro Gaming Mouse from Computer Accessories with the welcome discount, employing the platform's next cart and order numbers. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_081",
        "instruction": "You are Mike Rivera at Frontier Industries. Utilizing 's.adams@pioneercorp.com', arrange a light retention initiative for your 'Returning-30d' audience. Plan to execute 'RET-8' followed by acquiring one USB-C Hub from the Computer Accessories catalog with the welcome discount at checkout. Ensure the promotion was recorded and return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-30d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 30
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-8",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 8
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_082",
        "instruction": "Utilizing 'chloe.davis@email.com', set up CloudFront in 'us-east-1', retrieve similar products for your profile, then purchase 1 'Mechanical Keyboard' using WELCOME5; confirm the CDN setup within the audit log. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.davis@email.com"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "211",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "211",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_083",
        "instruction": "You are Mike Rivera at Frontier Industries. Through 's.adams@pioneercorp.com', add Redis 6379/TCP from 10.0.0.0/16 on 'sg-0123456789abcdef0', refine the rules, then make a purchase of 1 'USB-C Hub' from the 'Computer Accessories' category with WELCOME5, and document the SG optimization audit as 'security_group_optimized'. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_084",
        "instruction": "Using 't.jenkins@pioneercorp.com', proceed to onboard CamVision, adjust the 4K Webcam list price to 175.00, buy one 4K Webcam with WELCOME5, and log the bulk-update audit. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "t.jenkins@pioneercorp.com"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "CamVision",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "sales@camvision.example"
                    }
                },
            },
            {
                "name": "ProcessBulkProductUpdate",
                "arguments": {
                    "update_type": "price",
                    "product_ids": [
                        "1018"
                    ],
                    "update_data": {
                        "list_price": 175.0
                    }
                },
            },
            {
                "name": "FindProductByName",
                "arguments": {
                    "name": "4K Webcam"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "214",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "bulk_product_update"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_085",
        "instruction": "By using 'chloe.d@email.com', examine the 30-day behavior, adjust '/returns' to 30 rpm, set up CloudFront in 'us-east-1', then purchase 1 'Wireless Mouse' with WELCOME5 and confirm the rate-limit configuration through audit. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "215",
                    "analysis_period": "30d"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/returns",
                    "rate_limit": 30
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/returns"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "CloudFront",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "215",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "rate_limit_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_086",
        "instruction": "As Maria Garcia at WorldWide Systems, with 'john.doe@globaltech.com', ensure authorization of the connected app 'APP907' with permissions ['read','write'] and scopes ['api','refresh_token'], and assess the app's access status. Impose a 550 rpm limit on '/oauth/token' and confirm. Following this, make a purchase of 1 USB-C Hub from the Computer Accessories catalog utilizing the WELCOME5 discount, and inspect the app-security update via audit for app_id 'APP907'. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP907",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "refresh_token"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP907"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/oauth/token",
                    "rate_limit": 550
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/oauth/token"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "app_security_updated",
                    "resource_id": "APP907"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_087",
        "instruction": "From 'maria.garcia@globaltech.com', establish the segment 'Returning-60d' (\u22652 orders in 60 days), analyze 60-day patterns, activate 'RET-9', then procure 1 'Pro Gaming Mouse' using WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "maria.garcia@globaltech.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "Returning-60d",
                    "criteria": {
                        "min_orders": 2,
                        "period_days": 60
                    }
                },
            },
            {
                "name": "AnalyzeCustomerBehavior",
                "arguments": {
                    "contact_id": "202",
                    "analysis_period": "60d"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "RET-9",
                    "target_segment": "Returning-60d",
                    "discount_percentage": 9
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_088",
        "instruction": "With 'emily.white@innovate.com', enable the connected app 'APP904' with permissions ['read'] and scopes ['api'], define the 'US-Std' shipping rule for your profile at the contact-level, and subsequently purchase 1 'Wireless Mouse' from the Computer Accessories catalog with WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.white@innovate.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP904",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": true,
                    "customer_id": "203"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_089",
        "instruction": "Using 'emily.w@email.com', request replenishment of 'Mechanical Keyboard' by 5, then purchase 1 'Mechanical Keyboard' with WELCOME5. Return the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1017",
                    "quantity_adjustment": 5,
                    "movement_type": "restock"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "inventory_updated"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_090",
        "instruction": "From 'tom.j@email.com', submit feedback ('Mouse tracking is perfect', rating 5), add 20 loyalty points, purchase 1 'Pro Gaming Mouse' using WELCOME5, and verify the feedback activity in the audit log (event 'feedback_processed'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ProcessCustomerFeedback",
                "arguments": {
                    "contact_id": "205",
                    "feedback_text": "Mouse tracking is perfect",
                    "rating": 5
                },
            },
            {
                "name": "ProcessLoyaltyProgram",
                "arguments": {
                    "contact_id": "205",
                    "action": "adjust_points",
                    "points": 20
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "feedback_processed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_091",
        "instruction": "Handle the preparation and restriction of the 'dcomm-uat-redis' cache following policy guidelines by leveraging 'john.doe@globaltech.com'. Add a security group rule to allow Redis (6379/TCP from 10.0.0.0/16) and optimize for internal access. Upon confirming cache readiness, locate products in the Computer Accessories category and purchase 2 'USB\u2011C Hub' using the B2BVOLUME15 discount. Do not choose a shipping method explicitly. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "B2BVOLUME15"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_092",
        "instruction": "Coordinate the temporary allowance of TLS access on the Redis cache by adding a rule for port 6380/TCP from 10.0.0.0/16 within the authorized security group via 'emily.w@email.com'. Subsequently, revert to standard internal-only access by optimizing the group for port 6379/TCP from 10.0.0.0/16 as stipulated by policy. Post security updates completion, order 1 'Wireless Mouse' from the Computer Accessories catalog utilizing the WELCOME5 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "emily.w@email.com"
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6380,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_093",
        "instruction": "As David Chen at Summit Shipping, using 'tom.j@email.com', configure the payment through 'Adyen' for merchant_id='MERCH_040' and set up shipping as 'US-Std' (US, tracking=false, customer_id='208'). Then purchase 1 'Ergo Laptop Stand' under the 'Computer Accessories' category utilizing the WELCOME5 and log the payment-gateway audit. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "tom.j@email.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_040",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ConfigureShippingRules",
                "arguments": {
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": false,
                    "customer_id": "208"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1010",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_094",
        "instruction": "Handle '/products' configuration at 210 rpm while empowering the connected app 'APP902' with necessary permissions ['read','write'] and scopes ['api','openid'] using 'david.c@email.com'. Set up Cloudflare in 'us-east-1' next, and order 1 'Wireless Mouse' from the Computer Accessories catalog using the WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "david.c@email.com"
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/products",
                    "rate_limit": 210
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/products"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902",
                    "permissions": [
                        "read",
                        "write"
                    ],
                    "oauth_scopes": [
                        "api",
                        "openid"
                    ]
                },
            },
            {
                "name": "GetConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP902"
                },
            },
            {
                "name": "ConfigureContentDeliveryNetwork",
                "arguments": {
                    "cdn_provider": "Cloudflare",
                    "region": "us-east-1"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "cdn_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_095",
        "instruction": "Handle the addition of supplier 'ProMouse Co' with contact email 'support@promouse.example' using 'kevin.lee@starlight.net'. Restock 'Pro Gaming Mouse' by a quantity of 10, then proceed to purchase 1 'Pro Gaming Mouse' utilizing the WELCOME5. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "kevin.lee@starlight.net"
                },
            },
            {
                "name": "ManageSupplierRelationships",
                "arguments": {
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {
                        "contact_email": "support@promouse.example"
                    }
                },
            },
            {
                "name": "ManageInventoryLevels",
                "arguments": {
                    "product_id": "1013",
                    "quantity_adjustment": 10,
                    "movement_type": "restock"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "supplier_managed"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_096",
        "instruction": "Utilizing 'chloe.davis@email.com', aim to initiate the 'CLEAR20' campaign (20% to all) as a retention strategy\u2014ensure it does not impact cart totals\u2014then purchase 1 'Mechanical Keyboard' from the Computer Accessories catalog and apply WELCOME5 to the cart prior to requesting the order number; check the promotion in the audit log (event 'promotion_created'). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.davis@email.com"
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "CLEAR20",
                    "target_segment": "all",
                    "discount_percentage": 20
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "211",
                    "items": [
                        {
                            "product_id": "1017",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_097",
        "instruction": "With 's.adams@pioneercorp.com', proceed to activate the connected app 'APP908' (read, api), retrieve 'bought_together' recommendations, and acquire 1 'Wireless Mouse' from the 'Computer Accessories' category using WELCOME5; verify the app-security update within the audit log. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "s.adams@pioneercorp.com"
                },
            },
            {
                "name": "ManageConnectedAppSecurity",
                "arguments": {
                    "app_id": "APP908",
                    "permissions": [
                        "read"
                    ],
                    "oauth_scopes": [
                        "api"
                    ]
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "213",
                    "recommendation_type": "bought_together"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [
                        {
                            "product_id": "1003",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "app_security_updated",
                    "resource_id": "APP908"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_098",
        "instruction": "As Maria Garcia at WorldWide Systems, using 'john.doe@globaltech.com', configure the 'Stripe' payment gateway for merchant_id='MERCH_052' (USD), set the API rate limit to 120 rpm for '/checkout' and confirm, then order 2 USB-C Hub in Computer Accessories applying the welcome discount using next ids and record the payment-gateway audit. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigurePaymentGateway",
                "arguments": {
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_052",
                    "supported_currencies": [
                        "USD"
                    ]
                },
            },
            {
                "name": "ManageApiRateLimits",
                "arguments": {
                    "api_endpoint": "/checkout",
                    "rate_limit": 120
                },
            },
            {
                "name": "GetApiRateLimitConfig",
                "arguments": {
                    "api_endpoint": "/checkout"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1002",
                            "quantity": 2
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "payment_gateway_configured"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_099",
        "instruction": "Employing 'chloe.d@email.com', identify the 'VIP' segment (lifetime_spend_usd \u2265 1000) and launch 'VIP-12' targeting the 'VIP' segment by name, obtain similar_products for your profile, then purchase 1 'Pro Gaming Mouse' with WINTER20; ensure the promotion is verified in the audit log (promotion_created). Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "chloe.d@email.com"
                },
            },
            {
                "name": "ManageCustomerSegments",
                "arguments": {
                    "segment_name": "VIP",
                    "criteria": {
                        "lifetime_spend_usd": 1000
                    }
                },
            },
            {
                "name": "GeneratePromotionalCampaign",
                "arguments": {
                    "campaign_name": "VIP-12",
                    "target_segment": "VIP",
                    "discount_percentage": 12
                },
            },
            {
                "name": "ManageProductRecommendations",
                "arguments": {
                    "contact_id": "215",
                    "recommendation_type": "similar_products"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "215",
                    "items": [
                        {
                            "product_id": "1013",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WINTER20"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                },
            },
            {
                "name": "GetAuditLog",
                "arguments": {
                    "action_type": "promotion_created"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
    ,
    {
        "annotator": v3,
        "user_id": "task_100",
        "instruction": "Under 'john.doe@globaltech.com', get the 'dcomm-dev-redis' environment ready for production by setting up the cache cluster, including a 6379/TCP allowlist for 10.0.0.0/16 in the approved security group, optimize the group, and configure the endpoint URL to 'redis://dcomm-dev-redis.cache.amazonaws.com:6379'. Confirm readiness by checking the cache cluster details. Then, purchase 1 '4K Webcam' through the Computer Accessories catalog with the WELCOME5 discount. Provide the order id.",
        "actions": [
            {
                "name": "GetCustomerProfile",
                "arguments": {
                    "email": "john.doe@globaltech.com"
                },
            },
            {
                "name": "ConfigureCacheIntegration",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {
                        "node_type": "cache.r5.large",
                        "num_cache_nodes": 3
                    }
                },
            },
            {
                "name": "AddSecurityGroupRule",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": "10.0.0.0/16"
                },
            },
            {
                "name": "OptimizeSecurityGroupRules",
                "arguments": {
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16"
                },
            },
            {
                "name": "UpdateCacheClusterStatus",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis",
                    "status": "available",
                    "endpoint_url": "redis://dcomm-dev-redis.cache.amazonaws.com:6379",
                    "security_group_id": "sg-0123456789abcdef0"
                },
            },
            {
                "name": "GetCacheClusterInfo",
                "arguments": {
                    "cluster_id": "dcomm-dev-redis"
                },
            },
            {
                "name": "SearchProductsByCategory",
                "arguments": {
                    "category_name": "Computer Accessories"
                },
            },
            {
                "name": "GetNextCartId",
                "arguments": {
                {}
                },
            },
            {
                "name": "CreateShoppingCart",
                "arguments": {
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [
                        {
                            "product_id": "1018",
                            "quantity": 1
                        }
                    ]
                },
            },
            {
                "name": "ApplyDiscountBundle",
                "arguments": {
                    "cart_id": "706",
                    "offer_code": "WELCOME5"
                },
            },
            {
                "name": "GetNextOrderId",
                "arguments": {
                {}
                },
            },
            {
                "name": "ProcessOrderWithFulfillment",
                "arguments": {
                    "order_id": "9017",
                    "cart_id": "706"
                }
            }
        ],
        "outputs": [
                "9017"
        ]
    }
]
