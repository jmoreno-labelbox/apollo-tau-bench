from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction="Acting as a customer service representative, assist the customer Olivia Johnson, located in zip code 10192. Assist her in placing a new order for 2 laptops: one with a 15-inch screen and an i9 processor, and the other featuring a 13-inch screen with an i7 processor in black, along with the most affordable smartphone available. Ensure that her PayPal payment method is utilized. [System IDs: user_id=olivia_johnson_8564; item_ids=5339029584; payment_method_id=paypal_6228291]. Key entities: Laptop, Smartphone, Smith, Emma.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Emma', 'last_name': 'Smith', 'zip': '10192'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smartphone'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_johnson_8564'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'olivia_johnson_8564', 'item_ids': ['5339029584', '2913673670', '1657832319'], 'payment_method_id': 'paypal_6228291'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_002",
        instruction="As a warehouse manager, William Andersson (user ID william_andersson_2031, zip 28260), coordinate a supply order for 40 units of T-shirts (black, size XXL, cotton, crew neck) from supplier # SUP0001 is priced at $25 each. Use your gift card to buy one t-shirt for yourself. [System IDs: item_id=3799046073; payment_method_id=gift_card_9136273]. Key entities: T-Shirt, 25.0, 34.73.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'T-Shirt'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'products': '9523456873'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '3799046073', 'quantity': 40, 'unit_cost': 25.0},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {"3799046073": 7}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'william_andersson_2031'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'william_andersson_2031', 'item_ids': ['3799046073'], 'payment_method_id': 'gift_card_9136273'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'william_andersson_2031'}, 'update_params': {"payment_methods":{"gift_card_9136273":{'balance': 88-53.27}}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_003",
        instruction="You are a customer service rep. A customer Ahmad Russo with zip 19122 received their order # W2378156 intends to swap the mechanical keyboard for the cheapest option featuring clicky switches and replace the smart thermostat with one that works with Google Home instead of Apple HomeKit. [System IDs: item_ids=1151293680; new_item_ids=2299424241; payment_method_id=credit_card_9513926]. Key entities: Ahmad, Rossi, Yusuf.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Rossi', 'zip': '19122'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2378156'}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '1656367028'}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '4896585277'}},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W2378156', 'item_ids': ['1151293680', '4983901480'], 'new_item_ids': ['2299424241', '7747408585'], 'payment_method_id': 'credit_card_9513926'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_004",
        instruction="You are Ahmad Russo from zip 19122. You intend to return the cleaner, headphone, and smart watch from a previous order.",
        actions=[
            # Retrieve the user identifier.
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Rossi', 'zip': '19122'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={
                    'database_name': 'users',
                    'filter_params': {'user_id': 'ahmad_russo_9620'},
                    'required_fields': ['orders', "payment_methods"]},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': ["#W6247578","#W9711842","#W4776164","#W6679257","#W2378156"]}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W2378156', 'item_ids': ['4602305039', '4202497723', '9408160950'], 'payment_method_id': 'credit_card_9513926'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_005",
        instruction="You are responsible for managing inventory. Change the status of all incomplete supply orders from supplier # Change SUP0002 status to 'fulfilled' and retrieve the product names associated with the delivery. Also, check for any unfulfilled orders that include items from these supply orders and create a delivery tracking record using International Speed Services' standard delivery method.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', "status": "pending"}, 'required_fields': ['supply_order_id', 'product_id', 'item_id']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', "status": "pending"}, 'update_params': {"status": "fulfilled"}},
            ),
            # retrieve item names from procurement orders
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': ['6858788497', '2892623495']}, 'required_fields': ['name']},
            ),
            # retrieve courier identification for International Speed Services
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'Global Express Couriers'}, 'required_fields': ['courier_id']},
            ),
            # locate orders that include these products
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'items': [{"item_id": "7579176349"},{"item_id": "9007697085"}], 'status': 'pending'}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W1258841', 'item_ids': ['7579176349', '3232433601', '5209958006'], 'courier_id': "#COU0010", 'delivery_option': 'standard'},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W1348609', 'item_ids': ['5606522780', '9007697085', '6313971174', '7195021808'], 'courier_id': "#COU0010", 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_006",
        instruction="You work as a customer support representative. Customer Omar Lopez (user_id: omar_lopez_3107), located in zip code 90339, wishes to add a new gift card (gift_card_3107) with a $100 balance as a payment method to his account. Subsequently, assist him in returning the air purifier (item_ids: 9375701158) from the recent order #W7273336 (order_id: # W7273336 (order_id: #W7273336). Ensure the refund is processed to the updated gift card (payment_method_id: gift_card_3107).",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Omar', 'last_name': 'Lopez', 'zip': '90339'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_lopez_3107'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={"user_id": "omar_jackson_3107", "payment_method_source": "gift_card", "balance": 100.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'omar_lopez_3107'}, 'required_fields': ['order_id', 'items']}
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W7273336', 'item_ids': ['9375701158'], 'payment_method_id': 'gift_card_3107'},
            ),
            # Refresh the user's gift card balance.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_jackson_3107'}, 'update_params': {"payment_methods":{"gift_card_3107":{'balance': 100+489.5}}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_007",
        instruction="As a product manager, identify which items from Digital Paradise Distributors are no longer available. Locate any pending orders for these discontinued items and initiate a return process using the original payment method.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Digital Paradise Distributors'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'items':{'item_id': ['1631373418', "6195938807", "2499294441", "8759627937", "8964750292"]}, "status": "pending"}, 'required_fields': ['order_id', 'items', "payment_history"]},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W5432440", 'item_ids': ['1631373418'], 'payment_method_id': 'gift_card_4129829'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W7398274", 'item_ids': ['1631373418'], 'payment_method_id': 'paypal_7732922'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W8268544", 'item_ids': ['1631373418'], 'payment_method_id': 'gift_card_1402922'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W6940125", 'item_ids': ['6195938807'], 'payment_method_id': 'paypal_9379149'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W3618959", 'item_ids': ['6195938807'], 'payment_method_id': 'gift_card_9246707'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W2624389", 'item_ids': ['6195938807'], 'payment_method_id': 'credit_card_5809636'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W6599568", 'item_ids': ['2499294441'], 'payment_method_id': 'gift_card_3242199'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W7390432", 'item_ids': ['2499294441'], 'payment_method_id': 'paypal_1249653'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W7342738", 'item_ids': ['2499294441'], 'payment_method_id': 'gift_card_3491931'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': "#W9722559", 'item_ids': ['8964750292'], 'payment_method_id': 'paypal_8963303'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_008",
        instruction="Acting as Mei Kovacs (zip code: 28236), you wish to exchange both the water bottle and the desk lamp. The water bottle should be swapped for the largest available size with the same color maintained, while the desk lamp should be exchanged for one with low brightness that is battery powered. Any price differences should be settled using the payment method from the initial purchase.",
        actions=[
            # Retrieve user identification.
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Mei', 'last_name': 'Kovacs', 'zip': '28236'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mei_kovacs_8020'}, 'required_fields': ['order_id','items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Water Bottle', 'Desk Lamp']}, 'required_fields': ['name', 'variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={
                    'order_id': '#W6390527',
                    'item_ids': ['8538875209', '8384507844'],
                    'new_item_ids': ['7661609223', '7453605304'],
                    'payment_method_id': 'paypal_7644869'
                },
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_009",
        instruction="You are emma_martinez_4516 (emma.martinez2723@example.com). Suppose you wish to return all items purchased. You possess two payment methods (paypal_9497703 and credit_card_3124723) and two orders (#W5490111 and # Verify your account information and order history to ensure all items and associated costs are accurate before processing refunds for W5490111 and #W7387996 to the respective alternate payment methods."
        actions=[
            # Retrieve user identification number.
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'mia.garcia2723@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': ['#W5490111', '#W7387996']}, 'required_fields': ['order_id', 'items', 'payment_history', 'status', 'timestamp']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5490111'}, 'required_fields': ['items', 'fulfilments']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W7387996'}, 'required_fields': ['items', 'fulfilments']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W5490111', 'item_ids': ['4579334072', '1421289881', '6117189161','4947717507'], 'payment_method_id': 'paypal_9497703'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W7387996', 'item_ids': ['5796612084'], 'payment_method_id': 'credit_card_3124723'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['payment_methods']},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_010",
        instruction="Your role is a customer service supervisor. You are assisting a customer with the email mei.patel3193@example.com who desires to place a substantial order for 10 mechanical keyboards (full size, clicky with a white backlight) and 5 smart thermostats (black, compatible with Google Assistant). She plans to cover the purchase using a new gift card with a $14000 balance. Subsequently, assist her by generating tracking for 'expedited' shipping for the order, utilizing SpeedWay Delivery.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'mei.patel3193@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mei_patel_7272'}, 'required_fields': ['payment_methods', 'address', 'membership_tier']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'mei_patel_7272', 'payment_method_source': 'gift_card', "balance":14000},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Mechanical Keyboard'}, 'required_fields': ['variants', 'availability', 'product_id']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smart Thermostat'}, 'required_fields': ['variants', 'availability', 'product_id']},
            ),
            Action(
                name="CreateBulkOrder",
                kwargs={'user_id': 'mei_patel_7272', 'item_ids': {'6342039236': 10, '7747408585': 5}, 'payment_method_id': 'gift_card_7272'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['6342039236', '7747408585'], 'courier_id': '#COU0001', 'delivery_option': 'expedited'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_011",
        instruction="As a supply chain analyst, handle the review of all suppliers that deliver laptops, specifically the product name 'Laptop'. Confirm their present stock quantities of laptop products and arrange supply orders to procure the entire stock for any laptop item with less than 20 units available (disregard items out of stock or discontinued) at a rate of $800 per unit. Ensure that supply orders are made only if the item is a laptop. Subsequently, mark those items as out of stock in the supplier database. Additionally, evaluate the supplier contact details and confirm that the supply order creation was accomplished successfully.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['product_id', 'supplier_id', "variants"]},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {"supplier_id": "#SUP0002"}, 'required_fields': ['item_stock', 'name', 'contact_info']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '1657832319', 'quantity': 8, 'unit_cost': 800.0},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '9844888101', 'quantity': 3, 'unit_cost': 800.0},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '4241599783', 'quantity': 1, 'unit_cost': 800.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', 'status': 'pending'}, 'required_fields': ['supply_order_id', 'item_id', 'quantity', 'total_cost']},
            ),
            Action(
                name="UpdateDb",
                kwargs = {"database_name":"suppliers", "filter_params":{"supplier_id":"#SUP0002"}, "update_params":{"item_stock":{"1657832319": "out_of_stock","9844888101": "out_of_stock","4241599783": "out_of_stock"}}}
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {"supplier_id": "#SUP0002"}, 'required_fields': ['item_stock']},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_012",
        instruction="As Fatima Williams with zip number 78712, coordinate the amendment of the pending order for hiking boots by changing the size to 8, maintaining the same material, while being indifferent to waterproof features. Utilize the existing payment method for the alteration. Furthermore, establish tracking for the new item with a standard delivery by using courier #COU0002. [System IDs: order_id=# COU0002. [System Identifiers: order_id=#W5199551; item_ids=1615379700; new_item_ids=3613716226; payment_method_id=paypal_5364164]. Important entities: Johnson, fatima_johnson_7581, Hiking."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Johnson', 'zip': '78712'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'fatima_johnson_7581', 'status': 'pending'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={"database_name":"products", "filter_params":{"name":"Hiking Boots"}, "required_fields":['variants']}
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={"order_id":"#W5199551","item_ids":["1615379700"], "new_item_ids":["3613716226"], "payment_method_id":"paypal_5364164"}
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W5199551', 'item_ids': ['3613716226'], 'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_013",
        instruction="Assist customer Daiki Muller, residing in zip code 94157, who wishes to update the delivery address for her pending order that includes a dumbell set. The new address is 842 Oak Street, Suite 205, Fort Wayne, IN 46202. Additionally, establish tracking for this order using standard shipping via SpeedWay Delivery and set the order status to 'processed'.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Daiki', 'last_name': 'Muller', 'zip': '94157'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'daiki_muller_8062'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6790887'}, 'update_params': {'address': {'address1': '842 Oak Street', 'address2': 'Suite 205', 'city': 'Indianapolis', 'state': 'IN', 'zip': '46202'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W6790887', 'item_ids': ['6585768447', '2052249669'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6790887'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_014",
        instruction="As an account manager, handle the request from customer Chen Silva (user_id: chen_silva_7250692) with the email chen.silva2698@example.com to alter their profile name from 'Chen Silva' to 'Chen Roberts' and to introduce a new credit card payment method (payment_method_id: credit_card_1565124, a visa card ending in 2534). Furthermore, they wish to increment their gift card balance (gift_card_id: gift_card_7250692) by $200 using their existing mastercard credit card. Begin by verifying current account details and confirming all payment methods. Key entities: chen_silva_7485, 200.0.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'chen.silva2698@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['name', 'payment_methods', 'address']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'update_params': {'name': {'first_name': 'Chen', 'last_name': 'Roberts'}}},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'chen_silva_7485', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2534'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'chen_silva_7485', 'gift_card_id': 'gift_card_7250692', 'payment_method_id': 'credit_card_1565124', 'amount': 200.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['name', 'payment_methods']},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_015",
        instruction="As a customer service representative, handle a return request from customer Raleigh Simpson, residing in zip code 78786, because of compatibility issues with her bluetooth speaker. Facilitate the return using her original payment method and arrange a new purchase for headphones (on-ear, red, wireless) with the same payment method. Ensure the customer's information is verified and generate a tracking number (with standard delivery and using courier ID # COU0004) for the new order."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ava', 'last_name': 'Nguyen', 'zip': '78786'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'charlotte_simpson_2175'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'charlotte_simpson_2175'}, 'required_fields': ['payment_history', 'items', 'order_id']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3779151', 'item_ids': ['2635605237'], 'payment_method_id': 'paypal_6262583'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Headphones'}, 'required_fields': ['variants', 'availability', 'price']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'charlotte_simpson_2175', 'item_ids': ['3104857380'], 'payment_method_id': 'paypal_6262583'},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['3104857380'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_016",
        instruction="As a warehouse supervisor, coordinate the creation of a new supply order for 75 units of electric kettles (2L, glass, white) priced at $95 each. Following this, amend the payment history for Raleigh Moore's (zip 85032) order of the same model of electric kettle to indicate a 'partial refund' of $150 issued to her PayPal owing to the delivery delay. [System IDs: supplier_id=# SUP0009; identifier=4064702754]."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Kettle'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '4064702754', 'quantity': 75, 'unit_cost': 95.0},
            ),
            # Modify the inventory of the supplier's items.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'4064702754': 40}}},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ava', 'last_name': 'Moore', 'zip': '85032'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'charlotte_moore_4814'}, 'required_fields': ['items', 'order_id', 'payment_history']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8495163'}, 'update_params': {'payment_history': {'transaction_type': 'partial_refund', 'amount': 150.0, 'payment_method_id': 'paypal_7478252'}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_017",
        instruction="As a customer support specialist, assist customer James Jackson in zip 28221 with exchanging his cycling helmet for the most affordable gaming mouse available. Ensure to aid him in adding a new PayPal payment method to his account for future transactions. [System IDs: order_id=# W9892169; item_ids=6401214406; new_item_ids=2880340443; payment_method_id=credit_card_2327218; user_id=james_jackson_8519]. Important entities: Gaming, Lopez, Mason."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Mason', 'last_name': 'Lopez', 'zip': '28221'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'james_jackson_8519'}, 'required_fields': ['orders']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'james_jackson_8519'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Gaming Mouse'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W9892169', 'item_ids': ['6401214406'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'credit_card_2327218'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'james_jackson_8519', 'payment_method_source': 'paypal'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_018",
        instruction="As a customer service representative, support customer Sofia Li, with the email sofia.li5731@example.com, in adding $750 to her current gift card using an alternate payment method. Also, facilitate her order for a yoga mat (4mm, PVC, blue) and a portable charger (20000mAh, black, wireless), utilizing the gift card as payment. [System IDs: user_id=sofia_li_8235; gift_card_id=gift_card_3242199; payment_method_id=credit_card_8296913; item_ids=5586947715]. Key entities: Yoga, 750.0, Portable.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'sofia.li5731@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_8235'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'sofia_li_8235', 'gift_card_id': 'gift_card_3242199', 'payment_method_id': 'credit_card_8296913', 'amount': 750.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Portable Charger']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'sofia_li_8235', 'item_ids': ['5586947715', '8349903180'], 'payment_method_id': 'gift_card_3242199'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_019",
        instruction="As a customer account manager, assist customer Olivia Ito from zip 19022 in updating her name to 'Isabella Ito-Martinez' and in returning the coffee maker from her recent order, issuing the refund to her original payment method. [System IDs: order_id=# W3780282; item_ids=9862136885; payment_method_id=credit_card_8058445."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Emma', 'last_name': 'Ito', 'zip': '19022'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_ito_4529'}, 'required_fields': ['name', 'orders', 'payment_methods']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_ito_4529'}, 'update_params': {'name': {'first_name': 'Emma', 'last_name': 'Ito-Martinez'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'olivia_ito_4529'}, 'required_fields': ['order_id', 'items', 'payment_history', 'timestamp']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3780282', 'item_ids': ['9862136885'], 'payment_method_id': 'credit_card_8058445'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_020",
        instruction="As a fulfillment specialist, assist customer Mason Lee whose email is mason.lee9297@example.com in changing the delivery address of his pending order #W2624389 to a business address: 456 Corporate Blvd, Suite 200, San Francisco, NV 94105. Additionally, initiate tracking for this order using business class with delivery service # W2624389 should be sent to the business address: 456 Corporate Blvd, Suite 200, San Francisco, NV 94105. Furthermore, start tracking this order with business class using delivery service #COU0001 and change the status to 'processed'."
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'mason.lee9297@example.com'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'update_params': {'address': {'address1': '456 Corporate Blvd', 'address2': 'Suite 200', 'city': 'San Francisco', 'state': 'NV', 'zip': '94105'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'required_fields': ['items']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W2624389', 'item_ids': ['5930656038', '6195938807', '9314474252'], 'courier_id': '#COU0001', 'delivery_option': 'business'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_021",
        instruction="As a warehouse manager, arrange a new order for 100 units of the wireless earbuds with IPX4 water resistance that are currently unavailable, priced at $85 each. Additionally, Customer Raleigh Clark from zip code 20236 seeks to include a new credit card payment option to her account (mastercard, ending in 5678). [System IDs: supplier_id=# SUP0004; item_id=3694871183; user_id=ava_martin_2430]. Main components: Wireless, 85.0, Martin."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wireless Earbuds'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '3694871183', 'quantity': 100, 'unit_cost': 85.0},
            ),
            # Revise the inventory of the supplier's products.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'update_params': {'item_stock': {'3694871183': 17}}},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ava', 'last_name': 'Martin', 'zip': '20236'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ava_martin_2430', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '5678'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_022",
        instruction="In your role as a customer service agent, assist customer Yusuf Khan (user_id: yusuf_khan_7091) at email yusuf.khan7390@example.com in swapping his laptop (item 2216662955) for the most affordable e-reader offered (item 7609274509) in order #W1787190. Use his PayPal payment method (paypal_5796936). He also desires to add a gift card with a $150 balance to his account. [System IDs: order_id=# W1787190. Utilize his PayPal account (paypal_5796936) for payment. He wishes to include a gift card with a $150 balance in his account. [System IDs: order_id=#W1787190; product_id]. Key entities: 150.0, E-Reader. Ref: gift_card."
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'yusuf.khan7390@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'E-Reader'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W1787190', 'item_ids': ['2216662955'], 'new_item_ids': ['7609274509'], 'payment_method_id': 'paypal_5796936'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'yusuf_khan_7091', 'payment_method_source': 'gift_card', 'balance': 150.0},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_023",
        instruction="As a returns coordinator, assist customer Amelia Kim (user_id: amelia_kim_4019778) from zip 28230 in sending back the Mechanical Keyboard (item_ids: 1421289881) from order # W7634667, issue the refund to her gift card (payment_method_id: gift_card_4019778) and create a new order for size 8 running shoes using her PayPal as the payment method. [System IDs: user_id=amelia_kim_4338; item_ids=4153505238; payment_method_id=paypal_1742092]. Important entities: Running."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Amelia', 'last_name': 'Kim', 'zip': '28230'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'amelia_kim_4338'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W7634667'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W7634667', 'item_ids': ['1421289881'], 'payment_method_id': 'gift_card_4019778'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'amelia_kim_4338', 'item_ids': ['4153505238'], 'payment_method_id': 'paypal_1742092'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_024",
        instruction="Working as an order specialist, update the payment history for order # W6679257 indicates a $200 partial refund was issued to the original credit card (credit_card_9513926). Furthermore, customer Harper Silva (user_id: harper_silva_8534) from zip 92188 requests a name change to 'Harper Silva-Johnson'. Key entities: partial_refund, 200.0."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6679257'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6679257'}, 'update_params': {'payment_history': {'transaction_type': 'partial_refund', 'amount': 200.0, 'payment_method_id': 'credit_card_9513926'}}},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Harper', 'last_name': 'Silva', 'zip': '92188'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'harper_silva_8534'}, 'update_params': {'name': {'first_name': 'Harper', 'last_name': 'Silva-Johnson'}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_025",
        instruction="As a supply chain coordinator, arrange a supply order for 40 units of 1080p, waterproof, black, action cameras from their supplier at $320 per unit. Next, set up tracking to manage the return of the cancelled order # W9711842 should utilize standard postage and AgileTransport Services, and confirm that the status is marked as 'returned'."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Action Camera'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '5925362855', 'quantity': 40, 'unit_cost': 320.0},
            ),
            # Revise the inventory count for the supplier's items.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'5925362855': 2}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9711842'}, 'required_fields': ['items']},
            ),
            # Retrieve courier details
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'AgileTransport Services'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W9711842', 'item_ids': ['4245201809'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9711842'}, 'update_params': {'status': 'returned'}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_026",
        instruction="In your role as a customer support representative, assist customer Ella Kovacs, who can be reached at email ella.kovacs5369@example.com, in changing the delivery address for all pending orders to: 456 New Street, Apt 12B, Houston, NM, 78701. Additionally, include a new gift card with a $300 balance in her account.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'ella.kovacs5369@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ella_kovacs_6742'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ella_kovacs_6742'}, 'required_fields': ['order_id', 'status', 'items', 'address']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ella_kovacs_6742', 'status': 'pending'}, 'update_params': {'address': {'address1': '456 New Street', 'address2': 'Apt 12B', 'city': 'Houston', 'state': 'NM', 'zip': '78701'}}},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ella_kovacs_6742', 'payment_method_source': 'gift_card', 'balance': 300},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_027",
        instruction="As a customer service expert, assist customer Ahmad Khan (user_id: ahmad_khan_7091) from zip code 75313 in adding a gift card (gift_card_7091) with a $2000 balance to his account for future transactions. Additionally, he intends to place a new order for a smartphone (product_id, item_ids: 128GB, black, 4GB RAM) and use that gift card (payment_method_id: gift_card_7091) as the payment method. [System IDs: item_ids=5339029584]. Key entities: Yusuf, 2000.0, Smartphone.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Khan', 'zip': '75313'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ahmad_khan_7091'}, 'required_fields': ['orders', 'payment_methods', 'address', 'email']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ahmad_khan_7091', 'payment_method_source': 'gift_card', 'balance': 2000.0},
            ),
            # Operation(
            # identifier="RetrieveDataFromDatabase",
            # kwargs={'db_name': 'orders', 'filters': {'user_id': 'ahmad_khan_7091'}, 'fields_needed': ['order_id', 'items', 'status']},
            # ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smartphone'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ahmad_khan_7091', 'item_ids': ['5339029584'], 'payment_method_id': 'gift_card_7091'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_028",
        instruction="Coordinate a new supply order for 4 units of garden hoses from supplier '#SUP0008' at $65 each and decrease the supplier's inventory. Additionally, assist customer Ella Campbell from zip code 19186 who wishes to return her smart watch from a previous purchase. (Ref:Gonzalez)",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Garden Hose'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '9829827210', 'quantity': 4, 'unit_cost': 65.0},
            ),
            # Revise the inventory levels of the supplier's products.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'update_params': {'item_stock':{"9829827210": 1}}},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Evelyn', 'last_name': 'Gonzalez', 'zip': '19186'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ella_campbell_8876'}, 'required_fields': ['orders']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ella_campbell_8876'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W1508165', 'item_ids': ['2554056026'], 'payment_method_id': 'paypal_4191414'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_029",
        instruction="Assist customer Lei Patel, with the email lei.patel2400@example.com, in updating her name to 'Lei Patel-Chen' and ensure that a new order for a fleece jacket is placed using her credit card as the method of payment. [System IDs: user_id=lei_patel_3139; item_ids=5992316252; payment_method_id=credit_card_4589919]. Key entities: Fleece. Use lei.patel2400@example.com.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'lei.patel2400@example.com'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lei_patel_3139'}, 'update_params': {'name': {'first_name': 'Lei', 'last_name': 'Patel-Chen'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Fleece Jacket'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lei_patel_3139'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'lei_patel_3139', 'item_ids': ['5992316252'], 'payment_method_id': 'credit_card_4589919'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_030",
        instruction="As a customer account manager, update the payment history pertaining to order # Apply a $75 'loyalty_refund' to Ahmad Russo's initial payment, W4776164. Assist Luna Kovacs, zip code 94145, in changing her delivery address for the pending order to: 789 Harbor Street, Suite 4, Boston, MA, 02101. Update her user profile to include the new address. (Ref:75.0)"
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W4776164'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W4776164'}, 'update_params': {'payment_history': {'transaction_type': 'loyalty_refund', 'amount': 75.0, 'payment_method_id': 'credit_card_9513926'}}},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Harper', 'last_name': 'Kovacs', 'zip': '94145'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'luna_kovacs_7861'}, 'required_fields': ['orders']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'luna_kovacs_7861', 'status': 'pending'}, 'update_params': {'address': {'address1': '789 Harbor Street', 'address2': 'Suite 4', 'city': 'Boston', 'state': 'MA', 'zip': '02101'}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'luna_kovacs_7861'}, 'update_params': {'address': {'address1': '789 Harbor Street', 'address2': 'Suite 4', 'city': 'Boston', 'state': 'MA', 'zip': '02101'}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_031",
        instruction="As a warehouse supervisor, handle the creation of a supply order for 180 units of wall clocks from supplier '#SUP0011' at $55 per unit. Following this, generate tracking for the order #W8665881 ('standard' delivery using courier '# W8665881 ('standard' delivery via courier '#COU0001') and change the status to 'processed'. (Ref:55.0)"
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wall Clock'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '9850781806', 'quantity': 180, 'unit_cost': 55.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8665881'}, 'required_fields': ['items']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W8665881', 'item_ids': ['5855700373', '9408160950', '4422467033', '1157853815', '8725040869'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8665881'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_032",
        instruction="Acting as a customer service agent, assist Aarav White (user_id: aarav_white_8794), who is associated with the email aarav.white9752@example.com, with returning his Sneakers (item_ids: 9727387530) from order # W5866402, and include a new credit card (Visa, last four digits 1955, payment_method_id: credit_card_8794) for payment on the account. Process a refund to paypal_8049766. Email: aarav.white9752@example.com."
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'aarav.white9752@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5866402'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'payment_method_id': 'paypal_8049766'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'aarav_white_8794', 'payment_method_source': 'credit_card', 'last_four': '1955', 'brand': 'visa'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_033",
        instruction="Assist customer Amelia Lopez from zip 85093 in exchanging her bluetooth speaker (from order # W4277243) for a wristwatch and the addition of a $250 gift card to her account. [System IDs: item_ids=2635605237; new_item_ids=2407258246; payment_method_id=paypal_8516781; user_id=amelia_lopez_2068]. Key entities: 250.0, Sanchez, Wristwatch, Isabella. [isabella_sanchez]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Sanchez', 'zip': '85093'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'amelia_lopez_2068'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wristwatch'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W4277243', 'item_ids': ['2635605237'], 'new_item_ids': ['2407258246'], 'payment_method_id': 'paypal_8516781'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'amelia_lopez_2068', 'payment_method_source': 'gift_card', 'balance': 250.0},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_034",
        instruction="As an order coordinator, you should initiate a new supply order for 100 units of indoor security cameras from supplier '#SUP0001' at $180 per unit. Customer Raj Jackson from zip 92147 desires to change his name to 'Raj Jackson-Kumar'. Key entities: 180.0, Sanchez-Kumar, Sanchez, Indoor. Customer: mei_sanchez_2068.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Indoor Security Camera'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '8470360507', 'quantity': 100, 'unit_cost': 180.0},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_lopez_2970'}, 'update_params': {'name': {'first_name': 'Raj', 'last_name': 'Sanchez-Kumar'}}},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_035",
        instruction="As a customer support specialist, assist customer Isabella Ito, who has the email isabella.ito5204@example.com. Olivia needs to change the delivery address for order # W3657213 to 987 Elm Street, Unit 2, San Francisco, NV, USA, 94110; customer wants to return the action camera from this order due to dissatisfaction with the color. Key entities: olivia.ito5204@example.com, CA."
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'olivia.ito5204@example.com'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3657213'}, 'update_params': {'address': {'address1': '987 Elm Street', 'address2': 'Unit 2', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '94110'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3657213'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3657213', 'item_ids': ['6700049080'], 'payment_method_id': 'gift_card_7794233'},
            ),
        ],
        outputs=[]
    ),

    Task(
        annotator="0",
        user_id="task_036",
        instruction="As a fulfillment manager, update the payment history for order #W1023987 to include a $125 'promotional cashback' applied to the original payment method. Adjust the tracking for this order to utilize courier # W1023987 should include a $125 'promotional cashback' credited to the original payment method. Update the order tracking to use courier #COU0001 with 'standard' delivery and set the order status to 'processed'. Also, help the customer with this order to add $400 to their gift card, using a credit card (Visa, last four digits 2635) for the payment of this top-up. Key entities: 400.0, promotional_cashback, 125"
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'required_fields': ['payment_history','items', 'user_id', 'fulfillments']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'update_params': {'payment_history': {'transaction_type': 'promotional_cashback', 'amount': 125.0, 'payment_method_id': 'gift_card_9450778'}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'tracking', 'filter_params': {'tracking_id': '974703204371'}, 'update_params': {'delivery_carrier': '#COU0001', 'delivery_option': 'standard'}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'update_params': {'status': 'processed'}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sophia_garcia_1101'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'sophia_garcia_1101', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2635'},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'sophia_garcia_1101', 'gift_card_id': 'gift_card_9450778', 'payment_method_id': 'credit_card_1101', 'amount': 400.0},
            ),
        ],
        outputs=[]
    ),

    # Task 037: Lucas Rodriguez requests a return for wireless earbuds due to poor sound quality.
    Task(
        annotator="0",
        user_id="task_037",
        instruction="As a customer service representative, you find that customer Ivan Santos (zip 75277) reports that the wireless earbuds from his order don't fit him. You handle a return and issue a refund to a new gift card that you generate. [System IDs: user_id=lucas_rodriguez_6635; order_id=# W6893533; item_ids=1646531091; payment_method_id=gift_card_6635]. Main entities: 0.0."
        actions=[
            # Retrieve user ID using the full name and zip code.
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['items', 'order_id']},
            ),
            # issue a new gift card for the reimbursement
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'lucas_rodriguez_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Handle the return.
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6893533', 'item_ids': ['1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
        ],
        outputs=[]
    ),

    # Task 038: Anya Garcia needs to monitor her cancelled order and verify her gift card balance.
    Task(
        annotator="0",
        user_id="task_038",
        instruction=" You are assisting user Anya Garcia (user_id: mia_martinez_3271, zip 19036) who is inquiring about her cancelled order. You assist her in verifying the current balance on her gift card (gift_card_4374071) following a refund. She then decides to use her updated gift card balance (payment_method_id: gift_card_4374071) to order an LED Light Bulb (item_ids: 7445824652, 75W Equivalent, daylight, WiFi-enabled). Use zip 19036.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_martinez_3271'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'LED Light Bulb'}, 'required_fields': ['variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'mia_martinez_3271', 'item_ids': ['7445824652'], 'payment_method_id': 'gift_card_4374071'},
            )
        ],
        outputs=[]
    ),

    # Task 039: Yara Sanchez intends to swap her mechanical keyboard for an alternative switch type.
    Task(
        annotator="0",
        user_id="task_039",
        instruction="Support customer zoe_lopez_1902 in exchanging item_id 9025753381 ('Mechanical Keyboard with clicky switches') for the same model but featuring tactile switches, as she finds the clicky type too noisy for her office. Facilitate her request to use a gift card for the transaction, ensuring she has one, and if not, provide her with one. [System IDs: required_fields=order_id; required_fields=variants; required_fields=payment_methods; order_id=# W6015009; new_item_ids=3616838507; payment_method_id=gift_card_1902."
        actions=[
            # Identify the order and item for the exchange.
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'zoe_lopez_1902', 'items':{'item_id': '9025753381'}}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '1656367028'}, 'required_fields': ['variants', 'name']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'zoe_lopez_1902'}, 'required_fields': ['payment_methods']},
            ),
            # Verify the user's gift card status; if absent, generate a new one.
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'zoe_lopez_1902', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Handle the transaction.
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W6015009', 'item_ids': ['9025753381'], 'new_item_ids': ['3616838507'], 'payment_method_id': 'gift_card_1902'},
            ),
        ],
        outputs=[]
    ),

    # Task 004: Ivan Santos must revise his address for upcoming shipments.
    Task(
        annotator="0",
        user_id="task_040",
        instruction="Assist user Lucas Rodriguez in modifying his address from '477 Park Avenue, Suite 558, Houston, NM 75277' to '825 Main Street, Apt 12B, Houston, NM 78701'. Aid Ivan in adding a new credit card (mastercard, last four 2053) and update his pending orders to reflect the new address and payment details.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'update_params': {'address': {'address1': '825 Main Street', 'address2': 'Apt 12B', 'city': 'Houston', 'state': 'NM', 'zip': '78701', 'country': 'USA'}}},
            ),
            # Implement an additional credit card payment option.
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'lucas_rodriguez_6635', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '2053'},
            ),
            # Retrieve all outstanding orders and modify them with the updated address and payment details.
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635', 'status': 'pending'}, 'required_fields': ['order_id']},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W8770097', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W5183325', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W3913498', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635', 'status': 'pending'}, 'update_params': {'address': {'address1': '825 Main Street', 'address2': 'Apt 12B', 'city': 'Houston', 'state': 'NM', 'zip': '78701', 'country': 'USA'}}},
            ),
        ],
        outputs=[]
    ),

    # Task 041: Noah Brown intends to introduce a new payment method and submit an order.
    Task(
        annotator="0",
        user_id="task_041",
        instruction="Assist customer Ethan Wilson (zip 80279) in adding a PayPal payment method and subsequently placing an order for Running Shoes (size 10, white) using his PayPal. To ensure timely delivery, initiate tracking for the order with the 'express' delivery option, employing RapidTransit Solutions.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ethan_wilson_6181'}, 'required_fields': ['address', 'payment_methods', 'name', 'email']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ethan_wilson_6181', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ethan_wilson_6181', 'item_ids': ['1775591963'], 'payment_method_id': 'paypal_6181'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'RapidTransit Solutions'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['1775591963'], 'courier_id': '#COU0002', 'delivery_option': 'express'},
            ),
        ],
        outputs=[]
    ),

    # Task 042: Anya Garcia aims to verify product availability and inventory levels.
    Task(
        annotator="0",
        user_id="task_042",
        instruction="Assist user Mia Martinez (zip 19036), who is interested in buying a Laptop. She intends to load $3000 onto her gift card with her credit card and then verify if the balance will cover the laptop with a 17-inch screen and i9 processor. If affordable, help her by placing the order. [System IDs: required_fields=payment_methods; user_id=mia_martinez_3271; gift_card_id=gift_card_4374071; payment_method_id=credit_card_8955149; required_fields=variants; item_ids=3265035808]. Key entities: Anya, 3000.0, Garcia.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            # Verify if there is a balance on the gift card.
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_martinez_3271'}, 'required_fields': ['payment_methods']},
            ),
            # Load funds onto the gift card.
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'mia_martinez_3271', 'gift_card_id': 'gift_card_4374071', 'payment_method_id': 'credit_card_8955149', 'amount': 3000.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['variants']},
            ),
            # generate order
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'mia_martinez_3271', 'item_ids': ['3265035808'], 'payment_method_id': 'gift_card_4374071'},
            ),
        ],
        outputs=[]
    ),

    # Task 043: Yara Sanchez seeks to change a current order prior to dispatch.
    Task(
        annotator="0",
        user_id="task_043",
        instruction="Assist customer Fatima Li (zip 94180) in adding a Yoga Mat (4mm, blue, PVC) to her pending order. Ensure the item is included and adjust the payment to account for the updated total amount.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Li', 'zip': '94180'},
            ),
            # Retrieve details of outstanding orders.
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'fatima_li_8519', 'status': 'pending'}, 'required_fields': ['order_id', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Yoga Mat'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5267498'}, 'update_params': {'items': {'name': 'Yoga Mat', 'product_id':'4635925001', 'item_id': '5586947715', 'price': 92.53, 'options': {'color': 'blue', 'thickness': '4mm', 'material': 'PVC'}}}},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W5267498', 'transaction_type': 'payment', 'payment_info_to_update': {'amount': 466.75+92.53, 'payment_method_id': 'gift_card_4220746'}},
            ),
        ],
        outputs=[]
    ),

    # Task 044: Ivan Santos has reported a delivery problem and requires tracking details.
    Task(
        annotator="0",
        user_id="task_044",
        instruction="Assist user Lucas Rodriguez (zip 75277) whose order is noted as delivered but was never received, in obtaining a refund by returning all items in the order. Then, set up a new order for the same items. Generate a new gift card for Ivan to utilize for both the refund and the new order, ensuring seamless payment. Additionally, credit $100 to the gift card as an apology for the inconvenience, and monitor the gift card balance during the transactions.",
        actions=[
            # Retrieve user ID using complete name and postal code.
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            # Retrieve order details
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635', 'status': 'delivered'}, 'required_fields': ['order_id', 'items']},
            ),
            # Generate a new gift card for the reimbursement.
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'lucas_rodriguez_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Handle the return for every item in the order.
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487', '1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods']},
            ),
            # Generate a new order for identical items.
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'lucas_rodriguez_6635', 'item_ids': ['5206946487', '1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods']},
            ),
            # Increase the gift card balance by $100 as reimbursement.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id':'lucas_rodriguez_6635'}, 'update_params': {'payment_methods': { 'gift_card_6635': {'balance': 100.0} } } },
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods']},
            ),
        ],
        outputs=[]
    ),

    # Task 045: Multiple users - Noah Brown intends to present a gift to Anya Garcia.
    Task(
        annotator="0",
        user_id="task_045",
        instruction="Assist customer Ethan Wilson (zip 80279) in purchasing a Smart Thermostat (item ID 7747408585) as a gift for mia_martinez_3271. Ensure it is shipped to Anya's address while charging Noah's credit card credit_card_7815826. Additionally, generate tracking for the order using the 'next-day' delivery option with RapidTransit Solutions.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ethan_wilson_6181', 'item_ids': ['7747408585'], 'payment_method_id': 'credit_card_7815826'}
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_martinez_3271'}, 'required_fields': ['address']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {"address": {
                "address1": "615 Laurel Lane",
                "address2": "Suite 552",
                "city": "Pittsburgh",
                "country": "USA",
                "state": "OH",
                "zip": "19036"}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'RapidTransit Solutions'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['7747408585'], 'courier_id': '#COU0002', 'delivery_option': 'next-day'},
            ),
        ],
        outputs=[]
    ),

    # Task 010: Yara Sanchez intends to return several items and initiate a partial refund.
    Task(
        annotator="0",
        user_id="task_046",
        instruction="Assist user Zoe Lopez (zip 75255) with returning both the Skateboard (item_id 3877188862) and Bluetooth Speaker (item_id 7597543861) from order # W6015009. Permit her to keep the Mechanical Keyboard. Start the return procedure and confirm that the refund is processed to her initial payment method. [System IDs: required_fields=orders; required_fields=payment_history; payment_method_id=credit_card_5884162]. Key entities: Yara, Sanchez. [yara_sanchez_1902]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yara', 'last_name': 'Sanchez', 'zip': '75255'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'zoe_lopez_1902'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6015009'}, 'required_fields': ['items', 'payment_history', 'status']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6015009', 'item_ids': ['3877188862', '7597543861'], 'payment_method_id': 'credit_card_5884162'},
            ),
        ],
        outputs=[]
    ),

    # Task 011: Olivia Jackson requests to cancel her pending order and receive a complete refund.
    Task(
        annotator="0",
        user_id="task_047",
        instruction="Assist customer Isabella Thompson (zip 95119) who wishes to return the hiking boots and gaming mouse from a recent order. Execute full cancellation and refund to her original payment method. [System IDs: required_fields=order_id; required_fields=payment_history; order_id=# W3168895; item_ids=2648909398; payment_method_id=paypal_3999493]. Main entities: Olivia, Jackson."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Olivia', 'last_name': 'Jackson', 'zip': '95119'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'isabella_thompson_1219'}, 'required_fields': ['items', 'order_id']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3168895'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3168895', 'item_ids': ['2648909398', '5796612084'], 'payment_method_id': 'paypal_3999493'},
            ),
        ],
        outputs=[]
    ),

    # Task 012: Ava Nguyen requires assistance in locating her user account via email.
    Task(
        annotator="0",
        user_id="task_048",
        instruction="You are a customer service specialist. A customer named Raleigh Simpson called but misplaced her user ID. She provided the email Raleigh.simpson3664@example.com. Help her locate her user ID and update her last name to Smith. Additionally, she wants to add $1000 to her gift card balance. [System IDs: required_fields=payment_methods; user_id=charlotte_simpson_2175; gift_card_id=gift_card_3324938; payment_method_id=paypal_6262583]. Key entities: 1000.0, charlotte.simpson3664@example.com. Email: charlotte.simpson3664@example.com, amount: $1000.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'charlotte.simpson3664@example.com'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'charlotte_simpson_2175'}, 'update_params': {'name': {'first_name': 'Ava', 'last_name': 'Smith'}}},
            ),
            # verify payment options
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'charlotte_simpson_2175'}, 'required_fields': ['payment_methods']},
            ),
            # load funds onto the gift card
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'charlotte_simpson_2175', 'gift_card_id': 'gift_card_3324938', 'payment_method_id': 'paypal_6262583', 'amount': 1000.0},
            ),
        ],
        outputs=[]
    ),

    # Task 049: Sofia Li intends to swap her laptop for an alternative RAM setup.
    Task(
        annotator="0",
        user_id="task_049",
        instruction="Assist customer luna_dean_2998 who has purchased a laptop but requires additional RAM for her work. She desires to swap her existing laptop (8GB RAM) for a 32GB RAM laptop featuring a 17-inch screen, with no concern regarding other attributes. She requests that you attach her PayPal account to her profile and subsequently utilize it to credit $500 to her gift card balance. Following this, the gift card should be used to complete the laptop exchange.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'luna_dean_2998'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'luna_dean_2998'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'luna_dean_2998', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'luna_dean_2998', 'gift_card_id': 'gift_card_5328393', 'payment_method_id': 'paypal_2998', 'amount': 500.0},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W2959713', 'item_ids': ['3265035808'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'gift_card_5328393'},
            ),
        ],
        outputs=[]
    ),

    # Task 014: Emma Brown aims to include a gift card and buy several items.
    Task(
        annotator="0",
        user_id="task_050",
        instruction="Guide customer Olivia Wilson (zip 32165) who received a $500 gift card for her birthday. Assist her in adding it to her account and then proceed to purchase a coffee maker and a water bottle as gifts for her workplace. [System IDs: required_fields=payment_methods; user_id=olivia_wilson_8847; required_fields=variants; item_ids=1349017811; payment_method_id=gift_card_8847]. Key entities: Brown, Coffee, Emma, 500.0, Water.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Emma', 'last_name': 'Brown', 'zip': '32165'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_wilson_8847'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'olivia_wilson_8847', 'payment_method_source': 'gift_card', 'balance': 500.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Coffee Maker', 'Water Bottle']}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'olivia_wilson_8847', 'item_ids': ['1349017811', '5758737025'], 'payment_method_id': 'gift_card_8847'},
            ),
        ],
        outputs=[]
    ),

    # Task 015: Yusuf Khan reports a faulty smartphone and requires a replacement.
    Task(
        annotator="0",
        user_id="task_051",
        instruction="Assist customer ahmad_khan_7091 with a situation where a laptop got damaged due to moisture during delivery. Facilitate the return of the damaged item and place a new order for the same model as a replacement. [System IDs: required_fields=orders; required_fields=order_id; order_id=# W1787190; item_ids=2216662955; payment_method_id=paypal_5796936."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ahmad_khan_7091'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ahmad_khan_7091'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W1787190', 'item_ids': ['2216662955'], 'payment_method_id': 'paypal_5796936'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ahmad_khan_7091', 'item_ids': ['2216662955'], 'payment_method_id': 'paypal_5796936'},
            ),
        ],
        outputs=[]
    ),

    # Task 052: Amelia Kim intends to buy gifts to be shipped to various addresses.
    Task(
        annotator="0",
        user_id="task_052",
        instruction="Assist customer evelyn_dean_4338 in purchasing a wristwatch for her brother and a backpack for her sister. Both siblings reside in different suites within the same building. Ensure the wristwatch is sent to her brother at Suite 214 and the backpack is shipped to her sister at Suite 523, billing the charges to her paypal account.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'evelyn_dean_4338'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wristwatch'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Backpack'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'evelyn_dean_4338', 'item_ids': ['2407258246'], 'payment_method_id': 'paypal_1742092'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'evelyn_dean_4338', 'item_ids': ['9851293632'], 'payment_method_id': 'paypal_1742092'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address2': 'Suite 214'}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001002'}, 'update_params': {'address': {'address2': 'Suite 523'}}},
            ),
        ],
        outputs=[]
    ),

    # Task 017: Raj Sanchez intends to verify product availability prior to placing an order.
    Task(
        annotator="0",
        user_id="task_053",
        instruction="Assist customer Raj Jackson (zip 92147) in purchasing a desk lamp and notebook for his home office. Arrange to procure these items for him and prepare tracking for standard delivery via FleetFast Delivery.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_lopez_2970'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Desk Lamp', 'Notebook']}, 'required_fields': ['variants', 'supplier_id']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'raj_lopez_2970', 'item_ids': ['5320792178', '9799386954'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FleetFast Delivery'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5320792178', '9799386954'], 'courier_id': '#COU0006', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    # Task 054: Chen Silva requires an update to the shipping address for the outstanding order.
    Task(
        annotator="0",
        user_id="task_054",
        instruction="Support customer amelia_andersson_2152 who has placed an order with an incorrect address. The order is still pending, and you need to adjust the order address to the accurate location: 456 New Street, Apt 789, Portland, OR 97201, USA. Customer: lucas_costa_7245, zip: 19031.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'amelia_andersson_2152', 'status': 'pending'}, 'required_fields': ['order_id']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2575533'}, 'update_params': {'address': {'address1': '456 New Street', 'address2': 'Apt 789', 'city': 'Portland', 'state': 'OR', 'zip': '97201', 'country': 'USA'}}},
            ),
        ],
        outputs=[]
    ),

    # Task 019: Aarav Anderson intends to return several items and increase the balance on a gift card.
    Task(
        annotator="0",
        user_id="task_055",
        instruction="Assist customer Aarav White (zip 19031), who is seeking to return a bookshelf and water bottle from his latest purchase. Rather than processing refunds to his credit card, transfer the amounts to his gift card for upcoming buys. [System IDs: required_fields=orders; required_fields=order_id; order_id=# W3470184; item_ids=2366567022; payment_method_id=gift_card_7245904]. Important entities: Anderson, 620.88."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Aarav', 'last_name': 'Anderson', 'zip': '19031'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'aarav_white_8794'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'aarav_white_8794'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3470184', 'item_ids': ['2366567022', '1768466237'], 'payment_method_id': 'gift_card_7245904'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'aarav_white_8794'}, 'update_params': {"payment_methods": {"gift_card_7245904": {'balance': 17 + 549.84 + 54.04}}}},
            ),
        ],
        outputs=[]
    ),

    # Task 056: Isabella Sanchez intends to generate a supply order for items with low inventory.
    Task(
        annotator="0",
        user_id="task_056",
        instruction="Support inventory manager amelia_lopez_2068, who has observed that Running Shoes and Backpacks are in low stock. Aid her in generating supply orders to restock inventory from suppliers (30 units, unit cost of $50 for both shoes and backpacks), and update the supplier stock accordingly to reflect these adjustments. Further, assist her in purchasing a pair of the same running shoes for herself, delivering to her address with zip 85093.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Running Shoes','Backpack']}, 'required_fields': ['supplier_id', 'product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ["#SUP0006", "#SUP0005"]}, 'required_fields': ['supplier_id', 'item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '9791469541', 'quantity': 30, 'unit_cost': 50.0},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0005', 'item_id': '9851293632', 'quantity': 30, 'unit_cost': 50.0},
            ),
            # Refresh supplier inventory.
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0006'}, 'update_params': {'item_stock': {'9791469541': 157}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0005'}, 'update_params': {'item_stock': {'9851293632': 90}}},
            ),
            # Retrieve user ID using the complete name and postal code.
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Sanchez', 'zip': '85093'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'amelia_lopez_2068'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'amelia_lopez_2068', 'item_ids': ['9791469541'], 'payment_method_id': 'paypal_8516781'},
            ),
        ],
        outputs=[]
    ),

    # Task 057: Yara Li intends to return a faulty electric toothbrush.
    Task(
        annotator="0",
        user_id="task_057",
        instruction="Assist customer sofia_martin_1518, who mentioned her electric toothbrush ceased functioning after 2 days. You must guide her through exchanging it for the identical model. [System IDs: required_fields=orders; required_fields=order_id; required_fields=variants; order_id=# W7619352; item_ids=8798690242; payment_method_id=paypal_5334408]. [Electric]."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_martin_1518'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'sofia_martin_1518'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Toothbrush'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W7619352', 'item_ids': ['8798690242'], 'new_item_ids': ['8798690242'], 'payment_method_id': 'paypal_5334408'},
            ),
        ],
        outputs=[]
    ),

    # Task 058: Omar Lopez aims to locate his account using his name and postal code.
    Task(
        annotator="0",
        user_id="task_058",
        instruction="Assist a customer who has phoned in stating his name is Omar Jackson, resides in zip code 90339, but cannot recall his email and user ID. You will also assist him in adding a new credit card (mastercard, last four digits 6789) to his account to facilitate future purchases. Subsequently, help him verify the new card by purchasing a pair of white, size 10, leather running shoes. [System IDs: user_id=omar_jackson_3107; required_fields=variants; item_ids=1775591963; payment_method_id=credit_card_3107]. Key entities: Running, Lopez.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Omar', 'last_name': 'Lopez', 'zip': '90339'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'omar_jackson_3107', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '6789'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'omar_jackson_3107', 'item_ids': ['1775591963'], 'payment_method_id': 'credit_card_3107'},
            ),
        ],
        outputs=[]
    ),

    # Task 023: Several clients - Noah Brown intends to purchase a gift for Anya Garcia's birthday.
    Task(
        annotator="0",
        user_id="task_059",
        instruction="Assist customer Noah Anderson (zip 80279) who wishes to arrange a birthday surprise for his friend Mia Martinez (zip 19036). Facilitate Noah in purchasing a smart watch for Anya and update the shipping address to Anya's location.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ethan_wilson_6181'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_martinez_3271'}, 'required_fields': ['address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smart Watch'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ethan_wilson_6181', 'item_ids': ['2860956907'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {"address": {
                "address1": "615 Laurel Lane",
                "address2": "Suite 552",
                "city": "Pittsburgh",
                "country": "USA",
                "state": "OH",
                "zip": "19036"}}},
            ),
        ],
        outputs=[]
    ),

    # Task 060: Ivan Santos intends to switch his PayPal to a credit card for enhanced rewards.
    Task(
        annotator="0",
        user_id="task_060",
        instruction="Support customer lucas_rodriguez_6635 in adding a new credit card (visa, last four digits 0235) to his profile to enhance cashback benefits. Additionally, aid him in modifying the payment method for all outstanding orders to utilize the newly added credit card.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods', 'orders']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'lucas_rodriguez_6635', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '0235'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635', 'status': 'pending'}, 'required_fields': ['order_id', 'status', 'payment_history']},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W8770097', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W5183325', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W3913498', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
        ],
        outputs=[]
    ),

    # Task 061: Yara Sanchez aims to process returns for items from various orders in bulk.
    Task(
        annotator="0",
        user_id="task_061",
        instruction="You are assisting customer zoe_lopez_9145 who has decided to return several items purchased from different orders. Assist her in processing the return of a bluetooth speaker from one order and a bicycle from another, converting all returns to a gift card. Should she lack a gift card, ensure to create one initially. Utilize the gift card for processing these returns.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'zoe_lopez_9145'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'zoe_lopez_9145', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6519831'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9102482'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6519831', 'item_ids': ['3624655057'], 'payment_method_id': 'gift_card_9145'},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W9102482', 'item_ids': ['4716977452'], 'payment_method_id': 'gift_card_9145'},
            ),
        ],
        outputs=[]
    ),

    # Task 026: Sofia Li intends to set up monthly orders for coffee maker filters.
    Task(
        annotator="0",
        user_id="task_062",
        instruction="You are supporting customer sofia_li_9219, an enthusiast of jigsaw puzzles, who intends to purchase one of each 1000 piece jigsaw puzzle available, utilizing her PayPal account for payment. Appreciate her passion by offering a complimentary 2000 piece puzzle (id 5645314103) as a gift. Achieve this by generating a new order with her PayPal, ensuring the payment amount is set to $0. [System IDs: required_fields=payment_methods; required_fields=variants; item_ids=3112842858; payment_method_id=paypal_8194385; order_id=# W0001002]. Important entities: 0.0, Jigsaw."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_9219'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Jigsaw Puzzle'}, 'required_fields': ['variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['3112842858',  '4572024853'], 'payment_method_id': 'paypal_8194385'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['5645314103'], 'payment_method_id': 'paypal_8194385'},
            ),
            Action(
                name="UpdatePaymentHistory",
                kwargs={'order_id': '#W0001002', 'transaction_type': 'payment', 'payment_info_to_update': {'amount': 0.0}},
            ),
        ],
        outputs=[]
    ),

    # Task 027: Emma Brown reports stolen package and requests a replacement.
    Task(
        annotator="0",
        user_id="task_063",
        instruction="Assist customer olivia_wilson_8847 (Olivia Wilson, Suite 100) who cancelled an order but then realised she still needs the Hiking Boots (item: 1262139877) from that order. Facilitate placing a new order for the boots, this time shipping to her workplace address (123 Office Park, Suite 100, San Francisco, NV, USA, 94105). Utilize the original payment method (credit_card_8850930) for this new purchase.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'olivia_wilson_8847'}, 'required_fields': ['payment_history', 'items', 'status']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'olivia_wilson_8847', 'item_ids': ['1262139877'], 'payment_method_id': 'credit_card_8850930'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address1': '123 Office Park', 'address2': 'Suite 100', 'city': 'San Francisco', 'state': 'NV', 'zip': '94105', 'country': 'USA'}}},
            ),
        ],
        outputs=[]
    ),

    # Task 064: Yusuf Khan intends to buy office supplies in bulk for his company.
    Task(
        annotator="0",
        user_id="task_064",
        instruction="Assist customer ahmad_khan_2015 in purchasing bulk office supplies for his company: exactly 50 notebooks, 50 desk lamps, and 5 coffee makers. Help him add his company credit card (visa, ending 0482) to pay for the transaction. Next, arrange shipping using the 'corporate-shipping' option with Priority Shipping Co.' express delivery. [System IDs: required_fields=payment_methods; required_fields=variants; user_id=yusuf_khan_2015; payment_method_id=credit_card_2015; required_fields=courier_id; order_id=#W0001001; item_ids=9799386954; courier_id=# W0001001; item_ids=9799386954; courier_id=#COU0003]."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_2015'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Notebook', 'Desk Lamp', 'Coffee Maker']}, 'required_fields': ['variants']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'yusuf_khan_2015', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '0482'},
            ),
            Action(
                name="CreateBulkOrder",
                kwargs={'user_id': 'yusuf_khan_2015', 'item_ids': {'9799386954':50, '5320792178':50, '1349017811':5}, 'payment_method_id': 'credit_card_2015'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'Express Delivery Services'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['9799386954', '5320792178', '1349017811'], 'courier_id': '#COU0003', 'delivery_option': 'corporate-shipping'},
            ),
        ],
        outputs=[]
    ),

    # Task 065: Evelyn Dean needs to verify if the damaged item is still covered by warranty.
    Task(
        annotator="0",
        user_id="task_065",
        instruction="Assist customer Mia Garcia (user_id: mia_garcia_4516, zip 46229) who possesses a mechanical keyboard (item 1421289881) from order # Assist her in exchanging W5490111, which she no longer wants, for a gaming mouse (item 2880340443) and process the payment through her PayPal account (paypal_9497703). [System IDs: required_fields=orders; required_fields=order_id; required_fields=variants]."
        actions=[
            # retrieve user identifier
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Mia', 'last_name': 'Garcia', 'zip': '46229'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Gaming Mouse'}, 'required_fields': ['variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W5490111', 'item_ids': ['1421289881'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'paypal_9497703'},
            ),
        ],
        outputs=[]
    ),

    # Task 066: Advanced management of supplier relationships and inventory monitoring
    Task(
        annotator="0",
        user_id="task_066",
        instruction="As an inventory manager, coordinate the creation of supply orders to procure 100 units of the item with the highest stock from several suppliers (#SUP0001, #SUP0009, # Update the inventory for items SUP0001, SUP0009, and SUP0011, each valued at $10, to account for the reduction in stock after order fulfillment."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0001', '#SUP0009', '#SUP0011']}, 'required_fields': ['name', 'products', 'item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '8124970213', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '6324294385', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '8941974610', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {'8124970213': 99}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'6324294385': 100}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'8941974610': 90}}},
            ),
        ],
        outputs=[]
    ),

    # Task 067: Handling orders from multiple users with validation of payment methods.
    Task(
        annotator="0",
        user_id="task_067",
        instruction="Act as a customer service representative. Assist customer Mia Martinez from zip 19036 and Noah Anderson from zip 80279 with placing orders. Anya is interested in a yoga mat and a bluetooth speaker, while Noah is looking for running shoes and a water bottle. Process their orders, ensuring to set up tracking for standard shipping through AgileTransport Services.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': ['anya_garcia_3271', 'noah_brown_6181']}, 'required_fields': ['name','payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker', 'Running Shoes', 'Water Bottle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'credit_card_8955149'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['9791469541', '5758737025'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5586947715', '2635605237'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001002', 'item_ids': ['9791469541', '5758737025'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    # Task 068: Intricate process for returns and exchanges involving payment modifications.
    Task(
        annotator="0",
        user_id="task_068",
        instruction="Assist customer Ivan Santos from zip 75277 with his request to return a Garden Hose and exchange Wireless Earbuds for a tablet within the same delivered order. Additionally, help him generate a gift card and deposit $200 into it using his PayPal account. [System IDs: required_fields=order_id; order_id=# W6893533; item_ids=5206946487; payment_method_id=paypal_6151711; mandatory_fields=variants; item_ids=1646531091; updated_item_ids=2106335193; user_id=ivan_santos_6635."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', "status":"delivered"}, 'required_fields': ['order_id','items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Tablet'}, 'required_fields': ['variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W6893533', 'item_ids': ['1646531091'], 'new_item_ids': ['2106335193'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'ivan_santos_6635', 'gift_card_id': 'gift_card_6635', 'payment_method_id': 'paypal_6151711', 'amount': 200.0},
            ),
        ],
        outputs=[]
    ),

    # Task 069: Electronics customer order with tracking functionality.
    Task(
        annotator="0",
        user_id="task_069",
        instruction="Assist customer Noah Anderson from zip 80279 who plans to purchase a smartphone and tablet for his enterprise. His preferred payment method is his mastercard ending in 9212. Help him finalize the order and arrange tracking for standard delivery via RapidTransit Solutions. [System IDs: required_fields=payment_methods; required_fields=variants; user_id=noah_brown_6181; item_ids=5339029584; payment_method_id=credit_card_7815826; required_fields=courier_id; order_id=#W0001001; courier_id=# W0001001; courier_id=#COU0002]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'noah_brown_6181'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smartphone', 'Tablet']}, 'required_fields': ['variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['5339029584', '2106335193'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'QuickShip Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5339029584', '2106335193'], 'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    # Task 070: Management of supply orders and inventory
    Task(
        annotator="0",
        user_id="task_070",
        instruction="Support the warehouse manager in generating a supply order for 30 units of Coffee Makers (at 182.93 unit cost) from supplier Animal Care Worldwide due to low inventory. Adjust the supplier's stock levels accordingly afterward. [System IDs: required_fields=product_id; required_fields=item_stock; supplier_id=# SUP0009; item_id=1349017811."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Coffee Maker'}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '1349017811', 'quantity': 30, 'unit_cost': 182.93},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'1349017811': 6}}},
            ),
        ],
        outputs=[]
    ),

    # Task 071: Procedure for returning and exchanging products
    Task(
        annotator="0",
        user_id="task_071",
        instruction="You are assisting customer Lucas Rodriguez from zip 75277 who wishes to return his Smart Watch and trade the Skateboard from the same order for a Gaming Mouse. You handle both the return and exchange using his PayPal payment method. [System IDs: required_fields=payment_methods; required_fields=order_id; required_fields=variants; order_id=# W3913498; item_ids=1706622510; payment_method_id=paypal_6151711; item_ids=5038485381; new_item_ids=2880340443."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'lucas_rodriguez_6635'}, 'required_fields': ['order_id', 'items', 'status', 'payment_history']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Gaming Mouse']}, 'required_fields': ['variants']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W3913498', 'item_ids': ['1706622510'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W3913498', 'item_ids': ['5038485381'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'paypal_6151711'},
            ),
        ],
        outputs=[]
    ),

    # Task 072: Customer includes payment method and submits order.
    Task(
        annotator="0",
        user_id="task_072",
        instruction="You are assisting customer Ahmad Khan from zip 78242 who intends to add a new Visa credit card (last four digits 4321) to his account, and then you assist him in using it to purchase a Water Bottle and Desk Lamp for his office. [System IDs: user_id=ahmad_khan_2015; required_fields=product_id; item_ids=5758737025; payment_method_id=credit_card_2015]. Key entities: visa, Yusuf.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Khan', 'zip': '78242'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ahmad_khan_2015', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '4321'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Water Bottle', 'Desk Lamp']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ahmad_khan_2015', 'item_ids': ['5758737025', '5320792178'], 'payment_method_id': 'credit_card_2015'},
            ),
        ],
        outputs=[]
    ),

    # Task 073: Management of gift cards and creation of orders
    Task(
        annotator="0",
        user_id="task_073",
        instruction="Assist customer Isabella Wilson from zip 43118 who wants to load $400 onto a new gift card and subsequently place an order for a Backpack and Running Shoes using the gift card balance. [System IDs: required_fields=payment_methods; user_id=isabella_wilson_4616; required_fields=product_id; item_ids=9851293632; payment_method_id=gift_card_4616]. Key entities: Olivia, Brown, 400.0.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Olivia', 'last_name': 'Brown', 'zip': '43118'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'isabella_wilson_4616'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'isabella_wilson_4616', 'payment_method_source': 'gift_card', 'balance': 400.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Backpack', 'Running Shoes']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'isabella_wilson_4616', 'item_ids': ['9851293632', '9791469541'], 'payment_method_id': 'gift_card_4616'},
            ),
        ],
        outputs=[]
    ),

    # Task 074: Order for multiple product supplies
    Task(
        annotator="0",
        user_id="task_074",
        instruction="Assist a customer in creating supply orders for a variety of products: procure 40 T-Shirts (item id 3799046073) from Tech Supplies Inc., 30 Notebooks (item id 7579176349) from Worldwide Electronics Partners, and 25 Sunglasses (item id 4245201809) from Style Trend Distributors. Align the unit cost with the current price listed in the product database. Afterward, update supplier inventories to reflect these reductions.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['T-Shirt', 'Notebook', 'Sunglasses']}, 'required_fields': ['variants', 'supplier_id']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0001', '#SUP0002', '#SUP0007']}, 'required_fields': ['name', 'item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '3799046073', 'quantity': 40, 'unit_cost': 53.27},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '7579176349', 'quantity': 30, 'unit_cost': 29.28},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0007', 'item_id': '4245201809', 'quantity': 25, 'unit_cost': 281.48},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {'3799046073': 7}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0002'}, 'update_params': {'item_stock': {'7579176349': 40}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0007'}, 'update_params': {'item_stock': {'4245201809': 142}}},
            ),
        ],
        outputs=[]
    ),

    # Task 075: Support for order tracking inquiries.
    Task(
        annotator="0",
        user_id="task_075",
        instruction="As customer William Lee from zip 43138, you're purchasing a Wristwatch and Action Camera for photography. Establish a new credit card (visa, last four digits 2039) for the payment. Arrange express delivery via SpeedWay Delivery and relay the tracking information. [System IDs: required_fields=payment_methods; required_fields=product_id; user_id=james_lee_9638; item_ids=2407258246; payment_method_id=credit_card_9638; required_fields=courier_id; order_id=#W0001001; courier_id=# W0001001; courier_id=#COU0001]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'James', 'last_name': 'Lee', 'zip': '43138'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'james_lee_9638'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wristwatch', 'Action Camera']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'james_lee_9638', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2039'},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'james_lee_9638', 'item_ids': ['2407258246', '6700049080'], 'payment_method_id': 'credit_card_9638'},
            ),
            # retrieve courier_id for SpeedWay Delivery
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2407258246', '6700049080'],'courier_id': '#COU0001', 'delivery_option': 'express'},
            ),
        ],
        outputs=[]
    ),

    # Task 076: Update database and manage users
    Task(
        annotator="0",
        user_id="task_076",
        instruction="Assist customer Lucas Johnson (user_id: lucas_johnson_2067, item: 6017636844) from zip 98147 in placing an order for a Laptop and E-Reader for professional use. Use his pre-existing credit card payment method (credit_card_3956549).",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Lucas', 'last_name': 'Johnson', 'zip': '98147'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_johnson_2067'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'E-Reader']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'lucas_johnson_2067', 'item_ids': ['6017636844', '7609274509'], 'payment_method_id': 'credit_card_3956549'},
            ),
        ],
        outputs=[]
    ),

    # Task 077: Customer retrieval and order processing via email.
    Task(
        annotator="0",
        user_id="task_077",
        instruction="Assist a customer with the email mei.kim7945@example.com (user_id: mei_kim_6875) who wishes to purchase Yoga Mat (item 5586947715) and Bluetooth Speaker (item 2635605237) for her fitness routine. Use her existing credit card linked to her account if available; otherwise, add her PayPal (paypal_6875) and proceed with that payment method.",
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'mei.kim7945@example.com'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mei_kim_6875'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'mei_kim_6875', 'payment_method_source': 'paypal'}
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'mei_kim_6875', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'paypal_6875'},
            ),
        ],
        outputs=[]
    ),

    # Task 078: Coordination of multi-step orders and suppliers
    Task(
        annotator="0",
        user_id="task_078",
        instruction="Support customer Olivia Costa, located in zip code 75217, in ordering Hiking Boots and Fleece Jacket for her outdoor activities. Subsequently, arrange for standard delivery tracking with AgileTransport Services. [System IDs: required_fields=payment_methods; required_fields=product_id; user_id=emma_silva_1269; item_ids=8277474082; payment_method_id=credit_card_4492026; required_fields=courier_id; order_id=#W0001001; courier_id=# W0001001; courier_identifier=#COU0004]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Emma', 'last_name': 'Silva', 'zip': '75217'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_silva_1269'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Hiking Boots', 'Fleece Jacket']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'emma_silva_1269', 'item_ids': ['8277474082', '5992316252'], 'payment_method_id': 'credit_card_4492026'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['8277474082', '5992316252'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    # Task 079: Customer order requiring global delivery
    Task(
        annotator="0",
        user_id="task_079",
        instruction="Assist customer Raleigh Khan from zip 94171 who is interested in purchasing a Tablet and Wireless Earbuds. Help Ava link her PayPal to her account, which will then be used to place any orders. Generate tracking with a courier capable of delivering to Mexico, opting for the standard delivery method. [System IDs: required_fields=payment_methods; required_fields=product_id; user_id=ava_khan_1840; item_ids=2106335193; payment_method_id=paypal_1840; required_fields=courier_id; order_id=#W0001001; courier_id=# W0001001; courier_id=#COU0001]."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ava', 'last_name': 'Khan', 'zip': '94171'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ava_khan_1840'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Tablet', 'Wireless Earbuds']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'ava_khan_1840', 'payment_method_source': 'paypal'}
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'ava_khan_1840', 'item_ids': ['2106335193', '8555936349'], 'payment_method_id': 'paypal_1840'},
            ),
            # retrieve courier_id for Mexico
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'coverage_area': 'Mexico'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2106335193', '8555936349'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),

    # Task 080: Management of bulk supply orders
    Task(
        annotator="0",
        user_id="task_080",
        instruction="As the head of warehousing, you're tasked with restocking popular products: Coordinate supply orders for 100 Mechanical Keyboards (at $125.99 unit cost) from Athletic Equipment Co., 80 Water Bottles (500ml, glass, black) at $24.50 unit cost from Workplace Solutions Center, and update the supplier item inventory.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Mechanical Keyboard', 'Water Bottle']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0010', '#SUP0008']}, 'required_fields': ['item_stock', 'contact_info']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0010', 'item_id': '3616838507', 'quantity': 100, 'unit_cost': 125.99},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '8538875209', 'quantity': 80, 'unit_cost': 24.50},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0010'}, 'update_params': {'item_stock': {'3616838507': 62}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'update_params': {'item_stock': {'8538875209': 94}}},
            ),
        ],
        outputs=[]
    ),

    # Task 081: Handling customer returns and processing refunds
    Task(
        annotator="0",
        user_id="task_081",
        instruction="Assist customer Omar White from zip 85011 who wishes to return his Desk Lamp and Hiking Boots from a past purchase. Coordinate the process for the returns and issue a refund to his PayPal account. [System IDs: required_fields=orders; order_id=# W2091016; item_ids=1270145486; payment_method_id=paypal_2055565]. Main entities: Anderson."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Omar', 'last_name': 'Anderson', 'zip': '85011'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_white_5940'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2091016'}, 'required_fields': ['items']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W2091016', 'item_ids': ['1270145486', '6546364613'], 'payment_method_id': 'paypal_2055565'},
            ),
        ],
        outputs=[]
    ),

    # Task 082: Establish new customer account and process initial order.
    Task(
        annotator="0",
        user_id="task_082",
        instruction="Facilitate customer Mason Anderson from zip 85060 in adding a new American Express credit card (last four 8765) and arranging his initial order for a Portable Charger and Indoor Security Camera. [System IDs: user_id=mason_anderson_3178; required_fields=product_id; item_ids=1178356107; payment_method_id=credit_card_3178]. Key entities: american_express, Liam, Wilson.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Liam', 'last_name': 'Wilson', 'zip': '85060'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'mason_anderson_3178', 'payment_method_source': 'credit_card', 'brand': 'american_express', 'last_four': '8765'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Portable Charger', 'Indoor Security Camera']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'mason_anderson_3178', 'item_ids': ['1178356107', '8470360507'], 'payment_method_id': 'credit_card_3178'},
            ),
        ],
        outputs=[]
    ),

    # Task 083: Reloading and buying gift cards
    Task(
        annotator="0",
        user_id="task_083",
        instruction="Assist customer Amelia Jackson from zip 85034 who is looking to add $250 to her gift card using her mastercard. Help her with this task and then assist in purchasing a Wall Clock and Garden Hose for her home renovation project by utilizing the gift card balance. [System IDs: required_fields=payment_methods; user_id=amelia_jackson_6490; gift_card_id=gift_card_8245350; payment_method_id=credit_card_8554680; required_fields=product_id; item_ids=9850781806].",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Lopez', 'zip': '85034'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'amelia_jackson_6490'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'amelia_jackson_6490', 'gift_card_id': 'gift_card_8245350', 'payment_method_id': 'credit_card_8554680', 'amount': 250.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wall Clock', 'Garden Hose']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'amelia_jackson_6490', 'item_ids': ['9850781806', '9829827210'], 'payment_method_id': 'gift_card_8245350'},
            ),
        ],
        outputs=[]
    ),

    # Task 084: Workflow for product exchange
    Task(
        annotator="0",
        user_id="task_084",
        instruction="Assist customer Mei Dean from zip 77083 who has received the incorrect type of espresso machine and wishes to exchange it for the correct type (item id 3709608322). Also, aid her in exchanging her mechanical keyboard for a different style (item id 3616838507). You should register her credit card (mastercard, last four 3505) as a payment method for the exchanges.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Mei', 'last_name': 'Kim', 'zip': '77083'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mei_dean_3337'}, 'required_fields': ['order_id', 'payment_history', 'items']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'mei_dean_3337', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '3505'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Espresso Machine', 'Mechanical Keyboard']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W3263208', 'item_ids': ['6324294385','7867398203'], 'new_item_ids': ['3709608322','3616838507'], 'payment_method_id': 'credit_card_3337'},
            ),
        ],
        outputs=[]
    ),

    # Task 085: Coordination with suppliers and execution of orders.
    Task(
        annotator="0",
        user_id="task_085",
        instruction="As an inventory specialist, review the inventory levels for Digital Paradise Distributors. Proceed to create supply orders to request one unit for items with low stock (2 units or fewer, excluding out-of-stock or discontinued items), each costing $100. Afterward, process customer Mia Martinez's (zip 19036) order for a Yoga Mat and Bluetooth Speaker. [System IDs: required_fields=supplier_id; supplier_id=# SUP0004; item_id=5510402676; mandatory_fields=payment_methods; mandatory_fields=product_id; user_id=anya_garcia_3271; item_ids=5586947715; payment_method_id=credit_card_8955149."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': ['Tech Haven Supplies']}, 'required_fields': ['supplier_id', 'item_stock', 'products']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '5510402676', 'quantity': 1, 'unit_cost': 100},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'credit_card_8955149'},
            ),
        ],
        outputs=[]
    ),

    # Task 086: Customer support with tracking status update
    Task(
        annotator="0",
        user_id="task_086",
        instruction="In your role as a customer service representative, assist customer Harper Silva (user_id: harper_silva_8534) from zip 92188 who placed an order that includes a Cycling Helmet and wishes to upgrade to express shipping with SwiftMove Couriers (courier #COU0004). Ensure the tracking details (tracking_id: 360095850863) are updated to reflect this change to express delivery. Order: #W7111365, courier: # Update the tracking information (tracking_id: 360095850863) to indicate the change to express delivery for Order: #W7111365, courier: #COU0004."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Harper', 'last_name': 'Silva', 'zip': '92188'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'harper_silva_8534'}, 'required_fields': ['items', 'fulfillments']},
            ),
            # retrieve identifier for AgileTransport Services
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'tracking', 'filter_params': {'tracking_id': '360095850863'}, 'update_params': {'delivery_options': 'express', 'delivery_carrier': '#COU0004'}},
            ),
        ],
        outputs=[]
    ),

    # Task 087: Update payment method for multi-item order
    Task(
        annotator="0",
        user_id="task_087",
        instruction="Assist customer Chen Costa from zip 46281 in updating his payment details by adding a new PayPal account. Next, purchase a Laptop, Gaming Mouse, and Notebook for his work arrangement utilizing the newly added payment method. [System IDs: user_id=chen_silva_7485; required_fields=product_id; item_ids=6017636844; payment_method_id=paypal_7485].",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Chen', 'last_name': 'Silva', 'zip': '46281'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'chen_silva_7485', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'Gaming Mouse', 'Notebook']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'chen_silva_7485', 'item_ids': ['6017636844', '2880340443', '9799386954'], 'payment_method_id': 'paypal_7485'},
            ),
        ],
        outputs=[]
    ),

    # Task 088: Managing inventory and fulfilling customer orders
    Task(
        annotator="0",
        user_id="task_088",
        instruction="As a warehouse manager, coordinate a supply order for Bluetooth Speakers from Home Essentials Co. Given the high demand, choose the variant with the highest stock and place an order for 90 units at $90 per unit. Subsequently, generate an order for the identical item for customer Ella Kovacs from zip 32117. [System IDs: required_fields=product_id; required_fields=supplier_id; supplier_id=# SUP0006; item_id=7617930199; necessary_fields=payment_methods; user_id=evelyn_kovacs_6742; payment_method_id=paypal_7732922]."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Bluetooth Speaker'}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            # retrieve the supplier_id for Home Essentials Co.

            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Home Essentials Co.'}, 'required_fields': ['supplier_id', 'item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '7617930199', 'quantity': 90, 'unit_cost': 90},
            ),
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Evelyn', 'last_name': 'Kovacs', 'zip': '32117'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'evelyn_kovacs_6742'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'evelyn_kovacs_6742', 'item_ids': ['7617930199'], 'payment_method_id': 'paypal_7732922'},
            ),
        ],
        outputs=[]
    ),

    # Task 089: Retrieve and rearrange workflow
    Task(
        annotator="0",
        user_id="task_089",
        instruction="Assist customer Yara Sanchez from zip 75255 in returning her faulty skateboard and placing a new order for the identical item, along with a Portable Charger featuring options 5000mAh, USB-C, white. Handle the return and initiate a new order. [System IDs: required_fields=orders; required_fields=payment_history; order_id=# W6015009; item_ids=3877188862; payment_method_id=credit_card_5884162; mandatory_fields=product_id; user_id=yara_sanchez_1902; item_ids=7866854614."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Yara', 'last_name': 'Sanchez', 'zip': '75255'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['items', 'payment_history', 'order_id']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W6015009', 'item_ids': ['3877188862'], 'payment_method_id': 'credit_card_5884162'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Skateboard', 'Portable Charger']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'yara_sanchez_1902', 'item_ids': ['7866854614', '3877188862'], 'payment_method_id': 'credit_card_5884162'},
            ),
        ],
        outputs=[]
    ),

    # Task 090: Retrieve email addresses and establish priority sequencing.
    Task(
        annotator="0",
        user_id="task_090",
        instruction="Support the customer with email aarav.white9752@example.com who requires urgent delivery of Smart Thermostat and Electric Kettle for his smart home project. Coordinate to add a credit card (visa, last four 2512) for payment. Utilize priority shipping via QuickPath Distribution. [System IDs: user_id=aarav_anderson_8794; required_fields=product_id; item_ids=4953074738; payment_method_id=credit_card_8794; required_fields=courier_id; order_id=#W0001001; courier_id=# W0001001; courier_id=#COU0005]."
        actions=[
            Action(
                name="GetUserIdFromEmail",
                kwargs={'email': 'aarav.anderson9752@example.com'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'aarav_anderson_8794', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2512'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smart Thermostat', 'Electric Kettle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'aarav_anderson_8794', 'item_ids': ['4953074738', '1240311797'], 'payment_method_id': 'credit_card_8794'},
            ),
            # retrieve courier_id for QuickPath Distribution
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'RapidRoute Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['4953074738', '1240311797'], 'courier_id': '#COU0005', 'delivery_option': 'priority'},
            ),
        ],
        outputs=[]
    ),

    # Task 055: Managing supplier connections and large-scale purchasing
    Task(
        annotator="0",
        user_id="task_091",
        instruction="Coordinate with various suppliers: order 120 E-Readers (item id 7609274509) from Digital Paradise Distributors, procure 85 Running Shoes (item id 9635758562) from Home Essentials Co., and update supplier inventories. Ensure the unit cost for these supply orders matches the item's price in the product database.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['E-Reader', 'Running Shoes']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0004', '#SUP0006']}, 'required_fields': ['contact_info', 'item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '7609274509', 'quantity': 120, 'unit_cost': 243.40},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '9635758562', 'quantity': 85, 'unit_cost': 148.95},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'update_params': {'item_stock': {'7609274509': 57}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0006'}, 'update_params': {'item_stock': {'9635758562': 35}}},
            ),
        ],
        outputs=[]
    ),

    # Task 056: Loyalty program for customers and custom orders.
    Task(
        annotator="0",
        user_id="task_092",
        instruction="Assist customer Sofia Li from zip 78260 who intends to place an order for a Wristwatch and a Fleece Jacket, using her mastercard for payment. Generate tracking and opt for the white-glove delivery service from courier # COU0001."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Sofia', 'last_name': 'Li', 'zip': '78260'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wristwatch', 'Fleece Jacket']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_9219'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['2407258246', '5992316252'], 'payment_method_id': 'credit_card_8105988'},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2407258246', '5992316252'], 'courier_id': '#COU0001', 'delivery_option': 'white_glove'},
            ),
        ],
        outputs=[]
    ),

    # Task 057: Complicated request involving several operations
    Task(
        annotator="0",
        user_id="task_093",
        instruction="Handle the complex order for customer Olivia Wilson from zip 32165: generate a gift card valued at $900 for her. Assist her in placing an order for a Yoga Mat and a Wall Clock, utilize her gift card for payment, and organize standard delivery tracking with couriers # COU0002. Next, check supplier inventory for the 25ft green rubber Garden Hose and place an order for 35 units at $15.00 per unit."
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Emma', 'last_name': 'Brown', 'zip': '32165'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_wilson_8847'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'olivia_wilson_8847', 'payment_method_source': 'gift_card', 'balance': 900.0},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Wall Clock']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'olivia_wilson_8847', 'item_ids': ['5586947715', '9850781806'], 'payment_method_id': 'gift_card_8847'},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5586947715', '9850781806'],'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Garden Hose']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '5753502325', 'quantity': 35, 'unit_cost': 15.00},
            ),
        ],
        outputs=[]
    ),

    # Task 058: Escalation of customer service regarding multiple returns.
    Task(
        annotator="0",
        user_id="task_094",
        instruction="Converse with customer Raj Jackson from zip 92147 who has encountered quality issues with multiple items. He intends to return the wireless earbuds and swap the grill for the portable, electric, side burner model. Afterwards, apply a compensation credit of $25 to his account.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            # retrieve his order details
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'raj_lopez_2970'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="ProcessItemReturn",
                kwargs={'order_id': '#W1067251', 'item_ids': ['6452271382'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Grill'}, 'required_fields': ['variants']},
            ),
            Action(
                name="ProcessItemExchange",
                kwargs={'order_id': '#W1067251', 'item_ids': ['7848293342'], 'new_item_ids': ['3876764226'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_lopez_2970'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_lopez_2970'}, 'update_params': {'payment_methods': {'gift_card_2259499': {'balance': 55.00}}}},
            ),
        ],
        outputs=[]
    ),

    # Task 059: Preparation of inventory for the season.
    Task(
        annotator="0",
        user_id="task_095",
        instruction="Manage seasonal demand preparation: draft significant supply orders for 150 Fleece Jackets (item id 5992316252) from Kitchen Essentials Co., and 50 Hiking Boots (item id 2658930189) from Worldwide Electronics Partners, each priced at $50 per unit. Afterward, adjust the pricing for both items in the product database to be reduced by $10. [System IDs: required_fields=product_id; supplier_id=#SUP0012; supplier_id=# SUP0012; supplier_id=#SUP0002."
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Fleece Jacket', 'Hiking Boots']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0012', 'item_id': '5992316252', 'quantity': 150, 'unit_cost': 50},
            ),
            Action(
                name="CreateSupplyOrder",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '2658930189', 'quantity': 50, 'unit_cost': 50},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Fleece Jacket']}, 'update_params': {'variants':{'5992316252': {"price": 131.29}}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Hiking Boots']}, 'update_params': {'variants':{'2658930189': {"price": 231.68}}}},
            ),
        ],
        outputs=[]
    ),

    # Task 060: Bulk order for corporate clients
    Task(
        annotator="0",
        user_id="task_096",
        instruction="As a customer service representative, assist corporate client Evelyn Simpson from zip 94113 with bulk office supply needs: 25 Laptops, 50 Notebooks, and 30 Desk Lamps. She intends to establish payment using a new credit card (visa, last four 2533). Coordinate a business delivery through RapidTransit Solutions.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Amelia', 'last_name': 'Nguyen', 'zip': '94113'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'evelyn_simpson_5209', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2533'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'Notebook', 'Desk Lamp']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateBulkOrder",
                kwargs={'user_id': 'evelyn_simpson_5209', 'item_ids': {'6017636844':25, '9799386954':50, '5320792178':30}, 'payment_method_id': 'credit_card_5209'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'RapidTransit Solutions'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001','item_ids': ['6017636844', '9799386954', '5320792178'], 'courier_id': '#COU0002', 'delivery_option': 'business'},
            ),
        ],
        outputs=[]
    ),

    # Task 097: Enrollment in the customer loyalty program
    Task(
        annotator="0",
        user_id="task_097",
        instruction="Assist customer Lucas Russo from zip 10056 in placing his initial order for 'Running Shoes' and 'Water Bottle'. Collect his email to send the order confirmation. [System IDs: required_fields=product_id; required_fields=payment_methods; user_id=lucas_russo_9776; item_ids=9791469541; payment_method_id=credit_card_8621045]. Key entities: Rossi, Ivan.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Rossi', 'zip': '10056'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Running Shoes', 'Water Bottle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_russo_9776'}, 'required_fields': ['email', 'payment_methods']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'lucas_russo_9776', 'item_ids': ['9791469541', '5758737025'], 'payment_method_id': 'credit_card_8621045'},
            ),
        ],
        outputs=[]
    ),

    # Task 098: Global order with customs processing
    Task(
        annotator="0",
        user_id="task_098",
        instruction="Assist customer Juan Dean from zip 95120. He needs to order 'portable charger (10000mAh, USB-C, blue)' and ship it to Mexico. Initiate the order and update the delivery address to Lakeview Drive, W 3rd St, Toronto, ON, Mexico, M4C 1A1. Coordinate 'international_express' tracking with an appropriate courier.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Juan', 'last_name': 'Kim', 'zip': '95120'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'juan_dean_6026'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Portable Charger']}, 'required_fields': ['variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'juan_dean_6026', 'item_ids': ['7884173033'], 'payment_method_id': 'paypal_5061070'},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address1': 'Lakeview Drive', 'address2': 'W 3rd St', 'city': 'Toronto', 'state': 'ON', 'country': 'Mexico', 'zip': 'M4C 1A1'}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'coverage_area': 'Mexico'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['7884173033'],'courier_id': '#COU0002', 'delivery_option': 'international_express'},
            ),
        ],
        outputs=[]
    ),

    # Task 063: Management of supplier relationships and quality assurance
    Task(
        annotator="0",
        user_id="task_099",
        instruction="As a quality control officer, handle the reported defective Electric Toothbrush batch (variant 1583904702) from the Literature Plus supplier. Complete the necessary actions. Key entities: False.",
        actions=[
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Literature Plus'}, 'required_fields': ['supplier_id']},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'1583904702':'defective'}}},
            ),
            Action(
                name="UpdateDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Toothbrush'}, 'update_params': {'variants': {'1583904702':{'available':False}}}},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'orders', 'filter_params': {'items':{'item_id': '1583904702'}}, 'required_fields': ['user_id']},
            ),
             Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': ['emma_moore_8366','isabella_ahmed_6778','ahmad_hernandez_5411']}, 'required_fields': ['email']},
            ),
        ],
        outputs=[]
    ),

    # Task 100: Management of customer accounts and processing of orders.
    Task(
        annotator="0",
        user_id="task_100",
        instruction="Assist customer Fatima Anderson from zip 78746 in updating her account with a new Mastercard (last four 2468), adding a gift card, and separately increasing her gift card balance by $3000 using the new Mastercard. Following that, order the Smart Thermostat and Garden Hose for her home improvement project with her gift card. Finally, expedite the package by establishing a tracking with the standard delivery option using SpeedWay Delivery.",
        actions=[
            Action(
                name="GetUserIdFromFullNameAndZip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Wilson', 'zip': '78746'},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'fatima_anderson_6873', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '2468'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'fatima_anderson_6873'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="AddPaymentMethod",
                kwargs={'user_id': 'fatima_anderson_6873', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="AddMoneyToGiftCard",
                kwargs={'user_id': 'fatima_anderson_6873', 'gift_card_id': 'gift_card_6873', 'payment_method_id': 'credit_card_6873', 'amount': 3000.0},
            ),
            # retrieve value from specified card
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smart Thermostat', 'Garden Hose']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="CreateOrder",
                kwargs={'user_id': 'fatima_anderson_6873', 'item_ids': ['9829827210', '4953074738'], 'payment_method_id': 'gift_card_6873'},
            ),
            Action(
                name="GetInfoFromDb",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SpeedWay Delivery'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="CreateTracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['9829827210', '4953074738'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[]
    ),
]
