from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="campaign_manager",
        user_id="TASK_95",
        instruction="You are launching a seasonal campaign. Search for Running Shoes products, create a promotional campaign 'Spring Running Season' with 30% discount, get top selling products in this category, update the price of the expensive item in this category to $200",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Running Shoes"}),
            Action(name="create_promotional_campaign", kwargs={"campaign_name": "Spring Running Season", "target_category": "Running Shoes", "discount_percentage": 30}),
            Action(name="get_top_selling_products", kwargs={"category": "Running Shoes"}),
            Action(name="update_product_price", kwargs={"product_id": "6938111410", "item_id": "4153505238", "new_price": 200}),

        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_05",
        instruction="You are a quality control manager. Conduct quality control on supply orders. Review all pending supply orders, identify orders with quantities less than 10 units, and increase their quantities to 25 for quality samplin and verify the increase. Update supply order #SO6035 quantity to 65 units. Then get updated supply order details and check if the supplier has sufficient stock levels for pending order #SO6035.",
        actions=[
            Action(name="list_supply_orders_by_status", kwargs={"status": "pending"}),
            Action(name="update_supply_order_quantity", kwargs={"supply_order_id": "#SO5993", "new_quantity": 25}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="update_supply_order_quantity", kwargs={"supply_order_id": "#SO6035", "new_quantity": 65}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_06",
        instruction="You are a product manager. Setting up supply chain for a new product launch. Check the top-selling products to understand market trends. Focus on the Laptop category, get details for the most expensive laptop variant, update its price to $3200 for premium positioning. Find the supplier info for the laptop and Create a new supply order for 50 units of this premium laptop variant at $2000 cost and verify that the order was placed. Update their contact to the new email: premium@globaltech.com an verify the update",
        actions=[
            Action(name="get_top_selling_products", kwargs={"category": "Laptop"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="update_product_price", kwargs={"product_id": "4760268021", "item_id": "1657832319", "new_price": 3200}),
            Action(name="get_supplier_info", kwargs={"product_id": "4760268021"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "1657832319", "quantity": 50, "unit_cost": 2000}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0002", "email": "premium@globaltech.com"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_auditor",
        user_id="sc_task_20",
        instruction="You are a supply chain analyst. You must conduct a comprehensive supply chain audit across all suppliers. You should Review all suppliers and identify the supplier with most diverse product portfolios, check their order histories. Create supply orders item: 8997785118 (50 units at $1500 each unit), verify the order  and update the supplier email with audit@globaltech.com and verify the update.",
        actions=[
            Action(name="list_all_suppliers", kwargs={}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "8997785118"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "8997785118", "quantity": 50, "unit_cost": 1500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0002", "email": "audit@globaltech.com"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="generator",
        user_id="TASK_80",
        instruction="You are a fulfillment coordinator. Customer 'Ethan Muller' needs urgent delivery of a 15 inch Laptop i7 1TB SSD within the USA. Check delivery estimates for express delivery. Find an courier service and Create a pending order for him and assign the fastest available courier.",
        actions=[
            Action(name="search_users", kwargs={"name": "Ethan Muller"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="create_pending_order", kwargs={"user_id": "ethan_muller_6097", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_5721095", "shipping_address": {
                                                                          "address1": "668 Spruce Street",
                                                                          "address2": "Suite 237",
                                                                          "city": "Seattle",
                                                                          "country": "USA",
                                                                          "state": "WA",
                                                                          "zip": "98128"
                                                                        }}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="fulfillment_manager",
        user_id="TASK_81",
        instruction="You are a fulfillment manager processing pending orders. Find all pending orders for user 'Sofia Rossi', select order #W5918442, update its status to 'processing', analyze the user and assign it to courier, then update the tracking status to 'dispatched'.",
        actions=[
            Action(name="search_users", kwargs={"name": "Sofia Rossi"}),
            Action(name="get_user_orders", kwargs={"user_id": "sofia_rossi_8776", "status": "pending"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "new_status": "processing"}),
            Action(name="analyze_customer_purchase_history",kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W5918442", "courier_id": "#COU0001"}),
            Action(name="update_tracking_status", kwargs={"tracking_id": "fd520c73", "status": "dispatched"})
        ],
        outputs=[]
    ),


    Task(
        annotator="customer_service_agent",
        user_id="TASK_82",
        instruction="You are handling a comprehensive customer service case for user James Li. Search for his delivered orders, find his most recent completed order #W4435622, process a return for Hiking Boots item due to 'defective product', analyze his complete purchase history, and create recommendations, create a promotional campaign named : Loyal Customer Appreciation for loyal customers discount of 15% for the 'water bottle category' ",
        actions=[
            Action(name="search_users", kwargs={"name": "James Li"}),
            Action(name="get_user_orders", kwargs={"user_id": "james_li_5688", "status": "delivered"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4435622"}),
            Action(name="process_return", kwargs={"order_id": "#W4435622", "item_ids": ["4694984344"], "reason": "defective product"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "james_li_5688"}),
            Action(name="create_recommendations", kwargs={"user_id": "james_li_5688", "preferred_category": "Water Bottle"}),
            Action(name="create_promotional_campaign", kwargs={"campaign_name": "Loyal Customer Appreciation", "target_category": "Water Bottle", "discount_percentage": 15})
        ],
        outputs=[]
    ),

    Task(
        annotator="account_manager",
        user_id="TASK_85",
        instruction="You are managing user accounts. Search for user Ava Moore (ava.moore6020@example.com), update her address to '123 New Street, Austin, TX, 78701, USA', add a new PayPal payment method, get her revenue summary, cancel one item from her pending order, and finally, search for her again to confirm the updates.",
        actions=[
            Action(name="search_users", kwargs={"email": "ava.moore6020@example.com"}),
            Action(name="update_user_address", kwargs={"user_id": "ava_moore_2033", "address": {"address1": "123 New Street", "address2": "", "city": "Austin", "state": "TX", "zip": "78701", "country": "USA"}}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "ava_moore_2033", "payment_method": {"source": "paypal"}}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_user_orders", kwargs={"user_id": "ava_moore_2033", "status": "pending"}),
            Action(name="cancel_order_item", kwargs={"order_id": "#W4135875", "item_id": "7535423717"}),
            Action(name="search_users", kwargs={"email": "ava.moore6020@example.com"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="vendor_manager",
        user_id="TASK_86",
        instruction="You are managing vendor relationships. Get supplier info for Tech Supplies Inc (#SUP0001), check their pending supply orders, update the status of their oldest order to 'completed' and check the stock level of the item in the supply order to verify the stock update, create a new supply order of  200 units at $25 each for their lowest stock, ignore out of stock items, and get all pending orders again to verify changes.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "new_status": "completed"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "9612497925"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9973034634"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 25}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_87",
        instruction="You are analyzing customer behavior. Search for user Sofia Rossi, analyze her purchase history, you must create recommendations for her in her preferred category and also find top selling products in her preferred category, check express delivery estimates and all couriers delivery options for her location, and create a targeted promotional campaign named: 'Sofia's Action Camera Collection' offering her 20% discount for category Action Camera.",
        actions=[
            Action(name="search_users", kwargs={"name": "Sofia Rossi"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="create_recommendations", kwargs={"user_id": "sofia_rossi_8776", "preferred_category": "Action Camera"}),
            Action(name="get_top_selling_products", kwargs={"category": "Action Camera"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="create_promotional_campaign", kwargs={"campaign_name": "Sofia's Action Camera Collection", "target_category": "Action Camera", "discount_percentage": 20})
        ],
        outputs=[]
    ),


    Task(
        annotator="shipping_coordinator",
        user_id="TASK_88",
        instruction="You are coordinating shipments. Get tracking info for order #W2611340, update its tracking status to 'in_transit', get courier info for the shipment, check delivery estimates, update tracking to 'out_for_delivery', then to 'delivered', and finally update the order status to 'completed'.",
        actions=[
            Action(name="get_tracking_info", kwargs={"order_id": "#W2611340"}),
            Action(name="update_tracking_status", kwargs={"tracking_id": "357962501027", "status": "in_transit"}),
            Action(name="get_courier_info", kwargs={"courier_id": "#COU0003"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="update_tracking_status", kwargs={"tracking_id": "357962501027", "status": "out_for_delivery"}),
            Action(name="update_tracking_status", kwargs={"tracking_id": "357962501027", "status": "delivered"}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "new_status": "completed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="operations_manager",
        user_id="TASK_89",
        instruction="You are processing multiple orders efficiently. You should get the pending orders with limit 5, select top 3 order IDs, update them all to 'processing' status using bulk processing and verify the update by getting their details and assign fulfillment to all of them, get revenue summary by product, and create inventory alerts for items with stock below or equal to 25.",
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "pending", "limit": 5}),
            Action(name="bulk_order_processing", kwargs={"order_ids": ["#W9962383", "#W9933266", "#W9929926"], "new_status": "processing"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9962383"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9933266"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9929926"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W9962383", "courier_id": "#COU0001"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W9933266", "courier_id": "#COU0001"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W9929926", "courier_id": "#COU0001"}),
            Action(name="get_revenue_summary", kwargs={"group_by": "product"}),
            Action(name="inventory_alert", kwargs={"threshold": 25})
        ],
        outputs=[]
    ),

    Task(
        annotator="catalog_manager",
        user_id="TASK_90",
        instruction="You are managing the product catalog. You have to Search for Laptop products under $2500, check availability of the cheapest one, validate order items for it, create a pending order for user olivia_jackson_1219, apply payment to complete it. get estimates for express delivery and assign fulfillment and get the tracking info.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Laptop", "max_price": 2500}),
            Action(name="check_product_availability", kwargs={"item_id": "6017636844"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["6017636844"], "quantities": [1]}),
            Action(name="search_users", kwargs={"user_id": "olivia_jackson_1219"}),
            Action(name="create_pending_order", kwargs={"user_id": "olivia_jackson_1219", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_3999493", "shipping_address": {"address1": "208 Cedar Street", "address2": "Suite 993", "city": "San Jose", "country": "USA", "state": "CA", "zip": "95119"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option":"express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_6017636844"})

        ],
        outputs=[]
    ),

    Task(
        annotator="loyalty_manager",
        user_id="TASK_91",
        instruction="You are managing customer loyalty. You should find user Olivia Jackson, analyze her purchase history and revenue summary, apply a special discount by updating her pending order item: 4953074738 price to $200, adjust the payment and update the status to processing. You must then call the create_recommendations api to create recommendations for the user in Hiking Boots category.",
        actions=[
            Action(name="search_users", kwargs={"name": "Olivia Jackson"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "olivia_jackson_1219"}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "olivia_jackson_1219"}),
            Action(name="get_user_orders", kwargs={"user_id": "olivia_jackson_1219", "status": "pending"}),
            Action(name="update_order_item_price", kwargs={"order_id": "#W6975922", "item_id": "4953074738", "new_price": 200}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#W6975922", "payment_method_id": "paypal_3999493"}),
            Action(name="update_order_status", kwargs={"order_id": "#W6975922", "new_status": "processing"}),
            Action(name="create_recommendations", kwargs={"user_id": "olivia_jackson_1219", "preferred_category": "Hiking Boots"})
        ],
        outputs=[]
    ),


    Task(
        annotator="quality_manager",
        user_id="TASK_92",
        instruction="You are handling quality issues. You should find delivered orders with limit 5, and select the order #W9907310, process returns for multiple items due to 'quality issues', and check updated stock levels, Analyze the customer purchase and create recommendations for the customer in Water Bottle category.",
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "delivered", "limit": 5}),
            Action(name="get_order_details", kwargs={"order_id": "#W9907310"}),
            Action(name="get_supplier_info", kwargs={"product_id": "6819683148"}),
            Action(name="get_supplier_info", kwargs={"product_id": "8560156827"}),
            Action(name="process_return", kwargs={"order_id": "#W9907310", "item_ids": ["5745575001", "8733974883"], "reason": "quality issues"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007", "item_id": "5745575001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0012", "item_id": "8733974883"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "ava_moore_4814"}),
            Action(name="create_recommendations", kwargs={"user_id": "ava_moore_4814", "preferred_category": "Water Bottle"})
        ],
        outputs=[]
    ),



    Task(
        annotator="customer_scenarios",
        user_id="TASK_93",
        instruction="You are Omar Lopez (omar_lopez_3107), You're placing a large order as a long-time customer. Buy 1 T-Shirt and 1 pair of Running Shoes, choosing the least expensive variant for each. Create the order using your PayPal account. Since this is a loyalty purchase, manually adjust the Running Shoes price to $100. Then, get the estimates for express delivery and arrange for courier shipping.",
        actions=[
            Action(name="search_users", kwargs={"name": "Omar Lopez"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "Running Shoes"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8124970213", "9791469541"], "quantities": [1, 1]}),
            Action(name="create_pending_order", kwargs={"user_id": "omar_lopez_3107", "item_details": [{"item_id": "8124970213", "quantity": 1}, {"item_id": "9791469541", "quantity": 1}]}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "item_id": "9791469541", "new_price": 100}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "payment_method_id": "paypal_1530316", "shipping_address": {
            "address1": "959 Broadway",
            "address2": "Suite 363",
            "city": "Los Angeles",
            "country": "USA",
            "state": "CA",
            "zip": "90339"
        }}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="TASK_94",
        instruction="You are Liam Lee with email id: liam.lee9297@example.com dealing with a situation. Check your most recently delivered order with ID:  #W9710999. Return the Electric Toothbrush with reason 'defective product'. Then, browse available Electric Toothbrush to find the expensive one and add a Water Bottle to this new order order the most expensive water bottle. Finally, since this is for personal use, apply for express delivery to your address.",
        actions=[
            Action(name="search_users", kwargs={"email": "liam.lee9297@example.com"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9710999"}),
            Action(name="process_return", kwargs={"order_id": "#W9710999", "item_ids": ["3320557165"], "reason": "defective product"}),
            Action(name="search_products_by_category", kwargs={"category": "Electric Toothbrush"}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8798690242", "3453331371"]}),
            Action(name="create_pending_order", kwargs={"user_id": "liam_lee_5696", "item_details": [{"item_id": "8798690242", "quantity": 1}, {"item_id": "3453331371", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_87986902423453331371", "payment_method_id": "credit_card_5809636", "shipping_address":{
                                                                          "address1": "668 Highland Drive",
                                                                          "address2": "Suite 584",
                                                                          "city": "Fort Worth",
                                                                          "country": "USA",
                                                                          "state": "TX",
                                                                          "zip": "76176"
                                                                        }}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_87986902423453331371", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),
    Task(
        annotator="sales_manager",
        user_id="TASK_97",
        instruction="You are driving sales growth. Find user Raj Li (raj.li3320@example.com), analyze his purchase history, create recommendations based on his preferences, Create recommendations for the user in Smart Thermostat category and Create an order for him a ship it to his adress and use credit card as the payment mode,  for the cheapest thermostat from his recommendations",
        actions=[
            Action(name="search_users", kwargs={"email": "raj.li3320@example.com"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "raj_li_8594"}),
            Action(name="create_recommendations", kwargs={"user_id": "raj_li_8594", "preferred_category": "Smart Thermostat"}),
            Action(name="search_products_by_category", kwargs={"category": "Smart Thermostat"}),
            Action(name="create_pending_order", kwargs={"user_id": "raj_li_8594", "item_details": [{"item_id": "4953074738", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_4953074738", "payment_method_id": "credit_card_3425145", "shipping_address": {
                                                                          "address1": "422 Elm Street",
                                                                          "address2": "Suite 893",
                                                                          "city": "Washington",
                                                                          "country": "USA",
                                                                          "state": "DC",
                                                                          "zip": "20369"
                                                                        }}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_4953074738", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="data_privacy_officer",
        user_id="TASK_98",
        instruction="You are ensuring data privacy compliance. You must search for user Evelyn Kovacs, update her address 505 Cedar Avenue Updated, Suite 539, city: Jacksonville, country: USA, state: FL, zip: 32118 for data accuracy, you should also add a new secure payment method visa credit card ending with 1234, get her complete order history and analyze purchase patterns",
        actions=[
            Action(name="search_users", kwargs={"name": "Evelyn Kovacs"}),
            Action(name="update_user_address", kwargs={"user_id": "evelyn_kovacs_6742", "address": {"address1": "505 Cedar Avenue Updated", "address2": "Suite 539", "city": "Jacksonville", "country": "USA", "state": "FL", "zip": "32118"}}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "evelyn_kovacs_6742", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "1234"}}),
            Action(name="get_user_orders", kwargs={"user_id": "evelyn_kovacs_6742"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "evelyn_kovacs_6742"})
        ],
        outputs=[]
    ),

    Task(
        annotator="integration_specialist",
        user_id="TASK_99",
        instruction="You are integrating orders across channels. Search for Bluetooth Speaker products, create a pending order for a customer harper_brown_7363 with the least expensive variant, validate the order items,  apply payment with paypal, and  get courier info and handle fulfillment assignment.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Bluetooth Speaker"}),
            Action(name="search_users", kwargs={"user_id": "harper_brown_7363"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["7617930199"], "quantities": [1]}),
            Action(name="create_pending_order", kwargs={"user_id": "harper_brown_7363", "item_details": [{"item_id": "7617930199", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_7617930199", "payment_method_id": "paypal_2306935", "shipping_address": {"address1": "723 Park Avenue", "address2": "Suite 802", "city": "Fort Worth", "country": "USA", "state": "TX", "zip": "76112"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_7617930199", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supplier_relations",
        user_id="TASK_96",
        instruction="You are managing supplier relationships. Get info for supplier #SUP0004, check their stock levels for items below 20 units, create supply order of 100 units at $100 each for their lowest stock item and verify the order was placed, ignore out of stock items. update the supply order status to 'confirmed' and update the inventory, check pending orders, and generate an inventory alert for this product 'E-Reader' with a threshold of 20.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0004", "low_stock_threshold": 20}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "5510402676"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0004", "product_id": "3801771308", "item_id": "5510402676", "quantity": 100, "unit_cost": 100}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-5510402676", "new_status": "confirmed"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0004", "item_id": "5510402676", "adjustment": 100}),
            Action(name="inventory_alert", kwargs={"threshold": 20, "category_filter": "E-Reader"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_01",
        instruction="You are a supply chain manager dealing with critical stock shortages.  get all item id's with stock below 50 units for supplier #SUP0001. Identify the most critical item (lowest stock), you can ignore out of stock items. Get detailed supplier information, then create a supply order for 200 units of that critical item at $35 per unit. Check the pending orders, to see the newly created supply order. Update the supply order status to 'confirmed' and check the pending orders again to verify it is not there and that the stock level have been updated.",
        actions=[
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 50}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9973034634"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 35}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-9973034634", "new_status": "confirmed"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634", "adjustment": 200}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_02",
        instruction="You are a performance analyst, Analyze the performance of supplier Global Tech Distributors (#SUP0002). Get their complete supplier information, check all their pending supply orders, and review their order history. update the price of their most expensive laptop to $2800. and order 200 more units of this item with a unit price of $2000. update their contact phone to '+1-800-555-UPDATED'.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="update_product_price", kwargs={"product_id": "4760268021", "item_id": "3334537816", "new_price": 2800}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "3334537816", "quantity": 200, "unit_cost": 2000}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0002", "phone": "+1-800-555-UPDATED", "email": "info@globaltech.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_03",
        instruction="You are a supply chain manager, A critical product availability issue has occurred. Check the stock level of T-shirt item '5253880258' which customers are reporting as out of stock. Investigate its supplier details, current stock levels, and see if there are pending supply orders.  update the inventory to 0 to reflect reality, then create an urgent supply order for 300 units at $25 each, and immediately update its status to 'rush'.",
        actions=[
            Action(name="get_product_by_item_id", kwargs={"item_id": "5253880258"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 0}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 300, "unit_cost": 25}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-5253880258", "new_status": "rush"})

        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_04",
        instruction="You are warehouse manager. Perform a stock rebalancing operation across multiple suppliers. Check stock levels for suppliers #SUP0001, #SUP0002, and #SUP0003. Identify any items with stock below 20 units. For the item with the lowest stock (consider out of stock as stock_level 0), incase of multiple items, use the least id item from each supplier, create supply orders for 150 units each at $30 per unit. Update all suppliers' contact information to include 'PRIORITY SUPPLIER' basically make it as priority@<domain>.com in their email domains.",
        actions=[
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 20}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002", "low_stock_threshold": 20}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0003", "low_stock_threshold": 20}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "2791467853"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "3915604618"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "4410138384"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "4896585277", "item_id": "2791467853", "quantity": 150, "unit_cost": 30}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4794339885", "item_id": "3915604618", "quantity": 150, "unit_cost": 30}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0003", "product_id": "7471004230", "item_id": "4410138384", "quantity": 150, "unit_cost": 30}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0001",  "email": "priority@techsupplies.com"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0002", "email": "priority@globaltech.com"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0003", "email": "priority@initech.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_07",
        instruction="You are an ecommerce customer relations manager, Handle an emergency stock redistribution. A major customer needs immediate supply of T-shirt. Check current stock levels for supplier #SUP0001, identify all T-shirt variants with stock above 100 units. Update inventory for item '1176194968' by reducing it by 50 units (emergency allocation). Create a replenishment supply order for 100 units at $40 each and and verify the order placement",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt", "min_stock": 100}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "1176194968"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "1176194968", "adjustment": -50}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "1176194968"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "1176194968", "quantity": 100, "unit_cost": 40}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),


    Task(
        annotator="5",
        user_id="sc_task_08",
        instruction="You are a warehouse manager. Conduct supplier diversification analysis. Get a complete list of all suppliers, analyze supplier #SUP0004's order history and products. Check their stock levels and Create a new supply order for their cancelled supply order (20 units at $45 each). Update their contact information to phone: +1-800-555-1234",
        actions=[
            Action(name="list_all_suppliers", kwargs={}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_product_details", kwargs={"product_id": "5426915165"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0004", "product_id": "5426915165", "item_id": "9956648681", "quantity": 20, "unit_cost": 45}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0004", "phone": "+1-800-555-1234"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="5",
        user_id="TASK_09",
        instruction="You are an inventory manager, Execute seasonal inventory planning for winter products. Check product availability for seasonal items (Smart Thermostat, Fleece Jacket). Get their supplier information, create supply orders to build up inventory: 75 Smart Thermostats, order their most expensive one at $120 each, and update the price of the most expensive Fleece Jacket to $200 for seasonal premium. Verify the supply order for thermostat and price increase for fleece jacket are properly recorded.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Smart Thermostat"}),
            Action(name="search_products_by_category", kwargs={"category": "Fleece Jacket"}),
            Action(name="get_supplier_info", kwargs={"product_id": "4896585277"}),
            Action(name="get_supplier_info", kwargs={"product_id": "8560156827"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "4896585277", "item_id": "3377900078", "quantity": 75, "unit_cost": 120}),
            Action(name="update_product_price", kwargs={"product_id": "8560156827", "item_id": "7528037711", "new_price": 200}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="search_products_by_category", kwargs={"category": "Fleece Jacket"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_10",
        instruction="You are a supply chain analyst, Perform supply chain cost optimization. Review supplier #SUP0006's products and order history. Reduce the most expensive Running Shoes price to $150, check its stock level and create a supply order for 40 units at cost of $130 each. and check the pending order to verify the order",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_product_details", kwargs={"product_id": "6938111410"}),
            Action(name="update_product_price", kwargs={"product_id": "6938111410", "item_id": "4153505238", "new_price": 150}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "6938111410", "item_id": "4153505238", "quantity": 40, "unit_cost": 130}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    # # SUPPLY CHAIN TASK 11 - Cross-Functional Supply Analysis
    Task(
        annotator="supply_chain_director",
        user_id="sc_task_11",
        instruction="You are an supply chain analyst, you should conduct a comprehensive cross-functional supply analysis and Get product-supplier summary for T-shirts. Analyze the supplier's complete order history, check stock levels across multiple items, and also update the inventory for received shipment of 2 variants with id's 9647292434 - 25 units and id 8349118980 - 30 units and You should also create a strategic supply order for 120 units at premium pricing of $50 each for the least expensive item and verify that that order was placed.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="get_product_supplier_summary", kwargs={"product_id": "9523456873"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9647292434", "adjustment": 25}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "8349118980", "adjustment": 30}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "3234800602", "quantity": 120, "unit_cost": 50}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    # # SUPPLY CHAIN TASK 12 - Vendor Performance Improvement
    Task(
        annotator="vendor_manager",
        user_id="sc_task_12",
        instruction="You are an operation manager, You have to improve vendor performance for Office Supplies Hub (#SUP0008). Review their supplier information, check their product catalog, and analyze current stock levels. Create improvement initiatives by updating product pricing for their most expensive LED Light Bulb to $45.99, and create a  supply order for 60 units at $35 each for that bulb, and updating their contact with new number +1-800-555-0000 and verify the order was placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_product_details", kwargs={"product_id": "2696197613"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="update_product_price", kwargs={"product_id": "2696197613", "item_id": "5570660360", "new_price": 45.99}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0008", "product_id": "2696197613", "item_id": "5570660360", "quantity": 60, "unit_cost": 35}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0008", "phone": "+1-800-555-0000"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0008"})
        ],
        outputs=[]
    ),

    # # SUPPLY CHAIN TASK 13 - Supply Chain Risk Management
    Task(
        annotator="risk_manager",
        user_id="sc_task_13",
        instruction="You are a supply chain risk analyst. Implement supply chain risk management measures. Check product portfolios of #SUP0009, #SUP0010, #SUP0011. For each supplier, get their order history, assess their product diversity,  create risk mitigation supply order of 35 units with a unit price of 28 for the item with lowest stock for the supplier with lowest number of products, ignore out of stock items and verify that the order was placed. update the contact of supplier with lowest product count with email hello@sportsgearsuppliers.com.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "7907773809"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "7907773809", "quantity": 35, "unit_cost": 28}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0010", "email": "hello@sportsgearsuppliers.com"})
        ],
        outputs=[]
    ),

    # SUPPLY CHAIN TASK 14 - Technology Product Lifecycle Management
    Task(
        annotator="product_lifecycle_manager",
        user_id="sc_task_14",
        instruction="You are a tech product lifecycle manager. Manage technology product lifecycle for Electronics suppliers. Focus on Tech Supplies Inc. (#SUP0001) and Global Tech Distributors (#SUP0002). Check their technology products (Digital Camera, Laptop), update pricing for end-of-lifecycle products by reducing the price of the most expensive Digital Camera variant to $2200, and create supply orders for newer technology Laptop item 1684786391 at $1500 of 25 units each item and verify the order",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_details", kwargs={"product_id": "8940227892"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="update_product_price", kwargs={"product_id": "8940227892", "item_id": "9644439410", "new_price": 2200}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "1684786391", "quantity": 25, "unit_cost": 1500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="global_operations_manager",
        user_id="sc_task_15",
        instruction="You are a global supply chain operations manager. Review top 10 selling products across all categories to understand global demand patterns. Focus on the top 3 products, get their supplier information and create strategic supply orders of 100 units each at $100 for White low S size helmet , $42 for jigsaw puzzle animal theme beginner available variant and $350 for bookshelf black glass 5ft variant  per unit price and verify order placement",
        actions=[
            Action(name="get_top_selling_products", kwargs={"limit": 10}),
            Action(name="search_products_by_category", kwargs={"category": "Cycling Helmet"}),
            Action(name="search_products_by_category", kwargs={"category": "Jigsaw Puzzle"}),
            Action(name="search_products_by_category", kwargs={"category": "Bookshelf"}),
            Action(name="get_supplier_info", kwargs={"product_id": "7765186836"}),
            Action(name="get_supplier_info", kwargs={"product_id": "1808611083"}),
            Action(name="get_supplier_info", kwargs={"product_id": "8600330539"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "1596993217", "quantity": 100, "unit_cost": 100}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "9665100170", "quantity": 100, "unit_cost": 42}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "4900661478", "quantity": 100, "unit_cost": 350}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0007"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="emergency_coordinator",
        user_id="sc_task_16",
        instruction="You are a emergency coordinator. A critical supplier (#SUP0007) has experienced disruption. Check their products and stock levels, identify critical items needing immediate attention (out of stock item with the lowest id). Create emergency supply order for that item for Fashion Forward Supplies for 80 units at $250 each , verify the order placement, and once the order is delivered, mark it as delivered and adjust the inventory and the stock levels again",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name ="get_product_by_item_id", kwargs={"item_id": "1111254697"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "1111254697", "quantity": 80, "unit_cost": 250}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-1111254697", "new_status": "delivered"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SOfd520c73-1111254697"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0007", "item_id": "1111254697", "adjustment": 80}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007", "item_id": "1111254697"})
        ],
        outputs=[]
    ),

    # # SUPPLY CHAIN TASK 17 - Strategic Partnership Development
    Task(
        annotator="partnership_manager",
        user_id="sc_task_17",
        instruction="You are a strategic partnership manager. Focus on Supplier #SUP0009 - analyze their product portfolio, order history, and potential for expansion.  Negotiate better pricing by updating the most expensive Tea Kettle variant price to $85, and Create a strategic supply order for 45 units Tea kettle variant with $65 each and verify it.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="search_products_by_category", kwargs={"category": "Tea Kettle"}),
            Action(name="get_product_details", kwargs={"product_id": "9832717871"}),
            Action(name="update_product_price", kwargs={"product_id": "9832717871", "item_id": "9647374798", "new_price": 85}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0009", "product_id": "9832717871", "item_id": "9647374798", "quantity": 45, "unit_cost": 65}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0009"})
        ],
        outputs=[]
    ),


    Task(
        annotator="quality_assurance_manager",
        user_id="sc_task_18",
        instruction="You are a quality assurance specialist. Review Sports Gear Suppliers (#SUP0010) products and quality standards and stock levels. Check their current supply orders, update product pricing of their most expensive cycling helmet item to reflect quality premiums to $250, create quality-focused supply order for the same expensive item for 100 units at $150 each, verify the order and update supplier contact to include quality assurance requirements with email quality@sportsgearsuppliers.com.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_product_details", kwargs={"product_id": "7765186836"}),
            Action(name="update_product_price", kwargs={"product_id": "7765186836", "item_id": "9013366374", "new_price": 250}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "9013366374", "quantity": 100, "unit_cost": 150}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0010", "email": "quality@sportsgearsuppliers.com"})

        ],
        outputs=[]
    ),

    # # SUPPLY CHAIN TASK 19 - Supply Chain Digital Transformation
    Task(
        annotator="digital_transformation_lead",
        user_id="sc_task_19",
        instruction="You are digital consultant. You should Focus on supplier with ID: #SUP0006 to implement digital processes. Analyze their product catalog, particularly Vacuum Cleaners and Bluetooth Speakers, You have received an request from the supplier to Update the price of their item 5967152432 to $299,  and also create technology-enabled supply orders for the item 4602305039 (50 units at $500 each) and item 5967152432 (30 units at $200 each), and update their systems by modifying contact information with new mail digital@homeessentials.com. You should Verify the supply orders and contact updates.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_product_details", kwargs={"product_id": "1762337868"}),
            Action(name="get_product_details", kwargs={"product_id": "4768869376"}),
            Action(name="update_product_price", kwargs={"product_id": "4768869376", "item_id": "5967152432", "new_price": 299}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "1762337868", "item_id": "4602305039", "quantity": 50, "unit_cost": 500}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "5967152432", "quantity": 30, "unit_cost": 200}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0006", "email": "digital@homeessentials.com"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_manager",
        user_id="TASK_21",
        instruction="You are a supply manager with critical stock shortages.  get all item id's with stock below 20 units for supplier #SUP0006, ignore the out of stock items.  Get detailed supplier information, then create a supply order for 150 units of the item with the lowest stock at $2500 per unit. verify the order. Receive the product and change the order status to delivered and update the inventory with the new stock levels",
        actions=[
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0006", "low_stock_threshold": 20}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "4772738468"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "4772738468", "quantity": 150, "unit_cost": 2500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-4772738468", "new_status": "delivered"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468", "adjustment": 150}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_analyst",
        user_id="sc_task_22",
        instruction="You are an analyst for an ecommerce website , Analyze the performance of (#SUP0012). get their info and check all their pending supply orders and history. update the price of their most expensive item to $180. and order 200 more units of this item with a unit price of $100 nad verify the order update their contact phone to '+1-800-555-9100'.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_product_details", kwargs={"product_id": "8560156827"}),
            Action(name="update_product_price", kwargs={"product_id": "8560156827", "item_id": "9385662952", "new_price": 180}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 200, "unit_cost": 100}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0012", "phone": "+1-800-555-9100"})
        ],
        outputs=[]
    ),

    Task(
        annotator="warehouse_operator",
        user_id="sc_task_23",
        instruction="You are a supply chain manager, Check the details of T-shirt item '5253880258' which customers are reporting as out of stock. Investigate its supplier details, current stock levels, and see if there are pending supply orders. If stock is indeed low (under 10), update the inventory to 0 to reflect reality, then create an urgent supply order for 300 units at $25 each, and immediately update its status to 'rush'.",
        actions=[
            Action(name="get_product_by_item_id", kwargs={"item_id": "5253880258"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 0}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 300, "unit_cost": 25}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-5253880258", "new_status": "rush"})

        ],
        outputs=[]
    ),


    Task(
        annotator="inventory_manager",
        user_id="sc_task_24",
        instruction="You are inventory manager. Check stock levels for suppliers #SUP0008, #SUP0006 #SUP0012. Identify any items with stock below 10 units. For the item with the lowest stock from each supplier, ignore out of stock items, create supply orders for 150 units each at $80 per unit. Update all suppliers' contact information to include 'PRIORITY SUPPLIER' basically make it as priority@<domain>.com in their email domains.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0008", "low_stock_threshold": 10}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0006", "low_stock_threshold": 10}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0012", "low_stock_threshold": 10}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9829827210"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "4772738468"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0008", "product_id": "6679515468", "item_id": "9829827210", "quantity": 150, "unit_cost": 80}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "4772738468", "quantity": 150, "unit_cost": 80}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0008",  "email": "priority@officesupplieshub.com"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0006", "email": "priority@homeessentials.com"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0012", "email": "priority@kitchenessentials.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="shipping manager",
        user_id="sc_task_25",
        instruction="You are a shipping control manager. Review the supply orders that are pending and identify orders with quantities less than 10 units, and update their quantities to 50 for better shipping prices. Create a supply order of 150 units at $120 each for item 9385662952 which is out of stock and verify that the order was placed and mapped to the supplier successfully",
        actions=[
            Action(name="list_supply_orders_by_status", kwargs={"status": "pending"}),
            Action(name="update_supply_order_quantity", kwargs={"supply_order_id": "#SO5993", "new_quantity": 50}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9385662952"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 150, "unit_cost": 120}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SOfd520c73-9385662952"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0012"})
        ],
        outputs=[]
    ),


    Task(
        annotator="drop_shipping_manager",
        user_id="sc_task_26",
        instruction="You are a drop shipping manager. Check the top 20 selling products to understand market trends. Focus on the costly items like Espresso Machine and digital camera category, get details for the most expensive variant of espresso and digital camera, Order 20 quantities of the most expensive item among these 2 products at $1500 each. Verify the order and update the supplier contact information to include dropshipping@<domain>.com.",
        actions=[
            Action(name="get_top_selling_products", kwargs={"limit": 20}),
            Action(name="search_products_by_category", kwargs={"category": "Espresso Machine"}),
            Action(name="search_products_by_category", kwargs={"category": "Digital Camera"}),
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="get_product_details", kwargs={"product_id": "8940227892"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0009", "product_id": "4354588079", "item_id": "3951031513", "quantity": 20, "unit_cost": 1500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0009", "email": "dropshipping@petsuppliesworld.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="logistics_coordinator",
        user_id="sc_task_27",
        instruction="You are an ecommerce customer relations manager, You must handle an emergency stock redistribution. A major customer needs immediate supply of Cycling Helmet. You must Check current stock levels for supplier #SUP0010, identify all Cycling Helmet variants with stock above 100 units. Also the supplier has sent a message to update their inventory, as per their message you must Update inventory for item '5537798301' by reducing it by 50 units (emergency allocation) and Create a replenishment supply order for 100 units at $40 each for the same item and Update the supply order status to 'urgent' and verify the stock adjustment.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="search_products_by_category", kwargs={"category": "Cycling Helmet", "min_stock": 100}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301", "adjustment": -50}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "5537798301"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "5537798301", "quantity": 100, "unit_cost": 40}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-5537798301", "new_status": "urgent"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="analyst",
        user_id="sc_task_28",
        instruction="You are a warehouse manager. Get a list of all suppliers, analyze supplier #SUP0007's products and order history. Update their the pending supply order to confirmed as we have received the items and update the inventory. Check the status update and inventory update were successful. Also update their contact information to phone: +1-800-555-1245",
        actions=[
            Action(name="list_all_suppliers", kwargs={}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO4238", "new_status": "confirmed"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO4238"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0007", "item_id": "8018699955", "adjustment": 91}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0007", "phone": "+1-800-555-1245"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="me",
        user_id="sc_task_29",
        instruction="You are an demand manager, Execute seasonal inventory planning for summer season. Check product availability for seasonal items Cotton T-shirt and Air Purifiers. Check if there are any pending orders for purple cottom XL T-shirt, if not create a supply orders to build up inventory: 75 purple Cotton Tshirts of size XL, at $10 each, and update the price of the most expensive Air purifier to $2000 and Verify the supply order and price increase are properly recorded.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "Air Purifier"}),
            Action(name="get_product_details", kwargs={"product_id": "9523456873"}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "8124970213", "quantity": 75, "unit_cost": 10}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_product_price", kwargs={"product_id": "3821016478", "item_id": "8302289002", "new_price": 2000}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"})
        ],
        outputs=[]
    ),

    Task(
        annotator="cost_analyst",
        user_id="sc_task_30",
        instruction="You are a cost specialist analyst, Perform supply chain cost optimization. check supplier #SUP0009's order history and product catalog. and reduce the cost of their most expensive expensive item by $50, check its stock level and create a supply order for 40 units at cost of $1300 each for that item. and check the pending order to verify the order",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="update_product_price", kwargs={"product_id": "4354588079", "item_id": "3951031513", "new_price": 3239.46}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0009", "product_id": "4354588079", "item_id": "3951031513", "quantity": 40, "unit_cost": 1300}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0009"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_director",
        user_id="sc_task_31",
        instruction="You are an supply chain analyst, Perform a thorough cross-functional supply review for Skateboard. Compile a product supplier summary, including the supplier's full order history and current stock levels across all items. Also we received a shipment for item 3098764622, mark that supply order as fulfilled and update the inventory. Along with this prepare a supply order for 120 units of the least expensive Skateboard at $150, confirm that the order has been successfully placed.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Skateboard"}),
            Action(name="get_product_supplier_summary", kwargs={"product_id": "1968349452"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6767"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6767", "new_status": "fulfilled"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0005", "item_id": "3098764622", "adjustment": 39}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0005", "product_id": "1968349452", "item_id": "6843647669", "quantity": 120, "unit_cost": 150}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0005"})
        ],
        outputs=[]
    ),

    Task(
        annotator="vendor_manager",
        user_id="sc_task_32",
        instruction="You are an operation manager, Enhance vendor performance for #SUP0007. Begin by reviewing the supplier profile, product catalog, and current stock levels. Develop improvement measures by adjusting the price of their highest-cost Wristwatch to $2200. Place a supply order for 60 units of that wrist watch at $1500 each, update their contact details to +1-800-555-0110, and confirm that the order has been successfully placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_product_details", kwargs={"product_id": "6066914160"}),
            Action(name="update_product_price", kwargs={"product_id": "6066914160", "item_id": "4510078629", "new_price": 2200}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "6066914160", "item_id": "4510078629", "quantity": 60, "unit_cost": 1500}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0007", "phone": "+1-800-555-0110"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="lifecycle_manager",
        user_id="sc_task_34",
        instruction="You are a product lifecycle manager. Oversee the product lifecycle for suppliers, specifically #SUP0007 and #SUP0008, get their info, products and stock levels. Review their product lines — Bookshelf and Desklamp. reduce the price of the highest-priced Bookshelf to $500 and Place supply order for the Desk lamp variant id: 4385534692 at $100 each 25 units, and confirm that the order has been successfully placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_product_details", kwargs={"product_id": "8600330539"}),
            Action(name="get_product_details", kwargs={"product_id": "6817146515"}),
            Action(name="update_product_price", kwargs={"product_id": "8600330539", "item_id": "1768466237", "new_price": 500}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0008", "product_id": "6817146515", "item_id": "4385534692", "quantity": 25, "unit_cost": 100}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0008"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="global_operations_manager",
        user_id="TASK_35",
        instruction="You are a global supply chain operations manager. Review top 10 selling products across all categories to understand global demand patterns. Focus on the top 3 products, get their supplier information, check availability, and create strategic supply orders of 100 units each at $100 for helmets, $42 for jigsaw puzzles and $350 for bookshelves per unit price. Order the least expensive variant for each product and verify order placement",
        actions=[
            Action(name="get_top_selling_products", kwargs={"limit": 10}),
            Action(name="get_product_supplier_summary", kwargs={"product_id": "7765186836"}),
            Action(name="get_product_supplier_summary", kwargs={"product_id": "1808611083"}),
            Action(name="get_product_supplier_summary", kwargs={"product_id": "8600330539"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "1596993217", "quantity": 100, "unit_cost": 100}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "9665100170", "quantity": 100, "unit_cost": 42}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "8479046075", "quantity": 100, "unit_cost": 350}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0007"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="Supply chain emergency coordinator",
        user_id="sc_task_36",
        instruction="You are a Supply Chain Emergency Coordinator, address the disruption affecting Supplier #SUP0012. Review their product list and current stock levels, identifying any items that are out of stock. For each affected item, create a supply order for 80 units at $50 each and confirm that the order has been placed. Once the shipment arrives, mark the order as delivered, update the inventory records, and adjust stock levels accordingly.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 80, "unit_cost": 50}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SOfd520c73-9385662952", "new_status": "delivered"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SOfd520c73-9385662952"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952", "adjustment": 80}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952"})
        ],
        outputs=[]
    ),

    Task(
        annotator="me",
        user_id="sc_task_37",
        instruction="You are a global supply chain manager, evaluate Supplier #SUP0006 by reviewing their product portfolio, analyzing order history, and assessing opportunities for expansion. Renegotiate terms by adjusting the price of their highest-cost available Bluetooth Speaker variant to $300. Also Place a supply order of 150 units at $150 for variants with stock level as 0 and verify that the order has been successfully placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="search_products_by_category", kwargs={"category": "Bluetooth Speaker"}),
            Action(name="update_product_price", kwargs={"product_id": "4768869376", "item_id": "7751905257", "new_price": 300}),
            Action(name="search_products_by_category", kwargs={"category": "Bluetooth Speaker", "min_stock": 0, "max_stock": 0}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "2635605237", "quantity": 150, "unit_cost": 150}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "1052700637", "quantity": 150, "unit_cost": 150}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "4716977452", "quantity": 150, "unit_cost": 150}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    Task(
        annotator="quality_assurance_manager",
        user_id="sc_task_38",
        instruction="You are a quality assurance specialist. Assess Suppliers #SUP0003 by reviewing their product range, quality standards, and current stock levels. Examine existing supply orders, then update the price of their highest-cost Tablet to $1500 to reflect its quality premium. Place a quality-focused supply order for 100 units of this Tablet variant at $500 each, confirm that the order has been placed, and update the supplier's contact information to include quality assurance requirements at quality@initech.com",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_product_details", kwargs={"product_id": "8024098596"}),
            Action(name="update_product_price", kwargs={"product_id": "8024098596", "item_id": "2235648106", "new_price": 1500}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0003", "product_id": "8024098596", "item_id": "2235648106", "quantity": 100, "unit_cost": 500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0003", "email": "quality@initech.com"})

        ],
        outputs=[]
    ),

    Task(
        annotator="lead",
        user_id="sc_task_39",
        instruction="You are consultant. Work with Fashion Forward Supplies (ID: #SUP0007) to implement enhanced digital processes. Review their product catalog, focusing on Air Purifiers and Headphones. Update the price of the Air Purifier (Item ID: 8302289002) to $499. Place technology-enabled supply orders for Item ID: 3104857380 — 50 units at $300 each — and for Item ID: 8302289002 — 30 units at $300 each. Update their system records by changing the contact email to digital@fashionforward.com, and verify both the supply orders and the contact update.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="search_products_by_category", kwargs={"category": "Air Purifier"}),
            Action(name="search_products_by_category", kwargs={"category": "Headphones"}),
            Action(name="update_product_price", kwargs={"product_id": "3821016478", "item_id": "8302289002", "new_price": 499}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "6992792935", "item_id": "3104857380", "quantity": 50, "unit_cost": 300}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0007", "product_id": "3821016478", "item_id": "8302289002", "quantity": 30, "unit_cost": 300}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0007", "email": "digital@fashionforward.com"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_auditor",
        user_id="sc_task_40",
        instruction="You are a supply chain analyst. Carry out a full supply chain audit across all suppliers. Evaluate each supplier to identify the one with the most diverse product portfolio, review their order history, and apply the audit insights to optimize supply orders. Place an order for Item ID: 8997785118 — 50 units at $1,500 each — confirm the order placement, and update the supplier's records with the audit compliance email audit@globaltech.com. Verify that the contact update has been successfully applied.",
        actions=[
            Action(name="list_all_suppliers", kwargs={}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_supplier_order_history", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "8997785118"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "8997785118", "quantity": 50, "unit_cost": 1500}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0002", "email": "audit@globaltech.com"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),



    Task(
        annotator="generator",
        user_id="medium_05_update_address_and_get_delivery_estimate",
        instruction="You are Noah Brown. You've moved to Canada. First, update your address to 123 Maple St, Toronto, ON, M5H 2N2, Canada. Then, check the standard delivery estimate for your new country.",
        actions=[
            Action(name="search_users", kwargs={"name": "Noah Brown"}),
            Action(name="update_user_address", kwargs={"user_id": "noah_brown_6181", "address": {"address1": "123 Maple St", "address2": "", "city": "Toronto", "country": "Canada", "state": "ON", "zip": "M5H 2N2"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Canada", "delivery_option": "standard"})
        ],
        outputs=[]
    ),

    Task(
        annotator="generator",
        user_id="hard_01_full_order_workflow",
        instruction="You are customer Noah Brown. You want to purchase the 15-inch, i7, 32GB RAM, 1TB SSD Laptop (item ID '6017636844'). Create an order, apply your PayPal payment method ('paypal_5727330'), ship to your default address, and assign the best courier for delivery within the USA. What is your final tracking ID?",
        actions=[
            Action(name="search_users", kwargs={"name": "Noah Brown"}),
            Action(name="create_pending_order", kwargs={"user_id": "noah_brown_6181", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_5727330", "shipping_address": {"address1": "986 Sunset Drive", "address2": "Suite 259", "city": "Denver", "country": "USA", "state": "CO", "zip": "80279"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_02_multi_item_return_and_stock_check",
        instruction="You are a returns department manager. A customer, Ava Moore, is returning a 'Water Bottle'  and 'Hiking Boots' from order #W4817420. Process this return for the reason 'no longer needed'. After processing, check the new stock level for the returned hiking boots, which are managed by supplier #SUP0002.",
        actions=[
            Action(name="search_users", kwargs={"name": "Ava Moore"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="process_return", kwargs={"order_id": "#W4817420", "item_ids": ["6777246137", "3812493782"], "reason": "no longer needed"}),
            Action(name="get_supplier_info", kwargs={"product_id": "7363354090"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_03_low_stock_analysis_and_reorder",
        instruction="You are a supply chain director. First, find all items from supplier 'Tech Supplies Inc.' with supplier ID: #SUP0001 that are low on stock (threshold 40) , ignore out of stock items. you should get the supplier info and for each low-stock item, create a new supply order to bring its stock up to 200 units. Assume a unit cost of $30 for each. Verify that the order was placed",
        actions=[
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 40}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "1804581713"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9973034634"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "1804581713", "quantity": 163, "unit_cost": 30}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 164, "unit_cost": 30}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_05_manual_inventory_correction_and_validation",
        instruction="You are an inventory auditor. You've done a physical count and found that for supplier '#SUP0002', item '8997785118' actually has 50 units, not 51. Correct this in the system. Then, to be sure, update the stock of item '4241599783' by an adjustment of +10 units.",
        actions=[
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002", "item_id": "8997785118"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0002", "item_id": "8997785118", "new_stock": 50}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0002", "item_id": "4241599783", "adjustment": 10})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_06_add_payment_and_place_order",
        instruction="You are Anya Garcia. You want to add a new PayPal account to your profile. Then, you want to buy a black, size S, polyester, crew neck T-Shirt. Use your new PayPal account for the purchase and ship to your default address with Express Delivery Services. What is the new order's ID?",
        actions=[
            Action(name="search_users", kwargs={"name": "Anya Garcia"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "anya_garcia_3271", "payment_method": {"source": "paypal"}}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="create_pending_order", kwargs={"user_id": "anya_garcia_3271", "item_details": [{"item_id": "1176194968", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_1176194968", "payment_method_id": "paypal_fd520c73", "shipping_address": {"address1": "615 Laurel Lane", "address2": "Suite 552", "city": "Philadelphia", "country": "USA", "state": "PA", "zip": "19036"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_1176194968", "courier_id": "#COU0003"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_07_price_adjustment_and_recalculation",
        instruction="You are a sales manager. There was a pricing error on a pending order for user 'mei_ahmed_5058', update the price of the Garden Hose in it to $100.00, and then then charge the difference to the user's PayPal account and assign a courier and ship it. Finally, get the updated order details and confirm the new total revenue for this user.",
        actions=[
            Action(name="search_users", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="get_user_orders", kwargs={"user_id": "mei_ahmed_5058", "status": "pending"}),
            Action(name="update_order_item_price", kwargs={"order_id": "#W2631563", "item_id": "5753502325", "new_price": 100.00}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#W2631563", "payment_method_id": "paypal_7160322"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W2631563", "courier_id": "#COU0001"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2631563"}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "mei_ahmed_5058"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_08_resolve_discontinued_stock_issue",
        instruction="You are an inventory specialist. You see that item '5253880258' for supplier '#SUP0001' is 'out_of_stock'. Manually update the stock for '5253880258' to 50 units and verify the update in the supplier information. Then, create a supply order for 100 units of this item from the same supplier at a cost of $25 per unit and verify the order was placed. ",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 50}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "5253880258"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 100, "unit_cost": 25}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_09_cross_border_shipping_coordination",
        instruction="You are a logistics planner. Customer 'Anya Garcia' wants to order a 15inch Laptop i7 1TB SSD to be shipped to Mexico. First, check delivery estimates for Mexico. Then, find a suitable courier. Finally, create a pending order for her, pay using the user's credit card and assign the courier. The order should be for her default US address for now, but the key is courier assignment for the correct destination.",
        actions=[
            Action(name="search_users", kwargs={"name": "Anya Garcia"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Mexico"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "Mexico"}),
            Action(name="create_pending_order", kwargs={"user_id": "anya_garcia_3271", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_8955149", "shipping_address": {"address1": "615 Laurel Lane", "address2": "Suite 552", "city": "Philadelphia", "country": "USA", "state": "PA", "zip": "19036"}}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_01",

        instruction="You are a customer service manager. A customer, James Li, reported that her recent order #W2611340 was delivered, but the Office Chair (item_id: 8426249116) was damaged. You must process a return for only the damaged chair with reason 'Item arrived damaged' and credit her account. Check the stock level for the returned item. Afterwards, check her total spending history to see if she qualifies for a loyalty discount voucher.",
        actions=[
            Action(name="search_users", kwargs={"name": "James Li"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="process_return", kwargs={"order_id": "#W2611340", "item_ids": ["8426249116"], "reason": "Item arrived damaged"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="check_product_availability", kwargs={"item_id": "8426249116"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "8426249116"}),
            Action(name="get_stock_levels", kwargs={"item_id": "8426249116", "supplier_id": "#SUP0002"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "james_li_5688"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_03",
        instruction="You are Noah Brown, You want to change your shipping address. Check if there are orders in pending state. If so cancel them and Update the address to 123 Pine St, Apt 4B, Boulder, CO, 80302, USA. After updating, find the most recent order, check its tracking status, and identify the courier. Finally, find all couriers that deliver to the updated address for future reference and get the delivery estimates for standard and express shipping to the new address.",
        actions=[
            Action(name="search_users", kwargs={"name": "Noah Brown"}),
            Action(name="get_user_orders", kwargs={"user_id": "noah_brown_6181", "status": "pending"}),
            Action(name="update_user_address", kwargs={"user_id": "noah_brown_6181", "address": {"address1": "123 Pine St", "address2": "Apt 4B", "city": "Boulder", "state": "CO", "zip": "80302", "country": "USA"}}),
            Action(name="search_users", kwargs={"user_id": "noah_brown_6181"}),
            Action(name="get_user_orders", kwargs={"user_id": "noah_brown_6181"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#W7678072"}),
            Action(name="get_courier_info", kwargs={"courier_id": "#COU0007"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "standard"})

        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_04",
        instruction="You are a marketing analyst. You must first generate a list of all 'pending' and 'processing' orders in the system to understand the current workload. Then, for a specific user, Ivan Santos (ivan.santos3158@example.com), you should analyze his purchase history to check if Garden hose is among his preferred categories. Based on this category, create a new promotional campaign named campaign1 offering a 15% discount.",
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "pending"}),
            Action(name="get_orders_by_status", kwargs={"status": "processing"}),
            Action(name="search_users", kwargs={"email": "ivan.santos3158@example.com"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "ivan_santos_6635"}),
            Action(name="create_promotional_campaign", kwargs={"campaign_name": "campaign1", "target_category": "Garden Hose", "discount_percentage": 15}),

        ],
        outputs=[]
    ),



    Task(
        annotator="generator_01",
        user_id="high_task_02",

        instruction="You are a supply chain manager, run a critical inventory alert for items with stock below 50 in Cycling Helmet category. For the critical item found with least stock, identify its supplier. Then, check all pending supply orders for that supplier. If there are no pending orders for that specific critical item, you should create a new supply order for 200 units at $25 each. Finally, find if there are any 'cancelled' supply order for that supplier and update its status to 'archived', and get a full revenue summary grouped by product.",
        actions=[
            Action(name="inventory_alert", kwargs={"threshold": 50, "category_filter": "Cycling Helmet"}),

            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="get_product_by_item_id", kwargs={"item_id": "7907773809"}),

            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "7907773809", "quantity": 200, "unit_cost": 25.00}),

            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="list_supply_orders_by_status", kwargs={"supplier_id": "#SUP0010", "status": "cancelled"}),

            Action(name="get_revenue_summary", kwargs={"group_by": "product"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="5",
        user_id="high_task_03",

        instruction="You are a VIP customer executive, one of the customer Ava Moore (ava.moore6020@example.com), wants to cancel the 'Hiking Boots' from her order #W4817420. However, the order is already 'delivered'. You must process a return with the reason 'Item no longer needed'. Then, guide her by analyzing her purchase history to recommend a new pair of boots, checking availability for a specific variant (size 8), and add a new PayPal payment method to her account for the future purchase.",
        actions=[
            Action(name="search_users", kwargs={"email": "ava.moore6020@example.com"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="process_return", kwargs={"order_id": "#W4817420", "item_ids": ["3812493782"], "reason": "Item no longer needed"}),
            Action(name="create_recommendations", kwargs={"user_id": "ava_moore_2033", "preferred_category": "Hiking Boots"}),
            Action(name="search_products_by_category", kwargs={"category": "Hiking Boots"}),
            Action(name="check_product_availability", kwargs={"item_id": "3613716226"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "ava_moore_2033", "payment_method": {"source": "paypal"}}),
        ],
        outputs=[]
    )
    ,

    Task(
        annotator="generator_01",
        user_id="high_task_07",

        instruction="You are a logistics coordinator. A fulfillment for order #W2611340 has been dispatched. Update its tracking status to 'in_transit' and verify the update. Then, find the courier responsible for this delivery. After identifying the courier, check what countries they deliver to. Finally, find all supply orders from supplier #SUP0001 and cancel any that are still 'pending'. Get a revenue summary grouped by product to analyze the impact of these cancellations.",
        actions=[
            Action(name="get_tracking_info", kwargs={"order_id": "#W2611340"}),

            Action(name="update_tracking_status", kwargs={"tracking_id": "357962501027", "status": "in_transit"}),

            Action(name="get_tracking_info", kwargs={"tracking_id": "357962501027"}),

            Action(name="get_courier_info", kwargs={"courier_id": "#COU0003"}),

            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"}),

            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "new_status": "cancelled"}),

            Action(name="get_revenue_summary", kwargs={"group_by": "product"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="high_task_11",

        instruction="You are an operations specialist, Find all orders that are currently 'delivered'. From that list, you take the first two orders, get their details and move them to an 'archived' status using a bulk update. Then, find user 'James Li' and analyze his purchase history. Based on his history, generate new product recommendations for him. Finally, check for any pending supply orders from 'Tech Supplies Inc.' (#SUP0001).",
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "delivered"}),

            Action(name="get_order_details", kwargs={"order_id": "#W9994227"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9980894"}),
            Action(name="bulk_order_processing", kwargs={"order_ids": ["#W9994227", "#W9980894"], "new_status": "archived"}),
            Action(name="search_users", kwargs={"name": "James Li"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "james_li_5688"}),
            Action(name="create_recommendations", kwargs={"user_id": "james_li_5688", "preferred_category": "Water Bottle"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="high_task_12",

        instruction="You are a customer service agent handling a complex request from 'Ava Moore' (ava.moore6020@example.com). She wants to return the 'Bookshelf' from order #W4817420 due to reason 'Item does not fit'. Process the return. Then, she wants to buy a specific T-shirt (item_id: 9612497925). Create a new pending order for this T-shirt. She also mentions she's moving. Update her address to '999 Lakeview Dr, Austin, TX, 78701, USA'. Finally, check delivery estimates for an express shipment to her new address.",
        actions=[
            Action(name="search_users", kwargs={"email": "ava.moore6020@example.com"}),

            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),

            Action(name="process_return", kwargs={"order_id": "#W4817420", "item_ids": ["4900661478"], "reason": "Item does not fit"}),

            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),

            Action(name="validate_order_items", kwargs={"item_ids": ["9612497925"]}),

            Action(name="create_pending_order", kwargs={"user_id": "ava_moore_2033", "item_details": [{"item_id": "9612497925", "quantity": 1}]}),

            Action(name="update_user_address", kwargs={"user_id": "ava_moore_2033", "address": {"address1": "999 Lakeview Dr", "address2": "", "city": "Austin", "state": "TX", "zip": "78701", "country": "USA"}}),

            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),


        ],
        outputs=[]
    ),

     Task(
        annotator="generator_01",
        user_id="high_task_15",

        instruction="You are a marketing manager planning a campaign for 'Laptops'. First, find all available laptops that cost less than $2700. Then, for the most expensive available laptop on that list, find its supplier. Manually update the inventory for that laptop, adding 20 units. Finally, get a revenue summary grouped by product, search for a user named 'James Li', and analyze his purchase history to create personalized recommendations for him. Also, check the delivery estimate for shipping to Mexico.",
        actions=[
            Action(name="search_products_by_category", kwargs={"category": "Laptop", "max_price": 2700}),

            Action(name="get_supplier_info", kwargs={"product_id": "4760268021"}),

            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638"}),

            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638", "adjustment": 20}),

            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638"}),

            Action(name="get_revenue_summary", kwargs={"group_by": "product"}),

            Action(name="search_users", kwargs={"name": "James Li"}),

            Action(name="get_user_orders", kwargs={"user_id": "james_li_5688"}),

            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "james_li_5688"}),

            Action(name="create_recommendations", kwargs={"user_id": "james_li_5688", "preferred_category": "Water Bottle"}),

            Action(name="get_delivery_estimate", kwargs={"destination_country": "Mexico"}),

        ],
        outputs=[]
    ),

    # New E-commerce Customer Tasks - Complex Scenarios
    Task(
        annotator="customer_scenarios",
        user_id="bulk_purchase_discount_workflow",
        instruction="You are Sophia Garcia (sophia.garcia9791@example.com),  a business owner buying Office Chairs (item_id: 8426249116). Create the order, apply your gift card payment, but discover the total exceeds your gift card balance ($5). Add a new visa credit card to your account with last 4 digits 1234, then adjust the payment to cover the remaining balance. Ship to your address and assign any courier. Finally, because the customer is a long time user, we user we give a discount and manually adjust one chair's price to $400 to apply a discount, then rebalance the payment.",
        actions=[
            Action(name="search_users", kwargs={"email": "sophia.garcia9791@example.com"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8426249116"], "quantities": [1]}),
            Action(name="create_pending_order", kwargs={"user_id": "sophia_garcia_1101", "item_details": [{"item_id": "8426249116", "quantity": 1}]}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_8426249116", "item_id": "8426249116", "new_price": 400}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_8426249116", "payment_method_id": "gift_card_9450778", "shipping_address": {"address1": "197 Elm Street", "address2": "Suite 737", "city": "San Antonio", "country": "USA", "state": "TX", "zip": "78263"}}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "sophia_garcia_1101", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "1234"}}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#Wfd520c73_8426249116", "payment_method_id": "credit_card_fd520c73"}),
            Action(name="update_order_status", kwargs={"order_id": "#Wfd520c73_8426249116", "new_status": "processing"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_8426249116", "courier_id": "#COU0001"}),
            Action(name="get_order_details", kwargs={"order_id": "#Wfd520c73_8426249116"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="address_change_shipping_crisis",
        instruction="You are Evelyn Wilson moving to a new state to visit someone. You just placed order #W7381650 but realized you need to move urgently and need one item from the order, delivered to the new address address to '456 Ocean Ave, Miami, FL, 33101, USA'.  Cancel Air Purifier item from your order and update your address. Create a new order for the cancelled item to be shipped to your new address as a separate delivery. The rest of the items in the old order can go to your previous address. Track your new order",
        actions=[
            Action(name="search_users", kwargs={"name": "Evelyn Wilson"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7381650"}),
            Action(name="cancel_order_item", kwargs={"order_id": "#W7381650", "item_id": "8302289002"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7381650"}),
            Action(name="update_user_address", kwargs={"user_id": "evelyn_wilson_8460", "address": {"address1": "456 Ocean Ave", "address2": "", "city": "Miami", "state": "FL", "zip": "33101", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "standard"}),
            Action(name="create_pending_order", kwargs={"user_id": "evelyn_wilson_8460", "item_details": [{"item_id": "8302289002", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_8302289002", "payment_method_id": "gift_card_8931217", "shipping_address": {"address1": "456 Ocean Ave", "address2": "", "city": "Miami", "state": "FL", "zip": "33101", "country": "USA"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_8302289002", "courier_id": "#COU0001"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_8302289002"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="international_shipping_complication",
        instruction="You are Noah Patel with email id : noah.patel9232@example.com planning to ship a Laptop (15-inch, i9, 32GB RAM, 512GB SSD) to your friend in Mexico as a gift. Create the order with your PayPal account, but use a special international shipping address: '123 Revolucion Ave, Mexico City, CDMX, 01000, Mexico'. Check the delivery estimate for express. However, after placing the order, you realize the laptop might have import restrictions. Check if there's a similar but cheaper laptop alternative under $2300, cancel the original laptop from your order, and replace it with the alternative and get it shipped with express courier.",
        actions=[
            Action(name="search_users", kwargs={"email": "noah.patel9232@example.com"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["2913673670"]}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Mexico", "delivery_option": "express"}),
            Action(name="create_pending_order", kwargs={"user_id": "noah_patel_1311", "item_details": [{"item_id": "2913673670", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_2913673670", "payment_method_id": "paypal_3720127", "shipping_address": {"address1": "123 Revolucion Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="cancel_order_item", kwargs={"order_id": "#Wfd520c73_2913673670", "item_id": "2913673670"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop", "max_price": 2300}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Mexico", "delivery_option": "express"}),
            Action(name="create_pending_order", kwargs={"user_id": "noah_patel_1311", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_3720127", "shipping_address": {"address1": "123 Revolucion Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "Mexico"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="wedding_shopping_spree_coordination",
        instruction="You are Isabella Lopez (isabella.lopez3271@example.com) preparing for your wedding. You need to buy multiple items: 2 Water Bottles for the bridal party, 1 Smart Thermostat for your new home, and 1 Office Chair for your home office. Order the most expensive options available for each product. Create the order using your credit card ending in 8902. However, you want the thermostat shipped to your new home address '789 Wedding Lane, Austin, TX, 78701, USA' while the other items go to your current address. Split this into two separate orders, manage the payments accordingly, and ensure both get express delivery. Finally, add a PayPal account to your profile for future purchases.",
        actions=[
            Action(name="search_users", kwargs={"email": "isabella.lopez3271@example.com"}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="search_products_by_category", kwargs={"category": "Smart Thermostat"}),
            Action(name="search_products_by_category", kwargs={"category": "Office Chair"}),
            Action(name="create_pending_order", kwargs={"user_id": "isabella_lopez_6490", "item_details": [{"item_id": "3453331371", "quantity": 2}, {"item_id": "4274709903", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_34533313714274709903", "payment_method_id": "credit_card_8897086", "shipping_address": {"address1": "710 Sunset Drive", "address2": "Suite 176", "city": "Phoenix", "country": "USA", "state": "AZ", "zip": "85034"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_34533313714274709903", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="create_pending_order", kwargs={"user_id": "isabella_lopez_6490", "item_details": [{"item_id": "3377900078", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_3377900078", "payment_method_id": "credit_card_8897086", "shipping_address": {"address1": "789 Wedding Lane", "address2": "", "city": "Austin", "state": "TX", "zip": "78701", "country": "USA"}}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_3377900078", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "isabella_lopez_6490", "payment_method": {"source": "paypal"}}),
            Action(name="get_user_orders", kwargs={"user_id": "isabella_lopez_6490", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="tech_enthusiast_upgrade_path",
        instruction="You are Omar Silva (omar.silva4147@example.com), a tech enthusiast looking to upgrade your setup. You want the most expensive available Laptop and Smartphone. However, you first need to check your purchase history to see your total spending, then validate if these items are in stock. Create the order, but realize your gift card ($68) won't cover it. Add a new PayPal account, then carefully adjust the payment to use both the gift card and PayPal, then finalize with express shipping.",
        actions=[
            Action(name="search_users", kwargs={"email": "omar.silva4147@example.com"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "omar_silva_7446"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="search_products_by_category", kwargs={"category": "Smartphone"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["1657832319", "1507389580"]}),
            Action(name="create_pending_order", kwargs={"user_id": "omar_silva_7446", "item_details": [{"item_id": "1657832319", "quantity": 1}, {"item_id": "1507389580", "quantity": 1}]}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "omar_silva_7446", "payment_method": {"source": "paypal"}}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "payment_method_id": "gift_card_5540683", "shipping_address": {"address1": "510 Hickory Lane", "address2": "Suite 712", "city": "San Diego", "country": "USA", "state": "CA", "zip": "92107"}}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "payment_method_id": "paypal_fd520c73"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="family_relocation_shopping",
        instruction="You are Fatima Wilson (fatima.wilson5906@example.com) relocating your family to Seattle. You need to buy items for your new home: 1 Air Purifier, 1 Bookshelf, and 2 Office Chairs. Order the most expensive variants for each product. First, update your address to '100 Seattle Ave, Seattle, WA, 98101, USA'. Create the order and use your credit card. Also, you realize you need express delivery since you're moving in 2 days. Get the express delivery estimates and ship it.  Update the shipping method and verify the tracking information.",
        actions=[
            Action(name="search_users", kwargs={"name": "Fatima Wilson"}),
            Action(name="update_user_address", kwargs={"user_id": "fatima_wilson_6873", "address": {"address1": "100 Seattle Ave", "address2": "", "city": "Seattle", "state": "WA", "zip": "98101", "country": "USA"}}),
            Action(name="search_products_by_category", kwargs={"category": "Air Purifier"}),
            Action(name="search_products_by_category", kwargs={"category": "Bookshelf"}),
            Action(name="search_products_by_category", kwargs={"category": "Office Chair"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8302289002", "1768466237", "4274709903"], "quantities": [1, 1, 2]}),
            Action(name="create_pending_order", kwargs={"user_id": "fatima_wilson_6873", "item_details": [{"item_id": "8302289002", "quantity": 1}, {"item_id": "1768466237", "quantity": 1}, {"item_id": "4274709903", "quantity": 2}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903", "payment_method_id": "credit_card_9557278", "shipping_address": {"address1": "100 Seattle Ave", "address2": "", "city": "Seattle", "state": "WA", "zip": "98101", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="loyalty_customer_large_order",
        instruction="You are Olivia Jackson, a long-time customer making a large purchase. You want to buy 3 T-Shirts, 2 Running Shoes , and 1 Laptop, order the least expensive variant for each product. First analyze your purchase history and revenue summary to see your loyalty status and then Create the order with your PayPal account. Since this is a large order, adjust the laptop price to $2000 as a loyalty discount. get the estimates for express deliver and courier it",
        actions=[
            Action(name="search_users", kwargs={"name": "Olivia Jackson"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "olivia_jackson_1219"}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "olivia_jackson_1219"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "Running Shoes"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8124970213", "9791469541", "6017636844"], "quantities": [3, 2, 1]}),
            Action(name="create_pending_order", kwargs={"user_id": "olivia_jackson_1219", "item_details": [{"item_id": "8124970213", "quantity": 3}, {"item_id": "9791469541", "quantity": 2}, {"item_id": "6017636844", "quantity": 1}]}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "item_id": "6017636844", "new_price": 2000}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "payment_method_id": "paypal_3999493", "shipping_address": {"address1": "208 Cedar Street", "address2": "Suite 993", "city": "San Jose", "country": "USA", "state": "CA", "zip": "95119"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="gift_return_exchange_workflow",
        instruction="You are Sophia Garcia with email id: sophia.garcia1495@example.com dealing with a gift situation. You received a Bookshelf as a gift order with only one item in the order but it's the wrong size/style. Return the Bookshelf with reason 'gift exchange'. Then, browse available Bookshelf to find the expensive one and create a new order for your preferred Bookshelf. However, realize you also want to add a Water Bottle to this new order. Cancel the previous and create a new order to include both items, order the most expensive water bottle. Use your credit card for payment. Finally, since this is for personal use, apply for express delivery to your address.",
        actions=[
            Action(name="search_users", kwargs={"email": "sophia.garcia1495@example.com"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9336725"}),
            Action(name="process_return", kwargs={"order_id": "#W9336725", "item_ids": ["7154215719"], "reason": "gift exchange"}),
            Action(name="search_products_by_category", kwargs={"category": "Bookshelf"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["1768466237"]}),
            Action(name="create_pending_order", kwargs={"user_id": "sophia_garcia_5025", "item_details": [{"item_id": "1768466237", "quantity": 1}]}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="cancel_order_item", kwargs={"order_id": "#Wfd520c73_1768466237", "item_id": "1768466237"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["1768466237", "3453331371"]}),
            Action(name="create_pending_order", kwargs={"user_id": "sophia_garcia_5025", "item_details": [{"item_id": "1768466237", "quantity": 1}, {"item_id": "3453331371", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_17684662373453331371", "payment_method_id": "credit_card_4147840", "shipping_address":{"address1":"418 Park Avenue","address2":"Suite 351","city":"Washington","country":"USA","state":"DC","zip":"20156"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_17684662373453331371", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="subscription_business_bulk_order",
        instruction="You are Yusuf Rossi setting up a subscription box business. You need to purchase in bulk: 10 cotton T-Shirts of size M, 2 least expensive 500ml stainless steel green color Water Bottles. Create this bulk order using your credit card. Since this is for business, negotiate better pricing by reducing each T-shirt to $35 and each Water Bottle to $35. Check if you qualify for any bulk discounts by analyzing the top-selling products. arrange for standard delivery. Track the order to ensure business continuity.",
        actions=[
            Action(name="search_users", kwargs={"name": "Yusuf Rossi"}),
            Action(name="get_top_selling_products", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["9612497925", "7533802601"], "quantities": [10,2]}),
            Action(name="create_pending_order", kwargs={"user_id": "yusuf_rossi_9620", "item_details": [{"item_id": "9612497925", "quantity": 10}, {"item_id": "7533802601", "quantity": 2}]}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "item_id": "9612497925", "new_price": 35}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "item_id": "7533802601", "new_price": 35}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "payment_method_id": "credit_card_9513926", "shipping_address": {"address1": "763 Broadway", "address2": "Suite 135", "city": "Philadelphia", "country": "USA", "state": "PA", "zip": "19122"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "courier_id": "#COU0001"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_96124979257533802601"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="emergency_replacement_order",
        instruction="You are Liam Thomas with email : liam.thomas9081@example.com facing an equipment emergency at work. Your Laptop broke and you need a replacement, order the cheapest one. However, you're traveling and need it shipped to a temporary address: '555 Hotel Drive, Las Vegas, NV, 89101, USA'. Find the cheapest laptop under $2800, create the order with your credit card. Get express delivery estimates and get it shipped. Also, since it's an emergency, you're willing to pay extra of $200 as an expedite fee. Finally, add your PayPal as payment method to the user profile",
        actions=[
            Action(name="search_users", kwargs={"email": "liam.thomas9081@example.com"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop", "max_price": 2800}),
            Action(name="validate_order_items", kwargs={"item_ids": ["6017636844"]}),
            Action(name="create_pending_order", kwargs={"user_id": "liam_thomas_7882", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_6017636844", "item_id": "6017636844", "new_price": 2492.37}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "liam_thomas_7882", "payment_method": {"source": "paypal"}}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_3261838", "shipping_address": {"address1": "555 Hotel Drive", "address2": "", "city": "Las Vegas", "state": "NV", "zip": "89101", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_order_details", kwargs={"order_id": "#Wfd520c73_6017636844"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_6017636844"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="multi_gift_recipient_management",
        instruction="You are Mia Jackson email: mia.jackson5798@example.com organizing holiday gifts for 3 different people. Create separate orders: 1) A Laptop for your brother (ship to '111 Brother St, Detroit, MI, 48201, USA'), 2) Running Shoes for your sister (ship to '222 Sister Ave, Boston, MA, 02101, USA'), and 3) A T-Shirt and Water Bottle combo for your friend (ship to '333 Friend Rd, Portland, OR, 97201, USA'). order the least expensive ones, and Use your gift card for the T-shirt combo if possible otherwise use PayPal, and  PayPal for the laptop. Apply express shipping to all orders and track each one individually.",
        actions=[
            Action(name="search_users", kwargs={"email": "mia.jackson5798@example.com"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="search_products_by_category", kwargs={"category": "Running Shoes"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="create_pending_order", kwargs={"user_id": "mia_jackson_2250", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_2031016", "shipping_address": {"address1": "111 Brother St", "address2": "", "city": "Detroit", "state": "MI", "zip": "48201", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="create_pending_order", kwargs={"user_id": "mia_jackson_2250", "item_details": [{"item_id": "9791469541", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_9791469541", "payment_method_id": "paypal_2031016", "shipping_address": {"address1": "222 Sister Ave", "address2": "", "city": "Boston", "state": "MA", "zip": "02101", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_9791469541", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="create_pending_order", kwargs={"user_id": "mia_jackson_2250", "item_details": [{"item_id": "8124970213", "quantity": 1}, {"item_id": "5758737025", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "payment_method_id": "gift_card_5715854", "shipping_address": {"address1": "333 Friend Rd", "address2": "", "city": "Portland", "state": "OR", "zip": "97201", "country": "USA"}}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "payment_method_id": "paypal_2031016"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_user_orders", kwargs={"user_id": "mia_jackson_2250", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="post_purchase_customer_service",
        instruction="You are Evelyn Davis dealing with a problematic order. You ordered 3 items but only want to return Water Bottle due to 'defective product'. Process the return and get a refund. Then, you want to reorder a replacement water bottle , the most expensive one. Browse available water bottles, create a new order for your preferred replacement, and arrange standard shipping. However, you're moving next month so update your address to '999 New Home Blvd, Seattle, WA, 98199, USA' before finalizing the new order. Also check your overall purchase history to see if you qualify for loyalty benefits.",
        actions=[
            Action(name="search_users", kwargs={"name": "Evelyn Davis"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6798117"}),
            Action(name="process_return", kwargs={"order_id": "#W6798117", "item_ids": ["8538875209"], "reason": "defective product"}),
            Action(name="update_user_address", kwargs={"user_id": "evelyn_davis_7541", "address": {"address1": "999 New Home Blvd", "address2": "", "city": "Seattle", "state": "WA", "zip": "98199", "country": "USA"}}),
            Action(name="search_products_by_category", kwargs={"category": "Water Bottle"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["3453331371"]}),
            Action(name="create_pending_order", kwargs={"user_id": "evelyn_davis_7541", "item_details": [{"item_id": "3453331371", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_3453331371", "payment_method_id": "paypal_9734841", "shipping_address": {"address1": "999 New Home Blvd", "address2": "", "city": "Seattle", "state": "WA", "zip": "98199", "country": "USA"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_3453331371", "courier_id": "#COU0001"}),
            Action(name="analyze_customer_purchase_history", kwargs={"user_id": "evelyn_davis_7541"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="seasonal_inventory_shopping",
        instruction="You are Emma Brown preparing for a home office setup during winter season. You need multiple items but want to check availability first. Browse and validate: 2 Office Chairs, 1 Laptop, 1 Air Purifier, and 1 Smart Thermostat. Order the least expensive options available. If any item is unavailable, find alternatives in the same category. Create the order with your PayPal account.",
        actions=[
            Action(name="search_users", kwargs={"name": "Emma Brown"}),
            Action(name="search_products_by_category", kwargs={"category": "Office Chair"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="search_products_by_category", kwargs={"category": "Air Purifier"}),
            Action(name="search_products_by_category", kwargs={"category": "Smart Thermostat"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["4168944673", "6017636844", "9534205511", "4953074738"], "quantities": [2, 1, 1, 1]}),
            Action(name="create_pending_order", kwargs={"user_id": "emma_brown_8847", "item_details": [{"item_id": "4168944673", "quantity": 2}, {"item_id": "6017636844", "quantity": 1}, {"item_id": "9534205511", "quantity": 1}, {"item_id": "4953074738", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_4168944673601763684495342055114953074738", "payment_method_id": "paypal_9039769", "shipping_address": {"address1": "984 Hickory Lane", "address2": "Suite 834", "city": "Jacksonville", "country": "USA", "state": "FL", "zip": "32165"}}),
            # Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            # Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            # Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_4168944673601763684495342055114953074738", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="social_media_influencer_unboxing",
        instruction="You are Sophia Nguyen (sophia.nguyen1498@example.com), a social media influencer planning unboxing videos. get the top 10 selling products and You need to order products for content creation: 1 premium Laptop (highest priced available), 2 different Smartphones (least 2 priced ones), 1 Action Camera (most expensive one). First check the top-selling products to understand trends. Create the order with PayPal, but since this is for business content, you want premium service - manually increase each price of laptop and smartphone by $50 as 'content creation fee'. After pricing adjustments, rebalance payment and request the express  delivery with courier service. Track the order for content planning.",
        actions=[
            Action(name="search_users", kwargs={"name": "Sophia Nguyen"}),
            Action(name="get_top_selling_products", kwargs={"limit": 10}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="search_products_by_category", kwargs={"category": "Smartphone"}),
            Action(name="search_products_by_category", kwargs={"category": "Action Camera"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["1657832319", "5339029584", "1507389580", "7523669277"]}),
            Action(name="create_pending_order", kwargs={"user_id": "sophia_nguyen_2370", "item_details": [{"item_id": "1657832319", "quantity": 1}, {"item_id": "5339029584", "quantity": 1}, {"item_id": "1507389580", "quantity": 1}, {"item_id": "7523669277", "quantity": 1}]}),
            Action(name="get_order_details", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277"}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "1657832319", "new_price": 2779.32}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "5339029584", "new_price": 1178.99}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "1507389580", "new_price": 1207.86}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "payment_method_id": "paypal_3738584", "shipping_address": {"address1": "464 Main Street", "address2": "Suite 450", "city": "Washington", "country": "USA", "state": "DC", "zip": "20171"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="corporate_account_setup",
        instruction="You are James Kim setting up a corporate account for your startup. You need office supplies: 5 Office Chairs, 3 Laptops. Order the most expensive office chair and the 3 units of the single lowest priced laptop. Create this large corporate order and add a new corporate visa credit card with 9999 as the last 4 digits to your account. Since this is B2B, negotiate volume pricing by reducing office chair price to $350 each and laptop prices to $2000 each. Arrange standard delivery but ensure all items ship to your business address: '777 Startup Lane, Austin, TX, 78702, USA'.",
        actions=[
            Action(name="search_users", kwargs={"name": "James Kim"}),
            Action(name="search_products_by_category", kwargs={"category": "Office Chair"}),
            Action(name="search_products_by_category", kwargs={"category": "Laptop"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["4274709903", "6017636844"], "quantities": [5, 3]}),
            Action(name="create_pending_order", kwargs={"user_id": "james_kim_7213", "item_details": [{"item_id": "4274709903", "quantity": 5}, {"item_id": "6017636844", "quantity": 3}]}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "james_kim_7213", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "9999"}}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "item_id": "4274709903", "new_price": 350}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "item_id": "6017636844", "new_price": 2000}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "payment_method_id": "credit_card_fd520c73", "shipping_address": {"address1": "777 Startup Lane", "address2": "", "city": "Austin", "state": "TX", "zip": "78702", "country": "USA"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="cross_border_family_shopping",
        instruction="You are Ava Nguyen email: ava.nguyen3664@example.com shopping for family members across different countries. You need to create 2 separate international orders: 1) Smartphone to Canada ('100 Maple St, Toronto, ON, M5H 2N2, Canada'), 2) Running Shoes to Mexico ('200 Centro Ave, Mexico City, CDMX, 01000, Mexico'). Order the least expensive variant of each product. First check delivery estimates for international shipping and ship it for Canada and Mexico orders. Track all orders separately and verify international courier assignments.",
        actions=[
            Action(name="search_users", kwargs={"email": "ava.nguyen3664@example.com"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Canada"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "Mexico"}),
            Action(name="search_products_by_category", kwargs={"category": "Smartphone"}),
            Action(name="search_products_by_category", kwargs={"category": "Running Shoes"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["5339029584", "9791469541"]}),
            Action(name="create_pending_order", kwargs={"user_id": "ava_nguyen_2175", "item_details": [{"item_id": "5339029584", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_5339029584", "payment_method_id": "paypal_6262583", "shipping_address": {"address1": "100 Maple St", "address2": "", "city": "Toronto", "state": "ON", "zip": "M5H 2N2", "country": "Canada"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "Canada"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_5339029584", "courier_id": "#COU0002"}),
            Action(name="create_pending_order", kwargs={"user_id": "ava_nguyen_2175", "item_details": [{"item_id": "9791469541", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_9791469541", "payment_method_id": "paypal_6262583", "shipping_address": {"address1": "200 Centro Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="get_courier_info", kwargs={"coverage_area": "Mexico"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_9791469541", "courier_id": "#COU0001"}),
            Action(name="get_user_orders", kwargs={"user_id": "ava_nguyen_2175", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="damaged_shipment_emergency_reorder",
        instruction="You are Lucas Johnson dealing with a shipping disaster. Your order #W7016806 arrived damaged during transit. You need the items urgently for a presentation tomorrow. Return the items Bookshelf and Water Bottle with reason 'shipping damage'. Immediately reorder the same items but arrange for overnight express delivery. Use your credit card for payment. Ship to your work address: '888 Business Plaza, Seattle, WA, 98102, USA'. Track the order. add your gift card as backup payment for future orders",
        actions=[
            Action(name="search_users", kwargs={"name": "Lucas Johnson"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7016806"}),
            Action(name="process_return", kwargs={"order_id": "#W7016806", "item_ids": [ "5758737025", "4894369688"], "reason": "shipping damage"}),
            Action(name="validate_order_items", kwargs={"item_ids": [ "5758737025", "4894369688"]}),
            Action(name="create_pending_order", kwargs={"user_id": "lucas_johnson_2067", "item_details": [{"item_id": "5758737025", "quantity": 1}, {"item_id": "4894369688", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_57587370254894369688", "payment_method_id": "credit_card_3956549", "shipping_address": {"address1": "888 Business Plaza", "address2": "", "city": "Seattle", "state": "WA", "zip": "98102", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_57587370254894369688", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_57587370254894369688"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "lucas_johnson_2067", "payment_method": {"source": "gift_card"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="last_minute_gift_coordination",
        instruction="You are Chen Smith with only 2 hours to arrange a last-minute birthday gift. You need a 6.5-inch black Smartphone and S size roundneck polyster T-Shirt combo delivered today to your friend's address: '123 Birthday Lane, Miami, FL, 33130, USA'. Check product availability, create the order. Since it's extremely urgent, apply emergency pricing by increasing the smartphone price by $300 and T-shirt by $50. you also add the express option to the courier. However, realize your PayPal does not have enough funds, so add your visa credit card with 7777 as the last 4 digits as secondary payment and pay with it.",
        actions=[
            Action(name="search_users", kwargs={"name": "Chen Smith"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "chen_smith_8425", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "7777"}}),
            Action(name="search_products_by_category", kwargs={"category": "Smartphone"}),
            Action(name="search_products_by_category", kwargs={"category": "T-Shirt"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["5339029584", "1176194968"]}),
            Action(name="create_pending_order", kwargs={"user_id": "chen_smith_8425", "item_details": [{"item_id": "5339029584", "quantity": 1}, {"item_id": "1176194968", "quantity": 1}]}),
            Action(name="get_order_details", kwargs={"order_id": "#Wfd520c73_53390295841176194968"}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "item_id": "5339029584", "new_price": 1428.99}),
            Action(name="update_order_item_price", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "item_id": "1176194968", "new_price": 102.88}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "payment_method_id": "credit_card_fd520c73", "shipping_address": {"address1": "123 Birthday Lane", "address2": "", "city": "Miami", "state": "FL", "zip": "33130", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#Wfd520c73_53390295841176194968"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_76",
        instruction="You are Amelia Kim. You want to add a new visa credit card ending with 6798 to your profile. you also want to buy a blue color, S size Cycling Helmet. Use your new credit card for the purchase and ship to your default address with Express Delivery Services. What is the new order's ID?",
        actions=[
            Action(name="search_users", kwargs={"name": "Amelia Kim"}),
            Action(name="add_payment_method_to_user", kwargs={"user_id": "amelia_kim_4338", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "6798"}}),
            Action(name="search_products_by_category", kwargs={"category": "Cycling Helmet"}),
            Action(name="create_pending_order", kwargs={"user_id": "amelia_kim_4338", "item_details": [{"item_id": "5886093635", "quantity": 1}]}),
            Action(name="apply_payment_to_order", kwargs={"order_id": "#Wfd520c73_5886093635", "payment_method_id": "credit_card_fd520c73", "shipping_address":  {
                                                                          "address1": "250 River Road",
                                                                          "address2": "Suite 668",
                                                                          "city": "Charlotte",
                                                                          "country": "USA",
                                                                          "state": "NC",
                                                                          "zip": "28230"
                                                                        }}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#Wfd520c73_5886093635", "courier_id": "#COU0003"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_77",
        instruction="You are a shipping manager. get the list of pending order for user amelia_kim_4338. update their status to processing and get the estimate for express delivery and the couriers who deliver to the address and ship it, also get the total revenue for that user and get the tracking info for the shipped order",
        actions=[
            Action(name="search_users", kwargs={"user_id": "amelia_kim_4338"}),
            Action(name="get_user_orders", kwargs={"user_id": "amelia_kim_4338", "status": "pending"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="update_order_status", kwargs={"order_id": "#W7634667", "new_status": "processing"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W7634667", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7634667"}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "amelia_kim_4338"}),
            Action(name="get_tracking_info", kwargs={"order_id": "#W7634667"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_78",
        instruction="You are a customer service representative. Apply a loyalty discount to a pending order for user 'aarav_santos_2259', reducing the price of the Vacuum Cleaner to $600.00, and process the refund to his paypal account and update the status of the order to processing and get estimates for shipping and assign a courier for shipment. Finally confirm the new total revenue for this user.",
        actions=[
            Action(name="search_users", kwargs={"user_id": "aarav_santos_2259"}),
            Action(name="get_user_orders", kwargs={"user_id": "aarav_santos_2259", "status": "pending"}),
            Action(name="update_order_item_price", kwargs={"order_id": "#W9672333", "item_id": "1345513440", "new_price": 600.00}),
            Action(name="adjust_order_payment", kwargs={"order_id": "#W9672333", "payment_method_id": "paypal_7664977"}),
            Action(name="update_order_status", kwargs={"order_id": "#W9672333", "new_status": "processing"}),
            Action(name="get_courier_info", kwargs={"coverage_area": "USA"}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA"}),
            Action(name="assign_fulfillment_to_order", kwargs={"order_id": "#W9672333", "courier_id": "#COU0001"}),
            Action(name="get_user_revenue_summary", kwargs={"user_id": "aarav_santos_2259"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_79",
        instruction="You are a purchasing manager. You notice that item '9973034634' for supplier '#SUP0001' is running low with only 36 units remaining. Increase the current stock to 100 units to meet demand. Then, create a supply order for 200 units of this item from the same supplier at a cost of $30 per unit to ensure adequate inventory.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_inventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634", "new_stock": 100}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_product_by_item_id", kwargs={"item_id": "9973034634"}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 30}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_101",

        instruction="You are an operations specialist, you locate all orders marked as 'cancelled'. From that list, take the first 3 orders, review their details, and use a bulk update to move them to 'archived' status.",
        actions=[
            Action(name="get_orders_by_status", kwargs={"status": "cancelled"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9978601"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9931224"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9711842"}),
            Action(name="bulk_order_processing", kwargs={"order_ids": ["#W9978601", "#W9931224", "#W9711842"], "new_status": "archived"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="TASK_102",

        instruction="You are a customer service agent handling a complex request from 'Yusuf Gonzalez' (yusuf.gonzalez2399@example.com). He wants to return the 'T-Shirt' from his delivered order due to reason 'Item does not fit'. Process the return. Then, he wants to buy a specific T-shirt (item_id: 8124970213). Create a new pending order for this T-shirt. He also mentions he's moving. Update his address to '999 Lakeview Dr, Austin, TX, 78701, USA'. Finally, check delivery estimates for an express shipment to his new address.",
        actions=[
            Action(name="search_users", kwargs={"email": "yusuf.gonzalez2399@example.com"}),
            Action(name="get_user_orders", kwargs={"user_id": "yusuf_gonzalez_8900", "status":"delivered"}),
            Action(name="get_order_details", kwargs={"order_id": "#W1679211"}),
            Action(name="process_return", kwargs={"order_id": "#W1679211", "item_ids": ["9612497925"], "reason": "Item does not fit"}),
            Action(name="get_order_details", kwargs={"order_id": "#W1679211"}),
            Action(name="validate_order_items", kwargs={"item_ids": ["8124970213"]}),
            Action(name="create_pending_order", kwargs={"user_id": "yusuf_gonzalez_8900", "item_details": [{"item_id": "8124970213", "quantity": 1}]}),
            Action(name="update_user_address", kwargs={"user_id": "yusuf_gonzalez_8900", "address": {"address1": "999 Lakeview Dr", "address2": "", "city": "Austin", "state": "TX", "zip": "78701", "country": "USA"}}),
            Action(name="get_delivery_estimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="5",
        user_id="TASK_103",
        instruction="You are an vendor manager, you have to check the performance for #SUP0003. start by reviewing the supplier profile, product catalog, and current stock levels. Develop improvement measures by adjusting the price of their highest-cost Sneakers to $200. Place a supply order for 60 units of that sneaker variant at $150 each, update their contact details to +1-800-555-0010, and confirm that the order has been successfully placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_product_details", kwargs={"product_id": "7471004230"}),
            Action(name="update_product_price", kwargs={"product_id": "7471004230", "item_id": "9727387530", "new_price": 200}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0003", "product_id": "7471004230", "item_id": "9727387530", "quantity": 60, "unit_cost": 150}),
            Action(name="update_supplier_contact", kwargs={"supplier_id": "#SUP0003", "phone": "+1-800-555-0010"}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0003"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_104",
        instruction="You are a product lifecycle manager. Analyze suppliers #SUP0012 and #SUP0008, get their info, products and stock levels. Review their product lines — Fleece Jacket and Desklamp. reduce the price of the highest-priced Fleece Jacket to $150 and Place supply order for the Desk lamp variant id: 4385534692 at $100 each 25 units, and confirm that the order has been successfully placed.",
        actions=[
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_supplier_info", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="list_products_by_supplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_stock_levels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_product_details", kwargs={"product_id": "8560156827"}),
            Action(name="get_product_details", kwargs={"product_id": "6817146515"}),
            Action(name="update_product_price", kwargs={"product_id": "8560156827", "item_id": "9385662952", "new_price": 150}),
            Action(name="create_supply_order", kwargs={"supplier_id": "#SUP0008", "product_id": "6817146515", "item_id": "4385534692", "quantity": 25, "unit_cost": 100}),
            Action(name="get_pending_supply_orders", kwargs={"supplier_id": "#SUP0008"}),
        ],
        outputs=[]
    )
]
