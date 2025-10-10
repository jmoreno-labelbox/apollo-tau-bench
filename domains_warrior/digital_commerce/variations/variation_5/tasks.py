from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="v5",
        user_id="task_001",
        instruction=(
            "You are Alice Johnson (alice.j@email.com).You want to complete a two-unit purchase "
            "of a Wireless Mouse from CAT103."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1003", "new_quantity": 2}
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_002",
        instruction="You are Bob Williams (bob.w@email.com). You want to buy a Wireless Mouse and Branded Hoodie (M) "
        "which you realize you really like the hoodie so you end up getting 2. ",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 2},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_003",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want your order to contain 1 Ergo Laptop Stand and 1 4K Webcam from CAT103."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_004",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to shop and build a quick order. "
            "You select two USB-C Hub and add to the cart. You then decide to also buy one Wireless Mouse. "
            "You preview totals, then place the order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={"contact_id": "204", "created_at": "2025-08-06T12:00:00Z"},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={"cart_id": "706", "created_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_005",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to buy a ProBook X15. When "
            "you create the cart you want to review it before adding any items to make sure you hadnt left anything in it. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_006",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to complete a purchase of a USB-C Hub."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_007",
        instruction=(
            "You are Priya Shah from Cloud Engineering. You want to use the UAT cache subnet group esg-uat-1 to stand up a temporary "
            "Redis cache with cluster_id ec-lab-01 (engine redis, node_type cache.t3.small, endpoint ec-lab-01.cache.local, port 6379) "
            "on the cache security group sg-cache. You move the cluster status through Modifying and then to Available, verify its details, "
            "and then add a security-group rule with direction ingress, protocol tcp, cidr 10.2.0.0/16, port 6379, description Temporary allow "
            "for verification. Finally, you list the security-group rules for audit."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-lab-01",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-uat-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-lab-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-lab-01",
                    "status": "Modifying",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-lab-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-lab-01"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 6379,
                    "cidr": "10.2.0.0/16",
                    "description": "Temporary allow for verification",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_008",
        instruction="You are Sandra Sands (sandra.sands@email.com). You want to buy a USB-C Hub.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.sands@email.com"}),
            Action(
                name="create_account",
                kwargs={
                    "email": "sandra.sands@email.com",
                    "first_name": "Sandra",
                    "last_name": "Sands",
                },
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "114"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "216",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_009",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to use your WINTER20 promotion, "
            "add a USB-C Hub and a 4K Webcam, review the totals, and place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_010",
        instruction=(
            "You are Mike Rivera from SRE. Using the production cache subnet group, you want a maintenance Redis cache "
            "ec-maint-01 (engine redis, node cache.t3.micro, endpoint ec-maint-01.cache.local, tcp port 6379) on the cache "
            "security group sg-cache brought online with auth tokens disabled and encryption (in transit and at rest) disabled. "
            "You want to verify the changes to the cluster details after it’s marked Available and confirm the active rules are implemented. "
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-maint-01",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-maint-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-maint-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-maint-01"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_011",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to put a Wireless Mouse in your cart."
            "You then want to add a Branded Hoodie (M) and place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_012",
        instruction=(
            "You are Alex Nguyen from Cloud Engineering. Using the production cache subnet group, you want a small Redis cache "
            "ec-lite-01 tcp (engine redis, node cache.t3.small, endpoint ec-lite-01.cache.local, port 6379) on security group "
            "sg-cache brought online and its details confirmed. You should allow a short-lived HTTPS egress on  0.0.0.0/0 443 described exactly as "
            "Temporary HTTPS egress for audit. You then confirm the rule set."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-lite-01",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-lite-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "egress",
                    "protocol": "tcp",
                    "port": 443,
                    "cidr": "0.0.0.0/0",
                    "description": "Temporary HTTPS egress for audit",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_013",
        instruction=("You are Kevin Lee (kevin.lee@starlight.net). You want to buy a ProBook X15."),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_014",
        instruction="You are Mike Rivera (m.rivera@apexlogistics.com). You want to apply the WINTER20 offer and add a Wireless Mouse and a USB-C Hub to "
        "your cart.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_015",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to browse category CAT103 to pick a 4K Webcam, "
            "review the totals, add a Wireless Mouse then place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_016",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to pick a Pro Gaming Mouse from CAT103 but you "
            "are a new employee at Quantum Solutions are will be using B2B pricing and this has been verified."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_017",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to apply the coupon B2BVOLUME15 and buy 2 "
            "ProBook X15."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_offer_by_code", kwargs={"code": "B2BVOLUME15"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "B2BVOLUME15"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_018",
        instruction="You are Mike Rivera (m.rivera@apexlogistics.com). You want to switch to the B2B Wholesale "
        "pricebook and buy a Wireless Mouse.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_019",
        instruction="You are Maria Garcia (maria.g@email.com). You want to apply WINTER20 and buy a USB-C Hub.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_020",
        instruction="You are Bob Builder (bob.builder@email.com). You want to buy a Pro Gaming Mouse. "
        ". ",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.builder@email.com"}),
            Action(
                name="create_account",
                kwargs={
                    "email": "bob.builder@email.com",
                    "first_name": "Bob",
                    "last_name": "Builder",
                },
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "114"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "216",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_021",
        instruction=(
            "You are Taylor Reed from Security. On the cache security group sg-cache, you document controlled connectivity "
            "in a fixed sequence: first add an ingress rule for Redis on 6379/tcp from cidr 10.140.0.0/16 described Redis allow; "
            "next add an egress rule for HTTPS on 443/tcp to cidr 0.0.0.0/0 described HTTPS egress; "
            "then add an ingress rule for metrics on 9121/TCP from cidr 10.140.0.0/16 described Metrics scrapers. "
            "You capture a rule listing before any changes and again after each addition to show the progression."
        ),
        actions=[
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 6379,
                    "cidr": "10.140.0.0/16",
                    "description": "Redis allow",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "egress",
                    "protocol": "tcp",
                    "port": 443,
                    "cidr": "0.0.0.0/0",
                    "description": "HTTPS egress",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 9121,
                    "cidr": "10.140.0.0/16",
                    "description": "Metrics scrapers",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_022",
        instruction=(
            "Using sandra.d@email.com, you want to order 1 Ergo Laptop Stand but first preview the Stand in the cart before continuing. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_023",
        instruction=(
            "You are Maria Flower (maria.flower@email.com). You want to lookup a Branded Hoodie (M) "
            "and a Wireless Mouse and add the mouse to the cart. You want to know what the new cart total is."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.flower@email.com"}),
            Action(
                name="create_account",
                kwargs={
                    "email": "maria.flower@email.com",
                    "first_name": "Maria",
                    "last_name": "Flower",
                },
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "114"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "216",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
        ],
        outputs=["35"],
    ),
    Task(
        annotator="v5",
        user_id="task_024",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to purchase a Wireless Mouse "
            "from CAT103 using the WINTER20 promotion."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_025",
        instruction=(
            "You are Alex Nguyen from Cloud Engineering. Using the production cache subnet group, you want a small Redis cache "
            "ec-lite-02 tcp (engine redis, node cache.t3.small, endpoint ec-lite-02.cache.local, port 6379) on the cache "
            "security group sg-cache brought to Available and its details confirmed. Then allow HTTPS egress on 443 with the "
            "description exactly Temporary HTTPS egress for audit and confirm the rules."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-lite-02",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-lite-02.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-lite-02"}),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-lite-02",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-lite-02"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "egress",
                    "protocol": "tcp",
                    "port": 443,
                    "cidr": "0.0.0.0/0",
                    "description": "Temporary HTTPS egress for audit",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_026",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to use the WINTER20 promotion to "
            "complete a purchase of a USB-C Hub and a Wireless Mouse."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_027",
        instruction=(
            "You are reviewing a Pro Gaming Mouse and a USB-C Hub. You decide you want to buy "
            "them as Bob Williams (bob.w@email.com)."
        ),
        actions=[
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_028",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to purchase an Ergo Laptop Stand. After that is done you add 1 Stand to a new cart. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1010", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_029",
        instruction=(
            "You are Bob Williams (bob.w@email.com). In UAT you register a cache subnet group sgp-audit-01 named cache-audit in VPC vpc-001 "
            "over subnets [subnet-a7,subnet-b7] with the description Audit cache subnets. You then provision a Redis cache with cluster_id "
            "ec-audit-01 on security group sg-cache and subnet group sgp-audit-1, using engine redis, node_type cache.t3.micro, num_nodes 1, "
            "endpoint ec-audit-01.cache.local, and port 6379. You set auth_token_enabled, transit_encryption_enabled, and at_rest_encryption_enabled disabled. "
            "You mark the cluster Available and confirm its details. To validate pricing reads cleanly "
            "after the change, you use her normal account pricing, create a cart, preview totals, and stop before checkout. Finally, you list "
            "ElastiCache clusters to confirm ec-audit-01 appears in inventory."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="create_subnet_group",
                kwargs={
                    "subnet_group_id": "sgp-audit-01",
                    "name": "cache-audit",
                    "description": "Audit cache subnets",
                    "subnet_ids": ["subnet-a7", "subnet-b7"],
                    "vpc_id": "vpc-001",
                },
            ),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "sgp-audit-01"}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-audit-01",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "sgp-audit-01",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-audit-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-audit-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-audit-01"}),
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(
                name="create_cart",
                kwargs={"contact_id": "205", "created_at": "2025-08-06T12:00:00Z"},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="list_elasticache_clusters", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_030",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to buy a USB-C Hub and a Wireless Mouse, "
            "read back the items on the order, and then return the mouse because you Changed mind."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1003", "qty": 1}],
                    "reason": "Changed mind",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_031",
        instruction=(
            "Using alice.j@email.com, you want to buy 1 USB-C Hub, then file and resolve a support case titled "
            "Package never arrived."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "204",
                    "subject": "Package never arrived",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_032",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want your order to include a 4K Webcam "
            "from CAT103 and exclude the USB-C Hub."
        ),
        actions=[
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="remove_item_from_cart", kwargs={"cart_id": "706", "product_id": "1002"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_033",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to purchase two Pro Gaming Mouse "
            "units using the B2BVOLUME15 promotion."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_offer_by_code", kwargs={"code": "B2BVOLUME15"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1013", "new_quantity": 2}
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "B2BVOLUME15"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_034",
        instruction=(
            "You want to purchase a USB-C Hub from CAT103 using Sandra Dee (sandra.d@email.com)."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_035",
        instruction=(
            "Using kevin.lee@starlight.net, you want to purchase 1 Wireless Mouse and 1 Branded Hoodie (M) "
            "then return exactly 1 Unwanted Wireless Mouse and have the refund reflect what was actually paid."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1003", "qty": 1}],
                    "reason": "Unwanted",
                },
            ),
            Action(
                name="refund_order_partial",
                kwargs={"order_id": "9017", "amount": 32.0, "reason": "Unwanted"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_036",
        instruction=(
            "You are Ruth Rivera (ruth.rivera@apexlogistics.com). You want to purchase a USB-C Hub  and have a support case "
            "titled Gift receipt needed that is associated to the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "ruth.rivera@apexlogistics.com"}),
            Action(
                name="create_account",
                kwargs={
                    "email": "ruth.rivera@apexlogistics.com",
                    "first_name": "Ruth",
                    "last_name": "Rivera",
                },
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "114"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "216",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "216",
                    "subject": "Gift receipt needed",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_037",
        instruction=(
            "You are a Cloud Engineer. Using the production cache subnet group, you want a cache.t3.small Redis cache brought online with endpoint ec-scale-02.cache.local for this task’s "
            "cluster, with auth tokens False. You want to update the config to cache.t3.medium for 2 nodes and its details and after it becomes Available."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-scale-02",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-scale-02.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_config",
                kwargs={
                    "cluster_id": "ec-scale-02",
                    "node_type": "cache.t3.medium",
                    "num_nodes": 2,
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-scale-02",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-scale-02"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_038",
        instruction=(
            "You are a Cloud Engineer. You want to provision a Redis cache with cluster_id ec-throw-03 "
            "in the production cache subnet group esg-prod-1 using the cache security group sg-cache. "
            "You set engine=redis, node_type=cache.t3.micro, num_nodes=1, port=6379, and endpoint ec-throw-03.cache.local. "
            "You set auth_token_enabled=False, transit_encryption_enabled=False, and at_rest_encryption_enabled=False. "
            "You bring the cluster to status Available, confirm its details and verify its shown in all clusters. "
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-throw-03",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-throw-03.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-throw-03",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-throw-03"}),
            Action(name="list_elasticache_clusters", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_039",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You order a Pro Gaming Mouse. You realize after "
            "finalizing the order it's not the color you wanted and you need to create a support case titled 'Wrong color'."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "204",
                    "subject": "Wrong color",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_040",
        instruction=(
            "You want to compare retail and wholesale (pb 2) totals as Maria Garcia (maria.g@email.com) "
            "and proceed with whichever yields a lower total when buying a USB-C Hub; if equal, keep your original pricing."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_041",
        instruction=(
            "Using m.rivera@apexlogistics.com, you want to purchase 1 1TB NVMe SSD then set the "
            "shipping address exactly to Mike Rivera, 900 Industrial Way, Dallas, TX 75001, US and cancel the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Mike Rivera",
                        "line1": "900 Industrial Way",
                        "city": "Dallas",
                        "region": "TX",
                        "postal_code": "75001",
                        "country": "US",
                    },
                },
            ),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_042",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to purchase two units of the "
            "1TB NVMe SSD but right after submitting you realize they are the Wrong capacity. You decide to return 1 "
            "and keep the second one."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 2},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1016", "qty": 1}],
                    "reason": "Wrong capacity",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_043",
        instruction="You are Alice Johnson (alice.j@email.com). Buy 4K Webcam, After you order "
        "you wrote a complaint about Webcam saying 'Defective lens'. You want to return the item and resolve the created case.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "204",
                    "subject": "Defective lens",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1018", "qty": 1}],
                    "reason": "Defective",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_044",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to add a USB-C Hub to your cart. "
            "You then want to preview the cart to see the price, add a second one and place the order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_045",
        instruction=(
            "Using bob.w@email.com, you want to purchase 1 Branded Hoodie (M) and 1 Wireless Mouse, "
            "read back the items on the order, and then cancel it."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_046",
        instruction="You are Maria Garcia (maria.g@email.com). Buy Branded Hoodie (M), open case labeled Packaging damaged, "
        "move it to In Progress, then resolve it.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "207",
                    "subject": "Packaging damaged",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "In Progress"}),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_047",
        instruction=(
            "You are Priya Shah from Cloud Engineering. From the environment’s list of subnet groups, use the UAT group esg-uat-1 to "
            "stand up a temporary Redis cache.t3.small  ec-lab-02 (endpoint ec-lab-02.cache.local, port 6379) on sg-cache, move it through "
            "Modifying to Available, and verify the details."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-lab-02",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-uat-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-lab-02.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-lab-02",
                    "status": "Modifying",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-lab-02",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-lab-02"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_048",
        instruction=(
            "You are Daniel Kim from Platform Ops. You want to list subnet groups and register the subnet group sgp-green-01 named cache-green in VPC vpc-001 over "
            "subnets [subnet-g1,subnet-g2] with the description exactly Green cache subnets and verify it. Then provision a Redis "
            "cache ec-green-01 (endpoint ec-green-01.cache.local, port 6379) on sg-cache with auth tokens False and encryption "
            "disabled (in transit and at rest), bring it to Available, and confirm the details."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="create_subnet_group",
                kwargs={
                    "subnet_group_id": "sgp-green-01",
                    "name": "cache-green",
                    "description": "Green cache subnets",
                    "subnet_ids": ["subnet-g1", "subnet-g2"],
                    "vpc_id": "vpc-001",
                },
            ),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "sgp-green-01"}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-green-01",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "sgp-green-01",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-green-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-green-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-green-01"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_049",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). In UAT you need to restore pricing cache headroom by scaling the shared Redis "
            "cluster dcomm-uat-redis to node_type cache.t3.medium with num_nodes 2, recording the change at 2025-08-06T12:00:00Z and "
            "verifying the status moves through Modifying to Available. To confirm pricing reads cleanly after the change, you test by "
            "adding one USB-C Hub to a cart, preview totals, and stop before checkout."
        ),
        actions=[
            Action(name="list_elasticache_clusters", kwargs={}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="update_elasticache_cluster_config",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "node_type": "cache.t3.medium",
                    "num_nodes": 2,
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "status": "Modifying",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={"contact_id": "210", "created_at": "2025-08-06T12:00:00Z"},
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_050",
        instruction="You are Bob Williams (bob.w@email.com). "
        "Purchase a 4K Webcam, list the items on the order, then return the webcam with reason Not needed "
        "and show the refund amount.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1018", "qty": 1}],
                    "reason": "Not needed",
                },
            ),
            Action(name="refund_order_full", kwargs={"order_id": "9017", "reason": "Not needed"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_051",
        instruction=(
            "You want to buy Branded Hoodie (M) as Alice Johnson (alice.j@email.com) "
            "and open a support case titled Wrong size, resolving it after creation."
        ),
        actions=[
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "204",
                    "subject": "Wrong size",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_052",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com) from Commerce Platform. You list cache subnet groups and register sgp-mini-01 named cache-mini in VPC vpc-001 "
            "over subnets [subnet-m1,subnet-m2] with the description Mini cache group, then verify it. You provision a Redis cache with "
            "cluster_id ec-mini-01 on security group sg-cache and subnet group sgp-mini-01 using engine redis, node_type cache.t3.micro, "
            "num_nodes 1, endpoint ec-mini-01.cache.local. You set auth_token_enabled, transit_encryption_enabled, "
            "and at_rest_encryption_enabled disabled, set the cluster as Available, and read it back. To validate pricing reads after the "
            "change. You want to test by adding one USB-C Hub to a cart and preview totals."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="create_subnet_group",
                kwargs={
                    "subnet_group_id": "sgp-mini-01",
                    "name": "cache-mini",
                    "description": "Mini cache group",
                    "subnet_ids": ["subnet-m1", "subnet-m2"],
                    "vpc_id": "vpc-001",
                },
            ),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "sgp-mini-01"}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-mini-01",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "sgp-mini-01",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-mini-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-mini-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-mini-01"}),
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={"contact_id": "208", "created_at": "2025-08-06T12:00:00Z"},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_053",
        instruction="You are Maria Garcia (maria.g@email.com) and you want to buy 1TB NVMe SSD "
        "after adding to the cart you decide you would like to get a total of 2 and complete the order.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1016", "new_quantity": 2}
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_054",
        instruction="You are Sandra Dee (sandra.d@email.com). Buy two Branded Hoodie (M), preview cart before creating the order, "
        "and then you browse the Computer Accessories Catalog CAT103.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 2},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_055",
        instruction="You are Bob Williams (bob.w@email.com). Buy ProBook X15, list the items, then cancel the order.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_056",
        instruction="You are Mike Rivera (m.rivera@apexlogistics.com). "
        "Buy a USB-C Hub, then issue a $5.0 partial refund with reason Goodwill.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="refund_order_partial",
                kwargs={"order_id": "9017", "amount": 5.0, "reason": "Goodwill"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_057",
        instruction="You are Maria Garcia (maria.g@email.com) and you want to buy a Wireless Mouse Before you purchase you browse the rest of the Computer Accessories "
        "category. You find a USB-C Hub add to cart and then finalize the order. ",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_058",
        instruction="You are Alice Johnson (alice.j@email.com). "
        "You buy a Pro Gaming Mouse, then set the shipping address exactly to: "
        "name Alice Johnson, line1 123 Maple St, city Nashville, region TN, postal_code 37209, country US.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Alice Johnson",
                        "line1": "123 Maple St",
                        "city": "Nashville",
                        "region": "TN",
                        "postal_code": "37209",
                        "country": "US",
                    },
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_059",
        instruction=(
            "You want to buy a USB-C Hub as Kevin Lee (kevin.lee@starlight.net), "
            "list the items on the order, then return the hub for Changed mind."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1002", "qty": 1}],
                    "reason": "Changed mind",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_060",
        instruction="You are Sandra Dee (sandra.d@email.com). You want to add a 1TB NVMe SSD to a cart and then buy. "
        "After purchase, you realized you wanted two, add another to the cart and complete a second order.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "707",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_061",
        instruction="You are Alice Johnson (alice.j@email.com). Buy Pro Gaming Mouse, preview totals, then cancel the order.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_062",
        instruction="You are Levin Lee (kevin.lee@starlight.net. Buy Ergo Laptop Stand. After you buy it you realize "
        "that it was not needed and you want to return it as Not needed.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1010", "qty": 1}],
                    "reason": "Not needed",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_063",
        instruction="You are Alice Johnson (alice.j@email.com) and you would like to get a discount for a Wireless Mouse because you think its too expensive. "
        "You want to stop once the item is in the cart and create a case called Charge discrepancy under order 9004. ",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9004",
                    "contact_id": "204",
                    "subject": "Charge discrepancy",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_064",
        instruction=(
            "You are Casey Brooks from Data Engineering. Using the production cache subnet group, you bring ec-analytics-03 online on "
            "sg-cache as a Redis cache (node type cache.t4g.small) with auth tokens False and encryption enabled in transit and "
            "at rest. You want to set it to Available and confirm details. Then grant metrics access on tcp/9121 from 10.10.0.0/16 with the "
            "description exactly Metrics scrapers and show the before and after resulting rules."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-analytics-03",
                    "engine": "redis",
                    "node_type": "cache.t4g.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-analytics-03.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-analytics-03",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 9121,
                    "cidr": "10.10.0.0/16",
                    "description": "Metrics scrapers",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_065",
        instruction="You are Kevin Lee (kevin.lee@starlight.net). You want to put 1TB NVMe SSD in your cart, apply WINTER20 and buy it.",
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_066",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to buy two Wireless Mouse, then set the shipping "
            "address exactly to: name Maria Garcia, line1 77 Pine St, city Austin, region TX, postal_code 73301, "
            "country US. After that, you want to return one Wireless Mouse with reason Changed mind."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1003", "new_quantity": 2}
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Maria Garcia",
                        "line1": "77 Pine St",
                        "city": "Austin",
                        "region": "TX",
                        "postal_code": "73301",
                        "country": "US",
                    },
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1003", "qty": 1}],
                    "reason": "Changed mind",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_067",
        instruction=(
            "You are Jordan Lee from SRE. From the environment’s list of subnet groups, use the UAT group esg-uat-1 to bring up a small "
            "Redis cache ec-mod-01 (endpoint ec-mod-01.cache.local, port 6379) on sg-cache with auth tokens False and encryption "
            "disabled (in transit and at rest). Move it  to Available and verify the details."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-mod-01",
                    "engine": "redis",
                    "node_type": "cache.t3.micro",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-uat-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": False,
                    "transit_encryption_enabled": False,
                    "at_rest_encryption_enabled": False,
                    "endpoint": "ec-mod-01.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-mod-01",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-mod-01"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_068",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to add a USB-C Hub "
            "then place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_069",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to cancel your existing order 9015. You  then want "
            "to buy a 1TB NVMe SSD, read back the items on the new order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="list_order_items", kwargs={"order_id": "9015"}),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9015", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_070",
        instruction=(
            "You are Mike Rivera (m.rivera@apexlogistics.com). You want to buy a USB-C Hub and a 4K Webcam, "
            "preview totals, then place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_071",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to buy a USB-C Hub. After ordering you want to browse other items in the same category "
            "and add one Wireless Mouse, Ergo Laptop Stand, and Pro Gaming Mouse into a cart for future review."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1010", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1013", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_072",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to cart a Wireless Mouse and 1TB NVMe SSD but do not "
            "complete the order until you get the go ahead from management."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_073",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to purchase a 4K Webcam, 3 USB-C Hubs and 5 1TB NVMe SSD. Because of your big purchase"
            "you are offered WINTER20 which is automatically applied after your items were entered. You complete the purchase then set the shipping "
            "address exactly to: name Bob Williams, line1 9 Elm Rd, city Denver, region CO, postal_code 80202, "
            "country US."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 3},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 5},
            ),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Bob Williams",
                        "line1": "9 Elm Rd",
                        "city": "Denver",
                        "region": "CO",
                        "postal_code": "80202",
                        "country": "US",
                    },
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_074",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to buy a USB-C Hub, preview the cart and add a Wireless Mouse and complete the order.  "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_075",
        instruction=(
            "Using alice.j@email.com, you want to purchase 1 Branded Hoodie (M) with cart id 706 and order id 9017, "
            "open a support case titled Cancel requested then cancel the order and resolve the case. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "204",
                    "subject": "Cancel requested",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
            Action(name="update_case_status", kwargs={"case_id": "5001", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_076",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to create a cart, review and add ProBook X15, preview totals, then complete the order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_077",
        instruction=(
            "You are Taylor Reed from Security. Using the cache group sg-cache, you want controlled connectivity documented: "
            "allow Redis on tcp 6379 ingress from 10.150.0.0/16 with the description exactly Redis allow, then allow HTTPS egress on 443 0.0.0.0/0 "
            "with the description exactly HTTPS egress, listing rules after each step."
        ),
        actions=[
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 6379,
                    "cidr": "10.150.0.0/16",
                    "description": "Redis allow",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "egress",
                    "protocol": "tcp",
                    "port": 443,
                    "cidr": "0.0.0.0/0",
                    "description": "HTTPS egress",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_078",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to complete a discounted purchase of "
            "Branded Hoodie (M) with the WINTER20 coupon comparing the price before and after the offer is applied. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1006", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_079",
        instruction=(
            "You are Mike Rivera (m.rivera@apexlogistics.com). From category CAT103, you want to ensure the final basket "
            "includes USB-C Hub and excludes 4K Webcam. You should complete the purchase."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="remove_item_from_cart", kwargs={"cart_id": "706", "product_id": "1018"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_080",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to buy a ProBook X15. "
            "After checkout, you want to set the shipping address exactly to: name Sandra Dee, line1 42 Ocean Ave, "
            "city Miami, region FL, postal_code 33101, country US. Then you want to return the ProBook X15 with "
            "reason Return within policy."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Sandra Dee",
                        "line1": "42 Ocean Ave",
                        "city": "Miami",
                        "region": "FL",
                        "postal_code": "33101",
                        "country": "US",
                    },
                },
            ),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9017",
                    "lines": [{"product_id": "1001", "qty": 1}],
                    "reason": "Return within policy",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_081",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to buy a Pro Gaming Mouse. "
            "After checkout, you want to set the shipping address exactly to: name Bob Williams, line1 9 Elm Rd, city Denver, "
            "region CO, postal_code 80202, country US. Then you want to cancel the order."
        ),
        actions=[
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Bob Williams",
                        "line1": "9 Elm Rd",
                        "city": "Denver",
                        "region": "CO",
                        "postal_code": "80202",
                        "country": "US",
                    },
                },
            ),
            Action(
                name="cancel_order",
                kwargs={"order_id": "9017", "cancel_at": "2025-08-06T12:00:00Z"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_082",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to buy a 1TB NVMe SSD, but after "
            "placing it in your cart you decide not to buy it yet. Instead you create a second cart and add 2 Wireless Mouse and complete the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1003", "quantity": 2},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "707",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_083",
        instruction=(
            "You are Maria Garcia. You are browsing both USB-C Hub and Wireless Mouse and decide to use maria.g@email.com to create a cart and "
            "add one of each and complete the purchase."
        ),
        actions=[
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_084",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to buy a 4K Webcam, "
            "then issue a full refund with reason Goodwill."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="refund_order_full", kwargs={"order_id": "9017", "reason": "Goodwill"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_085",
        instruction=(
            "You are Priya Shah from Cloud Engineering. You register a Performance Cache subnet group sgp-perf-02 "
            "(name perf-cache, VPC vpc-perf, subnets [subnet-p3,subnet-p4]) with description Performance cache and verify it. "
            "You then deploy a Redis cache ec-perf-02 on security group sg-cache and subnet group sgp-perf-02 using engine redis, "
            "node_type cache.m6g.large, num_nodes 2, endpoint ec-perf-02.cache.local, and port 6379. You enable auth tokens and encryption "
            "(in transit and at rest). You bring the cluster to status Available and read it back, then list clusters to confirm inventory. "
            "This change supports commerce pricing throughput during peak promos."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="create_subnet_group",
                kwargs={
                    "subnet_group_id": "sgp-perf-02",
                    "name": "perf-cache",
                    "description": "Performance cache",
                    "subnet_ids": ["subnet-p3", "subnet-p4"],
                    "vpc_id": "vpc-perf",
                },
            ),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "sgp-perf-02"}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-perf-02",
                    "engine": "redis",
                    "node_type": "cache.m6g.large",
                    "num_nodes": 2,
                    "subnet_group_id": "sgp-perf-02",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-perf-02.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-perf-02",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-perf-02"}),
            Action(name="list_elasticache_clusters", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_086",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to buy a Wireless Mouse. After seeing the price "
            "in the cart you decide to add a second one and a USB-C Hub and complete the order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1003", "new_quantity": 2}
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_087",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to buy a USB-C Hub and a Wireless Mouse and complete the order, "
            "then you look up Branded Hoodie (M) but you dont like the style so you do not add to cart."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "Branded Hoodie (M)"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_088",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to add a 1TB NVMe SSD, "
            "then complete the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_089",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to purchase a 1TB NVMe SSD. You realize "
            "after creating the order that you needed 2 and add a one to a new cart but decide to wait to purchase because you missed the "
            "shipping window."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1016", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_090",
        instruction=(
            "You are Mike Rivera (m.rivera@apexlogistics.com). You want buy a Wireless Mouse and then "
            "you then want to browse the Computer Accessories catalog, and add a USB-C Hub to a cart. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "707", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "707", "product_id": "1002", "quantity": 1},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_091",
        instruction=(
            "You are Kevin Lee (kevin.lee@starlight.net). You want to buy a ProBook X15 and QuantumBook Pro, "
            "read back the items on the order. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_product_by_name", kwargs={"name": "ProBook X15"}),
            Action(name="get_product_by_name", kwargs={"name": "QuantumBook Pro"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "210",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1001", "quantity": 1},
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1005", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_092",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want buy a USB-C Hub as a Replacement, then start the return process for "
            "your old order 9009."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="list_order_items", kwargs={"order_id": "9009"}),
            Action(
                name="return_order",
                kwargs={
                    "order_id": "9009",
                    "lines": [{"product_id": "1002", "qty": 1}],
                    "reason": "Replacement",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_093",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to purchase an Ergo Laptop Stand reviewing the cart before finalizing, then set the "
            "shipping address exactly to: name Sandra Dee, line1 42 Ocean Ave, city Miami, region FL, "
            "postal_code 33101, country US. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Sandra Dee",
                        "line1": "42 Ocean Ave",
                        "city": "Miami",
                        "region": "FL",
                        "postal_code": "33101",
                        "country": "US",
                    },
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_094",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to buy a 4K Webcam, double check you added the right item, "
            "then issue a $20.0 partial refund with reason Goodwill and show the refund record."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "204",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="refund_order_partial",
                kwargs={"order_id": "9017", "amount": 20.0, "reason": "Goodwill"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_095",
        instruction=(
            "You are Maria Garcia (maria.g@email.com). You want to browse CAT103, apply B2BVOLUME15, "
            "then buy a Pro Gaming Mouse."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="list_products_in_category", kwargs={"category_id": "CAT103"}),
            Action(name="get_offer_by_code", kwargs={"code": "B2BVOLUME15"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "207",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "B2BVOLUME15"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_096",
        instruction=(
            "You are Mike Rivera (m.rivera@apexlogistics.com). You want to purchase 50 1TB NVMe SSD. "
            "You want to preview the totals and apply B2BVOLUME15 if it applies before placing the order and then finalize the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "m.rivera@apexlogistics.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "209",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 50},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "B2BVOLUME15"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_097",
        instruction=(
            "You are Bob Williams (bob.w@email.com). You want to purchase a Wireless Mouse and review your cart. "
            "You decide to also add and 2 USB-C Hub and review again. You decide you dont need 2 Hubs and drop the quantity down "
            "to 1 and add a second mouse instead then place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "205",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1002", "new_quantity": 1}
            ),
            Action(
                name="set_item_quantity", kwargs={"cart_item_id": "706:1003", "new_quantity": 2}
            ),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_098",
        instruction=(
            "You are Taylor Reed from Security & Commerce Ops. You record a cache connectivity update on the security group sg-cache "
            "by allowing Redis on 6379/tcp ingress from cidr 10.160.0.0/16 described Redis allow. To validate pricing against the cache, "
            "you run a quick basket smoke for David Chen (david.chen@quantum.co): build a cart for one USB-C Hub, preview totals using "
            "his normal account pricing, and stop before checkout. You keep the final rule listing visible for audit."
        ),
        actions=[
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 6379,
                    "cidr": "10.160.0.0/16",
                    "description": "Redis allow",
                },
            ),
            Action(name="get_contact_by_email", kwargs={"email": "david.chen@quantum.co"}),
            Action(name="get_account_by_id", kwargs={"account_id": "105"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="create_cart",
                kwargs={"contact_id": "206", "created_at": "2025-08-06T12:00:00Z"},
            ),
            Action(name="switch_cart_pricebook", kwargs={"cart_id": "706", "pricebook_id": "2"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_099",
        instruction=(
            "You are Priya Shah from Cloud Engineering. In production, create a small Redis metrics cache with cluster_id ec-metrics-02 "
            "on the production cache subnet group and the cache security group. Bring it to Available and confirm the cluster. "
            "For audit, show the security-group rules before any change, then allow metrics on 9121/tcp from 10.20.0.0/16 with the "
            "description Metrics scrapers, and show the rules again."
        ),
        actions=[
            Action(name="list_subnet_groups", kwargs={}),
            Action(
                name="provision_elasticache_cluster",
                kwargs={
                    "cluster_id": "ec-metrics-02",
                    "engine": "redis",
                    "node_type": "cache.t3.small",
                    "num_nodes": 1,
                    "subnet_group_id": "esg-prod-1",
                    "security_group_id": "sg-cache",
                    "auth_token_enabled": True,
                    "transit_encryption_enabled": True,
                    "at_rest_encryption_enabled": True,
                    "endpoint": "ec-metrics-02.cache.local",
                    "port": 6379,
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="update_elasticache_cluster_status",
                kwargs={
                    "cluster_id": "ec-metrics-02",
                    "status": "Available",
                    "changed_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "ec-metrics-02"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "group_id": "sg-cache",
                    "direction": "ingress",
                    "protocol": "tcp",
                    "port": 9121,
                    "cidr": "10.20.0.0/16",
                    "description": "Metrics scrapers",
                },
            ),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-cache"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v5",
        user_id="task_100",
        instruction=(
            "You are Sandra Dee (sandra.d@email.com). You want to apply the WINTER20 coupon and "
            "purchase a Wireless Mouse. After checkout, you want to set the shipping address exactly to: "
            "name Sandra Dee, line1 42 Ocean Ave, city Miami, region FL, postal_code 33101, country US."
        ),
        actions=[
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="create_cart",
                kwargs={
                    "contact_id": "208",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(
                name="create_order",
                kwargs={
                    "cart_id": "706",
                    "created_at": "2025-08-06T12:00:00Z",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={
                    "order_id": "9017",
                    "address": {
                        "name": "Sandra Dee",
                        "line1": "42 Ocean Ave",
                        "city": "Miami",
                        "region": "FL",
                        "postal_code": "33101",
                        "country": "US",
                    },
                },
            ),
        ],
        outputs=[],
    ),
]
