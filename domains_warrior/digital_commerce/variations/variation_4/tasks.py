from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="v4",
        user_id="task_001",
        instruction=(
            "You are John Doe at Global Tech, using john.doe@globaltech.com. "
            "You want to order 1 'USB-C Hub' and 2 'Ergo Laptop Stand', apply WELCOME5, review the totals, and place the order with shipping. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_002",
        instruction=(
            "You are Emily White at Innovate, using emily.white@innovate.com. "
            "You want to buy three 'Wireless Mouse' using WELCOME5 and have the items shipped. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 3},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_003",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). You want to return one '4K Webcam' from Order 9016 "
            "and track it with a case. You want to mark it Resolved."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "204"}),
            Action(
                name="create_case",
                kwargs={"contact_id": "204", "order_id": "9016", "subject": "Return processed for Order #9016"},
            ),
            Action(name="list_order_items", kwargs={"order_id": "9016"}),
            Action(name="validate_return_eligibility", kwargs={"order_id": "9016"}),
            Action(
                name="return_order",
                kwargs={"order_id": "9016", "lines": [{"product_id": "1018", "qty": 1}]},
            ),
            Action(name="list_order_items", kwargs={"order_id": "9016"}),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_004",
        instruction=(
            "You are Bob Williams at B2B Co., using 'bob.w@email.com'. "
            "You want to purchase one 'Ergo Laptop Stand'. You want to know if you're eligible for any promo."
            "Since you're business user, you're not eligible for any welcome promo. You want to know order total."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["55"],
    ),
    Task(
        annotator="v4",
        user_id="task_005",
        instruction=(
            "You are Alice Johnson at Apex Logistics, using 'alice.j@email.com'. "
            "You want to validate discount calculus by applying WELCOME5 to two 'Wireless Mouse' and reviewing the totals before ordering. "
            "After the totals look right, place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="create_cart", kwargs={"contact_id": "204"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_006",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want a single-item purchase of a 'USB-C Hub' and to use your saved shipping address."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_007",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want a two-line order: two 'Wireless Mouse' and a 'Ergo Laptop Stand'. Apply WELCOME5, review totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_008",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to place a quick one-unit order for 'USB-C Hub' using WINTER20, ship, "
            "and then cancel the order. Track the cancellation with a case titled 'Cancellation for Order #9017' and close it."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "207",
                    "subject": "Cancellation for Order #9017",
                },
            ),
            Action(name="cancel_order", kwargs={"order_id": "9017"}),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_009",
        instruction=(
            "You are Bob Williams, using 'bob.w@email.com'. "
            "You want to order 1 'Ergo Laptop Stand', ship, open a support case titled 'Please attach invoice PDF', and then mark the case as 'Closed'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "205",
                    "subject": "Please attach invoice PDF",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Closed"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_010",
        instruction=(
            "You are John Doe at Global Tech (john.doe@globaltech.com) checking on your case 5009. "
            "You want to correct the shipping address on Order #9002 to '123 Tech Park, Building B' and close the case after verifying the items."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "201"}),
            Action(
                name="create_case",
                kwargs={
                    "contact_id": "201",
                    "order_id": "9002",
                    "subject": "Address Correction: Order #9002",
                },
            ),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9002", "address": "123 Tech Park, Building B"},
            ),
            Action(name="list_order_items", kwargs={"order_id": "9002"}),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_011",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to buy 2 'Pro Gaming Mouse' with WELCOME5, review the totals, and place the order. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_012",
        instruction=(
            "You are Chloe Davis at Contoso, using 'chloe.davis@email.com'. "
            "You want to see which offers are active, then buy 1 '4K Webcam'. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "chloe.davis@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "110"}),
            Action(name="create_cart", kwargs={"contact_id": "211"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_013",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want your UAT cache 'dcomm-uat-redis' reachable from corporate by allowing tcp 6379 from 10.0.0.0/16 on its security group. "
            "Then you want a one-unit validation order for 'USB-C Hub' using WELCOME5 and shipped. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.0.0.0/16",
                },
            ),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_014",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to buy 1 '4K Webcam' with WELCOME5, review the totals, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_015",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to buy 1 'Mechanical Keyboard' and 1 'Wireless Mouse' with WINTER20, you want to know the totals but you don't want to create the order yet. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1017", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
        ],
        outputs=["152"],
    ),
    Task(
        annotator="v4",
        user_id="task_016",
        instruction=(
            "You are Alice Johnson (alice.j@email.com). For UAT caches, you want to rename subnet group "
            "'esg-uat-1' to 'uat-cache-subnets-v2'. You want to use your last order_id for the case with subject Subnet group rename."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "204"}),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "esg-uat-1"}),
            Action(
                name="create_case",
                kwargs={"order_id": "9016", "contact_id": "204", "subject": "Subnet group rename"},
            ),
            Action(
                name="update_subnet_group_description",
                kwargs={
                    "subnet_group_id": "esg-uat-1",
                    "name": "uat-cache-subnets-v2",
                    "description": "esg-uat-1",
                },
            ),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "esg-uat-1"}),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_017",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to buy 1 'USB-C Hub' and 1 'Wireless Mouse', apply WELCOME5, review totals both before and after the discount, "
            "and then place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_018",
        instruction=(
            "You are Maria Garcia. "
            "You want to buy 2 'Pro Gaming Mouse' and 1 '1TB NVMe SSD' with no discount and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(name="set_order_shipping_address", kwargs={"order_id": "9017", "address": "888 Ocean View"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_019",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to buy 1 'USB-C Hub' and 1 '1TB NVMe SSD', review the totals, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_020",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to buy 1 'Pro Gaming Mouse', review the totals before applying WELCOME5, apply WELCOME5, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_021",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to buy 2 'USB-C Hub', 1 'Ergo Laptop Stand', and 1 '4K Webcam', apply WINTER20, review the totals, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_022",
        instruction=(
            "You are Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want to see what offers are active, then buy 2 'Wireless Mouse' and 1 'Pro Gaming Mouse' with WELCOME5, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "107"}),
            Action(name="create_cart", kwargs={"contact_id": "208"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Oak Avenue"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_023",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to buy 1 '1TB NVMe SSD' with no discount, review the totals, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_024",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to buy 1 'USB-C Hub' and 2 'Mechanical Keyboard', review the totals, apply WINTER20, and place the order with shipping. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1017", "quantity": 2},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_025",
        instruction=(
            "You are Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want to see the active offers, then buy 2 'Ergo Laptop Stand' and 1 'USB-C Hub'. "
            "You think you should preview totals, apply WINTER20, preview again, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "202"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_026",
        instruction=(
            "You are Chloe Davis at Contoso, using 'chloe.davis@email.com'. "
            "You want to buy 1 'Pro Gaming Mouse' and 1 'Wireless Mouse', apply WELCOME5, review the totals, and place the order. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "chloe.davis@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "110"}),
            Action(name="create_cart", kwargs={"contact_id": "211"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_027",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to buy 1 'Ergo Laptop Stand' and 1 '4K Webcam', apply WELCOME5, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_028",
        instruction=(
            "You are Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want to check active offers, buy 1 'USB-C Hub' apply WINTER20, review totals, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "202"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_029",
        instruction=(
            "You are Chloe Davis at Contoso, using 'chloe.davis@email.com'. "
            "You want to buy 1 'USB-C Hub', 2 'Wireless Mouse', and 1 'Pro Gaming Mouse' with no discount, review totals, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "chloe.davis@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "110"}),
            Action(name="create_cart", kwargs={"contact_id": "211"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_030",
        instruction=(
            "You are Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want to buy 1 'Pro Gaming Mouse' and 1 'USB-C Hub', apply WINTER20 after adding the first item, review totals, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "107"}),
            Action(name="create_cart", kwargs={"contact_id": "208"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Oak Avenue"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_031",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to buy 1 '1TB NVMe SSD', review totals, apply WELCOME5, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_032",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to buy 3 'Wireless Mouse' with no discount and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 3},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_033",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to check active offers, then buy 1 '1TB NVMe SSD' and 1 '4K Webcam' with no discount, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_034",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to buy 2 'Ergo Laptop Stand', apply WELCOME5, review totals, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_035",
        instruction=(
            "You are Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want to buy 1 'Pro Gaming Mouse' with no discount, preview totals, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "202"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_036",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to buy 1 'USB-C Hub' and 2 'Ergo Laptop Stand', preview totals, then apply WINTER20, preview again, and place the order with shipping. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_037",
        instruction=(
            "You are John Doe. "
            "You want your UAT cache 'dcomm-uat-redis' reachable from corporate: look up the cluster and add a tcp 6379 rule for 10.0.0.0/16 to its security group. "
            "Then place a one-unit validation order for 'USB-C Hub' using WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.0.0.0/16",
                },
            ),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_038",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to place a one-unit validation order for 'Ergo Laptop Stand' with WELCOME5 and ship. After that, open a support case with subject 'Need invoice copy'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "213", "subject": "Need invoice copy"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_039",
        instruction=(
            "You are Sandra Dee at Apex Logistics, using 'sandra.d@email.com'. "
            "You want to buy 1 'USB-C Hub' with WELCOME5, and place the order. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "sandra.d@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "107"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "107"}),
            Action(name="create_cart", kwargs={"contact_id": "208"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_040",
        instruction=(
            "You are Kevin Lee. "
            "You want to buy 1 '1TB NVMe SSD', preview the totals and place the order with address '123 Tech Park'. You want to know the order total."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["95"],
    ),
    Task(
        annotator="v4",
        user_id="task_041",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to buy 1 'Pro Gaming Mouse' using WINTER20, preview totals, ship, "
            "and then refund $10.00 as a partial goodwill credit. Track the refund with case ID 7013 titled "
            "'Partial Refund for Order #9017' and close it after. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "210",
                    "subject": "Partial Refund for Order #9017",
                },
            ),
            Action(name="refund_order_partial", kwargs={"order_id": "9017", "amount": 10.0}),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_042",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to scale your cache: set the instance type on 'dcomm-uat-redis' to 'cache.r5.large'. "
            "Then you want a two-line purchase: 2 'Ergo Laptop Stand' and 1 'USB-C Hub', apply WELCOME5, preview totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="update_elasticache_instance_type",
                kwargs={"cluster_id": "dcomm-uat-redis", "instance_type": "cache.r5.large"},
            ),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_043",
        instruction=(
            "You are Emily White (emily.white@innovate.com). You want to start a return for Order #9011 for one 'Wireless Mouse' and track it with a case."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="list_order_items", kwargs={"order_id": "9011"}),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9011",
                    "contact_id": "203",
                    "subject": "Return request for Order #9011",
                },
            ),
            Action(name="validate_return_eligibility", kwargs={"order_id": "9011"}),
            Action(name="list_order_items", kwargs={"order_id": "9011"}),
            Action(
                name="return_order",
                kwargs={"order_id": "9011", "lines": [{"product_id": "1013", "qty": 1}]},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_044",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to resize 'dcomm-uat-redis' to node_type 'cache.r5.large' with 3 nodes to give UAT headroom. "
            "Then you want a one-unit order for 'USB-C Hub' shipped. Return the order total."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="update_elasticache_cluster_config",
                kwargs={
                    "cluster_id": "dcomm-uat-redis",
                    "node_type": "cache.r5.large",
                    "num_nodes": 3,
                },
            ),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["60"],
    ),
    Task(
        annotator="v4",
        user_id="task_045",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to confirm available promos, apply WELCOME5 to 1 'Ergo Laptop Stand', preview totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_046",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want a cart clean-up before checkout: add 1 'USB-C Hub', change it to 2, and add 1 'Pro Gaming Mouse'. "
            "Preview totals, create the order, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="set_item_quantity", kwargs={"cart_item_id": "9", "quantity": 2}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_047",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to purchase 'USB-C Hub' quantity 2 and one 'Ergo Laptop Stand' with no discount "
            "with shipping to '809 Main St'. Return the order total."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "809 Main St"},
            ),
        ],
        outputs=["165"],
    ),
    Task(
        annotator="v4",
        user_id="task_048",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to start a cart with 2 'Pro Gaming Mouse' using WELCOME5. "
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_049",
        instruction=(
            "You are John Doe. "
            "You want to stock up on stands: buy 2 'Ergo Laptop Stand', apply WELCOME5, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_050",
        instruction=(
            "You are Chloe Davis (chloe.davis@email.com). Add two items, 1 Pro Gaming Mouse and 1 USB-C Hub and preview the cart. "
            "You want to then remove the hub, preview the cart again and place the order."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "chloe.davis@email.com"}),
            Action(name="create_cart", kwargs={"contact_id": "211"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="remove_item_from_cart", kwargs={"cart_id": "706", "product_id": "1002"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_051",
        instruction=(
            "You are Jane Smith at Global Tech. Buy 1 'Pro Gaming Mouse' using WELCOME5 and ship to your address."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "202"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_052",
        instruction=(
            "You are John Doe (john.doe@globaltech.com). Change the instance class of 'dcomm-uat-redis' to "
            "'cache.r6g.large' and track it with a case."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "201"}),
            Action(
                name="create_case",
                kwargs={"order_id": "9002", "contact_id": "201", "subject": "cache.r6g.large"},
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="update_elasticache_instance_type",
                kwargs={"cluster_id": "dcomm-uat-redis", "instance_type": "cache.r6g.large"},
            ),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_053",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to review carts are clean before buying then start a new cart, add 1 'Ergo Laptop Stand', preview totals, "
            "and make the order. Return the order total."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="list_carts_for_contact", kwargs={"contact_id": "207"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["55"],
    ),
    Task(
        annotator="v4",
        user_id="task_054",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to double-check cart contents before purchase: create a cart, add 1 'USB-C Hub', list cart items, then add 1 'Ergo Laptop Stand', preview totals, and ship the order. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="list_cart_items", kwargs={"cart_id": "706"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_055",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to review cache access before buying: list security-group rules on 'sg-0123456789abcdef0' and then "
            "place a two-line order—1 'USB-C Hub' and 1 'Pro Gaming Mouse'—apply WELCOME5, and ship. "
            "Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-0123456789abcdef0"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_056",
        instruction=(
            "You are Jane Smith at Global Tech, using 'jane.smith@globaltech.com'. "
            "You want a quick one-unit order for 'USB-C Hub', ship, and then review the items on the order. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "jane.smith@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "202"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
            Action(name="list_order_items", kwargs={"order_id": "9017"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_057",
        instruction=(
            "You are John Doe at Global Tech. "
            "You want a straightforward two-line checkout: 1 'USB-C Hub' apply WELCOME5, and preview totals. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_058",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to check what promos are live, then buy 1 'USB-C Hub' with WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_059",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want a clean purchase of 1 '4K Webcam' shipped, and then you want to open a support case on that order with subject 'Need RMA instructions'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "207",
                    "subject": "Need RMA instructions",
                },
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_060",
        instruction=(
            "You are Bob Williams. "
            "You want to place a simple order for 1 'Pro Gaming Mouse' with no discount. You want to review the cart and ship."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Bob", "last_name": "Williams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_061",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to review your most recent order items, then buy 1 'USB-C Hub' with WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "201"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_062",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want a two-line order—1 'Ergo Laptop Stand' and 1 'Wireless Mouse'—apply WINTER20, review totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_063",
        instruction=(
            "You are Maria Garcia. "
            "You want to check active offers, then buy 1 '1TB NVMe SSD' with WINTER20, review the totals, and ship. Return the order id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_064",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want corporate access to Redis by adding a tcp 6379 rule from 10.1.0.0/16 on security group 'sg-0123456789abcdef0'. "
            "Then buy 2 'Wireless Mouse' with WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-0123456789abcdef0"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.1.0.0/16",
                },
            ),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_065",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to see if you already have a cart open; if not, start a new cart and buy 1 '4K Webcam' with WELCOME5, review the totals, and ship."
            "You want to know the amount of money you saved by using any promo."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="list_carts_for_contact", kwargs={"contact_id": "213"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
        ],
        outputs=["5"],
    ),
    Task(
        annotator="v4",
        user_id="task_066",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to fetch WELCOME5 first, then buy 2 'Pro Gaming Mouse', review the totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 2},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_067",
        instruction=(
            "You are Alice Johnson. You want to know if you're eligible for any welcome promo. "
            "You want to buy 1 'Mechanical Keyboard' and order it right away. You want to know the amount of money you saved by using any promo."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Alice", "last_name": "Johnson"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "103"}),
            Action(name="create_cart", kwargs={"contact_id": "204"}),
            Action(name="get_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1017", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "789 Home St"},
            ),
        ],
        outputs=["5"],
    ),
    Task(
        annotator="v4",
        user_id="task_068",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to review rules on security group for 'dcomm-uat-redis' and add a tcp 6379 rule from 10.2.0.0/16. "
            "Then buy 1 'USB-C Hub' and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-0123456789abcdef0"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.2.0.0/16",
                },
            ),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_069",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to review your ElastiCache subnet groups, then buy 1 'USB-C Hub' with WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="list_subnet_groups", kwargs={}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_070",
        instruction=(
            "You are Susan Adams at Pioneer Corp. "
            "You want to buy 1 'Ergo Laptop Stand' with WINTER20, ship, and open a case titled 'Please ship asap'. Return the order id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Susan", "last_name": "Adams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "213", "subject": "Please ship asap"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_071",
        instruction=(
            "You are John Doe. "
            "You want to use WELCOME5, then buy 2 'USB-C Hub', review the totals and complete the order."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_072",
        instruction=(
            "You are Alice Johnson at Innovate, using 'alice.j@email.com'. "
            "You want to close support case '5002' using Closed. Then place a one-unit order for 'USB-C Hub' and ship."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="update_case_status", kwargs={"case_id": "5002", "status": "Closed"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "103"}),
            Action(name="create_cart", kwargs={"contact_id": "204"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "789 Home St"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_073",
        instruction=(
            "You are Susan Adams. "
            "You want to buy 1 'Ergo Laptop Stand' and ship. After placing the order, you want a case opened with subject 'Please email receipt'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Susan", "last_name": "Adams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "213", "subject": "Please email receipt"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_074",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to allow corporate access to 'dcomm-uat-redis' by adding a tcp 6379 rule from 10.0.0.0/16 on security group 'sg-0123456789abcdef0'. "
            "Then buy 1 '1TB NVMe SSD' with WELCOME5 and ship."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="list_elasticache_clusters", kwargs={}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.0.0.0/16",
                },
            ),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_075",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to label support case '5007' Closed. Then buy 1 'Wireless Mouse' with WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="update_case_status", kwargs={"case_id": "5007", "status": "Closed"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_076",
        instruction=(
            "You are Chloe Davis. "
            "You want a two-item order — 1 'USB-C Hub' and 1 '4K Webcam' — and you want to apply WELCOME5 and review the totals before placing the order."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Chloe", "last_name": "Davis"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "110"}),
            Action(name="create_cart", kwargs={"contact_id": "211"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_077",
        instruction=(
            "You are Bob Williams. "
            "You want to buy 2 'Pro Gaming Mouse', verify totals with WELCOME5, and ship."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Bob", "last_name": "Williams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 2},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_078",
        instruction=(
            "You are Susan Adams. "
            "You want to mark support case '5008' Closed. Then place a one-unit order for '4K Webcam' and ship."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Susan", "last_name": "Adams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="update_case_status", kwargs={"case_id": "5008", "status": "Closed"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_079",
        instruction=(
            "You are Alice Johnson at Innovate, using 'alice.j@email.com'. "
            "You want to start a new cart if none exist, then buy 1 'Mechanical Keyboard' and ship. After ordering, open a case titled 'Key chatter issue'."
            "You want to know the stock quantity of USB-C Hub as well"
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "alice.j@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="list_carts_for_contact", kwargs={"contact_id": "204"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "103"}),
            Action(name="create_cart", kwargs={"contact_id": "204"}),
            Action(name="get_product_by_name", kwargs={"name": "Mechanical Keyboard"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1017", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "789 Home St"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "204", "subject": "Key chatter issue"},
            ),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
        ],
        outputs=["200"],
    ),
    Task(
        annotator="v4",
        user_id="task_080",
        instruction=(
            "You are Kevin Lee at Starlight. "
            "You want to fetch the WELCOME5 offer and then buy 2 'USB-C Hub', review the totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_081",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to reorder 1 'USB-C Hub': check your recent orders, apply WELCOME5, preview the totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="list_orders_for_contact", kwargs={"contact_id": "201"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="list_active_offers", kwargs={}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_082",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to buy 1 'USB-C Hub', place the order with shipping, and open a case titled 'Keys feel stiff' to track a concern."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "203", "subject": "Keys feel stiff"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v4",
        user_id="task_083",
        instruction=(
            "You are Maria Garcia. "
            "You want to buy 1 'Wireless Mouse' and ship. Return the order id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_084",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to place a quick one-unit order for 'Ergo Laptop Stand' and then cancel it before fulfillment by creating a case with subject 'Ordered by mistake'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "205", "subject": "Ordered by mistake"},
            ),
            Action(name="cancel_order", kwargs={"order_id": "9017"}),
            Action(name="update_case", kwargs={"case_id": "5009", "status": "Resolved"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_085",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to review your ElastiCache fleet and confirm the presence of 'dcomm-uat-redis', then place a one-unit order for 'USB-C Hub' shipped. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="list_elasticache_clusters", kwargs={}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "555 Galaxy Blvd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_086",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to upsize 'dcomm-uat-redis' to 'cache.r5.large' for performance, then place a one-unit order for '1TB NVMe SSD' and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(
                name="update_elasticache_instance_type",
                kwargs={"cluster_id": "dcomm-uat-redis", "instance_type": "cache.r5.large"},
            ),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_087",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to review subnet groups, check 'esg-uat-1', and update its description to 'UAT Redis subnets'. "
            "Then buy 1 'Wireless Mouse' and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="list_subnet_groups", kwargs={}),
            Action(name="get_subnet_group", kwargs={"subnet_group_id": "esg-uat-1"}),
            Action(
                name="update_subnet_group_description",
                kwargs={
                    "subnet_group_id": "esg-uat-1",
                    "description": "UAT Redis subnets",
                    "name": "uat-cache-subnets",
                },
            ),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_088",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to fetch the WINTER20 offer, then place a one-unit order for 'USB-C Hub' using WINTER20 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_offer_by_code", kwargs={"code": "WINTER20"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_089",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to start a cart for 1 'Ergo Laptop Stand', review the cart contents, then apply WELCOME5 and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="list_cart_items", kwargs={"cart_id": "706"}),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_090",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to buy 1 'Pro Gaming Mouse', preview the totals, place the order, and open a case titled 'Need invoice copy'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "205", "subject": "Need invoice copy"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_091",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want a two-line order—1 'USB-C Hub' and 1 '4K Webcam'—check active offers, apply WELCOME5, review totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_092",
        instruction=(
            "You are Emily White at Innovate, using 'emily.white@innovate.com'. "
            "You want to buy 1 'USB-C Hub', preview the totals, ship, and open a case titled 'Keys feel stiff' after the order is placed. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "emily.white@innovate.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "203", "subject": "Keys feel stiff"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_093",
        instruction=(
            "You are Maria Garcia, using 'maria.g@email.com'. "
            "You want to fetch the WELCOME5 offer, then buy 1 'Ergo Laptop Stand', create the order, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "maria.g@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="get_offer_by_code", kwargs={"code": "WELCOME5"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_094",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want corporate access to Redis by adding a tcp 6379 rule from 10.3.0.0/16 on security group 'sg-0123456789abcdef0'. "
            "Then buy 1 'Pro Gaming Mouse' with WINTER20, review totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="list_security_group_rules", kwargs={"group_id": "sg-0123456789abcdef0"}),
            Action(
                name="add_security_group_rule",
                kwargs={
                    "security_group_id": "sg-0123456789abcdef0",
                    "port": 6379,
                    "protocol": "tcp",
                    "source_ip": "10.3.0.0/16",
                },
            ),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Pro Gaming Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1013", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_095",
        instruction=(
            "You are Susan Adams at Pioneer Corp., using 's.adams@pioneercorp.com'. "
            "You want to check if you already have carts open, then start a new cart and buy 1 '1TB NVMe SSD' with WELCOME5. "
            "Create the order, ship, and open a case titled 'Please expedite if possible'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "s.adams@pioneercorp.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(name="list_carts_for_contact", kwargs={"contact_id": "213"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "112"}),
            Action(name="create_cart", kwargs={"contact_id": "213"}),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "1 Technology Plaza"},
            ),
            Action(
                name="create_case",
                kwargs={
                    "order_id": "9017",
                    "contact_id": "213",
                    "subject": "Please expedite if possible",
                },
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_096",
        instruction=(
            "You are Kevin Lee at Starlight, using 'kevin.lee@starlight.net'. "
            "You want to review your ElastiCache clusters and confirm details for 'dcomm-uat-redis', then buy 1 'Wireless Mouse' and '1TB NVMe SSD'. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "kevin.lee@starlight.net"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "109"}),
            Action(name="list_elasticache_clusters", kwargs={}),
            Action(name="get_elasticache_cluster", kwargs={"cluster_id": "dcomm-uat-redis"}),
            Action(name="create_cart", kwargs={"contact_id": "210"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "1TB NVMe SSD"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1016", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_097",
        instruction=(
            "You are John Doe at Global Tech, using 'john.doe@globaltech.com'. "
            "You want to check active offers, apply WINTER20 to 1 'Wireless Mouse', review cart contents, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "john.doe@globaltech.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "101"}),
            Action(name="list_active_offers", kwargs={}),
            Action(name="create_cart", kwargs={"contact_id": "201"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 1},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WINTER20"}),
            Action(name="list_cart_items", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "123 Tech Park"},
            ),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_098",
        instruction=(
            "You are Emily White at Innovate. "
            "You want a two-line order—1 'USB-C Hub' and 1 'Ergo Laptop Stand'—create the order and ship, then open a case titled 'Package arrived late' and mark it Closed. Return the order id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "102"}),
            Action(name="create_cart", kwargs={"contact_id": "203"}),
            Action(name="get_product_by_name", kwargs={"name": "USB-C Hub"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1002", "quantity": 1},
            ),
            Action(name="get_product_by_name", kwargs={"name": "Ergo Laptop Stand"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1010", "quantity": 1},
            ),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "456 Innovation Ave"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "203", "subject": "Package arrived late"},
            ),
            Action(name="update_case_status", kwargs={"case_id": "5009", "status": "Closed"}),
        ],
        outputs=["9017"],
    ),
    Task(
        annotator="v4",
        user_id="task_099",
        instruction=(
            "You are Maria Garcia. "
            "You want to buy 1 '4K Webcam', preview the totals, ship, and open a case titled 'Need delivery ETA'. Return the case id."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "106"}),
            Action(name="create_cart", kwargs={"contact_id": "207"}),
            Action(name="get_product_by_name", kwargs={"name": "4K Webcam"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1018", "quantity": 1},
            ),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "888 Ocean View"},
            ),
            Action(
                name="create_case",
                kwargs={"order_id": "9017", "contact_id": "207", "subject": "Need delivery ETA"},
            ),
        ],
        outputs=["5009"],
    ),
    Task(
        annotator="v4",
        user_id="task_100",
        instruction=(
            "You are Bob Williams at Tech Solutions, using 'bob.w@email.com'. "
            "You want to apply WELCOME5 to 2 'Wireless Mouse', review totals, and ship. Return the order id."
        ),
        actions=[
            Action(name="get_contact_by_email", kwargs={"email": "bob.w@email.com"}),
            Action(name="get_account_by_id", kwargs={"account_id": "104"}),
            Action(name="get_default_pricebook_for_account", kwargs={"account_id": "104"}),
            Action(name="create_cart", kwargs={"contact_id": "205"}),
            Action(name="get_product_by_name", kwargs={"name": "Wireless Mouse"}),
            Action(
                name="add_item_to_cart",
                kwargs={"cart_id": "706", "product_id": "1003", "quantity": 2},
            ),
            Action(name="apply_offer_to_cart", kwargs={"cart_id": "706", "code": "WELCOME5"}),
            Action(name="preview_cart_totals", kwargs={"cart_id": "706"}),
            Action(name="create_order", kwargs={"cart_id": "706"}),
            Action(
                name="set_order_shipping_address",
                kwargs={"order_id": "9017", "address": "321 Maple Rd"},
            ),
        ],
        outputs=["9017"],
    ),
]
