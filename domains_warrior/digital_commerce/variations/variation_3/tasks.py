from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="v3",
        user_id="task_001",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want to turn on Stripe for MERCH_001 so finance can settle USD payments, "
            "cap checkout traffic at 50 rpm on /checkout to blunt bot spikes, "
            "and stand up CloudFront in us-east-1 to speed up static assets. "
            "You also want to browse Computer Accessories and request similar_products on your profile to prime cross-sell. "
            "Output the recommendation product name with highest confidence."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_001",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 50},
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="search_products_by_category",
                kwargs={"category_name": "Computer Accessories", "account_id": "108"},
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "209", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=["ProBook X15"],
    ),
    Task(
        annotator="v3",
        user_id="task_002",
        instruction=(
            "You are Jane Smith at Global Tech Inc., using 'jane.smith@globaltech.com'. "
            "You want to review your last 30d of activity first to sanity-check targeting. "
            "Next, you want to define a high-value audience for the last 90 days—customers with at least five orders—and save it as the segment 'High-Value-90d' so marketing can target repeat buyers. "
            "Create the segment directly from those 90-day criteria; do not run an additional 90-day analysis step. "
            "After the segment exists, you want to launch a 10% promo called 'HV-10' to that 'High-Value-90d' cohort."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "202", "analysis_period": "30d"},
            ),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "High-Value-90d",
                    "criteria": {"min_orders": 5, "period_days": 90},
                },
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "HV-10",
                    "target_segment": "High-Value-90d",
                    "discount_percentage": 10,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_003",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want to bring on ProMouse Co so you can formalize RMAs and stabilize lead times (contact support@promouse.example). "
            "To avoid ID mistakes, you want to find the product by name—'Pro Gaming Mouse'—before making changes. "
            "You want to restock that mouse by 25 units to cover Q4 demand, and standardize its list price at 89.99 so channels stay aligned. "
            "You also want to improve West Coast performance by configuring Akamai in us-west-2."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {"contact_email": "support@promouse.example"},
                },
            ),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1013",
                    "quantity_adjustment": 25,
                    "movement_type": "restock",
                },
            ),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1013"],
                    "update_data": {"list_price": 89.99},
                },
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Akamai", "region": "us-west-2"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_004",
        instruction=(
            "You’re Alice Johnson at Apex Logistics, using 'alice.j@email.com'. "
            "You want your dev Redis cache 'dcomm-dev-redis' ready for peak traffic as cache.r5.large with three nodes, "
            "and you want access locked to internal traffic only by tightening sg-0123456789abcdef0 to TCP 6379 from 10.0.0.0/16. "
            "Before checkout, you want to find the item by name—'USB-C Hub'—so you don’t rely on a stale ID. "
            "Then you want to place a quick order for 1 unit with the welcome discount WELCOME5 and return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(
                name="optimize_security_group_rules",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_005",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want your services to call commerce APIs without manual tokens by enabling APP900 with read/write permissions and the OAuth scopes api and refresh_token, "
            "and you want the connected app’s profile verified. "
            "To protect the auth plane, you want the token endpoint capped at 600 rpm on /oauth/token and you want the limit confirmed."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP900",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP900"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/oauth/token", "rate_limit": 600},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/oauth/token"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_006",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want to accept cards in Europe by enabling Adyen for MERCH_002 so finance can settle in USD and EUR. "
            "You then want the exact EU shipping rule 'EU-Std' applied on the EU zone with tracking disabled (False) so costs stay predictable. "
            "To boost attach rate, you also want similar_products recommendations on your profile."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_002",
                    "supported_currencies": ["USD", "EUR"],
                },
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": False,
                    "customer_id": "206",
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "206", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_007",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want a clean rollback point by running a full backup to s3 and checking its details. "
            "You’ll add supplier USB Hub Works (hello@usbhub.example) to formalize replenishment. "
            "Before any stock move, you’ll find the item by name—'Pro Gaming Mouse'—so you’re not relying on a stale ID. "
            "You want to reserve one unit (movement type: reserve) by decreasing on-hand by 1, then place a quick order with WELCOME5. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "USB Hub Works",
                    "action": "add",
                    "supplier_data": {"contact_email": "hello@usbhub.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1013",
                    "quantity_adjustment": -1,
                    "movement_type": "reserve",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_008",
        instruction=(
            "You’re Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want to record post-purchase feedback — “Order arrived early” with a five-star rating — so CX has a paper trail. "
            "You also want to add 50 loyalty points to reinforce the experience. "
            "Before checkout, you’ll find the item by name—'Ergo Laptop Stand'—to avoid browsing noise, then apply the welcome discount WELCOME5 and complete the purchase of 2 unit. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "sandra.d@email.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "208", "feedback_text": "Order arrived early", "rating": 5},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "208", "action": "add", "points": 50},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [{"product_id": "1010", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_009",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want your dev Redis cache 'dcomm-dev-redis' ready as cache.r5.large with three nodes, "
            "and you want access locked to the dev subnet by tightening sg-0123456789abcdef0 to a single 6379/TCP ingress from 10.0.5.0/24. "
            "After the change, you want to confirm cache details and learn all similar_products on your profile to sanity-check personalization."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(
                name="optimize_security_group_rules",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.5.0/24",
                },
            ),
            Action(name="get_cache_cluster_info", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "205", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=["ProBook X15", "Wireless Mouse", "USB-C Hub"],
    ),
    Task(
        annotator="v3",
        user_id="task_010",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want faster delivery by applying the US-Priority shipping rule in the US zone with tracking enabled (True). "
            "You also want to protect checkout by capping /checkout at 75 rpm and you want the limit confirmed. "
            "Then you want to find 'Wireless Mouse' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "207",
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 75},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "US-Priority"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_011",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to enable APP900 for headless API access by granting read and write permissions and the OAuth scopes api and refresh_token, then confirm the app profile. "
            "Before any release activity, you also want a clean rollback point by running a full backup to s3 and checking its details."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP900",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP900"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_012",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want to work on the laptop stand line: first find it by name — 'Ergo Laptop Stand' — so you avoid ID mistakes. "
            "Then you want to onboard ErgoWorks (ops@ergoworks.example) as a supplier to stabilize replenishment, "
            "restock by 10 units to cover an upcoming promo, and standardize the list price at 59.00 so channels stay aligned."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ErgoWorks",
                    "action": "add",
                    "supplier_data": {"contact_email": "ops@ergoworks.example"},
                },
            ),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1010",
                    "quantity_adjustment": 10,
                    "movement_type": "restock",
                },
            ),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1010"],
                    "update_data": {"list_price": 59.00},
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_013",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "You want to build a repeat-buyer audience for CRM by creating a segment named Repeat-30d (two or more orders in the last 30 days), "
            "then fetch similar_products on your profile to validate cross-sell signals. "
            "Once signals look healthy, you want to launch a lightweight 8% promo called Repeat-8 to that Repeat-30d cohort."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "Repeat-30d",
                    "criteria": {"min_orders": 2, "period_days": 30},
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "204", "recommendation_type": "similar_products"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "Repeat-8",
                    "target_segment": "Repeat-30d",
                    "discount_percentage": 8,
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_014",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want Adyen enabled for merchant 'MERCH_060' supporting currencies ['USD'] ahead of a pilot. "
            "Discover the product via the Computer Accessories catalog (not by name), then buy 1 'Pro Gaming Mouse' with WELCOME5 to validate checkout. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_060",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_015",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to speed up static content by standing up CloudFront in us-east-1. "
            "You also want to blunt traffic spikes by capping /checkout at 90 rpm and confirming the limit, "
            "then pull similar_products on your profile to validate post-change behavior."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 90},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "205", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_016",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want to log CX feedback — “Site search felt slow” with a three-star rating — and add 120 loyalty points to make it right. "
            "To reduce delivery issues, you want the US-Std rule in the US zone applied with tracking enabled (True). "
            "Then you’ll find 'Mechanical Keyboard' by name and buy 1 with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "207", "feedback_text": "Site search felt slow", "rating": 3},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "207", "action": "add", "points": 120},
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "207",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_017",
        instruction=(
            "You’re Jane Smith at Global Tech Inc., using 'jane.smith@globaltech.com'. "
            "You want to define a high-value audience from the last 90 days—customers with at least five orders and lifetime_spend_usd >= 1000—"
            "and save it as the segment High-Value-90d so marketing can target repeat buyers. "
            "You want to analyze your last 30d of behavior to tune messaging, then launch a 10% promo called HV-10 to that High-Value-90d cohort. "
            "To avoid stockouts during the promo, restock 'Pro Gaming Mouse' by +10 using movement_type 'restock'. "
            "Then find 'Pro Gaming Mouse' by name and buy 2 with B2BVOLUME15 to validate pricing. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "High-Value-90d",
                    "criteria": {"min_orders": 5, "period_days": 90, "lifetime_spend_usd": 1000},
                },
            ),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "202", "analysis_period": "30d"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "HV-10",
                    "target_segment": "High-Value-90d",
                    "discount_percentage": 10,
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1013",
                    "quantity_adjustment": 10,
                    "movement_type": "restock",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1013", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "B2BVOLUME15"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_018",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to record feedback — “Hub arrived fast” with a five-star rating — so CX has a clear trail. "
            "You want to adjust loyalty by adding 40 points using the adjust_points action to reward the experience. "
            "You also want to review your activity over the last 30d, then find 'USB-C Hub' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "203", "feedback_text": "Hub arrived fast", "rating": 5},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "203", "action": "adjust_points", "points": 40},
            ),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "203", "analysis_period": "30d"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_019",
        instruction=(
            "You’re Alice Johnson at Apex Logistics, using 'alice.j@email.com'. "
            "You want Braintree live for MERCH_003 so you can clear USD transactions, and you want US-Priority on the US zone with tracking enabled (True) for faster delivery. "
            "To protect returns infrastructure, you’ll cap /returns at 20 rpm and confirm the limit. "
            "Then you’ll find two items by name — 'Wireless Mouse' and 'USB-C Hub' — apply WINTER20, and complete checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Braintree",
                    "merchant_id": "MERCH_003",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "204",
                },
            ),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/returns", "rate_limit": 20}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/returns"}),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [
                        {"product_id": "1003", "quantity": 1},
                        {"product_id": "1002", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "US-Priority"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_020",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to stand up Cloudflare in us-east-1 to harden and accelerate the edge, and you want APP902 enabled with read/write and the OAuth scopes api and openid for headless flows. "
            "Before buying, you want similar_products on your profile to prime merchandising. "
            "Then you’ll browse the Computer Accessories category (not by name) and purchase one Pro Gaming Mouse with the 'WELCOME5' discount. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Cloudflare", "region": "us-east-1"},
            ),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP902",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "openid"],
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "205", "recommendation_type": "similar_products"},
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_021",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want Stripe live for MERCH_010 to process USD, and you want to cap /checkout at 80 rpm and confirm the limit so you can handle bursts safely. "
            "Then you want to find 'USB-C Hub' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_010",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 80},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_022",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want faster static delivery by standing up CloudFront in us-east-1. "
            "Then you’ll browse the Computer Accessories category, add two Wireless Mouse to the cart, apply WINTER20, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1003", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_023",
        instruction=(
            "You are Emily White at Innovate Corp., using 'emily.white@innovate.com'. "
            "Analyze your behavior for the last 30 days (analysis_period '30d'), then launch campaign 'SPRING9' (9% to 'all'). "
            "Discover the item via the Computer Accessories catalog (do not use a name lookup) and select product_id '1010' (Ergo Laptop Stand). "
            "Buy 1 with the 'WELCOME5' discount. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "203", "analysis_period": "30d"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "SPRING9",
                    "target_segment": "all",
                    "discount_percentage": 9,
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_024",
        instruction=(
            "You’re Alice Johnson at Apex Logistics, using 'alice.j@email.com'. "
            "You want a high-value audience for Q1 by creating a segment named High-Value-90d (five or more orders in the last ninety days). "
            "You also want the US-Std rule applied on the US zone with tracking enabled (True) for predictable delivery. "
            "Then you’ll find 'Pro Gaming Mouse' by name, apply B2BVOLUME15, and place the order using the next cart and order numbers. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "High-Value-90d",
                    "criteria": {"min_orders": 5, "period_days": 90},
                },
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "204",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "B2BVOLUME15"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_025",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to add 'ProMouse Co' to your supplier list using supplier_data.contact_email 'support@promouse.example' so RMAs and replenishment are formalized. "
            "You already have the product details for 'Pro Gaming Mouse' with product_id '1013' and you want to restock by +20 units to get ahead of promo traffic. "
            "Then you will purchase exactly 2 units of 'Pro Gaming Mouse' using 'WELCOME5'. "
            "When you place the order, do not pass a 'shipping_method' parameter—rely on the platform default. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {"contact_email": "support@promouse.example"},
                },
            ),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1013",
                    "quantity_adjustment": 20,
                    "movement_type": "restock",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1013", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_026",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want your dev Redis cache 'dcomm-dev-redis' ready for internal-only access by standing it up as cache.r5.large with three nodes and tightening sg-0123456789abcdef0 to a single 6379/TCP ingress from 10.0.0.0/16. "
            "Then you’ll browse the Computer Accessories category (not by name), add two Wireless Mouse, apply WINTER20, and complete checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(
                name="optimize_security_group_rules",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16",
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1003", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_027",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want your integrations to call commerce APIs without manual tokens by enabling APP900 with read and write permissions and the OAuth scopes api and refresh_token. "
            "You already have Wireless Mouse details, including product id 1003, so you’ll skip browsing and buy three units with the B2BVOLUME15 discount. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP900",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1003", "quantity": 3}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "B2BVOLUME15"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_028",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "Run a full backup to 's3' and review details. "
            "Launch a 5% promo called 'BKUP-5' to the 'all' audience. "
            "Find 'Mechanical Keyboard' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "BKUP-5",
                    "target_segment": "all",
                    "discount_percentage": 5,
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_029",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want to throttle product browsing by setting the /products endpoint to 220 rpm and improve static delivery by standing up Fastly in us-east-1. "
            "Then you want to find Wireless Mouse by name, apply the B2BVOLUME15 discount, and purchase two units. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/products", "rate_limit": 220},
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Fastly", "region": "us-east-1"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1003", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "B2BVOLUME15"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_030",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to explore attach opportunities by pulling 'bought_together' recommendations on your profile. "
            "To make checkout fast for domestic orders, you want to apply the 'US-Express' rule on the US zone with tracking enabled (True). "
            "Then you think you should find '4K Webcam' by name and purchase exactly 1 using 'WINTER20'. "
            "When you place the order, do not pass a 'shipping_method' parameter—rely on the configured rule. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "210", "recommendation_type": "bought_together"},
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Express",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "210",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_031",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want a retention audience by creating a segment named Returning-30d for customers with at least two orders in the last 30 days, then launch a 10% promotion called RET-10 to that audience. "
            "Next, you’ll browse the Computer Accessories category (not by name), add one Wireless Mouse, apply WELCOME5, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "Returning-30d",
                    "criteria": {"min_orders": 2, "period_days": 30},
                },
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "RET-10",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 10,
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_032",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want a quick retention play by creating or refreshing Returning-30d (two or more orders in the last 30 days) and launching RET-8 at 8% to that audience. "
            "You already have USB-C Hub details, including product id 1002, so you’ll skip browsing and place a one-unit order with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={
                    "segment_name": "Returning-30d",
                    "criteria": {"min_orders": 2, "period_days": 30},
                },
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "RET-8",
                    "target_segment": "Returning-30d",
                    "discount_percentage": 8,
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_033",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want to throttle search traffic by capping /search at 120 rpm and speed up static assets by standing up CloudFront in us-east-1. "
            "Then you’ll browse for one Mechanical Keyboard, apply WELCOME5, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/search", "rate_limit": 120}
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_034",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want to correct pricing on 'USB-C Hub' by first finding it by name so you avoid ID mistakes, then standardize its list price to 24.99 across channels. "
            "To validate downstream pricing, you’ll place a small QA order for one unit using the welcome discount WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1002"],
                    "update_data": {"list_price": 24.99},
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_035",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want the EU rule 'EU-Std' applied on the EU zone with tracking disabled (False) to control costs. "
            "To protect carrier-rate calls during peaks, you also want /shipping/quote capped at 45 rpm and you want to confirm the cap. "
            "Finally, you want similar_products recommendations on your profile to boost attach rate."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": False,
                    "customer_id": "203",
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/shipping/quote", "rate_limit": 45},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/shipping/quote"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "203", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_036",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to run a full backup to 's3' and review details. "
            "You think you should find '1TB NVMe SSD' by name and purchase 2 units using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1016", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_037",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "Enable Stripe for merchant 'MERCH_062' supporting currencies ['USD'] ahead of a pilot. "
            "Cap '/checkout' at 60 rpm to protect the payment flow, then identify 'Pro Gaming Mouse' by name to confirm the catalog mapping. "
            "Place a one-unit order with no discount to validate checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_062",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 60},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_038",
        instruction=(
            "You’re Alice Johnson at Apex Logistics, using 'alice.j@email.com'. "
            "You want to onboard camera supplier CamVision (sales@camvision.example) to stabilize the line. "
            "You’ll find '4K Webcam' by name, restock by 15 units to prepare for a promo, then buy one unit with WELCOME5 for QA. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "CamVision",
                    "action": "add",
                    "supplier_data": {"contact_email": "sales@camvision.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1018",
                    "quantity_adjustment": 15,
                    "movement_type": "restock",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_039",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want to reward an active user by adding 200 loyalty points to your profile. "
            "Then you should find '1TB NVMe SSD' by name and purchase exactly 1 unit using the 'WINTER20' discount. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "206", "action": "add", "points": 200},
            ),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_040",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want the '/session/refresh' endpoint capped at 400 rpm and you want to confirm the cap. "
            "After that control is in place, you want the connected app 'APP904' enabled for backend flows "
            "with permissions ['read','write'] and scopes ['api','refresh_token'], and you want the app profile verified."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/session/refresh", "rate_limit": 400},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/session/refresh"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP904",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP904"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_041",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want the US rule 'US-Std' applied on the US zone with tracking enabled (True) for predictable delivery, and you want to understand your recent activity by analyzing the last 30d. "
            "To validate the end-to-end experience, you’ll find 'Wireless Mouse' by name, apply the welcome discount WELCOME5, and complete a quick purchase. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "210",
                },
            ),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "210", "analysis_period": "30d"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_042",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want to improve West Coast performance by configuring Akamai in 'us-west-2'. "
            "Then you want to find 'USB-C Hub' by name and purchase exactly 1 unit using 'WINTER20'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Akamai", "region": "us-west-2"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_043",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want '/checkout' capped at 90 rpm and you want to confirm the cap. "
            "Then you want Adyen enabled for 'MERCH_077' (USD) to support a regional launch. "
            "Browse the Computer Accessories category (not by name) and place a one-unit order for 'Ergo Laptop Stand' with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 90},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_077",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_044",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "You want to protect availability before a campaign by reserving two units of 'Mechanical Keyboard' "
            "(decrease on-hand by -2 using movement_type 'reserve'). "
            "Then you want to buy one 'Mechanical Keyboard' with the welcome discount WELCOME5 to validate end-to-end. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1017",
                    "quantity_adjustment": -2,
                    "movement_type": "reserve",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_045",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want the EU rule 'EU-Std' applied on the EU zone with tracking enabled (True) so export deliveries are predictable. "
            "Before checkout, you will find '4K Webcam' by name. "
            "Then you will purchase exactly 1 using 'WELCOME5'. When you place the order, rely on the configured shipping rule—do not pass a 'shipping_method' parameter. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": True,
                    "customer_id": "209",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_046",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want Fastly set up in 'us-west-2' to improve West Coast latency. "
            "You also want an incremental backup to 's3' and to check its details before a catalog change. "
            "Then you want to find '1TB NVMe SSD' by name, apply WINTER20, and buy one for validation. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Fastly", "region": "us-west-2"},
            ),
            Action(
                name="process_data_backup",
                kwargs={"backup_type": "incremental", "storage_location": "s3"},
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_047",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to enable the connected app 'APP903' with permissions ['read','write'] and OAuth scopes ['api','openid']. "
            "You should cap '/catalog' at 200 rpm and confirm the cap. "
            "You think you should find 'Ergo Laptop Stand' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP903",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "openid"],
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/catalog", "rate_limit": 200},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/catalog"}),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_048",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "Configure the UAT cache 'dcomm-uat-redis' and confirm its cluster details. "
            "Then find 'USB-C Hub' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(name="get_cache_cluster_info", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_049",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to locate 'Mechanical Keyboard' by name and standardize its list price to 129.99 across channels. "
            "After updating price, you want 'similar_products' on your profile to prep an attach strategy for keyboards."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1017"],
                    "update_data": {"list_price": 129.99},
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "205", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_050",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want to onboard supplier 'CamVision' and explicitly set supplier_data.contact_email to 'sales@camvision.example' so the vendor record is complete. "
            "Then you will find '4K Webcam' by name and purchase exactly 1 unit using 'WELCOME5' as a quick validation of the new supplier flow. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "CamVision",
                    "action": "add",
                    "supplier_data": {"contact_email": "sales@camvision.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_051",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want '/offers' capped at 300 rpm and you want to confirm the limit, then launch a 7% promotion named WARMUP7 to the 'all' audience. "
            "After that, you want to find 'Wireless Mouse' by name, apply WINTER20, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/offers", "rate_limit": 300}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/offers"}),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "WARMUP7",
                    "target_segment": "all",
                    "discount_percentage": 7,
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_052",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want the US rule 'US-Priority' applied on the US zone with tracking enabled (True) for faster deliveries. "
            "You also want CloudFront set up in 'us-west-2' to improve latency. "
            "Then you find 'Pro Gaming Mouse' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "206",
                },
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-west-2"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "US-Priority"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_053",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want Braintree live for 'MERCH_060' to process USD, and you want '/payments/auth' capped at 90 rpm with confirmation. "
            "To reduce asset latency, you also want Cloudflare configured in 'us-east-1'. "
            "Then you want to find 'Ergo Laptop Stand' by name and purchase exactly 1 unit using 'WINTER20'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Braintree",
                    "merchant_id": "MERCH_060",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/payments/auth", "rate_limit": 90},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/payments/auth"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Cloudflare", "region": "us-east-1"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_054",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want the connected app 'APP904' enabled with permissions ['read','write'] and scopes ['api','openid'], and you want to verify the app profile. "
            "To control EU shipping costs, you also want the EU rule 'EU-Std' applied on the EU zone with tracking disabled (False). "
            "Before buying, you want 'similar_products' on your profile. Then browse the 'Computer Accessories' category and place a one-unit USB-C Hub order with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP904",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "openid"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP904"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": False,
                    "customer_id": "203",
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "203", "recommendation_type": "similar_products"},
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "EU-Std"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_055",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want the dev cache 'dcomm-dev-redis' configured (cache.r5.large, three nodes) and sg-0123456789abcdef0 optimized to a single 6379/TCP ingress from 10.0.0.0/16; then confirm the cluster details. "
            "To protect admin controls, cap '/cache/flush' at 10 rpm and confirm the cap. "
            "Finally, find '4K Webcam' by name, apply WELCOME5, and complete checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(
                name="optimize_security_group_rules",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "target_port": 6379,
                    "allowed_cidr": "10.0.0.0/16",
                },
            ),
            Action(name="get_cache_cluster_info", kwargs={"cluster_id": "dcomm-dev-redis"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/cache/flush", "rate_limit": 10},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/cache/flush"}),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_056",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. You want to run a full backup to 's3' and review details. "
            "You want to configure Fastly in 'us-east-1' and launch a 12% promo called 'VIP-12' to the 'all' audience. "
            "You should find 'Pro Gaming Mouse' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Fastly", "region": "us-east-1"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "VIP-12",
                    "target_segment": "all",
                    "discount_percentage": 12,
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_057",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want to locate 'Wireless Mouse' by name, standardize its list price to 34.99, and formalize 'ProMouse Co' as a supplier (support@promouse.example). "
            "To get ahead of Q4 demand, restock the mouse by +15 units and pull 'similar_products' to plan attach strategy. "
            "Then place a two-unit order with WINTER20. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1003"],
                    "update_data": {"list_price": 34.99},
                },
            ),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {"contact_email": "support@promouse.example"},
                },
            ),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1003",
                    "quantity_adjustment": 15,
                    "movement_type": "restock",
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "206", "recommendation_type": "similar_products"},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1003", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_058",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want authentication stabilized by capping '/login' at 120 rpm and '/oauth/token' at 300 rpm, and you want to confirm the '/oauth/token' cap. "
            "For predictable delivery, apply the US rule 'US-Std' on the US zone with tracking enabled (True). "
            "Then find 'USB-C Hub' by name, apply WELCOME5, and complete checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/login", "rate_limit": 120}
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/oauth/token", "rate_limit": 300},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/oauth/token"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "201",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_059",
        instruction=(
            "You’re Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want to understand recent behavior by analyzing the last '30d', then capture feedback 'Order tracking unclear' with rating 3 and add 20 loyalty points to recover the experience. "
            "To improve West Coast performance, set up CloudFront in 'us-west-2'. "
            "Then find 'Ergo Laptop Stand' by name and purchase exactly 1 unit using 'WINTER20'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "sandra.d@email.com"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "208", "analysis_period": "30d"},
            ),
            Action(
                name="process_customer_feedback",
                kwargs={
                    "contact_id": "208",
                    "feedback_text": "Order tracking unclear",
                    "rating": 3,
                },
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "208", "action": "add", "points": 20},
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-west-2"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_060",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want 'bought_together' recommendations to design a keyboard bundle, then launch a 5% all-audience promo named 'BUNDLE-5'. "
            "Finance approved Stripe for 'MERCH_055' in USD, so you enable it. "
            "Finally, you find 'Mechanical Keyboard' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "209", "recommendation_type": "bought_together"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "BUNDLE-5",
                    "target_segment": "all",
                    "discount_percentage": 5,
                },
            ),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_055",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_061",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want faster deliveries by applying the US rule 'US-Priority' on the US zone with tracking enabled (True). "
            "To stabilize supply, add 'ErgoWorks' (ops@ergoworks.example) as a supplier and restock 'Ergo Laptop Stand' by 10 units using movement_type 'restock'. "
            "Launch a simple 7% promo called 'ERG-7' to the 'all' audience. "
            "Then find 'Ergo Laptop Stand' by name and purchase exactly 1 unit using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Priority",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "213",
                },
            ),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ErgoWorks",
                    "action": "add",
                    "supplier_data": {"contact_email": "ops@ergoworks.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1010",
                    "quantity_adjustment": 10,
                    "movement_type": "restock",
                },
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "ERG-7",
                    "target_segment": "all",
                    "discount_percentage": 7,
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "US-Priority"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_062",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want the connected app 'APP905' enabled with permissions ['read','write'] and scopes ['api','refresh_token'], and you want to verify the app profile. "
            "Limit partner traffic by capping '/integrations' at 180 rpm and confirm the cap. "
            "Before a catalog refresh, run an incremental backup to 's3' and check details. "
            "Then find '1TB NVMe SSD' by name and buy exactly 1 with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP905",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP905"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/integrations", "rate_limit": 180},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/integrations"}),
            Action(
                name="process_data_backup",
                kwargs={"backup_type": "incremental", "storage_location": "s3"},
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_063",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want the US rule 'US-Std' on the US zone with tracking enabled (True) so delivery windows are predictable. "
            "You already have the product id '1002' for 'USB-C Hub', so skip browsing and place a one-unit order with the welcome code WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "201",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_064",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want '/search' capped at 150 rpm and you want to confirm the cap. "
            "You already have the product id '1018' for '4K Webcam', so place a quick one-unit order (no discount) to validate search performance under throttling. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/search", "rate_limit": 150}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/search"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_065",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want Cloudflare configured in 'us-east-1' to improve asset latency. "
            "You also want '/assets' capped at 150 rpm and confirmed so spikes don’t stress origin. "
            "Then you’ll place a one-unit validation order for 'Ergo Laptop Stand' using 'WELCOME5' (you can skip browsing; you know the product id is '1010'). Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Cloudflare", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/assets", "rate_limit": 150},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/assets"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_066",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want to formalize 'ProMouse Co' as a supplier (support@promouse.example). "
            "First find 'Wireless Mouse' by name to confirm the catalog mapping, then restock it by +5 units using movement_type 'restock' to get ahead of demand. "
            "Use the known product id '1003' to place a one-unit sanity order (no discount) to validate the inventory update. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ProMouse Co",
                    "action": "add",
                    "supplier_data": {"contact_email": "support@promouse.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="manage_inventory_levels",
                kwargs={"product_id": "1003", "quantity_adjustment": 5, "movement_type": "restock"},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_067",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want Adyen enabled for merchant 'MERCH_061' in USD ahead of a drop. "
            "Then find '1TB NVMe SSD' by name to confirm the catalog mapping and use product id '1016' to place a one-unit order with WELCOME5 as a final checkout test. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_061",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_068",
        instruction=(
            "You’re Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want '/oauth/token' capped at 300 rpm and you want to confirm the cap. "
            "Then you want the connected app 'APP906' enabled with permissions ['read','write'] and scopes ['api','refresh_token'], "
            "and you want the app profile verified. "
            "To standardize delivery estimates for EU customers, you also want the 'EU-Std' shipping rule on the EU zone "
            "with tracking enabled (True) for your profile (customer_id '208')."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "sandra.d@email.com"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/oauth/token", "rate_limit": 300},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/oauth/token"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP906",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP906"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": True,
                    "customer_id": "208",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_069",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "Before pricing changes, you want an incremental backup to 's3' and to review its details. "
            "Then use the product id '1017' for 'Mechanical Keyboard' to place a one-unit order with no discount and return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="process_data_backup",
                kwargs={"backup_type": "incremental", "storage_location": "s3"},
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_070",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want Stripe live for 'MERCH_031' to process USD, and you want 'similar_products' recommendations on your profile to plan attach offers. "
            "You also want '/payments/auth' capped at 120 rpm and confirmed so traffic spikes don’t overload auth. "
            "Then you want to buy exactly one '4K Webcam'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_031",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "210", "recommendation_type": "similar_products"},
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/payments/auth", "rate_limit": 120},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/payments/auth"}),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_071",
        instruction=(
            "You’re Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want the EU rule 'EU-Std' on the EU zone with tracking disabled (False) to manage costs. "
            "Discover the item via the Computer Accessories catalog (not by name), then buy 1 'USB-C Hub' with WELCOME5 "
            "using only the next cart and order ids. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "sandra.d@email.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": False,
                    "customer_id": "208",
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "EU-Std"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_072",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want Akamai set up in 'us-east-1' to improve static asset delivery. "
            "Cap '/assets' at 500 rpm and confirm the cap. "
            "Then review your last 30d of activity and request 'similar_products' on your profile to prep a landing-page refresh."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Akamai", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/assets", "rate_limit": 500}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/assets"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "213", "analysis_period": "30d"},
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "213", "recommendation_type": "similar_products"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v3",
        user_id="task_073",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "You want '/checkout' capped at 120 rpm so ops can manage flash-sale load, and you want to confirm the cap. "
            "Then you want to locate 'Wireless Mouse' by name and place a single-unit order with WINTER20 to validate checkout under throttling. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 120},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_074",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "You want the connected app 'APP904' enabled with permissions ['read','write'] and scopes ['api','openid'] for a partner portal, "
            "then apply the US rule 'US-Std' on the US zone with tracking enabled (True) for your profile. "
            "Buy one 'Wireless Mouse' using product_id '1003' with WELCOME5 to validate the end-to-end path. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP904",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "openid"],
                },
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "204",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_075",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "Apply the shipping rule 'US-Std' on the US zone with tracking enabled (True) for your profile. "
            "Analyze your behavior for the last 30 days (analysis_period '30d') to validate messaging, then find 'Pro Gaming Mouse' by name "
            "and complete a one-unit order with no discount to validate shipping at checkout. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "204",
                },
            ),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "204", "analysis_period": "30d"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_076",
        instruction=(
            "You are David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want to onboard 'USB Hub Works' as a supplier using supplier_data.contact_email 'hello@usbhub.example' so you can source hubs directly. "
            "Then you will find 'USB-C Hub' by name and restock the hub by +10 units using movement_type 'restock' to avoid backorder risk. "
            "Finally, you will purchase exactly 1 unit (no discount). "
            "When you place the order, do not pass a 'shipping_method' parameter—rely on the platform default. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "USB Hub Works",
                    "action": "add",
                    "supplier_data": {"contact_email": "hello@usbhub.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1002",
                    "quantity_adjustment": 10,
                    "movement_type": "restock",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_077",
        instruction=(
            "You’re John Doe at Global Tech Inc., using 'john.doe@globaltech.com'. "
            "You want CloudFront configured in 'us-east-1' to stabilize media delivery for a campaign. "
            "You also want '/checkout' capped at 80 rpm and you want to confirm the cap. "
            "Then you want to locate 'Pro Gaming Mouse' by name, apply WELCOME5, and place a one-unit order as a canary test. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/checkout", "rate_limit": 80},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/checkout"}),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_078",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want '/offers' capped at 250 rpm and you want to confirm the cap. "
            "You also want a quick 30d behavior check to validate merchandising impact before buying. "
            "You already know the product id '1016' for '1TB NVMe SSD', so place a one-unit order with WINTER20. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/offers", "rate_limit": 250}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/offers"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "203", "analysis_period": "30d"},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_079",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "Finance approved Stripe for 'MERCH_065' (USD), so you want it enabled. "
            "To improve West Coast latency, you also want Fastly configured in 'us-west-2'. "
            "Then locate '4K Webcam' by name, apply WELCOME5, and place a one-unit order to validate performance. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_065",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Fastly", "region": "us-west-2"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_080",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want the connected app 'APP908' enabled for server-to-server flows with permissions ['read','write'] and scopes ['api','refresh_token']. "
            "To standardize delivery times, you want the EU rule 'EU-Std' applied on the EU zone with tracking enabled (True) for your profile. "
            "Then locate 'Wireless Mouse' by name, apply WELCOME5, and place a one-unit order. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP908",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "EU-Std",
                    "shipping_zone": "EU",
                    "tracking_enabled": True,
                    "customer_id": "210",
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706", "shipping_method": "EU-Std"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_081",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to record CX feedback — “Packaging was dented” with a 2-star rating — and add fifty loyalty points to recover the experience. "
            "To sanity-check merchandising before you buy, you want similar_products on your profile. "
            "Then you will find 'USB-C Hub' by name and purchase exactly 1 unit. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "207", "feedback_text": "Packaging was dented", "rating": 2},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "207", "action": "add", "points": 50},
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "207", "recommendation_type": "similar_products"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_082",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want the UAT cache 'dcomm-uat-redis' configured as a single node on node_type 'cache.r5.large'. "
            "Then you want to find 'Ergo Laptop Stand' by name and purchase exactly 1 unit using 'WELCOME5'. "
            "When you place the order, do not pass a 'shipping_method' parameter—rely on the platform default. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 1},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_083",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want Cloudflare configured in 'us-east-1' to improve static delivery and you want to surface similar_products for cross-sell. "
            "Then buy one 'Pro Gaming Mouse' using product_id '1013' with WELCOME5 to validate performance. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Cloudflare", "region": "us-east-1"},
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "213", "recommendation_type": "similar_products"},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_084",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "Standardize pricing for '4K Webcam' using product id 1018 by setting list price to 119.00 via a bulk update, then locate it by name to confirm the mapping. "
            "Buy 1 '4K Webcam' with WELCOME5 to validate availability and pricing. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1018"],
                    "update_data": {"list_price": 119.00},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_085",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to capture feedback 'Keys feel mushy' with rating 3 and add 30 loyalty points to recover the experience. "
            "Then locate 'Mechanical Keyboard' by name and place a one-unit order without a discount to validate the journey. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "203", "feedback_text": "Keys feel mushy", "rating": 3},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "203", "action": "add", "points": 30},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_086",
        instruction=(
            "You’re Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "Cap '/products' at 150 rpm to protect the catalog service, then buy one 'USB-C Hub' using product_id '1002' "
            "with no discount to validate browse-to-buy. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/products", "rate_limit": 150},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "210",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_087",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want the '4K Webcam' list price standardized to 119.00 using product_id '1018', and you want '/media' capped at 500 rpm with confirmation. "
            "Then buy one '4K Webcam' with WELCOME5 to validate the flow. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1018"],
                    "update_data": {"list_price": 119.0},
                },
            ),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/media", "rate_limit": 500}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/media"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_088",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want Akamai configured in 'us-west-2' and supplier 'ErgoWorks' (ops@ergoworks.example) added to stabilize lead times. "
            "Locate 'Ergo Laptop Stand' by name, then restock by +8 units using movement_type 'restock'. "
            "Buy one with WINTER20 to validate inventory sync. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Akamai", "region": "us-west-2"},
            ),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "ErgoWorks",
                    "action": "add",
                    "supplier_data": {"contact_email": "ops@ergoworks.example"},
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="manage_inventory_levels",
                kwargs={"product_id": "1010", "quantity_adjustment": 8, "movement_type": "restock"},
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1010", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_089",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want the UAT cache 'dcomm-uat-redis' set up with a single node and details confirmed. "
            "Then locate '1TB NVMe SSD' by name and place a one-unit order using WELCOME5 to validate performance. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 1},
                },
            ),
            Action(name="get_cache_cluster_info", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_090",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "Analyze your behavior for the last 30 days (analysis_period '30d') to tune messaging, then launch a 7% promo called 'ENGAGE-7' targeting 'all'. "
            "Identify 'Wireless Mouse' by name to confirm the catalog mapping, then buy 1 with WELCOME5 to validate conversion. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "203", "analysis_period": "30d"},
            ),
            Action(
                name="generate_promotional_campaign",
                kwargs={
                    "campaign_name": "ENGAGE-7",
                    "target_segment": "all",
                    "discount_percentage": 7,
                },
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_091",
        instruction=(
            "You’re Mike Rivera at Apex Logistics, using 'm.rivera@apexlogistics.com'. "
            "You want Adyen enabled for 'MERCH_070' (USD) and you want 'bought_together' recommendations to plan a bundle. "
            "Then locate 'Wireless Mouse' by name and place a one-unit order with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Adyen",
                    "merchant_id": "MERCH_070",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "209", "recommendation_type": "bought_together"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "209",
                    "items": [{"product_id": "1003", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_092",
        instruction=(
            "You’re Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "Configure CloudFront in 'us-east-1' for static delivery and cap '/media' at 450 rpm. "
            "Then find '4K Webcam' by name and buy one with WELCOME5 to validate performance. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "sandra.d@email.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "CloudFront", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/media", "rate_limit": 450}
            ),
            Action(name="find_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "208",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_093",
        instruction=(
            "You’re Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "Before a promo change, you want a full backup to 's3' and details reviewed, plus a 30d behavior snapshot on your profile. "
            "Then browse 'Computer Accessories' and buy one 'Pro Gaming Mouse' with WINTER20 as a smoke test. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(
                name="process_data_backup", kwargs={"backup_type": "full", "storage_location": "s3"}
            ),
            Action(name="get_data_backup_info", kwargs={}),
            Action(
                name="analyze_customer_behavior",
                kwargs={"contact_id": "213", "analysis_period": "30d"},
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "213",
                    "items": [{"product_id": "1013", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WINTER20"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_094",
        instruction=(
            "You’re John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want supplier 'CamVision' added (sales@camvision.example) and the '4K Webcam' price standardized to 115.00 "
            "using product_id '1018' so pricing is consistent across channels. "
            "Then place a one-unit order for '4K Webcam' with WELCOME5 to confirm the price in cart. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "john.doe@globaltech.com"}),
            Action(
                name="manage_supplier_relationships",
                kwargs={
                    "supplier_name": "CamVision",
                    "action": "add",
                    "supplier_data": {"contact_email": "sales@camvision.example"},
                },
            ),
            Action(
                name="process_bulk_product_update",
                kwargs={
                    "update_type": "price",
                    "product_ids": ["1018"],
                    "update_data": {"list_price": 115.0},
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "201",
                    "items": [{"product_id": "1018", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_095",
        instruction=(
            "You’re Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want a VIP cohort—create segment 'VIP' for lifetime_spend_usd >= 1000. "
            "Locate 'Pro Gaming Mouse' by name, then restock by +10 units to prepare a targeted drop. "
            "Buy two 'Pro Gaming Mouse' with B2BVOLUME15 to validate pricing. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(
                name="manage_customer_segments",
                kwargs={"segment_name": "VIP", "criteria": {"lifetime_spend_usd": 1000}},
            ),
            Action(name="find_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="manage_inventory_levels",
                kwargs={
                    "product_id": "1013",
                    "quantity_adjustment": 10,
                    "movement_type": "restock",
                },
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "202",
                    "items": [{"product_id": "1013", "quantity": 2}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "B2BVOLUME15"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_096",
        instruction=(
            "You’re Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to improve offer-page latency by configuring Fastly in 'us-east-1' and capping '/offers' at 200 rpm, with a confirmation that the limit is active. "
            "Then you browse 'Computer Accessories' and purchase exactly 1 unit of product id '1017' (Mechanical Keyboard) with no discount. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "emily.white@innovate.com"}),
            Action(
                name="configure_content_delivery_network",
                kwargs={"cdn_provider": "Fastly", "region": "us-east-1"},
            ),
            Action(
                name="manage_api_rate_limits", kwargs={"api_endpoint": "/offers", "rate_limit": 200}
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/offers"}),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "203",
                    "items": [{"product_id": "1017", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_097",
        instruction=(
            "You’re Alice Johnson, using 'alice.j@email.com'. "
            "You want the connected app 'APP912' enabled with permissions ['read','write'] and scopes ['api','openid'], and you want to verify the app profile. "
            "Request 'similar_products' on your profile for cross-sell planning, then locate 'USB-C Hub' by name and place a one-unit order with WELCOME5. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "alice.j@email.com"}),
            Action(
                name="manage_connected_app_security",
                kwargs={
                    "app_id": "APP912",
                    "permissions": ["read", "write"],
                    "oauth_scopes": ["api", "openid"],
                },
            ),
            Action(name="get_connected_app_security", kwargs={"app_id": "APP912"}),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "204", "recommendation_type": "similar_products"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "204",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_098",
        instruction=(
            "You’re Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want 'dcomm-dev-redis' configured (three nodes) and '/cache/mget' capped at 120 rpm with confirmation to protect internal APIs. "
            "Then browse 'Computer Accessories' and buy one 'USB-C Hub' with WELCOME5 as a final smoke test. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "bob.w@email.com"}),
            Action(
                name="configure_cache_integration",
                kwargs={
                    "cluster_id": "dcomm-dev-redis",
                    "elasticache_config": {"node_type": "cache.r5.large", "num_cache_nodes": 3},
                },
            ),
            Action(
                name="manage_api_rate_limits",
                kwargs={"api_endpoint": "/cache/mget", "rate_limit": 120},
            ),
            Action(name="get_api_rate_limit_config", kwargs={"api_endpoint": "/cache/mget"}),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "205",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_099",
        instruction=(
            "You’re David Chen at Quantum Co., using 'david.chen@quantum.co'. "
            "You want Stripe enabled for 'MERCH_075' (USD) and 'similar_products' on your profile for attach insights. "
            "Then locate '1TB NVMe SSD' by name and place a one-unit order without a discount to confirm baseline pricing. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "david.chen@quantum.co"}),
            Action(
                name="configure_payment_gateway",
                kwargs={
                    "gateway_name": "Stripe",
                    "merchant_id": "MERCH_075",
                    "supported_currencies": ["USD"],
                },
            ),
            Action(
                name="manage_product_recommendations",
                kwargs={"contact_id": "206", "recommendation_type": "similar_products"},
            ),
            Action(name="find_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "206",
                    "items": [{"product_id": "1016", "quantity": 1}],
                },
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v3",
        user_id="task_100",
        instruction=(
            "You’re Maria Garcia, using 'maria.g@email.com'. "
            "You want to capture feedback 'Support was helpful' with rating 5 and add 30 loyalty points. "
            "You want the US rule 'US-Std' applied on the US zone with tracking enabled (True) for your profile. "
            "Then you browse the Computer Accessories category and purchase exactly 1 unit of product id '1002' (USB-C Hub) using 'WELCOME5'. Return the order id."
        ),
        actions=[
            Action(name="get_customer_profile", kwargs={"email": "maria.g@email.com"}),
            Action(
                name="process_customer_feedback",
                kwargs={"contact_id": "207", "feedback_text": "Support was helpful", "rating": 5},
            ),
            Action(
                name="process_loyalty_program",
                kwargs={"contact_id": "207", "action": "add", "points": 30},
            ),
            Action(
                name="configure_shipping_rules",
                kwargs={
                    "rule_name": "US-Std",
                    "shipping_zone": "US",
                    "tracking_enabled": True,
                    "customer_id": "207",
                },
            ),
            Action(
                name="search_products_by_category", kwargs={"category_name": "Computer Accessories"}
            ),
            Action(name="get_next_cart_id", kwargs={}),
            Action(
                name="create_shopping_cart",
                kwargs={
                    "cart_id": "706",
                    "contact_id": "207",
                    "items": [{"product_id": "1002", "quantity": 1}],
                },
            ),
            Action(
                name="apply_discount_bundle", kwargs={"cart_id": "706", "offer_code": "WELCOME5"}
            ),
            Action(name="get_next_order_id", kwargs={}),
            Action(
                name="process_order_with_fulfillment", kwargs={"order_id": "9017", "cart_id": "706"}
            ),
        ],
        outputs=["9017"],
    ),
]
