from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="aws_v1",
        user_id="task_A01",
        instruction=(
            "After a tough audit, you’re putting Commerce in UAT back on solid ground so customers don’t feel the wobble. "
            "You want to start by confirming UAT’s network defaults. Before you touch any security rules, you look up the Redis "
            "cluster so you know exactly what you’re pinning to; only then do you pull the Commerce API security group and "
            "tighten it to the standard internal range on the usual TLS and Redis ports. With AUTH/TLS enforced, you point "
            "Commerce at the cluster using your existing secret and the standard UAT partition key. Because first hits were "
            "laggy, you give metadata a quick warm so pages snap. To keep an eye on regressions, you restore the baseline "
            "visibility (simple cache dashboard + the standard Errors alarm) and run a quick UAT SMOKE. Finally, you record "
            "the change against the Redis cluster for audit."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce API"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443, 6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(name="set_redis_auth_and_tls", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-commerce-api-uat-commerce-api-443-6379-10-0-0-0-16",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "change_log_id: chg-networking-dcomm-uat-redis-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A02",
        instruction=(
            "You are Dana Brooks from API. Merchandising goes live in UAT this afternoon and partners will start pulling from Catalog v3 within minutes. "
            "You want the 3.1.0 OpenAPI (from blob_901) live behind the canonical 'catalog-v3' gateway so you can catch early failures before they fan out. "
            "You want to sanity-check offer discovery with 'Catalog-v3-SMOKE'. "
            "You want baseline API monitoring on the gateway — a simple 'api' dashboard and a 5xxErrorRate alarm at 1.0 over 300s — so on-call can spot spikes. "
            "You want the rollout recorded against 'spec-catalog-v3-3-1-0' in UAT for audit."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.0",
                    "spec_blob_id": "blob_901",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "catalog-v3", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-catalog-v3-3-1-0", "gateway_id": "dcg-catalog-v3-uat"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"collection_name": "Catalog-v3-SMOKE", "environment": "UAT"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-catalog-v3-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "change_type": "rollout",
                    "target_id": "spec-catalog-v3-3-1-0",
                    "environment": "UAT",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-catalog-v3-3-1-0",
            "dcg_id: dcg-catalog-v3-uat",
            "run_id: run-catalog-v3-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
            "alarm_id: al-dcg-catalog-v3-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A03",
        instruction=(
            "You are Ethan Rowe from Platform. Peak traffic has been causing cold starts in UAT and you want them gone. "
            "You want to deploy a lightweight warmer from bundle 'bundle_cachewarmer_v1' (purpose 'cache_warmer') and you want it scheduled on the default 15-minute cadence. "
            "You want a 'lambda' dashboard for quick visibility. "
            "You want a baseline Errors alarm at 1.0 over 300s attached to the function’s ARN so alerts bind to the right resource. "
            "You want a quick 'SMOKE' validation after deploy, and you want the ops change recorded against 'fn-commerce-api-cache_warmer-uat'."
        ),
        actions=[
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={
                    "environment": "UAT",
                    "purpose": "lambda",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "UAT",
                    "collection_name": "SMOKE",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-functi-rate-15-minutes",
            "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache-warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
            "dashboard_name: dash-uat-lambda",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A04",
        instruction=(
            "You are Sam Lee from Commerce Ops. A recent pen test flagged the Checkout Gateway as too open. "
            "In UAT, you want it restricted to the UAT allowlist so only trusted traffic can reach it, without breaking checkout. "
            "To prove the path still works end-to-end, you’ll place a simple cart for sam@example.com for USB-C Hub using WINTER20 "
            "with STANDARD shipping and capture the cart id for audit."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Checkout Gateway"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WINTER20"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "sam@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WINTER20",
                    "shipping_method": "STANDARD",
                },
            ),
        ],
        outputs=[
            "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A05",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want 'm.rivera@apexlogistics.com' on the 'B2B Wholesale' tier and a cart "
            "with 2× 'USB-C Hub' and 1× 'Thunderbolt Docking Station' using 'B2BVOLUME15' and STANDARD shipping. Publish a lightweight 'api' dashboard "
            "for visibility, and record the change for 'B2B Wholesale'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 2},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A06",
        instruction=(
            "You are Priya Sharma from Platform Reliability. In UAT, shoppers hit stale promos, so you clean up the cache on dcomm-uat-redis. "
            "You set partition key 'dcomm-uat-redis' to v4, remove 'offer:Crosstrek' and 'offer:Dock4K', publish a simple 'cache' dashboard, warm metadata, "
            "keep a CacheHitRate guardrail at 75.0 over 300 seconds (LessThanThreshold), and record the change."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key",
                kwargs={"partition_key": "dcomm-uat-redis", "version": "v4"},
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:Crosstrek", "offer:Dock4K"]},
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 75.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-uat-redis", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v4",
            "invalidated_count: 2",
            "dashboard_name: dash-uat-cache",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-75-0-300-lessthanthreshold",
            "change_log_id: chg-ops-dcomm-uat-redis-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A07",
        instruction=(
            "You are Priya Sharma from Platform Security. In UAT, lock 'Commerce API' to TLS-only from 10.0.0.0/16, prove it with a 'SMOKE' run, "
            "alarm on unexpected errors, then publish an 'api' dashboard and record the change."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce API"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "sg-uat-commerce-api",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "change_type": "security",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-commerce-api-uat-commerce-api-443-10-0-0-0-16",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "alarm_id: al-sg-uat-commerce-api-errors-1-0-300-greaterthanorequaltothreshold",
            "dashboard_name: dash-uat-api",
            "change_log_id: chg-security-sg-uat-commerce-api-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A08",
        instruction=(
            "You are Dana Li from Identity. In UAT, you want the 'Connected Checkout' app ready for login with tight redirect hygiene. "
            "You want OAuth configured with scopes api and openid with callback https://checkout.uat.example.com/oauth/callback, "
            "you want the callback domain verified against example.com, you want audiences catalog-v3 and checkout registered as trusted, "
            "you want 'SMOKE' run in UAT, and you want the update recorded for 'app-connected-checkout'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Connected Checkout",
                    "scopes": ["api", "openid"],
                    "callback_urls": ["https://checkout.uat.example.com/oauth/callback"],
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://checkout.uat.example.com/oauth/callback",
                    "expected_domain": "checkout.uat.example.com",
                },
            ),
            Action(
                name="register_oauth_trusted_audience",
                kwargs={
                    "app_name_hint": "Connected Checkout",
                    "audiences": ["catalog-v3", "checkout"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-connected-checkout",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-connected-checkout",
            "client_id: client-connected-checkout",
            "status: verified",
            "policy_id: aud-e913f62f61",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-oauth-app-connected-checkout-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A09",
        instruction=(
            "You are Nora James from Platform. In UAT, you want Redis secured with AUTH/TLS and the Cache API pointed at the exact endpoint. "
            "Use the Redis host 'dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com' with the API auth secret "
            "'arn:aws:secretsmanager:local:000000000000:secret:app-cache-api' and partition key 'dcomm-uat'. Add a baseline 'Errors' alarm on "
            "'dcomm-uat-redis', validate with a quick smoke, and record the security update."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(name="set_redis_auth_and_tls", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:app-cache-api",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(name="create_cloudwatch_alarm", kwargs={"resource_id": "dcomm-uat-redis"}),
            Action(name="run_test_collection", kwargs={"environment": "UAT"}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "security",
                },
            ),
        ],
        outputs=[
            "tls_status: enabled",
            "kms_key_alias: alias/dcomm-uat",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-security-dcomm-uat-redis-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A10",
        instruction=(
            "You’re Kelly Nguyen in Sales Ops. In UAT, first-time shoppers keep abandoning because they don’t know which shipping to pick. "
            "You give them a gentle nudge: add a ‘Prefer-Standard-Shipping’ context rule on the NewCustomers segment **bound to WELCOME5**, and set the "
            "attribute **shipping_preference=STANDARD** so the default is obvious. You sanity-check the catalog entry for USB-C Hub so you’re not testing with a ghost product, "
            "confirm the WELCOME5 code is live, and then do a quick real cart for newuser@example.com with AC-USBC-HUB, promo WELCOME5, and STANDARD shipping to see the hint stick. "
            "Finally, you record the personalization change against the rule id so audit can see when this nudge went in."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard-Shipping",
                    "attributes": {"shipping_preference": "STANDARD"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="resolve_catalog_entities", kwargs={"kind": "product", "names": ["USB-C Hub"]}
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "newuser@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "change_type": "personalization",
                    "target_id": "ctx-newcustomers-prefer-standard-shipping",
                    "environment": "UAT",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-newcustomers-prefer-standard-shipping",
            "cart_id: cart-cust-newuser-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A11",
        instruction=(
            "You are Dana Brooks from API. In UAT, you want early-signal visibility as Catalog v3 goes live. "
            "Your goal: get Catalog v3 online behind the UAT gateway with a quick smoke and light observability so you hear about problems first. "
            "You publish the Catalog v3 OpenAPI 3.1.0 from 'blob_901', bind it to the UAT gateway group for catalog-v3, "
            "run the 'Catalog-v3-SMOKE' suite, make an 'api' dashboard available, set trace sampling to 0.10 during shakeout, "
            "and you record the rollout against 'spec-catalog-v3-3-1-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.0",
                    "spec_blob_id": "blob_901",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "catalog-v3", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-catalog-v3-3-1-0", "gateway_id": "dcg-catalog-v3-uat"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Catalog-v3-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "api"},
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-catalog-v3-3-1-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-catalog-v3-3-1-0",
            "dcg_id: dcg-catalog-v3-uat",
            "run_id: run-catalog-v3-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A12",
        instruction=(
            "You are Priya Kapoor from Performance. In UAT, you want to cut stale reads by moving the Commerce cache to partition key "
            "'dcomm-uat' at version 'v6', do a quick metadata warm, and keep the 75.0/300 'CacheHitRate' alarm (LessThanThreshold) so drift shows up. "
            "Run 'SMOKE' and record the ops change for 'dcomm-v6'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key",
                kwargs={"partition_key": "dcomm-uat", "version": "v6"},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 75.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v6", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v6",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-75-0-300-lessthanthreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A13",
        instruction=(
            "You’re Luis Ortega from Identity. UAT tokens have been drifting, so you refresh the Commerce API connected app and limit it to trusted callers. "
            "You configure OAuth with scopes api, refresh_token, openid and callback https://acme.example/callback. "
            "Then you store a single managed client secret in UAT as OAUTH_CLIENT_SECRET, **sourced from the connected app’s short id ‘app-commerce-api’ (not an ARN)**, "
            "register catalog-v3 and checkout as trusted audiences, run OAuth-Smoke in UAT so Login can sleep at night, and record the change against the Commerce API app."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://acme.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="register_oauth_trusted_audience",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "audiences": ["catalog-v3", "checkout"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-commerce-api",
            "client_id: client-commerce-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
            "policy_id: aud-082826bf03",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-oauth-app-commerce-api-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A14",
        instruction=(
            "You are Omar Kelly from Performance. In UAT, you want to bump the Commerce cache to 'dcomm-uat' version 'v2', clear prior "
            "promo entries to avoid stale lookups, do a quick warm, attach the baseline error alarm, publish a cache dashboard, and then "
            "record the ops change for 'dcomm-uat-redis'. Specifically invalidate 'offer:welcome5' and 'offer:b2bvolume15'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key",
                kwargs={"partition_key": "dcomm-uat", "version": "v2"},
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:welcome5", "offer:b2bvolume15"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "applied_version: v2",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "dashboard_name: dash-uat-cache",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A15",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want 'WINTER20' set active=False and 'WELCOME5' set active=True. "
            "You want a quick cart for 'newuser2@example.com' for 'USB-C Hub' with 'WELCOME5' and STANDARD shipping, and you want to record "
            "the change for 'WELCOME5' with change_type 'personalization'."
        ),
        actions=[
            Action(name="get_offer_by_code", kwargs={"offer_code": "WINTER20"}),
            Action(name="upsert_promotion", kwargs={"code": "WINTER20", "active": False}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(name="upsert_promotion", kwargs={"code": "WELCOME5", "active": True}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "newuser2@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "WELCOME5",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "promo_id: 503",
            "cart_id: cart-cust-newuser2-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A16",
        instruction=(
            "You are Dana Liu from Performance. In UAT, you want to advance the Commerce cache to partition key 'dcomm' at version 'v5' and flush two legacy promo entries "
            "so customers don’t see outdated discounts. Set the partition key, invalidate 'offer:USB-C Hub' and 'offer:Thunderbolt Docking Station', run a quick 'metadata' warm, "
            "attach the baseline 'Errors' alarm (1.0/300, GreaterThanOrEqualToThreshold), run 'SMOKE' to confirm reads, and record the ops change for 'dcomm-v5'."
        ),
        actions=[
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v5"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:USB-C Hub", "offer:Thunderbolt Docking Station"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v5", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v5",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A17",
        instruction=(
            "You are Dana Brooks from API. In UAT, you roll out Catalog v3 with lightweight visibility. "
            "You publish the Catalog v3 OpenAPI (3.1.0 from 'blob_901') on 'dcg-catalog-v3-uat', run Catalog-v3-SMOKE, keep an 'api' dashboard handy, "
            "and record the rollout for 'spec-catalog-v3-3-1-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.0",
                    "spec_blob_id": "blob_901",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "catalog-v3", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-catalog-v3-3-1-0", "gateway_id": "dcg-catalog-v3-uat"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Catalog-v3-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-catalog-v3-3-1-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A18",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you’re standing up PrivateLink to ElastiCache in the "
            "exact VPC and subnets named here — use VPC id 'vpc-resolved' and subnets 'subnet-a' and 'subnet-b' "
            "literally (do not substitute environment defaults). You create the interface endpoint for "
            "'com.amazonaws.us-east-1.elasticache', lock the 'Cache Integration' service to Redis 6379 from "
            "'10.0.0.0/16', publish a simple 'cache' dashboard for visibility, and record the change for "
            "'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-a", "subnet-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Cache Integration"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
            "sg_change_applied: True",
            "dashboard_name: dash-uat-cache",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A19",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want 'm.rivera@apexlogistics.com' on the 'B2B Wholesale' tier and a quick "
            "cart with 'USB-C Hub' and 'Thunderbolt Docking Station' using 'B2BVOLUME15' and STANDARD shipping. You want the change recorded."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Thunderbolt Docking Station"}),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 1},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A20",
        instruction=(
            "You are Rafael Gomez from Platform. In UAT, you want the Cache API to authenticate to Redis and prove the wiring. "
            "Confirm UAT network defaults, rotate the API auth header secret for dcomm-uat-redis, point the integration at "
            "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com with partition key dcomm-uat, do a quick metadata warm, "
            "publish a simple 'cache' dashboard, add a light Errors alarm on dcomm-uat-redis, run a quick SMOKE, and record the change for 'CacheAPI.ExternalSystemURL'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={"resource_id": "dcomm-uat-redis", "metric_name": "Errors"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemURL",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "setting_ids: CacheAPI.ExternalSystemURL, CacheAPI.ExternalSystemAuthHeader, CacheAPI.ExternalSystemPartitionKey",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-ops-cacheapi-externalsystemurl-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A21",
        instruction=(
            "You are Alex Wu from API Platform. In UAT, you bring Inventory v1 live with essential guardrails. "
            "Publish the Inventory v1 OpenAPI (1.0.0 from 'blob_inventory_v1'), enable the inventory-v1 gateway, register endpoints, "
            "run 'Inventory-v1-SMOKE', attach a 5xx error-rate alarm to the gateway, and record the rollout."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Inventory v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_inventory_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={
                    "api_group_name": "inventory-v1",
                    "environment": "UAT",
                },
            ),
            Action(
                name="register_api_endpoints",
                kwargs={
                    "spec_id": "spec-inventory-v1-1-0-0",
                    "gateway_id": "dcg-inventory-v1-uat",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Inventory-v1-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-inventory-v1-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-inventory-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-inventory-v1-1-0-0",
            "dcg_id: dcg-inventory-v1-uat",
            "endpoint_id: ep-spec-inventory-v1-1-0-0-dcg-inventory-v1-uat",
            "run_id: run-inventory-v1-smoke-uat-2025-08-06t12-00-00z",
            "alarm_id: al-dcg-inventory-v1-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
            "change_log_id: chg-rollout-spec-inventory-v1-1-0-0-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A22",
        instruction=(
            "You are Luis Ortega from Identity. In UAT, the 'Commerce API' connected app must use the scopes api, refresh_token, and openid "
            "with the callback https://acme.example/callback. You want to verify the callback domain ownership for acme.example before issuing credentials, "
            "store the OAUTH_CLIENT_SECRET, publish the 'api' dashboard, set trace sampling to 0.10 briefly so support can watch token exchanges "
            "during shakeout, validate with 'OAuth-Smoke', and record the change for 'app-commerce-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://acme.example/callback"],
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://acme.example/callback",
                    "expected_domain": "acme.example",
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-commerce-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A23",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you want ElastiCache reachable privately in VPC 'vpc-resolved' across subnets "
            "'subnet-a' and 'subnet-b' (use these exact ids, not environment defaults) for service 'com.amazonaws.us-east-1.elasticache'. "
            "Limit 'Cache Integration' to Redis 6379 from '10.0.5.0/24' and record the change for "
            "'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-a", "subnet-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Cache Integration"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.5.0/24"],
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-subnet-b",
            "sg_change_applied: True",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A24",
        instruction=(
            "You are Morgan Lee from Platform. In UAT, you want a safe cache partition bump with visibility. "
            "You want 'dcomm-uat-redis' checked, partition key 'dcomm' set to 'v5', keys ['offer:WELCOME5','offer:WINTER20'] invalidated, "
            "a 'metadata' warm run, a 'cache' dashboard published for UAT, and the change recorded for 'dcomm-v5'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v5"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:WELCOME5", "offer:WINTER20"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v5", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v5",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-cache",
            "change_log_id: chg-ops-dcomm-v5-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A25",
        instruction=(
            "You are Jenna Ortiz from Growth. In UAT, onboarding traffic is getting the wrong discount. "
            "You want the conflicting B2B promo paused and the welcome offer active for new users: deactivate 'B2BVOLUME15', activate 'WELCOME5', "
            "warm 'metadata' so changes propagate, run 'B2B-Offer-SMOKE' and a quick 'SMOKE', and record the change for 'B2BVOLUME15'."
        ),
        actions=[
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(name="upsert_promotion", kwargs={"code": "B2BVOLUME15", "active": False}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(name="upsert_promotion", kwargs={"code": "WELCOME5", "active": True}),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "B2B-Offer-SMOKE"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "B2BVOLUME15",
                    "environment": "UAT",
                },
            ),
        ],
        outputs=[
            "offer_code: B2BVOLUME15",
            "active: False",
            "run_id: run-b2b-offer-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A26",
        instruction=(
            "You are Dana Brooks from API. In UAT, you want to enable the 'payments-v1' gateway and register the "
            "'Payments v1' API version '1.2.0' from 'blob_payments_120'. You want trace sampling at 0.08, to run 'SMOKE', "
            "create an 'api' dashboard, and record the rollout for 'spec-payments-v1-1-2-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Payments v1",
                    "spec_version": "1.2.0",
                    "spec_blob_id": "blob_payments_120",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "payments-v1", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-payments-v1-1-2-0", "gateway_id": "dcg-payments-v1-uat"},
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.08}),
            Action(name="run_test_collection", kwargs={"environment": "UAT"}),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-payments-v1-1-2-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-payments-v1-1-2-0",
            "dcg_id: dcg-payments-v1-uat",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A27",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want Commerce pointed at the existing cache cluster using a fresh API auth header so calls authenticate cleanly. "
            "You read 'dcomm-uat-redis', create the new API_AUTH_HEADER secret sourced from that cluster, wire the client to the cluster endpoint with partition key 'dcomm-uat', "
            "run 'Cache-Integration-SMOKE' to confirm, do a quick metadata warm so lookups aren’t cold, add a simple Errors alarm on 'dcomm-uat-redis' for a basic signal, "
            "and record the change for 'CacheAPI.ExternalSystemURL'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Cache-Integration-SMOKE"},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemURL",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "cache_integration_verified: True",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A28",
        instruction=(
            "You are Nia Jackson from Growth. In UAT, you need WELCOME5 live and consistent for onboarding. "
            "Make sure the WELCOME5 offer actually exists—write it if needed—then activate that offer and its paired promotion. "
            "Validate with the 'Offer-Smoke' test, and record the change for 'offer-WELCOME5'."
        ),
        actions=[
            Action(
                name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}
            ),
            Action(name="upsert_promotion", kwargs={"code": "WELCOME5", "active": True}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Offer-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "offer-WELCOME5", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "offer_code: WELCOME5",
            "promotion_code: WELCOME5",
            "run_id: run-offer-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A29",
        instruction=(
            "You are Pat Jones from Sales Enablement. In UAT, you want the volume discount clearly live and proven in a real flow. "
            "Activate 'B2BVOLUME15' and place a quick cart for 'pat.jones@example.com' for 'USB-C Hub' using code 'B2BVOLUME15' "
            "with 'STANDARD' shipping, then record the change for 'B2BVOLUME15' under ops."
        ),
        actions=[
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(name="upsert_promotion", kwargs={"code": "B2BVOLUME15", "active": True}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "pat.jones@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "B2BVOLUME15", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "promo_id: 504",
            "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A30",
        instruction=(
            "You are Rafael Kim from SRE. In UAT, Confirm environment defaults first so the schedule and metrics bind cleanly, then keep Commerce API’s "
            "cache warm on a 15-minute cadence. Deploy the 'bundle_cachewarmer_v1' Lambda (purpose 'cache_warmer'), schedule it, publish a 'cache' "
            "dashboard, alarm on Errors at 1.0 over 300s (GreaterThanOrEqualToThreshold) for "
            "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat, run a metadata warm now, run 'SMOKE', and record the change "
            "for 'fn-commerce-api-cache_warmer-uat' with change_type 'ops'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A31",
        instruction=(
            "You are Dana Brooks from API. UAT networking was adjusted for capacity and gateways have mis-bound without a preflight. Sanity-check "
            "UAT network defaults, then enable the 'inventory-v1' gateway, register 'Inventory v1' (1.0.0 from blob_inventory_v1), run "
            "'Inventory-v1-SMOKE', publish an 'api' dashboard, and record the rollout for 'spec-inventory-v1-1-0-0'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Inventory v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_inventory_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "inventory-v1", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-inventory-v1-1-0-0", "gateway_id": "dcg-inventory-v1-uat"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Inventory-v1-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-inventory-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-inventory-v1-1-0-0",
            "dcg_id: dcg-inventory-v1-uat",
            "run_id: run-inventory-v1-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A32",
        instruction=(
            "You are Daniel Cho from Pricing. In UAT, you want to standardize entry-level catalog pricing so downstream flows use "
            "known values. You will upsert two entries into the 'Standard' pricebook for 'TSHIRT-001' at 20.0 and 'MUG-001' at 8.0, "
            "warm the cache metadata to propagate pricing quickly, run the 'Pricing-Smoke' test to confirm totals, and record the change for 'pb-standard'."
        ),
        actions=[
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard",
                    "items": [
                        {"product_code": "TSHIRT-001", "unit_price": 20.0},
                        {"product_code": "MUG-001", "unit_price": 8.0},
                    ],
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Pricing-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "pb-standard", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "pbe_ids: ['pbe-pb-standard-tshirt-001', 'pbe-pb-standard-mug-001']",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "run_id: run-pricing-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A33",
        instruction=(
            "You are Sam Lee from Commerce Ops. A catalog update just landed and pricing must be confirmed before a UAT walkthrough. "
            "Update 'Standard Retail' to 62.50 for 'USB-C Hub' (AC-USBC-HUB) and 209.00 for 'Thunderbolt Docking Station' (HW-TB-DOCK), "
            "assign the 'Standard Retail' tier to sam@example.com, then prove pricing in a cart using WELCOME5 with STANDARD shipping. "
            "Record the change for 'Standard Retail'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "Standard Retail"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 62.50},
                        {"product_code": "HW-TB-DOCK", "unit_price": 209.00},
                    ],
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "sam@example.com",
                    "pricing_tier_name": "Standard Retail",
                },
            ),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "sam@example.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 1},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "Standard Retail", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 2",
            "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A34",
        instruction=(
            "You are Omar Kelly from Performance. In UAT, you want a light cache partition bump with a targeted warm and a quick verification. "
            "You want cluster 'dcomm-uat-redis' checked, the partition key 'dcomm' set to version 'v7', keys 'offer:WELCOME5' and "
            "'offer:WINTER20' invalidated, a 'metadata' warm run, a 'Cache-SMOKE' run in UAT, and the change recorded for 'dcomm-v7'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v7"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:WELCOME5", "offer:WINTER20"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Cache-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v7", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v7",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "run_id: run-cache-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-ops-dcomm-v7-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A35",
        instruction=(
            "You are Luis Ortega from Identity. In PROD, you want the connected app named 'Checkout API' updated with the required access and callback, validated, "
            "and watched with baseline visibility. You set scopes 'api' and 'openid' with callback https://checkout.example/callback, store both the client secret and API auth header, "
            "verify with 'OAuth-Smoke', publish the 'api' dashboard, attach a light 5xxErrorRate alarm on the app id, and record the change for 'app-checkout-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Checkout API",
                    "scopes": ["api", "openid"],
                    "callback_urls": ["https://checkout.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "PROD",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-checkout-api",
                },
            ),
            # bump: also store the API auth header for the connected app
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "PROD",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-checkout-api",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "PROD", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "PROD", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "app-checkout-api",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-checkout-api",
                    "environment": "PROD",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-checkout-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-prod-app-checkout-api-alias-dcomm-prod",
            "secret_arn_api_auth: arn:secret-secret-api-auth-header-prod-app-checkout-api-alias-dcomm-prod",
            "run_id: run-oauth-smoke-prod-2025-08-06t12-00-00z",
            "dashboard_name: dash-prod-api",
            "alarm_id: al-app-checkout-api-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A36",
        instruction=(
            "You are Raj Patel from Personalization. UAT moved rule evaluation behind a new gateway and you want VIP deliveries to default fast. "
            "Define 'Prefer-Overnight' for the 'VIP' segment (shipping_preference='OVERNIGHT') bound to 'WELCOME5', sanity-check UAT environment defaults, "
            "then prove it with a cart for 'pat.jones@example.com' buying 'Thunderbolt Docking Station' with 'WELCOME5' and 'OVERNIGHT' shipping. "
            "Record the personalization change."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Overnight",
                    "attributes": {"shipping_preference": "OVERNIGHT"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(name="get_product_by_name", kwargs={"name": "Thunderbolt Docking Station"}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "pat.jones@example.com",
                    "items": [{"product_code": "HW-TB-DOCK", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "OVERNIGHT",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-vip-prefer-overnight",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-vip-prefer-overnight",
            "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A37",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want to rotate the API auth header secret for Commerce’s use of 'dcomm-uat-redis' without cold-start pain. "
            "You read the cluster, create the new API_AUTH_HEADER secret from it, wire the client to the endpoint with partition key 'dcomm-uat', warm metadata so basic lookups are ready, "
            "publish a simple 'cache' dashboard for quick checks, verify with 'Cache-Integration-SMOKE', and record the change for 'CacheAPI.ExternalSystemAuthHeader'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Cache-Integration-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "cache_integration_verified: True",
            "dashboard_name: dash-uat-cache",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A38",
        instruction=(
            "You are Amira Patel from Networking. In PROD, you want the 'Checkout Gateway' service restricted to '10.0.0.0/16' "
            "on TLS 443. You want an 'api' dashboard, and you want to record the change for 'sg-prod-checkout-gateway'."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "PROD", "service_name": "Checkout Gateway"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "PROD", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "change_type": "security",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-prod-checkout-gateway-prod-checkout-gateway-443-10-0-0-0-16",
            "dashboard_name: dash-prod-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A39",
        instruction=(
            "You are Dana Brooks from API. Search gateways in PROD mis-bound after capacity changes when defaults weren’t checked. "
            "In PROD, confirm network defaults, publish 'Search v1' (1.0.0 from 'blob_search_v1_0_0') behind 'search-v1', set trace sampling to 0.05, "
            "verify with 'Search-v1-SMOKE', enable the 'api' dashboard, and record the rollout to 'spec-search-v1-1-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Search v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_search_v1_0_0",
                },
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "PROD"}),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "search-v1", "environment": "PROD"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-search-v1-1-0-0", "gateway_id": "dcg-search-v1-prod"},
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.05}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "PROD", "collection_name": "Search-v1-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "PROD", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-search-v1-1-0-0",
                    "environment": "PROD",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-search-v1-1-0-0",
            "dcg_id: dcg-search-v1-prod",
            "run_id: run-search-v1-smoke-prod-2025-08-06t12-00-00z",
            "dashboard_name: dash-prod-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A40",
        instruction=(
            "You are Omar Kelly from Performance. In UAT, you want the Commerce cache partition key 'dcomm' set to version 'v8', "
            "invalidate 'offer:WELCOME5' and 'offer:WINTER20', and warm 'metadata' so cards stay fresh. You also want a CacheHitRate "
            "alarm at 72.0 over 300 with 'LessThanThreshold', then a quick 'Cache-SMOKE' to confirm reads stayed healthy, and you want "
            "the change recorded for 'dcomm-v8'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v8"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:WELCOME5", "offer:WINTER20"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 72.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "UAT",
                    "collection_name": "Cache-SMOKE",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-v8",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "applied_version: v8",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-72-0-300-lessthanthreshold",
            "run_id: run-cache-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-ops-dcomm-v8-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A41",
        instruction=(
            "You are Dana Brooks from API. UAT partners consume Orders over private paths, so you want 'Orders v1' live with PrivateLink in place. "
            "Publish 'Orders v1' 1.0.0 from blob_orders_v1, enable the 'orders-v1' gateway in UAT, create a VPC interface endpoint for service 'com.apis.orders-v1' "
            "in vpc-uat-0001 (subnets subnet-uat-a and subnet-uat-b), register endpoints to 'dcg-orders-v1-uat', run 'Orders-v1-SMOKE', publish an 'api' dashboard, "
            "and record the rollout on 'spec-orders-v1-1-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Orders v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_orders_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "orders-v1", "environment": "UAT"},
            ),
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.apis.orders-v1",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-orders-v1-1-0-0", "gateway_id": "dcg-orders-v1-uat"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Orders-v1-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-orders-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-orders-v1-1-0-0",
            "dcg_id: dcg-orders-v1-uat",
            "endpoint_id: vpce-vpc-uat-0001-com-apis-orders-v1-subnet-uat-a-subnet-uat-b",
            "dashboard_name: dash-uat-api",
            "run_id: run-orders-v1-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A42",
        instruction=(
            "You are onboarding OAuth client 'Profiles Portal' in UAT. Configure scopes ['openid'] with callback "
            "'https://profiles.example/callback', verify domain 'profiles.example', register trusted audiences "
            "['https://apis.example.com/profiles'], store 'OAUTH_CLIENT_SECRET' for 'app-profiles-portal' in UAT, then run 'OAuth-Smoke' and record the change."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Profiles Portal",
                    "scopes": ["openid"],
                    "callback_urls": ["https://profiles.example/callback"],
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://profiles.example/callback",
                    "expected_domain": "profiles.example",
                },
            ),
            Action(
                name="register_oauth_trusted_audience",
                kwargs={
                    "app_name_hint": "Profiles Portal",
                    "audiences": ["https://apis.example.com/profiles"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-profiles-portal",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-profiles-portal",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-profiles-portal",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-profiles-portal-alias-dcomm-uat",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A43",
        instruction=(
            "You are Miguel Alvarez from Pricing. In UAT, you want B2B pricing verified quickly. "
            "You want pricebook 'B2B Wholesale' confirmed, you want customer m.rivera@apexlogistics.com set to that tier, "
            "you want a cart created with 'AC-USBC-HUB' (qty 2) and 'HW-TB-DOCK' (qty 1) using promo 'B2BVOLUME15', "
            "you want 'B2B-Pricing-Smoke' run in UAT, and you want the ops change recorded for B2B Wholesale."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 2},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "B2B-Pricing-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "B2B Wholesale",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "pricebook_id: 2",
            "customer_id: cust-m-rivera-apexlogistics-com",
            "cart_id: cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
            "run_id: run-b2b-pricing-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-ops-b2b-wholesale-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A44",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. A catalog import just landed and you need pricing to be right before the B2B demo. "
            "You update the 'B2B Wholesale' pricebook (USB-C Hub to 58.50, Thunderbolt Docking Station to 185.00), run 'Pricebook-SpotCheck' in UAT to verify the pricebook reflects the change, "
            "apply the 'B2B Wholesale' tier to sara.lee@example.com, validate the B2BVOLUME15 promo before using it, prove pricing in a cart with STANDARD shipping, "
            "and you record the change for the pricebook 'B2B Wholesale'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Thunderbolt Docking Station"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 58.50},
                        {"product_code": "HW-TB-DOCK", "unit_price": 185.00},
                    ],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Pricebook-SpotCheck"},
            ),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "sara.lee@example.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "sara.lee@example.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 1},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "B2B Wholesale", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 2",
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-sara-lee-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A45",
        instruction=(
            "You are Omar Kelly from Performance. UAT shoppers are hitting stale cache. You want to advance the Commerce cache partition 'dcomm' to v9, "
            "invalidate the keys 'offer:USB-C Hub' and 'offer:WELCOME5', and run a 'metadata' warm. Set trace sampling to 0.22 for short-term "
            "diagnostics and attach a CacheHitRate alarm at 76.0 over 300s (LessThanThreshold) on 'dcomm-uat-redis', publish the 'cache' dashboard, "
            "and record the change for 'dcomm-v9'."
        ),
        actions=[
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v9"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:USB-C Hub", "offer:WELCOME5"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.22}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 76.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v9", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v9",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-cache",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A46",
        instruction=(
            "You are Raj Patel from Personalization. In UAT, roll out 'Prefer-Standard' for 'Returning' (shipping_preference=STANDARD) bound to WELCOME5. "
            "You want to attach a RuleHitAnomaly alarm (1.0 over 300s, GreaterThanOrEqualToThreshold) on 'ctx-returning-prefer-standard' so support sees unusual rule spikes, "
            "then prove it with a cart for returning.buyer@example.com on 'USB-C Hub' with STANDARD shipping and WELCOME5. Record the change."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "Returning",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {"shipping_preference": "STANDARD"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "ctx-returning-prefer-standard",
                    "metric_name": "RuleHitAnomaly",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "returning.buyer@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-returning-prefer-standard",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-returning-prefer-standard",
            "cart_id: cart-cust-returning-buyer-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A47",
        instruction=(
            "You are Amir Khan from Networking. In DEV, you want Redis reachable only over PrivateLink and nothing else. "
            "Create a VPC interface endpoint for 'com.amazonaws.us-east-1.elasticache' in 'vpc-dev-0001' across 'subnet-dev-a' and 'subnet-dev-b'. "
            "Tighten the 'Cache Integration' security group in DEV to allow TCP 6379 only from '10.2.5.0/24', attach a guardrail 5xxErrorRate alarm "
            "on 'sg-dev-cache-integration' (1.0 over 300s, GreaterThanOrEqualToThreshold), and record the networking change against the new endpoint id."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-dev-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-dev-a", "subnet-dev-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "DEV", "service_name": "Cache Integration"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-dev-cache-integration",
                    "environment": "DEV",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.2.5.0/24"],
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "sg-dev-cache-integration",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
                    "environment": "DEV",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-dev-0001-com-amazonaws-us-east-1-elasticache-subnet-dev-a-subnet-dev-b",
            "change_set_id: chg-sg-sg-dev-cache-integration-dev-cache-integration-6379-10-2-5-0-24",
            "alarm_id: al-sg-dev-cache-integration-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
            "change_log_id: chg-networking-vpce-vpc-dev-0001-com-amazonaws-us-east--dev-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A48",
        instruction=(
            "You are Priya Banerjee from Platform. In UAT, you want a reliable cache warmer for Commerce to cut cold-start misses. "
            "You confirm UAT network defaults, deploy the Commerce API cache_warmer Lambda from bundle 'bundle-cache-warmer-2025-08-06', "
            "put it on the default 15-minute schedule, attach a CloudWatch Errors alarm to the function ARN, run 'Lambda-Smoke', "
            "and record the change for 'fn-commerce-api-cache_warmer-uat'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle-cache-warmer-2025-08-06",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Lambda-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-functi-rate-15-minutes",
            "alarm_id: al-arn-aws-lambda-local-000000000000-functi-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-lambda-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A49",
        instruction=(
            "You are Priya Shah from Platform. In UAT, rotate the API auth header secret (purpose 'API_AUTH_HEADER') for Commerce’s use of "
            "the existing 'dcomm-uat-redis' cluster. After configuring the integration, You want to warm metadata and set trace sampling to 0.10 briefly "
            "to watch for authentication errors, then record the change for 'CacheAPI.ExternalSystemAuthHeader'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "cache_integration_verified: True",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A50",
        instruction=(
            "You are Alice Morgan from Checkout. In UAT, you want to validate that carts price correctly using today’s "
            "Standard pricebook without any promo code. You will upsert entries for 'SOCKS-001' at 5.0 and 'CAP-001' at 12.0, "
            "warm 'metadata' so pricing propagates, create a cart for alice@example.com with 3 × SOCKS-001 and 1 × CAP-001 "
            "using STANDARD shipping and no promo, run 'Checkout-Smoke', publish a 'pricing' dashboard for UAT visibility, "
            "and record the change for the created cart."
        ),
        actions=[
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard",
                    "items": [
                        {"product_code": "SOCKS-001", "unit_price": 5.0},
                        {"product_code": "CAP-001", "unit_price": 12.0},
                    ],
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "alice@example.com",
                    "items": [
                        {"product_code": "SOCKS-001", "qty": 3},
                        {"product_code": "CAP-001", "qty": 1},
                    ],
                    "promo_code": None,
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Checkout-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "pricing"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "cart-cust-alice-example-com-2025-08-06t12-00-00z",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "pbe_ids: ['pbe-pb-standard-socks-001','pbe-pb-standard-cap-001']",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "cart_id: cart-cust-alice-example-com-2025-08-06t12-00-00z",
            "total: 32.0",
            "run_id: run-checkout-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-pricing",
            "change_log_id: chg-ops-cart-cust-alice-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A51",
        instruction=(
            "You are Luis Ortega from Identity. In UAT, you want the 'Commerce API' app refreshed with a single managed secret and strict redirect. "
            "You want OAuth configured (api, openid) with callback https://acme.example/callback, store 'OAUTH_CLIENT_SECRET' from 'app-commerce-api', "
            "verify the callback domain is example.com, run 'OAuth-Smoke' in UAT, and record the update."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "scopes": ["api", "openid"],
                    "callback_urls": ["https://acme.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://acme.example/callback",
                    "expected_domain": "acme.example",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-commerce-api",
            "client_id: client-commerce-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
            "status: verified",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-oauth-app-commerce-api-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A52",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you want to harden the perimeter without breaking checkout. "
            "Confirm UAT network defaults for alignment, then restrict the 'Checkout Gateway' security group to TLS 443 for '10.0.5.0/24'. "
            "Surface the change on the 'api' dashboard and record the change with change_type 'networking' tied to 'sg-uat-checkout-gateway'."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Checkout Gateway"},
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.5.0/24"],
                },
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-5-0-24",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A53",
        instruction=(
            "You are Evan Brooks from Networking. In UAT, you want private access for the Cache Integration service to ElastiCache. "
            "Use the literal network IDs provided: VPC 'vpc-uat' and subnets 'subnet-uat-a' and 'subnet-uat-b' — do not resolve or substitute "
            "environment defaults like vpc-uat-0001. Create the interface endpoint for 'com.amazonaws.us-east-1.elasticache' in that VPC across those "
            "subnets, restrict 'Cache Integration' to Redis 6379 from 10.0.0.0/16, run a quick UAT SMOKE to confirm connectivity, and record the change "
            "for 'vpce-vpc-uat-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Cache Integration"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-uat-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A54",
        instruction=(
            "You are Omar Kelly from Performance. UAT shoppers are seeing stale offers and the cache hit rate is wobbling. You want to advance the "
            "Commerce cache partition 'dcomm' to v10, invalidate the specific offer keys 'offer:WINTER20' and 'offer:Thunderbolt Docking Station', "
            "then run a 'populate' warm. Keep an early-warning CacheHitRate alarm (74.0 / 300s, LessThanThreshold) on 'dcomm-uat-redis', you want to use trace "
            "sampling for short-term diagnostics, and record the change against 'dcomm-v10'."
        ),
        actions=[
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v10"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:WINTER20", "offer:Thunderbolt Docking Station"]},
            ),
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 74.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "populate"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v10", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v10",
            "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-74-0-300-lessthanthreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A55",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want 'B2B Wholesale' updated to 55.00 for 'USB-C Hub'. You want 'kelly.ross@example.com' "
            "on 'B2B Wholesale', a quick cart with 3× 'USB-C Hub' using 'B2BVOLUME15' and STANDARD shipping, and you want the change recorded for 'B2B Wholesale'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "B2B Wholesale",
                    "items": [{"product_code": "AC-USBC-HUB", "unit_price": 55.00}],
                },
            ),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "kelly.ross@example.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "kelly.ross@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 3}],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "B2B Wholesale", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 1",
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-kelly-ross-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A56",
        instruction=(
            "You are Raj Patel from Personalization. In UAT, add 'Prefer-Ent-Addon' for 'B2B-Enterprise' (addon_priority=enterprise_support) "
            "bound to B2BVOLUME15. You want to assign the 'B2B Wholesale' pricing tier to alex.cho@example.com to mirror enterprise pricing, then prove "
            "the behavior with a cart on 'USB-C Hub' using B2BVOLUME15 and STANDARD shipping. Record the change for 'ctx-b2b-enterprise-prefer-ent-addon'."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "B2B-Enterprise",
                    "rule_name_hint": "Prefer-Ent-Addon",
                    "attributes": {"addon_priority": "enterprise_support"},
                    "bind_to_offer_code": "B2BVOLUME15",
                },
            ),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "alex.cho@example.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "alex.cho@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-b2b-enterprise-prefer-ent-addon",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-b2b-enterprise-prefer-ent-addon",
            "cart_id: cart-cust-alex-cho-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A57",
        instruction=(
            "You are Arjun Mehta from API Platform. In UAT, you put Orders v1 online cleanly. "
            "You publish Orders v1 (1.0.0 from 'blob_orders_v1') and bind it to 'dcg-orders-v1-uat', with API metadata warmed, Gateway-SMOKE passing, "
            "and the rollout recorded for 'spec-orders-v1-1-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Orders v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_orders_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "orders-v1", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-orders-v1-1-0-0", "gateway_id": "dcg-orders-v1-uat"},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Gateway-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-orders-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-orders-v1-1-0-0",
            "dcg_id: dcg-orders-v1-uat",
            "run_id: run-gateway-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A58",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you need private connectivity to the internal offer service and a tighter Commerce boundary. "
            "Create a VPC interface endpoint for 'com.amazonaws.us-east-1.execute-api' in 'vpc-uat-main' across 'subnet-uat-a' and 'subnet-uat-b' "
            "using those exact IDs. Confirm the 'Commerce API' security group is in use and tighten ingress to port 443 from '10.0.0.0/16'. "
            "Run a quick 'SMOKE' for regressions, add a baseline 'Errors' alarm on 'sg-uat-commerce-api', and record the networking change for 'vpc-uat-main'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-main",
                    "service_name": "com.amazonaws.us-east-1.execute-api",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce API"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "sg-uat-commerce-api",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpc-uat-main",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-main-com-amazonaws-us-east-1-execute-api-subnet-uat-a-subnet-uat-b",
            "change_set_id: chg-sg-sg-uat-commerce-api-uat-commerce-api-443-10-0-0-0-16",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "alarm_id: al-sg-uat-commerce-api-errors-1-0-300-greaterthanorequaltothreshold",
            "change_log_id: chg-networking-vpc-uat-main-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A59",
        instruction=(
            "You are Dana Ruiz from Identity. In UAT, you want to refresh the 'Commerce API' connected app to use scopes "
            "api, refresh_token, and openid with callback https://acme.example/callback. You want to store BOTH secrets "
            "(OAUTH_CLIENT_SECRET and API_AUTH_HEADER), publish a lightweight 'oauth' dashboard for visibility, and record the update "
            "for 'app-commerce-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://acme.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "oauth"},
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-commerce-api",
            "secret_arn_oauth: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
            "secret_arn_api_auth: arn:secret-secret-api-auth-header-uat-app-commerce-api-alias-dcomm-uat",
            "dashboard_name: dash-uat-oauth",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A60",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, you want 'Standard Retail' updated to 60.25 for 'USB-C Hub'. You want a quick cart for "
            "'trialshopper@example.com' with 'USB-C Hub' and 'WELCOME5' using EXPRESS shipping, and you want the pricebook change recorded for 'Standard Retail'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "Standard Retail"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard Retail",
                    "items": [{"product_code": "AC-USBC-HUB", "unit_price": 60.25}],
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "trialshopper@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "Standard Retail", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 1",
            "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A61",
        instruction=(
            "You are Ravi Iyer from API Platform. In UAT, you want Pricing v2 live with just-enough visibility. "
            "Publish the **Pricing v2** OpenAPI (2.0.0 from 'blob_pricing_v2'), enable the 'pricing-v2' gateway, register endpoints, "
            "make an 'api' dashboard available for the team, run 'Pricing-v2-SMOKE', and **record the rollout for 'spec-pricing-v2-2-0-0'**."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Pricing v2",
                    "spec_version": "2.0.0",
                    "spec_blob_id": "blob_pricing_v2",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "pricing-v2", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-pricing-v2-2-0-0", "gateway_id": "dcg-pricing-v2-uat"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Pricing-v2-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-pricing-v2-2-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-pricing-v2-2-0-0",
            "dcg_id: dcg-pricing-v2-uat",
            "endpoint_id: ep-spec-pricing-v2-2-0-0-dcg-pricing-v2-uat",
            "dashboard_name: dash-uat-api",
            "run_id: run-pricing-v2-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-rollout-spec-pricing-v2-2-0-0-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A62",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want the Commerce API limited to the standard internal network on TLS and Redis, keep using the UAT cache cluster "
            "with AUTH/TLS, and expose ElastiCache privately in VPC 'vpc-uat-0001' on 'subnet-uat-a' and 'subnet-uat-b'. "
            "Point Commerce at dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com **with the existing secret and partition key 'dcomm-uat'**, "
            "run a quick metadata warm, create a 'cache' dashboard, and alert if cache hit rate drops below 76.0 in five-minute windows. "
            "Record the change for 'dcomm-uat-redis'."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce API"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443, 6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="set_redis_auth_and_tls", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 76.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-uat-redis",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-76-0-300-lessthanthreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A63",
        instruction=(
            "You are Luis Ortega from Identity. In UAT, you want the 'Orders API' connected app to allow api, refresh_token, and openid "
            "with callback https://orders.example/callback. You want to store 'OAUTH_CLIENT_SECRET' and an 'API_AUTH_HEADER' secret for "
            "'app-orders-api', run 'OAuth-Smoke', create an 'api' dashboard, and record the change for 'app-orders-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Orders API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://orders.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-orders-api",
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-orders-api",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-orders-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-orders-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-orders-api-alias-dcomm-uat",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A64",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want 'Standard Retail' updated to 63.25 for 'USB-C Hub' (AC-USBC-HUB) and 212.00 "
            "for 'Thunderbolt Docking Station' (HW-TB-DOCK), and 'B2B Wholesale' updated to 56.75 for AC-USBC-HUB and 182.50 for HW-TB-DOCK. "
            "You want 'm.rivera@apexlogistics.com' on 'B2B Wholesale', a cart with 2× AC-USBC-HUB and 1× HW-TB-DOCK using 'B2BVOLUME15' and "
            "STANDARD shipping, and you want the change recorded for 'B2B Wholesale'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "Standard Retail"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 63.25},
                        {"product_code": "HW-TB-DOCK", "unit_price": 212.00},
                    ],
                },
            ),
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 56.75},
                        {"product_code": "HW-TB-DOCK", "unit_price": 182.50},
                    ],
                },
            ),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 2},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "B2B Wholesale", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 2",
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A65",
        instruction=(
            "You are Raj Patel from Personalization. In UAT, you want consistent defaults for new and VIP shoppers bound to the same welcome code. "
            "Create 'Prefer-Express' for 'VIP' (shipping_preference='EXPRESS') and 'Prefer-Standard-New' for 'NewCustomers' (shipping_preference='STANDARD'), both bound to 'WELCOME5'. "
            "Run 'Context-Rule-SMOKE', then verify with a quick cart for 'trialshopper@example.com' for product_code 'AC-USBC-HUB' using 'WELCOME5' and 'EXPRESS' shipping, "
            "and record the change for 'ctx-vip-prefer-express'."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {"shipping_preference": "EXPRESS"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard-New",
                    "attributes": {"shipping_preference": "STANDARD"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Context-Rule-SMOKE"},
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "trialshopper@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-vip-prefer-express",
            "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A66",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you want private ElastiCache access finalized with basic visibility. "
            "Create a VPC interface endpoint for com.amazonaws.us-east-1.elasticache in 'vpc-uat-0001' (subnets 'subnet-uat-a' and 'subnet-uat-b'), "
            "restrict the 'Cache Integration' security group 'sg-uat-cache-integration' to 6379 from 10.0.0.0/16, add a 'NetworkBytesOut' alarm on the "
            "endpoint, and record the change for 'vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                    "metric_name": "NetworkBytesOut",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
            "change_set_id: chg-sg-sg-uat-cache-integration-uat-cache-integration-6379-10-0-0-0-16",
            "alarm_id: al-vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b-networkbytesout-1-0-300-greaterthanorequaltothreshold",
            "change_log_id: chg-networking-vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A67",
        instruction=(
            "You are Omar Kelly from Performance. In UAT, you carry out a clean 'dcomm' v11 bump on dcomm-uat-redis with light diagnostics. "
            "You clear the stale keys ('offer:USB-C Hub', 'offer:Thunderbolt Docking Station'), warm metadata, apply trace sampling at 0.13, "
            "set a CacheHitRate guardrail at 73.0 over 300 seconds with LessThanThreshold, and record the change for 'dcomm-v11'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v11"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={"keys": ["offer:USB-C Hub", "offer:Thunderbolt Docking Station"]},
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.13}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "CacheHitRate",
                    "threshold": 73.0,
                    "period_seconds": 300,
                    "comparison": "LessThanThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v11", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v11",
            "invalidated_count: 2",
            "job_run_id: run-load-api-metadata-2025-08-06t12-00-00z",
            "alarm_id: al-dcomm-uat-redis-cachehitrate-73-0-300-lessthanthreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A68",
        instruction=(
            "You want Checkout v3 visible in DEV without surprises. You want to publish spec 3.0.0 from blob_checkout_300, enable it behind "
            "'checkout-v3', register endpoints, and set trace sampling to 0.07 for initial traffic. You want to run 'Checkout-v3-SMOKE' to prove "
            "the basics, attach a 5xxErrorRate alarm (1.2 over 300s, GreaterThanOrEqualToThreshold) on the gateway, and you want the rollout "
            "recorded against the spec id."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Checkout v3",
                    "spec_version": "3.0.0",
                    "spec_blob_id": "blob_checkout_300",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={
                    "api_group_name": "checkout-v3",
                    "environment": "DEV",
                },
            ),
            Action(
                name="register_api_endpoints",
                kwargs={
                    "spec_id": "spec-checkout-v3-3-0-0",
                    "gateway_id": "dcg-checkout-v3-dev",
                },
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.07}),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "DEV",
                    "collection_name": "Checkout-v3-SMOKE",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-checkout-v3-dev",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.2,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-checkout-v3-3-0-0",
                    "environment": "DEV",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-checkout-v3-3-0-0",
            "dcg_id: dcg-checkout-v3-dev",
            "run_id: run-checkout-v3-smoke-dev-2025-08-06t12-00-00z",
            "alarm_id: al-dcg-checkout-v3-dev-5xxerrorrate-1-2-300-greaterthanorequaltothreshold",
            "change_log_id: chg-rollout-spec-checkout-v3-3-0-0-dev-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A69",
        instruction=(
            "You are Luis Ortega from Identity. In PROD, the 'Search API' connected app must allow api, refresh_token, and openid with the "
            "callback https://search.example/callback. You want to store the OAUTH_CLIENT_SECRET and an API_AUTH_HEADER secret for service calls, run 'OAuth-Smoke', "
            "publish an 'api' dashboard, and add an AuthFailureRate alarm at 1.0 over 300s (GreaterThanOrEqualToThreshold) for early warning. "
            "Record the change for 'app-search-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Search API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://search.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "PROD",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-search-api",
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "PROD",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "app-search-api",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "app-search-api",
                    "metric_name": "AuthFailureRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "PROD", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "PROD", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-search-api",
                    "environment": "PROD",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-search-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-prod-app-search-api-alias-dcomm-prod",
            "run_id: run-oauth-smoke-prod-2025-08-06t12-00-00z",
            "dashboard_name: dash-prod-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A70",
        instruction=(
            "You are Dana Li from Identity. In UAT, you want the 'Payments Portal' app secured with a strict redirect and a header secret. "
            "You want OAuth configured with scopes api and openid with callback https://pay.uat.example.com/oauth/callback, "
            "you want the callback domain verified against example.com, you want an API auth header stored as 'API_AUTH_HEADER' from "
            "'src_auth_header_payments', you want 'OAuth-Smoke' run in UAT, and you want the change recorded for 'app-payments-portal'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Payments Portal",
                    "scopes": ["api", "openid"],
                    "callback_urls": ["https://pay.uat.example.com/oauth/callback"],
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://pay.uat.example.com/oauth/callback",
                    "expected_domain": "pay.uat.example.com",
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "src_auth_header_payments",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-payments-portal",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-payments-portal",
            "client_id: client-payments-portal",
            "status: verified",
            "secret_arn: arn:secret-secret-api-auth-header-uat-src-auth-header-payments-alias-dcomm-uat",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-oauth-app-payments-portal-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A71",
        instruction=(
            "You want UAT’s cache auth header rotated without drama. You want to read the 'dcomm-uat-redis' cluster first, mint a new "
            "API_AUTH_HEADER secret sourced from that cluster, and point Commerce at the live endpoint with that secret and partition key 'dcomm-uat'. "
            "You want a quick metadata warm, baseline trace sampling at 0.10, a 'cache' dashboard, the required 'Errors' alarm at 1.0 over 300s "
            "(GreaterThanOrEqualToThreshold) on the cache, a simple 'SMOKE' run, and you want the change recorded for 'CacheAPI.ExternalSystemAuthHeader'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "cache_integration_verified: True",
            "dashboard_name: dash-uat-cache",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A72",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you want the Checkout Gateway limited to 10.0.5.0/24 on TLS 443 and verified. "
            "Run 'Gateway-SMOKE', apply the API monitoring baseline, and record the change for 'sg-uat-checkout-gateway'."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Checkout Gateway"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.5.0/24"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Gateway-SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "sg-uat-checkout-gateway",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-5-0-24",
            "dashboard_name: dash-uat-api",
            "run_id: run-gateway-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A73",
        instruction=(
            "You are Rafael Kim from SRE. In PROD, keep Search API’s cache warm on a recurring cadence and watch for failures and capacity issues. "
            "Deploy 'bundle_cachewarmer_v1' (purpose 'cache_warmer'), schedule it, publish a 'cache' dashboard, attach an Errors alarm at 1.0 over 300s "
            "(GreaterThanOrEqualToThreshold) and a Throttles alarm at 1.0 over 300s on "
            "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod, run a metadata warm now, run 'SMOKE', and record the change "
            "for 'fn-search-api-cache_warmer-prod'."
        ),
        actions=[
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "PROD",
                    "service_name": "Search API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod"
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "PROD", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod",
                    "metric_name": "Throttles",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "PROD", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-search-api-cache_warmer-prod",
                    "environment": "PROD",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-search-api-cache_warmer-prod",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-search-api-cache_warmer-prod-rate-15-minutes",
            "dashboard_name: dash-prod-cache",
            "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-search-api-cache_warmer-prod-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-prod-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A74",
        instruction=(
            "You are Priya Shah from Platform. In UAT, harden and wire the existing Redis cluster dcomm-uat-redis. "
            "Enable AUTH and TLS on dcomm-uat-redis, keep the partition key as 'dcomm-uat', "
            "ensure Commerce can reach Redis on 6379, and record the change."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="set_redis_auth_and_tls", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                    "partition_key": "dcomm-uat",
                },
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-uat-redis", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=["cluster_id: dcomm-uat-redis"],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A75",
        instruction=(
            "You are steering B2B users in UAT to wholesale pricing via context. Create or overwrite a rule for segment 'b2b' named 'PreferWholesalePricing' "
            "with attributes {'pricebook': 'B2B Wholesale'} bound to offer 'B2BVOLUME15'. You then warm the metadata cache, run the 'B2B-Offer-SMOKE' test and a standard 'SMOKE' test to prove the behavior, and record the personalization change."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "b2b",
                    "rule_name_hint": "PreferWholesalePricing",
                    "attributes": {"pricebook": "B2B Wholesale"},
                    "bind_to_offer_code": "B2BVOLUME15",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "B2B-Offer-SMOKE"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-b2b-preferwholesalepricing",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-b2b-preferwholesalepricing",
            "run_id: run-b2b-offer-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A76",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want the Commerce API secured to the standard internal network, "
            "ElastiCache reachable privately, and Commerce integrated with the UAT cache cluster. Apply the cache monitoring baseline "
            "and record the change for 'dcomm-uat-redis'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce API"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443, 6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="set_redis_auth_and_tls", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:aws:secretsmanager:local:000000000000:secret:dcomm-uat-redis",
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(name="create_cloudwatch_dashboard", kwargs={"environment": "UAT"}),
            Action(name="create_cloudwatch_alarm", kwargs={"resource_id": "dcomm-uat-redis"}),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-uat-redis", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "cache_integration_verified: True",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A77",
        instruction=(
            "You want Pricing v1 available in UAT with OAuth wired cleanly and basic visibility. "
            "Publish the Pricing v1 OpenAPI 1.0.0 from 'blob_pricing_v1', enable the 'pricing-v1' gateway, "
            "register endpoints, authorize a client 'Pricing-v1-Client' with scopes ['openid','profile','pricing.read'] and callback "
            "https://uat.example.com/oauth/callback, set trace sampling to 0.10, prove core paths with 'SMOKE' and OAuth basics with 'OAuth-Smoke', "
            "publish an 'api' dashboard, attach a 5xxErrorRate alarm to the gateway 'dcg-pricing-v1-uat', and record the rollout against 'spec-pricing-v1-1-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Pricing v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_pricing_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "pricing-v1", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-pricing-v1-1-0-0", "gateway_id": "dcg-pricing-v1-uat"},
            ),
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Pricing-v1-Client",
                    "scopes": ["openid", "profile", "pricing.read"],
                    "callback_urls": ["https://uat.example.com/oauth/callback"],
                },
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "OAuth-Smoke"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-pricing-v1-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-pricing-v1-1-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-pricing-v1-1-0-0",
            "dcg_id: dcg-pricing-v1-uat",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
            "alarm_id: al-dcg-pricing-v1-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A78",
        instruction=(
            "You are Casey Nguyen from CX. In UAT, you want a quick checkout smoke for a single-item cart with a welcome promo and a bit "
            "of signal for troubleshooting. Confirm the USB-C Hub product and WELCOME5 promo, build a cart for sam@example.com with that "
            "item and STANDARD shipping, briefly sample traces at 0.07 to observe the path, run Checkout-Smoke, and record the change."
        ),
        actions=[
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "sam@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.07}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Checkout-Smoke"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "cart-cust-sam-example-com-2025-08-06t12-00-00z",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "product_id: 1002",
            "offer_id: 503",
            "cart_id: cart-cust-sam-example-com-2025-08-06t12-00-00z",
            "policy_id: trace-0-07",
            "run_id: run-checkout-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-ops-cart-cust-sam-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A79",
        instruction=(
            "You are tightening surface area for Commerce API in UAT. Restrict SG 'sg-uat-commerce-api' to CIDR 10.0.0.0/16 on TCP 443, read back rules, "
            "warm metadata, run 'Gateway-SMOKE' and 'SMOKE', and record the security change for 'sg-uat-commerce-api'."
        ),
        actions=[
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="get_security_group_rules", kwargs={"security_group_id": "sg-uat-commerce-api"}
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Gateway-SMOKE"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "change_type": "security",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-commerce-api-uat-commerce-api-443-10-0-0-0-16",
            "run_id: run-gateway-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A80",
        instruction=(
            "You are Rafael Gomez from Platform. In UAT, you want the Inventory service reachable privately without surprises. You will create a VPC interface endpoint for 'com.apis.inventory-v1' in vpc-uat-0001 (subnets subnet-uat-a and subnet-uat-b), "
            "warm the metadata cache to ensure resolution, run the 'Inventory-v1-SMOKE' test collection, and record the change for the new endpoint."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.apis.inventory-v1",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Inventory-v1-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-uat-0001-com-apis-inventory-v1-subnet-uat-a-subnet-uat-b",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-0001-com-apis-inventory-v1-subnet-uat-a-subnet-uat-b",
            "run_id: run-inventory-v1-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A81",
        instruction=(
            "You’re running a quick VIP checkout sanity pass in UAT. Your VIPs have been telling Support that the site feels slower "
            "when they’re just trying to buy a cable, so you want the experience to gently bias toward faster shipping whenever they use WELCOME5. "
            "You add a ‘Prefer-Express’ rule on the VIP segment and bind it to WELCOME5, using the business attribute shipping_preference=EXPRESS "
            "so the UI hints are obvious. Trial shopper trialshopper@example.com is **already VIP in UAT**, so you don’t change their tier; "
            "you simply prove the rule end-to-end with a real cart for AC-USBC-HUB using promo WELCOME5 and EXPRESS shipping. "
            "Give the rule a quick context smoke so you know it’s live, then record the personalization change against the rule id for audit."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {"shipping_preference": "EXPRESS"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "UAT",
                    "collection_name": "Context-Rule-SMOKE",
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "trialshopper@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-vip-prefer-express",
            "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A82",
        instruction=(
            "You are Rafael Kim from SRE. In UAT, cold starts on Commerce spike overnight, so you want a small cache warmer with baseline monitoring. "
            "First confirm UAT network defaults so scheduling and metrics hook up cleanly, then deploy the Commerce API warmer from 'bundle_cachewarmer_v1' "
            "with function_purpose 'cache_warmer' and put it on the usual 15-minute cadence. Publish the cache dashboard and attach an 'Errors' alarm at 1.0 over 300s "
            "targeted to the function’s ARN (not just the short name). Kick a 'metadata' warm now, enable trace sampling at 0.08 for short-term visibility, "
            "run 'SMOKE' in UAT, and record the ops change to 'fn-commerce-api-cache_warmer-uat'."
        ),
        actions=[
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(name="create_cloudwatch_dashboard", kwargs={"environment": "UAT"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.08}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A83",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want the Commerce cache advanced and proven on dcomm-uat-redis. "
            "You move the 'dcomm' partition to v13, clear stale offer keys ('offer:USB-C Hub', 'offer:Thunderbolt Docking Station', 'offer:WELCOME5', 'offer:WINTER20'), "
            "create the nightly cache maintenance schedule (idempotent), warm metadata and populate hot paths, apply 0.10 trace sampling for short-term visibility, "
            "keep the 'cache' dashboard and Errors alarm baseline, run SMOKE, and record the change for 'dcomm-v13'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="set_cache_partition_key", kwargs={"partition_key": "dcomm", "version": "v13"}
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5",
                        "offer:WINTER20",
                    ],
                },
            ),
            Action(
                name="manage_cache_maintenance", kwargs={"environment": "UAT", "action": "create"}
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "populate"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "dcomm-v13", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "applied_version: v13",
            "schedule_id: cm-uat",
            "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A84",
        instruction=(
            "You are Dana Brooks from API. You want to ship a tiny pre-UAT guard for Catalog v3 so partners don’t get caught by surprise. "
            "You want OpenAPI spec 3.1.1 from blob 'blob_905' published as 'Catalog v3', then you want the 'catalog-v3' gateway enabled in UAT. "
            "You want the endpoints registered for gateway id 'dcg-catalog-v3-uat' and you want a single CloudWatch alarm on that gateway "
            "for 'Errors' at 1.0 over 300 seconds (GreaterThanOrEqualToThreshold) to catch bad deploys fast. "
            "You want the change recorded against 'spec-catalog-v3-3-1-1' in UAT so audit can track who did what and when."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Catalog v3",
                    "spec_version": "3.1.1",
                    "spec_blob_id": "blob_905",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "catalog-v3", "environment": "UAT"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-catalog-v3-3-1-1", "gateway_id": "dcg-catalog-v3-uat"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-catalog-v3-uat",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-catalog-v3-3-1-1",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A85",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want retail and wholesale pricing tuned by setting 'Standard Retail' to 61.25 for 'AC-USBC-HUB' and 206.5 for 'HW-TB-DOCK'; also setting 'B2B Wholesale' to 56.25 for "
            "'AC-USBC-HUB' and 181.75 for 'HW-TB-DOCK'. You want to validate creating a cart for 'pat.jones@example.com' with 'AC-USBC-HUB' and 'HW-TB-DOCK' using 'WELCOME5'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "Standard Retail"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 61.25},
                        {"product_code": "HW-TB-DOCK", "unit_price": 206.50},
                    ],
                },
            ),
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 56.25},
                        {"product_code": "HW-TB-DOCK", "unit_price": 181.75},
                    ],
                },
            ),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "pat.jones@example.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 1},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "WELCOME5",
                },
            ),
        ],
        outputs=[
            "upserted_count: 2",
            "cart_id: cart-cust-pat-jones-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A86",
        instruction=(
            "You are Amira Patel from Networking. You want to checkout Gateway needs to be on the standard internal network in UAT. Confirm environment defaults first, "
            "then you want to enforce TLS 443 to 10.0.0.0/16, verify basic reachability, attach baseline API monitoring, and record the change for 'sg-uat-checkout-gateway'."
        ),
        actions=[
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Checkout Gateway"},
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "sg-uat-checkout-gateway",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "sg-uat-checkout-gateway",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "change_set_id: chg-sg-sg-uat-checkout-gateway-uat-checkout-gateway-443-10-0-0-0-16",
            "dashboard_name: dash-uat-api",
            "alarm_id: al-sg-uat-checkout-gateway-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A87",
        instruction=(
            "You want Checkout API in DEV kept warm on a steady cadence and monitored at baseline. "
            "You want the 'bundle_cachewarmer_v1' Lambda deployed for purpose 'cache_warmer', "
            "scheduled to run regularly, a 'cache' dashboard published, trace sampling briefly set to 0.07 "
            "to observe warm cycles, an Errors alarm on the function ARN at 1.0 over 300s with "
            "GreaterThanOrEqualToThreshold, nightly cache maintenance created (instead of a one-off warm), "
            "a 'SMOKE' run, and you want the ops change recorded for 'fn-checkout-api-cache_warmer-dev'."
        ),
        actions=[
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "DEV",
                    "service_name": "Checkout API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={
                    "environment": "DEV",
                    "purpose": "cache",
                },
            ),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.07}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="manage_cache_maintenance",
                kwargs={
                    "environment": "DEV",
                    "action": "create",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "DEV",
                    "collection_name": "SMOKE",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-checkout-api-cache_warmer-dev",
                    "environment": "DEV",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-checkout-api-cache_warmer-dev",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-functi-rate-15-minutes",
            "dashboard_name: dash-dev-cache",
            "alarm_id: al-arn-aws-lambda-local-000000000000-functi-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-dev-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A88",
        instruction=(
            "You want Orders v1 in PROD live behind 'orders-v1' with OAuth verified. "
            "You want version 1.0.0 from blob_orders_v1 published and routed, client hint 'Orders-v1-Client' "
            "authorized with scopes ['openid','profile','orders.read'] and callback https://prod.example.com/oauth/callback, "
            "core paths proven with SMOKE, OAuth basics proven with 'OAuth-Smoke', baseline API monitoring enabled "
            "('api' dashboard + 5xxErrorRate alarm on the gateway), and you want the rollout recorded to the spec id."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Orders v1",
                    "spec_version": "1.0.0",
                    "spec_blob_id": "blob_orders_v1",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={
                    "api_group_name": "orders-v1",
                    "environment": "PROD",
                },
            ),
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Orders-v1-Client",
                    "scopes": ["openid", "profile", "orders.read"],
                    "callback_urls": ["https://prod.example.com/oauth/callback"],
                },
            ),
            Action(
                name="register_api_endpoints",
                kwargs={
                    "spec_id": "spec-orders-v1-1-0-0",
                    "gateway_id": "dcg-orders-v1-prod",
                },
            ),
            Action(name="run_test_collection", kwargs={"environment": "PROD"}),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "PROD",
                    "collection_name": "OAuth-Smoke",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={
                    "environment": "PROD",
                    "purpose": "api",
                },
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-orders-v1-prod",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-orders-v1-1-0-0",
                    "environment": "PROD",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-orders-v1-1-0-0",
            "dcg_id: dcg-orders-v1-prod",
            "run_id: run-smoke-prod-2025-08-06t12-00-00z",
            "dashboard_name: dash-prod-api",
            "alarm_id: al-dcg-orders-v1-prod-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A89",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want to pause WINTER20 and explicitly set WELCOME5 active, validate with a cart for "
            "'newuser2@example.com', run 'Promo-SMOKE', and record the change for 'WINTER20'."
        ),
        actions=[
            Action(name="get_offer_by_code", kwargs={"offer_code": "WINTER20"}),
            Action(name="upsert_promotion", kwargs={"code": "WINTER20", "active": False}),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(name="upsert_promotion", kwargs={"code": "WELCOME5", "active": True}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "newuser2@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Promo-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "WINTER20", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "promo_id: promo-winter20",
            "cart_id: cart-cust-newuser2-example-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A90",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want Commerce to rotate its API auth header secret for the existing 'dcomm-uat-redis' cache cluster and confirm end-to-end cache usage. "
            "You will apply the cache monitoring baseline and record the change for 'CacheAPI.ExternalSystemAuthHeader'."
        ),
        actions=[
            Action(name="get_cache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "API_AUTH_HEADER",
                    "value_source_id": "dcomm-uat-redis",
                },
            ),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "external_url": "dcomm-uat-redis.abcdef.ng.0001.use1.cache.amazonaws.com",
                    "auth_header_secret_arn": "arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(name="create_cloudwatch_alarm", kwargs={"resource_id": "dcomm-uat-redis"}),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "CacheAPI.ExternalSystemAuthHeader",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "secret_arn: arn:secret-secret-api-auth-header-uat-dcomm-uat-redis-alias-dcomm-uat",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
            "cache_integration_verified: True",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A91",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you want to harden Commerce to the standard internal network, make "
            "ElastiCache private, enable AUTH and TLS on the UAT cache cluster (no new header secret rotation), move the "
            "cache partition 'dcomm' to 'v14', invalidate 'offer:USB-C Hub', 'offer:Thunderbolt Docking Station', and "
            "'offer:WELCOME5', and record the change for 'dcomm-v14'. You want the exact service name 'Commerce' used for "
            "the security group."
        ),
        actions=[
            Action(
                name="get_environment_network_defaults",
                kwargs={"environment": "UAT"},
            ),
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "UAT", "service_name": "Commerce"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce",
                    "environment": "UAT",
                    "service_name": "Commerce",
                    "tcp_ports": [443, 6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="get_cache_cluster",
                kwargs={"cluster_id": "dcomm-uat-redis"},
            ),
            Action(
                name="set_redis_auth_and_tls",
                kwargs={"cluster_id": "dcomm-uat-redis"},
            ),
            Action(
                name="set_cache_partition_key",
                kwargs={"partition_key": "dcomm", "version": "v14"},
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5",
                    ]
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-v14",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-uat-0001-com-amazonaws-us-east-1-elasticache-subnet-uat-a-subnet-uat-b",
            "applied_version: v14",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A92",
        instruction=(
            "You are Dana Brooks from API. Partners in UAT require private access to Catalog v5 over PrivateLink. Make version 5.0.0 "
            "(from blob_catalog_500) available behind 'catalog-v5' and ensure the PrivateLink service 'com.apis.catalog-v5' is in place. "
            "Verify with SMOKE, enable baseline API monitoring on the gateway, and record the rollout to the spec id 'spec-catalog-v5-5-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Catalog v5",
                    "spec_version": "5.0.0",
                    "spec_blob_id": "blob_catalog_500",
                },
            ),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "catalog-v5", "environment": "UAT"},
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "UAT"}),
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-uat-0001",
                    "service_name": "com.apis.catalog-v5",
                    "subnet_ids": ["subnet-uat-a", "subnet-uat-b"],
                },
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-catalog-v5-5-0-0", "gateway_id": "dcg-catalog-v5-uat"},
            ),
            Action(name="run_test_collection", kwargs={"environment": "UAT"}),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-catalog-v5-uat",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-catalog-v5-5-0-0",
                    "environment": "UAT",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-catalog-v5-5-0-0",
            "dcg_id: dcg-catalog-v5-uat",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
            "alarm_id: al-dcg-catalog-v5-uat-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A93",
        instruction=(
            "You are Luis Ortega from Identity. In UAT, you want the 'Commerce API' connected app refreshed with scopes "
            "api, refresh_token, openid and a single callback https://acme.example/callback. You want to store the client secret "
            "as 'OAUTH_CLIENT_SECRET' using source 'app-commerce-api', verify the callback domain matches example.com, run "
            "'OAuth-Smoke' in UAT, and record the update for 'app-commerce-api'."
        ),
        actions=[
            Action(
                name="configure_connected_app_oauth",
                kwargs={
                    "app_name_hint": "Commerce API",
                    "scopes": ["api", "refresh_token", "openid"],
                    "callback_urls": ["https://acme.example/callback"],
                },
            ),
            Action(
                name="create_secret_for",
                kwargs={
                    "environment": "UAT",
                    "purpose": "OAUTH_CLIENT_SECRET",
                    "value_source_id": "app-commerce-api",
                },
            ),
            Action(
                name="verify_oauth_redirect_domain",
                kwargs={
                    "callback_url": "https://acme.example/callback",
                    "expected_domain": "acme.example",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={
                    "environment": "UAT",
                    "collection_name": "OAuth-Smoke",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "app-commerce-api",
                    "environment": "UAT",
                    "change_type": "oauth",
                },
            ),
        ],
        outputs=[
            "app_id: app-commerce-api",
            "client_id: client-commerce-api",
            "secret_arn: arn:secret-secret-oauth-client-secret-uat-app-commerce-api-alias-dcomm-uat",
            "status: verified",
            "run_id: run-oauth-smoke-uat-2025-08-06t12-00-00z",
            "change_log_id: chg-oauth-app-commerce-api-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A94",
        instruction=(
            "You are Amira Patel from Networking. In PROD, you want private ElastiCache access and you want both Checkout "
            "Gateway and Cache Integration secured to the standard internal network. You want a VPC interface endpoint for "
            "com.amazonaws.us-east-1.elasticache in vpc-prod-0001 (subnets subnet-prod-a, subnet-prod-b), you want "
            "Checkout Gateway restricted to 443 from 10.0.0.0/16, you want Cache Integration restricted to 6379 from "
            "10.0.0.0/16, and you want to record the networking change for "
            "'vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-prod-0001",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-prod-a", "subnet-prod-b"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "PROD", "service_name": "Checkout Gateway"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-prod-checkout-gateway",
                    "environment": "PROD",
                    "service_name": "Checkout Gateway",
                    "tcp_ports": [443],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="get_service_security_group",
                kwargs={"environment": "PROD", "service_name": "Cache Integration"},
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-prod-cache-integration",
                    "environment": "PROD",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
                    "environment": "PROD",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-prod-0001-com-amazonaws-us-east-1-elasticache-subnet-prod-a-subnet-prod-b",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A95",
        instruction=(
            "You are Kelly Nguyen from Sales Ops. In UAT, you want pricebooks aligned for retail and wholesale, apply the 'B2B Wholesale' tier to "
            "'m.rivera@apexlogistics.com', and verify with a cart of 2× AC-USBC-HUB and 1× HW-TB-DOCK using B2BVOLUME15 and STANDARD shipping. "
            "Set 'Standard Retail' to 62.0 and 208.0; set 'B2B Wholesale' to 56.0 and 182.0 (for AC-USBC-HUB and HW-TB-DOCK). "
            "Run 'Pricing-SMOKE' and record the change for 'B2B Wholesale'."
        ),
        actions=[
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "Standard Retail"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "Standard Retail",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 62.00},
                        {"product_code": "HW-TB-DOCK", "unit_price": 208.00},
                    ],
                },
            ),
            Action(name="get_pricebook_by_name", kwargs={"pricebook_name": "B2B Wholesale"}),
            Action(
                name="upsert_pricebook_entries_batch",
                kwargs={
                    "pricebook_name": "B2B Wholesale",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "unit_price": 56.00},
                        {"product_code": "HW-TB-DOCK", "unit_price": 182.00},
                    ],
                },
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "B2BVOLUME15"}),
            Action(
                name="set_pricing_tier_for_customer",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "pricing_tier_name": "B2B Wholesale",
                },
            ),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "m.rivera@apexlogistics.com",
                    "items": [
                        {"product_code": "AC-USBC-HUB", "qty": 2},
                        {"product_code": "HW-TB-DOCK", "qty": 1},
                    ],
                    "promo_code": "B2BVOLUME15",
                    "shipping_method": "STANDARD",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Pricing-SMOKE"},
            ),
            Action(
                name="record_api_change_log",
                kwargs={"target_id": "B2B Wholesale", "environment": "UAT", "change_type": "ops"},
            ),
        ],
        outputs=[
            "upserted_count: 2",
            "applied_tier: B2B Wholesale",
            "cart_id: cart-cust-m-rivera-apexlogistics-com-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A96",
        instruction=(
            "You are Raj Patel from Personalization. In UAT, you want to adjust shipper for VIP to prefer EXPRESS. You should honor both VIP and new customers with WELCOME5, "
            "then verified with a quick cart for 'trialshopper@example.com'. Keep the experience visible with an 'api' dashboard and record the change for 'ctx-vip-prefer-express'."
        ),
        actions=[
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "VIP",
                    "rule_name_hint": "Prefer-Express",
                    "attributes": {"shipping_preference": "EXPRESS"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="upsert_context_rule",
                kwargs={
                    "segment_name": "NewCustomers",
                    "rule_name_hint": "Prefer-Standard",
                    "attributes": {"shipping_preference": "STANDARD"},
                    "bind_to_offer_code": "WELCOME5",
                },
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "Context-Rule-SMOKE"},
            ),
            Action(name="get_offer_by_code", kwargs={"offer_code": "WELCOME5"}),
            Action(
                name="create_cart_with_items",
                kwargs={
                    "customer_email": "trialshopper@example.com",
                    "items": [{"product_code": "AC-USBC-HUB", "qty": 1}],
                    "promo_code": "WELCOME5",
                    "shipping_method": "EXPRESS",
                },
            ),
            Action(
                name="create_cloudwatch_dashboard", kwargs={"environment": "UAT", "purpose": "api"}
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "ctx-vip-prefer-express",
                    "environment": "UAT",
                    "change_type": "personalization",
                },
            ),
        ],
        outputs=[
            "context_rule_id: ctx-vip-prefer-express",
            "cart_id: cart-cust-trialshopper-example-com-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-api",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A97",
        instruction=(
            "You are Rafael Kim from SRE. In UAT, you want the Commerce API cache warmer running every 15 minutes and monitored at baseline. "
            "Use the bundle 'bundle_cachewarmer_v1' for a 'cache_warmer' function, run a quick metadata warm, apply sampling at 0.10, "
            "and record the change for 'fn-commerce-api-cache_warmer-uat'."
        ),
        actions=[
            Action(
                name="deploy_lambda_function",
                kwargs={
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "source_bundle_id": "bundle_cachewarmer_v1",
                    "function_purpose": "cache_warmer",
                },
            ),
            Action(
                name="create_lambda_schedule",
                kwargs={
                    "function_arn": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(name="create_cloudwatch_dashboard", kwargs={"environment": "UAT"}),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat"
                },
            ),
            Action(name="run_cache_warm_jobs", kwargs={"mode": "metadata"}),
            Action(name="run_test_collection", kwargs={"environment": "UAT"}),
            Action(name="configure_trace_sampling", kwargs={"sample_rate": 0.10}),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "fn-commerce-api-cache_warmer-uat",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "function_arn: arn:aws:lambda:local:000000000000:function:fn-commerce-api-cache_warmer-uat",
            "schedule_id: sched-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-rate-15-minutes",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-arn-aws-lambda-local-000000000000-function-fn-commerce-api-cache_warmer-uat-errors-1-0-300-greaterthanorequaltothreshold",
            "run_id: run-smoke-uat-2025-08-06t12-00-00z",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A98",
        instruction=(
            "You are Dana Brooks from API. For a DEV cut of Payments v3, confirm environment network defaults, "
            "roll out version 3.0.0 from 'blob_payments_300' behind 'payments-v3', verify core paths with 'SMOKE', "
            "attach a 5xx error-rate alarm to the gateway 'dcg-payments-v3-dev' (not the spec), and record the rollout against 'spec-payments-v3-3-0-0'."
        ),
        actions=[
            Action(
                name="publish_openapi_spec",
                kwargs={
                    "spec_name": "Payments v3",
                    "spec_version": "3.0.0",
                    "spec_blob_id": "blob_payments_300",
                },
            ),
            Action(name="get_environment_network_defaults", kwargs={"environment": "DEV"}),
            Action(
                name="enable_digital_commerce_gateway",
                kwargs={"api_group_name": "payments-v3", "environment": "DEV"},
            ),
            Action(
                name="register_api_endpoints",
                kwargs={"spec_id": "spec-payments-v3-3-0-0", "gateway_id": "dcg-payments-v3-dev"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "DEV", "collection_name": "SMOKE"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcg-payments-v3-dev",
                    "metric_name": "5xxErrorRate",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "spec-payments-v3-3-0-0",
                    "environment": "DEV",
                    "change_type": "rollout",
                },
            ),
        ],
        outputs=[
            "spec_id: spec-payments-v3-3-0-0",
            "dcg_id: dcg-payments-v3-dev",
            "run_id: run-smoke-dev-2025-08-06t12-00-00z",
            "alarm_id: al-dcg-payments-v3-dev-5xxerrorrate-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A99",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you’re preparing Commerce for a campaign and want a clean cache cutover on dcomm-uat-redis. "
            "You move the 'dcomm' partition to v15, clear stale offer keys ('offer:USB-C Hub', 'offer:Thunderbolt Docking Station', 'offer:WELCOME5', "
            "'offer:WINTER20', 'offer:B2BVOLUME15'), keep nightly cache maintenance running, give ops baseline visibility with a 'cache' dashboard and an "
            "Errors alarm on dcomm-uat-redis, run a quick SMOKE check, and record the change under 'dcomm-v15'."
        ),
        actions=[
            Action(
                name="get_cache_cluster",
                kwargs={"cluster_id": "dcomm-uat-redis"},
            ),
            Action(
                name="set_cache_partition_key",
                kwargs={"partition_key": "dcomm", "version": "v15"},
            ),
            Action(
                name="invalidate_cache_by_keys",
                kwargs={
                    "keys": [
                        "offer:USB-C Hub",
                        "offer:Thunderbolt Docking Station",
                        "offer:WELCOME5",
                        "offer:WINTER20",
                        "offer:B2BVOLUME15",
                    ]
                },
            ),
            Action(
                name="manage_cache_maintenance",
                kwargs={"environment": "UAT", "action": "create"},
            ),
            Action(
                name="run_cache_warm_jobs",
                kwargs={"mode": "metadata"},
            ),
            Action(
                name="run_test_collection",
                kwargs={"environment": "UAT", "collection_name": "SMOKE"},
            ),
            Action(
                name="create_cloudwatch_dashboard",
                kwargs={"environment": "UAT", "purpose": "cache"},
            ),
            Action(
                name="create_cloudwatch_alarm",
                kwargs={
                    "resource_id": "dcomm-uat-redis",
                    "metric_name": "Errors",
                    "threshold": 1.0,
                    "period_seconds": 300,
                    "comparison": "GreaterThanOrEqualToThreshold",
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "dcomm-v15",
                    "environment": "UAT",
                    "change_type": "ops",
                },
            ),
        ],
        outputs=[
            "applied_version: v15",
            "schedule_id: cm-uat",
            "job_run_id: run-populate-cache-job-2025-08-06t12-00-00z",
            "dashboard_name: dash-uat-cache",
            "alarm_id: al-dcomm-uat-redis-errors-1-0-300-greaterthanorequaltothreshold",
        ],
    ),
    Task(
        annotator="aws_v1",
        user_id="task_A100",
        instruction=(
            "You are Amira Patel from Networking. In UAT, you want private access to ElastiCache and tight rules for the two client services. "
            "Create a VPC interface endpoint for com.amazonaws.us-east-1.elasticache in 'vpc-resolved' (subnet 'subnet-a'). "
            "Tighten the 'Commerce API' security group 'sg-uat-commerce-api' to 443 and 6379 from 10.0.0.0/16, and tighten the 'Cache Integration' "
            "security group 'sg-uat-cache-integration' to 6379 from 10.0.0.0/16. Record the networking change for "
            "'vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a'."
        ),
        actions=[
            Action(
                name="create_interface_endpoint",
                kwargs={
                    "vpc_id": "vpc-resolved",
                    "service_name": "com.amazonaws.us-east-1.elasticache",
                    "subnet_ids": ["subnet-a"],
                },
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-commerce-api",
                    "environment": "UAT",
                    "service_name": "Commerce API",
                    "tcp_ports": [443, 6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="update_security_group_ruleset",
                kwargs={
                    "sg_id": "sg-uat-cache-integration",
                    "environment": "UAT",
                    "service_name": "Cache Integration",
                    "tcp_ports": [6379],
                    "allowlist_cidrs": ["10.0.0.0/16"],
                },
            ),
            Action(
                name="record_api_change_log",
                kwargs={
                    "target_id": "vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a",
                    "environment": "UAT",
                    "change_type": "networking",
                },
            ),
        ],
        outputs=[
            "endpoint_id: vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a",
            "change_set_id_commerce: chg-sg-sg-uat-commerce-api-uat-commerce-api-443-6379-10-0-0-0-16",
            "change_set_id_cache: chg-sg-sg-uat-cache-integration-uat-cache-integration-6379-10-0-0-0-16",
            "change_log_id: chg-networking-vpce-vpc-resolved-com-amazonaws-us-east-1-elasticache-subnet-a-uat-2025-08-06t12-00-00z",
        ],
    ),
]
