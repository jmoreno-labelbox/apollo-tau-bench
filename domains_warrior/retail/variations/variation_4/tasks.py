from calendar import c
from domains.dto import Action, Task

TASKS = [

    Task(
        annotator="0",
        user_id="V5TSK_USR_1",
        instruction=
                     (
                     "You're Lucas Brown with user_id lucas_brown_6720, a "
                     "premium customer from Chicago wanting to place a new "
                     "electronics order. You're interested in purchasing a "
                     "laptop and digital camera setup for your photography "
                     "business with a budget of $2000-3000 per item. The "
                     "laptop should have the following specifications: "
                     "17-inch display, Intel Core i7 processor, 32GB RAM, "
                     "black in color and 1TB SSD. The digital camera should "
                     "have at least 30MP resolution with 3x optical zoom and "
                     "a SD card slot. You need to search for available "
                     "laptops and cameras in your price range, validate "
                     "their availability. Once validated you will create an "
                     "order with your credit card as payment method."
                     ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lucas", "last_name": "Brown", "user_id": "lucas_brown_6720"}),
            Action(name="search_products_by_filter", kwargs={"category": "laptop", "min_price": 2000, "max_price": 3000,
                                                             "options": {
                                                               "screen size": "17-inch",
                                                                "processor": "i7",
                                                                "ram": "32GB",
                                                                "storage": "1TB SSD",
                                                                "color": "black"
                                                            }}),
            Action(name="search_products_by_filter", kwargs={"category": "digital camera", "min_price": 2000, "max_price": 3000,
                                                             "options": {
                                                                "resolution": "30MP",
                                                                "storage": "SD card",
                                                                "zoom": "3x"
                                                            }}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1684786391", "quantity": 1},
                    {"item_id": "1804581713", "quantity": 1}
                ]
            }),
            Action(name="create_order", kwargs={
                "user_id": "lucas_brown_6720",
                "items": [
                    {"item_id": "1684786391", "quantity": 1},
                    {"item_id": "1804581713", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card"]
            }),
        ],
        outputs=[
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_2",
        instruction=(
            "You're helping customer Chen Moore (user_id: chen_moore_6080) update their account profile and add a new payment method. "
            "The customer currently lives at 275 Cedar Avenue, Suite 148, Los Angeles, CA 91087, USA but wants to move to a new Los Angeles location at 456 Sunset Boulevard, Apt 12B, Los Angeles, CA 90028, USA. "
            "They want to add a gift card with a balance of $500, update their delivery address to the new Sunset Boulevard location, and verify their current order #W9205196 can be delivered to the new address at 456 Sunset Boulevard, Apt 12B, Los Angeles, CA 90028, USA. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="get_user_order_history", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="add_payment_method", kwargs={
                "user_id": "chen_moore_6080",
                "payment_type": "gift_card",
                "payment_details":{
                    "balance": 500.00
                }
            }),
            Action(name="update_user_profile", kwargs={
                "user_id": "chen_moore_6080",
                "profile_updates": {
                    "address": {
                        "address1": "456 Sunset Boulevard",
                        "address2": "Apt 12B",
                        "city": "Los Angeles",
                        "state": "CA",
                        "zip": "90028",
                        "country": "USA"
                    }
                }
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="update_delivery_address", kwargs={
                "user_id": "chen_moore_6080",
                "order_id": "#W9205196",
                "new_address": {
                    "address1": "456 Sunset Boulevard",
                    "address2": "Apt 12B",
                    "city": "Los Angeles",
                    "state": "CA",
                    "zip": "90028",
                    "country": "USA"
                }
            }),
        ],
        outputs=[
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_3",
        instruction=(
            "You're customer service representative handling a return request from Sofia Li (user_id: sofia_li_3261) who wants to return items from her processed order #W6874763. "
            "The customer received a damaged e-reader and an action camera that doesn't match the color she ordered. "
            "You need to validate her identity, check her order history, verify the order exists, process the return request, and update the order status to for return."
            "Additionally, you need to validate the shipping address and calculate the shipping cost for the return using the same courier that delivered the product."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Sofia", "last_name": "Li", "user_id": "sofia_li_3261"}),
            Action(name="get_user_order_history", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="get_purchased_items", kwargs={"user_id": "sofia_li_3261", "order_id": "#W6874763"}),
            Action(name="get_courier", kwargs={"tracking_id": "342513139974"}),
            Action(name="request_order_return", kwargs={
                "user_id": "sofia_li_3261",
                "order_id": "#W6874763",
                "return_items": [
                    {"item_id": "9494281769", "quantity": 1, "reason": "damaged"},
                    {"item_id": "6700049080", "quantity": 1, "reason": "wrong color"}
                ],
                "return_reason": "Damage and wrong color"
            }),

            Action(name="update_order_status", kwargs={"order_id": "#W6874763", "new_status": "for return"}),
            Action(name="validate_shipping_address", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 718.81, "courier_id": "#COU0003"}),
        ],
        outputs=[
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_4",
        instruction=(
            "You're Anya Garcia (user_id: anya_garcia_3271) living at 615 Laurel Lane, Suite 552, Philadelphia, PA 19036, USA. "
            "You want to buy a water bottle using your gift card and coffee maker using your credit card for your home office and get the cheapest option. "
            "You need to search for affordable options for both, validate the items are available, and create separate orders for each item."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"}),
            Action(name="verify_gift_card_balance", kwargs={
                "first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"
            }),
            Action(name="search_products_by_filter", kwargs={"category": "water bottle", "max_price": 51, "price_flag": "cheapest"}),
            Action(name="search_products_by_filter", kwargs={"category": "coffee maker", "price_flag": "cheapest"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},  # Water bottle $45.09
                    {"item_id": "1349017811", "quantity": 1}   # Coffee maker $226.05
                ],
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "anya_garcia_3271"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "anya_garcia_3271",
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},
                ],
                "payment_methods_source": ["gift_card"],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "anya_garcia_3271",
                "item_list": [
                    {"item_id": "1349017811", "quantity": 1},
                ],
                "payment_methods_source": ["credit_card"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "anya_garcia_3271",
                "items": [
                    {"item_id": "5758737025", "quantity": 1},
                ],
                "payment_method_sources": ["gift_card"],
                "tax_amount": 3.61
            }),
            Action(name="create_order", kwargs={
                "user_id": "anya_garcia_3271",
                "items": [
                    {"item_id": "1349017811", "quantity": 1},
                ],
                "payment_method_sources": ["credit_card"],
                "tax_amount": 18.08
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_5",
        instruction=(
            "You're Ivan Santos (user_id: ivan_santos_6635) from 477 Park Avenue, Suite 558, Dallas, TX 75277, USA. "
            "You're a frequent customer with 4 orders and want to check the status of all your orders (#W6893533, #W8770097, #W5183325, #W3913498). "
            "You're particularly concerned about order #W8770097 and want to update your delivery address to a temporary location at 500 Commerce Street, Suite 100, Dallas, TX 75202, USA for that specific order. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ivan", "last_name": "Santos", "user_id": "ivan_santos_6635"}),
            Action(name="get_user_order_history", kwargs={"user_id": "ivan_santos_6635"}),
            Action(name="check_order_status", kwargs={"order_id": "#W6893533"}),
            Action(name="check_order_status", kwargs={"order_id": "#W8770097"}),
            Action(name="check_order_status", kwargs={"order_id": "#W5183325"}),
            Action(name="check_order_status", kwargs={"order_id": "#W3913498"}),
            Action(name="update_delivery_address", kwargs={
                "user_id": "ivan_santos_6635",
                "order_id": "#W8770097",
                "new_address": {
                    "address1": "500 Commerce Street",
                    "address2": "Suite 100",
                    "city": "Dallas",
                    "state": "TX",
                    "zip": "75202",
                    "country": "USA"
                }
            }),
        ],
        outputs=[
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_6",
        instruction=(
            "You're Juan Smith (user_id: juan_smith_5229) at 444 Highland Drive, Suite 419, Dallas, TX 75218, USA. "
            "You will be making the large purchase using only your paypal. "
            "You need to find 3 cheapest water bottle options within the $45 to $50 range, payment terms will be via paypal, validate all items, and coordinate delivery to your Dallas office address."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_smith_5229"}),
            Action(name="get_user_order_history", kwargs={"user_id": "juan_smith_5229"}),
            Action(name="search_products_by_filter", kwargs={"category": "water bottle", "min_price": 45, "max_price": 50, "price_flag": "cheapest", "limit": 3}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},  # $45.09
                    {"item_id": "8538875209", "quantity": 1},  # $45.13
                    {"item_id": "7661609223", "quantity": 1}   # $46.51
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "juan_smith_5229"}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 3, "order_value": 136.73}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_smith_5229",
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},
                    {"item_id": "8538875209", "quantity": 1},
                    {"item_id": "7661609223", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_9679338"],
                "shipping_cost": 16.49
            }),
            Action(name="allocate_inventory", kwargs={"item_id": "5758737025", "quantity": 1}),
            Action(name="allocate_inventory", kwargs={"item_id": "8538875209", "quantity": 1}),
            Action(name="allocate_inventory", kwargs={"item_id": "7661609223", "quantity": 1}),
            Action(name="create_order", kwargs={
                "user_id": "juan_smith_5229",
                "items": [
                    {"item_id": "5758737025", "quantity": 1},
                    {"item_id": "8538875209", "quantity": 1},
                    {"item_id": "7661609223", "quantity": 1}
                ],
                "payment_method_sources": ["paypal_9679338"],
                "tax_amount": 10.94,
                "shipping_cost": 16.49
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 164.16, "courier_id": "#COU0001"}),
            Action(name="process_payment", kwargs={
                "user_id": "juan_smith_5229",
                "payment_method_source": "paypal_9679338",
                "amount": 164.16
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_7",
        instruction=(
            "You're Olivia Smith (user_id: olivia_smith_5265) at 273 Highland Drive, Suite 953, Denver, CO 80216, USA. "
            "You're planning an upcoming hiking trip and want to invest in quality gear. You're specifically interested in premium backpacks "
            "in the $200-220 range and want to purchase the top 3 most expensive options to compare their features. "
            "Your budget allows for multiple purchases, and you prefer using your credit card for outdoor equipment investments."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Olivia", "last_name": "Smith", "user_id": "olivia_smith_5265"}),
            Action(name="get_user_order_history", kwargs={"user_id": "olivia_smith_5265"}),
            Action(name="search_products_by_filter", kwargs={"category": "backpack", "min_price": 200, "max_price": 220, "price_flag": "expensive", "limit": 3}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "8084436579", "quantity": 1},  # $219.43 - Navy, Large, Polyester, Laptop compartment
                    {"item_id": "6309044598", "quantity": 1},  # $218.59 - Blue, Medium, Leather, Laptop compartment
                    {"item_id": "5917587651", "quantity": 1}   # $212.79 - Grey, Medium, Polyester, Laptop compartment
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "olivia_smith_5265"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "olivia_smith_5265",
                "item_list": [
                    {"item_id": "8084436579", "quantity": 1},
                    {"item_id": "6309044598", "quantity": 1},
                    {"item_id": "5917587651", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_7971769"],
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 3, "order_value": 702.87}),
            Action(name="create_order", kwargs={
                "user_id": "olivia_smith_5265",
                "items": [
                    {"item_id": "8084436579", "quantity": 1},
                    {"item_id": "6309044598", "quantity": 1},
                    {"item_id": "5917587651", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_7971769"],
                "tax_amount": 52.06,     # 8% tax on $650.81
                "shipping_cost": 16.49
            }),
            Action(name="process_payment", kwargs={
                "user_id": "olivia_smith_5265",
                "payment_method_source": "credit_card_7971769",
                "amount": 719.36
            }),
        ],
        outputs=[]
    ),

    Task(
    annotator="0",
        user_id="V5TSK_USR_8",
        instruction=(
            "You're Ethan Khan (user_id: ethan_khan_3904) from 264 Elm Street, Suite 579, San Diego, CA 92117, USA. "
            "You placed order #W4347784 but now need to cancel it due to a change in circumstances. "
            "You want to check your order status, cancel the order, request a refund to your Visa credit card, and then place a smaller replacement order for just one cheap water bottle. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ethan", "last_name": "Khan", "user_id": "ethan_khan_3904"}),
            Action(name="get_user_order_history", kwargs={"user_id": "ethan_khan_3904"}),
            Action(name="cancel_order", kwargs={"user_id": "ethan_khan_3904", "order_id": "#W4347784", "cancellation_reason": "change in circumstances"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4347784", "new_status": "cancelled"}),
            Action(name="search_products_by_filter", kwargs={"category": "water bottle", "price_flag": "cheapest", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [{"item_id": "5758737025", "quantity": 1}]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "ethan_khan_3904"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "ethan_khan_3904",
                "item_list": [{"item_id": "5758737025", "quantity": 1}],
                "payment_methods_source": ["credit_card"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "ethan_khan_3904",
                "items": [{"item_id": "5758737025", "quantity": 1}],
                "payment_method_sources": ["credit_card"],
                "tax_amount": 3.61
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_9",
        instruction=(
            "You're Chen Johnson (user_id: chen_johnson_4204) from 503 Elm Avenue, Suite 641, Houston, TX 77004, USA. "
            "You're setting up a home office and want to purchase a complete expensive tech bundle: 1 mechanical keyboard, 1 wireless earbuds, and 1 bluetooth speaker. "
            "You have both PayPal (paypal_3742148) and a gift card with $79 balance (gift_card_3406421) and want to use the gift card first, then PayPal for the remaining amount. "
            "You need to find available options around $230-300 each and split payments appropriately."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Johnson", "user_id": "chen_johnson_4204"}),
            Action(name="get_user_order_history", kwargs={"user_id": "chen_johnson_4204"}),
            Action(name="search_products_by_filter", kwargs={"category": "mechanical keyboard", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="search_products_by_filter", kwargs={"category": "wireless earbuds", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="search_products_by_filter", kwargs={"category": "bluetooth speaker", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6452271382", "quantity": 1},
                    {"item_id": "9440686670", "quantity": 1}
                ]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "chen_johnson_4204",
                "item_list": [{"item_id": "1151293680", "quantity": 1},
                              {"item_id": "6452271382", "quantity": 1},
                               {"item_id": "9440686670", "quantity": 1}],
                "payment_methods_source": ["gift_card", "paypal"],
            }),
            Action(name="process_payment", kwargs={
                "user_id": "chen_johnson_4204",
                "payment_method_source": "gift_card",
                "amount": 79
            }),
            Action(name="process_payment", kwargs={
                "user_id": "chen_johnson_4204",
                "payment_method_source": "paypal",
                "amount": 817.49
            }),
            Action(name="create_order", kwargs={
                "user_id": "chen_johnson_4204",
                "items": [{"item_id": "1151293680", "quantity": 1}, {"item_id": "6452271382", "quantity": 1}, {"item_id": "9440686670", "quantity": 1}],
                "payment_method_sources": ["gift_card", "paypal"],
                "tax_amount": 66.41
            }),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_10",
        instruction=(
            "You're Omar Santos (user_id: omar_santos_4830) at 621 Spruce Street, Suite 698, Fort Worth, TX 76180, USA. "
            "You want to start a wellness routine and need an electric toothbrush and yoga mat. Your budget is flexible, and you have both a Mastercard (credit_card_8992222) and gift card with $75 balance (gift_card_3895897). "
            "You want an electric rechargeable white toothbrush, a blue yoga mat, and make the purchase with your gift card first, then credit card for any remaining balance. "
            "All items should be delivered to your Fort Worth address."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Omar", "last_name": "Santos", "user_id": "omar_santos_4830"}),
            Action(name="get_user_order_history", kwargs={"user_id": "omar_santos_4830"}),
            Action(name="search_products_by_filter", kwargs={"category": "electric toothbrush", "options": {"battery type": ["rechargeable"], "color": ["white"]}}),
            Action(name="search_products_by_filter", kwargs={"category": "yoga mat", "options": {"color": ["blue"]}}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "6164262152", "quantity": 1},  # Electric toothbrush rechargeable $192.15
                    {"item_id": "5586947715", "quantity": 1}   # Yoga mat 4mm PVC $92.53
                ]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "omar_santos_4830",
                "item_list": [
                    {"item_id": "6164262152", "quantity": 1},
                    {"item_id": "5586947715", "quantity": 1}
                ],
                "payment_methods_source": ["gift_card", "credit_card"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "omar_santos_4830",
                "items": [{"item_id": "6164262152", "quantity": 1}, {"item_id": "5586947715", "quantity": 1}],
                "payment_method_sources": ["gift_card", "credit_card"],
                "tax_amount": 24.29,
                "shipping_cost": 0.00
            }),
            Action(name="allocate_inventory", kwargs={"item_id": "6164262152", "quantity": 1}),
            Action(name="allocate_inventory", kwargs={"item_id": "5586947715", "quantity": 1}),
            Action(name="validate_shipping_address", kwargs={"user_id": "omar_santos_4830"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 327.93})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_11",
        instruction=(
            "You're Yusuf Hernandez (user_id: yusuf_hernandez_5411) and need to assess "
            "your recent order history. Your goal is to ensure you have adequate wireless audio equipment that meets "
            "your quality standards: specifically earbuds with strong battery life (6 hours) "
            "and water protection (IPX4 rating minimum) for your active lifestyle. Consider "
            "your current order status and purchase the items accordingly."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={
                "first_name": "Yusuf",
                "last_name": "Hernandez",
                "user_id": "yusuf_hernandez_5411"
            }),
            Action(name="get_user_order_history", kwargs={
                "user_id": "yusuf_hernandez_5411"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W9978601"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W4817567"
            }),
            Action(name="search_products_by_filter", kwargs={"category": "wireless earbuds", "options": {"battery life": ["6 hours"], "water resistance": ["IPX4"]}}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1646531091", "quantity": 1}
                ]
            }),
            Action(name="check_user_payment_methods", kwargs={
                "user_id": "yusuf_hernandez_5411"
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "yusuf_hernandez_5411",
                "item_list": [{"item_id": "1646531091", "quantity": 1}],
                "payment_methods_source": ["paypal_6753664"]
            }),
            Action(name="process_payment", kwargs={
                "user_id": "yusuf_hernandez_5411",
                "payment_method_source": "paypal_6753664",
                "amount": 251.09
            }),
            Action(name="create_order", kwargs={
                "user_id": "yusuf_hernandez_5411",
                "items": [{"item_id": "1646531091", "quantity": 1}],
                "payment_method_sources": ["paypal_6753664"],
                "tax_amount": 18.6,
                "shipping_cost": 0.00
            }),
            Action(name="allocate_inventory", kwargs={
                "item_id": "1646531091",
                "quantity": 1
            }),
            Action(name="validate_shipping_address", kwargs={
                "user_id": "yusuf_hernandez_5411"
            }),
            Action(name="assign_courier", kwargs={
                "destination_country": "USA",
                "order_value": 251.09
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_12",
        instruction=(
            "You're Daiki Silva (user_id: daiki_silva_2903) at 713 Park Avenue, Suite 800, San Francisco, CA 94102, USA. "
            "You want to buy a gift for a friend's birthday - you're looking for something in the $150-200 range, preferably an electric toothbrush. "
            "You're friends favorite color is black, so you want to find a black electric toothbrush. "
            "You only have a gift card with $19 balance (gift_card_2652153), so you know you'll need to add a new payment method which is your visa with last four digits 1234. "
            "You need to explore your options, check what's available in your budget, and see what the shipping costs. Once that has been settled then create an order."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_silva_2903"}),
            Action(name="get_user_order_history", kwargs={"user_id": "daiki_silva_2903"}),
            Action(name="search_products_by_filter", kwargs={"category": "electric toothbrush", "min_price": 150, "max_price": 200, "options": {"color": ["black"]}}),
            Action(name="validate_order_items", kwargs={
                "item_list": [{"item_id": "8098621301", "quantity": 1}]  # Electric toothbrush $183.11
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "daiki_silva_2903",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1234",
                },
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "daiki_silva_2903",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["gift_card", "credit_card"],
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "daiki_silva_2903"}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 207.52}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 207.52}),
            Action(name="allocate_inventory", kwargs={"item_id": "8098621301", "quantity": 1}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "daiki_silva_2903",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["gift_card", "credit_card"],
                "shipping_cost": 11.49,  # shipping cost for 1 item
            }),
            Action(name="process_payment", kwargs={
                "user_id": "daiki_silva_2903",
                "payment_method_source": "gift_card",
                "amount": 19.00
            }),
            Action(name="process_payment", kwargs={
                "user_id": "daiki_silva_2903",
                "payment_method_source": "credit_card",
                "amount":  200.01
            }),
            Action(name="create_order", kwargs={
                "user_id": "daiki_silva_2903",
                "items": [{"item_id": "8098621301", "quantity": 1}],
                "payment_method_sources": ["gift_card", "credit_card"],
                "tax_amount": 15.37,
                "shipping_cost": 11.49  # shipping cost
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_13",
        instruction=(
            "You're a customer service representative handling an escalated case for VIP customer Mei Wilson (user_id: mei_wilson_1792) from 319 Laurel Lane, Suite 319, Charlotte, NC 28260, USA. "
            "The customer is complaining that their order #W4498118 is still pending and they need it expedited for an important business presentation. "
            "You need to validate their identity and items ordered, check their order history and status. If any of the items are not available, update the order status to for return. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mei", "last_name": "Wilson", "user_id": "mei_wilson_1792"}),
            Action(name="get_user_order_history", kwargs={"user_id": "mei_wilson_1792"}),
            Action(name="check_order_status", kwargs={"order_id": "#W4498118"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5745575001", "quantity": 1},
                    {"item_id": "7736359414", "quantity": 1},
                    {"item_id": "5312063289", "quantity": 1},
                    {"item_id": "5565631513", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ]
            }),
            Action(name="update_order_status", kwargs={"order_id": "#W4498118", "new_status": "for return"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_14",
        instruction=(
            "You're James Nguyen (user_id: james_nguyen_2792), a first-time customer at 570 Main Street, Suite 708, Chicago, IL 60627, USA. "
            "You want to create your first order and purchase a starter tech package: the cheapest electric toothbrush and yoga mat for your wellness journey. "
            "You have a new Mastercard (credit_card_2645445) and want to test the entire process from account validation to order placement. "
            "You need to ensure your payment method works, validate your Chicago address for shipping, and complete your first order successfully."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Nguyen", "user_id": "james_nguyen_2792"}),
            Action(name="get_user_order_history", kwargs={"user_id": "james_nguyen_2792"}),
            Action(name="search_products_by_filter", kwargs={"category": "electric toothbrush", "price_flag": "cheapest", "limit": 1}),
            Action(name="search_products_by_filter", kwargs={"category": "yoga mat", "price_flag": "cheapest", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2645006275", "quantity": 1},  # Electric toothbrush $183.11
                    {"item_id": "5586947715", "quantity": 1}   # Yoga mat $92.53
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "james_nguyen_2792"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "james_nguyen_2792",
                "item_list": [
                    {"item_id": "2645006275", "quantity": 1},
                    {"item_id": "5586947715", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_2645445"],
            }),
            Action(name="process_payment", kwargs={
                "user_id": "james_nguyen_2792",
                "payment_method_source": "credit_card_2645445",
                "amount": 297.69
            }),
            Action(name="create_order", kwargs={
                "user_id": "james_nguyen_2792",
                "items": [{"item_id": "2645006275", "quantity": 1}, {"item_id": "5586947715", "quantity": 1}],
                "payment_method_sources": ["credit_card_2645445"],
                "tax_amount": 22.05,
                "shipping_cost": 0.00  # shipping cost
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_15",
        instruction=(
            "You're Anya Garcia (user_id: anya_garcia_3271). "
            "Update your email to 'anya.garcia2061@example.com' and address to 248 Pinecrest Drive, Apt 9C, Austin, TX 73301, USA. "
            "Validate if its reflected and check your gift card balance."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "anya_garcia_3271",
                "profile_updates": {"email": "anya.garcia2061@example.com",
                                    "address": {
                                        "address1": "248 Pinecrest Drive",
                                        "address2": "Apt 9C",
                                        "city": "Austin",
                                        "state": "TX",
                                        "zip": "73301",
                                        "country": "USA"
                                    }}
            }),
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"}),
            Action(name="verify_gift_card_balance", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"})
        ],
        outputs=[
            '"gift_card_balance": 51',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_17",
        instruction=(
            "You're Emma Smith (user_id: emma_smith_8564) a supply manager. Set the stock levels of 2235648106 to 200 units. "
            "Update its supplier #SUP0003 phone and email to +1-800-555-NEW1 phonesupplier@example.com."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Smith", "user_id": "emma_smith_8564"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0003",
                "item_id": "2235648106",
                "new_stock_level": 200,
                "stock_action": "set"
            }),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0003",
                "contact_updates": {"phone": "+1-800-555-NEW1", "email": "phonesupplier@example.com"}
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_18",
        instruction=(
            "You're Mia Nguyen (user_id: mia_nguyen_6399) from 412 Lakeview Drive, Suite 698, San Antonio, TX 78229, USA. "
            "You want to buy a birthday gift for your friend with a $100-$300 budget for the cheapest bluetooth speakers. "
            "You have PayPal (paypal_3722088) as your payment method and need to find the best value item within budget, validate availability, and order it. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mia", "last_name": "Nguyen", "user_id": "mia_nguyen_6399"}),
            Action(name="get_user_order_history", kwargs={"user_id": "mia_nguyen_6399"}),
            Action(name="search_products_by_filter", kwargs={"category": "bluetooth speaker", "min_price": 100, "max_price": 300, "available_only": True, "price_flag": "cheapest", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2635605237", "quantity": 1}
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "mia_nguyen_6399"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "mia_nguyen_6399",
                "item_list": [
                   {"item_id": "2635605237", "quantity": 1}
                ],
                "payment_methods_source": ["paypal"],
            }),
                Action(name="create_order", kwargs={
                "user_id": "mia_nguyen_6399",
                "items": [{"item_id": "2635605237", "quantity": 1}],
                "payment_method_sources": ["paypal"],
                "tax_amount": 21.75,
                "shipping_cost": 0.00
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_19",
        instruction=(
            "You're a customer service rep. helping Yusuf Rossi user_id: "
            "yusuf_rossi_9620. Update all his pending orders to processed status."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yusuf", "last_name": "Rossi", "user_id": "yusuf_rossi_9620"}),
            Action(name="get_user_order_history", kwargs={"user_id": "yusuf_rossi_9620"}),
            Action(name="update_order_status", kwargs={"order_id": "#W6247578", "new_status": "processed"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4776164", "new_status": "processed"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_20",
        instruction=(
            "You're Ethan Smith (user_id: ethan_smith_7905) from 218 Main Street, Suite 792, Phoenix, AZ 85001, USA. "
            "You're a tech enthusiast wanting to upgrade your entire workspace: mechanical keyboard with RGB lighting, wireless earbuds with 8 hours battery life, and a red bluetooth speaker that has water resistance. "
            "You want the most expensive available options regardless of price, have a Visa card (credit_card_3185406), and order everything. "
            "You also want to validate each item's specifications before purchase."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ethan", "last_name": "Smith", "user_id": "ethan_smith_7905"}),

            Action(name="get_user_order_history", kwargs={"user_id": "ethan_smith_7905"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "mechanical keyboard",
                "options": {"backlight": "RGB"},
                "price_flag": "expensive"
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "wireless earbuds",
                "options": {"battery life": ["8 hours"]},
                "price_flag": "expensive",
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "bluetooth speaker",
                "options": {"water resistance": "yes", "color": "red"},
                "price_flag": "expensive",
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6077640618", "quantity": 1},
                    {"item_id": "7751905257", "quantity": 1}
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "ethan_smith_7905"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "ethan_smith_7905"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "ethan_smith_7905",
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6077640618", "quantity": 1},
                    {"item_id": "7751905257", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3185406"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "ethan_smith_7905",
                "items": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6077640618", "quantity": 1},
                    {"item_id": "7751905257", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_3185406"],
                "tax_amount": 66.91,
                "shipping_cost": 0.00
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_21",
        instruction=(
            "You're a customer service representative managing an urgent inventory crisis for Chen Moore (user_id: chen_moore_6080), who is requesting a laptop with 32GB RAM, 256GB SSD, and an Intel i7 processor, but the model currently shows as unavailable. To resolve this, you confirm Chen's identity and review their purchasing history, locate the laptop within the $2400–2700 price range, update the system to mark it as available at $2450.00, validate all order components, and complete the purchase using Chen’s credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="get_user_order_history", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="search_products_by_filter", kwargs={"category": "laptop", "min_price": 2400, "max_price": 2700, "available_only": False,
                                                             "options": {"ram": ["32GB"], "storage": ["256GB SSD"], "processor": ["i7"]}}),
            Action(name="update_product_availability", kwargs={"product_id": "4760268021", "item_id": "8997785118", "available": True, "new_price": 2450.00}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "8997785118", "quantity": 1}
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "chen_moore_6080",
                "item_list": [{"item_id": "8997785118", "quantity": 1}],
                "payment_methods_source": ["credit_card_4041739"],
            }),
            Action(name="process_payment", kwargs={
                "user_id": "chen_moore_6080",
                "payment_method_source": "credit_card_4041739",
                "amount": 2646.0
            }),
            Action(name="create_order", kwargs={
                "user_id": "chen_moore_6080",
                "items": [
                    {"item_id": "8997785118", "quantity": 1},
                ],
                "payment_method_sources": ["credit_card_4041739"],
                "tax_amount": 196.0,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_22",
        instruction=(
           "You're Juan Anderson (user_id: juan_anderson_5671) relocating from Jacksonville to Seattle 1200 Pine Street, Apt 15B, Seattle, Washington (98101)."
            "Ensure your profile reflects your new address and updated contact email to juan.anderson.seattle@example.com, arrange payment "
            "using a newly issued $750 gift card, and source affordable home office furnitures (desk lamp, office chair) within the "
            "$100–$500 range. Choose options that balance cost and suitability, confirm availability, and "
            "have Reliable Delivery Co. ship them to your new Seattle residence."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Anderson", "user_id": "juan_anderson_5671"}),
            Action(name="get_user_order_history", kwargs={"user_id": "juan_anderson_5671"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "juan_anderson_5671",
                "profile_updates": {
                    "email": "juan.anderson.seattle@example.com",
                    "address": {
                        "address1": "1200 Pine Street",
                        "address2": "Apt 15B",
                        "city": "Seattle",
                        "state": "WA",
                        "zip": "98101",
                        "country": "USA"
                    }
                }
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "juan_anderson_5671",
                "payment_type": "gift_card",
                "payment_details": {
                    "balance": 750
                }
            }),
            Action(name="search_products_by_filter", kwargs={"category": "desk lamp", "min_price": 100, "max_price": 500, "price_flag": "cheapest", "limit": 1}),
            Action(name="search_products_by_filter", kwargs={"category": "office chair", "min_price": 100, "max_price":500, "price_flag": "cheapest", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5320792178", "quantity": 1},  # desk lamp
                    {"item_id": "4168944673", "quantity": 1}   # chair
                ]
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "juan_anderson_5671"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_anderson_5671",
                "item_list": [{"item_id": "5320792178", "quantity": 1}, {"item_id": "4168944673", "quantity": 1}],
                "payment_methods_source": ["gift_card_25671"],
            }),
            Action(name="get_courier_by_name", kwargs={"courier_name": "Reliable Delivery Co."}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 655.62, "courier_id": "#COU0009"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_anderson_5671",
                "item_list": [{"item_id": "5320792178", "quantity": 1}, {"item_id": "4168944673", "quantity": 1}],
                "payment_methods_source": ["gift_card_25671"],
                "shipping_cost": 13.99  # shipping cost for 2 items
            }),
            Action(name="process_payment", kwargs={
                "user_id": "juan_anderson_5671",
                "payment_method_source": "gift_card_25671",
                "amount": 669.61
            }),
            Action(name="create_order", kwargs={
                "user_id": "juan_anderson_5671",
                "items": [
                    {"item_id": "5320792178", "quantity": 1},
                    {"item_id": "4168944673", "quantity": 1},
                ],
                "payment_method_sources": ["gift_card_25671"],
                "tax_amount": 48.56,
                "shipping_cost": 13.99
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA","order_value": 669.61,  "courier_id": "#COU0009"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_23",
        instruction=(
            "You're Lei Johansson (user_id: lei_johansson_7574) moving from Denver to a new address at 245 Mountain View Drive, Apt 8C, Boulder, CO 80302, USA. "
            "You need to update your email to lei.johansson.boulder@example.com, update your address, add a new Visa credit card (ending in 7890), "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lei", "last_name": "Johansson", "user_id": "lei_johansson_7574"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "lei_johansson_7574",
                "profile_updates": {
                    "email": "lei.johansson.boulder@example.com",
                    "address": {
                        "address1": "245 Mountain View Drive",
                        "address2": "Apt 8C",
                        "city": "Boulder",
                        "state": "CO",
                        "zip": "80302",
                        "country": "USA"
                    }
                }
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "lei_johansson_7574",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "7890"
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_24",
        instruction=(
            "You're Aarav Davis (user_id: aarav_davis_4756) from 178 Lakeview Drive, Suite 576, Fort Worth, TX 76150, USA. "
            "Use your gift card to purchase a blue cotton T-shirt in medium size. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Aarav", "last_name": "Davis", "user_id": "aarav_davis_4756"}),
            Action(name="get_user_order_history", kwargs={"user_id": "aarav_davis_4756"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "aarav_davis_4756"}),
            Action(name="search_products_by_filter", kwargs={"category": "t-shirt", "options": {"color": ["blue"], "material": ["cotton"], "size": ["M"]}}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "9612497925", "quantity": 1},  # T-shirt
                ]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "aarav_davis_4756",
                "item_list": [{"item_id": "9612497925", "quantity": 1}],
                "payment_methods_source": ["gift_card_9708163"],
            }),
            Action(name="process_payment", kwargs={
                "user_id": "aarav_davis_4756",
                "payment_method_source": "gift_card_9708163",
                "amount": 54.95
            }),
            Action(name="create_order", kwargs={
                "user_id": "aarav_davis_4756",
                "items": [
                    {"item_id": "9612497925", "quantity": 1}
                ],
                "payment_method_sources": ["gift_card_9708163"],
                "tax_amount": 4.07
            }),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_25",
        instruction=(
            "You're a customer service representative helping Chen Brown (user_id: chen_brown_8075) from 945 Hickory Lane, Suite 262, San Jose, CA 95190, USA. "
            "The customer wants to change their delivery address for all his orders to their office at 500 Technology Drive, Building A, San Jose, CA 95110, USA. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Brown", "user_id": "chen_brown_8075"}),
            Action(name="get_user_order_history", kwargs={"user_id": "chen_brown_8075"}),
            Action(name="check_order_status", kwargs={"order_id": "#W4296426"}),
            Action(name="check_order_status", kwargs={"order_id": "#W3381155"}),
            Action(name="update_delivery_address", kwargs={
                "user_id": "chen_brown_8075",
                "order_id": "#W4296426",
                "new_address": {
                    "address1": "500 Technology Drive",
                    "address2": "Building A",
                    "city": "San Jose",
                    "state": "CA",
                    "zip": "95110",
                    "country": "USA"
                }
            }),
            Action(name="update_delivery_address", kwargs={
                "user_id": "chen_brown_8075",
                "order_id": "#W3381155",
                "new_address": {
                    "address1": "500 Technology Drive",
                    "address2": "Building A",
                    "city": "San Jose",
                    "state": "CA",
                    "zip": "95110",
                    "country": "USA"
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_26",
        instruction=(
            "You're a customer service representative helping Mei Martin (user_id: mei_martin_6103). "
            "She wants to update her email to mei.martin.updated@example.com. Also the product she wants is out of stock, which is a gold colored smartphone with "
            "128GB storage and 6GB ram. Update the product availability to true, adjust the price to $1499.99, and help her complete the purchase using her Visa card (credit_card_8398849). "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mei", "last_name": "Martin", "user_id": "mei_martin_6103"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "mei_martin_6103",
                "profile_updates": {
                    "email": "mei.martin.updated@example.com"
                }
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "smartphone",
                "available_only": False,
                "options": {"color": ["gold"], "storage": ["128GB"], "RAM": ["6GB"]},
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1801728040",
                "item_id": "1631373418",
                "available": True,
                "new_price": 1499.99
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [{"item_id": "1631373418", "quantity": 1}]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "mei_martin_6103",
                "item_list": [{"item_id": "1631373418", "quantity": 1}],
                "payment_methods_source": ["credit_card_8398849"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "mei_martin_6103",
                "items": [
                    {"item_id": "1631373418", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_8398849"],
                "tax_amount": 120.0,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_27",
        instruction=(
            "You're Juan Sanchez (user_id: juan_sanchez_8249) from 281 Main Street, Suite 979, Washington, DC 20156, USA. "
            "You want to cancel your existing order due to changed plans, then place a new order for a gaming mouse. "
            "Use your PayPal account to order the cheapest available product."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Sanchez", "user_id": "juan_sanchez_8249"}),
            Action(name="get_user_order_history", kwargs={"user_id": "juan_sanchez_8249"}),
            Action(name="check_order_status", kwargs={"order_id": "#W6483628"}),
            Action(name="cancel_order", kwargs={
                "user_id": "juan_sanchez_8249",
                "order_id": "#W6483628",
                "cancellation_reason": "change of plans"
            }),
            Action(name="search_products_by_filter", kwargs={"category": "gaming mouse", "price_flag": "cheapest", "limit": 1}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                ]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_sanchez_8249",
                "item_list": [{"item_id": "2880340443", "quantity": 1}],
                "payment_methods_source": ["paypal"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "juan_sanchez_8249",
                "items": [
                    {"item_id": "2880340443", "quantity": 1}
                ],
                "payment_method_sources": ["paypal"],
                "tax_amount": 10.98,
                "shipping_cost": 0.00
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_28",
        instruction=(
            "You're Lucas Brown (user_id: lucas_brown_6720), an inventory manager for the retail company. You need to review the supply chain status for laptop products (product_id: 4760268021). "
            "Check the status of the said product and validate the capacity of its supplier. Once validated create a new supply order of the same product with a quantity of 150 units from the same supplier. "
            "Once the supply order is created, update the previous supply order status to pending and set the product to be unavailable in the system. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lucas", "last_name": "Brown", "user_id": "lucas_brown_6720"}),
            Action(name="check_supply_order_status", kwargs={"product_id": "4760268021"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0002",
                "product_id": "4760268021",
                "item_id": "3265035808",
                "quantity": 150,
                "unit_cost": 1140.45
            }),
            Action(name="update_supply_order_status", kwargs={
                "supply_order_id": "#SO5813",
                "new_status": "pending"
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "4760268021",
                "item_id": "3265035808",
                "available": False
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_30",
        instruction=(
            "You're Mei Wilson (user_id: mei_wilson_1792) a store manager for the retail company. "
            "Your regular supplier #SUP0007 is having issues with grill orders. Check supplier #SUP0007 for their highest stock items if they could fulfill order for a minimum of 20 units. "
            "Once checked, create a new supply order and update stock inventory in the system to subtract 20 units."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mei", "last_name": "Wilson", "user_id": "mei_wilson_1792"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["grill"]}),
            Action(name="search_suppliers_by_product", kwargs={
                "supplier_id": "#SUP0007",
                "product_id": "6819683148",
                "min_stock_level": 20,
                "product_type": ["grill"],
                "stock_level_preference": "highest"
            }),
            Action(name="get_product_info", kwargs={"item_id": "9724317332"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0007",
                "product_id": "6819683148",
                "item_id": "9724317332",
                "quantity": 20,
                "unit_cost": 1042.19
            }),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0007",
                "item_id": "9724317332",
                "new_stock_level": 20,
                "stock_action": "subtract"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_31",
        instruction=(
            "You're Omar Santos (user_id: omar_santos_4830) a supply chain manager for the retail company. "
            "You need to update pricing terms for an existing supply order #SO6035 because costs have changed. "
            "Check the supply order details, update the terms to COD with new pricing set at $30.0, and adjust "
            "inventory accordingly to add 45 units."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Omar", "last_name": "Santos", "user_id": "omar_santos_4830"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="update_supply_order_terms", kwargs={
                "supply_order_id": "#SO6035",
                "new_unit_cost": 30.0,
                "payment_terms": "COD"
            }),
            Action(name="get_product_info", kwargs={"item_id": "7579176349"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0002",
                "item_id": "7579176349",
                "new_stock_level": 45,
                "stock_action": "add"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_32",
        instruction=(
            "You're Daiki Silva (user_id: daiki_silva_2903) a supply coordinator for the retail company. "
            "You need to check supplier inventory levels for smartphones, ensuring that every variant is available and kept at a minimum value of 50 units. " \
            "Validate supplier capacity and update supplier ratings based on recent performance. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_silva_2903"}),
            Action(name="search_suppliers_by_product", kwargs={
                "min_stock_level": 50,
                "product_type": ["smartphone"],
            }),
            Action(name="get_product_info", kwargs={"item_id": "5490694069"}),
            Action(name="get_product_info", kwargs={"item_id": "9929635042"}),
            Action(name="get_product_info", kwargs={"item_id": "5758570643"}),
            Action(name="get_product_info", kwargs={"item_id": "5311660992"}),
            Action(name="update_product_availability", kwargs={
                "product_id": "1801728040",
                "item_id": "5490694069",
                "available": True
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1801728040",
                "item_id": "9929635042",
                "available": True
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1801728040",
                "item_id": "5758570643",
                "available": True
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1801728040",
                "item_id": "5311660992",
                "available": True
            }),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0004",
                "performance_rating": 2.0,
                "notes": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability."
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_33",
        instruction=(
            "You're Daiki Silva (user_id: daiki_silva_2903) from 713 Park Avenue, Suite 800, San Francisco, CA 94102, USA. "
            "You need to search supplier inventory levels for available only headphones, because you're placing a large order. "
            "Once you have the information, create supply order for 30 units each variant."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_silva_2903"}),
            Action(name="search_suppliers_by_product", kwargs={
                "product_type": ["headphones"],
                "available_only": True,
            }),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_product_info", kwargs={"item_id": "3374679624"}),
            Action(name="get_product_info", kwargs={"item_id": "3104857380"}),
            Action(name="get_product_info", kwargs={"item_id": "7493556126"}),
            Action(name="get_product_info", kwargs={"item_id": "9805150490"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0007",
                "product_id": "6992792935",
                "item_ids": ["3374679624", "3104857380", "7493556126", "9805150490"],
                "quantity": 30,
                "unit_cost": [370.53, 377.97, 346.97, 368.87]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_34",
        instruction=(
            "You're James Lee (user_id: james_lee_5010), a supply chain expert overseeing supplier #SUP0011. "
            "Ensure the supplier's information is accurate and performance ratings reflect recent evaluations, "
            "and confirm all their available electric toothbrush inventory is maintained at optimal stock levels of 200 units."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Lee", "user_id": "james_lee_5010"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0011",
                "contact_updates": {
                    "phone": "+1-800-555-0089"
                },
                "performance_rating": 1.0
            }),
            Action(name="get_product_items_per_supplier", kwargs={"supplier_id": "#SUP0011", "stock_available": True, "product_type": "electric toothbrush"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0011",
                "item_ids": ['1583904702', '6555827912', '8098621301', '3320557165', '8798690242'],
                "new_stock_level": 200,
                "stock_action": "set"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_35",
        instruction=(
            "You're Ethan Wilson (user_id: ethan_wilson_5687) from 312 Chestnut Street, Suite 578, San Diego, CA 92152, USA. "
            "You want to buy your first laptop for college. You need to search for cheapest laptops with 1TB storage, "
            "validate your identity, check available payment methods, validate the order items, and complete your purchase "
            "using your gift card and add a new payment method using your visa credit card (**** **** **** 1234) to pay for the remaining balance. Make sure the laptop is available. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ethan", "last_name": "Wilson", "user_id": "ethan_wilson_5687"}),
            Action(name="get_user_order_history", kwargs={"user_id": "ethan_wilson_5687"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "laptop",
                "options": {"storage": "1TB SSD"},
                "price_flag": "cheapest",
                "available_only": True,
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "ethan_wilson_5687"}),
            Action(name="add_payment_method", kwargs={
                "user_id": "ethan_wilson_5687",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1234",
                },
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "ethan_wilson_5687",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                ],
                "payment_methods_source": ["gift_card_6470461", "credit_card_25687"],
            }),
            Action(name="create_order", kwargs={
                "user_id": "ethan_wilson_5687",
                "items": [{"item_id": "6017636844", "quantity": 1}],
                "payment_method_sources": ["gift_card_6470461", "credit_card_25687"],
                "tax_amount": 183.39,
                "shipping_cost": 0.00
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_36",
        instruction=(
            "You're a customer service representative assisting Mei Moore (user_id: mei_moore_8248) "
            "with a payment issue. Her credit card was declined for a tablet purchase in the $1050+ "
            "price range, and she wants to complete the transaction using PayPal instead. Your goal "
            "is to help Mei successfully obtain the tablet she needs while ensuring her account is "
            "properly configured and the order process follows all standard verification procedures."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={
                "first_name": "Mei",
                "last_name": "Moore",
                "user_id": "mei_moore_8248"
            }),
            Action(name="get_user_order_history", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="check_user_payment_methods", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "mei_moore_8248",
                "payment_type": "paypal",
                "payment_details": {}
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "tablet",
                "min_price": 1050,
                "available_only": True
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2235648106", "quantity": 1}
                ]
            }),
            Action(name="validate_shipping_address", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "mei_moore_8248",
                "item_list": [
                    {"item_id": "2235648106", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_28248"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "mei_moore_8248",
                "items": [{"item_id": "2235648106", "quantity": 1}],
                "payment_method_sources": ["paypal_28248"],
                "tax_amount": 84.35,
                "shipping_cost": 0.00
            })
        ],
        outputs=[]
    ),


    Task(
        annotator="0",
        user_id="V5TSK_USR_37",
        instruction=(
            "You're Yusuf Taylor (yusuf_taylor_7149) a procurement specialist managing supplier relationships. Supplier #SUP0003 has updated their contact information "
            "and you need to update their details in the system. Check their current details, update contact info (email newsupport@premiumparts.com, phone +1-800-555-0134), "
            "and performance rating to 4.2. Also add in some notes for the supplier (reliable supplier). You also need to validate their capacity, search for products they supply, "
            "check their stock levels, and review their supply orders."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yusuf", "last_name": "Taylor", "user_id": "yusuf_taylor_7149"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0003",
                "contact_updates": {
                    "email": "newsupport@premiumparts.com",
                    "phone": "+1-800-555-0134"
                },
                "performance_rating": 4.2,
                "notes": "reliable supplier"
            }),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_product_items_per_supplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="check_supply_order_status", kwargs={"product_id": "8024098596"}),
            Action(name="check_supply_order_status", kwargs={"product_id": "7471004230"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO7422"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5993"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_38",
        instruction=(
            "You're Liam Gonzalez (user_id: liam_gonzalez_4265) from 647 Laurel Lane, Suite 627, Austin, TX 78747, USA. "
            "You want to buy a complete home office setup: a laptop, headphones and a smartphone. Everything should be available and cheap. "
            "Validate all items are available, check your payment methods, "
            "generate order summary, and complete the purchase using your credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Liam", "last_name": "Gonzalez", "user_id": "liam_gonzalez_4265"}),
            Action(name="get_user_order_history", kwargs={"user_id": "liam_gonzalez_4265"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "laptop",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "headphones",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "smartphone",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "liam_gonzalez_4265"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "liam_gonzalez_4265",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_6341155"]
            }),
            Action(name="process_payment", kwargs={
                "user_id": "liam_gonzalez_4265",
                "payment_method_source": "credit_card_6341155",
                "amount": 4067.18
            }),
            Action(name="create_order", kwargs={
                "user_id": "liam_gonzalez_4265",
                "items": [
                    {"item_id": "6017636844", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_6341155"],
                "tax_amount": 301.27
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_39",
        instruction=(
            "You're a customer service representative handling a complex case for Mei Gonzalez (user_id: mei_gonzalez_4785) "
            "The customer received a damaged backpack and wants to return it plus get a replacement backpack within the same price range. "
            "You need to process the return, find the cheapest replacement and validate it, update order status, and ensure customer satisfaction. "
            "Use her paypal to purchase the order. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_order_history", kwargs={"user_id": "mei_gonzalez_4785", "product_type": ["backpack"]}),
            Action(name="check_order_status", kwargs={"order_id": "#W7303089"}),
            Action(name="request_order_return", kwargs={
                "user_id": "mei_gonzalez_4785",
                "order_id": "#W7303089",
                "item_id": "2492465580",
                "return_reason": "Damaged backpack"
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "backpack",
                "max_price": 201.95,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "9851293632", "quantity": 1},
                ],
            }),
            Action(name="update_order_status", kwargs={
                "order_id": "#W7303089",
                "new_status": "for return"
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="create_order", kwargs={
                "user_id": "mei_gonzalez_4785",
                "items": [
                    {"item_id": "9851293632", "quantity": 1},
                ],
                "payment_method_sources": ["paypal_2568958"],
                "return_refund_amount": 201.95,
                "return_order_id": "#W7303089"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_40",
        instruction=(
            "You're Ethan Lopez user_id: ethan_lopez_6291, an inventory manager handling "
            "emergency stock replenishment for smartwatches due to high customer demand. "
            "Check current supplier stock levels and include only suppliers with at least "
            "100 units. Set inventory so all available smartwatch variants are exactly "
            "250 units ensuring unavailable items are excluded, and update the supplier performance rating to 4.5."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ethan", "last_name": "Lopez", "user_id": "ethan_lopez_6291"}),
            Action(name="search_suppliers_by_product", kwargs={
                "min_stock_level": 100,
                "product_type": ["smart watch"],
            }),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0002",
                "performance_rating": 4.5
            }),
            Action(name="get_product_items_per_supplier", kwargs={"supplier_id": "#SUP0002", "product_type": "smart watch", "stock_available": True}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0002",
                "item_ids": ['4920090458', '9320099340', '2860956907', '1631806422', '9192177173', '1706622510', '2540052208', '5694328282',
                             '9408160950', '2554056026', '1007724142', '2993891288', '9811090008', '2681513500'],
                "new_stock_level": 250,
                "exclude_unavailable": True,
                "stock_action": "set"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_41",
        instruction=(
            "You're James Wilson (user_id: james_wilson_1842). "
            "You recently moved and need to update your profile address to 234 Mountain View Drive, Apt 15, Denver, CO 80205, USA. "
            "You also want to place a new order for the cheapest smartphone you could find and ensure it ships to your new address. "
            "Update your profile, validate the new shipping address, place an order which is to be fulfilled by RapidRoute Logistics."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Wilson", "user_id": "james_wilson_1842"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "james_wilson_1842",
                "profile_updates": {
                    "address": {
                        "address1": "234 Mountain View Drive",
                        "address2": "Apt 15",
                        "city": "Denver",
                        "state": "CO",
                        "zip": "80205",
                        "country": "USA"
                    }
                }
            }),
            Action(name="validate_shipping_address", kwargs={"user_id": "james_wilson_1842"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "smartphone",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5339029584", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "james_wilson_1842"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "RapidRoute Logistics"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "james_wilson_1842",
                "item_list": [
                    {"item_id": "5339029584", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_7871433"]
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1,
                                                           "courier_id": "#COU0005",
                                                           "order_value": 1219.31,
                                                           "location": {
                                                                "address1": "234 Mountain View Drive",
                                                                "address2": "Apt 15",
                                                                "city": "Denver",
                                                                "state": "CO",
                                                                "zip": "80205",
                                                                "country": "USA"
                                                            }
                                                           }),
            Action(name="create_order", kwargs={
                "user_id": "james_wilson_1842",
                "items": [{"item_id": "5339029584", "quantity": 1}],
                "payment_method_sources": ["credit_card_7871433"],
                "tax_amount": 90.32,
                "shipping_cost": 29.78
            }),
            Action(name="assign_tracking_number", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0005"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 1249.09,
                                                  "courier_id": "#COU0005",
                                                  "tracking_ids": ["TRKBATCH01C0005"],
                                                  "location": {
                                                      "address1": "234 Mountain View Drive",
                                                      "address2": "Apt 15",
                                                      "city": "Denver",
                                                      "state": "CO",
                                                      "zip": "80205",
                                                      "country": "USA"
                                                  }}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_42",
        instruction=(
            "You're assisting Noah Ito (user_id: noah_ito_3850) with a bulk corporate electronics order—3 tablets and 2 headphones for their office."
            "Buy the cheapest items, validate them, check availability, calculate total costs, process the order, and arrange delivery via Express Delivery Services."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Noah", "last_name": "Ito", "user_id": "noah_ito_3850"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "tablet",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "headphones",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "noah_ito_3850"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "noah_ito_3850",
                "item_list": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
                "payment_methods_source": ["credit_card_1620755"]
            }),
            Action(name="get_courier_by_name", kwargs={"courier_name": "Express Delivery Services"}),

            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 5, "order_value": 3673.03,
                                                           "courier_id": "#COU0003",
                                                            "address": {
                                                                "address1": "619 Broadway",
                                                                "address2": "Suite 484",
                                                                "city": "Seattle",
                                                                "country": "USA",
                                                                "state": "WA",
                                                                "zip": "98187"
                                                            }}),
            Action(name="create_order", kwargs={
                "user_id": "noah_ito_3850",
                "items": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
                "payment_method_sources": ["credit_card_1620755"],
                "tax_amount": 272.08,
                "shipping_cost": 76.59
            }),
            Action(name="assign_tracking_number", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0003"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 3749.62, "courier_id": "#COU0003",
                                                  "tracking_ids": ["TRKBATCH01C0003"],
                                                  "location": {
                                                        "address1": "619 Broadway",
                                                        "address2": "Suite 484",
                                                        "city": "Seattle",
                                                        "country": "USA",
                                                        "state": "WA",
                                                        "zip": "98187"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_43",
        instruction=(
            "You're Anya Rossi (anya_rossi_7776) procurement manager conducting a comprehensive supplier performance review for electronics suppliers. "
            "Review suppliers #SUP0001, #SUP0004, and #SUP0007, check their capacity and update performance ratings and feedbacks. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Rossi", "user_id": "anya_rossi_7776"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0001",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0004",
                "performance_rating": 2.0,
                "notes": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability."
            }),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0007",
                "performance_rating": 1.0,
                "notes": "Unacceptable performance with very poor reliability. Frequent order cancellations pose serious supply chain risks."
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_44",
        instruction=(
            "You're Anya Sanchez (user_id: anya_sanchez_9707). "
            "You want to buy gifts to Lucas Davis (lucas_davis_5124) and Emma Brown (emma_brown_8847), "
            "You need an expensive Vacuum Cleaner for Lucas and an expensive Air Purifier for Emma and create orders for both. "
            "Deliver them to their addresses using RapidRoute Logistics."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Sanchez", "user_id": "anya_sanchez_9707"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "vacuum cleaner",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "air purifier",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "4806644905", "quantity": 1},
                    {"item_id": "8302289002", "quantity": 1},
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "anya_sanchez_9707"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Lucas", "last_name": "Davis", "user_id": "lucas_davis_5124"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Brown", "user_id": "emma_brown_8847"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "anya_sanchez_9707",
                "item_list": [
                    {"item_id": "4806644905", "quantity": 1},
                ],
                "payment_methods_source": ["paypal_1191071"]
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "anya_sanchez_9707",
                "item_list": [
                    {"item_id": "8302289002", "quantity": 1},
                ],
                "payment_methods_source": ["paypal_1191071"]
            }),
            Action(name="get_courier_by_name", kwargs={"courier_name": "RapidRoute Logistics"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 711.6, "courier_id": "#COU0005",
                                                  "location": {
                                                       "address1": "852 Oak Street",
                                                        "address2": "Suite 747",
                                                        "city": "Jacksonville",
                                                        "country": "USA",
                                                        "state": "FL",
                                                        "zip": "32187"}}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 591.35, "courier_id": "#COU0005",
                                                  "location": {
                                                       "address1": "984 Hickory Lane",
                                                        "address2": "Suite 834",
                                                        "city": "Jacksonville",
                                                        "country": "USA",
                                                        "state": "FL",
                                                        "zip": "32165"}}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 711.6,
                                                           "courier_id": "#COU0005",
                                                           "address": {
                                                               "address1": "852 Oak Street",
                                                               "address2": "Suite 747",
                                                               "city": "Jacksonville",
                                                               "country": "USA",
                                                               "state": "FL",
                                                               "zip": "32187"}}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 591.35,
                                                           "courier_id": "#COU0005",
                                                           "address": {
                                                               "address1": "984 Hickory Lane",
                                                               "address2": "Suite 834",
                                                               "city": "Jacksonville",
                                                               "country": "USA",
                                                               "state": "FL",
                                                               "zip": "32165"}}),
            Action(name="create_order", kwargs={
                "user_id": "anya_sanchez_9707",
                "items": [
                    {"item_id": "4806644905", "quantity": 1},
                ],
                "payment_method_sources": ["paypal_1191071"],
                "tax_amount": 52.71,
                "shipping_cost": 11.49
            }),
            Action(name="create_order", kwargs={
                "user_id": "anya_sanchez_9707",
                "items": [
                    {"item_id": "8302289002", "quantity": 1},
                ],
                "payment_method_sources": ["paypal_1191071"],
                "tax_amount": 43.8,
                "shipping_cost": 11.49
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_45",
        instruction=(
            "You're Chen Moore (user_id: chen_moore_6080) and want to buy a black smart watch and headphones for your new apartment. Both items must be available and affordable. "
            "Search for these products, validate your identity, check availability, and complete the purchase using your credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "smart watch",
                "options": {"color": "black"},
                "available_only": True,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "headphones",
                "options": {"color": "black"},
                "available_only": True,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2860956907", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "chen_moore_6080",
                "item_list": [
                    {"item_id": "2860956907", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_4041739"]
            }),
            Action(name="process_payment", kwargs={
                "user_id": "chen_moore_6080",
                "payment_method_source": "credit_card_4041739",
                "amount": 712.97
            }),
            Action(name="create_order", kwargs={
                "user_id": "chen_moore_6080",
                "items": [
                    {"item_id": "2860956907", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_4041739"],
                "tax_amount": 52.81,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_46",
        instruction=(
            "You're a customer service representative helping Yara Lee (user_id: yara_lee_7701)."
            "The customer needs to update their email address to yara.lee.new@example.com and add a new payment method because they got a new job. The payment method is a Visa credit card with the last four digits 8899. "
            "Help them update their profile, add the payment method, and assist with the most affordable t-shirt purchase using the recently added payment method."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yara", "last_name": "Lee", "user_id": "yara_lee_7701"}),
            Action(name="get_user_order_history", kwargs={"user_id": "yara_lee_7701"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "yara_lee_7701",
                "profile_updates": {
                    "email": "yara.lee.new@example.com"
                }
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "yara_lee_7701",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "8899"
                }
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "t-shirt",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "3234800602", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "yara_lee_7701"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "yara_lee_7701",
                "item_list": [
                    {"item_id": "3234800602", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_37701"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "yara_lee_7701",
                "items": [{"item_id": "3234800602", "quantity": 1}],
                "payment_method_sources": ["credit_card_37701"],
                "tax_amount": 3.73,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_47",
        instruction=(
            "You're Omar Lopez (omar_lopez_3107) a procurement assistant doing routine maintenance on supplier #SUP0005. "
            "Check their details, update their performance rating + feedback. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Omar", "last_name": "Lopez", "user_id": "omar_lopez_3107"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0005",
                "performance_rating": 2.0,
                "notes": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability."
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_48",
        instruction=(
            "You're Evelyn Hernandez (user_id: evelyn_hernandez_1701) and you're doing weekend shopping. "
            "You're doing weekend shopping and want to buy a black fleece jacket in large size and a cheap animal puzzle for family game night. "
            "Search for these items, check your payment options, and complete the purchase with your account."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Evelyn", "last_name": "Hernandez", "user_id": "evelyn_hernandez_1701"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "fleece jacket",
                "options": {"size": "L", "color": "black"},
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "jigsaw puzzle",
                "options": {"theme": "animals"},
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                    {"item_id": "9665100170", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "evelyn_hernandez_1701"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "evelyn_hernandez_1701",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                    {"item_id": "9665100170", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3631888"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "evelyn_hernandez_1701",
                "items": [
                    {"item_id": "9385662952", "quantity": 1},
                    {"item_id": "9665100170", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_3631888"],
                "tax_amount": 16.42,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_49",
        instruction=(
            "You're a customer service representative helping Chen Anderson (user_id: chen_anderson_8078). "
            "The customer is asking about their order status and wants to update their delivery address to 789 New Street, Apt 2B, Portland, OR, 97210, USA for future orders. "
            "Check their order history, validate their identity, and update their profile address."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Anderson", "user_id": "chen_anderson_8078"}),
            Action(name="get_user_order_history", kwargs={"user_id": "chen_anderson_8078"}),
            Action(name="check_order_status", kwargs={"order_id": "#W5332101"}),
            Action(name="check_order_status", kwargs={"order_id": "#W1701126"}),
            Action(name="check_order_status", kwargs={"order_id": "#W1348788"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "chen_anderson_8078",
                "profile_updates": {
                    "address": {
                        "address1": "789 New Street",
                        "address2": "Apt 2B",
                        "city": "Portland",
                        "state": "OR",
                        "zip": "97210",
                        "country": "USA"
                    }
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_50",
        instruction=(
            "You're Lei Khan (user_id: lei_khan_6353), an inventory coordinator setting up a new product line with supplier #SUP0008. You need to check their supplier details, update their rating based on recent evaluations, and update their contact email to newproducts@supplier8.com. Additionally, create a new supply order for 50 units to replace a cancelled order with product ID 6679515468, and update inventory stocks to add the new items."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lei", "last_name": "Khan", "user_id": "lei_khan_6353"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0008",
                "contact_updates": {
                    "email": "newproducts@supplier8.com"
                },
                "performance_rating": 2.0,
            }),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5916"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0008",
                "product_id": "6679515468",
                "item_id": "3230708338",
                "quantity": 50,
                "unit_cost": 63.6
            }),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0008",
                "item_id": "3230708338",
                "new_stock_level": 50,
                "stock_action": "add"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_51",
        instruction=(
            "You're Sofia Li (user_id: sofia_li_3261)"
            "You're a returning customer who wants to quickly buy a white cycling helmet within the budget of $210 because your old one broke. "
            "Search for small sized helmets, validate the item, check your saved payment methods, and complete a fast checkout to be delivered to your address. " \
            "The delivery will be fulfilled by Global Express Couriers"
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Sofia", "last_name": "Li", "user_id": "sofia_li_3261"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "cycling helmet",
                "options": {"size": "S", "color": "white"},
                "max_price": 210,
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1596993217", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "sofia_li_3261",
                "item_list": [
                    {"item_id": "1596993217", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_4046723"]
            }),
            Action(name="get_courier_by_name", kwargs={"courier_name": "Global Express Couriers"}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 194.42,
                                                           "courier_id": "#COU0010",
                                                           "location": {
                                                                "address1": "130 Hickory Lane",
                                                                "address2": "Suite 869",
                                                                "city": "New York",
                                                                "country": "USA",
                                                                "state": "NY",
                                                                "zip": "10199"
                                                            }}),
            Action(name="create_order", kwargs={
                "user_id": "sofia_li_3261",
                "items": [{"item_id": "1596993217", "quantity": 1}],
                "payment_method_sources": ["credit_card_4046723"],
                "tax_amount": 14.4,
                "shipping_cost": 11.49
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 205.91,
                                                  "courier_id": "#COU0010",
                                                  "location": {
                                                      "address1": "130 Hickory Lane",
                                                      "address2": "Suite 869",
                                                      "city": "New York",
                                                      "state": "NY",
                                                      "zip": "10199",
                                                      "country": "USA"
                                                  }}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_52",
        instruction=(
            "You're a customer service representative helping Emma Martin (user_id: emma_martin_6993). "
            "The customer has questions about their gift card balance and wants to make a purchase for LED Light Bulb with wifi connectivity but isn't sure if they have enough. "
            "Help them check their balance, find products within their budget, and assist with the purchase."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Martin", "user_id": "emma_martin_6993"}),
            Action(name="get_user_order_history", kwargs={"user_id": "emma_martin_6993"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "emma_martin_6993"}),
            Action(name="verify_gift_card_balance", kwargs={"first_name": "Emma", "last_name": "Martin", "user_id": "emma_martin_6993"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "led light bulb",
                "options": {"connectivity": "Wi-Fi"},
                "max_price": 57
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "7445824652", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "emma_martin_6993",
                "item_list": [
                    {"item_id": "7445824652", "quantity": 1}
                ],
                "payment_methods_source": ["gift_card_4129829"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "emma_martin_6993",
                "items": [{"item_id": "7445824652", "quantity": 1}],
                "payment_method_sources": ["gift_card_4129829"],
                "tax_amount": 3.98,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_53",
        instruction=(
            "You're Mason Li (mason_li_6934) a warehouse manager adjusting inventory levels for supplier #SUP0010 because of seasonal demand changes. "
            "Check their supplier details, review their capacity, update stock levels for recent orders to add 50 more units, "
            "and create new supply orders of the same amount to prepare for increased demand."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mason", "last_name": "Li", "user_id": "mason_li_6934"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0010",
                "item_id": "8591113813",
                "new_stock_level": 50,
                "stock_action": "add"
            }),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0010",
                "product_id": "7765186836",
                "item_id": "8591113813",
                "quantity": 50,
                "unit_cost": 109.11
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_54",
        instruction=(
            "You're Yara Martin user_id: yara_martin_9470, getting ready for outdoor "
            "adventures. Find hiking boots within a $240 budget and a fleece jacket within "
            "a $145 budget. Using your credit card, buy both items."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yara", "last_name": "Martin", "user_id": "yara_martin_9470"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "hiking boots",
                "max_price": 240,
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "fleece jacket",
                "max_price": 145,
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "8277474082", "quantity": 1},
                    {"item_id": "5992316252", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "yara_martin_9470"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "yara_martin_9470",
                "item_list": [
                    {"item_id": "8277474082", "quantity": 1},
                    {"item_id": "5992316252", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1006622"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "yara_martin_9470",
                "items": [
                    {"item_id": "8277474082", "quantity": 1},
                    {"item_id": "5992316252", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_1006622"],
                "tax_amount": 30.23,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_55",
        instruction=(
            "You're a customer service representative helping Olivia Khan user_id: "
            "olivia_khan_9030. The customer wants to ship clothing to 456 Maple Street, "
            "Suite 890, Vancouver, BC V6B 1A1, Canada. She has questions about international "
            "shipping costs. She needs to order the most expensive fleece jacket, calculate "
            "international shipping, and process the order using your visa credit card. Delivery "
            "will be handled by QuickShip Logistics."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Olivia", "last_name": "Khan", "user_id": "olivia_khan_9030"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "fleece jacket",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "olivia_khan_9030"}),
            Action(name="validate_shipping_address", kwargs={"user_id": "olivia_khan_9030",
                                                             "custom_address": {
                                                                 "address1": "456 Maple Street",
                                                                 "address2": "Suite 890",
                                                                 "city": "Vancouver",
                                                                 "state": "BC",
                                                                 "zip": "V6B 1A1",
                                                                 "country": "Canada"
                                                             }}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "QuickShip Logistics"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "olivia_khan_9030",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1936578"],
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "Canada", "total_items": 1, "order_value": 172.71,
                                                           "courier_id": "#COU0002",
                                                            "address": {
                                                                "address1": "456 Maple Street",
                                                                "address2": "Suite 890",
                                                                "city": "Vancouver",
                                                                "state": "BC",
                                                                "zip": "V6B 1A1",
                                                                "country": "Canada"
                                                            }}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "olivia_khan_9030",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1936578"],
                "shipping_cost": 26.49
            }),
            Action(name="create_order", kwargs={
                "user_id": "olivia_khan_9030",
                "items": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_1936578"],
                "tax_amount": 12.79,
                "shipping_cost": 26.49
            }),
            Action(name="assign_courier", kwargs={"destination_country": "Canada", "order_value": 199.2, "courier_id": "#COU0002",
                                                  "location": {
                                                       "address1": "456 Maple Street",
                                                        "address2": "Suite 890",
                                                        "city": "Vancouver",
                                                        "state": "BC",
                                                        "zip": "V6B 1A1",
                                                        "country": "Canada"}}),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_56",
        instruction=(
            "You're Liam Johnson (liam_johnson_5676) a vendor relations coordinator updating contact information for supplier #SUP0006. "
            "They've moved offices and changed their phone number and email to +1-800-555-0167 and newoffice@supplier6.com respectively. Update their details, check their current capacity, "
            "and create supply orders for the available running shoes (5 units each) being offered"
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Liam", "last_name": "Johnson", "user_id": "liam_johnson_5676"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0006",
                "contact_updates": {
                    "phone": "+1-800-555-0167",
                    "email": "newoffice@supplier6.com"
                },
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["running shoes"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["6938111410"],
                                                           "show_available": True,
                                                           "product_type": "running shoes"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0006",
                "product_id": "6938111410",
                "item_ids": ["4153505238", "9635758562", "9791469541", "4107812777"],
                "quantity": 5,
                "unit_cost": [158.67, 148.95, 147.05, 155.33]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_57",
        instruction=(
            "You're Amelia Kim (user_id: amelia_kim_4338). "
            "You're setting up a new kitchen and want to buy a automatic espresso machine and 3 piece luggage for an upcoming trip. "
            "You have a budget $500 for the luggage and a $2700-$2800 budget for the espresso machine. "
            "Search for these items, validate your identity, check availability, and complete the purchase using your paypal account."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Amelia", "last_name": "Kim", "user_id": "amelia_kim_4338"}),\
            Action(name="search_products_by_filter", kwargs={
                "category": "espresso machine",
                "options": {"type": "automatic"},
                "min_price": 2700,
                "max_price": 2800,
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "luggage set",
                "options": {"piece count": "3-piece"},
                "max_price": 500,
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "3709608322", "quantity": 1},
                    {"item_id": "6301799585", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "amelia_kim_4338"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "amelia_kim_4338",
                "item_list": [
                    {"item_id": "3709608322", "quantity": 1},
                    {"item_id": "6301799585", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_1742092"]
            }),
            Action(name="process_payment", kwargs={
                "user_id": "amelia_kim_4338",
                "payment_method_source": "paypal_1742092",
                "amount": 3499.82
            }),
            Action(name="create_order", kwargs={
                "user_id": "amelia_kim_4338",
                "items": [
                    {"item_id": "3709608322", "quantity": 1},
                    {"item_id": "6301799585", "quantity": 1}
                ],
                "payment_method_sources": ["paypal_1742092"],
                "tax_amount": 259.25,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_58",
        instruction=(
            "You're a customer service representative helping Juan Martin (user_id: juan_martin_4740) "
            "The customer got a new mastercard credit card with last four digits 5678 and wants to update their payment methods, then make a purchase for a black dialed silicone wristwatch. "
            "Help them add the new payment method,  and assist with the order."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Martin", "user_id": "juan_martin_4740"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "juan_martin_4740"}),
            Action(name="add_payment_method", kwargs={
                "user_id": "juan_martin_4740",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "mastercard",
                    "last_four": "5678"
                }
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "wristwatch",
                "options": {"strap material": "silicone", "dial color": "black"},
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1994478369", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_martin_4740",
                "item_list": [
                    {"item_id": "1994478369", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_24740"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "juan_martin_4740",
                "items": [{"item_id": "1994478369", "quantity": 1}],
                "payment_method_sources": ["credit_card_24740"],
                "tax_amount": 162.04,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_59",
        instruction=(
            "You're Isabella Brown (user_id: isabella_brown_4999), a seasonal planning manager preparing inventory for sneaker sales with supplier #SUP0003. "
            "Review the supplier's details, update their performance metrics based on recent reviews, "
            "check their sneaker capacity, and create one supply order of 10 units for each available sneaker variant they offer."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Isabella", "last_name": "Brown", "user_id": "isabella_brown_4999"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0003",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["sneakers"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["7471004230"],
                                                           "show_available": True,
                                                           "product_type": "sneakers"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0003",
                "product_id": "7471004230",
                "item_ids": ['2509076505', '6477915553'],
                "quantity": 10,
                "unit_cost": [189.5, 186.45]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_60",
        instruction=(
            "You're Mohamed Jackson (user_id: mohamed_jackson_1549). "
            "You want to upgrade your old electronics with a new and expensive smartphone and wireless headphones. "
            "Search for these items, validate them, check your payment options, and complete the upgrade purchase."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mohamed", "last_name": "Jackson", "user_id": "mohamed_jackson_1549"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "smartphone",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "headphones",
                "options": {"connectivity": "wireless"},
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "1507389580", "quantity": 1},
                    {"item_id": "3104857380", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "mohamed_jackson_1549"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "mohamed_jackson_1549",
                "item_list": [
                    {"item_id": "1507389580", "quantity": 1},
                    {"item_id": "3104857380", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3313158"]
            }),
            Action(name="process_payment", kwargs={
                "user_id": "mohamed_jackson_1549",
                "payment_method_source": "credit_card_3313158",
                "amount": 1658.7
            }),
            Action(name="create_order", kwargs={
                "user_id": "mohamed_jackson_1549",
                "items": [
                    {"item_id": "1507389580", "quantity": 1},
                    {"item_id": "3104857380", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_3313158"],
                "tax_amount": 122.87,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_61",
        instruction=(
            "You're a customer service representative helping Daiki Johnson (user_id: daiki_johnson_9523). "
            "The customer placed an order under #W1436802 but wants to modify it by adding a 24MP digital camera with 3x zoom before it ships. "
            "Check their current order, help them add the new item, and update the order accordingly."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Johnson", "user_id": "daiki_johnson_9523"}),
            Action(name="get_user_order_history", kwargs={"user_id": "daiki_johnson_9523"}),
            Action(name="check_order_status", kwargs={"order_id": "#W1436802"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "digital camera",
                "options": {"resolution": "24MP", "zoom": "3x"},
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5996159312", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "daiki_johnson_9523"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "daiki_johnson_9523",
                "item_list": [
                    {"item_id": "5996159312", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_2433177"]
            }),
            Action(name="add_to_order", kwargs={
                "order_id": "#W1436802",
                "item_id": "5996159312",
                "payment_method": "paypal_2433177",
                "tax_amount": 231.64,
                "quantity": 1
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_62",
        instruction=(
            "You're Evelyn Lee a category manager expanding the electronics product line with supplier #SUP0009. "
            "Review their current offerings, check their capacity, update the supplier email to thenewemail@example.com, "
            "and create supply orders of 5 units each for all the available products they can provide."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Evelyn", "last_name": "Lee"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0009",
                "contact_updates": {
                    "email": "thenewemail@example.com"
                },
            }),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["7996920482", "1075968781", "4354588079", "9832717871"],
                                                           "show_available": True}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "7996920482",
                "item_ids": ["3020722515", "9862136885", "5952720925", "7211586944", "1349017811"],
                "quantity": 5,
                "unit_cost": [238.64, 258.32, 260.19, 272.71, 226.05]
            }),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "1075968781",
                "item_ids": ["4064702754", "5428723833", "1240311797", "9472539378", "2323972008", "9624127908", "4458619711", "7602931732"],
                "quantity": 5,
                "unit_cost": [159.78, 145.48, 137.17, 143.72, 146.98, 158.9, 153.81, 153.25]
            }),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "4354588079",
                "item_ids": ["3709608322", "7407838442", "1157853815", "2190871011", "3714494375", "3815173328", "7774234341", "3951031513", "9884666842", "3379843752"],
                "quantity": 5,
                "unit_cost":[2744.7, 3081.91, 3096.7, 3105.6, 2709.83, 2908.42, 2719.16, 3289.46, 2794.7, 3203.76]
            }),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "9832717871",
                "item_ids": ["3909406921", "2820119811", "3761330360", "7292993796", "9747045638", "3312883418", "1906487464", "3738831434", "8293778132"],
                "quantity": 5,
                "unit_cost":[98.25, 94.68, 101.12, 94.8, 94.01, 104.82, 102.02, 98.89, 100.62]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_63",
        instruction=(
            "You're Olivia Sanchez. You're buying expensive gifts for your family: a bicycle for your son and a cycling helmet for safety. "
            "Search for these items, validate them, complete the holiday purchase using paypal and have it delivered to your location using Reliable Delivery Co."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Olivia", "last_name": "Sanchez"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "bicycle",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "cycling helmet",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "olivia_sanchez_2914"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "Reliable Delivery Co."}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "olivia_sanchez_2914",
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_3388537"],
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 2608.11,
                                                           "courier_id": "#COU0009",
                                                            "location": {
                                                                "address1": "710 Sunset Drive",
                                                                "address2": "Suite 855",
                                                                "city": "Philadelphia",
                                                                "country": "USA",
                                                                "state": "PA",
                                                                "zip": "19116"
                                                            }}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "olivia_sanchez_2914",
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_3388537"],
                "shipping_cost": 53.11,
            }),
            Action(name="process_payment", kwargs={
                "user_id": "olivia_sanchez_2914",
                "payment_method_source": "paypal_3388537",
                "amount": 2661.22
            }),
            Action(name="create_order", kwargs={
                "user_id": "olivia_sanchez_2914",
                "items": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_method_sources": ["paypal_3388537"],
                "tax_amount": 193.19,
                "shipping_cost": 53.11
            }),
            Action(name="assign_tracking_number", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0009"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 2661.22, "courier_id": "#COU0009",
                                                  "tracking_ids": ["TRKBATCH01C0009"],
                                                  "location": {
                                                      "address1": "710 Sunset Drive",
                                                      "address2": "Suite 855",
                                                      "city": "Philadelphia",
                                                      "country": "USA",
                                                      "state": "PA",
                                                      "zip": "19116"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_64",
        instruction=(
            "You're Emma Ito (user_id: emma_ito_4529). "
            "You placed an order yesterday but forgot to add a small red fleece jacket. You want to add it to your existing order #W8664580 "
            "before it ships. Validate your identity, check your order history, add the fleece jacket to your existing order, "
            "and add it to your existing order using your visa."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Ito", "user_id": "emma_ito_4529"}),
            Action(name="get_user_order_history", kwargs={"user_id": "emma_ito_4529"}),
            Action(name="check_order_status", kwargs={"order_id": "#W8664580"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "fleece jacket",
                "options": {"size": "S", "color": "red"},
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5992316252", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "emma_ito_4529"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "emma_ito_4529",
                "item_list": [
                    {"item_id": "5992316252", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8058445"]
            }),
            Action(name="add_to_order", kwargs={
                "order_id": "#W8664580",
                "item_id": "5992316252",
                "payment_method": "credit_card_8058445",
                "tax_amount": 11.3,
                "quantity": 1
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_65",
        instruction=(
            "You're a customer service representative helping Ivan Santos (user_id: ivan_santos_6635). "
            "The customer wants to know what products they bought in their recent orders. "
            "They want to cancel the office chair ordered due to a change in circumstances."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ivan", "last_name": "Santos", "user_id": "ivan_santos_6635"}),
            Action(name="get_user_order_history", kwargs={"user_id": "ivan_santos_6635"}),
            Action(name="get_product_ids", kwargs={
                "user_id": "ivan_santos_6635",
                "order_ids": ["#W6893533", "#W8770097", "#W5183325", "#W3913498"],
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["office chair"],
                                                                         "product_ids": ['1656367028', '1968349452', '2696197613', '4794339885',
                                                                                         '6679515468', '6945232052', '8940227892', '9924732112']}),
            Action(name="get_order_ids_by_product_ids", kwargs={"product_ids": ["4794339885"], "user_id": "ivan_santos_6635"}),
            Action(name="cancel_order", kwargs={"user_id": "ivan_santos_6635", "order_id": "#W8770097", "cancellation_reason": "change in circumstances"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_66",
        instruction=(
            "You're Fatima Garcia a procurement manager adding a new product line to supplier #SUP0011's portfolio. "
            "They want to start supplying kitchen appliances, specifically available espresso machines. You need to create supply orders (10 units each) "
            "for all variants of the espresso machine. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Fatima", "last_name": "Garcia"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["espresso machine"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["4354588079"],
                                                           "show_available": True,
                                                           "product_type": "espresso machine"}),
             Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0011",
                "product_id": "4354588079",
                "item_ids": ["3709608322", "7407838442", "1157853815", "2190871011", "3714494375", "3815173328", "7774234341", "3951031513", "9884666842", "3379843752"],
                "quantity": 10,
                "unit_cost":[2744.7, 3081.91, 3096.7, 3105.6, 2709.83, 2908.42, 2719.16, 3289.46, 2794.7, 3203.76]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_67",
        instruction=(
            "You're Anya Garcia (user_id: anya_garcia_3271). "
            "You want to review your purchase history to see the laptop you've bought. "
            "Get your order history, check your payment methods, and create another order for the same laptop you have purchased."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "anya_garcia_3271"}),
            Action(name="get_user_order_history", kwargs={"user_id": "anya_garcia_3271"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "anya_garcia_3271"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "anya_garcia_3271",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8955149"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "anya_garcia_3271",
                "items": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_8955149"],
                "tax_amount": 183.39,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_68",
        instruction=(
            "You're a customer service representative helping Evelyn Ahmed (user_id: evelyn_ahmed_3960). "
            "The customer moved to a new address at 789 Mountain View Drive, Apt 3A, Denver, CO 80218, USA and wants to update their profile. "
            "They also want to add a new gift card with a balance of $500 and validate that it reflects in their account."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Evelyn", "last_name": "Ahmed", "user_id": "evelyn_ahmed_3960"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "evelyn_ahmed_3960",
                "profile_updates": {
                    "address": {
                        "address1": "789 Mountain View Drive",
                        "address2": "Apt 3A",
                        "city": "Denver",
                        "state": "CO",
                        "zip": "80218",
                        "country": "USA"
                    }
                }
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "evelyn_ahmed_3960",
                "payment_type": "gift_card",
                "payment_details":{
                    "balance": 500
                }
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "evelyn_ahmed_3960"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_69",
        instruction=(
            "You're Emma Kovacs (emma_kovacs_9839) a category manager reviewing supplier #SUP0010's portfolio and considering adding new t-shirt items. "
            "Review their current details, check their capacity, search for suppliers of available similar products that have at least 20 units in stock and create an order "
            "of 20 units for each of the variants available. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Kovacs", "user_id": "emma_kovacs_9839"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["t-shirt"]}),
            Action(name="search_suppliers_by_product", kwargs={
                "product_id": "9523456873",
                "product_type": ["t-shirt"],
                "min_stock_level": 20
            }),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["9523456873"],
                                                           "show_available": True,
                                                           "product_type": "t-shirt"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0001",
                "product_id": "9523456873",
                "item_ids": ["9612497925", "8124970213", "1176194968", "9647292434", "8349118980", "3799046073", "2060066974"],
                "quantity": 20,
                "unit_cost":[50.88, 49.67, 52.88, 53.48, 53.43, 53.27, 51.05]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_70",
        instruction=(
            "You're Lucas Johnson (user_id: lucas_johnson_2067) "
            "You want to check your recent order #W7016806 and consider placing another order of water bottle. "
            "Check your order history, validate your payment methods, search for another water bottle with the same color but is made of up stainless steel, "
            "validate it and complete a new purchase using your credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lucas", "last_name": "Johnson", "user_id": "lucas_johnson_2067"}),
            Action(name="get_user_order_history", kwargs={"user_id": "lucas_johnson_2067"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "lucas_johnson_2067"}),
            Action(name='get_product_info', kwargs={"item_id": "5758737025"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "water bottle",
                "options": {"color": "green", "material": "stainless steel"},
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "7533802601", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "lucas_johnson_2067",
                "item_list": [
                    {"item_id": "7533802601", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3956549"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "lucas_johnson_2067",
                "items": [
                    {"item_id": "7533802601", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_3956549"],
                "tax_amount": 3.89,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_71",
        instruction=(
            "You're a customer service representative helping Juan Anderson (user_id: juan_anderson_5671). "
            "The customer wants help finding an action camera with 5k resolution and in black. They need recommendations, want to add his visa with last four digits 7890 as a new payment method, "
            "validate the order, payment methods, and complete the purchase. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Anderson", "user_id": "juan_anderson_5671"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "action camera",
                "options": {"resolution": "5k", "color": "black"},
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "juan_anderson_5671",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "7890"
                }
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "juan_anderson_5671"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "7523669277", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "juan_anderson_5671",
                "item_list": [
                    {"item_id": "7523669277", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_25671"]
            }),
            Action(name="create_order", kwargs={
                "user_id": "juan_anderson_5671",
                "items": [
                    {"item_id": "7523669277", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_25671"],
                "tax_amount": 41.89,
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_72",
        instruction=(
            "You're Harper Kim (harper_kim_2998) a vendor manager enhancing supplier #SUP0010's sports equipment portfolio. "
            "They want to expand their cycling product line beyond just helmets. Review their capacity, update their information based on their recent performance, "
            "and set up new supply orders of 35 units each for the available variants of the bicycles."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "harper_kim_2998"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0010",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["bicycle"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["9783735446"],
                                                           "show_available": True,
                                                           "product_type": "bicycle"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0010",
                "product_id": "9783735446",
                "item_ids": ['7758198585', '5606522780', '3624655057', '2143041831'],
                "quantity": 35,
                "unit_cost":[1917.21, 1902.67, 2195.04, 2076.5]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_73",
        instruction=(
            "You're Daiki Johnson user_id: daiki_johnson_6200. You're setting up a home "
            "office and want to buy a laptop and a gaming mouse. Search for products by "
            "name. Your preference is to find the cheapest options available. Validate "
            "items, check your payment methods, and complete the purchase using your credit "
            "card. This should be delivered to your address using SwiftMove Couriers."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Johnson", "user_id": "daiki_johnson_6200"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "laptop",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="search_products_by_filter", kwargs={
                "category": "gaming mouse",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "daiki_johnson_6200"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "SwiftMove Couriers"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "daiki_johnson_6200",
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8934029"]
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 2623.96,
                                                           "courier_id": "#COU0004",
                                                            "location": {
                                                                "address1": "375 Elm Avenue",
                                                                "address2": "Suite 947",
                                                                "city": "Phoenix",
                                                                "country": "USA",
                                                                "state": "AZ",
                                                                "zip": "85017"
                                                            }}),
            Action(name="create_order", kwargs={
                "user_id": "daiki_johnson_6200",
                "items": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_8934029"],
                "tax_amount": 194.37,
                "shipping_cost": 53.35
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 2677.31, "courier_id": "#COU0004",
                                                  "location": {
                                                       "address1": "375 Elm Avenue",
                                                        "address2": "Suite 947",
                                                        "city": "Phoenix",
                                                        "country": "USA",
                                                        "state": "AZ",
                                                        "zip": "85017"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_74",
        instruction=(
            "You're Chen Johnson (user_id: chen_johnson_4204). "
            "You want to purchase a smart watch for fitness tracking with your gift card and PayPal as backup payment. "
            "Search for gold smart watches with AMOLED display under $350, validate availability and address, create the order, and use NextDay Couriers for delivery to his address."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Chen", "last_name": "Johnson", "user_id": "chen_johnson_4204"}),
            Action(name="search_products_by_filter", kwargs={"category": "smart watch", "max_price": 350,
                                                             "options": {
                                                                "color": "gold",
                                                                "display": "AMOLED",
                                                            }}),
            Action(name="get_product_info", kwargs={"item_id": "5694328282"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "5694328282", "quantity": 1}]}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "chen_johnson_4204"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "NextDay Couriers"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "chen_johnson_4204",
                "item_list": [{"item_id": "5694328282", "quantity": 1}],
                "payment_methods_source": ["gift_card_3406421", "paypal_3742148"],
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 349.05,
                                                           "courier_id": "#COU0008",
                                                            "location": {
                                                                "address1": "503 Elm Avenue",
                                                                "address2": "Suite 641",
                                                                "city": "Houston",
                                                                "country": "USA",
                                                                "state": "TX",
                                                                "zip": "77004"
                                                            }}),
            Action(name="create_order", kwargs={
                "user_id": "chen_johnson_4204",
                "items": [
                    {"item_id": "5694328282", "quantity": 1}
                ],
                "payment_method_sources": ["gift_card_3406421", "paypal_3742148"],
                "tax_amount": 25.86,
                "shipping_cost": 11.49
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 360.54, "courier_id": "#COU0008",
                                                  "location": {
                                                        "address1": "503 Elm Avenue",
                                                        "address2": "Suite 641",
                                                        "city": "Houston",
                                                        "country": "USA",
                                                        "state": "TX",
                                                        "zip": "77004"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_75",
        instruction=(
            "You're a customer service representative helping Sofia Rossi (user_id: sofia_rossi_8776). "
            "She needs to update her pending deliveries to her new office at 1000 Market Street, Suite 500, Philadelphia, PA 19107, USA. "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Sofia", "last_name": "Rossi", "user_id": "sofia_rossi_8776"}),
            Action(name="get_user_order_history", kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="update_delivery_address", kwargs={
                "user_id": "sofia_rossi_8776",
                "order_id": "#W5918442",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Philadelphia",
                    "state": "PA",
                    "zip": "19107",
                    "country": "USA"
                }
            }),
            Action(name="update_delivery_address", kwargs={
                "user_id": "sofia_rossi_8776",
                "order_id": "#W5500815",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Philadelphia",
                    "state": "PA",
                    "zip": "19107",
                    "country": "USA"
                }
            }),
            Action(name="update_delivery_address", kwargs={
                "user_id": "sofia_rossi_8776",
                "order_id": "#W2818151",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Philadelphia",
                    "state": "PA",
                    "zip": "19107",
                    "country": "USA"
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_76",
        instruction=(
            "You're Olivia Smith (user_id: olivia_smith_5265) a supply chain manager for the retail company. "
            "Supplier #SUP0008 needs inventory updates for led lighting products. Check their current details, update contact email to 'support@smartlighting.com', "
            "verify their available led lighting inventory levels, and ensure to add 50 units stock for each available variant."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Olivia", "last_name": "Smith", "user_id": "olivia_smith_5265"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0008",
                "contact_updates": {"email": "support@smartlighting.com"}
            }),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["led light bulb"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["2696197613"],
                                                           "show_available": True,
                                                           "product_type": "led light bulb"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0008",
                "item_ids": [
                    "7445824652", "5570660360", "4938013542"
                ],
                "new_stock_level": 50,
                "stock_action": "add"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_77",
        instruction=(
            "You're Amelia Wilson (user_id: amelia_wilson_4614). "
            "You want to return the dumbbell because it arrived damaged. You need to request for a return of the order, "
            "and get the shipping cost from the same courier that delivered it."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Amelia", "last_name": "Wilson", "user_id": "amelia_wilson_4614"}),
            Action(name="get_user_order_history", kwargs={"user_id": "amelia_wilson_4614"}),
            Action(name="get_purchased_items", kwargs={"user_id": "amelia_wilson_4614", "order_id": "#W9077205"}),
            Action(name="get_courier", kwargs={"tracking_id": "882867966563"}),
            Action(name="request_order_return", kwargs={
                "user_id": "amelia_wilson_4614",
                "order_id": "#W9077205",
                "return_items": [
                    {"item_id": "3877338112", "quantity": 1, "reason": "arrived damaged"},
                ],
                "return_reason": "arrived damaged"
            }),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "new_status": "for return"}),
            Action(name="validate_shipping_address", kwargs={"user_id": "amelia_wilson_4614"}),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 545.68,
                                                           "courier_id": "#COU0009"}),
        ],
        outputs=[
            '"shipping_cost": "11.49"',
        ]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_78",
        instruction=(
            "You're a customer service representative assisting Ivan Khan (user_id: ivan_khan_7475), "
            "who needs clarification about his order fulfillment status. Ivan wants to ensure his "
            "pending orders are progressing toward delivery and has expressed preference for OnTime "
            "Delivery Solutions as his courier service. Your objective is to provide Ivan with a "
            "comprehensive status update and facilitate efficient order processing that meets his "
            "delivery preferences while following standard operational procedures."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={
                "first_name": "Ivan",
                "last_name": "Khan",
                "user_id": "ivan_khan_7475"
            }),
            Action(name="get_user_order_history", kwargs={
                "user_id": "ivan_khan_7475"
            }),
            Action(name="get_courier_by_name", kwargs={
                "courier_name": "OnTime Delivery Solutions"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W5270061"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W7032009"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W1519594"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W5782623"
            }),
            Action(name="assign_tracking_number", kwargs={
                "order_ids": ["#W5270061", "#W7032009", "#W5782623"],
                "preferred_courier_id": "#COU0007"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_79",
        instruction=(
            "You're Juan Smith (user_id: juan_smith_5229) a procurement specialist for the retail company. "
            "You need to manage supplier #SUP0001 relationships. Check their performance, update their phone to '+1-555-0123' and performance rating to 5.0. "
            "Create new supply orders for available t-shirts at exactly 40 units for each item variant."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_smith_5229"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="validate_supplier_capacity", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0001",
                "contact_updates": {"phone": "+1-555-0123"},
                "performance_rating": 5.0,
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["t-shirt"]}),
            Action(name="search_suppliers_by_product", kwargs={
                "product_id": "9523456873",
                "supplier_id": "#SUP0001",
                "product_type": ["t-shirt"]
            }),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["9523456873"],
                                                           "show_available": True,
                                                           "product_type": "t-shirt"}),
            Action(name="create_supply_order", kwargs={
                "supplier_id": "#SUP0001",
                "product_id": "9523456873",
                "item_ids": ['9612497925', '8124970213', '1176194968', '9647292434', '8349118980', '3799046073', '2060066974'],
                "quantity": 40,
                "unit_cost":[50.88, 49.67, 52.88, 53.48, 53.43, 53.27, 51.05]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_80",
        instruction=(
            "You're Ethan Khan (user_id: ethan_khan_3904). "
            "You need a laptop for work with specific requirements: 15-inch screen, i7 processor, 32GB RAM, under $2800 budget. "
            "Search for available options, validate specifications, create order with your credit card, and ensure it is delivered to you by SpeedyShip Couriers."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Ethan", "last_name": "Khan", "user_id": "ethan_khan_3904"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "laptop",
                "options": {"screen size": "15-inch", "processor": "i7", "ram": "32GB"},
                "max_price": 2800,
            }),
            Action(name="get_product_info", kwargs={"item_id": "6017636844"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "ethan_khan_3904"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "SpeedyShip Couriers"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "ethan_khan_3904",
                "item_list": [{"item_id": "6017636844", "quantity": 1}],
                "payment_methods_source": ["credit_card_5608852"]
            }),
            Action(name="calculate_shipping_cost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 2475.76,
                                                           "courier_id": "#COU0006",
                                                            "location": {
                                                                "address1": "264 Elm Street",
                                                                "address2": "Suite 579",
                                                                "city": "San Diego",
                                                                "country": "USA",
                                                                "state": "CA",
                                                                "zip": "92117"
                                                            }}),
            Action(name="create_order", kwargs={
                "user_id": "ethan_khan_3904",
                "items": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_5608852"],
                "tax_amount": 183.39,
                "shipping_cost": 48.63
            }),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 2524.39, "courier_id": "#COU0006",
                                                  "location": {
                                                        "address1": "264 Elm Street",
                                                        "address2": "Suite 579",
                                                        "city": "San Diego",
                                                        "country": "USA",
                                                        "state": "CA",
                                                        "zip": "92117"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_81",
        instruction=(
            "You're assisting Sophia Garcia (user_id: sophia_garcia_5795) with shipping "
            "logistics for her recent orders #W4958652 and #W6447372. She's moved to a new "
            "address and wants to consolidate shipping using SpeedyShip Couriers for both "
            "orders. Your objective is to ensure both orders are properly configured for "
            "delivery to her current address and ready for shipment processing with her "
            "preferred courier service."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={
                "first_name": "Sophia",
                "last_name": "Garcia",
                "user_id": "sophia_garcia_5795"
            }),
            Action(name="get_user_order_history", kwargs={
                "user_id": "sophia_garcia_5795"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W4958652"
            }),
            Action(name="check_order_status", kwargs={
                "order_id": "#W6447372"
            }),
            Action(name="get_courier_by_name", kwargs={
                "courier_name": "SpeedyShip Couriers"
            }),
            Action(name="validate_shipping_address", kwargs={
                "user_id": "sophia_garcia_5795"
            }),
            Action(name="update_delivery_address", kwargs={
                "user_id": "sophia_garcia_5795",
                "order_id": "#W4958652",
                "new_address": {
                    "address1": "536 Cedar Street",
                    "address2": "Suite 916",
                    "city": "Charlotte",
                    "country": "USA",
                    "state": "NC",
                    "zip": "28212"
                }
            }),
            Action(name="assign_tracking_number", kwargs={
                "order_ids": ["#W4958652", "#W6447372"],
                "preferred_courier_id": "#COU0006"
            })
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_82",
        instruction=(
            "You're Yusuf Taylor (user_id: yusuf_taylor_7149) a cost analyst for the retail company. "
            "Supply order #SO6035 needs cost adjustments. Check current terms, update unit cost to $28.50, change payment terms to 'COD', "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yusuf", "last_name": "Taylor", "user_id": "yusuf_taylor_7149"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="update_supply_order_terms", kwargs={
                "supply_order_id": "#SO6035",
                "new_unit_cost": 28.50,
                "payment_terms": "COD"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_83",
        instruction=(
            "You're Yusuf Moore (user_id: yusuf_moore_6437) and you need an electric toothbrush with high-speed settings and a rechargeable battery. Search for available options, validate your stored address, and complete the purchase using your credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yusuf", "last_name": "Moore", "user_id": "yusuf_moore_6437"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "electric toothbrush",
                "options": {"speed settings": "high", "battery type": "rechargeable"},
            }),
            Action(name="get_product_info", kwargs={"item_id": "8098621301"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "8098621301", "quantity": 1}]}),
            Action(name="validate_shipping_address", kwargs={"user_id": "yusuf_moore_6437"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "yusuf_moore_6437"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "yusuf_moore_6437",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["credit_card_6302410"]
            }),
            Action(name="process_payment", kwargs={"user_id": "yusuf_moore_6437", "payment_method_source": "credit_card_6302410", "amount": 207.52}),
            Action(name="create_order", kwargs={
                "user_id": "yusuf_moore_6437",
                "items": [{"item_id": "8098621301", "quantity": 1}],
                "payment_method_sources": ["credit_card_6302410"],
                "tax_amount": 15.37
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_84",
        instruction=(
            "You're a customer service representative helping Lei Ahmed user_id: "
            "lei_ahmed_1705. Check the status of order #W9015076, and if it's pending, "
            "add the cheapest garden hose you can find to the order. Once added, update "
            "the order status to processed."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Lei", "last_name": "Ahmed", "user_id": "lei_ahmed_1705"}),
            Action(name="get_user_order_history", kwargs={"user_id": "lei_ahmed_1705"}),
            Action(name="check_order_status", kwargs={"order_id": "#W9015076"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "garden hose",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "9829827210", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "lei_ahmed_1705"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "lei_ahmed_1705",
                "item_list": [
                    {"item_id": "9829827210", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3593714"]
            }),
            Action(name="add_to_order", kwargs={
                "order_id": "#W9015076",
                "item_id": "9829827210",
                "payment_method": "credit_card_3593714",
                "tax_amount": 7.23,
                "quantity": 1
            }),
            Action(name="update_order_status", kwargs={"order_id": "#W9015076", "new_status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_85",
        instruction=(
            "You're Juan Smith (user_id: juan_smith_9901), a warehouse manager for the "
            "retail company. Check supplier #SUP0011's inventory for electric toothbrush "
            "products, get available items that have below than 50 stock units and set "
            "their stock levels to 50. Also update unavailable items back to available. "
            "Update the contact phone number to '+1-800-555-0089'."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_smith_9901"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="get_supplier_inventory", kwargs={"supplier_id": "#SUP0011", "product_types": ["electric toothbrush"], "stock_level": 50,
                                                          "stock_level_comparison": "below"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0011",
                "item_id": "8098621301",
                "new_stock_level": 50,
                "stock_action": "set"
            }),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0011",
                "item_id": "3320557165",
                "new_stock_level": 50,
                "stock_action": "set"
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "7352963235",
                "item_id": "3320557165",
                "available": True
            }),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0011",
                "contact_updates": {"phone": "+1-800-555-0089"}
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_86",
        instruction=(
            "You're Omar Moore (user_id: omar_moore_9540), a warehouse employee for the "
            "retail company. Update supplier #SUP0011's contact phone number to "
            "'+1-800-555-0089' and email to 'supplierameile@example.com', and verify "
            "the changes."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Omar", "last_name": "Moore", "user_id": "omar_moore_9540"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0011",
                "contact_updates": {"phone": "+1-800-555-0089", "email": "supplierameile@example.com"}
            }),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_87",
        instruction=(
            "You're Emma Rossi (user_id: emma_rossi_2839). You want to buy a red "
            "Bluetooth speaker with water resistance and 20-hour battery life for your "
            "outdoor activities. Search for available speakers and order the item."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Rossi", "user_id": "emma_rossi_2839"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "bluetooth speaker",
                "options": {"battery life": "20 hours",
                            "color": "red",
                            "water resistance": "yes"
                           },
            }),
            Action(name="get_product_info", kwargs={"item_id": "7617930199"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "7617930199", "quantity": 1}]}),
            Action(name="validate_shipping_address", kwargs={"user_id": "emma_rossi_2839"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "emma_rossi_2839"}),
            Action(name="process_payment", kwargs={"user_id": "emma_rossi_2839", "payment_method_source": "paypal_3824028", "amount": 285.94}),
            Action(name="create_order", kwargs={
                "user_id": "emma_rossi_2839",
                "items": [{"item_id": "7617930199", "quantity": 1}],
                "payment_method_sources": ["paypal_3824028"],
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_88",
        instruction=(
            "You're a customer service representative assisting Amelia Ito "
            "(user_id: amelia_ito_8772) as she moves in with Emma Ito "
            "(user_id: emma_ito_4529). Update her delivery address and change her "
            "email to 'amelia2@example.com'."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Amelia", "last_name": "Ito", "user_id": "amelia_ito_8772"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Emma", "last_name": "Ito", "user_id": "emma_ito_4529"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "amelia_ito_8772",
                "profile_updates": {
                    "email": "amelia2@example.com",
                    "address": {
                        "address1": "965 Broadway",
                        "address2": "Suite 140",
                        "city": "Philadelphia",
                        "country": "USA",
                        "state": "PA",
                        "zip": "19022"
                    }
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_89",
        instruction=(
            "You're Yusuf Garcia (user_id: yusuf_garcia_5427) and you want to add "
            "multiple payment methods to your account. Add a Visa card ending in 1111 "
            "and a Mastercard ending in 2222."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Yusuf", "last_name": "Garcia", "user_id": "yusuf_garcia_5427"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "yusuf_garcia_5427"}),
            Action(name="add_payment_method", kwargs={
                "user_id": "yusuf_garcia_5427",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1111"
                }
            }),
            Action(name="add_payment_method", kwargs={
                "user_id": "yusuf_garcia_5427",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "mastercard",
                    "last_four": "2222"
                }
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "yusuf_garcia_5427"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_90",
        instruction=(
            "You're a customer service representative helping Fatima Anderson "
            "(user_id: fatima_anderson_2157). She wants to cancel all her pending "
            "orders due to personal reasons."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Fatima", "last_name": "Anderson", "user_id": "fatima_anderson_2157"}),
            Action(name="get_user_order_history", kwargs={"user_id": "fatima_anderson_2157"}),
            Action(name="check_order_status", kwargs={"order_id": "#W2974929"}),
            Action(name="check_order_status", kwargs={"order_id": "#W4111294"}),
            Action(name="check_order_status", kwargs={"order_id": "#W4514908"}),
            Action(name="cancel_order", kwargs={
                "user_id": "fatima_anderson_2157",
                "order_id": "#W2974929",
                "cancellation_reason": "personal reasons"
            }),
            Action(name="cancel_order", kwargs={
                "user_id": "fatima_anderson_2157",
                "order_id": "#W4514908",
                "cancellation_reason": "personal reasons"
            }),
            Action(name="check_order_status", kwargs={"order_id": "#W2974929"}),
            Action(name="check_order_status", kwargs={"order_id": "#W4514908"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_91",
        instruction=(
            "You're Harper Moore user_id: harper_moore_7767, a cost analyst for the "
            "retail company. Supply orders from supplier #SUP0011 need updates. Update and verify"
            "all pending and cancelled supply orders' pricing terms to 'NET30'."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Harper", "last_name": "Moore", "user_id": "harper_moore_7767"}),
            Action(name="search_get_supply_orders", kwargs={"supplier_ids": ["#SUP0011"], "statuses": ["pending", "cancelled"]}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="update_supply_order_terms", kwargs={
                "supply_order_id": "#SO6998",
                "payment_terms": "NET30"
            }),
            Action(name="update_supply_order_terms", kwargs={
                "supply_order_id": "#SO2377",
                "payment_terms": "NET30"
            }),
            Action(name="update_supply_order_terms", kwargs={
                "supply_order_id": "#SO5398",
                "payment_terms": "NET30"
            }),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO2377"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5398"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_92",
        instruction=(
            "You're Evelyn Ahmed user_id: evelyn_ahmed_3960. You need a 6mm yoga mat "
            "for your home workouts. Find available options in your preferred "
            "thickness, validate the item, and purchase using your credit card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Evelyn", "last_name": "Ahmed", "user_id": "evelyn_ahmed_3960"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "yoga mat",
                "options": {"thickness": "6mm"},
            }),
            Action(name="get_product_info", kwargs={"item_id": "7510236436"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "7510236436", "quantity": 1}]}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "evelyn_ahmed_3960"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "evelyn_ahmed_3960",
                "item_list": [{"item_id": "7510236436", "quantity": 1}],
                "payment_methods_source": ["credit_card_7898168"]
            }),
            Action(name="process_payment", kwargs={"user_id": "evelyn_ahmed_3960", "payment_method_source": "credit_card_7898168", "amount": 114.13}),
            Action(name="create_order", kwargs={
                "user_id": "evelyn_ahmed_3960",
                "items": [{"item_id": "7510236436", "quantity": 1}],
                "payment_method_sources": ["credit_card_7898168"],
                "tax_amount": 8.45
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_93",
        instruction=(
            "You're Daiki Kim user_id: daiki_kim_3197, an inventory manager. Update "
            "supplier #SUP0004's phone and email to '+1-800-555-0156' and "
            "'heythere@email.com', and add stock levels of 100 units for all available "
            "wireless earbuds."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Kim", "user_id": "daiki_kim_3197"}),
            Action(name="get_supplier_details", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0004",
                "contact_updates": {"phone": "+1-800-555-0156", "email": "heythere@email.com"}
            }),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["wireless earbuds"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["9924732112"],
                                                           "show_available": True,
                                                           "product_type": "wireless earbuds"}),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0004",
                "item_ids": ["9580569596", "1646531091", "8555936349", "6077640618", "4063058357", "6452271382", "2052249669"],
                "new_stock_level": 100,
                "stock_action": "add"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_94",
        instruction=(
            "You're a customer service rep helping Sofia Thomas (user_id: sofia_thomas_1518). "
            "Process her pending orders to processed and ship it out via Reliable Delivery Co."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Sofia", "last_name": "Thomas", "user_id": "sofia_thomas_1518"}),
            Action(name="get_user_order_history", kwargs={"user_id": "sofia_thomas_1518"}),
            Action(name="check_order_status", kwargs={"order_id": "#W7619352"}),
            Action(name="check_order_status", kwargs={"order_id": "#W3388163"}),
            Action(name="check_order_status", kwargs={"order_id": "#W2297866"}),
            Action(name="get_courier_by_name", kwargs={"courier_name": "Reliable Delivery Co."}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 1097.48, "order_id": "#W7619352", "courier_id": "#COU0009"}),
            Action(name="assign_courier", kwargs={"destination_country": "USA", "order_value": 1130.6, "order_id": "#W2297866", "courier_id": "#COU0009"}),
            Action(name="assign_tracking_number", kwargs={"order_ids":["#W7619352", "#W2297866"], "preferred_courier_id": "#COU0009"}),
            Action(name="update_order_status", kwargs={"order_ids": ["#W7619352", "#W2297866"], "new_status": "processed"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_95",
        instruction=(
            "You're Harper Kim (user_id: harper_kim_2998) from San Antonio. "
            "Check your gift card balance and buy a 500 pieces jigsaw puzzle if you have enough money."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "harper_kim_2998"}),
            Action(name="verify_gift_card_balance", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "harper_kim_2998"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "jigsaw puzzle",
                "options": {"pieces": "500"},
                "max_price": 51
            }),
            Action(name="get_product_info", kwargs={"item_id": "1096508426"}),
            Action(name="validate_order_items", kwargs={"item_list": [{"item_id": "1096508426", "quantity": 1}]}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "harper_kim_2998"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "harper_kim_2998",
                "item_list": [{"item_id": "1096508426", "quantity": 1}],
                "payment_methods_source": ["gift_card_5328393"]
            }),
            Action(name="process_payment", kwargs={"user_id": "harper_kim_2998", "payment_method_source": "gift_card_5328393", "amount": 49.82}),
            Action(name="create_order", kwargs={
                "user_id": "harper_kim_2998",
                "items": [{"item_id": "1096508426", "quantity": 1}],
                "payment_method_sources": ["gift_card_5328393"],
                "tax_amount": 3.69
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_96",
        instruction=(
            "You're James Martin (user_id: james_martin_1500) and want to check information for item #3254583681. "
            "Buy that item with your visa credit card. Validate and check it first before purchasing."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "james_martin_1500"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "james_martin_1500"}),
            Action(name="get_product_info", kwargs={"item_id": "3254583681"}),
             Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "3254583681", "quantity": 1}
                ],
            }),
            Action(name="generate_order_summary", kwargs={
                "user_id": "james_martin_1500",
                "item_list": [{"item_id": "3254583681", "quantity": 1}],
                "payment_methods_source": ["credit_card_7083997"]
            }),
            Action(name="process_payment", kwargs={"user_id": "james_martin_1500", "payment_method_source": "credit_card_7083997", "amount": 326.88}),
            Action(name="create_order", kwargs={
                "user_id": "james_martin_1500",
                "items": [{"item_id": "3254583681", "quantity": 1}],
                "payment_method_sources": ["credit_card_7083997"],
                "tax_amount": 24.21
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_97",
        instruction=(
            "You're Mia Anderson user_id: mia_anderson_7288. Update your email to "
            "'mia.updated@example.com' and address to 123 Park Avenue, Suite 112, "
            "Dallas, TX 75201, USA. Check if it reflects in your profile."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Mia", "last_name": "Anderson", "user_id": "mia_anderson_7288"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "mia_anderson_7288",
                "profile_updates": {
                    "email": "mia.updated@example.com",
                    "address": {
                        "address1": "123 Park Avenue",
                        "address2": "Suite 112",
                        "city": "Dallas",
                        "state": "TX",
                        "zip": "75201",
                        "country": "USA"
                    }
                }
            }),
            Action(name="validate_user_identity", kwargs={"first_name": "Mia", "last_name": "Anderson", "user_id": "mia_anderson_7288"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_98",
        instruction=(
            "You're a customer service rep. helping Evelyn Lopez user_id: "
            "evelyn_lopez_5487. Update all pending orders to processed status."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Evelyn", "last_name": "Lopez", "user_id": "evelyn_lopez_5487"}),
            Action(name="get_user_order_history", kwargs={"user_id": "evelyn_lopez_5487"}),
            Action(name="check_order_status", kwargs={"order_id": "#W1355800"}),
            Action(name="check_order_status", kwargs={"order_id": "#W1890669"}),
            Action(name="check_order_status", kwargs={"order_id": "#W3007862"}),
            Action(name="update_order_status", kwargs={"order_id": "#W1890669", "new_status": "processed"}),
            Action(name="update_order_status", kwargs={"order_id": "#W3007862", "new_status": "processed"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_99",
        instruction=(
            "You're Daiki Kim (user_id: daiki_kim_3197). "
            "Update supplier #SUP0004 phone to +1-800-555-NEW1 and email to daiki.kim@example.com, "
            "set item stock of 9580569596 to 100 units."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Kim", "user_id": "daiki_kim_3197"}),
            Action(name="update_supplier_info", kwargs={
                "supplier_id": "#SUP0004",
                "contact_updates": {"phone": "+1-800-555-NEW1", "email": "daiki.kim@example.com"}
            }),
            Action(name="update_inventory_stock", kwargs={
                "supplier_id": "#SUP0004",
                "item_id": "9580569596",
                "new_stock_level": 100,
                "stock_action": "set"
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_100",
        instruction=(
            "You're James Martin (user_id: james_martin_1500). "
            "Buy item #6704763132 with your mastercard."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "james_martin_1500"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "6704763132", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "james_martin_1500"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "james_martin_1500",
                "item_list": [
                    {"item_id": "6704763132", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_6932154"]
            }),
            Action(name="process_payment", kwargs={"user_id": "james_martin_1500", "payment_method_source": "credit_card_6932154", "amount": 329.89}),
            Action(name="allocate_inventory", kwargs={"item_id": "6704763132", "quantity": 1}),
            Action(name="create_order", kwargs={
                "user_id": "james_martin_1500",
                "items": [{"item_id": "6704763132", "quantity": 1}],
                "payment_method_sources": ["credit_card_6932154"],
                "tax_amount": 24.44
            }),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_101",
        instruction=(
            "You're a customer sales representative that is helping James Martin (user_id: james_martin_1500)"
            "Buy the cheapest mechanical keyboard using your visa and update the product to be unavailable after purchase."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "james_martin_1500"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "mechanical keyboard",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="get_product_info", kwargs={"item_id": "3616838507"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "3616838507", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "james_martin_1500"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "james_martin_1500",
                "item_list": [{"item_id": "3616838507", "quantity": 1}],
                "payment_methods_source": ["credit_card_7083997"]
            }),
            Action(name="process_payment", kwargs={"user_id": "james_martin_1500", "payment_method_source": "credit_card_7083997", "amount": 244.2}),
            Action(name="create_order", kwargs={
                "user_id": "james_martin_1500",
                "items": [{"item_id": "3616838507", "quantity": 1}],
                "payment_method_sources": ["credit_card_7083997"],
                "tax_amount": 18.09
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1656367028",
                "item_id": "3616838507",
                "available": False
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_102",
        instruction=(
            "You're Noah Patel (noah_patel_1311) a retail manager. "
            "You were informed that there is a price increase for the wireless earbuds of $5 "
            "for each of the available variants. Update all available item variants to reflect the new price."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Noah", "last_name": "Patel", "user_id": "noah_patel_1311"}),
            Action(name="filter_by_product_id_per_product_name", kwargs={"product_names": ["wireless earbuds"]}),
            Action(name="get_item_ids_by_product", kwargs={"product_ids": ["9924732112"],
                                                           "show_available": True,
                                                           "product_type": "wireless earbuds"}),
            Action(name="get_product_info", kwargs={"item_id": "9580569596"}),
            Action(name="get_product_info", kwargs={"item_id": "1646531091"}),
            Action(name="get_product_info", kwargs={"item_id": "8555936349"}),
            Action(name="get_product_info", kwargs={"item_id": "6077640618"}),
            Action(name="get_product_info", kwargs={"item_id": "4063058357"}),
            Action(name="get_product_info", kwargs={"item_id": "6452271382"}),
            Action(name="get_product_info", kwargs={"item_id": "2052249669"}),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "9580569596",
                "new_price": 262.38
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "1646531091",
                "new_price": 237.49
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "8555936349",
                "new_price": 231.49
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "6077640618",
                "new_price": 247.92
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "4063058357",
                "new_price": 248.34
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "6452271382",
                "new_price": 263.84
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "9924732112",
                "item_id": "2052249669",
                "new_price": 242.14
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_103",
        instruction=(
           "You're a customer service rep helping Aarav Nguyen (user_id: aarav_nguyen_7344). "
            "Cancel his pending order and restore product items in that order to available."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Aarav", "last_name": "Nguyen", "user_id": "aarav_nguyen_7344"}),
            Action(name="get_user_order_history", kwargs={"user_id": "aarav_nguyen_7344"}),
            Action(name="check_order_status", kwargs={"order_id": "#W7728728"}),
            Action(name="check_order_status", kwargs={"order_id": "#W2443586"}),
            Action(name="cancel_order", kwargs={
                "user_id": "aarav_nguyen_7344",
                "order_id": "#W2443586",
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "1656367028",
                "item_id": "9690244451",
                "available": True
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "7363354090",
                "item_id": "1437889264",
                "available": True
            }),
            Action(name="update_product_availability", kwargs={
                "product_id": "6679515468",
                "item_id": "3369928769",
                "available": True
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_104",
        instruction=(
           "You are a Customer Service Representative, that needs to update the billing profiles of four customers "
            "by adding their preferred payment methods: add a Visa card ending in 4821 to Noah Patel's "
            "(noah_patel_1311) account, a Mastercard ending in 7395 to Daiki Sanchez's (daiki_sanchez_2422) account, "
            "a PayPal account with the email sofia.payments@example.com to Sofia Hernandez's (sofia_hernandez_5364) account, "
            "and a Visa card ending in 1198 to Fatima Li's (fatima_li_8519) account. Also validate all changes."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Noah", "last_name": "Patel", "user_id": "noah_patel_1311"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Daiki", "last_name": "Sanchez", "user_id": "daiki_sanchez_2422"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Sofia", "last_name": "Hernandez", "user_id": "sofia_hernandez_5364"}),
            Action(name="validate_user_identity", kwargs={"first_name": "Fatima", "last_name": "Li", "user_id": "fatima_li_8519"}),
            Action(name="add_payment_method", kwargs={
                "user_id": "noah_patel_1311",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "4821",
                },
            }),

            Action(name="add_payment_method", kwargs={
                "user_id": "daiki_sanchez_2422",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "mastercard",
                    "last_four": "7395",
                },
            }),

            Action(name="add_payment_method", kwargs={
                "user_id": "sofia_hernandez_5364",
                "payment_type": "paypal",
                "payment_details": {
                    "email": "sofia.payments@example.com",
                },
            }),

            Action(name="add_payment_method", kwargs={
                "user_id": "fatima_li_8519",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1198",
                },
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "noah_patel_1311"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "daiki_sanchez_2422"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "sofia_hernandez_5364"}),
            Action(name="check_user_payment_methods", kwargs={"user_id": "fatima_li_8519"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_105",
        instruction=(
            "You're Aarav Ito (user_id: aarav_ito_1827). "
            "Update your address to 994 Hickory Lane, Apt 5B, Denver, CO 80224, USA, "
            "and purchase the cheapest water bottle using your gift card."
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Aarav", "last_name": "Ito", "user_id": "aarav_ito_1827"}),
            Action(name="update_user_profile", kwargs={
                "user_id": "aarav_ito_1827",
                "profile_updates": {
                    "address": {
                        "address1": "994 Hickory Lane",
                        "address2": "Apt 5B",
                        "city": "Denver",
                        "state": "CO",
                        "zip": "80224",
                        "country": "USA"
                    }
                }
            }),
            Action(name="verify_gift_card_balance", kwargs={"first_name": "Aarav", "last_name": "Ito", "user_id": "aarav_ito_1827"}),
            Action(name="search_products_by_filter", kwargs={
                "category": "water bottle",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="get_product_info", kwargs={"item_id": "5758737025"}),
            Action(name="validate_order_items", kwargs={
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1}
                ],
            }),
            Action(name="check_user_payment_methods", kwargs={"user_id": "aarav_ito_1827"}),
            Action(name="generate_order_summary", kwargs={
                "user_id": "aarav_ito_1827",
                "item_list": [{"item_id": "5758737025", "quantity": 1}],
                "payment_methods_source": ["gift_card_1468632"]
            }),
            Action(name="process_payment", kwargs={"user_id": "aarav_ito_1827", "payment_method_source": "gift_card_1468632", "amount": 48.7}),
            Action(name="create_order", kwargs={
                "user_id": "aarav_ito_1827",
                "items": [{"item_id": "5758737025", "quantity": 1}],
                "payment_method_sources": ["gift_card_1468632"],
                "tax_amount": 3.61
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_106",
        instruction=(
            "You're a customer service representative helping Aarav Nguyen (user_id: aarav_nguyen_7344)."
            "He wants to return items from his delivered order #W7728728 due to damage and wrong color. Process the return and update order status accordingly, "
        ),
        actions=[
            Action(name="validate_user_identity", kwargs={"first_name": "Aarav", "last_name": "Nguyen", "user_id": "aarav_nguyen_7344"}),
            Action(name="get_user_order_history", kwargs={"user_id": "aarav_nguyen_7344"}),
            Action(name="check_order_status", kwargs={"order_id": "#W7728728"}),
            Action(name="check_order_status", kwargs={"order_id": "#W2443586"}),
            Action(name="get_purchased_items", kwargs={"user_id": "aarav_nguyen_7344", "order_id": "#W7728728"}),
            Action(name="get_courier", kwargs={"tracking_id": "848032489512"}),
            Action(name="request_order_return", kwargs={
                "user_id": "aarav_nguyen_7344",
                "order_id": "#W7728728",
                "return_items": [
                    {"item_id": "8555936349", "quantity": 1},
                    {"item_id": "1437889264", "quantity": 1}
                ],
                "return_reason": "damage and wrong color"
            }),
            Action(name="update_order_status", kwargs={"order_id": "#W7728728", "new_status": "for return"}),
        ],
        outputs=[]
    ),

]
