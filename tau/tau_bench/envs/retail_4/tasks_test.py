from calendar import c
from tau_bench.types import Action, Task

TASKS = [

    Task(
        annotator="0",
        user_id="V5TSK_USR_1",
        instruction=
                     (
                     "You're Mason Anderson with user_id liam_wilson_6720, a "
                     "premium customer from Milwaukee wanting to place a new "
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
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lucas", "last_name": "Brown", "user_id": "liam_wilson_6720"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "laptop", "min_price": 2000, "max_price": 3000,
                                                             "options": {
                                                               "screen size": "17-inch",
                                                                "processor": "i7",
                                                                "ram": "32GB",
                                                                "storage": "1TB SSD",
                                                                "color": "black"
                                                            }}),
            Action(name="SearchProductsByFilter", kwargs={"category": "digital camera", "min_price": 2000, "max_price": 3000,
                                                             "options": {
                                                                "resolution": "30MP",
                                                                "storage": "SD card",
                                                                "zoom": "3x"
                                                            }}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1684786391", "quantity": 1},
                    {"item_id": "1804581713", "quantity": 1}
                ]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "liam_wilson_6720",
                "items": [
                    {"item_id": "1684786391", "quantity": 1},
                    {"item_id": "1804581713", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card"]
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_2",
        instruction=(
        "You are assisting customer Chen Moore (user_id: chen_moore_6080) in updating their account profile and adding a fresh payment method. The customer currently resides at 275 Cedar Avenue, Suite 148, San Diego, NV 91087, USA, but plans to relocate to a new address in San Diego at 456 Sunset Boulevard, Apt 12B, San Diego, NV 90028, USA. They wish to incorporate a gift card with a balance of $500, update their delivery address to this new Sunset Boulevard location, and ensure that their current order # W9205196 can be sent to the revised address: 456 Sunset Boulevard, Apt 12B, San Diego, NV 90028, USA."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "chen_moore_6080",
                "payment_type": "gift_card",
                "payment_details":{
                    "balance": 500.00
                }
            }),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "chen_moore_6080",
                "profile_updates": {
                    "address": {
                        "address1": "456 Sunset Boulevard",
                        "address2": "Apt 12B",
                        "city": "San Diego",
                        "state": "NV",
                        "zip": "90028",
                        "country": "USA"
                    }
                }
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "chen_moore_6080",
                "order_id": "#W9205196",
                "new_address": {
                    "address1": "456 Sunset Boulevard",
                    "address2": "Apt 12B",
                    "city": "San Diego",
                    "state": "NV",
                    "zip": "90028",
                    "country": "USA"
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_3",
        instruction=(
"As a customer service representative, you are tasked with managing a return request from Sofia Li (user_id: sofia_li_3261) regarding items from her completed order # W6874763. The client received a defective e-reader and an action camera in the wrong color. Verify her identity, review her order history, confirm the order's validity, process the return request, and change the order status to for return. Additionally, validate the shipping address and calculate the return shipping fee using the original courier."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Sofia", "last_name": "Li", "user_id": "sofia_li_3261"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="GetPurchasedItems", kwargs={"user_id": "sofia_li_3261", "order_id": "#W6874763"}),
            Action(name="GetCourier", kwargs={"tracking_id": "342513139974"}),
            Action(name="RequestOrderReturn", kwargs={
                "user_id": "sofia_li_3261",
                "order_id": "#W6874763",
                "return_items": [
                    {"item_id": "9494281769", "quantity": 1, "reason": "damaged"},
                    {"item_id": "6700049080", "quantity": 1, "reason": "wrong color"}
                ],
                "return_reason": "Damage and wrong color"
            }),

            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W6874763", "new_status": "for return"}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 718.81, "courier_id": "#COU0003"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_4",
        instruction=(
            "As Mia Martinez (user_id: mia_martinez_3271) residing at 615 Laurel Lane, Suite 552, Pittsburgh, OH 19036, USA, you intend to purchase a water bottle with your gift card and a coffee maker with your credit card for your home office, opting for the least expensive choice. Search for cost-effective options for both items, assure their availability, and generate separate orders for each product."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"}),
            Action(name="VerifyGiftCardBalance", kwargs={
                "first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"
            }),
            Action(name="SearchProductsByFilter", kwargs={"category": "water bottle", "max_price": 51, "price_flag": "cheapest"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "coffee maker", "price_flag": "cheapest"}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},  # Water bottle costs $45.09.
                    {"item_id": "1349017811", "quantity": 1}   # Coffee machine priced at $226.05
                ],
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "mia_martinez_3271"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mia_martinez_3271",
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},
                ],
                "payment_methods_source": ["gift_card"],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mia_martinez_3271",
                "item_list": [
                    {"item_id": "1349017811", "quantity": 1},
                ],
                "payment_methods_source": ["credit_card"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mia_martinez_3271",
                "items": [
                    {"item_id": "5758737025", "quantity": 1},
                ],
                "payment_method_sources": ["gift_card"],
                "tax_amount": 3.61
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mia_martinez_3271",
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
"Assume the identity of Lucas Rodriguez (user_id: lucas_rodriguez_6635) located at 477 Park Avenue, Suite 558, Houston, NM 75277, USA. As a regular customer with 4 past orders, review the status of all your orders (#W6893533, #W8770097, #W5183325, #W3913498). Especially focus on order #W6893533, #W8770097, #W5183325, #W3913498. Pay particular attention to order #W8770097 and change the delivery address to a temporary site at 500 Commerce Street, Suite 100, Houston, NM 75202, USA for this order."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ivan", "last_name": "Santos", "user_id": "lucas_rodriguez_6635"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "lucas_rodriguez_6635"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W6893533"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W8770097"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W5183325"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W3913498"}),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "lucas_rodriguez_6635",
                "order_id": "#W8770097",
                "new_address": {
                    "address1": "500 Commerce Street",
                    "address2": "Suite 100",
                    "city": "Houston",
                    "state": "NM",
                    "zip": "75202",
                    "country": "USA"
                }
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_6",
        instruction=(
            "Identify yourself as Juan Johnson (user_id: juan_johnson_5229) residing at 444 Highland Drive, Suite 419, Houston, NM 75218, USA. Plan to make a substantial purchase using only your paypal account. Search for the 3 most affordable water bottle choices within the $45 to $50 price range, ensure all products are validated, and organize delivery to your office in Houston."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_johnson_5229"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "juan_johnson_5229"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "water bottle", "min_price": 45, "max_price": 50, "price_flag": "cheapest", "limit": 3}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},  # $45.09
                    {"item_id": "8538875209", "quantity": 1},  # $45.13
                    {"item_id": "7661609223", "quantity": 1}   # $46.51
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "juan_johnson_5229"}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 3, "order_value": 136.73}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_johnson_5229",
                "item_list": [
                    {"item_id": "5758737025", "quantity": 1},
                    {"item_id": "8538875209", "quantity": 1},
                    {"item_id": "7661609223", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_9679338"],
                "shipping_cost": 16.49
            }),
            Action(name="AllocateInventory", kwargs={"item_id": "5758737025", "quantity": 1}),
            Action(name="AllocateInventory", kwargs={"item_id": "8538875209", "quantity": 1}),
            Action(name="AllocateInventory", kwargs={"item_id": "7661609223", "quantity": 1}),
            Action(name="CreateOrder", kwargs={
                "user_id": "juan_johnson_5229",
                "items": [
                    {"item_id": "5758737025", "quantity": 1},
                    {"item_id": "8538875209", "quantity": 1},
                    {"item_id": "7661609223", "quantity": 1}
                ],
                "payment_method_sources": ["paypal_9679338"],
                "tax_amount": 10.94,
                "shipping_cost": 16.49
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 164.16, "courier_id": "#COU0001"}),
            Action(name="ProcessPayment", kwargs={
                "user_id": "juan_johnson_5229",
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
            "You are Isabella Johnson (user_id: isabella_johnson_5265) located at 273 Highland Drive, Suite 953, Phoenix, AZ 80216, USA. You are preparing for an upcoming hiking excursion and wish to acquire high-quality gear. Focus is on premium backpacks in the $200-220 price bracket, aiming to buy the top 3 costliest to evaluate their features. Your financial plan accommodates several purchases, and you favor using your credit card for these outdoor gear acquisitions."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Olivia", "last_name": "Smith", "user_id": "isabella_johnson_5265"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "isabella_johnson_5265"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "backpack", "min_price": 200, "max_price": 220, "price_flag": "expensive", "limit": 3}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "8084436579", "quantity": 1},  # $219.43 - Navy color, Large size, Made of Polyester, Features a laptop compartment
                    {"item_id": "6309044598", "quantity": 1},  # $218.59 - Blue, Medium size, Leather material, with Laptop pocket
                    {"item_id": "5917587651", "quantity": 1}   # $212.79 - Gray, Medium size, Polyester material, Includes laptop pocket
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "isabella_johnson_5265"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "isabella_johnson_5265",
                "item_list": [
                    {"item_id": "8084436579", "quantity": 1},
                    {"item_id": "6309044598", "quantity": 1},
                    {"item_id": "5917587651", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_7971769"],
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 3, "order_value": 702.87}),
            Action(name="CreateOrder", kwargs={
                "user_id": "isabella_johnson_5265",
                "items": [
                    {"item_id": "8084436579", "quantity": 1},
                    {"item_id": "6309044598", "quantity": 1},
                    {"item_id": "5917587651", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_7971769"],
                "tax_amount": 52.06,     # 8% sales tax applied to $650.81.
                "shipping_cost": 16.49
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "isabella_johnson_5265",
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
"You are Ethan Khan (user_id: noah_khan_3904) residing at 264 Elm Street, Suite 579, San Diego, NV 92117, USA. Order # You created order W4347784, but it needs to be canceled due to changed conditions. Please check the order status, initiate the cancellation, process a refund to your Visa card, and then place a new order for a single budget-friendly water bottle."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ethan", "last_name": "Khan", "user_id": "noah_khan_3904"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "noah_khan_3904"}),
            Action(name="CancelOrder", kwargs={"user_id": "noah_khan_3904", "order_id": "#W4347784", "cancellation_reason": "change in circumstances"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4347784", "new_status": "cancelled"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "water bottle", "price_flag": "cheapest", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [{"item_id": "5758737025", "quantity": 1}]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "noah_khan_3904"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "noah_khan_3904",
                "item_list": [{"item_id": "5758737025", "quantity": 1}],
                "payment_methods_source": ["credit_card"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "noah_khan_3904",
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
            "You are Chen Williams (user_id: chen_williams_4204) residing at 503 Elm Avenue, Suite 641, Houston, NM 77004, USA. You are establishing a home office and aim to acquire a comprehensive and high-end tech bundle: 1 mechanical keyboard, 1 wireless earbuds, and 1 bluetooth speaker. You possess both PayPal (paypal_3742148) and a gift card with a $79 balance (gift_card_3406421) and wish to utilize the gift card first, followed by PayPal for the remaining sum. You must locate available options priced around $230-300 each and allocate payments accordingly."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Johnson", "user_id": "chen_williams_4204"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "chen_williams_4204"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "mechanical keyboard", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="SearchProductsByFilter", kwargs={"category": "wireless earbuds", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="SearchProductsByFilter", kwargs={"category": "bluetooth speaker", "min_price": 230, "max_price": 300, "price_flag": "expensive", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6452271382", "quantity": 1},
                    {"item_id": "9440686670", "quantity": 1}
                ]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "chen_williams_4204",
                "item_list": [{"item_id": "1151293680", "quantity": 1},
                              {"item_id": "6452271382", "quantity": 1},
                               {"item_id": "9440686670", "quantity": 1}],
                "payment_methods_source": ["gift_card", "paypal"],
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "chen_williams_4204",
                "payment_method_source": "gift_card",
                "amount": 79
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "chen_williams_4204",
                "payment_method_source": "paypal",
                "amount": 817.49
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "chen_williams_4204",
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
            "You are Omar Rodriguez (user_id: omar_rodriguez_4830) located at 621 Spruce Street, Suite 698, Fort Worth, NM 76180, USA. You desire to initiate a wellness routine and require an electric toothbrush and yoga mat. Your budget is adaptable, and you have both a Mastercard (credit_card_8992222) and a gift card with a $75 balance (gift_card_3895897). You prefer an electric rechargeable white toothbrush, a blue yoga mat, and wish to use your gift card first, then the credit card for any leftover balance. All items should be shipped to your Fort Worth address."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Omar", "last_name": "Santos", "user_id": "omar_rodriguez_4830"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "omar_rodriguez_4830"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "electric toothbrush", "options": {"battery type": ["rechargeable"], "color": ["white"]}}),
            Action(name="SearchProductsByFilter", kwargs={"category": "yoga mat", "options": {"color": ["blue"]}}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "6164262152", "quantity": 1},  # Rechargeable electric toothbrush priced at $192.15.
                    {"item_id": "5586947715", "quantity": 1}   # 4mm PVC yoga mat priced at $92.53
                ]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "omar_rodriguez_4830",
                "item_list": [
                    {"item_id": "6164262152", "quantity": 1},
                    {"item_id": "5586947715", "quantity": 1}
                ],
                "payment_methods_source": ["gift_card", "credit_card"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "omar_rodriguez_4830",
                "items": [{"item_id": "6164262152", "quantity": 1}, {"item_id": "5586947715", "quantity": 1}],
                "payment_method_sources": ["gift_card", "credit_card"],
                "tax_amount": 24.29,
                "shipping_cost": 0.00
            }),
            Action(name="AllocateInventory", kwargs={"item_id": "6164262152", "quantity": 1}),
            Action(name="AllocateInventory", kwargs={"item_id": "5586947715", "quantity": 1}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "omar_rodriguez_4830"}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 327.93})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_11",
        instruction=(
            "You are Ahmad Hernandez (user_id: ahmad_hernandez_5411) tasked with reviewing your recent order history. Your objective is to verify that you have sufficient wireless audio equipment that aligns with your quality criteria: specifically, earbuds with a strong battery life (6 hours) and a minimum water protection rating of IPX4 to suit your active lifestyle. Evaluate your existing order status and make the necessary purchases."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={
                "first_name": "Yusuf",
                "last_name": "Hernandez",
                "user_id": "ahmad_hernandez_5411"
            }),
            Action(name="GetUserOrderHistory", kwargs={
                "user_id": "ahmad_hernandez_5411"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W9978601"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W4817567"
            }),
            Action(name="SearchProductsByFilter", kwargs={"category": "wireless earbuds", "options": {"battery life": ["6 hours"], "water resistance": ["IPX4"]}}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1646531091", "quantity": 1}
                ]
            }),
            Action(name="CheckUserPaymentMethods", kwargs={
                "user_id": "ahmad_hernandez_5411"
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "ahmad_hernandez_5411",
                "item_list": [{"item_id": "1646531091", "quantity": 1}],
                "payment_methods_source": ["paypal_6753664"]
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "ahmad_hernandez_5411",
                "payment_method_source": "paypal_6753664",
                "amount": 251.09
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "ahmad_hernandez_5411",
                "items": [{"item_id": "1646531091", "quantity": 1}],
                "payment_method_sources": ["paypal_6753664"],
                "tax_amount": 18.6,
                "shipping_cost": 0.00
            }),
            Action(name="AllocateInventory", kwargs={
                "item_id": "1646531091",
                "quantity": 1
            }),
            Action(name="ValidateShippingAddress", kwargs={
                "user_id": "ahmad_hernandez_5411"
            }),
            Action(name="AssignCourier", kwargs={
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
            "You are Daiki Costa (user_id: daiki_costa_2903) located at 713 Park Avenue, Suite 800, San Francisco, NV 94102, USA. You wish to purchase a birthday gift for a friend, targeting a price range of $150-200, ideally an electric toothbrush. Since your friend's favorite color is black, you aim to find a black electric toothbrush. With a gift card balance of $19 (gift_card_2652153), introduce a new payment method using your visa ending in 1234. Investigate your options, verify available choices within your budget, and determine the shipping costs. Once clarified, proceed to create an order."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_costa_2903"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "daiki_costa_2903"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "electric toothbrush", "min_price": 150, "max_price": 200, "options": {"color": ["black"]}}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [{"item_id": "8098621301", "quantity": 1}]  # Electric toothbrush priced at $183.11.
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "daiki_costa_2903",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1234",
                },
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "daiki_costa_2903",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["gift_card", "credit_card"],
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "daiki_costa_2903"}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 207.52}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 207.52}),
            Action(name="AllocateInventory", kwargs={"item_id": "8098621301", "quantity": 1}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "daiki_costa_2903",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["gift_card", "credit_card"],
                "shipping_cost": 11.49,  # cost of shipping for a single item
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "daiki_costa_2903",
                "payment_method_source": "gift_card",
                "amount": 19.00
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "daiki_costa_2903",
                "payment_method_source": "credit_card",
                "amount":  200.01
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "daiki_costa_2903",
                "items": [{"item_id": "8098621301", "quantity": 1}],
                "payment_method_sources": ["gift_card", "credit_card"],
                "tax_amount": 15.37,
                "shipping_cost": 11.49  # delivery expenses
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_13",
        instruction=(
"As a customer service representative, you're addressing an escalated case for VIP customer Mei Anderson (user_id: mei_anderson_1792) located at 319 Laurel Lane, Suite 319, Raleigh, NC 28260, USA. The customer has a complaint regarding their order # W4498118 is still pending and requires urgent processing for a crucial business presentation. Verify their identity and the ordered items, review their order history and current status. If any items are out of stock, update the order status to reflect a return."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mei", "last_name": "Wilson", "user_id": "mei_anderson_1792"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "mei_anderson_1792"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W4498118"}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5745575001", "quantity": 1},
                    {"item_id": "7736359414", "quantity": 1},
                    {"item_id": "5312063289", "quantity": 1},
                    {"item_id": "5565631513", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ]
            }),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4498118", "new_status": "for return"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_14",
        instruction=(
            "You are William Simpson (user_id: william_simpson_2792), a new customer residing at 570 Main Street, Suite 708, Milwaukee, IN 60627, USA. You aim to place your inaugural order by purchasing a starter tech package: the most affordable electric toothbrush and yoga mat to commence your wellness journey. Using your new Mastercard (credit_card_2645445), you want to experience the entire procedure from account validation to order placement. Confirm the functionality of your payment method, verify your Milwaukee address for shipping purposes, and finalize your initial order successfully."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Nguyen", "user_id": "william_simpson_2792"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "william_simpson_2792"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "electric toothbrush", "price_flag": "cheapest", "limit": 1}),
            Action(name="SearchProductsByFilter", kwargs={"category": "yoga mat", "price_flag": "cheapest", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2645006275", "quantity": 1},  # Electric toothbrush priced at $183.11
                    {"item_id": "5586947715", "quantity": 1}   # Cost of yoga mat: $92.53
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "william_simpson_2792"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "william_simpson_2792",
                "item_list": [
                    {"item_id": "2645006275", "quantity": 1},
                    {"item_id": "5586947715", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_2645445"],
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "william_simpson_2792",
                "payment_method_source": "credit_card_2645445",
                "amount": 297.69
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "william_simpson_2792",
                "items": [{"item_id": "2645006275", "quantity": 1}, {"item_id": "5586947715", "quantity": 1}],
                "payment_method_sources": ["credit_card_2645445"],
                "tax_amount": 22.05,
                "shipping_cost": 0.00  # delivery expense
            }),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_15",
        instruction=(
            "You are Mia Martinez (user_id: mia_martinez_3271). Modify your email to 'mia.martinez2061@example.com' and your address to 248 Pinecrest Drive, Apt 9C, Houston, NM 73301, USA. Check if the changes are reflected and review your gift card balance."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "mia_martinez_3271",
                "profile_updates": {"email": "mia.martinez2061@example.com",
                                    "address": {
                                        "address1": "248 Pinecrest Drive",
                                        "address2": "Apt 9C",
                                        "city": "Houston",
                                        "state": "NM",
                                        "zip": "73301",
                                        "country": "USA"
                                    }}
            }),
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"}),
            Action(name="VerifyGiftCardBalance", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_17",
        instruction=(
"You are Olivia Johnson (user_id: olivia_johnson_8564), responsible for managing supplies. Adjust the stock levels of 2235648106 to 200 units. Update the supplier # SUP0003 contact number and email: +1-800-555-NEW1 phonesupplier@example.com."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Smith", "user_id": "olivia_johnson_8564"}),
            Action(name="UpdateInventoryStock", kwargs={
                "supplier_id": "#SUP0003",
                "item_id": "2235648106",
                "new_stock_level": 200,
                "stock_action": "set"
            }),
            Action(name="UpdateSupplierInfo", kwargs={
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
            "You are Emma Simpson (user_id: emma_simpson_6399) residing at 412 Lakeview Drive, Suite 698, San Antonio, NM 78229, USA. Your aim is to purchase a birthday gift for your friend, focusing on the most economical bluetooth speakers ranging from $100 to $300. Utilize PayPal (paypal_3722088) for payment purposes, ensuring you identify the item with the greatest value within budget, confirm it’s available, and proceed to place the order."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mia", "last_name": "Nguyen", "user_id": "emma_simpson_6399"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "emma_simpson_6399"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "bluetooth speaker", "min_price": 100, "max_price": 300, "available_only": True, "price_flag": "cheapest", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2635605237", "quantity": 1}
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "emma_simpson_6399"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "emma_simpson_6399",
                "item_list": [
                   {"item_id": "2635605237", "quantity": 1}
                ],
                "payment_methods_source": ["paypal"],
            }),
                Action(name="CreateOrder", kwargs={
                "user_id": "emma_simpson_6399",
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
            "Assist customer Ahmad Russo user_id: ahmad_russo_9620. Change the status of all his pending orders to processed."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yusuf", "last_name": "Rossi", "user_id": "ahmad_russo_9620"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "ahmad_russo_9620"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W6247578", "new_status": "processed"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4776164", "new_status": "processed"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_20",
        instruction=(
            "You are Noah Johnson (user_id: noah_johnson_7905) residing at 218 Main Street, Suite 792, Tucson, AZ 85001, USA. You have a passion for technology and are seeking to enhance your entire workspace setup: choose a mechanical keyboard with RGB lighting, wireless earbuds that offer 8 hours of battery life, and a red Bluetooth speaker that is water-resistant. Opt for the highest-priced options without concern for cost, utilize your Visa card (credit_card_3185406), and proceed to order everything. Additionally, ensure you verify the specifications of each item before making the purchase."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ethan", "last_name": "Smith", "user_id": "noah_johnson_7905"}),

            Action(name="GetUserOrderHistory", kwargs={"user_id": "noah_johnson_7905"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "mechanical keyboard",
                "options": {"backlight": "RGB"},
                "price_flag": "expensive"
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "wireless earbuds",
                "options": {"battery life": ["8 hours"]},
                "price_flag": "expensive",
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "bluetooth speaker",
                "options": {"water resistance": "yes", "color": "red"},
                "price_flag": "expensive",
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6077640618", "quantity": 1},
                    {"item_id": "7751905257", "quantity": 1}
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "noah_johnson_7905"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "noah_johnson_7905"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "noah_johnson_7905",
                "item_list": [
                    {"item_id": "1151293680", "quantity": 1},
                    {"item_id": "6077640618", "quantity": 1},
                    {"item_id": "7751905257", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3185406"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "noah_johnson_7905",
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
            "As a customer service representative, you're responsible for handling an urgent inventory crisis involving Chen Moore (user_id: chen_moore_6080). Chen is in need of a laptop equipped with 32GB RAM, a 256GB SSD, and an Intel i7 processor, but the model is currently listed as unavailable. To address this, confirm Chen's identity and analyze their past purchases, identify the laptop within the $2400–2700 range, modify the system to make it available at $2450.00, check all order details, and finalize the purchase using Chen’s credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "laptop", "min_price": 2400, "max_price": 2700, "available_only": False,
                                                             "options": {"ram": ["32GB"], "storage": ["256GB SSD"], "processor": ["i7"]}}),
            Action(name="UpdateProductAvailability", kwargs={"product_id": "4760268021", "item_id": "8997785118", "available": True, "new_price": 2450.00}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "8997785118", "quantity": 1}
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "chen_moore_6080",
                "item_list": [{"item_id": "8997785118", "quantity": 1}],
                "payment_methods_source": ["credit_card_4041739"],
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "chen_moore_6080",
                "payment_method_source": "credit_card_4041739",
                "amount": 2646.0
            }),
            Action(name="CreateOrder", kwargs={
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
            "You are Juan White (user_id: juan_white_5671) transitioning from Jacksonville to Portland, now residing at 1200 Pine Street, Apt 15B, Portland, Washington (98101). Make sure your profile includes your new address and your email updated to juan.anderson.Portland@example.com. Coordinate payment using a newly issued $750 gift card, and look for economical home office furniture (desk lamp, office chair) priced between $100–$500. Aim to select items that offer the right balance of cost and suitability, verify their availability, and arrange for Reliable Delivery Co. to transport them to your new home in Portland."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Anderson", "user_id": "juan_white_5671"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "juan_white_5671"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "juan_white_5671",
                "profile_updates": {
                    "email": "juan.anderson.seattle@example.com",
                    "address": {
                        "address1": "1200 Pine Street",
                        "address2": "Apt 15B",
                        "city": "Portland",
                        "state": "OR",
                        "zip": "98101",
                        "country": "USA"
                    }
                }
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "juan_white_5671",
                "payment_type": "gift_card",
                "payment_details": {
                    "balance": 750
                }
            }),
            Action(name="SearchProductsByFilter", kwargs={"category": "desk lamp", "min_price": 100, "max_price": 500, "price_flag": "cheapest", "limit": 1}),
            Action(name="SearchProductsByFilter", kwargs={"category": "office chair", "min_price": 100, "max_price":500, "price_flag": "cheapest", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5320792178", "quantity": 1},  # table lamp
                    {"item_id": "4168944673", "quantity": 1}   # seat
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "juan_white_5671"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_white_5671",
                "item_list": [{"item_id": "5320792178", "quantity": 1}, {"item_id": "4168944673", "quantity": 1}],
                "payment_methods_source": ["gift_card_25671"],
            }),
            Action(name="GetCourierByName", kwargs={"courier_name": "Reliable Delivery Co."}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 655.62, "courier_id": "#COU0009"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_white_5671",
                "item_list": [{"item_id": "5320792178", "quantity": 1}, {"item_id": "4168944673", "quantity": 1}],
                "payment_methods_source": ["gift_card_25671"],
                "shipping_cost": 13.99  # shipping fee for two products
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "juan_white_5671",
                "payment_method_source": "gift_card_25671",
                "amount": 669.61
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "juan_white_5671",
                "items": [
                    {"item_id": "5320792178", "quantity": 1},
                    {"item_id": "4168944673", "quantity": 1},
                ],
                "payment_method_sources": ["gift_card_25671"],
                "tax_amount": 48.56,
                "shipping_cost": 13.99
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA","order_value": 669.61,  "courier_id": "#COU0009"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_23",
        instruction=(
            "You are Lei Andersson (user_id: lei_andersson_7574), relocating from Phoenix to your new residence at 245 Mountain View Drive, Apt 8C, Boulder, AZ 80302, USA. Make sure to change your email to lei.johansson.boulder@example.com, update your address, and add a new Visa credit card (ending in 7890)."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lei", "last_name": "Johansson", "user_id": "lei_andersson_7574"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "lei_andersson_7574",
                "profile_updates": {
                    "email": "lei.johansson.boulder@example.com",
                    "address": {
                        "address1": "245 Mountain View Drive",
                        "address2": "Apt 8C",
                        "city": "Boulder",
                        "state": "AZ",
                        "zip": "80302",
                        "country": "USA"
                    }
                }
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "lei_andersson_7574",
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
            "You are Aarav Walker (user_id: aarav_walker_4756) residing at 178 Lakeview Drive, Suite 576, Fort Worth, NM 76150, USA. Utilize your gift card to acquire a blue cotton T-shirt in medium size."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Aarav", "last_name": "Davis", "user_id": "aarav_walker_4756"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "aarav_walker_4756"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "aarav_walker_4756"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "t-shirt", "options": {"color": ["blue"], "material": ["cotton"], "size": ["M"]}}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "9612497925", "quantity": 1},  # Tee shirt
                ]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "aarav_walker_4756",
                "item_list": [{"item_id": "9612497925", "quantity": 1}],
                "payment_methods_source": ["gift_card_9708163"],
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "aarav_walker_4756",
                "payment_method_source": "gift_card_9708163",
                "amount": 54.95
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "aarav_walker_4756",
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
            "As a customer service representative, assist Chen Wilson (user_id: chen_wilson_8075) from 945 Hickory Lane, Suite 262, Oakland, NV 95190, USA. The customer requests to alter the delivery address for all orders to their office located at 500 Technology Drive, Building A, Oakland, NV 95110, USA."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Brown", "user_id": "chen_wilson_8075"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "chen_wilson_8075"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W4296426"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W3381155"}),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "chen_wilson_8075",
                "order_id": "#W4296426",
                "new_address": {
                    "address1": "500 Technology Drive",
                    "address2": "Building A",
                    "city": "Oakland",
                    "state": "NV",
                    "zip": "95110",
                    "country": "USA"
                }
            }),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "chen_wilson_8075",
                "order_id": "#W3381155",
                "new_address": {
                    "address1": "500 Technology Drive",
                    "address2": "Building A",
                    "city": "Oakland",
                    "state": "NV",
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
            "As a customer service representative, assist Mei Clark (user_id: mei_clark_6103) in changing her email to mei.martin.updated@example.com. The product she's interested in is a gold colored smartphone with 128GB storage and 6GB ram, which is currently unavailable. Mark the product as available, modify the price to $1499.99, and facilitate her purchase using her Visa card (credit_card_8398849)."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mei", "last_name": "Martin", "user_id": "mei_clark_6103"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "mei_clark_6103",
                "profile_updates": {
                    "email": "mei.martin.updated@example.com"
                }
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "smartphone",
                "available_only": False,
                "options": {"color": ["gold"], "storage": ["128GB"], "RAM": ["6GB"]},
            }),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "1801728040",
                "item_id": "1631373418",
                "available": True,
                "new_price": 1499.99
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [{"item_id": "1631373418", "quantity": 1}]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mei_clark_6103",
                "item_list": [{"item_id": "1631373418", "quantity": 1}],
                "payment_methods_source": ["credit_card_8398849"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mei_clark_6103",
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
            "Handling the tasks for Juan Thompson (user_id: juan_lopez_8249) from 281 Main Street, Suite 979, Washington, DC 20156, USA, he needs to cancel his current order because of a change in plans and subsequently place a new order for a gaming mouse. Utilize his PayPal account to purchase the least expensive available option."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Sanchez", "user_id": "juan_lopez_8249"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "juan_lopez_8249"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W6483628"}),
            Action(name="CancelOrder", kwargs={
                "user_id": "juan_lopez_8249",
                "order_id": "#W6483628",
                "cancellation_reason": "change of plans"
            }),
            Action(name="SearchProductsByFilter", kwargs={"category": "gaming mouse", "price_flag": "cheapest", "limit": 1}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                ]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_lopez_8249",
                "item_list": [{"item_id": "2880340443", "quantity": 1}],
                "payment_methods_source": ["paypal"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "juan_lopez_8249",
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
            "Identify yourself as Mason Anderson (user_id: liam_wilson_6720), who is an inventory manager for the retail company. It is necessary for you to assess the supply chain status concerning laptop products (product_id: 4760268021). Verify the product’s status and confirm the supplier’s capacity for it. Upon confirmation, generate a new supply order for the same product with a quantity of 150 units from the identical supplier. After establishing the supply order, adjust the status of the previous supply order to pending and mark the product as unavailable in the system."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lucas", "last_name": "Brown", "user_id": "liam_wilson_6720"}),
            Action(name="CheckSupplyOrderStatus", kwargs={"product_id": "4760268021"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0002",
                "product_id": "4760268021",
                "item_id": "3265035808",
                "quantity": 150,
                "unit_cost": 1140.45
            }),
            Action(name="UpdateSupplyOrderStatus", kwargs={
                "supply_order_id": "#SO5813",
                "new_status": "pending"
            }),
            Action(name="UpdateProductAvailability", kwargs={
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
"Identify yourself as Mei Anderson (user_id: mei_anderson_1792), who is a store manager for the retail company. Supplier #SUP0007, your usual source, is encountering challenges with grill orders. Review supplier #SUP0007's inventory for items with the highest stock to see if they can fulfill an order of at least 20 units. After your assessment, place a new supply order and update the inventory by reducing it by 20 units."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mei", "last_name": "Wilson", "user_id": "mei_anderson_1792"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["grill"]}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "supplier_id": "#SUP0007",
                "product_id": "6819683148",
                "min_stock_level": 20,
                "product_type": ["grill"],
                "stock_level_preference": "highest"
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "9724317332"}),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0007",
                "product_id": "6819683148",
                "item_id": "9724317332",
                "quantity": 20,
                "unit_cost": 1042.19
            }),
            Action(name="UpdateInventoryStock", kwargs={
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
"You are Omar Rodriguez (user_id: omar_rodriguez_4830), serving as a supply chain manager for the retail company. Handle the task of updating the pricing terms for an existing supply order # SO6035 requires updates due to cost changes. Examine the supply order specifics, adjust the terms to COD with the new price of $30.0, and increase inventory by 45 units as needed."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Omar", "last_name": "Santos", "user_id": "omar_rodriguez_4830"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="UpdateSupplyOrderTerms", kwargs={
                "supply_order_id": "#SO6035",
                "new_unit_cost": 30.0,
                "payment_terms": "COD"
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "7579176349"}),
            Action(name="UpdateInventoryStock", kwargs={
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
            "You are Daiki Costa (user_id: daiki_costa_2903), acting as a supply coordinator for the retail company. Coordinate the review of supplier inventory levels for smartphones, ensuring that each variant is present and maintained at a minimum level of 50 units. Confirm supplier capacity and adjust supplier ratings based on recent performance."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_costa_2903"}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "min_stock_level": 50,
                "product_type": ["smartphone"],
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "5490694069"}),
            Action(name="GetProductInfo", kwargs={"item_id": "9929635042"}),
            Action(name="GetProductInfo", kwargs={"item_id": "5758570643"}),
            Action(name="GetProductInfo", kwargs={"item_id": "5311660992"}),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "1801728040",
                "item_id": "5490694069",
                "available": True
            }),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "1801728040",
                "item_id": "9929635042",
                "available": True
            }),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "1801728040",
                "item_id": "5758570643",
                "available": True
            }),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "1801728040",
                "item_id": "5311660992",
                "available": True
            }),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="UpdateSupplierInfo", kwargs={
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
            "As Daiki Costa (user_id: daiki_costa_2903) residing at 713 Park Avenue, Suite 800, San Francisco, NV 94102, USA, investigate supplier inventory levels specifically for headphones, as there is a large order to be made. Upon gathering the necessary details, organize a supply order for 30 units of each variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Silva", "user_id": "daiki_costa_2903"}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "product_type": ["headphones"],
                "available_only": True,
            }),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="GetProductInfo", kwargs={"item_id": "3374679624"}),
            Action(name="GetProductInfo", kwargs={"item_id": "3104857380"}),
            Action(name="GetProductInfo", kwargs={"item_id": "7493556126"}),
            Action(name="GetProductInfo", kwargs={"item_id": "9805150490"}),
            Action(name="CreateSupplyOrder", kwargs={
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
"Being William Lee (user_id: william_lee_5010), a supply chain expert managing supplier # SUP0011, confirm the correctness of the supplier's data and update performance ratings according to the latest assessments. Also, ensure that the stock of electric toothbrushes is maintained at an optimal level of 200 units."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Lee", "user_id": "william_lee_5010"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0011",
                "contact_updates": {
                    "phone": "+1-800-555-0089"
                },
                "performance_rating": 1.0
            }),
            Action(name="GetProductItemsPerSupplier", kwargs={"supplier_id": "#SUP0011", "stock_available": True, "product_type": "electric toothbrush"}),
            Action(name="UpdateInventoryStock", kwargs={
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
            "You are Noah Anderson (user_id: noah_anderson_5687) from 312 Chestnut Street, Suite 578, San Diego, NV 92152, USA. Your task is to procure your first laptop for college. Search for the most affordable laptops with 1TB storage, confirm your identity, review available payment options, verify the order contents, and finalize your purchase using your gift card while adding a new payment method via your visa credit card (**** **** **** 1234) for any remaining balance. Ensure the laptop is in stock."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ethan", "last_name": "Wilson", "user_id": "noah_anderson_5687"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "noah_anderson_5687"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "laptop",
                "options": {"storage": "1TB SSD"},
                "price_flag": "cheapest",
                "available_only": True,
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "noah_anderson_5687"}),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "noah_anderson_5687",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1234",
                },
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "noah_anderson_5687",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                ],
                "payment_methods_source": ["gift_card_6470461", "credit_card_25687"],
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "noah_anderson_5687",
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
            "As a customer service representative, assist Mei Moore (user_id: mei_moore_8248) with a payment problem. Her credit card failed for a tablet purchase in the $1050+ price range, and she prefers to use PayPal instead. Aim to help Mei successfully acquire the tablet she requires while confirming her account settings are correct and the order process adheres to all standard verification protocols."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={
                "first_name": "Mei",
                "last_name": "Moore",
                "user_id": "mei_moore_8248"
            }),
            Action(name="GetUserOrderHistory", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="CheckUserPaymentMethods", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "mei_moore_8248",
                "payment_type": "paypal",
                "payment_details": {}
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "tablet",
                "min_price": 1050,
                "available_only": True
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2235648106", "quantity": 1}
                ]
            }),
            Action(name="ValidateShippingAddress", kwargs={
                "user_id": "mei_moore_8248"
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mei_moore_8248",
                "item_list": [
                    {"item_id": "2235648106", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_28248"]
            }),
            Action(name="CreateOrder", kwargs={
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
"Your role is Ahmad Harris (ahmad_harris_7149), a procurement specialist in charge of managing supplier relationships. Supplier # SUP0003 has revised their contact details, requiring a system update. Examine their current information, update the contact info (email newsupport@premiumparts.com, phone +1-800-555-0134), and change the performance rating to 4.2. Also, add notes indicating the supplier is reliable. You must also verify their capacity, investigate the products they offer, check inventory levels, and evaluate their supply orders."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yusuf", "last_name": "Taylor", "user_id": "ahmad_harris_7149"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0003",
                "contact_updates": {
                    "email": "newsupport@premiumparts.com",
                    "phone": "+1-800-555-0134"
                },
                "performance_rating": 4.2,
                "notes": "reliable supplier"
            }),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="GetProductItemsPerSupplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="CheckSupplyOrderStatus", kwargs={"product_id": "8024098596"}),
            Action(name="CheckSupplyOrderStatus", kwargs={"product_id": "7471004230"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO7422"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5993"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_38",
        instruction=(
            "Assume the identity of Mason Campbell (user_id: mason_campbell_4265) from 647 Laurel Lane, Suite 627, Houston, NM 78747, USA. Your objective is to purchase a complete home office setup: a laptop, headphones, and a smartphone. All items should be in stock and low-cost. Confirm the availability of all items, review your payment methods, generate an order summary, and finalize the purchase with your credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Liam", "last_name": "Gonzalez", "user_id": "mason_campbell_4265"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "mason_campbell_4265"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "laptop",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "headphones",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "smartphone",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "mason_campbell_4265"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mason_campbell_4265",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1},
                    {"item_id": "5339029584", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_6341155"]
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "mason_campbell_4265",
                "payment_method_source": "credit_card_6341155",
                "amount": 4067.18
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mason_campbell_4265",
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
            "As a customer service representative managing an intricate case for Mei Campbell (user_id: mei_campbell_4785), you will address the situation where the customer received a damaged backpack. She wishes to return it and receive a replacement that falls within the same price bracket. You must carry out the return process, locate and confirm the least expensive replacement, update the order status, and make sure the customer is pleased. Utilize her PayPal to procure the order."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "user_id": "mei_campbell_4785"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "mei_campbell_4785", "product_type": ["backpack"]}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W7303089"}),
            Action(name="RequestOrderReturn", kwargs={
                "user_id": "mei_campbell_4785",
                "order_id": "#W7303089",
                "item_id": "2492465580",
                "return_reason": "Damaged backpack"
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "backpack",
                "max_price": 201.95,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "9851293632", "quantity": 1},
                ],
            }),
            Action(name="UpdateOrderStatus", kwargs={
                "order_id": "#W7303089",
                "new_status": "for return"
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="CreateOrder", kwargs={
                "user_id": "mei_campbell_4785",
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
            "As Noah Jackson user_id: noah_jackson_6291, functioning as an inventory manager, you are tasked with organizing an emergency restock of smartwatches in response to intense customer demand. Verify the current stock levels with suppliers, selecting only those who can provide a minimum of 100 units. Configure the inventory so that all available smartwatch models total precisely 250 units each, ensuring items not in stock are excluded, and adjust the supplier performance rating to 4.5."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ethan", "last_name": "Lopez", "user_id": "noah_jackson_6291"}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "min_stock_level": 100,
                "product_type": ["smart watch"],
            }),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0002",
                "performance_rating": 4.5
            }),
            Action(name="GetProductItemsPerSupplier", kwargs={"supplier_id": "#SUP0002", "product_type": "smart watch", "stock_available": True}),
            Action(name="UpdateInventoryStock", kwargs={
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
            "You are William Anderson (user_id: william_anderson_1842). You have recently relocated and must update your profile address to 234 Mountain View Drive, Apt 15, Phoenix, AZ 80205, USA. You also wish to make a purchase for the least expensive smartphone you could find and ensure it is sent to your new address. Update your profile, confirm the new shipping address, place an order that will be carried out by QuickPath Distribution."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Wilson", "user_id": "william_anderson_1842"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "william_anderson_1842",
                "profile_updates": {
                    "address": {
                        "address1": "234 Mountain View Drive",
                        "address2": "Apt 15",
                        "city": "Phoenix",
                        "state": "AZ",
                        "zip": "80205",
                        "country": "USA"
                    }
                }
            }),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "william_anderson_1842"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "smartphone",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5339029584", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "william_anderson_1842"}),
            Action(name="GetCourierByName", kwargs={"courier_name": "QuickPath Distribution"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "william_anderson_1842",
                "item_list": [
                    {"item_id": "5339029584", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_7871433"]
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1,
                                                           "courier_id": "#COU0005",
                                                           "order_value": 1219.31,
                                                           "location": {
                                                                "address1": "234 Mountain View Drive",
                                                                "address2": "Apt 15",
                                                                "city": "Phoenix",
                                                                "state": "AZ",
                                                                "zip": "80205",
                                                                "country": "USA"
                                                            }
                                                           }),
            Action(name="CreateOrder", kwargs={
                "user_id": "william_anderson_1842",
                "items": [{"item_id": "5339029584", "quantity": 1}],
                "payment_method_sources": ["credit_card_7871433"],
                "tax_amount": 90.32,
                "shipping_cost": 29.78
            }),
            Action(name="AssignTrackingNumber", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0005"}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 1249.09,
                                                  "courier_id": "#COU0005",
                                                  "tracking_ids": ["TRKBATCH01C0005"],
                                                  "location": {
                                                      "address1": "234 Mountain View Drive",
                                                      "address2": "Apt 15",
                                                      "city": "Phoenix",
                                                      "state": "AZ",
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
            "You are assisting Ethan Ito (user_id: ethan_ito_3850) with a substantial corporate electronics order—3 tablets and 2 headphones for their office. Purchase the most affordable items, verify them, check their availability, calculate the total costs, process the order, and arrange for delivery through Priority Shipping Co.."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Noah", "last_name": "Ito", "user_id": "ethan_ito_3850"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "tablet",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "headphones",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ethan_ito_3850"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "ethan_ito_3850",
                "item_list": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
                "payment_methods_source": ["credit_card_1620755"]
            }),
            Action(name="GetCourierByName", kwargs={"courier_name": "Priority Shipping Co."}),

            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 5, "order_value": 3673.03,
                                                           "courier_id": "#COU0003",
                                                            "address": {
                                                                "address1": "619 Broadway",
                                                                "address2": "Suite 484",
                                                                "city": "Portland",
                                                                "country": "USA",
                                                                "state": "OR",
                                                                "zip": "98187"
                                                            }}),
            Action(name="CreateOrder", kwargs={
                "user_id": "ethan_ito_3850",
                "items": [
                    {"item_id": "2106335193", "quantity": 3},
                    {"item_id": "7184044281", "quantity": 2}
                ],
                "payment_method_sources": ["credit_card_1620755"],
                "tax_amount": 272.08,
                "shipping_cost": 76.59
            }),
            Action(name="AssignTrackingNumber", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0003"}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 3749.62, "courier_id": "#COU0003",
                                                  "tracking_ids": ["TRKBATCH01C0003"],
                                                  "location": {
                                                        "address1": "619 Broadway",
                                                        "address2": "Suite 484",
                                                        "city": "Portland",
                                                        "country": "USA",
                                                        "state": "OR",
                                                        "zip": "98187"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_43",
        instruction=(
"You are Mia Russo (mia_russo_7776), the procurement manager tasked with conducting a detailed supplier performance evaluation for electronics suppliers. Evaluate suppliers #SUP0001, #SUP0004, and #SUP0007. Check the capacity of SUP0001, SUP0004, and SUP0007, and revise their performance ratings and comments."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Rossi", "user_id": "mia_russo_7776"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0001",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0004",
                "performance_rating": 2.0,
                "notes": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability."
            }),
            Action(name="UpdateSupplierInfo", kwargs={
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
            "You are Mia Lopez (user_id: mia_lopez_9707). You aim to purchase gifts for Liam Walker (liam_walker_5124) and Olivia Wilson (olivia_wilson_8847). Acquire a high-end Vacuum Cleaner for Lucas and a high-end Air Purifier for Emma, then create orders for both. Arrange delivery to their addresses via QuickPath Distribution."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Sanchez", "user_id": "mia_lopez_9707"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "vacuum cleaner",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "air purifier",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "4806644905", "quantity": 1},
                    {"item_id": "8302289002", "quantity": 1},
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "mia_lopez_9707"}),
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lucas", "last_name": "Davis", "user_id": "liam_walker_5124"}),
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Brown", "user_id": "olivia_wilson_8847"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mia_lopez_9707",
                "item_list": [
                    {"item_id": "4806644905", "quantity": 1},
                ],
                "payment_methods_source": ["paypal_1191071"]
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mia_lopez_9707",
                "item_list": [
                    {"item_id": "8302289002", "quantity": 1},
                ],
                "payment_methods_source": ["paypal_1191071"]
            }),
            Action(name="GetCourierByName", kwargs={"courier_name": "QuickPath Distribution"}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 711.6, "courier_id": "#COU0005",
                                                  "location": {
                                                       "address1": "852 Oak Street",
                                                        "address2": "Suite 747",
                                                        "city": "Jacksonville",
                                                        "country": "USA",
                                                        "state": "AL",
                                                        "zip": "32187"}}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 591.35, "courier_id": "#COU0005",
                                                  "location": {
                                                       "address1": "984 Hickory Lane",
                                                        "address2": "Suite 834",
                                                        "city": "Jacksonville",
                                                        "country": "USA",
                                                        "state": "AL",
                                                        "zip": "32165"}}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 711.6,
                                                           "courier_id": "#COU0005",
                                                           "address": {
                                                               "address1": "852 Oak Street",
                                                               "address2": "Suite 747",
                                                               "city": "Jacksonville",
                                                               "country": "USA",
                                                               "state": "AL",
                                                               "zip": "32187"}}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 591.35,
                                                           "courier_id": "#COU0005",
                                                           "address": {
                                                               "address1": "984 Hickory Lane",
                                                               "address2": "Suite 834",
                                                               "city": "Jacksonville",
                                                               "country": "USA",
                                                               "state": "AL",
                                                               "zip": "32165"}}),
            Action(name="CreateOrder", kwargs={
                "user_id": "mia_lopez_9707",
                "items": [
                    {"item_id": "4806644905", "quantity": 1},
                ],
                "payment_method_sources": ["paypal_1191071"],
                "tax_amount": 52.71,
                "shipping_cost": 11.49
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mia_lopez_9707",
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
            "As Chen Moore (user_id: chen_moore_6080), you wish to purchase a black smart watch and headphones for your new apartment. Ensure that both items are available and within your budget. Look for these products, confirm your identity, verify availability, and finalize the transaction using your credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Moore", "user_id": "chen_moore_6080"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "smart watch",
                "options": {"color": "black"},
                "available_only": True,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "headphones",
                "options": {"color": "black"},
                "available_only": True,
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2860956907", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "chen_moore_6080"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "chen_moore_6080",
                "item_list": [
                    {"item_id": "2860956907", "quantity": 1},
                    {"item_id": "7184044281", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_4041739"]
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "chen_moore_6080",
                "payment_method_source": "credit_card_4041739",
                "amount": 712.97
            }),
            Action(name="CreateOrder", kwargs={
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
            "As a customer service representative assisting Zoe Lee (user_id: zoe_lee_7701), your task is to update their email address to yara.lee.new@example.com and incorporate a new payment option due to a recent job change. The payment method involves a Visa credit card ending in 8899. Support them in updating their profile, adding the payment method, and help with purchasing the most cost-effective t-shirt using the newly added payment option."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yara", "last_name": "Lee", "user_id": "zoe_lee_7701"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "zoe_lee_7701"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "zoe_lee_7701",
                "profile_updates": {
                    "email": "yara.lee.new@example.com"
                }
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "zoe_lee_7701",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "8899"
                }
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "t-shirt",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "3234800602", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "zoe_lee_7701"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "zoe_lee_7701",
                "item_list": [
                    {"item_id": "3234800602", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_37701"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "zoe_lee_7701",
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
"You are Omar Jackson (omar_jackson_3107), a procurement assistant handling routine maintenance tasks for supplier # SUP0005. Examine their information, update their performance rating, and supply revised feedback."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Omar", "last_name": "Lopez", "user_id": "omar_jackson_3107"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="UpdateSupplierInfo", kwargs={
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
            "You are Ella Hernandez (user_id: ella_hernandez_1701) engaging in your weekend shopping. Plan to purchase a black fleece jacket in a large size along with an affordable animal puzzle for a family game night. Locate these products, verify your payment options, and finalize the transaction using your account."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Evelyn", "last_name": "Hernandez", "user_id": "ella_hernandez_1701"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "fleece jacket",
                "options": {"size": "L", "color": "black"},
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "jigsaw puzzle",
                "options": {"theme": "animals"},
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                    {"item_id": "9665100170", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ella_hernandez_1701"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "ella_hernandez_1701",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                    {"item_id": "9665100170", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3631888"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "ella_hernandez_1701",
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
            "As a customer service representative, you're assisting Chen White (user_id: chen_white_8078). The customer's inquiry pertains to their order status, and they would like to amend their delivery address to 789 New Street, Apt 2B, Portland, OR, 97210, USA for future transactions. Examine their order history, confirm their identity, and revise their profile address accordingly."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Anderson", "user_id": "chen_white_8078"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "chen_white_8078"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W5332101"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W1701126"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W1348788"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "chen_white_8078",
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
"You are Lei Khan (user_id: lei_khan_6353), responsible for managing inventory setup for a new product line in collaboration with supplier # SUP0008. Confirm supplier details, update their rating based on recent assessments, and update their contact email to newproducts@supplier8.com. Additionally, create a new supply order for 50 units to replace the cancelled order for product ID 6679515468, and adjust inventory to reflect the new items."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lei", "last_name": "Khan", "user_id": "lei_khan_6353"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0008",
                "contact_updates": {
                    "email": "newproducts@supplier8.com"
                },
                "performance_rating": 2.0,
            }),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5916"}),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0008",
                "product_id": "6679515468",
                "item_id": "3230708338",
                "quantity": 50,
                "unit_cost": 63.6
            }),
            Action(name="UpdateInventoryStock", kwargs={
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
            "You are Sofia Li (user_id: sofia_li_3261), a returning customer aiming to swiftly purchase a white cycling helmet within a budget of $210 due to your previous one being broken. Look for small-sized helmets, confirm the item, review your saved payment options, and proceed with a quick checkout for delivery to your address. The delivery will be managed by International Speed Services."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Sofia", "last_name": "Li", "user_id": "sofia_li_3261"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "sofia_li_3261"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "cycling helmet",
                "options": {"size": "S", "color": "white"},
                "max_price": 210,
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1596993217", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "sofia_li_3261",
                "item_list": [
                    {"item_id": "1596993217", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_4046723"]
            }),
            Action(name="GetCourierByName", kwargs={"courier_name": "International Speed Services"}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 194.42,
                                                           "courier_id": "#COU0010",
                                                           "location": {
                                                                "address1": "130 Hickory Lane",
                                                                "address2": "Suite 869",
                                                                "city": "Brooklyn",
                                                                "country": "USA",
                                                                "state": "CT",
                                                                "zip": "10199"
                                                            }}),
            Action(name="CreateOrder", kwargs={
                "user_id": "sofia_li_3261",
                "items": [{"item_id": "1596993217", "quantity": 1}],
                "payment_method_sources": ["credit_card_4046723"],
                "tax_amount": 14.4,
                "shipping_cost": 11.49
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 205.91,
                                                  "courier_id": "#COU0010",
                                                  "location": {
                                                      "address1": "130 Hickory Lane",
                                                      "address2": "Suite 869",
                                                      "city": "Brooklyn",
                                                      "state": "CT",
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
            "You are a customer service representative assisting Olivia Clark (user_id: olivia_clark_6993). The customer is inquiring about their gift card balance and wishes to buy an LED Light Bulb with wifi connectivity, but is uncertain about sufficient funds. Assist them in verifying their balance, locating suitable products within their budget, and facilitate the purchase."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Martin", "user_id": "olivia_clark_6993"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "olivia_clark_6993"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "olivia_clark_6993"}),
            Action(name="VerifyGiftCardBalance", kwargs={"first_name": "Emma", "last_name": "Martin", "user_id": "olivia_clark_6993"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "led light bulb",
                "options": {"connectivity": "Wi-Fi"},
                "max_price": 57
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "7445824652", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "olivia_clark_6993",
                "item_list": [
                    {"item_id": "7445824652", "quantity": 1}
                ],
                "payment_methods_source": ["gift_card_4129829"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "olivia_clark_6993",
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
"As William Li (james_li_6934), a warehouse manager, you need to adjust inventory levels for supplier # SUP0010 is prompted by fluctuations in seasonal demand. Check supplier information, evaluate their capacity, adjust stock levels for recent orders by increasing them by 50 units, and create new supply orders for the same amount to meet expected demand."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mason", "last_name": "Li", "user_id": "james_li_6934"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="UpdateInventoryStock", kwargs={
                "supplier_id": "#SUP0010",
                "item_id": "8591113813",
                "new_stock_level": 50,
                "stock_action": "add"
            }),
            Action(name="CreateSupplyOrder", kwargs={
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
            "As Zoe Clark with user_id: zoe_clark_9470, you are preparing for outdoor adventures. Search for hiking boots within a budget of $240 and a fleece jacket within a budget of $145. Proceed to purchase both items using your credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yara", "last_name": "Martin", "user_id": "zoe_clark_9470"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "hiking boots",
                "max_price": 240,
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "fleece jacket",
                "max_price": 145,
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "8277474082", "quantity": 1},
                    {"item_id": "5992316252", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "zoe_clark_9470"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "zoe_clark_9470",
                "item_list": [
                    {"item_id": "8277474082", "quantity": 1},
                    {"item_id": "5992316252", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1006622"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "zoe_clark_9470",
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
            "As a customer service representative, assist Isabella Khan with user_id: isabella_khan_9030. The customer intends to ship clothing to 456 Maple Street, Suite 890, Vancouver, BC V6B 1A1, Mexico. She requires information on international shipping costs. She needs to place an order for the most expensive fleece jacket, determine international shipping costs, and complete the order using your visa credit card. Delivery will be managed by RapidTransit Solutions."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Olivia", "last_name": "Khan", "user_id": "isabella_khan_9030"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "fleece jacket",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1},
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "isabella_khan_9030"}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "isabella_khan_9030",
                                                             "custom_address": {
                                                                 "address1": "456 Maple Street",
                                                                 "address2": "Suite 890",
                                                                 "city": "Vancouver",
                                                                 "state": "BC",
                                                                 "zip": "V6B 1A1",
                                                                 "country": "Mexico"
                                                             }}),
            Action(name="GetCourierByName", kwargs={"courier_name": "RapidTransit Solutions"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "isabella_khan_9030",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1936578"],
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "Mexico", "total_items": 1, "order_value": 172.71,
                                                           "courier_id": "#COU0002",
                                                            "address": {
                                                                "address1": "456 Maple Street",
                                                                "address2": "Suite 890",
                                                                "city": "Vancouver",
                                                                "state": "BC",
                                                                "zip": "V6B 1A1",
                                                                "country": "Mexico"
                                                            }}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "isabella_khan_9030",
                "item_list": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_1936578"],
                "shipping_cost": 26.49
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "isabella_khan_9030",
                "items": [
                    {"item_id": "9385662952", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_1936578"],
                "tax_amount": 12.79,
                "shipping_cost": 26.49
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "Mexico", "order_value": 199.2, "courier_id": "#COU0002",
                                                  "location": {
                                                       "address1": "456 Maple Street",
                                                        "address2": "Suite 890",
                                                        "city": "Vancouver",
                                                        "state": "BC",
                                                        "zip": "V6B 1A1",
                                                        "country": "Mexico"}}),

        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_56",
        instruction=(
"You are Mason Williams (mason_williams_5676), responsible for vendor relations and updating contact details for supplier # SUP0006. Their office has moved, and their contact details have been updated to +1-800-555-0167 and newoffice@supplier6.com. Update their information, confirm their current capacity, and place supply orders for the available running shoes (5 units each)."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Liam", "last_name": "Johnson", "user_id": "mason_williams_5676"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0006",
                "contact_updates": {
                    "phone": "+1-800-555-0167",
                    "email": "newoffice@supplier6.com"
                },
            }),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["running shoes"]}),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["6938111410"],
                                                           "show_available": True,
                                                           "product_type": "running shoes"}),
            Action(name="CreateSupplyOrder", kwargs={
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
            "You are Evelyn Dean (user_id: evelyn_dean_4338). You are in the process of outfitting a new kitchen and intend to purchase an automatic espresso machine along with a 3 piece luggage set for an upcoming trip. Your budget for the luggage is $500, and for the espresso machine, it ranges from $2700 to $2800. Search for these products, verify your identity, confirm their availability, and finalize the purchases using your PayPal account."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Amelia", "last_name": "Kim", "user_id": "evelyn_dean_4338"}),\
            Action(name="SearchProductsByFilter", kwargs={
                "category": "espresso machine",
                "options": {"type": "automatic"},
                "min_price": 2700,
                "max_price": 2800,
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "luggage set",
                "options": {"piece count": "3-piece"},
                "max_price": 500,
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "3709608322", "quantity": 1},
                    {"item_id": "6301799585", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "evelyn_dean_4338"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "evelyn_dean_4338",
                "item_list": [
                    {"item_id": "3709608322", "quantity": 1},
                    {"item_id": "6301799585", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_1742092"]
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "evelyn_dean_4338",
                "payment_method_source": "paypal_1742092",
                "amount": 3499.82
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "evelyn_dean_4338",
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
            "You are a customer service representative assisting Juan Clark (user_id: juan_clark_4740). The customer has obtained a new MasterCard credit card ending in 5678 and wishes to update their payment options. Following this, they want to order a black dialed silicone wristwatch. Assist them in adding the new payment method and help complete the purchase."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Martin", "user_id": "juan_clark_4740"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "juan_clark_4740"}),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "juan_clark_4740",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "mastercard",
                    "last_four": "5678"
                }
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "wristwatch",
                "options": {"strap material": "silicone", "dial color": "black"},
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1994478369", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_clark_4740",
                "item_list": [
                    {"item_id": "1994478369", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_24740"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "juan_clark_4740",
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
"Assume the role of Evelyn Anderson (user_id: amelia_wilson_4999), a seasonal planning manager tasked with organizing inventory for sneaker sales with supplier # SUP0003. Review the supplier's information, update their performance data based on the latest feedback, evaluate their sneaker production capability, and create a supply order for 10 units of each available sneaker variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Isabella", "last_name": "Brown", "user_id": "amelia_wilson_4999"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0003",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["sneakers"]}),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["7471004230"],
                                                           "show_available": True,
                                                           "product_type": "sneakers"}),
            Action(name="CreateSupplyOrder", kwargs={
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
            "Play the role of Mohamed Thompson (user_id: mohamed_thompson_1549). Your objective is to replace your outdated electronics with a luxurious smartphone and wireless headphones. Locate these products, verify them, review your payment options, and finalize the upgrade purchase."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Mohamed", "last_name": "Jackson", "user_id": "mohamed_thompson_1549"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "smartphone",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "headphones",
                "options": {"connectivity": "wireless"},
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "1507389580", "quantity": 1},
                    {"item_id": "3104857380", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "mohamed_thompson_1549"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mohamed_thompson_1549",
                "item_list": [
                    {"item_id": "1507389580", "quantity": 1},
                    {"item_id": "3104857380", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3313158"]
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "mohamed_thompson_1549",
                "payment_method_source": "credit_card_3313158",
                "amount": 1658.7
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mohamed_thompson_1549",
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
"As a customer service representative assisting Daiki Williams (user_id: daiki_williams_9523), you need to address the customer's request concerning order # W1436802 requires the addition of a 24MP digital camera with 3x zoom before shipment. Review the existing order, help incorporate the new product, and modify the order as needed."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Johnson", "user_id": "daiki_williams_9523"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "daiki_williams_9523"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W1436802"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "digital camera",
                "options": {"resolution": "24MP", "zoom": "3x"},
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5996159312", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "daiki_williams_9523"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "daiki_williams_9523",
                "item_list": [
                    {"item_id": "5996159312", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_2433177"]
            }),
            Action(name="AddToOrder", kwargs={
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
"In your role as Ella Lee, a category manager, you are tasked with expanding the electronics product line in collaboration with supplier # SUP0009. Review existing products, analyze their capacity, update the supplier email to thenewemail@example.com, and schedule supply orders of 5 units for all deliverable products."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Evelyn", "last_name": "Lee"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0009",
                "contact_updates": {
                    "email": "thenewemail@example.com"
                },
            }),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["7996920482", "1075968781", "4354588079", "9832717871"],
                                                           "show_available": True}),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "7996920482",
                "item_ids": ["3020722515", "9862136885", "5952720925", "7211586944", "1349017811"],
                "quantity": 5,
                "unit_cost": [238.64, 258.32, 260.19, 272.71, 226.05]
            }),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "1075968781",
                "item_ids": ["4064702754", "5428723833", "1240311797", "9472539378", "2323972008", "9624127908", "4458619711", "7602931732"],
                "quantity": 5,
                "unit_cost": [159.78, 145.48, 137.17, 143.72, 146.98, 158.9, 153.81, 153.25]
            }),
            Action(name="CreateSupplyOrder", kwargs={
                "supplier_id": "#SUP0009",
                "product_id": "4354588079",
                "item_ids": ["3709608322", "7407838442", "1157853815", "2190871011", "3714494375", "3815173328", "7774234341", "3951031513", "9884666842", "3379843752"],
                "quantity": 5,
                "unit_cost":[2744.7, 3081.91, 3096.7, 3105.6, 2709.83, 2908.42, 2719.16, 3289.46, 2794.7, 3203.76]
            }),
            Action(name="CreateSupplyOrder", kwargs={
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
            "Identify yourself as Isabella Lopez. You aim to purchase luxurious gifts for your family: a bicycle for your son and a cycling helmet to ensure safety. Locate these products, verify them, finalize the holiday purchase using PayPal and arrange for it to be delivered to your address via Reliable Delivery Co."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Olivia", "last_name": "Sanchez"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "bicycle",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "cycling helmet",
                "price_flag": "expensive",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "isabella_lopez_2914"}),
            Action(name="GetCourierByName", kwargs={"courier_name": "Reliable Delivery Co."}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "isabella_lopez_2914",
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_3388537"],
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 2608.11,
                                                           "courier_id": "#COU0009",
                                                            "location": {
                                                                "address1": "710 Sunset Drive",
                                                                "address2": "Suite 855",
                                                                "city": "Pittsburgh",
                                                                "country": "USA",
                                                                "state": "OH",
                                                                "zip": "19116"
                                                            }}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "isabella_lopez_2914",
                "item_list": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_methods_source": ["paypal_3388537"],
                "shipping_cost": 53.11,
            }),
            Action(name="ProcessPayment", kwargs={
                "user_id": "isabella_lopez_2914",
                "payment_method_source": "paypal_3388537",
                "amount": 2661.22
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "isabella_lopez_2914",
                "items": [
                    {"item_id": "3624655057", "quantity": 1},
                    {"item_id": "9013366374", "quantity": 1}
                ],
                "payment_method_sources": ["paypal_3388537"],
                "tax_amount": 193.19,
                "shipping_cost": 53.11
            }),
            Action(name="AssignTrackingNumber", kwargs={"order_ids": ["#W0001001"], "preferred_courier_id": "#COU0009"}),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 2661.22, "courier_id": "#COU0009",
                                                  "tracking_ids": ["TRKBATCH01C0009"],
                                                  "location": {
                                                      "address1": "710 Sunset Drive",
                                                      "address2": "Suite 855",
                                                      "city": "Pittsburgh",
                                                      "country": "USA",
                                                      "state": "OH",
                                                      "zip": "19116"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_64",
        instruction=(
"Identify yourself as Olivia Ito (user_id: olivia_ito_4529). You placed an order yesterday but neglected to include a small red fleece jacket. You intend to append it to your existing order # W8664580 prior to shipping. Verify your identity, check your order history, add the fleece jacket to your existing order, and complete the addition with your Visa."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Ito", "user_id": "olivia_ito_4529"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "olivia_ito_4529"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W8664580"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "fleece jacket",
                "options": {"size": "S", "color": "red"},
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "5992316252", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "olivia_ito_4529"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "olivia_ito_4529",
                "item_list": [
                    {"item_id": "5992316252", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8058445"]
            }),
            Action(name="AddToOrder", kwargs={
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
            "As a customer service representative, assist Lucas Rodriguez (user_id: lucas_rodriguez_6635). The customer is interested in finding out which products they purchased in their recent orders and intends to cancel the order for the office chair due to a change in circumstances."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ivan", "last_name": "Santos", "user_id": "lucas_rodriguez_6635"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "lucas_rodriguez_6635"}),
            Action(name="GetProductIds", kwargs={
                "user_id": "lucas_rodriguez_6635",
                "order_ids": ["#W6893533", "#W8770097", "#W5183325", "#W3913498"],
            }),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["office chair"],
                                                                         "product_ids": ['1656367028', '1968349452', '2696197613', '4794339885',
                                                                                         '6679515468', '6945232052', '8940227892', '9924732112']}),
            Action(name="GetOrderIdsByProductIds", kwargs={"product_ids": ["4794339885"], "user_id": "lucas_rodriguez_6635"}),
            Action(name="CancelOrder", kwargs={"user_id": "lucas_rodriguez_6635", "order_id": "#W8770097", "cancellation_reason": "change in circumstances"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_66",
        instruction=(
"You are Fatima Martinez, a procurement manager tasked with expanding supplier # Portfolio of SUP0011. The supplier aims to start providing kitchen appliances, specifically available espresso machines. You must organize supply orders for 10 units of each espresso machine variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Fatima", "last_name": "Garcia"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["espresso machine"]}),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["4354588079"],
                                                           "show_available": True,
                                                           "product_type": "espresso machine"}),
             Action(name="CreateSupplyOrder", kwargs={
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
            "You are Mia Martinez (user_id: mia_martinez_3271). Your task is to review your purchase history to locate the laptop you have bought. Retrieve your order history, examine your payment options, and place another order for the same laptop you previously purchased."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Anya", "last_name": "Garcia", "user_id": "mia_martinez_3271"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "mia_martinez_3271"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "mia_martinez_3271"}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "mia_martinez_3271",
                "item_list": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8955149"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "mia_martinez_3271",
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
            "You are assisting as a customer service representative for Ella Ahmed (user_id: ella_ahmed_3960). The customer has relocated to a new address at 789 Mountain View Drive, Apt 3A, Tucson, AZ 80218, USA and needs to update their profile accordingly. Additionally, they wish to add a new gift card with a $500 balance and ensure it is correctly reflected in their account."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Evelyn", "last_name": "Ahmed", "user_id": "ella_ahmed_3960"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "ella_ahmed_3960",
                "profile_updates": {
                    "address": {
                        "address1": "789 Mountain View Drive",
                        "address2": "Apt 3A",
                        "city": "Tucson",
                        "state": "AZ",
                        "zip": "80218",
                        "country": "USA"
                    }
                }
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "ella_ahmed_3960",
                "payment_type": "gift_card",
                "payment_details":{
                    "balance": 500
                }
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ella_ahmed_3960"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_69",
        instruction=(
"You are Olivia Kovacs (olivia_kovacs_9839), a category manager examining supplier # Evaluate SUP0010's current selection as you consider adding new t-shirt styles. Check their current inventory, confirm production capacity, identify suppliers with similar products that have a minimum of 20 units in stock, and place an order for 20 units of every available variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Kovacs", "user_id": "olivia_kovacs_9839"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["t-shirt"]}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "product_id": "9523456873",
                "product_type": ["t-shirt"],
                "min_stock_level": 20
            }),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["9523456873"],
                                                           "show_available": True,
                                                           "product_type": "t-shirt"}),
            Action(name="CreateSupplyOrder", kwargs={
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
"You are Liam Williams (user_id: liam_williams_2067). You need to review your recent order # Review order W7016806 and consider buying an additional water bottle. Check your purchase history, validate payment methods, find a stainless steel bottle in the same color, confirm it, and complete the transaction using your credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lucas", "last_name": "Johnson", "user_id": "liam_williams_2067"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "liam_williams_2067"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "liam_williams_2067"}),
            Action(name='GetProductInfo', kwargs={"item_id": "5758737025"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "water bottle",
                "options": {"color": "green", "material": "stainless steel"},
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "7533802601", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "liam_williams_2067",
                "item_list": [
                    {"item_id": "7533802601", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3956549"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "liam_williams_2067",
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
            "Handle customer service inquiries to assist Juan White (user_id: juan_white_5671). The customer seeks guidance in locating an action camera with 5k resolution in black. Provide recommendations, register his visa ending in 7890 as a new payment method, verify the order along with payment methods, and finalize the purchase."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Anderson", "user_id": "juan_white_5671"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "action camera",
                "options": {"resolution": "5k", "color": "black"},
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "juan_white_5671",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "7890"
                }
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "juan_white_5671"}),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "7523669277", "quantity": 1}
                ],
            }),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "juan_white_5671",
                "item_list": [
                    {"item_id": "7523669277", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_25671"]
            }),
            Action(name="CreateOrder", kwargs={
                "user_id": "juan_white_5671",
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
"As Luna Dean (luna_dean_2998), manage the vendor's activities to improve supplier # SUP0010's sports gear lineup aims to expand its cycling offerings beyond helmets. Evaluate their capacity, revise their data to include recent performance metrics, and arrange new purchase orders of 35 units for each available bicycle model."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "luna_dean_2998"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0010",
                "performance_rating": 5.0,
                "notes": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders."
            }),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["bicycle"]}),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["9783735446"],
                                                           "show_available": True,
                                                           "product_type": "bicycle"}),
            Action(name="CreateSupplyOrder", kwargs={
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
            "You are Daiki Williams user_id: daiki_williams_6200. You are organizing a home office and want to buy a laptop and a gaming mouse. Look up products by name. Your priority is to locate the most economical options available. Verify items, review your payment methods, and finalize the purchase using your credit card. This should be delivered to your location via AgileTransport Services."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Johnson", "user_id": "daiki_williams_6200"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "laptop",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "gaming mouse",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "daiki_williams_6200"}),
            Action(name="GetCourierByName", kwargs={"courier_name": "AgileTransport Services"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "daiki_williams_6200",
                "item_list": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_8934029"]
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 2, "order_value": 2623.96,
                                                           "courier_id": "#COU0004",
                                                            "location": {
                                                                "address1": "375 Elm Avenue",
                                                                "address2": "Suite 947",
                                                                "city": "Tucson",
                                                                "country": "USA",
                                                                "state": "AZ",
                                                                "zip": "85017"
                                                            }}),
            Action(name="CreateOrder", kwargs={
                "user_id": "daiki_williams_6200",
                "items": [
                    {"item_id": "2880340443", "quantity": 1},
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_8934029"],
                "tax_amount": 194.37,
                "shipping_cost": 53.35
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 2677.31, "courier_id": "#COU0004",
                                                  "location": {
                                                       "address1": "375 Elm Avenue",
                                                        "address2": "Suite 947",
                                                        "city": "Tucson",
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
            "You are Chen Williams (user_id: chen_williams_4204). You wish to buy a smart watch for tracking fitness using your gift card and PayPal as a backup payment method. Search for gold smart watches with AMOLED display under $350, confirm availability and address, place the order, and choose Tomorrow Shipping Co. for delivery to his address."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Chen", "last_name": "Johnson", "user_id": "chen_williams_4204"}),
            Action(name="SearchProductsByFilter", kwargs={"category": "smart watch", "max_price": 350,
                                                             "options": {
                                                                "color": "gold",
                                                                "display": "AMOLED",
                                                            }}),
            Action(name="GetProductInfo", kwargs={"item_id": "5694328282"}),
            Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "5694328282", "quantity": 1}]}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "chen_williams_4204"}),
            Action(name="GetCourierByName", kwargs={"courier_name": "Tomorrow Shipping Co."}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "chen_williams_4204",
                "item_list": [{"item_id": "5694328282", "quantity": 1}],
                "payment_methods_source": ["gift_card_3406421", "paypal_3742148"],
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 349.05,
                                                           "courier_id": "#COU0008",
                                                            "location": {
                                                                "address1": "503 Elm Avenue",
                                                                "address2": "Suite 641",
                                                                "city": "Houston",
                                                                "country": "USA",
                                                                "state": "NM",
                                                                "zip": "77004"
                                                            }}),
            Action(name="CreateOrder", kwargs={
                "user_id": "chen_williams_4204",
                "items": [
                    {"item_id": "5694328282", "quantity": 1}
                ],
                "payment_method_sources": ["gift_card_3406421", "paypal_3742148"],
                "tax_amount": 25.86,
                "shipping_cost": 11.49
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 360.54, "courier_id": "#COU0008",
                                                  "location": {
                                                        "address1": "503 Elm Avenue",
                                                        "address2": "Suite 641",
                                                        "city": "Houston",
                                                        "country": "USA",
                                                        "state": "NM",
                                                        "zip": "77004"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_75",
        instruction=(
            "As a customer service representative, assist Sofia Russo (user_id: sofia_russo_8776) in updating her pending deliveries to her new office location at 1000 Market Street, Suite 500, Pittsburgh, OH 19107, USA."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Sofia", "last_name": "Rossi", "user_id": "sofia_russo_8776"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "sofia_russo_8776",
                "order_id": "#W5918442",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Pittsburgh",
                    "state": "OH",
                    "zip": "19107",
                    "country": "USA"
                }
            }),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "sofia_russo_8776",
                "order_id": "#W5500815",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Pittsburgh",
                    "state": "OH",
                    "zip": "19107",
                    "country": "USA"
                }
            }),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "sofia_russo_8776",
                "order_id": "#W2818151",
                "new_address": {
                    "address1": "1000 Market Street",
                    "address2": "Suite 500",
                    "city": "Pittsburgh",
                    "state": "OH",
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
"Operating as Isabella Johnson (user_id: isabella_johnson_5265), a supply chain manager for the retail company, coordinate inventory updates for supplier # SUP0008 related to LED lighting products. Verify the existing information, update the contact email to 'support@smartlighting.com', check the inventory levels for LED lighting, and increase the stock by 50 units for each available variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Olivia", "last_name": "Smith", "user_id": "isabella_johnson_5265"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0008",
                "contact_updates": {"email": "support@smartlighting.com"}
            }),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["led light bulb"]}),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["2696197613"],
                                                           "show_available": True,
                                                           "product_type": "led light bulb"}),
            Action(name="UpdateInventoryStock", kwargs={
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
            "You are Evelyn Anderson (user_id: evelyn_anderson_4614). Your intention is to return the dumbbell due to it arriving damaged. You must initiate a return request for the order and obtain the shipping cost from the same courier that made the delivery."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Amelia", "last_name": "Wilson", "user_id": "evelyn_anderson_4614"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "evelyn_anderson_4614"}),
            Action(name="GetPurchasedItems", kwargs={"user_id": "evelyn_anderson_4614", "order_id": "#W9077205"}),
            Action(name="GetCourier", kwargs={"tracking_id": "882867966563"}),
            Action(name="RequestOrderReturn", kwargs={
                "user_id": "evelyn_anderson_4614",
                "order_id": "#W9077205",
                "return_items": [
                    {"item_id": "3877338112", "quantity": 1, "reason": "arrived damaged"},
                ],
                "return_reason": "arrived damaged"
            }),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "new_status": "for return"}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "evelyn_anderson_4614"}),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 545.68,
                                                           "courier_id": "#COU0009"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_78",
        instruction=(
            "As a customer service representative aiding Lucas Khan (user_id: lucas_khan_7475), you need to clarify the fulfillment status of his order. Ivan wishes to confirm that his pending orders are advancing towards delivery and prefers using Punctual Express Services as his courier. Your aim is to give Ivan a detailed status update and ensure effective order processing that aligns with his delivery preferences, adhering to standard operational procedures."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={
                "first_name": "Ivan",
                "last_name": "Khan",
                "user_id": "lucas_khan_7475"
            }),
            Action(name="GetUserOrderHistory", kwargs={
                "user_id": "lucas_khan_7475"
            }),
            Action(name="GetCourierByName", kwargs={
                "courier_name": "Punctual Express Services"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W5270061"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W7032009"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W1519594"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W5782623"
            }),
            Action(name="AssignTrackingNumber", kwargs={
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
"As Juan Johnson (user_id: juan_johnson_5229), a procurement specialist at the retail firm, handle supplier # Assess SUP0001 relationships, modify their contact number to '+1-555-0123', and adjust their performance rating to 5.0. Organize new t-shirt supply orders, ensuring 40 units are obtained for each item variant."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_johnson_5229"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="ValidateSupplierCapacity", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0001",
                "contact_updates": {"phone": "+1-555-0123"},
                "performance_rating": 5.0,
            }),
            Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["t-shirt"]}),
            Action(name="SearchSuppliersByProduct", kwargs={
                "product_id": "9523456873",
                "supplier_id": "#SUP0001",
                "product_type": ["t-shirt"]
            }),
            Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["9523456873"],
                                                           "show_available": True,
                                                           "product_type": "t-shirt"}),
            Action(name="CreateSupplyOrder", kwargs={
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
            "Being Ethan Khan (user_id: noah_khan_3904), you require a laptop meeting specific requirements: 15-inch screen, i7 processor, 32GB RAM, within a $2800 budget. Look for available models, confirm their specifications, place an order using your credit card, and make sure it is delivered by FleetFast Delivery."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Ethan", "last_name": "Khan", "user_id": "noah_khan_3904"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "laptop",
                "options": {"screen size": "15-inch", "processor": "i7", "ram": "32GB"},
                "max_price": 2800,
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "6017636844"}),
            Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "noah_khan_3904"}),
            Action(name="GetCourierByName", kwargs={"courier_name": "FleetFast Delivery"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "noah_khan_3904",
                "item_list": [{"item_id": "6017636844", "quantity": 1}],
                "payment_methods_source": ["credit_card_5608852"]
            }),
            Action(name="CalculateShippingCost", kwargs={"destination_country": "USA", "total_items": 1, "order_value": 2475.76,
                                                           "courier_id": "#COU0006",
                                                            "location": {
                                                                "address1": "264 Elm Street",
                                                                "address2": "Suite 579",
                                                                "city": "San Diego",
                                                                "country": "USA",
                                                                "state": "NV",
                                                                "zip": "92117"
                                                            }}),
            Action(name="CreateOrder", kwargs={
                "user_id": "noah_khan_3904",
                "items": [
                    {"item_id": "6017636844", "quantity": 1}
                ],
                "payment_method_sources": ["credit_card_5608852"],
                "tax_amount": 183.39,
                "shipping_cost": 48.63
            }),
            Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 2524.39, "courier_id": "#COU0006",
                                                  "location": {
                                                        "address1": "264 Elm Street",
                                                        "address2": "Suite 579",
                                                        "city": "San Diego",
                                                        "country": "USA",
                                                        "state": "NV",
                                                        "zip": "92117"}}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_81",
        instruction=(
"Assist Ava Martinez (user_id: ava_martinez_5795) with overseeing the shipping logistics for her recent orders #W4958652 and #W4958652 and #W6447372. She has moved and plans to consolidate shipping via FleetFast Delivery for these orders. Your responsibility is to configure both orders for delivery to her new address and prepare them for shipment with her selected courier."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={
                "first_name": "Sophia",
                "last_name": "Garcia",
                "user_id": "ava_martinez_5795"
            }),
            Action(name="GetUserOrderHistory", kwargs={
                "user_id": "ava_martinez_5795"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W4958652"
            }),
            Action(name="CheckOrderStatus", kwargs={
                "order_id": "#W6447372"
            }),
            Action(name="GetCourierByName", kwargs={
                "courier_name": "FleetFast Delivery"
            }),
            Action(name="ValidateShippingAddress", kwargs={
                "user_id": "ava_martinez_5795"
            }),
            Action(name="UpdateDeliveryAddress", kwargs={
                "user_id": "ava_martinez_5795",
                "order_id": "#W4958652",
                "new_address": {
                    "address1": "536 Cedar Street",
                    "address2": "Suite 916",
                    "city": "Raleigh",
                    "country": "USA",
                    "state": "NC",
                    "zip": "28212"
                }
            }),
            Action(name="AssignTrackingNumber", kwargs={
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
"Act as Ahmad Harris (user_id: ahmad_harris_7149), a cost analyst at the retail company. Supply order # SO6035 needs cost updates. Examine the existing terms, change the unit price to $28.50, and update the payment terms to 'COD'."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yusuf", "last_name": "Taylor", "user_id": "ahmad_harris_7149"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="UpdateSupplyOrderTerms", kwargs={
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
            "As Ahmad Moore (user_id: ahmad_moore_6437), you are looking for an electric toothbrush featuring high-speed settings and a rechargeable battery. Look into available options, confirm your stored address, and finalize the purchase with your credit card."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yusuf", "last_name": "Moore", "user_id": "ahmad_moore_6437"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "electric toothbrush",
                "options": {"speed settings": "high", "battery type": "rechargeable"},
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "8098621301"}),
            Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "8098621301", "quantity": 1}]}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "ahmad_moore_6437"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ahmad_moore_6437"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "ahmad_moore_6437",
                "item_list": [{"item_id": "8098621301", "quantity": 1}],
                "payment_methods_source": ["credit_card_6302410"]
            }),
            Action(name="ProcessPayment", kwargs={"user_id": "ahmad_moore_6437", "payment_method_source": "credit_card_6302410", "amount": 207.52}),
            Action(name="CreateOrder", kwargs={
                "user_id": "ahmad_moore_6437",
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
"As a customer service representative assisting Lei Ahmed (user_id: lei_ahmed_1705), verify the status of order # W9015076. If the order is pending, add the cheapest garden hose to it. After adding, update the order status to processed."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Lei", "last_name": "Ahmed", "user_id": "lei_ahmed_1705"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "lei_ahmed_1705"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W9015076"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "garden hose",
                "price_flag": "cheapest",
                "limit": 1
            }),
            Action(name="ValidateOrderItems", kwargs={
                "item_list": [
                    {"item_id": "9829827210", "quantity": 1}
                ],
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "lei_ahmed_1705"}),
            Action(name="GenerateOrderSummary", kwargs={
                "user_id": "lei_ahmed_1705",
                "item_list": [
                    {"item_id": "9829827210", "quantity": 1}
                ],
                "payment_methods_source": ["credit_card_3593714"]
            }),
            Action(name="AddToOrder", kwargs={
                "order_id": "#W9015076",
                "item_id": "9829827210",
                "payment_method": "credit_card_3593714",
                "tax_amount": 7.23,
                "quantity": 1
            }),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9015076", "new_status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_85",
        instruction=(
"Assume the role of Juan Johnson (user_id: juan_johnson_9901), a warehouse manager for the retail company. Inspect supplier # For SUP0011's electric toothbrush inventory, locate items with less than 50 units in stock and increase their levels to 50. Furthermore, change the status of any out-of-stock items to available. Update the contact number to '+1-800-555-0089'."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Juan", "last_name": "Smith", "user_id": "juan_johnson_9901"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="GetSupplierInventory", kwargs={"supplier_id": "#SUP0011", "product_types": ["electric toothbrush"], "stock_level": 50,
                                                          "stock_level_comparison": "below"}),
            Action(name="UpdateInventoryStock", kwargs={
                "supplier_id": "#SUP0011",
                "item_id": "8098621301",
                "new_stock_level": 50,
                "stock_action": "set"
            }),
            Action(name="UpdateInventoryStock", kwargs={
                "supplier_id": "#SUP0011",
                "item_id": "3320557165",
                "new_stock_level": 50,
                "stock_action": "set"
            }),
            Action(name="UpdateProductAvailability", kwargs={
                "product_id": "7352963235",
                "item_id": "3320557165",
                "available": True
            }),
            Action(name="UpdateSupplierInfo", kwargs={
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
"Take on the role of Omar Moore (user_id: omar_moore_9540), a warehouse employee for the retail company. Adjust the supplier # Update SUP0011's phone number to '+1-800-555-0089' and email to 'supplierameile@example.com', then verify the updates."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Omar", "last_name": "Moore", "user_id": "omar_moore_9540"}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="UpdateSupplierInfo", kwargs={
                "supplier_id": "#SUP0011",
                "contact_updates": {"phone": "+1-800-555-0089", "email": "supplierameile@example.com"}
            }),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_87",
        instruction=(
            "Assume you are Olivia Russo (user_id: olivia_russo_2839). Your interest is in purchasing a red Bluetooth speaker that features water resistance and a 20-hour battery life for use in outdoor activities. Locate available speakers and place the order for the item."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Rossi", "user_id": "olivia_russo_2839"}),
            Action(name="SearchProductsByFilter", kwargs={
                "category": "bluetooth speaker",
                "options": {"battery life": "20 hours",
                            "color": "red",
                            "water resistance": "yes"
                           },
            }),
            Action(name="GetProductInfo", kwargs={"item_id": "7617930199"}),
            Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "7617930199", "quantity": 1}]}),
            Action(name="ValidateShippingAddress", kwargs={"user_id": "olivia_russo_2839"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "olivia_russo_2839"}),
            Action(name="ProcessPayment", kwargs={"user_id": "olivia_russo_2839", "payment_method_source": "paypal_3824028", "amount": 285.94}),
            Action(name="CreateOrder", kwargs={
                "user_id": "olivia_russo_2839",
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
            "You're acting as a customer service representative attending to Evelyn Ito (user_id: evelyn_ito_8772) during her relocation with Olivia Ito (user_id: olivia_ito_4529). Amend her delivery address and update her email to 'amelia2@example.com'."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Amelia", "last_name": "Ito", "user_id": "evelyn_ito_8772"}),
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Emma", "last_name": "Ito", "user_id": "olivia_ito_4529"}),
            Action(name="UpdateUserProfile", kwargs={
                "user_id": "evelyn_ito_8772",
                "profile_updates": {
                    "email": "amelia2@example.com",
                    "address": {
                        "address1": "965 Broadway",
                        "address2": "Suite 140",
                        "city": "Pittsburgh",
                        "country": "USA",
                        "state": "OH",
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
            "You are Ahmad Martinez (user_id: ahmad_martinez_5427) and you seek to incorporate multiple payment methods into your account. Include a Visa card ending in 1111 and a Mastercard ending in 2222."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Yusuf", "last_name": "Garcia", "user_id": "ahmad_martinez_5427"}),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ahmad_martinez_5427"}),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "ahmad_martinez_5427",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "visa",
                    "last_four": "1111"
                }
            }),
            Action(name="AddPaymentMethod", kwargs={
                "user_id": "ahmad_martinez_5427",
                "payment_type": "credit_card",
                "payment_details": {
                    "brand": "mastercard",
                    "last_four": "2222"
                }
            }),
            Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ahmad_martinez_5427"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_90",
        instruction=(
            "You are assisting as a customer service representative for Fatima White (user_id: fatima_white_2157). She intends to cancel all her pending orders due to personal reasons."
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Fatima", "last_name": "Anderson", "user_id": "fatima_white_2157"}),
            Action(name="GetUserOrderHistory", kwargs={"user_id": "fatima_white_2157"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W2974929"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W4111294"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W4514908"}),
            Action(name="CancelOrder", kwargs={
                "user_id": "fatima_white_2157",
                "order_id": "#W2974929",
                "cancellation_reason": "personal reasons"
            }),
            Action(name="CancelOrder", kwargs={
                "user_id": "fatima_white_2157",
                "order_id": "#W4514908",
                "cancellation_reason": "personal reasons"
            }),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W2974929"}),
            Action(name="CheckOrderStatus", kwargs={"order_id": "#W4514908"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_91",
        instruction=(
"You are Luna Moore user_id: luna_moore_7767, functioning as a cost analyst for the retail company. Orders supplied by # SUP0011 needs modifications. Update and verify all pricing conditions for both pending and cancelled supply orders to 'NET30'.")
        ),
        actions=[
            Action(name="ValidateUserIdentity", kwargs={"first_name": "Harper", "last_name": "Moore", "user_id": "luna_moore_7767"}),
            Action(name="SearchGetSupplyOrders", kwargs={"supplier_ids": ["#SUP0011"], "statuses": ["pending", "cancelled"]}),
            Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="UpdateSupplyOrderTerms", kwargs={
                "supply_order_id": "#SO6998",
                "payment_terms": "NET30"
            }),
            Action(name="UpdateSupplyOrderTerms", kwargs={
                "supply_order_id": "#SO2377",
                "payment_terms": "NET30"
            }),
            Action(name="UpdateSupplyOrderTerms", kwargs={
                "supply_order_id": "#SO5398",
                "payment_terms": "NET30"
            }),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO2377"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5398"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="V5TSK_USR_92",
        instruction=(
            "You are Ella Ahmed user_id: ella_ahmed_3960. It is required to obtain a 6mm yoga mat for your home workouts. Search for options in your desired thickness, confirm the item, and make the purchase using your credit card."
        ),
        actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Evelyn", "last_name": "Ahmed", "user_id": "ella_ahmed_3960"}),
        Action(name="SearchProductsByFilter", kwargs={
            "category": "yoga mat",
            "options": {"thickness": "6mm"},
        }),
        Action(name="GetProductInfo", kwargs={"item_id": "7510236436"}),
        Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "7510236436", "quantity": 1}]}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ella_ahmed_3960"}),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "ella_ahmed_3960",
            "item_list": [{"item_id": "7510236436", "quantity": 1}],
            "payment_methods_source": ["credit_card_7898168"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "ella_ahmed_3960", "payment_method_source": "credit_card_7898168", "amount": 114.13}),
        Action(name="CreateOrder", kwargs={
            "user_id": "ella_ahmed_3960",
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
        "You are Daiki Dean user_id: daiki_dean_3197, responsible for inventory management. Update the supplier # Update SUP0004's contact information to '+1-800-555-0156' and 'heythere@email.com', and verify that 100 units are added for all in-stock wireless earbuds."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Kim", "user_id": "daiki_dean_3197"}),
        Action(name="GetSupplierDetails", kwargs={"supplier_id": "#SUP0004"}),
        Action(name="UpdateSupplierInfo", kwargs={
            "supplier_id": "#SUP0004",
            "contact_updates": {"phone": "+1-800-555-0156", "email": "heythere@email.com"}
        }),
        Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["wireless earbuds"]}),
        Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["9924732112"],
                                                       "show_available": True,
                                                       "product_type": "wireless earbuds"}),
        Action(name="UpdateInventoryStock", kwargs={
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
        "As a customer service representative, assist Sofia Martin (user_id: sofia_martin_1518) by moving her pending orders to a processed status and arranging shipment through Reliable Delivery Co."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Sofia", "last_name": "Thomas", "user_id": "sofia_martin_1518"}),
        Action(name="GetUserOrderHistory", kwargs={"user_id": "sofia_martin_1518"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W7619352"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W3388163"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W2297866"}),
        Action(name="GetCourierByName", kwargs={"courier_name": "Reliable Delivery Co."}),
        Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 1097.48, "order_id": "#W7619352", "courier_id": "#COU0009"}),
        Action(name="AssignCourier", kwargs={"destination_country": "USA", "order_value": 1130.6, "order_id": "#W2297866", "courier_id": "#COU0009"}),
        Action(name="AssignTrackingNumber", kwargs={"order_ids":["#W7619352", "#W2297866"], "preferred_courier_id": "#COU0009"}),
        Action(name="UpdateOrderStatus", kwargs={"order_ids": ["#W7619352", "#W2297866"], "new_status": "processed"}),
    ],
    outputs=[]
),

Task(
    annotator="0",
    user_id="V5TSK_USR_95",
    instruction=(
        "You are Luna Dean (user_id: luna_dean_2998) from San Antonio. Determine your gift card balance and proceed to purchase a 500 pieces jigsaw puzzle if your funds are sufficient."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "luna_dean_2998"}),
        Action(name="VerifyGiftCardBalance", kwargs={"first_name": "Harper", "last_name": "Kim", "user_id": "luna_dean_2998"}),
        Action(name="SearchProductsByFilter", kwargs={
            "category": "jigsaw puzzle",
            "options": {"pieces": "500"},
            "max_price": 51
        }),
        Action(name="GetProductInfo", kwargs={"item_id": "1096508426"}),
        Action(name="ValidateOrderItems", kwargs={"item_list": [{"item_id": "1096508426", "quantity": 1}]}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "luna_dean_2998"}),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "luna_dean_2998",
            "item_list": [{"item_id": "1096508426", "quantity": 1}],
            "payment_methods_source": ["gift_card_5328393"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "luna_dean_2998", "payment_method_source": "gift_card_5328393", "amount": 49.82}),
        Action(name="CreateOrder", kwargs={
            "user_id": "luna_dean_2998",
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
        "You are William Clark (user_id: william_clark_1500) seeking details for item # Use your Visa credit card to purchase item 3254583681. Ensure you validate and review it before completing the transaction."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "william_clark_1500"}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "william_clark_1500"}),
        Action(name="GetProductInfo", kwargs={"item_id": "3254583681"}),
         Action(name="ValidateOrderItems", kwargs={
            "item_list": [
                {"item_id": "3254583681", "quantity": 1}
            ],
        }),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "william_clark_1500",
            "item_list": [{"item_id": "3254583681", "quantity": 1}],
            "payment_methods_source": ["credit_card_7083997"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "william_clark_1500", "payment_method_source": "credit_card_7083997", "amount": 326.88}),
        Action(name="CreateOrder", kwargs={
            "user_id": "william_clark_1500",
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
        "You are Emma White user_id: emma_white_7288. Revise your email to 'mia.updated@example.com' and change your address to 123 Park Avenue, Suite 112, Houston, NM 75201, USA. Ensure it appears correctly in your profile."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Mia", "last_name": "Anderson", "user_id": "emma_white_7288"}),
        Action(name="UpdateUserProfile", kwargs={
            "user_id": "emma_white_7288",
            "profile_updates": {
                "email": "mia.updated@example.com",
                "address": {
                    "address1": "123 Park Avenue",
                    "address2": "Suite 112",
                    "city": "Houston",
                    "state": "NM",
                    "zip": "75201",
                    "country": "USA"
                }
            }
        }),
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Mia", "last_name": "Anderson", "user_id": "emma_white_7288"}),
    ],
    outputs=[]
),

Task(
    annotator="0",
    user_id="V5TSK_USR_98",
    instruction=(
        "You are a customer service representative assisting Ella Jackson user_id: ella_jackson_5487. Modify all pending orders to show as processed."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Evelyn", "last_name": "Lopez", "user_id": "ella_jackson_5487"}),
        Action(name="GetUserOrderHistory", kwargs={"user_id": "ella_jackson_5487"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W1355800"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W1890669"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W3007862"}),
        Action(name="UpdateOrderStatus", kwargs={"order_id": "#W1890669", "new_status": "processed"}),
        Action(name="UpdateOrderStatus", kwargs={"order_id": "#W3007862", "new_status": "processed"}),
    ],
    outputs=[]
),

Task(
    annotator="0",
    user_id="V5TSK_USR_99",
    instruction=(
        "You are Daiki Dean (user_id: daiki_dean_3197). Change supplier # Update the contact number to +1-800-555-NEW1, change the email to daiki.kim@example.com, and modify the stock for item 9580569596 to 100 units."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Kim", "user_id": "daiki_dean_3197"}),
        Action(name="UpdateSupplierInfo", kwargs={
            "supplier_id": "#SUP0004",
            "contact_updates": {"phone": "+1-800-555-NEW1", "email": "daiki.kim@example.com"}
        }),
        Action(name="UpdateInventoryStock", kwargs={
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
        "You are William Clark (user_id: william_clark_1500). Purchase item # 6704763132 via your Mastercard."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "william_clark_1500"}),
        Action(name="ValidateOrderItems", kwargs={
            "item_list": [
                {"item_id": "6704763132", "quantity": 1}
            ],
        }),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "william_clark_1500"}),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "william_clark_1500",
            "item_list": [
                {"item_id": "6704763132", "quantity": 1}
            ],
            "payment_methods_source": ["credit_card_6932154"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "william_clark_1500", "payment_method_source": "credit_card_6932154", "amount": 329.89}),
        Action(name="AllocateInventory", kwargs={"item_id": "6704763132", "quantity": 1}),
        Action(name="CreateOrder", kwargs={
            "user_id": "william_clark_1500",
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
        "As a customer sales representative, assist William Clark (user_id: william_clark_1500) in purchasing the most affordable mechanical keyboard using your Visa card and mark the product as unavailable post-purchase."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "James", "last_name": "Martin", "user_id": "william_clark_1500"}),
        Action(name="SearchProductsByFilter", kwargs={
            "category": "mechanical keyboard",
            "price_flag": "cheapest",
            "limit": 1
        }),
        Action(name="GetProductInfo", kwargs={"item_id": "3616838507"}),
        Action(name="ValidateOrderItems", kwargs={
            "item_list": [
                {"item_id": "3616838507", "quantity": 1}
            ],
        }),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "william_clark_1500"}),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "william_clark_1500",
            "item_list": [{"item_id": "3616838507", "quantity": 1}],
            "payment_methods_source": ["credit_card_7083997"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "william_clark_1500", "payment_method_source": "credit_card_7083997", "amount": 244.2}),
        Action(name="CreateOrder", kwargs={
            "user_id": "william_clark_1500",
            "items": [{"item_id": "3616838507", "quantity": 1}],
            "payment_method_sources": ["credit_card_7083997"],
            "tax_amount": 18.09
        }),
        Action(name="UpdateProductAvailability", kwargs={
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
        "You are Ethan Patel (ethan_patel_1311), a retail manager. You have been notified about a price increase of $5 on all variants of the wireless earbuds. Update the prices of all available variants to reflect the increase."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Noah", "last_name": "Patel", "user_id": "ethan_patel_1311"}),
        Action(name="FilterByProductIdPerProductName", kwargs={"product_names": ["wireless earbuds"]}),
        Action(name="GetItemIdsByProduct", kwargs={"product_ids": ["9924732112"],
                                                       "show_available": True,
                                                       "product_type": "wireless earbuds"}),
        Action(name="GetProductInfo", kwargs={"item_id": "9580569596"}),
        Action(name="GetProductInfo", kwargs={"item_id": "1646531091"}),
        Action(name="GetProductInfo", kwargs={"item_id": "8555936349"}),
        Action(name="GetProductInfo", kwargs={"item_id": "6077640618"}),
        Action(name="GetProductInfo", kwargs={"item_id": "4063058357"}),
        Action(name="GetProductInfo", kwargs={"item_id": "6452271382"}),
        Action(name="GetProductInfo", kwargs={"item_id": "2052249669"}),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "9580569596",
            "new_price": 262.38
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "1646531091",
            "new_price": 237.49
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "8555936349",
            "new_price": 231.49
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "6077640618",
            "new_price": 247.92
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "4063058357",
            "new_price": 248.34
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "9924732112",
            "item_id": "6452271382",
            "new_price": 263.84
        }),
        Action(name="UpdateProductAvailability", kwargs={
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
        "You're a customer service rep assisting Aarav Simpson (user_id: aarav_simpson_7344). Cancel his pending order and make the product items in that order available again."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Aarav", "last_name": "Nguyen", "user_id": "aarav_simpson_7344"}),
        Action(name="GetUserOrderHistory", kwargs={"user_id": "aarav_simpson_7344"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W7728728"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W2443586"}),
        Action(name="CancelOrder", kwargs={
            "user_id": "aarav_simpson_7344",
            "order_id": "#W2443586",
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "1656367028",
            "item_id": "9690244451",
            "available": True
        }),
        Action(name="UpdateProductAvailability", kwargs={
            "product_id": "7363354090",
            "item_id": "1437889264",
            "available": True
        }),
        Action(name="UpdateProductAvailability", kwargs={
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
        "You are a Customer Service Representative tasked with updating the billing profiles of four customers by adding their preferred payment methods: insert a Visa card ending in 4821 to Ethan Patel's (ethan_patel_1311) account, a Mastercard ending in 7395 to Daiki Lopez's (daiki_lopez_2422) account, a PayPal account with the email sofia.payments@example.com to Sofia Hernandez's (sofia_hernandez_5364) account, and a Visa card ending in 1198 to Fatima Li's (fatima_li_8519) account. Also verify all changes."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Noah", "last_name": "Patel", "user_id": "ethan_patel_1311"}),
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Daiki", "last_name": "Sanchez", "user_id": "daiki_lopez_2422"}),
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Sofia", "last_name": "Hernandez", "user_id": "sofia_hernandez_5364"}),
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Fatima", "last_name": "Li", "user_id": "fatima_li_8519"}),
        Action(name="AddPaymentMethod", kwargs={
            "user_id": "ethan_patel_1311",
            "payment_type": "credit_card",
            "payment_details": {
                "brand": "visa",
                "last_four": "4821",
            },
        }),

        Action(name="AddPaymentMethod", kwargs={
            "user_id": "daiki_lopez_2422",
            "payment_type": "credit_card",
            "payment_details": {
                "brand": "mastercard",
                "last_four": "7395",
            },
        }),

        Action(name="AddPaymentMethod", kwargs={
            "user_id": "sofia_hernandez_5364",
            "payment_type": "paypal",
            "payment_details": {
                "email": "sofia.payments@example.com",
            },
        }),

        Action(name="AddPaymentMethod", kwargs={
            "user_id": "fatima_li_8519",
            "payment_type": "credit_card",
            "payment_details": {
                "brand": "visa",
                "last_four": "1198",
            },
        }),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "ethan_patel_1311"}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "daiki_lopez_2422"}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "sofia_hernandez_5364"}),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "fatima_li_8519"}),
    ],
    outputs=[]
),

Task(
    annotator="0",
    user_id="V5TSK_USR_105",
    instruction=(
        "You are Aarav Ito (user_id: aarav_ito_1827). Adjust your address details to 994 Hickory Lane, Apt 5B, Phoenix, AZ 80224, USA, and acquire the most affordable water bottle using your gift card."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Aarav", "last_name": "Ito", "user_id": "aarav_ito_1827"}),
        Action(name="UpdateUserProfile", kwargs={
            "user_id": "aarav_ito_1827",
            "profile_updates": {
                "address": {
                    "address1": "994 Hickory Lane",
                    "address2": "Apt 5B",
                    "city": "Phoenix",
                    "state": "AZ",
                    "zip": "80224",
                    "country": "USA"
                }
            }
        }),
        Action(name="VerifyGiftCardBalance", kwargs={"first_name": "Aarav", "last_name": "Ito", "user_id": "aarav_ito_1827"}),
        Action(name="SearchProductsByFilter", kwargs={
            "category": "water bottle",
            "price_flag": "cheapest",
            "limit": 1
        }),
        Action(name="GetProductInfo", kwargs={"item_id": "5758737025"}),
        Action(name="ValidateOrderItems", kwargs={
            "item_list": [
                {"item_id": "5758737025", "quantity": 1}
            ],
        }),
        Action(name="CheckUserPaymentMethods", kwargs={"user_id": "aarav_ito_1827"}),
        Action(name="GenerateOrderSummary", kwargs={
            "user_id": "aarav_ito_1827",
            "item_list": [{"item_id": "5758737025", "quantity": 1}],
            "payment_methods_source": ["gift_card_1468632"]
        }),
        Action(name="ProcessPayment", kwargs={"user_id": "aarav_ito_1827", "payment_method_source": "gift_card_1468632", "amount": 48.7}),
        Action(name="CreateOrder", kwargs={
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
        "You are a customer service representative assisting Aarav Simpson (user_id: aarav_simpson_7344). He intends to return items from his delivered order # W7728728 is marked for return due to damage and wrong color. Process the return and update the order status accordingly."
    ),
    actions=[
        Action(name="ValidateUserIdentity", kwargs={"first_name": "Aarav", "last_name": "Nguyen", "user_id": "aarav_simpson_7344"}),
        Action(name="GetUserOrderHistory", kwargs={"user_id": "aarav_simpson_7344"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W7728728"}),
        Action(name="CheckOrderStatus", kwargs={"order_id": "#W2443586"}),
        Action(name="GetPurchasedItems", kwargs={"user_id": "aarav_simpson_7344", "order_id": "#W7728728"}),
        Action(name="GetCourier", kwargs={"tracking_id": "848032489512"}),
        Action(name="RequestOrderReturn", kwargs={
            "user_id": "aarav_simpson_7344",
            "order_id": "#W7728728",
            "return_items": [
                {"item_id": "8555936349", "quantity": 1},
                {"item_id": "1437889264", "quantity": 1}
            ],
            "return_reason": "damage and wrong color"
        }),
        Action(name="UpdateOrderStatus", kwargs={"order_id": "#W7728728", "new_status": "for return"}),
    ],
    outputs=[]
)
]