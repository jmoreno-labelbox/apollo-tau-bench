from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="v1",
        user_id="task_001",
        instruction=(
            "You are Jordan Kim from Commerce Ops. In UAT, you want a B2B quote for John Doe validated against stock so threshold pricing holds. "
            "You verify inventory for one QuantumBook Pro and two USB-C Hub, price from pricebook 2, apply B2BVOLUME15, and open a Low priority case."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(
                name="get_products_by_names", kwargs={"names": ["QuantumBook Pro", "USB-C Hub"]}
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1005", "required_quantity": 1},
                        {"product_id": "1002", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1005", "pricebook_id": "2"},
                        {"product_id": "1002", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1005", "quantity": 1, "price": 1900.0},
                        {"product_id": "1002", "quantity": 2, "price": 60.0},
                    ]
                },
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 2020.0, "offer_code": "B2BVOLUME15"},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_002",
        instruction=(
            "You are Dana Patel from Pricing. You want a fresh seasonal code wired through Digital Commerce so quotes see it. "
            "You create FALL25 as PERCENTAGE 25 then quote Kevin Lee for four 1TB NVMe SSDs at pricebook 2 with FALL25."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "FALL25",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 25,
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 4, "price": 95.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 380.0, "offer_code": "FALL25"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_003",
        instruction=(
            "You’re Sam Lee from Commerce Ops. In UAT, you prepare a small accessories quote for Nora Patel and her account: "
            "you fetch '4K Webcam' and 'Wireless Mouse', verify stock for 1 and 2 units, then price from pricebook '1' at unit 199.0 and 40.0 respectively "
            "to compute the subtotal (199.0*1 + 40.0*2 = 279.0). You open a Low case titled 'Quote Prepared' to attach the quote, and then resolve the case to show completion."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_account_by_id", kwargs={"account_id": "113"}),
            Action(name="get_products_by_names", kwargs={"names": ["4K Webcam", "Wireless Mouse"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1018", "required_quantity": 1},
                        {"product_id": "1003", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1018", "pricebook_id": "1"},
                        {"product_id": "1003", "pricebook_id": "1"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1018", "quantity": 1, "price": 199.0},
                        {"product_id": "1003", "quantity": 2, "price": 40.0},
                    ]
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_004",
        instruction=(
            "You are Jordan Kim from Commerce Ops. In UAT, you want a B2B reorder quote for John Doe based on shipped order 9002 "
            "so advisors can reuse the last configuration without surprises. "
            "You confirm the original order has status 'Shipped' first, if so, reprice from pricebook 2, verify availability, and open a Low priority case. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9002"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9002"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1001", "pricebook_id": "2"},
                        {"product_id": "1002", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1001", "quantity": 1, "price": 1250.0},
                        {"product_id": "1002", "quantity": 1, "price": 60.0},
                    ]
                },
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1001", "required_quantity": 1},
                        {"product_id": "1002", "required_quantity": 1},
                    ]
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                    "order_id": "9002",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_005",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, you want Emily White’s cart ready for a B2B review so reps can quote accurately. "
            "You add to the cart four USB-C Hub and two Wireless Mouse, confirm availability, price from pricebook 2. Return the subtotal of the added items. "
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub", "Wireless Mouse"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1002", "required_quantity": 4},
                        {"product_id": "1003", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={
                    "cart_id": "701",
                    "items": [
                        {"product_id": "1002", "quantity": 4},
                        {"product_id": "1003", "quantity": 2},
                    ],
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1002", "pricebook_id": "2"},
                        {"product_id": "1003", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1002", "quantity": 4, "price": 60.0},
                        {"product_id": "1003", "quantity": 2, "price": 32.0},
                    ]
                },
            ),
        ],
        outputs=["304"],
    ),
    Task(
        annotator="v1",
        user_id="task_006",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want a concession math check for John Doe at Global Tech Inc. priced without a promo so finance can sign off. "
            "You price two ProBook X15 from pricebook 2, apply a flat 500 discount, and log a Low case titled Math Check Logged. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_name", kwargs={"name": "Global Tech Inc."}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1001", "required_quantity": 2}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 2, "price": 1250.0}]},
            ),
            Action(
                name="calculate_discount_flat", kwargs={"subtotal": 2500.0, "discount_amount": 500}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Math Check Logged",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_007",
        instruction=(
            "You are Priya Rao from Sales Engineering. In UAT, you want a B2B quote for Kevin Lee for six '1TB NVMe SSD' priced from pricebook '2' with 'WINTER20' so the volume path and stock validation stay correct under staging data. "
            "You confirm availability first to avoid backorders, then log a Low priority case."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1016", "required_quantity": 6}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 6, "price": 95.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 570.0, "offer_code": "WINTER20"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_008",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, you want Sandra Dee’s cart cleaned so fulfillment isn’t blocked by OOS items. "
            "You make the cart show 'Ergo Laptop Stand' at quantity 2, remove 'Branded Water Bottle', verify availability of laptop stand."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Sandra", "last_name": "Dee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "208"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Ergo Laptop Stand", "Branded Water Bottle"]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "703", "items": [{"product_id": "1010", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "703", "product_ids": ["1012"]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1010", "required_quantity": 2}]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_009",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, you want the targeted code 'MIDMONTH10' (10%) registered and priced against real catalog data so marketing can roll it out with confidence. "
            "You create 'MIDMONTH10', run 'Load API Metadata', then compute totals for two 'Wireless Mouse' from pricebook '1' with 'MIDMONTH10' for John Doe and log a Low case 'Promo Lifecycle Logged'."
        ),
        actions=[
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "MIDMONTH10",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 10,
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "1",
                    "items_by_name": [{"name": "Wireless Mouse", "quantity": 2}],
                    "offer_code": "MIDMONTH10",
                },
            ),
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Promo Lifecycle Logged",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_010",
        instruction=(
            "You are Alex Chen from Customer Care. In UAT, you cancel Mike Rivera’s order 9010 that was placed by mistake, "
            "restock the returned items. Log this high priority case 'Ordered By Mistake'."
        ),
        actions=[
            Action(name="get_order_details_by_id", kwargs={"order_id": "9010"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9010"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "209",
                    "account_id": "108",
                    "order_id": "9010",
                    "subject": "Ordered By Mistake",
                    "priority": "High",
                },
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9010", "new_status": "Cancelled"}
            ),
            Action(
                name="add_stock_quantities",
                kwargs={
                    "items": [
                        {"product_id": "1005", "quantity_to_add": 1},
                        {"product_id": "1011", "quantity_to_add": 5},
                    ]
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_011",
        instruction=(
            "You are Leah Gomez from Finance Ops. In UAT, Alice Johnson reports that her delivered order 9016 (4K Webcam) might have been overpriced. "
            "You run a retail price-protection check by comparing today’s pricebook '1' pricing to what she was charged, and record the result as a Medium case "
            "'Price-protection inquiry'. "
        ),
        actions=[
            Action(name="get_order_details_by_id", kwargs={"order_id": "9016"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9016"}),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1018", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1018", "quantity": 1, "price": 199.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Price-protection inquiry",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_012",
        instruction=(
            "You are Jordan Hay from Sales. In UAT, you give Jane Smith a quick B2B price on one 'USB-C Hub' for Global Tech Inc. "
            "and close out a Low case 'Pricing Clarification' once the subtotal is confirmed. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Pricing Clarification",
                    "priority": "Low",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 1, "price": 60.0}]},
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_013",
        instruction=(
            "You are Chloe Davis from Retail Support. In UAT, you want a quick retail quote on your customer record "
            "(use contact 211 on account 110): price two '4K Webcam' (product 1018) from retail pricebook '1', "
            "then log a Low-priority 'Quote Prepared' case linked to that contact and account."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Chloe", "last_name": "Davis"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1018", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1018", "quantity": 2, "price": 199.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "211",
                    "account_id": "110",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_014",
        instruction=(
            "You compare pricebook '1' vs pricebook '2' for 'ProBook X15' at quantity 1, compute both "
            "subtotals, and then log a low priority Quote case for John Doe to record that the "
            "comparison was completed. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1500.0}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1250.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_015",
        instruction=(
            "You are Alex Chen from Customer Care. In UAT, you log a Medium case 'Address Update' for Emily White at Innovate Solutions, "
            "standardize her address to '456 Innovation Ave, Suite 900', and include a quick B2B snapshot for one 'USB-C Hub' so Sales sees the current unit price."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Address Update",
                    "priority": "Medium",
                },
            ),
            Action(
                name="update_street_address",
                kwargs={
                    "account_id": "102",
                    "new_shipping_street": "456 Innovation Ave, Suite 900",
                    "new_billing_street": "456 Innovation Ave, Suite 900",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 1, "price": 60.0}]},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_016",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, you bump the Digital Commerce cache partition for external cache to 'v2' so promo and catalog changes cut over cleanly, "
            "warm metadata, and then prove pricing against live data. You set 'CacheAPI.ExternalSystemPartitionKey' to 'v2', run 'Load API Metadata' and 'Populate Cache Job', "
            "then quote five 'USB-C Hub' from pricebook '2' with 'WINTER20' to confirm the path is working under version 'v2'."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemPartitionKey",
                    "value": "v2",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Populate Cache Job"}
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "USB-C Hub", "quantity": 5}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_017",
        instruction=(
            "You are Dana Patel from Support. In UAT, you want a quick retail reorder quote for Alice Johnson based on her most recent Delivered order. "
            "You identify her latest delivered order from history, reprice the same item at retail using pricebook '1', and log a Low-priority 'Quote Prepared' case "
            "linked to her contact and account only — do not attach the order to the case."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Alice", "last_name": "Johnson"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(name="get_orders_by_contact_id", kwargs={"contact_id": "204"}),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9016"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9016"}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1018", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1018", "quantity": 1, "price": 199.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_018",
        instruction=(
            "You are Leah Gomez from Customer Care. In UAT, Alice Johnson asks for an exchange estimate so she knows the expected amount before approval. "
            "You price one 'Branded T-Shirt (L)' and one 'Wireless Mouse' at retail and log a Medium case 'Exchange Estimate Logged'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Alice", "last_name": "Johnson"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "103"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Branded T-Shirt (L)", "Wireless Mouse"]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1004", "pricebook_id": "1"},
                        {"product_id": "1003", "pricebook_id": "1"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1004", "quantity": 1, "price": 25.0},
                        {"product_id": "1003", "quantity": 1, "price": 40.0},
                    ]
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Exchange Estimate Logged",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_019",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, Emily White asks to rebuild her B2B cart with a simple accessories bundle for a PO. "
            "You clear her cart, add three 'USB-C Hub' and one 'Mechanical Keyboard', and verify availability."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
            Action(name="clear_cart", kwargs={"cart_id": "701"}),
            Action(
                name="get_products_by_names", kwargs={"names": ["USB-C Hub", "Mechanical Keyboard"]}
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1002", "required_quantity": 3},
                        {"product_id": "1017", "required_quantity": 1},
                    ]
                },
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={
                    "cart_id": "701",
                    "items": [
                        {"product_id": "1002", "quantity": 3},
                        {"product_id": "1017", "quantity": 1},
                    ],
                },
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "701"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_020",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, Emily White asks for a clean B2B cart and a quick bundle quote for a PO. "
            "You rebuild her cart so it contains exactly 4 'USB-C Hub' and 2 'Wireless Mouse' and provide an itemized B2B subtotal so Purchasing can attach it to the PO."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub", "Wireless Mouse"]}),
            Action(name="clear_cart", kwargs={"cart_id": "701"}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1002", "required_quantity": 4},
                        {"product_id": "1003", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={
                    "cart_id": "701",
                    "items": [
                        {"product_id": "1002", "quantity": 4},
                        {"product_id": "1003", "quantity": 2},
                    ],
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1002", "pricebook_id": "2"},
                        {"product_id": "1003", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1002", "quantity": 4, "price": 60.0},
                        {"product_id": "1003", "quantity": 2, "price": 32.0},
                    ]
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_021",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, you want a fast pre-send sanity check for Global Tech Inc—"
            "price ten 'USB-C Hub' from pricebook '2', apply 'WINTER20', and open a Low priority quote case for John Doe so Sales has a record."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "USB-C Hub", "quantity": 10}],
                    "offer_code": "WINTER20",
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_022",
        instruction=(
            "You are Alex Morgan from Platform Security. In UAT, you want the Redis ingress standardized without changing behavior. "
            "You want rule 'sgr-fedcba9876543210f' to keep CIDR '10.0.5.0/24', set the base text to 'Redis – UAT app tier', and append exactly one ' [UAT]'. "
            "You want an inventory in the middle to document progress, then you want the final rule confirmed."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_023",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, marketing needs a sanity check on a limited-time code. "
            "You register the fixed $50 code 'FLASH50', confirm it correctly discounts a 75 subtotal, then deactivate it and verify it no longer applies."
        ),
        actions=[
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "FLASH50",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 50,
                },
            ),
            Action(name="get_offer_details", kwargs={"offer_id": "offer_5"}),
            Action(name="calculate_discount_flat", kwargs={"subtotal": 75, "discount_amount": 50}),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 75, "offer_code": "FLASH50"}
            ),
            Action(name="deactivate_offer", kwargs={"offer_code": "FLASH50"}),
            Action(name="get_offer_details", kwargs={"offer_id": "offer_5"}),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 75, "offer_code": "FLASH50"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_024",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, you clean Sandra Dee’s cart so fulfillment isn’t blocked by out-of-stock items. "
            "You leave only 'Ergo Laptop Stand' at quantity 2, remove 'Branded Water Bottle', and report the remaining item and the removed product id."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Sandra", "last_name": "Dee"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Ergo Laptop Stand", "Branded Water Bottle"]},
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "208"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "703", "items": [{"product_id": "1010", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "703", "product_ids": ["1012"]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_025",
        instruction=(
            "You are Sam Lee from Cloud Platform. In UAT, CAB wants a before/after for a Redis ingress cleanup. "
            "You take an inventory of current security-group rules to establish the baseline, fetch rule 'sgr-fedcba9876543210f', "
            "create an ingress change plan to ensure a single 6379/TCP from '10.0.5.0/24' with base 'Redis – UAT app tier' and exactly one ' [UAT]', "
            "apply all plan steps, then fetch the rule again so the final state is documented."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_026",
        instruction=(
            "You want to process a return for Alice Johnson’s delivered order 9001: you return the "
            "'Branded T-Shirt (L)' line and you **put that unit back into inventory**, open a 'Return Requested' case "
            "(Low), set the order status to 'Returned', and resolve the case."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Alice", "last_name": "Johnson"}
            ),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9001"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9001"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "204",
                    "account_id": "103",
                    "order_id": "9001",
                    "subject": "Return Requested",
                    "priority": "Low",
                },
            ),
            Action(
                name="add_stock_quantities",
                kwargs={"items": [{"product_id": "1004", "quantity_to_add": 1}]},
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9001", "new_status": "Returned"}
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_027",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, you want a retail reorder quote for Alice Johnson based on her most recent delivered order "
            "so pricing is consistent. You find her latest delivered order, price from pricebook '1' for the same items, "
            "compute the subtotal and round to the integer, call it x, and open a low-priority 'Quote Prepared [subsitute_x_in]' case. "
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Alice", "last_name": "Johnson"}
            ),
            Action(name="get_orders_by_contact_id", kwargs={"contact_id": "204"}),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9016"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9016"}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1018", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1018", "quantity": 1, "price": 199.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "204",
                    "account_id": "103",
                    "subject": "Quote Prepared [199]",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_028",
        instruction=(
            "You want a B2B quick quote for Emily White for one 'Wireless Mouse' and then open and resolve a low-priority case. "
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 1, "price": 32.0}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1003", "required_quantity": 1}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_029",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, product marketing wants a crisp snapshot to justify B2B contract rates on 'ProBook X15'. "
            "Price once from pricebook '1' and once from B2B pricebook '2' at quantity 1. "
            "Create a Low-priority case using Nora Patel as a contact and record it on her account."
        ),
        actions=[
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1500.0}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1250.0}]},
            ),
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_030",
        instruction=(
            "You’re in UAT doing a fast promo check for Jane Smith using the returned contact and account: price one 'Wireless Mouse' from pricebook '2' "
            "to get subtotal 32.0, apply WINTER20 to get total 25.6, verify at least one unit is in stock so the quote is realistic, "
            "then open a Low case with subject exactly 'Promo Price Check – Wireless Mouse: subtotal 32.0, total 25.6'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 1, "price": 32.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 32.0, "offer_code": "WINTER20"}
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1003", "required_quantity": 1}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Promo Price Check – Wireless Mouse: subtotal 32.0, total 25.6",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_031",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, Kevin Lee asks you to clean his cart and confirm it’s usable. "
            "You remove 'Server Rack Mount Kit (10-Pack)' (product 1008), add one 'USB-C Hub' briefly to validate the flow, then clear the cart and log a Low case 'Cart Cleaned'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "210"}),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "704", "product_ids": ["1008"]},
            ),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="add_items_to_cart_batch",
                kwargs={"cart_id": "704", "items": [{"product_id": "1002", "quantity": 1}]},
            ),
            Action(name="clear_cart", kwargs={"cart_id": "704"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Cart Cleaned",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_032",
        instruction="You verify stock for Kevin Lee for ten 'Flash Sale Power Bank' and two 'Mechanical Keyboard', then open a case 'Stock Verified' (Low) summarizing the request and mark it Resolved.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Flash Sale Power Bank", "Mechanical Keyboard"]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1015", "required_quantity": 10},
                        {"product_id": "1017", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Stock Verified",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_033",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, Kevin Lee asks for a quick B2B bundle check on his cart. "
            "You reset his cart, add one 'USB-C Hub' and one 'Wireless Mouse', apply 'WINTER20', and provide a brief receipt."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "210"}),
            Action(name="clear_cart", kwargs={"cart_id": "704"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub", "Wireless Mouse"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1002", "required_quantity": 1},
                        {"product_id": "1003", "required_quantity": 1},
                    ]
                },
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={
                    "cart_id": "704",
                    "items": [
                        {"product_id": "1002", "quantity": 1},
                        {"product_id": "1003", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1002", "pricebook_id": "2"},
                        {"product_id": "1003", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1002", "quantity": 1, "price": 60.0},
                        {"product_id": "1003", "quantity": 1, "price": 32.0},
                    ]
                },
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 92.0, "offer_code": "WINTER20"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_034",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want to prove Digital Commerce auth and cache wiring: resolve the UAT org, "
            "build the connected-app bearer with client_id 'dcg-uat', persist the returned Authorization header into 'CacheAPI.ExternalSystemAuthHeader', "
            "set 'CacheAPI.EcommLogger' is_active to False, run 'Load API Metadata', then price ten 'USB-C Hub' from pricebook '2' with 'WINTER20'."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(
                name="set_trace_flag",
                kwargs={"org_id": "UAT", "flag_name": "CacheAPI.EcommLogger", "is_active": False},
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "USB-C Hub", "quantity": 10}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_035",
        instruction=(
            "You are Priya Rao from Customer Care. In UAT, Maria Garcia reported a mis-keyed shipping street for account 106 and contact id 207. "
            "Open a case 'Address Correction', update her B2C account to '888 Ocean View, Apt 2B', and include a quick retail price snapshot for one 'Wireless Mouse' so she knows the current rate."
        ),
        actions=[
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "207",
                    "account_id": "106",
                    "subject": "Address Correction",
                    "priority": "Medium",
                },
            ),
            Action(
                name="update_street_address",
                kwargs={
                    "account_id": "106",
                    "new_shipping_street": "888 Ocean View, Apt 2B",
                    "new_billing_street": "888 Ocean View, Apt 2B",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 1, "price": 40.0}]},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_036",
        instruction=(
            "You’re in UAT pricing a quick check for Jane Smith using the returned contact and account: price two 'ProBook X15' from pricebook '2' "
            "to get subtotal 2500.0, apply WINTER20 to get total 2000.0, open a Low case with subject exactly "
            "'Price Check – ProBook X15 x2: subtotal 2500.0, total 2000.0', and then resolve the case so the ledger shows completed follow-through."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 2, "price": 1250.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 2500.0, "offer_code": "WINTER20"},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Price Check – ProBook X15 x2: subtotal 2500.0, total 2000.0",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_037",
        instruction=(
            "You are Priya Shah from Platform. In UAT, you resolve the org, ensure the DCG connected app for client_id 'dcg-uat' exists with scopes ['api','refresh_token'], "
            "build a bearer for that app using the 18-char org id; the Authorization header returned is 'Bearer 000000000000083b'. "
            "You persist that exact header to CacheAPI.ExternalSystemAuthHeader using the org alias 'UAT', then warm 'Load API Metadata'. "
            "You list 'Wireless Mouse' and 'USB-C Hub' for quoting and price one 'Wireless Mouse' from pricebook '2' with WINTER20."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="ensure_connected_app",
                kwargs={
                    "org_id": "00D8d000000LmnopQRS",
                    "app_name": "DCG",
                    "client_id": "dcg-uat",
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse", "USB-C Hub"]}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "Wireless Mouse", "quantity": 1}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_038",
        instruction="For Nora Patel, you compute a retail subtotal for eight Flash Sale Power Banks, subtract $5, and record the result in a low-priority case 'Discount Math Checked'.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_account_by_id", kwargs={"account_id": "113"}),
            Action(name="get_products_by_names", kwargs={"names": ["Flash Sale Power Bank"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1015", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1015", "quantity": 8, "price": 19.99}]},
            ),
            Action(
                name="calculate_discount_flat", kwargs={"subtotal": 159.92, "discount_amount": 5}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Discount Math Checked",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_039",
        instruction=(
            "You are Alex Chen from Commerce Ops. In UAT, Nora Patel wants the Mechanical Keyboard removed from her cart so fulfillment doesn’t pick it by mistake. "
            "You remove the keyboard, show the final cart, and log a Low case 'Cart Cleanup Complete' and mark case Resolved."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "215"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "705"}),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "705", "product_ids": ["1017"]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "705"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Cart Cleanup Complete",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_040",
        instruction=(
            "You are Sam Lee from Cloud Platform. In DEV, you want the Redis ingress made compliant without breaking traffic. "
            "You want rule 'sgr-badbadbadbadbadbad' to keep its effective CIDR as '10.0.5.0/24', set the base text to 'Redis – restricted', and append exactly one ' [DEV]'. "
            "You want to take an inventory first, then you want to apply the plan in stages and confirm before and after."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_041",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, prove auth and cache wiring before quarter-end pricing. "
            "Build a bearer for the connected app 'dcg-uat' to verify connectivity, but store the literal string 'BearerComputed' "
            "in 'CacheAPI.ExternalSystemAuthHeader' (do not store the runtime bearer). Use the org alias 'UAT' for settings writes. "
            "Also set 'CacheAPI.ExternalSystemURL' to https://cache.uat.example/api, run 'Load API Metadata', then quote ten 'USB-C Hub' "
            "from pricebook '2' with WINTER20."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "BearerComputed",
                },
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemURL",
                    "value": "https://cache.uat.example/api",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "USB-C Hub", "quantity": 10}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_042",
        instruction=(
            "You are Dana Patel from Sales Ops. In UAT, you prepare a B2B quote for Susan Adams on her account: "
            "load 'Server Rack Mount Kit (10-Pack)' x4 and 'USB-C Hub' x5, price them from pricebook '2' (unit 450.0 and 60.0), "
            "calculate subtotal 2100.0, apply B2BVOLUME15 to show the discount, and open a Medium-priority case with subject exactly "
            "'B2B Quote – subtotal 2100.0 with B2BVOLUME15 applied'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Susan", "last_name": "Adams"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "112"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Server Rack Mount Kit (10-Pack)", "USB-C Hub"]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1008", "pricebook_id": "2"},
                        {"product_id": "1002", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1008", "quantity": 4, "price": 450.0},
                        {"product_id": "1002", "quantity": 5, "price": 60.0},
                    ]
                },
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 2100.0, "offer_code": "B2BVOLUME15"},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "213",
                    "account_id": "112",
                    "subject": "B2B Quote – subtotal 2100.0 with B2BVOLUME15 applied",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_043",
        instruction="You process a partial return for John Doe’s shipped order 9002: restock one 'USB-C Hub', open a case 'Return Requested' (Medium), recompute the returned subtotal, and resolve the case.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9002"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9002"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "order_id": "9002",
                    "subject": "Return Requested",
                    "priority": "Medium",
                },
            ),
            Action(
                name="add_stock_quantities",
                kwargs={"items": [{"product_id": "1002", "quantity_to_add": 1}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 1, "price": 60.0}]},
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_044",
        instruction=(
            "In UAT, standardize 'sgr-fedcba9876543210f': keep CIDR at 10.0.5.0/24, set base 'Redis – UAT app tier', "
            "append one ' [UAT]', then list current Redis rule IDs for audit."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_045",
        instruction=(
            "You are Dana Patel from Merch Ops. In UAT, tidy Nora Patel’s cart so quantities and OOS cleanup are correct. "
            "Verify stock for 'Mechanical Keyboard' at quantity two before committing, then make sure the existing keyboard line is set to quantity two. "
            "Remove 'Branded Water Bottle'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Mechanical Keyboard", "Branded Water Bottle"]},
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "215"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "705"}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1017", "required_quantity": 2}]},
            ),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "705", "items": [{"product_id": "1017", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "705", "product_ids": ["1012"]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "705"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_046",
        instruction=(
            "You are Leah Gomez from Finance Ops. In UAT, John Doe at Global Tech Inc is asking for a price match on two 'ProBook X15' "
            "against a verified competitor quote of $1,200 per unit. You price from B2B pricebook '2', apply a single flat concession of 100.0 "
            "to meet a matched total of 2,400.0, and record the approval as a Medium case 'Price Match Approved'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 2, "price": 1250.0}]},
            ),
            Action(
                name="calculate_discount_flat",
                kwargs={"subtotal": 2500.0, "discount_amount": 100.0},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Price Match Approved",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_047",
        instruction=(
            "You validate a retail promotion. You want a 15% code 'SPRING15'  to be available "
            "and confirmed by ID, you want its effect demonstrated on two 'ProBook X15' at retail pricing for Nora Patel. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_account_by_id", kwargs={"account_id": "113"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "SPRING15",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 15,
                },
            ),
            Action(name="get_offer_details", kwargs={"offer_id": "offer_5"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 2, "price": 1500.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 3000.0, "offer_code": "SPRING15"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_048",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, Kevin Lee asked for a bulk B2B estimate to attach to a PO: "
            "you confirm stock and compute a subtotal for 30 '1TB NVMe SSD' from pricebook 2, then log a Low case "
            "'Bulk Stock & Estimate Prepared' so Procurement can reference it."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1016", "required_quantity": 30}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 30, "price": 95.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Bulk Stock & Estimate Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_049",
        instruction=(
            "You are Sam Lee from Cloud Platform. In DEV, quarantine the Redis SG referenced by 'sgr-badbadbadbadbadbad': "
            "end state is one 6379/TCP from 10.0.5.0/24 with 'Redis – restricted' and exactly one ' [DEV]'; produce an "
            "inventory and then fetch the rule again to show its final state."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_050",
        instruction=(
            "You are Maria Garcia from Customer Care. In DEV, you confirm promo math for John Doe on his account: "
            "price ten 'USB-C Hub' from pricebook '2' (unit 60.0) for a subtotal of 600.0, apply WINTER20 to get 480.0, "
            "verify at least one unit is in stock so the quote is realistic, then open a Low-priority case with subject exactly "
            "'USB-C Hub x10 – subtotal 600.0, total 480.0'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 10, "price": 60.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 600.0, "offer_code": "WINTER20"}
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1002", "required_quantity": 1}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "USB-C Hub x10 – subtotal 600.0, total 480.0",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_051",
        instruction=(
            "You are Alex Chen from Customer Care. In UAT, Starlight Enterprises asked us to standardize their address and attach a quick B2B pricing snapshot "
            "for audit notes. You open a Medium case 'Address Update' on Kevin Lee’s contact, update the address to '555 Galaxy Blvd, Suite 20', "
            "then spot-check price and stock for one '1TB NVMe SSD' from pricebook '2' and resolve the case."
        ),
        actions=[
            Action(name="get_account_by_name", kwargs={"name": "Starlight Enterprises"}),
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Address Update",
                    "priority": "Medium",
                },
            ),
            Action(
                name="update_street_address",
                kwargs={
                    "account_id": "109",
                    "new_shipping_street": "555 Galaxy Blvd, Suite 20",
                    "new_billing_street": "555 Galaxy Blvd, Suite 20",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 1, "price": 95.0}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1016", "required_quantity": 1}]},
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_052",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, Innovate Solutions needs a quick B2B snapshot for a requisition for Emily White. "
            "First resolve Emily White, then open a Low-priority case titled 'Price Snapshot'. "
            "Capture the unit price for one 'USB-C Hub' from pricebook '2', and verify stock for quantity 1."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Price Snapshot",
                    "priority": "Low",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 1, "price": 60.0}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1002", "required_quantity": 1}]},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_053",
        instruction=(
            "You’re resolving a mistaken order for Mike Rivera. You want to look up Mike by name and operate on his returned account and order. "
            "You need tofetch order '9010' and its lines, cancel the order, restock the returned items from the order, "
            "and open a High-priority 'Ordered By Mistake' case on the same account and resolve it."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Mike", "last_name": "Rivera"}
            ),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9010"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9010"}),
            Action(
                name="add_stock_quantities",
                kwargs={
                    "items": [
                        {"product_id": "1005", "quantity_to_add": 1},
                        {"product_id": "1011", "quantity_to_add": 5},
                    ]
                },
            ),
            Action(
                name="update_order_status",
                kwargs={"order_id": "9010", "new_status": "Cancelled"},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "209",
                    "account_id": "108",
                    "subject": "Ordered By Mistake",
                    "priority": "High",
                    "order_id": "9010",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_054",
        instruction="You create a new fixed $5 promo code 'CLEARANCE5', confirm by ID, apply it to ten 'Flash Sale Power Bank', then deactivate it and confirm by ID.",
        actions=[
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "CLEARANCE5",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 5,
                },
            ),
            Action(name="get_offer_details", kwargs={"offer_id": "offer_5"}),
            Action(name="get_products_by_names", kwargs={"names": ["Flash Sale Power Bank"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1015", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1015", "quantity": 10, "price": 19.99}]},
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 199.9, "offer_code": "CLEARANCE5"},
            ),
            Action(name="deactivate_offer", kwargs={"offer_code": "CLEARANCE5"}),
            Action(name="get_offer_details", kwargs={"offer_id": "offer_5"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_055",
        instruction=(
            "You are Chloe Davis from Customer Care. In UAT, Maria Garcia found one wrong unit in Delivered order 9005. "
            "You wamt tp put one Wireless Mouse back into inventory, set the order to 'Returned', and file a Low-priority case titled "
            "exactly 'Partial Return - 1 item' (Unicode minus)."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9005"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9005"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="add_stock_quantities",
                kwargs={"items": [{"product_id": "1003", "quantity_to_add": 1}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "207",
                    "account_id": "106",
                    "order_id": "9005",
                    "subject": "Partial Return - 1 item",
                    "priority": "Low",
                },
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9005", "new_status": "Returned"}
            ),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9005"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_056",
        instruction="You restructure Sandra Dee’s cart: set 'Ergo Laptop Stand' to quantity 3, remove 'Branded Water Bottle', verify stock for the stand, and list the final items.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Sandra", "last_name": "Dee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "208"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "703", "items": [{"product_id": "1010", "new_quantity": 3}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "703", "product_ids": ["1012"]},
            ),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Ergo Laptop Stand", "Branded Water Bottle"]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1010", "required_quantity": 3}]},
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_057",
        instruction=(
            "You’re in UAT proving auth and pricing. You resolve the UAT org, ensure the connected app named 'DCG' with client_id 'dcg-uat' exists with scopes ['api','refresh_token'], "
            "then you set CacheAPI.ExternalSystemAuthHeader to the literal value 'BearerComputed'. "
            "You warm 'Load API Metadata' and then price one 'Wireless Mouse' from pricebook '2' with WINTER20."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="ensure_connected_app",
                kwargs={
                    "org_id": "00D8d000000LmnopQRS",
                    "app_name": "DCG",
                    "client_id": "dcg-uat",
                    "oauth_scopes": ["api", "refresh_token"],
                },
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "BearerComputed",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "Wireless Mouse", "quantity": 1}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_058",
        instruction=(
            "You want to process a full return for delivered order 9005: you restock the items from that order "
            "and you mark the order as 'Cancelled' so the system reflects the return via a supported status."
        ),
        actions=[
            Action(name="get_order_details_by_id", kwargs={"order_id": "9005"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9005"}),
            Action(
                name="add_stock_quantities",
                kwargs={
                    "items": [
                        {"product_id": "1006", "quantity_to_add": 2},
                        {"product_id": "1003", "quantity_to_add": 1},
                    ]
                },
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9005", "new_status": "Cancelled"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_059",
        instruction="You want a B2B quote for John Doe for six ProBook X15, confirm the 10% discount math, log the result in a low-priority case titled 'B2B Math Check', and resolve the case.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 6, "price": 1250.0}]},
            ),
            Action(
                name="calculate_discount_percent",
                kwargs={"subtotal": 7500.0, "discount_percent": 10},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "B2B Math Check",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_060",
        instruction=(
            "You are Alex Chen from Customer Care. In UAT, you perform a quick retail pricing check for Maria Garcia on one 'Wireless Mouse' "
            "and document the result by opening and resolving a Medium case titled 'Retail Price Check'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "106"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 1, "price": 40.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "207",
                    "account_id": "106",
                    "subject": "Retail Price Check",
                    "priority": "Medium",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_061",
        instruction=(
            "You are Dana Patel from Platform. In UAT, refresh subnet group 'esg-uat-1' description to "
            "'Subnets for UAT caches [REVIEWED 2025-08-10]'. Then harden Redis using rule 'sgr-fedcba9876543210f' to a single "
            "'10.0.5.0/24' 6379/TCP with description 'Redis – UAT app tier' and append one ' [UAT]'. "
            "Confirm the final rule."
        ),
        actions=[
            Action(
                name="update_subnet_group_description",
                kwargs={
                    "subnet_group_id": "esg-uat-1",
                    "new_description": "Subnets for UAT caches [REVIEWED 2025-08-10]",
                },
            ),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_062",
        instruction=(
            "You’re in UAT and you want to preview the 'Q4SAVE10' 10% promo on one 'ProBook X15' at B2B pricing. "
            "You create the 'Q4SAVE10' code **before any pricing**, then price from pricebook '2', compute the subtotal, apply 'Q4SAVE10', "
            "verify availability for one unit, and finally deactivate the code."
        ),
        actions=[
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "Q4SAVE10",
                    "discount_type": "PERCENTAGE",
                    "discount_value": 10,
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1250.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 1250.0, "offer_code": "Q4SAVE10"},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1001", "required_quantity": 1}]},
            ),
            Action(name="deactivate_offer", kwargs={"offer_code": "Q4SAVE10"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_063",
        instruction=(
            "You are Maya Zhou from Platform Security. In UAT, you want Digital Commerce calls authenticated and quiet. "
            "Compute the Bearer for 'dcg-uat', store that exact value in CacheAPI.ExternalSystemAuthHeader, run 'Load API Metadata', "
            "disable CacheAPI.EcommLogger using False, and then prove pricing with a 1-unit quote of 'Mechanical Keyboard' "
            "from pricebook '1' using 'WELCOME5'."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="set_trace_flag",
                kwargs={"org_id": "UAT", "flag_name": "CacheAPI.EcommLogger", "is_active": False},
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "1",
                    "items_by_name": [{"name": "Mechanical Keyboard", "quantity": 1}],
                    "offer_code": "WELCOME5",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_064",
        instruction=(
            "You are Priya Rao from Infra Ops. In UAT (dev SG), you standardize Redis ingress with an auditable baseline. "
            "You first list the current security-group rules, then fetch 'sgr-badbadbadbadbadbad', create the ingress plan for a single 6379/TCP from '10.0.5.0/24' "
            "with base 'Redis – restricted' and one ' [DEV]', apply all steps, and finish with an inventory so reviewers see the standardized state."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_065",
        instruction=(
            "You’re updating Starlight Enterprises and capturing a quick B2B price snapshot for Kevin Lee. "
            "You want to open a Medium case titled 'Address Update' before you touch the account, change both shipping and billing to "
            "'555 Galaxy Blvd, Suite 100', then price one 1TB NVMe SSD at contract rates and close the case once the snapshot is captured."
        ),
        actions=[
            Action(name="get_account_by_name", kwargs={"name": "Starlight Enterprises"}),
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Address Update",
                    "priority": "Medium",
                },
            ),
            Action(
                name="update_street_address",
                kwargs={
                    "account_id": "109",
                    "new_shipping_street": "555 Galaxy Blvd, Suite 100",
                    "new_billing_street": "555 Galaxy Blvd, Suite 100",
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 1, "price": 95.0}]},
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_066",
        instruction="You create a case and restructure Sandra Dee’s cart: set 'Ergo Laptop Stand' to quantity 2, remove 'Branded Water Bottle', and resolve a case 'Cart Ready' (Low).",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Sandra", "last_name": "Dee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "208"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "208",
                    "account_id": "107",
                    "subject": "Cart Ready",
                    "priority": "Low",
                },
            ),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "703", "items": [{"product_id": "1010", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "703", "product_ids": ["1012"]},
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_067",
        instruction=(
            "You restock one 'USB-C Hub (Deluxe)' from Maria Garcia’s delivered order 9005; if the exact variant is not in the catalog, "
            "use the canonical 'USB-C Hub'. Set the order status to Returned and record a low-priority case titled 'Partial Return - 1 item'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Maria", "last_name": "Garcia"}
            ),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9005"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9005"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "207",
                    "account_id": "106",
                    "order_id": "9005",
                    "subject": "Partial Return - 1 item",
                    "priority": "Low",
                },
            ),
            Action(
                name="add_stock_quantities",
                kwargs={"items": [{"product_id": "1002", "quantity_to_add": 1}]},
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9005", "new_status": "Returned"}
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_068",
        instruction=(
            "You are Priya Rao from Infra Ops. In DEV, you want to standardize the Redis ingress description while preserving behavior. "
            "You want rule 'sgr-badbadbadbadbadbad' to use base 'Redis – restricted', keep the current CIDR '10.0.5.0/24', and append exactly one ' [DEV]' to base. "
            "You want the plan created and fully applied, and then you want an inventory recorded."
        ),
        actions=[
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [DEV]",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_069",
        instruction=(
            "You need a clean before/after for dev Redis on 'sgr-badbadbadbadbadbad': take a 'before' inventory, "
            "plan for a single 6379/TCP from 10.0.5.0/24 with DEV tag, apply steps, then list the resulting rules."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_070",
        instruction=(
            "You are Alex Chen from Customer Care. In UAT, Marketing asked for a clean retail pilot on keyboard attach. "
            "Clear Kevin Lee’s cart, create promo 'GEAR25' ($25 fixed), build a Bearer for the dcg-uat app and upsert it into CacheAPI.ExternalSystemAuthHeader for UAT, "
            "run 'Load API Metadata' to refresh Digital Commerce so the new code is visible, verify stock for two Mechanical Keyboard units, add them to Kevin’s cart, "
            "compute the retail subtotal from pricebook '1', apply 'GEAR25', then retire the code when done."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "210"}),
            Action(name="clear_cart", kwargs={"cart_id": "704"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "GEAR25",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 25,
                },
            ),
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(name="get_products_by_names", kwargs={"names": ["Mechanical Keyboard"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1017", "pricebook_id": "1"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1017", "required_quantity": 2}]},
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={"cart_id": "704", "items": [{"product_id": "1017", "quantity": 2}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1017", "quantity": 2, "price": 150.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 300.0, "offer_code": "GEAR25"}
            ),
            Action(name="deactivate_offer", kwargs={"offer_code": "GEAR25"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_071",
        instruction="You prepare a B2B bulk quote for John Doe for three 'Server Rack Mount Kit (10-Pack)' and one 'ProBook X15', evaluate 'B2BVOLUME15', and open and resolve a case 'Bulk Quote Evaluated' (Low).",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Server Rack Mount Kit (10-Pack)", "ProBook X15"]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1008", "pricebook_id": "2"},
                        {"product_id": "1001", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1008", "quantity": 3, "price": 450.0},
                        {"product_id": "1001", "quantity": 1, "price": 1250.0},
                    ]
                },
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 2600.0, "offer_code": "B2BVOLUME15"},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Bulk Quote Evaluated",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_072",
        instruction=(
            "You compute a deterministic B2B price check for Kevin Lee at Starlight. "
            "You want to resolve contact/account, get the current cart, look up the product IDs, "
            "verify stock for two 'ProBook X15'. You think you should then clear the cart to ensure it is empty, "
            "add two units to the cart, get the price (pricebook '2'), calculate the subtotal, and apply 'WINTER20'."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "210"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1001", "required_quantity": 2}]},
            ),
            Action(name="clear_cart", kwargs={"cart_id": "704"}),
            Action(
                name="add_items_to_cart_batch",
                kwargs={"cart_id": "704", "items": [{"product_id": "1001", "quantity": 2}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 2, "price": 1250.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 2500.0, "offer_code": "WINTER20"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_073",
        instruction=(
            "You’re in UAT and you want Nora Patel’s cart to reflect two Mechanical Keyboards without touching unrelated lines. "
            "You make sure the existing Mechanical Keyboard line is set to quantity 2 — no clearing the cart and no duplicate adds. "
            "Then you figure the retail (pricebook '1') subtotal together with one Branded Water Bottle for pricing only "
            "(it’s fine if it’s out of stock; you’re not changing inventory or cart contents for the bottle)."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_account_by_id", kwargs={"account_id": "113"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "215"}),
            Action(
                name="get_products_by_names",
                kwargs={"names": ["Mechanical Keyboard", "Branded Water Bottle"]},
            ),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "705", "items": [{"product_id": "1017", "new_quantity": 2}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1017", "pricebook_id": "1"},
                        {"product_id": "1012", "pricebook_id": "1"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1017", "quantity": 2, "price": 150.0},
                        {"product_id": "1012", "quantity": 1, "price": 15.0},
                    ]
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_074",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want the $10 welcome offer 'WELCOME10' validated on two 'Wireless Mouse' so fixed-amount math is proven before rollout. "
            "You work on Nora Patel, register 'WELCOME10' as a $10 fixed-amount code, run job 'Load API Metadata', price from pricebook '1' for quantity 2, apply the code, and return audit values."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "WELCOME10",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 10,
                },
            ),
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "1"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1003", "required_quantity": 2}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 2, "price": 40.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 80.0, "offer_code": "WELCOME10"}
            ),
        ],
        outputs=[
            '"subtotal": 80.0',
            '"code": "WELCOME10"',
            '"discount": 10.0',
            '"total": 70.0',
        ],
    ),
    Task(
        annotator="v1",
        user_id="task_075",
        instruction=(
            "You want to clean up a mistaken purchase for Mike Rivera — you confirm Mike first "
            "then you cancel order '9010', restock its lines, and resolve a "
            "High-priority 'Ordered By Mistake' case."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Mike", "last_name": "Rivera"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "108"}),
            Action(name="get_order_details_by_id", kwargs={"order_id": "9010"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9010"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "209",
                    "account_id": "108",
                    "order_id": "9010",
                    "subject": "Ordered By Mistake",
                    "priority": "High",
                },
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9010", "new_status": "Cancelled"}
            ),
            Action(
                name="add_stock_quantities",
                kwargs={
                    "items": [
                        {"product_id": "1005", "quantity_to_add": 1},
                        {"product_id": "1011", "quantity_to_add": 5},
                    ]
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_076",
        instruction=(
            "You want to update Redis using rule 'sgr-fedcba9876543210f' by setting the description to the exact string "
            "'Redis – UAT app tier [APPROVED] peer-reviewed 2025-08-10' and keeping the existing CIDR. "
            "Do not add any environment brackets beyond that text. Confirm the updated rule."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [APPROVED] peer-reviewed 2025-08-10",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_077",
        instruction=(
            "You are Priya Shah from Platform. In UAT, align Redis ingress on 'sgr-fedcba9876543210f' to one "
            "6379/TCP from 10.0.5.0/24 with base 'Redis – UAT app tier' and exactly one ' [UAT]': fetch rule, "
            "plan, apply, capture an inventory mid-stream, then fetch the rule again to confirm the final state."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_078",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want to prove a small B2B incentive for Global Tech Inc end-to-end. "
            "You create the 5% code 'SMALL5', refresh metadata so the platform recognizes it, verify stock for five 'USB-C Hub', price at B2B rates from pricebook '2', apply the code, and then disable it."
        ),
        actions=[
            Action(
                name="create_new_offer",
                kwargs={"offer_code": "SMALL5", "discount_type": "PERCENTAGE", "discount_value": 5},
            ),
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1002", "required_quantity": 5}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 5, "price": 60.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 300.0, "offer_code": "SMALL5"}
            ),
            Action(name="deactivate_offer", kwargs={"offer_code": "SMALL5"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_079",
        instruction=(
            "You are Priya Shah from Platform. In DEV, you want to bring the Redis ingress description into compliance while preserving traffic. "
            "You want rule 'sgr-badbadbadbadbadbad' standardized to keep CIDR '10.0.5.0/24', use base 'Redis – restricted', and append exactly one ' [DEV]'. "
            "You want to observe the rule after the first write, record an inventory mid-stream, finish the plan, and then confirm the final rule."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="dc",
        user_id="task_080",
        instruction=(
            "You are Ava Morales from Sales Ops. In UAT, account 102 (Innovate Solutions) asked for a clean B2B quote that shows laptop + accessory savings. "
            "You want to retrieve the cart created by Emily White and clear leftovers. You should add to it one "
            "'ProBook X15' and one 'USB-C Hub', price both from pricebook '2', and apply 'WINTER20' so the combined discount is proven end-to-end. "
        ),
        actions=[
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
            Action(name="clear_cart", kwargs={"cart_id": "701"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15", "USB-C Hub"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1001", "required_quantity": 1},
                        {"product_id": "1002", "required_quantity": 1},
                    ]
                },
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={
                    "cart_id": "701",
                    "items": [
                        {"product_id": "1001", "quantity": 1},
                        {"product_id": "1002", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="get_price_of_product",
                kwargs={
                    "items": [
                        {"product_id": "1001", "pricebook_id": "2"},
                        {"product_id": "1002", "pricebook_id": "2"},
                    ]
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={
                    "items": [
                        {"product_id": "1001", "quantity": 1, "price": 1250.0},
                        {"product_id": "1002", "quantity": 1, "price": 60.0},
                    ]
                },
            ),
            Action(
                name="apply_offer_to_subtotal",
                kwargs={"subtotal": 1310.0, "offer_code": "WINTER20"},
            ),
        ],
        outputs=[
            '"subtotal": 1310.0',
            '"code": "WINTER20"',
            '"discount": 262.0',
            '"total": 1048.0',
        ],
    ),
    Task(
        annotator="v1",
        user_id="task_081",
        instruction=(
            "You are Jordan Kim from Commerce Ops. In UAT, validate a mixed B2B bundle: "
            "price three 'USB-C Hub' and two 'Wireless Mouse' from pricebook '2' with 'WINTER20'. "
            "If pricing seems stale, refresh metadata first. After pricing, log a Low-priority "
            "'Bundle Price Audit' case for Jane Smith."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub", "Wireless Mouse"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={
                    "items": [
                        {"product_id": "1002", "required_quantity": 3},
                        {"product_id": "1003", "required_quantity": 2},
                    ]
                },
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [
                        {"name": "USB-C Hub", "quantity": 3},
                        {"name": "Wireless Mouse", "quantity": 2},
                    ],
                    "offer_code": "WINTER20",
                },
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Bundle Price Audit",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_082",
        instruction=(
            "You are Priya Rao from Sales Engineering. In UAT, you confirm Innovate Solutions’ employee Emily White contracted 10% renewal discount on one "
            "'ProBook X15' without using a public promo code. You price it from B2B pricebook '2', apply a 10% internal concession, "
            "and log a Low case titled 'Contract Discount Confirmed'."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "102"}),
            Action(name="get_products_by_names", kwargs={"names": ["ProBook X15"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1001", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1001", "quantity": 1, "price": 1250.0}]},
            ),
            Action(
                name="calculate_discount_percent",
                kwargs={"subtotal": 1250.0, "discount_percent": 10},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "203",
                    "account_id": "102",
                    "subject": "Contract Discount Confirmed",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="aws",
        user_id="task_083",
        instruction=(
            "You want the UAT group's Redis standardized using UAT rule 'sgr-fedcba9876543210f': "
            "a single '10.0.5.0/24' ingress with the description set to 'Redis – UAT app tier', then append exactly one ' [UAT]'. "
            "Return the final rule."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_084",
        instruction="For Sandra Dee, you want to set the Ergo Laptop Stand to two units and remove the Branded Water Bottle. You want to show the final cart and confirm stock for the stand. Log a low-priority case 'Cart Ready'.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Sandra", "last_name": "Dee"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "208"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "703"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "703", "items": [{"product_id": "1010", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "703", "product_ids": ["1012"]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1010", "required_quantity": 2}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "208",
                    "account_id": "107",
                    "subject": "Cart Ready",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_085",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, you want a B2B bulk quote for Starlight Enterprises validated so twenty '1TB NVMe SSD' "
            "price correctly before sending. You confirm recent orders for Kevin Lee first, then verify stock, price from pricebook '2', "
            "compute the subtotal, and track it with a low-priority case 'Bulk Stock Verified' resolved on completion."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Kevin", "last_name": "Lee"}),
            Action(name="get_orders_by_contact_id", kwargs={"contact_id": "210"}),
            Action(name="get_account_by_id", kwargs={"account_id": "109"}),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1016", "required_quantity": 20}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 20, "price": 95.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "210",
                    "account_id": "109",
                    "subject": "Bulk Stock Verified",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_086",
        instruction=(
            "You are Emily White in UAT reviewing cart UX. You fetch your cart, clear it for a fresh start, confirm the 'Wireless Mouse' exists and has stock, "
            "then add one unit to your empty cart and return the current contents."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Emily", "last_name": "White"}
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
            Action(name="clear_cart", kwargs={"cart_id": "701"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1003", "required_quantity": 1}]},
            ),
            Action(
                name="add_items_to_cart_batch",
                kwargs={"cart_id": "701", "items": [{"product_id": "1003", "quantity": 1}]},
            ),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "203"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_087",
        instruction=(
            "You are Alex Morgan from Platform Security. In UAT, you want an auditable baseline-to-final trail for the Redis rule. "
            "You record an initial inventory of security-group rules, fetch 'sgr-fedcba9876543210f', plan the standardization to one 6379/TCP from '10.0.5.0/24' "
            "with base text 'Redis – UAT app tier' and exactly one ' [UAT]', apply all steps, re-fetch the rule to confirm, and then list inventory again "
            "so reviewers see the post-change set."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_088",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want discounting to pick the single best code so shoppers get the lowest total. "
            "You look up the UAT org, register TEAM15 as a fixed-amount code with discount_value 15.0, then build a bearer for the 'dcg-uat' app using the 18-char org id you just looked up; "
            "the Authorization header returned is 'Bearer 000000000000083b'. When persisting CacheAPI settings you address the org by its environment alias 'UAT' and write that exact header. "
            "You warm 'Load API Metadata'. Then you compare TEAM15 versus WINTER20 on two 'Wireless Mouse' from pricebook '1' and return which wins."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "TEAM15",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 15.0,
                },
            ),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "1",
                    "items_by_name": [{"name": "Wireless Mouse", "quantity": 2}],
                    "offer_code": "TEAM15",
                },
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "1",
                    "items_by_name": [{"name": "Wireless Mouse", "quantity": 2}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_089",
        instruction=(
            "You are Chloe Davis from Retail Support. In UAT, prepare a quick retail quote for your own record "
            "(contact 211 under account 110): price two '1TB NVMe SSD' from pricebook '1' with 'WELCOME5' applied. "
            "Record the result in a Medium-priority case titled 'Retail Quote Generated' on that contact and account."
        ),
        actions=[
            Action(
                name="get_contact_by_name", kwargs={"first_name": "Chloe", "last_name": "Davis"}
            ),
            Action(name="get_account_by_id", kwargs={"account_id": "110"}),
            Action(name="get_products_by_names", kwargs={"names": ["1TB NVMe SSD"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1016", "pricebook_id": "1"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1016", "required_quantity": 2}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1016", "quantity": 2, "price": 120.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 240.0, "offer_code": "WELCOME5"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "211",
                    "account_id": "110",
                    "subject": "Retail Quote Generated",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_090",
        instruction=(
            "You are Sam Lee from Cloud Platform. In UAT, you want to refresh the subnet narrative and then standardize the Redis ingress. "
            "You want to set subnet group 'esg-uat-1' description to 'Subnets for UAT caches [REVIEWED 2025-08-10]'. "
            "Then you want rule 'sgr-fedcba9876543210f' to keep CIDR '10.0.5.0/24', set base 'Redis – UAT app tier', and append exactly one ' [UAT]'. "
            "Finally, you want an inventory to capture the end state."
        ),
        actions=[
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="update_subnet_group_description",
                kwargs={
                    "subnet_group_id": "esg-uat-1",
                    "new_description": "Subnets for UAT caches [REVIEWED 2025-08-10]",
                },
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_091",
        instruction=(
            "You are Dana Patel from Platform. In UAT, you want to refresh subnet documentation and then standardize Redis ingress. "
            "You want subnet group 'esg-uat-1' description set to 'Subnets for UAT caches [REVIEWED]'. "
            "Then you want rule 'sgr-fedcba9876543210f' to keep CIDR '10.0.5.0/24', use base 'Redis – UAT app tier', and append exactly one ' [UAT]'. "
            "You want to capture an inventory at the end."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="update_subnet_group_description",
                kwargs={
                    "subnet_group_id": "esg-uat-1",
                    "new_description": "Subnets for UAT caches [REVIEWED]",
                },
            ),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-fedcba9876543210f",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – UAT app tier [UAT]",
                    "env_tag": "UAT",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-fedcba9876543210f"}
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_092",
        instruction=(
            "You are Dana Patel from Pricing. In UAT, you want to demonstrate a simple fixed-amount code for "
            "John Doe (contact 201) at Global Tech Inc (account 101) using B2B rates. "
            "Create 'MOUSE20' for one 'Wireless Mouse', refresh metadata so pricing picks it up, verify stock, "
            "price from pricebook '2', apply the code, and open a Medium-priority case titled 'MOUSE20 Applied' "
            "on that contact and account."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(
                name="create_new_offer",
                kwargs={
                    "offer_code": "MOUSE20",
                    "discount_type": "FIXED_AMOUNT",
                    "discount_value": 20,
                },
            ),
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "2"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1003", "required_quantity": 1}]},
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [
                      {
                        "name": "Wireless Mouse",
                        "quantity": 1,
                    }
                ],
                    "offer_code": "MOUSE20",
                },
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 1, "price": 32.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 32.0, "offer_code": "MOUSE20"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "MOUSE20 Applied",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_093",
        instruction="You verify retail stock for Nora Patel for two 'Mechanical Keyboard', learn the retail subtotal to the integer, and log the result as a case with subject as 'Buy [substitue product name]' and priority 'Medium'.",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_products_by_names", kwargs={"names": ["Mechanical Keyboard"]}),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1017", "required_quantity": 2}]},
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1017", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1017", "quantity": 2, "price": 150.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Buy Mechanical Keyboard",
                    "priority": "Medium",
                },
            ),
        ],
        outputs=["300"],
    ),
    Task(
        annotator="v1",
        user_id="task_094",
        instruction=(
            "You are Alex Chen from Sales Ops. In UAT, Global Tech Inc needs an accessory-only price check for a PO attachment. "
            "Compute quote totals (no quote record) for Jane Smith (contact 202, account 101) for three 'USB-C Hub' from pricebook '2' "
            "so Procurement can see contract rates. Log a Low priority 'Quote Prepared' case."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(name="get_contact_by_name", kwargs={"first_name": "Jane", "last_name": "Smith"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1002", "pricebook_id": "2"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1002", "quantity": 3, "price": 60.0}]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "202",
                    "account_id": "101",
                    "subject": "Quote Prepared",
                    "priority": "Low",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_095",
        instruction=(
            "You are Sam Lee from Commerce Ops. In UAT, you want B2B pricing and promo application proven under a real Authorization header so staging mirrors production. "
            "You compute and store the Bearer for the dcg-uat connected app, refresh metadata, verify stock for one 'Server Rack Mount Kit (10-Pack)', then price from pricebook 2 with 'WINTER20'."
        ),
        actions=[
            Action(name="get_org_by_name", kwargs={"org_name": "UAT"}),
            Action(
                name="build_bearer_for_connected_app",
                kwargs={"org_id": "00D8d000000LmnopQRS", "client_id": "dcg-uat"},
            ),
            Action(
                name="upsert_custom_setting",
                kwargs={
                    "org_id": "UAT",
                    "setting_name": "CacheAPI.ExternalSystemAuthHeader",
                    "value": "Bearer 000000000000083b",
                },
            ),
            Action(name="run_cache_job", kwargs={"org_id": "UAT", "job_name": "Load API Metadata"}),
            Action(
                name="get_products_by_names", kwargs={"names": ["Server Rack Mount Kit (10-Pack)"]}
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1008", "required_quantity": 1}]},
            ),
            Action(
                name="price_and_apply_offer_by_names",
                kwargs={
                    "pricebook_id": "2",
                    "items_by_name": [{"name": "Server Rack Mount Kit (10-Pack)", "quantity": 1}],
                    "offer_code": "WINTER20",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_096",
        instruction=(
            "You tidy Nora Patel’s cart by setting 'Mechanical Keyboard' to quantity two and removing 'Branded Water Bottle'; "
            "when removing, use the product_id shown in the cart line items if it differs from the catalog id. "
            "Log a low-priority case titled 'Cart Tidy Completed'. "
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_cart_by_contact_id", kwargs={"contact_id": "215"}),
            Action(name="get_all_items_in_cart", kwargs={"cart_id": "705"}),
            Action(
                name="update_items_in_cart_batch",
                kwargs={"cart_id": "705", "items": [{"product_id": "1017", "new_quantity": 2}]},
            ),
            Action(
                name="remove_items_from_cart_batch",
                kwargs={"cart_id": "705", "product_ids": ["1019"]},
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Cart Tidy Completed",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_097",
        instruction=(
            "You complete a return for John Doe’s delivered order '9002' by restocking exactly the 'USB-C Hub' line and "
            "marking the order as 'Returned', then you open a high-priority case titled 'Return Completed'. Do not compute "
            "subtotals or perform pricing; only perform the reads needed to deterministically restock the correct product ID and finish the return."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_all_order_items_by_order_id", kwargs={"order_id": "9002"}),
            Action(name="get_products_by_names", kwargs={"names": ["USB-C Hub"]}),
            Action(
                name="add_stock_quantities",
                kwargs={"items": [{"product_id": "1002", "quantity_to_add": 1}]},
            ),
            Action(
                name="update_order_status", kwargs={"order_id": "9002", "new_status": "Returned"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Return Completed",
                    "priority": "High",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_098",
        instruction=(
            "You are Priya Shah from Platform. In DEV, you want to lock down the Redis perimeter text without changing connectivity so audit can proceed. "
            "You want rule 'sgr-badbadbadbadbadbad' to keep its current CIDR (10.0.5.0/24 after hardening), set the base to 'Redis – restricted', and append exactly one ' [DEV]'. "
            "You also want an inventory before and after to document the change."
        ),
        actions=[
            Action(name="inventory_security_group_rules", kwargs={}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(
                name="create_ingress_change_plan",
                kwargs={
                    "rule_id": "sgr-badbadbadbadbadbad",
                    "target_cidr": "10.0.5.0/24",
                    "final_description": "Redis – restricted [DEV]",
                    "env_tag": "DEV",
                },
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 0}),
            Action(
                name="get_security_group_rule_by_id", kwargs={"rule_id": "sgr-badbadbadbadbadbad"}
            ),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 1}),
            Action(name="apply_ingress_plan_step", kwargs={"plan_id": "ap-0001", "step_index": 2}),
            Action(name="inventory_security_group_rules", kwargs={}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_099",
        instruction=(
            "You open a case 'Retail Mouse Bundle' for Nora Patel, price four 'Wireless Mouse' at retail, apply 'WELCOME5', "
            "and resolve the case."
        ),
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "Nora", "last_name": "Patel"}),
            Action(name="get_account_by_id", kwargs={"account_id": "113"}),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "215",
                    "account_id": "113",
                    "subject": "Retail Mouse Bundle",
                    "priority": "Medium",
                },
            ),
            Action(name="get_products_by_names", kwargs={"names": ["Wireless Mouse"]}),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1003", "pricebook_id": "1"}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1003", "quantity": 4, "price": 40.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 160.0, "offer_code": "WELCOME5"}
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="v1",
        user_id="task_100",
        instruction="You compute a B2B subtotal for two 'Server Rack Mount Kit (10-Pack)' and apply 'WINTER20' for John Doe, then open and resolve a case 'Rack Kits Discounted' (Low).",
        actions=[
            Action(name="get_contact_by_name", kwargs={"first_name": "John", "last_name": "Doe"}),
            Action(name="get_account_by_id", kwargs={"account_id": "101"}),
            Action(
                name="get_products_by_names", kwargs={"names": ["Server Rack Mount Kit (10-Pack)"]}
            ),
            Action(
                name="get_price_of_product",
                kwargs={"items": [{"product_id": "1008", "pricebook_id": "2"}]},
            ),
            Action(
                name="verify_order_from_stock",
                kwargs={"items": [{"product_id": "1008", "required_quantity": 2}]},
            ),
            Action(
                name="calculate_sub_total_price",
                kwargs={"items": [{"product_id": "1008", "quantity": 2, "price": 450.0}]},
            ),
            Action(
                name="apply_offer_to_subtotal", kwargs={"subtotal": 900.0, "offer_code": "WINTER20"}
            ),
            Action(
                name="create_new_case",
                kwargs={
                    "contact_id": "201",
                    "account_id": "101",
                    "subject": "Rack Kits Discounted",
                    "priority": "Low",
                },
            ),
            Action(name="update_case_status", kwargs={"case_id": "case_9", "status": "Resolved"}),
        ],
        outputs=[],
    ),
]
