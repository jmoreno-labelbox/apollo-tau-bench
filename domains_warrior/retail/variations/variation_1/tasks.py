from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction="You are a customer service representative. You must help a customer, Emma Smith from zip code 10192.  You should help her place a new order for 2 laptops (one with 15-inch screen, i9 processor the other with a 13-inch screen, i7 processor in black) and the cheapest available smartphone. You should use her PayPal payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Emma', 'last_name': 'Smith', 'zip': '10192'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smartphone'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_smith_8564'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'emma_smith_8564', 'item_ids': ['5339029584', '2913673670', '1657832319'], 'payment_method_id': 'paypal_6228291'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_002",
        instruction="You are a warehouse manager, James Johansson (user ID james_johansson_2031, zip 28260). Create a supply order for 40 units of T-shirts (black, size XXL, cotton, crew neck) from supplier #SUP0001 at $25 per unit. Then buy one of the t-shirts for yourself using your gift card.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'T-Shirt'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'products': '9523456873'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '3799046073', 'quantity': 40, 'unit_cost': 25.0},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {"3799046073": 7}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'james_johansson_2031'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'james_johansson_2031', 'item_ids': ['3799046073'], 'payment_method_id': 'gift_card_9136273'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'james_johansson_2031'}, 'update_params': {"payment_methods":{"gift_card_9136273":{'balance': 88-53.27}}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_003",
        instruction="You are a customer service rep. A customer Yusuf Rossi with zip 19122 recieved their order #W2378156 and wants to exchange the mechanical keyboard for the cheapest available one with clicky switches and the smart thermostat for one compatible with Google Home instead of Apple HomeKit.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Rossi', 'zip': '19122'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2378156'}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '1656367028'}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '4896585277'}},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W2378156', 'item_ids': ['1151293680', '4983901480'], 'new_item_ids': ['2299424241', '7747408585'], 'payment_method_id': 'credit_card_9513926'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_004",
        instruction="You are Yusuf Rossi from zip 19122. You want to return the cleaner, headphone, and smart watch from a previous order.",
        actions=[
            # Get user ID
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Rossi', 'zip': '19122'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={
                    'database_name': 'users',
                    'filter_params': {'user_id': 'yusuf_rossi_9620'},
                    'required_fields': ['orders', "payment_methods"]},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': ["#W6247578","#W9711842","#W4776164","#W6679257","#W2378156"]}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W2378156', 'item_ids': ['4602305039', '4202497723', '9408160950'], 'payment_method_id': 'credit_card_9513926'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_005",
        instruction="You are an inventory manager. Update the status of all pending supply orders from supplier #SUP0002 to 'fulfilled' and get the name of the products they supply. Also check for any pending orders containing the items from these supply orders and create a tracking entry for the delivery of these orders using standard delivery with Global Express Couriers.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', "status": "pending"}, 'required_fields': ['supply_order_id', 'product_id', 'item_id']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', "status": "pending"}, 'update_params': {"status": "fulfilled"}},
            ),
            # get product names from supply orders
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': ['6858788497', '2892623495']}, 'required_fields': ['name']},
            ),
            # get courier id for Global Express Couriers
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'Global Express Couriers'}, 'required_fields': ['courier_id']},
            ),
            # find orders containing these items
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'items': [{"item_id": "7579176349"},{"item_id": "9007697085"}], 'status': 'pending'}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W1258841', 'item_ids': ['7579176349', '3232433601', '5209958006'], 'courier_id': "#COU0010", 'delivery_option': 'standard'},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W1348609', 'item_ids': ['5606522780', '9007697085', '6313971174', '7195021808'], 'courier_id': "#COU0010", 'delivery_option': 'standard'},
            ),
        ],
        outputs=[{"name": "Notebook"}, {"name": "Perfume"}],
    ),

    Task(
        annotator="0",
        user_id="task_006",
        instruction="You are a customer service agent. Customer Omar Lopez from zip 90339 wants to add a new gift card payment method with $100 balance to his account. You should then help him return the air purifier from a recent order #W7273336. You should ensure that the refund is processed to the new gift card.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Omar', 'last_name': 'Lopez', 'zip': '90339'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_lopez_3107'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="add_payment_method",
                kwargs={"user_id": "omar_lopez_3107", "payment_method_source": "gift_card", "balance": 100.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'omar_lopez_3107'}, 'required_fields': ['order_id', 'items']}
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W7273336', 'item_ids': ['9375701158'], 'payment_method_id': 'gift_card_3107'},
            ),
            # Update the user's gift card balance
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_lopez_3107'}, 'update_params': {"payment_methods":{"gift_card_3107":{'balance': 100+489.5}}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_007",
        instruction="You are a product manager. Find all items from Tech Haven Supplies that are discontinued. Find any orders for these items that are pending and process an item return for those items using the original payment method.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Tech Haven Supplies'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'items':{'item_id': ['1631373418', "6195938807", "2499294441", "8759627937", "8964750292"]}, "status": "pending"}, 'required_fields': ['order_id', 'items', "payment_history"]},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W5432440", 'item_ids': ['1631373418'], 'payment_method_id': 'gift_card_4129829'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W7398274", 'item_ids': ['1631373418'], 'payment_method_id': 'paypal_7732922'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W8268544", 'item_ids': ['1631373418'], 'payment_method_id': 'gift_card_1402922'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W6940125", 'item_ids': ['6195938807'], 'payment_method_id': 'paypal_9379149'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W3618959", 'item_ids': ['6195938807'], 'payment_method_id': 'gift_card_9246707'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W2624389", 'item_ids': ['6195938807'], 'payment_method_id': 'credit_card_5809636'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W6599568", 'item_ids': ['2499294441'], 'payment_method_id': 'gift_card_3242199'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W7390432", 'item_ids': ['2499294441'], 'payment_method_id': 'paypal_1249653'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W7342738", 'item_ids': ['2499294441'], 'payment_method_id': 'gift_card_3491931'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': "#W9722559", 'item_ids': ['8964750292'], 'payment_method_id': 'paypal_8963303'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_008",
        instruction="You are Mei Kovacs (zip code: 28236) and you want to exchange the water bottle and the desk lamp. You want to exchange the water bottle the biggest they have, keeping the colour the same, and the desk lamp for a low brightness, battery powered one. Any price difference should be paid using the same payment method as the original order.",
        actions=[
            # Get user ID
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Mei', 'last_name': 'Kovacs', 'zip': '28236'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mei_kovacs_8020'}, 'required_fields': ['order_id','items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Water Bottle', 'Desk Lamp']}, 'required_fields': ['name', 'variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={
                    'order_id': '#W6390527',
                    'item_ids': ['8538875209', '8384507844'],
                    'new_item_ids': ['7661609223', '7453605304'],
                    'payment_method_id': 'paypal_7644869'
                },
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_009",
        instruction="You are mia_garcia_4516 (mia.garcia2723@example.com). For some reason, you want to return all things ordered. You have two payment methods (paypal_9497703 and credit_card_3124723) and two orders (#W5490111 and #W7387996), and you want to refund each order to the opposite order's payment method. First check your account details and order history to confirm all the items and costs involved.",
        actions=[
            # Get user ID
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'mia.garcia2723@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': ['#W5490111', '#W7387996']}, 'required_fields': ['order_id', 'items', 'payment_history', 'status', 'timestamp']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5490111'}, 'required_fields': ['items', 'fulfilments']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W7387996'}, 'required_fields': ['items', 'fulfilments']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W5490111', 'item_ids': ['4579334072', '1421289881', '6117189161','4947717507'], 'payment_method_id': 'paypal_9497703'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W7387996', 'item_ids': ['5796612084'], 'payment_method_id': 'credit_card_3124723'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['payment_methods']},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_010",
        instruction="You are a customer service supervisor. You are helping a customer with email mei.patel3193@example.com who wants to place a large order for 10 mechanical keyboards (full size, clicky with a white backlight) and 5 smart thermostats (black, compatible with Google Assistant). She would like to pay for the order using a new gift card with $14000 balance. You then help her by creating tracking for 'expedited' shipping for the order, using FastTrack Couriers.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'mei.patel3193@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mei_patel_7272'}, 'required_fields': ['payment_methods', 'address', 'membership_tier']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'mei_patel_7272', 'payment_method_source': 'gift_card', "balance":14000},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Mechanical Keyboard'}, 'required_fields': ['variants', 'availability', 'product_id']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smart Thermostat'}, 'required_fields': ['variants', 'availability', 'product_id']},
            ),
            Action(
                name="create_bulk_order",
                kwargs={'user_id': 'mei_patel_7272', 'item_ids': {'6342039236': 10, '7747408585': 5}, 'payment_method_id': 'gift_card_7272'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['6342039236', '7747408585'], 'courier_id': '#COU0001', 'delivery_option': 'expedited'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_011",
        instruction="You are a supply chain analyst. Check all suppliers that provide laptops (product name 'Laptop'), verify their current stock levels of laptop items, and create supply orders to order the whole stock for any laptop item with stock below 20 units (ignore out of stock or discontinued items) at $800 per unit. Only create supply orders for if the item is a laptop. Then mark the items out of stock in the supplier database. Also analyze the supplier contact information and verify the supply order creation was successful.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['product_id', 'supplier_id', "variants"]},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {"supplier_id": "#SUP0002"}, 'required_fields': ['item_stock', 'name', 'contact_info']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '1657832319', 'quantity': 8, 'unit_cost': 800.0},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '9844888101', 'quantity': 3, 'unit_cost': 800.0},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '4241599783', 'quantity': 1, 'unit_cost': 800.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'supply_orders', 'filter_params': {'supplier_id': '#SUP0002', 'status': 'pending'}, 'required_fields': ['supply_order_id', 'item_id', 'quantity', 'total_cost']},
            ),
            Action(
                name="update_db",
                kwargs = {"database_name":"suppliers", "filter_params":{"supplier_id":"#SUP0002"}, "update_params":{"item_stock":{"1657832319": "out_of_stock","9844888101": "out_of_stock","4241599783": "out_of_stock"}}}
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {"supplier_id": "#SUP0002"}, 'required_fields': ['item_stock']},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_012",
        instruction="You are Fatima Johnson, zip number 78712. You want to modify the pending order for hiking boots to a size 8, and want the same material, but do not care about waterproof or not. Use the existing payment method for the exchange. Also create tracking for the new item with standard delivery using courier #COU0002.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Johnson', 'zip': '78712'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'fatima_johnson_7581', 'status': 'pending'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={"database_name":"products", "filter_params":{"name":"Hiking Boots"}, "required_fields":['variants']}
            ),
            Action(
                name="process_item_exchange",
                kwargs={"order_id":"#W5199551","item_ids":["1615379700"], "new_item_ids":["3613716226"], "payment_method_id":"paypal_5364164"}
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W5199551', 'item_ids': ['3613716226'], 'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_013",
        instruction="You are helping customer Daiki Muller from zip code 94157 who needs to change the delivery address for her pending order that contains a dumbell set to a new address: 842 Oak Street, Suite 205, Indianapolis, IN 46202. You also create tracking for this order with using standard shipping with FastTrack Couriers and update the status to 'processed'.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Daiki', 'last_name': 'Muller', 'zip': '94157'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'daiki_muller_8062'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6790887'}, 'update_params': {'address': {'address1': '842 Oak Street', 'address2': 'Suite 205', 'city': 'Indianapolis', 'state': 'IN', 'zip': '46202'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W6790887', 'item_ids': ['6585768447', '2052249669'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6790887'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_014",
        instruction="You are an account manager. Customer Chen Silva with email chen.silva2698@example.com wants to update their profile name from 'Chen Silva' to 'Chen Roberts' and add a new credit card payment method (a visa card ending in 2534). They also want to add $200 to their existing gift card balance using their existing mastercard credit card. First verify current account details and confirm all payment methods.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'chen.silva2698@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['name', 'payment_methods', 'address']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'update_params': {'name': {'first_name': 'Chen', 'last_name': 'Roberts'}}},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'chen_silva_7485', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2534'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'chen_silva_7485', 'gift_card_id': 'gift_card_7250692', 'payment_method_id': 'credit_card_1565124', 'amount': 200.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'chen_silva_7485'}, 'required_fields': ['name', 'payment_methods']},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_015",
        instruction="You are a customer service agent. Customer Ava Nguyen from zip 78786 wants to return the bluetooth speaker she ordered due to compatibility issues. Process the return using her original payment method and create a new order for headphones (on-ear, red, wireless) instead using the same payment method. Verify customer details first and create tracking (using standard delivery and courier ID #COU0004) for the new order.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ava', 'last_name': 'Nguyen', 'zip': '78786'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ava_nguyen_2175'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ava_nguyen_2175'}, 'required_fields': ['payment_history', 'items', 'order_id']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3779151', 'item_ids': ['2635605237'], 'payment_method_id': 'paypal_6262583'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Headphones'}, 'required_fields': ['variants', 'availability', 'price']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'ava_nguyen_2175', 'item_ids': ['3104857380'], 'payment_method_id': 'paypal_6262583'},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['3104857380'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_016",
        instruction="You are a warehouse supervisor. Create a new supply order for 75 units of electric kettles (2L, glass, white) at $95 per unit. Then update the payment history for order Ava Moore's (zip 85032) order of that same model of electric kettle to reflect a 'partial refund' of $150 was processed to her paypal due to the delay recieving it.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Kettle'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '4064702754', 'quantity': 75, 'unit_cost': 95.0},
            ),
            # Update the supplier's item stock
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'4064702754': 40}}},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ava', 'last_name': 'Moore', 'zip': '85032'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ava_moore_4814'}, 'required_fields': ['items', 'order_id', 'payment_history']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8495163'}, 'update_params': {'payment_history': {'transaction_type': 'partial_refund', 'amount': 150.0, 'payment_method_id': 'paypal_7478252'}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_017",
        instruction="You are a customer support specialist. You are helping customer Mason Lopez from zip 28221 to exchange his cycling helmet for the cheapest gaming mouse that is available. HYou help him to add a new PayPal payment method to his account for future purchases.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Mason', 'last_name': 'Lopez', 'zip': '28221'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mason_lopez_8519'}, 'required_fields': ['orders']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mason_lopez_8519'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Gaming Mouse'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W9892169', 'item_ids': ['6401214406'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'credit_card_2327218'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'mason_lopez_8519', 'payment_method_source': 'paypal'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_018",
        instruction="You are a customer service representative. You are helping customer Sofia Li with email sofia.li5731@example.com who wants to add $750 to her existing gift card using her other payment method. You also help her to order for a yoga mat (4mm, PVC, blue) and portable charger (20000mAh, black, wireless) using that gift card as payment.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'sofia.li5731@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_8235'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'sofia_li_8235', 'gift_card_id': 'gift_card_3242199', 'payment_method_id': 'credit_card_8296913', 'amount': 750.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Portable Charger']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'sofia_li_8235', 'item_ids': ['5586947715', '8349903180'], 'payment_method_id': 'gift_card_3242199'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_019",
        instruction="You are a customer account manager. You are helping customer Emma Ito from zip 19022 to change her name from 'Emma Ito' to 'Emma Ito-Martinez' and return the coffee maker from her recent order, putting the refund on her original payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Emma', 'last_name': 'Ito', 'zip': '19022'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_ito_4529'}, 'required_fields': ['name', 'orders', 'payment_methods']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_ito_4529'}, 'update_params': {'name': {'first_name': 'Emma', 'last_name': 'Ito-Martinez'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'emma_ito_4529'}, 'required_fields': ['order_id', 'items', 'payment_history', 'timestamp']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3780282', 'item_ids': ['9862136885'], 'payment_method_id': 'credit_card_8058445'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_020",
        instruction="You are a fulfillment specialist. Customer Liam Lee with email liam.lee9297@example.com wants to change the delivery address for his pending order #W2624389 to a business address: 456 Corporate Blvd, Suite 200, San Francisco, CA 94105. Also create tracking for this order using business class with delivery service #COU0001 and set the status to 'processed'.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'liam.lee9297@example.com'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'update_params': {'address': {'address1': '456 Corporate Blvd', 'address2': 'Suite 200', 'city': 'San Francisco', 'state': 'CA', 'zip': '94105'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'required_fields': ['items']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W2624389', 'item_ids': ['5930656038', '6195938807', '9314474252'], 'courier_id': '#COU0001', 'delivery_option': 'business'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2624389'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_021",
        instruction="You are a warehouse manager. Create a new supply order for 100 units of the wireless earbuds that have IPX4 water resistance, but are not available, at $85 per unit. Customer Ava Martin from zip 20236 also wants to add a new credit card payment method to her account (mastercard, last four digits 5678).",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wireless Earbuds'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '3694871183', 'quantity': 100, 'unit_cost': 85.0},
            ),
            # Update the supplier's item stock
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'update_params': {'item_stock': {'3694871183': 17}}},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ava', 'last_name': 'Martin', 'zip': '20236'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ava_martin_2430', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '5678'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_022",
        instruction="You are a customer service agent. You are helping customer Yusuf Khan with email yusuf.khan7390@example.com who wants to exchange his laptop for the cheapest e-reader available. He also wants to add a gift card with $150 balance to his account.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'yusuf.khan7390@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'E-Reader'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W1787190', 'item_ids': ['2216662955'], 'new_item_ids': ['7609274509'], 'payment_method_id': 'paypal_5796936'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yusuf_khan_7091', 'payment_method_source': 'gift_card', 'balance': 150.0},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_023",
        instruction="You are a returns coordinator. You are helping customer Amelia Kim from zip 28230 who wants to return the Mechanical Keyboard and put the refund on her gift card and create a new order for running shoes (she is a size 8) using her PayPal payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Amelia', 'last_name': 'Kim', 'zip': '28230'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'amelia_kim_4338'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W7634667'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W7634667', 'item_ids': ['1421289881'], 'payment_method_id': 'gift_card_4019778'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'amelia_kim_4338', 'item_ids': ['4153505238'], 'payment_method_id': 'paypal_1742092'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_024",
        instruction="You are an order specialist. You need to add to the payment history for order #W6679257 to reflect a partial refund of $200 was processed to the original credit card. Customer Harper Silva from zip 92188 also wants to change her name to 'Harper Silva-Johnson'.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6679257'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6679257'}, 'update_params': {'payment_history': {'transaction_type': 'partial_refund', 'amount': 200.0, 'payment_method_id': 'credit_card_9513926'}}},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Harper', 'last_name': 'Silva', 'zip': '92188'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'harper_silva_8534'}, 'update_params': {'name': {'first_name': 'Harper', 'last_name': 'Silva-Johnson'}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_025",
        instruction="You are a supply chain coordinator. You need to create a supply order for 40 units of 1080p, waterproof, black, action cameras from their supplier at $320 per unit. Then create tracking to track the return of the cancelled order #W9711842 using standard postage and SwiftMove Couriers and update status to 'returned'.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Action Camera'}, 'required_fields': ['supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '5925362855', 'quantity': 40, 'unit_cost': 320.0},
            ),
            # Update the supplier's item stock
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'5925362855': 2}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9711842'}, 'required_fields': ['items']},
            ),
            # Get courier information
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W9711842', 'item_ids': ['4245201809'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9711842'}, 'update_params': {'status': 'returned'}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_026",
        instruction="You are a customer support representative. You are helping customer Evelyn Kovacs with email evelyn.kovacs5369@example.com who wants to change the delivery address for all pending orders to : 456 New Street ,Apt 12B, Austin, TX, 78701. You should also add a new gift card with $300 balance to her account.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'evelyn.kovacs5369@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'evelyn_kovacs_6742'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'evelyn_kovacs_6742'}, 'required_fields': ['order_id', 'status', 'items', 'address']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'evelyn_kovacs_6742', 'status': 'pending'}, 'update_params': {'address': {'address1': '456 New Street', 'address2': 'Apt 12B', 'city': 'Austin', 'state': 'TX', 'zip': '78701'}}},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'evelyn_kovacs_6742', 'payment_method_source': 'gift_card', 'balance': 300},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_027",
        instruction="You are a customer service specialist. Your are helping customer Yusuf Khan from zip 75313 to add a gift card with $2000 balance to his account for future purchases. He also wants to create a new order for a smartphone (128GB, black, 4GB RAM) using that gift card as payment.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Khan', 'zip': '75313'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['orders', 'payment_methods', 'address', 'email']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yusuf_khan_7091', 'payment_method_source': 'gift_card', 'balance': 2000.0},
            ),
            # Action(
            #     name="get_info_from_db",
            #     kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['order_id', 'items', 'status']},
            # ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smartphone'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'yusuf_khan_7091', 'item_ids': ['5339029584'], 'payment_method_id': 'gift_card_7091'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_028",
        instruction="You need to create a new supply order for 4 units of garden hoses from supplier '#SUP0008' at $65 per unit and reduce the supplier stock. You are also helping customer Evelyn Gonzalez from zip 19186 also wants to return her smart watch from a previous order.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Garden Hose'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '9829827210', 'quantity': 4, 'unit_cost': 65.0},
            ),
            # Update the supplier's item stock
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'update_params': {'item_stock':{"9829827210": 1}}},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Evelyn', 'last_name': 'Gonzalez', 'zip': '19186'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'evelyn_gonzalez_8876'}, 'required_fields': ['orders']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'evelyn_gonzalez_8876'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W1508165', 'item_ids': ['2554056026'], 'payment_method_id': 'paypal_4191414'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_029",
        instruction="You are helping customer Lei Patel with email lei.patel2400@example.com to change her name to 'Lei Patel-Chen' and you need to create a new order for a fleece jacket using her credit card payment method.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'lei.patel2400@example.com'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lei_patel_3139'}, 'update_params': {'name': {'first_name': 'Lei', 'last_name': 'Patel-Chen'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Fleece Jacket'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lei_patel_3139'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'lei_patel_3139', 'item_ids': ['5992316252'], 'payment_method_id': 'credit_card_4589919'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_030",
        instruction="You are a customer account manager. You need to update the payment history for order #W4776164 for Yusuf Rossi to add a $75 'loyalty_refund' to the original payment. You are helping customer Harper Kovacs from zip 94145 who wants to change the delivery address for her pending order. The new address is: 789 Harbor Street, Suite 4, Boston, MA, 02101. Also update her user profile with the new address.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W4776164'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W4776164'}, 'update_params': {'payment_history': {'transaction_type': 'loyalty_refund', 'amount': 75.0, 'payment_method_id': 'credit_card_9513926'}}},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Harper', 'last_name': 'Kovacs', 'zip': '94145'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'harper_kovacs_7861'}, 'required_fields': ['orders']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'harper_kovacs_7861', 'status': 'pending'}, 'update_params': {'address': {'address1': '789 Harbor Street', 'address2': 'Suite 4', 'city': 'Boston', 'state': 'MA', 'zip': '02101'}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'harper_kovacs_7861'}, 'update_params': {'address': {'address1': '789 Harbor Street', 'address2': 'Suite 4', 'city': 'Boston', 'state': 'MA', 'zip': '02101'}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_031",
        instruction="You are a warehouse supervisor. You need to create a supply order for 180 units of wall clocks from supplier '#SUP0011' at $55 per unit. Then create tracking for order #W8665881 ('standard' delivery with courier '#COU0001') and set status to 'processed'.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wall Clock'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '9850781806', 'quantity': 180, 'unit_cost': 55.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8665881'}, 'required_fields': ['items']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W8665881', 'item_ids': ['5855700373', '9408160950', '4422467033', '1157853815', '8725040869'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W8665881'}, 'update_params': {'status': 'processed'}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_032",
        instruction="You are a customer service agent. You are helping customer Aarav Anderson with email aarav.anderson9752@example.com who wants to return his Sneakers from order #W5866402 and add a new credit card (visa, last four 1955) payment method to his account.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'aarav.anderson9752@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5866402'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W5866402', 'item_ids': ['9727387530'], 'payment_method_id': 'paypal_8049766'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'aarav_anderson_8794', 'payment_method_source': 'credit_card', 'last_four': '1955', 'brand': 'visa'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_033",
        instruction="You are helping customer Isabella Sanchez from zip 85093 who wants to exchange her bluetooth speaker (from order #W4277243) for a wristwatch and add a new gift card with $250 balance to her account.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Sanchez', 'zip': '85093'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'isabella_sanchez_2068'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wristwatch'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W4277243', 'item_ids': ['2635605237'], 'new_item_ids': ['2407258246'], 'payment_method_id': 'paypal_8516781'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'isabella_sanchez_2068', 'payment_method_source': 'gift_card', 'balance': 250.0},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_034",
        instruction="You are an order coordinator. You need to create a new supply order for 100 units of indoor security cameras from supplier '#SUP0001' at $180 per unit. Customer Raj Sanchez from zip 92147 wants to change his name to 'Raj Sanchez-Kumar'.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Indoor Security Camera'}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '8470360507', 'quantity': 100, 'unit_cost': 180.0},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_sanchez_2970'}, 'update_params': {'name': {'first_name': 'Raj', 'last_name': 'Sanchez-Kumar'}}},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_035",
        instruction="You are a customer support specialist. You are helping customer Olivia Ito with email olivia.ito5204@example.com who wants to change the delivery address for order #W3657213 (to 987 Elm Street, Unit 2, San Francisco, CA, USA, 94110) and return the action camera from that same order due to not liking the colour.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'olivia.ito5204@example.com'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3657213'}, 'update_params': {'address': {'address1': '987 Elm Street', 'address2': 'Unit 2', 'city': 'San Francisco', 'state': 'CA', 'country': 'USA', 'zip': '94110'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3657213'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3657213', 'item_ids': ['6700049080'], 'payment_method_id': 'gift_card_7794233'},
            ),
        ],
        outputs=[],
    ),

    Task(
        annotator="0",
        user_id="task_036",
        instruction="You are a fulfillment manager. You need to update the payment history for order #W1023987 to reflect a $125 'promotional cashback' was applied to the original payment method. Change tracking for this order to use courier #COU0001 and 'standard' delivery, and set order status to 'processed'. You also help the customer who placed this order to add $400 to their gift card, and add a credit card (visa, last four digits 2635) payment method as the source of the top up.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'required_fields': ['payment_history','items', 'user_id', 'fulfillments']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'update_params': {'payment_history': {'transaction_type': 'promotional_cashback', 'amount': 125.0, 'payment_method_id': 'gift_card_9450778'}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'tracking', 'filter_params': {'tracking_id': '974703204371'}, 'update_params': {'delivery_carrier': '#COU0001', 'delivery_option': 'standard'}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W1023987'}, 'update_params': {'status': 'processed'}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sophia_garcia_1101'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'sophia_garcia_1101', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2635'},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'sophia_garcia_1101', 'gift_card_id': 'gift_card_9450778', 'payment_method_id': 'credit_card_1101', 'amount': 400.0},
            ),
        ],
        outputs=[],
    ),

    # Task 037: Ivan Santos wants to return wireless earbuds - defective sound quality
    Task(
        annotator="0",
        user_id="task_037",
        instruction="You are a customer service representative. You hear that customer Ivan Santos (zip 75277) reports that the wireless earbuds from his order don't fit him. You process a return and refund to a new gift card that you create.",
        actions=[
            # Get user ID from full name and zip
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['items', 'order_id']},
            ),
            # create a new gift card for the refund
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Process the return
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6893533', 'item_ids': ['1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
        ],
        outputs=[],
    ),

    # Task 038: Anya Garcia wants to track her cancelled order and check gift card balance
    Task(
        annotator="0",
        user_id="task_038",
        instruction=" You are speaking to user Anya Garcia (zip 19036) who is asking about her cancelled order. You help her to check the current balance on her gift card since she received a refund. She then wants to place a new order for LED Light Bulb (75W Equivalent, daylight, WiFi-enabled) using her updated gift card balance.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'LED Light Bulb'}, 'required_fields': ['variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['7445824652'], 'payment_method_id': 'gift_card_4374071'},
            )
        ],
        outputs=[{"balance": 51}],
    ),

    # Task 039: Yara Sanchez wants to exchange mechanical keyboard for different switch type
    Task(
        annotator="0",
        user_id="task_039",
        instruction="You are a customer service rep helping customer yara_sanchez_1902 to exchange item_id 9025753381 (Mechanical Keyboard with clicky switches) for the same keyboard but with tactile switches instead. She finds the clicky switches too loud for her office. She also wants to use a gift card as the payment method for this exchange. You should add one for her if she doesn't already have one.",
        actions=[
            # Find the order and item to exchange
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yara_sanchez_1902', 'items':{'item_id': '9025753381'}}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'product_id': '1656367028'}, 'required_fields': ['variants', 'name']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['payment_methods']},
            ),
            # Check if the user has a gift card, if not create one
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yara_sanchez_1902', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Process the exchange
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W6015009', 'item_ids': ['9025753381'], 'new_item_ids': ['3616838507'], 'payment_method_id': 'gift_card_1902'},
            ),
        ],
        outputs=[],
    ),

    # Task 004: Ivan Santos needs to update his address for future deliveries
    Task(
        annotator="0",
        user_id="task_040",
        instruction="You are helping user Ivan Santos to update his address from '477 Park Avenue, Suite 558, Dallas, TX 75277' to '825 Main Street, Apt 12B, Austin, TX 78701'. You help Ivan add a new credit card (mastercard, last four 2053) and change all pending orders of his to use this new address and payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'update_params': {'address': {'address1': '825 Main Street', 'address2': 'Apt 12B', 'city': 'Austin', 'state': 'TX', 'zip': '78701', 'country': 'USA'}}},
            ),
            # Add new credit card payment method
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '2053'},
            ),
            # Get all pending orders and update them with the new address and payment method
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', 'status': 'pending'}, 'required_fields': ['order_id']},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W8770097', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W5183325', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W3913498', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', 'status': 'pending'}, 'update_params': {'address': {'address1': '825 Main Street', 'address2': 'Apt 12B', 'city': 'Austin', 'state': 'TX', 'zip': '78701', 'country': 'USA'}}},
            ),
        ],
        outputs=[],
    ),

    # Task 041: Noah Brown wants to add a new payment method and place an order
    Task(
        annotator="0",
        user_id="task_041",
        instruction="You are helping customer Noah Brown (zip 80279) who wants to add a PayPal payment method and then place an order for Running Shoes (size 10, white) using his paypal. To ensure he recieves tem soon, you create tracking for the order with 'express' delivery option, using QuickShip Logistics.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'noah_brown_6181'}, 'required_fields': ['address', 'payment_methods', 'name', 'email']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'noah_brown_6181', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['1775591963'], 'payment_method_id': 'paypal_6181'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'QuickShip Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['1775591963'], 'courier_id': '#COU0002', 'delivery_option': 'express'},
            ),
        ],
        outputs=[],
    ),

    # Task 042: Anya Garcia wants to check product availability and stock levels
    Task(
        annotator="0",
        user_id="task_042",
        instruction="You are helping user Anya Garcia (zip 19036) who is interested in purchasing a Laptop. She wants to add $3000 to her gift card, using her credit card, and then check if she can afford the laptop with 17-inch screen and the i9 processor using that gift card balance. If she can, you help her and place the order.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            # Check the has a gift card balance
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['payment_methods']},
            ),
            # Add money to the gift card
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'anya_garcia_3271', 'gift_card_id': 'gift_card_4374071', 'payment_method_id': 'credit_card_8955149', 'amount': 3000.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['variants']},
            ),
            # create order
            Action(
                name="create_order",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['3265035808'], 'payment_method_id': 'gift_card_4374071'},
            ),
        ],
        outputs=[],
    ),

    # Task 043: Yara Sanchez wants to modify an existing order before shipment
    Task(
        annotator="0",
        user_id="task_043",
        instruction="You are helping customer Fatima Li (zip 94180) who wants to add a Yoga Mat (4mm, blue, PVC) to her existing pending order. Add the item and update the payment to reflect the new total.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Li', 'zip': '94180'},
            ),
            # Get pending order information
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'fatima_li_8519', 'status': 'pending'}, 'required_fields': ['order_id', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Yoga Mat'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W5267498'}, 'update_params': {'items': {'name': 'Yoga Mat', 'product_id':'4635925001', 'item_id': '5586947715', 'price': 92.53, 'options': {'color': 'blue', 'thickness': '4mm', 'material': 'PVC'}}}},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W5267498', 'transaction_type': 'payment', 'payment_info_to_update': {'amount': 466.75+92.53, 'payment_method_id': 'gift_card_4220746'}},
            ),
        ],
        outputs=[],
    ),

    # Task 044: Ivan Santos reports a delivery issue and needs tracking information
    Task(
        annotator="0",
        user_id="task_044",
        instruction="You are helping user Ivan Santos (zip 75277) says he has an order that is marked as delivered but he never received it. You should help him get a refund by returning all items in the order. Then create a new order for the same items. Create a new gift card for Ivan to use for the refund and the new order so he has no issues with payment. Also add $100 to the gift card as compensation for the inconvenience, and you should check the gift card balance throughout the transactions.",
        actions=[
            # Get user ID from full name and zip
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            # Get order information
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', 'status': 'delivered'}, 'required_fields': ['order_id', 'items']},
            ),
            # Create a new gift card for the refund
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            # Process the return for all items in the order
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487', '1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods']},
            ),
            # Create a new order for the same items
            Action(
                name="create_order",
                kwargs={'user_id': 'ivan_santos_6635', 'item_ids': ['5206946487', '1646531091'], 'payment_method_id': 'gift_card_6635'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods']},
            ),
            # Add $100 to the gift card as compensation
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id':'ivan_santos_6635'}, 'update_params': {'payment_methods': { 'gift_card_6635': {'balance': 100.0} } } },
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods']},
            ),
        ],
        outputs=[],
    ),

    # Task 045: Multiple users - Noah Brown wants to gift an item to Anya Garcia
    Task(
        annotator="0",
        user_id="task_045",
        instruction="You are helping customer Noah Brown (zip 80279) to purchase a Smart Thermostat (item ID 7747408585) as a gift for anya_garcia_3271. You should ship it to Anya's address but charge Noah's credit card credit_card_7815826. You should also create tracking for the order with 'next-day' delivery option using QuickShip Logistics.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['7747408585'], 'payment_method_id': 'credit_card_7815826'}
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['address']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {"address": {
                "address1": "615 Laurel Lane",
                "address2": "Suite 552",
                "city": "Philadelphia",
                "country": "USA",
                "state": "PA",
                "zip": "19036"}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'QuickShip Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['7747408585'], 'courier_id': '#COU0002', 'delivery_option': 'next-day'},
            ),
        ],
        outputs=[],
    ),

    # Task 010: Yara Sanchez wants to return multiple items and process partial refund
    Task(
        annotator="0",
        user_id="task_046",
        instruction="You are helping user Yara Sanchez (zip 75255) who wants to return both the Skateboard (item_id 3877188862) and Bluetooth Speaker (item_id 7597543861) from order #W6015009. She wants to keep the Mechanical Keyboard. You need to process the return and refund to her original payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yara', 'last_name': 'Sanchez', 'zip': '75255'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6015009'}, 'required_fields': ['items', 'payment_history', 'status']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6015009', 'item_ids': ['3877188862', '7597543861'], 'payment_method_id': 'credit_card_5884162'},
            ),
        ],
        outputs=[],
    ),

    # Task 011: Olivia Jackson wants to cancel a pending order and get full refund
    Task(
        annotator="0",
        user_id="task_047",
        instruction="You are helping customer Olivia Jackson (zip 95119) who wants to return the hiking boots and gaming mouse from a recent order. Process full cancellation and refund to her original payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Olivia', 'last_name': 'Jackson', 'zip': '95119'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'olivia_jackson_1219'}, 'required_fields': ['items', 'order_id']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W3168895'}, 'required_fields': ['payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3168895', 'item_ids': ['2648909398', '5796612084'], 'payment_method_id': 'paypal_3999493'},
            ),
        ],
        outputs=[],
    ),

    # Task 012: Ava Nguyen needs help finding her user account using email
    Task(
        annotator="0",
        user_id="task_048",
        instruction="You are a customer service specialist. A customer called saying her name is Ava Nguyen but forgot her user ID. She provided email ava.nguyen3664@example.com. You need to help her find her user id and change her last name to Smith. She also wants to add $1000 to her gift card balance.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'ava.nguyen3664@example.com'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ava_nguyen_2175'}, 'update_params': {'name': {'first_name': 'Ava', 'last_name': 'Smith'}}},
            ),
            # check payment methods
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ava_nguyen_2175'}, 'required_fields': ['payment_methods']},
            ),
            # add money to gift card
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'ava_nguyen_2175', 'gift_card_id': 'gift_card_3324938', 'payment_method_id': 'paypal_6262583', 'amount': 1000.0},
            ),
        ],
        outputs=[{'user_id': 'ava_nguyen_2175'}],
    ),

    # Task 049: Sofia Li wants to exchange laptop for different RAM configuration
    Task(
        annotator="0",
        user_id="task_049",
        instruction="You are helping customer harper_kim_2998 who purchased a laptop but needs more RAM for her work. She wants to exchange her current laptop (8GB RAM) for a 32GB RAM laptop with a 17-inch screen, but she doesn't mind about other properties. She asks you to add her paypal account, and then use that to add $500 to her gift card balance. You then use the gift card to pay for the exchange.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'harper_kim_2998'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'harper_kim_2998'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Laptop'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'harper_kim_2998', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'harper_kim_2998', 'gift_card_id': 'gift_card_5328393', 'payment_method_id': 'paypal_2998', 'amount': 500.0},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W2959713', 'item_ids': ['3265035808'], 'new_item_ids': ['1684786391'], 'payment_method_id': 'gift_card_5328393'},
            ),
        ],
        outputs=[],
    ),

    # Task 014: Emma Brown wants to add gift card and purchase multiple items
    Task(
        annotator="0",
        user_id="task_050",
        instruction="You are helping customer Emma Brown (zip 32165) who received a $500 gift card for her birthday. You help her add it to her account and purchase a coffee maker and water bottle as gifts for her office.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Emma', 'last_name': 'Brown', 'zip': '32165'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_brown_8847'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'emma_brown_8847', 'payment_method_source': 'gift_card', 'balance': 500.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Coffee Maker', 'Water Bottle']}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'emma_brown_8847', 'item_ids': ['1349017811', '5758737025'], 'payment_method_id': 'gift_card_8847'},
            ),
        ],
        outputs=[],
    ),

    # Task 015: Yusuf Khan reports damaged smartphone and needs replacement
    Task(
        annotator="0",
        user_id="task_051",
        instruction="You are helping customer yusuf_khan_7091 who received a laptop that got wet during delivery. You help him to return the damaged item and create a new order for a replacement of the same model.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['orders', 'payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yusuf_khan_7091'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W1787190', 'item_ids': ['2216662955'], 'payment_method_id': 'paypal_5796936'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'yusuf_khan_7091', 'item_ids': ['2216662955'], 'payment_method_id': 'paypal_5796936'},
            ),
        ],
        outputs=[],
    ),

    # Task 052: Amelia Kim wants to purchase items as gifts with different shipping addresses
    Task(
        annotator="0",
        user_id="task_052",
        instruction="You are helping customer amelia_kim_4338 wants to buy a wristwatch for her brother and a backpack for her sister. They all live in different suites of the same building. You need to set the address for the wristwatch order to her brother in Suite 214 and the address for the backpack order to her sister in Suite 523, but you should charge her paypal account.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'amelia_kim_4338'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Wristwatch'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Backpack'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'amelia_kim_4338', 'item_ids': ['2407258246'], 'payment_method_id': 'paypal_1742092'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'amelia_kim_4338', 'item_ids': ['9851293632'], 'payment_method_id': 'paypal_1742092'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address2': 'Suite 214'}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001002'}, 'update_params': {'address': {'address2': 'Suite 523'}}},
            ),
        ],
        outputs=[],
    ),

    # Task 017: Raj Sanchez wants to check product availability before ordering
    Task(
        annotator="0",
        user_id="task_053",
        instruction="You are helping customer Raj Sanchez (zip 92147) who wants to buy a desk lamp and notebook for his home office. Order these items for him, and create tracking with standard delivery using SpeedyShip Couriers. ",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_sanchez_2970'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Desk Lamp', 'Notebook']}, 'required_fields': ['variants', 'supplier_id']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'raj_sanchez_2970', 'item_ids': ['5320792178', '9799386954'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SpeedyShip Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5320792178', '9799386954'], 'courier_id': '#COU0006', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    # Task 054: Chen Silva needs to update shipping address for pending order
    Task(
        annotator="0",
        user_id="task_054",
        instruction="You are helping customer isabella_johansson_2152 who placed an order but realized she provided the wrong address. The order is still pending. You should update the order address to the correct address: 456 New Street, Apt 789, Portland, OR 97201, USA.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'isabella_johansson_2152', 'status': 'pending'}, 'required_fields': ['order_id']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2575533'}, 'update_params': {'address': {'address1': '456 New Street', 'address2': 'Apt 789', 'city': 'Portland', 'state': 'OR', 'zip': '97201', 'country': 'USA'}}},
            ),
        ],
        outputs=[],
    ),

    # Task 019: Aarav Anderson wants to return multiple items and add money to gift card
    Task(
        annotator="0",
        user_id="task_055",
        instruction="You are helping customer Aarav Anderson (zip 19031) who wants to return both a bookshelf and water bottle from his recent order. Instead of getting refunds to his credit card, he has requested that you should add the money to his gift card for future purchases.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Aarav', 'last_name': 'Anderson', 'zip': '19031'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'aarav_anderson_8794'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'aarav_anderson_8794'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3470184', 'item_ids': ['2366567022', '1768466237'], 'payment_method_id': 'gift_card_7245904'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'aarav_anderson_8794'}, 'update_params': {"payment_methods": {"gift_card_7245904": {'balance': 17 + 549.84 + 54.04}}}},
            ),
        ],
        outputs=[],
    ),

    # Task 056: Isabella Sanchez wants to create supply order for low stock items
    Task(
        annotator="0",
        user_id="task_056",
        instruction="You are helping inventory manager isabella_sanchez_2068 who noticed that Running Shoes and Backpacks are running low in stock. You help her create supply orders to replenish inventory from the suppliers (30 units, unit cost of $50 for both shoes and backpack), and update supplier stock to show the reductions. You then help her to order a pair of the same running shoes for herself to her address with zip 85093",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Running Shoes','Backpack']}, 'required_fields': ['supplier_id', 'product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ["#SUP0006", "#SUP0005"]}, 'required_fields': ['supplier_id', 'item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '9791469541', 'quantity': 30, 'unit_cost': 50.0},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0005', 'item_id': '9851293632', 'quantity': 30, 'unit_cost': 50.0},
            ),
            # Update supplier stock
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0006'}, 'update_params': {'item_stock': {'9791469541': 157}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0005'}, 'update_params': {'item_stock': {'9851293632': 90}}},
            ),
            # Get user ID from full name and zip
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Sanchez', 'zip': '85093'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'isabella_sanchez_2068'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'isabella_sanchez_2068', 'item_ids': ['9791469541'], 'payment_method_id': 'paypal_8516781'},
            ),
        ],
        outputs=[],
    ),

    # Task 057: Yara Li wants to exchange defective electric toothbrush
    Task(
        annotator="0",
        user_id="task_057",
        instruction="You are helping customer sofia_thomas_1518 who reports that her electric toothbrush stopped working after 2 days. You need to help her process an exchange for the same model.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_thomas_1518'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'sofia_thomas_1518'}, 'required_fields': ['order_id', 'items', 'status']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Toothbrush'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W7619352', 'item_ids': ['8798690242'], 'new_item_ids': ['8798690242'], 'payment_method_id': 'paypal_5334408'},
            ),
        ],
        outputs=[],
    ),

    # Task 058: Omar Lopez wants to find his account using name and zip code
    Task(
        annotator="0",
        user_id="task_058",
        instruction="You are helping a customer who calls saying his name is Omar Lopez, lives in zip code 90339, but forgot his email and user ID. You also help him add a new credit card (mastercard, last four digits 6789) to his account for future purchases. You then help him test the new card by ordering a pair of white, size 10 running shoes, leather running shoes.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Omar', 'last_name': 'Lopez', 'zip': '90339'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'omar_lopez_3107', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '6789'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Running Shoes'}, 'required_fields': ['variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'omar_lopez_3107', 'item_ids': ['1775591963'], 'payment_method_id': 'credit_card_3107'},
            ),
        ],
        outputs=[],
    ),

    # Task 023: Multiple customers - Noah Brown wants to buy gift for Anya Garcia's birthday
    Task(
        annotator="0",
        user_id="task_059",
        instruction="You are helping customer Noah Brown (zip 80279) who wants to surprise his friend Anya Garcia (zip 19036) for her birthday. You help Noah to buy Anya a smart watch and change the order address to be Anya's address.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'noah_brown_6181'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Smart Watch'}, 'required_fields': ['variants', 'product_id']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['2860956907'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {"address": {
                "address1": "615 Laurel Lane",
                "address2": "Suite 552",
                "city": "Philadelphia",
                "country": "USA",
                "state": "PA",
                "zip": "19036"}}},
            ),
        ],
        outputs=[],
    ),

    # Task 060: Ivan Santos wants to upgrade his PayPal to credit card for better rewards
    Task(
        annotator="0",
        user_id="task_060",
        instruction="You are helping customer ivan_santos_6635 who wants to add a new credit card (visa, last four digits 0235) to his account for better cashback rewards. You also help him to change the payment method for all his pending orders to use the newly added credit card.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods', 'orders']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '0235'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', 'status': 'pending'}, 'required_fields': ['order_id', 'status', 'payment_history']},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W8770097', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W5183325', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W3913498', 'transaction_type': 'payment', 'payment_info_to_update': {'payment_method_id': 'credit_card_6635'}},
            ),
        ],
        outputs=[],
    ),

    # Task 061: Yara Sanchez wants to batch return items from multiple orders
    Task(
        annotator="0",
        user_id="task_061",
        instruction="You are helping customer yara_sanchez_9145 who bought items from multiple orders but changed her mind about several purchases. You help her to return a bluetooth speaker from one order and a bicycle from another order, all to a gift card. If she doesn't have one, you should create it first. You use the gift card to process the returns.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yara_sanchez_9145'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yara_sanchez_9145', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W6519831'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W9102482'}, 'required_fields': ['items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6519831', 'item_ids': ['3624655057'], 'payment_method_id': 'gift_card_9145'},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W9102482', 'item_ids': ['4716977452'], 'payment_method_id': 'gift_card_9145'},
            ),
        ],
        outputs=[],
    ),

    # Task 026: Sofia Li wants to schedule recurring monthly coffee maker filter orders
    Task(
        annotator="0",
        user_id="task_062",
        instruction="You are helping customer sofia_li_9219 who loves doing jigsaw puzzles and she wants to buy one unit of every 1000 piece jigsaw puzzle you have available using her paypal payment method. Due to her impressive love of jigsaw puzzles, you decide to give her a free 2000 piece puzzle (id 5645314103) as a gift. You do this by creating a new order using her paypal and then setting the payment amount to $0",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_9219'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Jigsaw Puzzle'}, 'required_fields': ['variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['3112842858',  '4572024853'], 'payment_method_id': 'paypal_8194385'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['5645314103'], 'payment_method_id': 'paypal_8194385'},
            ),
            Action(
                name="update_payment_history",
                kwargs={'order_id': '#W0001002', 'transaction_type': 'payment', 'payment_info_to_update': {'amount': 0.0}},
            ),
        ],
        outputs=[],
    ),

    # Task 027: Emma Brown reports package theft and needs replacement
    Task(
        annotator="0",
        user_id="task_063",
        instruction="You are helping customer emma_brown_8847 who cancelled an order but realised she actually needed the Hiking Boots that were in it. You need to help her order the boots again, this time use her workplace (address: 123 Office Park, Suite 100, San Francisco, CA, USA, 94105) instead. Use the same payment method for this order.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'emma_brown_8847'}, 'required_fields': ['payment_history', 'items', 'status']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'emma_brown_8847', 'item_ids': ['1262139877'], 'payment_method_id': 'credit_card_8850930'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address1': '123 Office Park', 'address2': 'Suite 100', 'city': 'San Francisco', 'state': 'CA', 'zip': '94105', 'country': 'USA'}}},
            ),
        ],
        outputs=[],
    ),

    # Task 064: Yusuf Khan wants to bulk purchase office supplies for his company
    Task(
        annotator="0",
        user_id="task_064",
        instruction="You are helping customer yusuf_khan_2015 who needs to purchase office supplies in bulk for his company: specifically 50 notebooks, 50 desk lamps, and 5 coffee makers. You help him add his company credit card (visa, ending 0482) and use this to pay for the order. You then create tracking with 'corporate-shipping' option with Express Delivery Services express delivery.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yusuf_khan_2015'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Notebook', 'Desk Lamp', 'Coffee Maker']}, 'required_fields': ['variants']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yusuf_khan_2015', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '0482'},
            ),
            Action(
                name="create_bulk_order",
                kwargs={'user_id': 'yusuf_khan_2015', 'item_ids': {'9799386954':50, '5320792178':50, '1349017811':5}, 'payment_method_id': 'credit_card_2015'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'Express Delivery Services'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['9799386954', '5320792178', '1349017811'], 'courier_id': '#COU0003', 'delivery_option': 'corporate-shipping'},
            ),
        ],
        outputs=[],
    ),

    # Task 065: Amelia Kim wants to check if damaged item is still under warranty
    Task(
        annotator="0",
        user_id="task_065",
        instruction="You are helping customer Mia Garcia (zip 46229) who has a mechanical keyboard from a previous delivered order that she no longer likes. You help her to exchange it for a gaming mouse and use her PayPal account for the transaction.",
        actions=[
            # get user id
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Mia', 'last_name': 'Garcia', 'zip': '46229'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mia_garcia_4516'}, 'required_fields': ['order_id', 'items']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Gaming Mouse'}, 'required_fields': ['variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W5490111', 'item_ids': ['1421289881'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'paypal_9497703'},
            ),
        ],
        outputs=[],
    ),

    # Task 066: Complex supplier relationship management and inventory tracking
    Task(
        annotator="0",
        user_id="task_066",
        instruction="You are an inventory manager. You create supply orders to order 100 of the item with the most stock for multiple suppliers (#SUP0001, #SUP0009, #SUP0011), all with a unit cost of $10. Update supplier item stock showing the reduction quantities after sending the orders.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0001', '#SUP0009', '#SUP0011']}, 'required_fields': ['name', 'products', 'item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '8124970213', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '6324294385', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0011', 'item_id': '8941974610', 'quantity': 100, 'unit_cost': 10.00},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {'8124970213': 99}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'6324294385': 100}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'8941974610': 90}}},
            ),
        ],
        outputs=[],
    ),

    # Task 067: Multi-user order processing with payment method validation
    Task(
        annotator="0",
        user_id="task_067",
        instruction="You are a customer service representative. You help customer Anya Garcia from zip 19036 and Noah Brown from zip 80279 place orders. Anya wants a yoga mat and bluetooth speaker, Noah wants running shoes and a water bottle. You should process both orders, and create tracking for standard shipping using SwiftMove Couriers.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': ['anya_garcia_3271', 'noah_brown_6181']}, 'required_fields': ['name','payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker', 'Running Shoes', 'Water Bottle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'credit_card_8955149'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['9791469541', '5758737025'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5586947715', '2635605237'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001002', 'item_ids': ['9791469541', '5758737025'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    # Task 068: Complex return and exchange workflow with payment adjustments
    Task(
        annotator="0",
        user_id="task_068",
        instruction="You are helping customer Ivan Santos from zip 75277 who wants to return a Garden Hose and exchange a Wireless Earbuds for a tablet in the same delivered order. You also help him to create a gift card then add $200 to it from his PayPal account.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635', "status":"delivered"}, 'required_fields': ['order_id','items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6893533', 'item_ids': ['5206946487'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Tablet'}, 'required_fields': ['variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W6893533', 'item_ids': ['1646531091'], 'new_item_ids': ['2106335193'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ivan_santos_6635', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'ivan_santos_6635', 'gift_card_id': 'gift_card_6635', 'payment_method_id': 'paypal_6151711', 'amount': 200.0},
            ),
        ],
        outputs=[],
    ),

    # Task 069: Customer order for electronics with tracking
    Task(
        annotator="0",
        user_id="task_069",
        instruction="You are helping customer Noah Brown from zip 80279 who wants to order a smartphone and tablet for his business. He prefers to pay with his mastercard ending in 9212. You help him create the order and set up tracking for standard delivery with QuickShip Logistics.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Noah', 'last_name': 'Brown', 'zip': '80279'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'noah_brown_6181'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smartphone', 'Tablet']}, 'required_fields': ['variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'noah_brown_6181', 'item_ids': ['5339029584', '2106335193'], 'payment_method_id': 'credit_card_7815826'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'QuickShip Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5339029584', '2106335193'], 'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    # Task 070: Supply order and inventory management
    Task(
        annotator="0",
        user_id="task_070",
        instruction="You are helping the warehouse manager who needs to create a supply order for 30 units of Coffee Makers (at 182.93 unit cost) from supplier Pet Supplies World due to low inventory. You should reduce the supplier's stock accordingly afterwards.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Coffee Maker'}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0009', 'item_id': '1349017811', 'quantity': 30, 'unit_cost': 182.93},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0009'}, 'update_params': {'item_stock': {'1349017811': 6}}},
            ),
        ],
        outputs=[],
    ),

    # Task 071: Product return and exchange process
    Task(
        annotator="0",
        user_id="task_071",
        instruction="You are helping customer Ivan Santos from zip 75277 who wants to return his Smart Watch and exchange the Skateboard from the same order for a Gaming Mouse. You process both the return and exchange using his PayPal payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Santos', 'zip': '75277'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'ivan_santos_6635'}, 'required_fields': ['order_id', 'items', 'status', 'payment_history']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Gaming Mouse']}, 'required_fields': ['variants']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W3913498', 'item_ids': ['1706622510'], 'payment_method_id': 'paypal_6151711'},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W3913498', 'item_ids': ['5038485381'], 'new_item_ids': ['2880340443'], 'payment_method_id': 'paypal_6151711'},
            ),
        ],
        outputs=[],
    ),

    # Task 072: Customer adding payment method and placing order
    Task(
        annotator="0",
        user_id="task_072",
        instruction="You are helping customer Yusuf Khan from zip 78242 who wants to add a new Visa credit card (last four digits 4321) to his account and then you help him use it to order a Water Bottle and Desk Lamp for his office.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yusuf', 'last_name': 'Khan', 'zip': '78242'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'yusuf_khan_2015', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '4321'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Water Bottle', 'Desk Lamp']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'yusuf_khan_2015', 'item_ids': ['5758737025', '5320792178'], 'payment_method_id': 'credit_card_2015'},
            ),
        ],
        outputs=[],
    ),

    # Task 073: Gift card management and order creation
    Task(
        annotator="0",
        user_id="task_073",
        instruction="You are helping customer Olivia Brown from zip 43118 who wants to add $400 to a new gift card, then order a Backpack and Running Shoes using the gift card balance.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Olivia', 'last_name': 'Brown', 'zip': '43118'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'olivia_brown_4616'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'olivia_brown_4616', 'payment_method_source': 'gift_card', 'balance': 400.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Backpack', 'Running Shoes']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'olivia_brown_4616', 'item_ids': ['9851293632', '9791469541'], 'payment_method_id': 'gift_card_4616'},
            ),
        ],
        outputs=[],
    ),

    # Task 074: Multiple product supply order
    Task(
        annotator="0",
        user_id="task_074",
        instruction="You are helping a customer create supply orders for multiple products: 40 T-Shirts (item id 3799046073) from Tech Supplies Inc., 30 Notebooks (item id 7579176349) from Global Tech Distributors, and 25 Sunglasses (item id 4245201809) from Fashion Forward Supplies. You should set the unit cost to be the same as their price on the product database. You should then update supplier inventories accordingly to show the reductions.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['T-Shirt', 'Notebook', 'Sunglasses']}, 'required_fields': ['variants', 'supplier_id']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0001', '#SUP0002', '#SUP0007']}, 'required_fields': ['name', 'item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0001', 'item_id': '3799046073', 'quantity': 40, 'unit_cost': 53.27},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '7579176349', 'quantity': 30, 'unit_cost': 29.28},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0007', 'item_id': '4245201809', 'quantity': 25, 'unit_cost': 281.48},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0001'}, 'update_params': {'item_stock': {'3799046073': 7}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0002'}, 'update_params': {'item_stock': {'7579176349': 40}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0007'}, 'update_params': {'item_stock': {'4245201809': 142}}},
            ),
        ],
        outputs=[],
    ),

    # Task 075: Customer service with order tracking
    Task(
        annotator="0",
        user_id="task_075",
        instruction="You are customer James Lee from zip 43138 you order a Wristwatch and Action Camera for your photography hobby, but you need to set up a new credit card (visa, last four digits 2039) to pay for them. Set up express delivery with FastTrack Couriers and provide tracking information.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'James', 'last_name': 'Lee', 'zip': '43138'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'james_lee_9638'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wristwatch', 'Action Camera']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'james_lee_9638', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2039'},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'james_lee_9638', 'item_ids': ['2407258246', '6700049080'], 'payment_method_id': 'credit_card_9638'},
            ),
            # find courier_id for FastTrack Couriers
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2407258246', '6700049080'],'courier_id': '#COU0001', 'delivery_option': 'express'},
            ),
        ],
        outputs=[],
    ),

    # Task 076: Database update and user management
    Task(
        annotator="0",
        user_id="task_076",
        instruction="You are helping customer Lucas Johnson from zip 98147 to create an order for a Laptop and E-Reader for his work. Use his existing credit card payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Lucas', 'last_name': 'Johnson', 'zip': '98147'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'lucas_johnson_2067'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'E-Reader']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'lucas_johnson_2067', 'item_ids': ['6017636844', '7609274509'], 'payment_method_id': 'credit_card_3956549'},
            ),
        ],
        outputs=[],
    ),

    # Task 077: Email-based customer lookup and order
    Task(
        annotator="0",
        user_id="task_077",
        instruction="You are helping a customer with email mei.kim7945@example.com who wants to order Yoga Mat and Bluetooth Speaker for her fitness routine. You will use her existing credit card if there is one associated with her account, if not you should add her paypal and use that.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'mei.kim7945@example.com'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'mei_kim_6875'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'mei_kim_6875', 'payment_method_source': 'paypal'}
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'mei_kim_6875', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'paypal_6875'},
            ),
        ],
        outputs=[],
    ),

    # Task 078: Multi-step order and supplier coordination
    Task(
        annotator="0",
        user_id="task_078",
        instruction="You are helping customer Emma Silva from zip 75217 to order Hiking Boots and Fleece Jacket for her outdoor adventures. You should then create tracking for standard delivery with SwiftMove Couriers.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Emma', 'last_name': 'Silva', 'zip': '75217'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_silva_1269'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Hiking Boots', 'Fleece Jacket']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'emma_silva_1269', 'item_ids': ['8277474082', '5992316252'], 'payment_method_id': 'credit_card_4492026'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['8277474082', '5992316252'], 'courier_id': '#COU0004', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    # Task 079: Customer order with international shipping
    Task(
        annotator="0",
        user_id="task_079",
        instruction="You are helping customer Ava Khan from zip 94171 who wants to order a Tablet and Wireless Earbuds. You help Ava add her paypal to her account, which you then use to make any orders. You should create tracking using a courier than can deliver to Mexico, and standard delivery option.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ava', 'last_name': 'Khan', 'zip': '94171'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ava_khan_1840'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Tablet', 'Wireless Earbuds']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'ava_khan_1840', 'payment_method_source': 'paypal'}
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'ava_khan_1840', 'item_ids': ['2106335193', '8555936349'], 'payment_method_id': 'paypal_1840'},
            ),
            # find courier_id for mexico
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'coverage_area': 'Mexico'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2106335193', '8555936349'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),

    # Task 080: Bulk supply order management
    Task(
        annotator="0",
        user_id="task_080",
        instruction="You are head of warehousing and need to restock popular items: you need to create supply orders for 100 Mechanical Keyboards (at $125.99 unit cost) from Sports Gear Suppliers, 80 Water Bottles (500ml, glass, black) at $24.50 unit cost from Office Supplies Hub, and update supplier item stock.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Mechanical Keyboard', 'Water Bottle']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0010', '#SUP0008']}, 'required_fields': ['item_stock', 'contact_info']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0010', 'item_id': '3616838507', 'quantity': 100, 'unit_cost': 125.99},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '8538875209', 'quantity': 80, 'unit_cost': 24.50},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0010'}, 'update_params': {'item_stock': {'3616838507': 62}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'update_params': {'item_stock': {'8538875209': 94}}},
            ),
        ],
        outputs=[],
    ),

    # Task 081: Customer return with refund processing
    Task(
        annotator="0",
        user_id="task_081",
        instruction="You are helping customer Omar Anderson from zip 85011 who wants to return his Desk Lamp and Hiking Boots from a previous order. Process the returns and refund to his PayPal account.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Omar', 'last_name': 'Anderson', 'zip': '85011'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'omar_anderson_5940'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W2091016'}, 'required_fields': ['items']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W2091016', 'item_ids': ['1270145486', '6546364613'], 'payment_method_id': 'paypal_2055565'},
            ),
        ],
        outputs=[],
    ),

    # Task 082: New customer setup and first order
    Task(
        annotator="0",
        user_id="task_082",
        instruction="You are helping customer Liam Wilson from zip 85060 who wants to add a new American Express credit card (last four 8765) and place his first order for a Portable Charger and Indoor Security Camera.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Liam', 'last_name': 'Wilson', 'zip': '85060'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'liam_wilson_3178', 'payment_method_source': 'credit_card', 'brand': 'american_express', 'last_four': '8765'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Portable Charger', 'Indoor Security Camera']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'liam_wilson_3178', 'item_ids': ['1178356107', '8470360507'], 'payment_method_id': 'credit_card_3178'},
            ),
        ],
        outputs=[],
    ),

    # Task 083: Gift card reload and purchase
    Task(
        annotator="0",
        user_id="task_083",
        instruction="You are helping customer Isabella Lopez from zip 85034 who wants to add $250 to her gift card using her mastercard. You help her with this and then help her purchase a Wall Clock and Garden Hose for her home renovation project using the gift card balance.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Isabella', 'last_name': 'Lopez', 'zip': '85034'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'isabella_lopez_6490'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'isabella_lopez_6490', 'gift_card_id': 'gift_card_8245350', 'payment_method_id': 'credit_card_8554680', 'amount': 250.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wall Clock', 'Garden Hose']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'isabella_lopez_6490', 'item_ids': ['9850781806', '9829827210'], 'payment_method_id': 'gift_card_8245350'},
            ),
        ],
        outputs=[],
    ),

    # Task 084: Product exchange workflow
    Task(
        annotator="0",
        user_id="task_084",
        instruction="You are helping customer Mei Kim from zip 77083 who received the wrong type of espresso machine and wants to exchange it for the correct type (item id 3709608322). You also help her to exchange her mechanical keyboard for a different style (item id 3616838507). You should add her credit card (mastercard, last four 3505) as a payment method for the exchanges.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Mei', 'last_name': 'Kim', 'zip': '77083'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'mei_kim_3337'}, 'required_fields': ['order_id', 'payment_history', 'items']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'mei_kim_3337', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '3505'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Espresso Machine', 'Mechanical Keyboard']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W3263208', 'item_ids': ['6324294385','7867398203'], 'new_item_ids': ['3709608322','3616838507'], 'payment_method_id': 'credit_card_3337'},
            ),
        ],
        outputs=[],
    ),

    # Task 085: Supplier coordination and order fulfillment
    Task(
        annotator="0",
        user_id="task_085",
        instruction="You are an inventory specialist. You need to check inventory levels for Tech Haven Supplies, and create supply orders to order a single unit for low-stock items (stock of 2 or less, but ignore out of stock or discontinued items), with a unit cost of $100. Then create customer Anya Garcia's (zip 19036) order for a Yoga Mat and Bluetooth Speaker.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': ['Tech Haven Supplies']}, 'required_fields': ['supplier_id', 'item_stock', 'products']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '5510402676', 'quantity': 1, 'unit_cost': 100},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Anya', 'last_name': 'Garcia', 'zip': '19036'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'anya_garcia_3271'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Bluetooth Speaker']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'anya_garcia_3271', 'item_ids': ['5586947715', '2635605237'], 'payment_method_id': 'credit_card_8955149'},
            ),
        ],
        outputs=[],
    ),

    # Task 086: Customer service with tracking update
    Task(
        annotator="0",
        user_id="task_086",
        instruction="You are a customer service rep helping customer Harper Silva from zip 92188 who placed an order including a Cycling Helmet and wants to upgrade to express shipping with SwiftMove Couriers. You need to update the tracking information to show this.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Harper', 'last_name': 'Silva', 'zip': '92188'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'harper_silva_8534'}, 'required_fields': ['items', 'fulfillments']},
            ),
            # get id for SwiftMove Couriers
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'SwiftMove Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'tracking', 'filter_params': {'tracking_id': '360095850863'}, 'update_params': {'delivery_options': 'express', 'delivery_carrier': '#COU0004'}},
            ),
        ],
        outputs=[],
    ),

    # Task 087: Multi-item order with payment method update
    Task(
        annotator="0",
        user_id="task_087",
        instruction="You are helping customer Chen Silva from zip 46281 who wants to update his payment information by adding a new PayPal account. You then order a Laptop, Gaming Mouse, and Notebook for his work setup using the new payment method.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Chen', 'last_name': 'Silva', 'zip': '46281'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'chen_silva_7485', 'payment_method_source': 'paypal'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'Gaming Mouse', 'Notebook']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'chen_silva_7485', 'item_ids': ['6017636844', '2880340443', '9799386954'], 'payment_method_id': 'paypal_7485'},
            ),
        ],
        outputs=[],
    ),

    # Task 088: Inventory management and customer fulfillment
    Task(
        annotator="0",
        user_id="task_088",
        instruction="You are a warehouse manager who needs to create supply order of Bluetooth Speakers from Home Essentials Co. Due to high demand, the supply order should select the variant with the highest stock, and should order 90 units for $90 unit cost. You then need to create an order for the same item for customer Evelyn Kovacs from zip 32117.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Bluetooth Speaker'}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            # get the supplier_id for Home Essentials Co.

            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Home Essentials Co.'}, 'required_fields': ['supplier_id', 'item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '7617930199', 'quantity': 90, 'unit_cost': 90},
            ),
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Evelyn', 'last_name': 'Kovacs', 'zip': '32117'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'evelyn_kovacs_6742'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'evelyn_kovacs_6742', 'item_ids': ['7617930199'], 'payment_method_id': 'paypal_7732922'},
            ),
        ],
        outputs=[],
    ),

    # Task 089: Return and reorder workflow
    Task(
        annotator="0",
        user_id="task_089",
        instruction="You are helping a customer Yara Sanchez from zip 75255 who wants to return her problematic skateboard and reorder a new one of the same item along with a Portable Charger with options 5000mAh, USB-C, white. You should process return and create new order.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Yara', 'last_name': 'Sanchez', 'zip': '75255'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'yara_sanchez_1902'}, 'required_fields': ['items', 'payment_history', 'order_id']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W6015009', 'item_ids': ['3877188862'], 'payment_method_id': 'credit_card_5884162'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Skateboard', 'Portable Charger']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'yara_sanchez_1902', 'item_ids': ['7866854614', '3877188862'], 'payment_method_id': 'credit_card_5884162'},
            ),
        ],
        outputs=[],
    ),

    # Task 090: Email lookup and priority order
    Task(
        annotator="0",
        user_id="task_090",
        instruction="You are helping a customer with email aarav.anderson9752@example.com needs urgent delivery of Smart Thermostat and Electric Kettle for his smart home project. You should add a credit card (visa, last four 2512) and use this to pay for the order. You use priority shipping with RapidRoute Logistics.",
        actions=[
            Action(
                name="get_user_id_from_email",
                kwargs={'email': 'aarav.anderson9752@example.com'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'aarav_anderson_8794', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2512'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smart Thermostat', 'Electric Kettle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'aarav_anderson_8794', 'item_ids': ['4953074738', '1240311797'], 'payment_method_id': 'credit_card_8794'},
            ),
            # find courier_id for RapidRoute Logistics
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'RapidRoute Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['4953074738', '1240311797'], 'courier_id': '#COU0005', 'delivery_option': 'priority'},
            ),
        ],
        outputs=[],
    ),

    # Task 055: Supplier relationship and bulk ordering
    Task(
        annotator="0",
        user_id="task_091",
        instruction="You need to coordinate with multiple suppliers: order 120 E-Readers (item id 7609274509) from Tech Haven Supplies, 85 Running Shoes (item id 9635758562) from Home Essentials Co., and update supplier stocks. You should keep the unit cost for the supply orders the same as the item's price on the product database.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['E-Reader', 'Running Shoes']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': ['#SUP0004', '#SUP0006']}, 'required_fields': ['contact_info', 'item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0004', 'item_id': '7609274509', 'quantity': 120, 'unit_cost': 243.40},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0006', 'item_id': '9635758562', 'quantity': 85, 'unit_cost': 148.95},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0004'}, 'update_params': {'item_stock': {'7609274509': 57}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0006'}, 'update_params': {'item_stock': {'9635758562': 35}}},
            ),
        ],
        outputs=[],
    ),

    # Task 056: Customer loyalty program and special order
    Task(
        annotator="0",
        user_id="task_092",
        instruction="You are helping customer Sofia Li from zip 78260 who wants to place a order for Wristwatch and Fleece Jacket, paying with her mastercard. You should create tracking and use white-glove delivery option from courier #COU0001.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Sofia', 'last_name': 'Li', 'zip': '78260'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Wristwatch', 'Fleece Jacket']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'sofia_li_9219'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'sofia_li_9219', 'item_ids': ['2407258246', '5992316252'], 'payment_method_id': 'credit_card_8105988'},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['2407258246', '5992316252'], 'courier_id': '#COU0001', 'delivery_option': 'white_glove'},
            ),
        ],
        outputs=[],
    ),

    # Task 057: Complex order with multiple operations
    Task(
        annotator="0",
        user_id="task_093",
        instruction="You need to process complex order for customer Emma Brown from zip 32165: create a gift card with $900 on it. You help her to order a Yoga Mat and a Wall Clock, pay with her gift card, and arrange standard delivery tracking with couriers #COU0002. You then check supplier stock for Garden Hose (green, 25ft, rubber) and create supply order for 35 units at $15.00 each.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Emma', 'last_name': 'Brown', 'zip': '32165'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'emma_brown_8847'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'emma_brown_8847', 'payment_method_source': 'gift_card', 'balance': 900.0},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Yoga Mat', 'Wall Clock']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'emma_brown_8847', 'item_ids': ['5586947715', '9850781806'], 'payment_method_id': 'gift_card_8847'},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['5586947715', '9850781806'],'courier_id': '#COU0002', 'delivery_option': 'standard'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Garden Hose']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0008'}, 'required_fields': ['item_stock']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0008', 'item_id': '5753502325', 'quantity': 35, 'unit_cost': 15.00},
            ),
        ],
        outputs=[],
    ),

    # Task 058: Customer service escalation with multiple returns
    Task(
        annotator="0",
        user_id="task_094",
        instruction="You are speaking to customer Raj Sanchez from zip 92147 who has quality issues with multiple items. He wants to return the wireless earbuds and exchange the grill for the portable, electric, side burner variant. You then add compensation credit of $25 to his account.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Raj', 'last_name': 'Sanchez', 'zip': '92147'},
            ),
            # get his order info
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'user_id': 'raj_sanchez_2970'}, 'required_fields': ['order_id', 'items', 'payment_history']},
            ),
            Action(
                name="process_item_return",
                kwargs={'order_id': '#W1067251', 'item_ids': ['6452271382'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Grill'}, 'required_fields': ['variants']},
            ),
            Action(
                name="process_item_exchange",
                kwargs={'order_id': '#W1067251', 'item_ids': ['7848293342'], 'new_item_ids': ['3876764226'], 'payment_method_id': 'credit_card_3362387'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_sanchez_2970'}, 'required_fields': ['orders', 'payment_methods']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'raj_sanchez_2970'}, 'update_params': {'payment_methods': {'gift_card_2259499': {'balance': 55.00}}}},
            ),
        ],
        outputs=[],
    ),

    # Task 059: Seasonal inventory preparation
    Task(
        annotator="0",
        user_id="task_095",
        instruction="You should prepare for seasonal demand: create large supply orders for 150 Fleece Jackets (item id 5992316252) from Kitchen Essentials Co., 50 Hiking Boots (item id 2658930189) from Global Tech Distributors, each with a unit cost of $50. You should then update pricing on both items in the product database to be $10 less.",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Fleece Jacket', 'Hiking Boots']}, 'required_fields': ['product_id', 'supplier_id', 'variants']},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0012', 'item_id': '5992316252', 'quantity': 150, 'unit_cost': 50},
            ),
            Action(
                name="create_supply_order",
                kwargs={'supplier_id': '#SUP0002', 'item_id': '2658930189', 'quantity': 50, 'unit_cost': 50},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Fleece Jacket']}, 'update_params': {'variants':{'5992316252': {"price": 131.29}}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Hiking Boots']}, 'update_params': {'variants':{'2658930189': {"price": 231.68}}}},
            ),
        ],
        outputs=[],
    ),

    # Task 060: Corporate customer bulk order
    Task(
        annotator="0",
        user_id="task_096",
        instruction="You are a customer service rep helping corporate customer Amelia Nguyen from zip 94113 needs bulk office supplies: 25 Laptops, 50 Notebooks, and 30 Desk Lamps. She wants to setup and pay with a new credit card (visa, last four 2533). Arrange business delivery with QuickShip Logistics.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Amelia', 'last_name': 'Nguyen', 'zip': '94113'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'amelia_nguyen_5209', 'payment_method_source': 'credit_card', 'brand': 'visa', 'last_four': '2533'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Laptop', 'Notebook', 'Desk Lamp']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_bulk_order",
                kwargs={'user_id': 'amelia_nguyen_5209', 'item_ids': {'6017636844':25, '9799386954':50, '5320792178':30}, 'payment_method_id': 'credit_card_5209'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'QuickShip Logistics'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001','item_ids': ['6017636844', '9799386954', '5320792178'], 'courier_id': '#COU0002', 'delivery_option': 'business'},
            ),
        ],
        outputs=[],
    ),

    # Task 097: Customer loyalty program enrollment
    Task(
        annotator="0",
        user_id="task_097",
        instruction="You are helping customer Ivan Rossi from zip 10056 wants to place his first order for Running Shoes and Water Bottle. You should also get his email so you can send confirmation.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Ivan', 'last_name': 'Rossi', 'zip': '10056'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Running Shoes', 'Water Bottle']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'ivan_rossi_9776'}, 'required_fields': ['email', 'payment_methods']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'ivan_rossi_9776', 'item_ids': ['9791469541', '5758737025'], 'payment_method_id': 'credit_card_8621045'},
            ),
        ],
        outputs=[{"email": "ivan.rossi1946@example.com"}],
    ),

    # Task 098: International order with customs handling
    Task(
        annotator="0",
        user_id="task_098",
        instruction="You are helping customer Juan Kim from zip 95120. He wants to order a portable charger (10000mAh, USB-C, blue) and have it delivered to Canada. Create the order then change order address to Lakeview Drive, W 3rd St, Toronto, ON, Canada, M4C 1A1. Then arrange 'international_express' tracking with a suitable courier.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Juan', 'last_name': 'Kim', 'zip': '95120'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'juan_kim_6026'}, 'required_fields': ['payment_methods', 'address']},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Portable Charger']}, 'required_fields': ['variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'juan_kim_6026', 'item_ids': ['7884173033'], 'payment_method_id': 'paypal_5061070'},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'orders', 'filter_params': {'order_id': '#W0001001'}, 'update_params': {'address': {'address1': 'Lakeview Drive', 'address2': 'W 3rd St', 'city': 'Toronto', 'state': 'ON', 'country': 'Canada', 'zip': 'M4C 1A1'}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'coverage_area': 'Canada'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['7884173033'],'courier_id': '#COU0002', 'delivery_option': 'international_express'},
            ),
        ],
        outputs=[],
    ),

    # Task 063: Supplier relationship management and quality control
    Task(
        annotator="0",
        user_id="task_099",
        instruction="You are a quality control officer. Books and More supplier has reported defective Electric Toothbrush batch (variant 1583904702). Complete the required actions. ",
        actions=[
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'name': 'Books and More'}, 'required_fields': ['supplier_id']},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'suppliers', 'filter_params': {'supplier_id': '#SUP0011'}, 'update_params': {'item_stock': {'1583904702':'defective'}}},
            ),
            Action(
                name="update_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': 'Electric Toothbrush'}, 'update_params': {'variants': {'1583904702':{'available':False}}}},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'orders', 'filter_params': {'items':{'item_id': '1583904702'}}, 'required_fields': ['user_id']},
            ),
             Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': ['mia_moore_8366','olivia_ahmed_6778','yusuf_hernandez_5411']}, 'required_fields': ['email']},
            ),
        ],
        outputs=[{ "email": "mia.moore8091@example.com",}, { "email": "olivia.ahmed5620@example.com",}, { "email": "yusuf.hernandez9721@example.com",}],
    ),

    # Task 100: Customer account management and order processing
    Task(
        annotator="0",
        user_id="task_100",
        instruction="You are helping customer Fatima Wilson from zip 78746 who wants to update her account with a new Mastercard (last four 2468), add a gift card, and then separately update her gift card balance by $3000 using the new mastercard, and order Smart Thermostat and Garden Hose for her home improvement project using her gift card. You then expedite the package, by creating a tracking with standard delivery option using FastTrack Couriers.",
        actions=[
            Action(
                name="get_user_id_from_full_name_and_zip",
                kwargs={'first_name': 'Fatima', 'last_name': 'Wilson', 'zip': '78746'},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'fatima_wilson_6873', 'payment_method_source': 'credit_card', 'brand': 'mastercard', 'last_four': '2468'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'users', 'filter_params': {'user_id': 'fatima_wilson_6873'}, 'required_fields': ['payment_methods']},
            ),
            Action(
                name="add_payment_method",
                kwargs={'user_id': 'fatima_wilson_6873', 'payment_method_source': 'gift_card', 'balance': 0.0},
            ),
            Action(
                name="add_money_to_gift_card",
                kwargs={'user_id': 'fatima_wilson_6873', 'gift_card_id': 'gift_card_6873', 'payment_method_id': 'credit_card_6873', 'amount': 3000.0},
            ),
            # take value from give card
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'products', 'filter_params': {'name': ['Smart Thermostat', 'Garden Hose']}, 'required_fields': ['product_id', 'variants']},
            ),
            Action(
                name="create_order",
                kwargs={'user_id': 'fatima_wilson_6873', 'item_ids': ['9829827210', '4953074738'], 'payment_method_id': 'gift_card_6873'},
            ),
            Action(
                name="get_info_from_db",
                kwargs={'database_name': 'couriers', 'filter_params': {'name': 'FastTrack Couriers'}, 'required_fields': ['courier_id']},
            ),
            Action(
                name="create_tracking",
                kwargs={'order_id': '#W0001001', 'item_ids': ['9829827210', '4953074738'], 'courier_id': '#COU0001', 'delivery_option': 'standard'},
            ),
        ],
        outputs=[],
    ),
]
