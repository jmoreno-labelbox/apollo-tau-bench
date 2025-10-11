from tau_bench.types import Action, Task

TASKS = [

    Task(
        annotator="campaign_manager",
        user_id="TASK_95",
        instruction="Initiate a seasonal campaign by searching for Running Shoes products. Develop a promotional campaign titled 'Spring Running Season' offering a 30% discount, identify the top-selling items in this category, and adjust the price of the highest priced item in this category to $200.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Running Shoes"}),
            Action(name="createPromotionalCampaign", kwargs={"campaign_name": "Spring Running Season", "target_category": "Running Shoes", "discount_percentage": 30}),
            Action(name="getTopSellingProducts", kwargs={"category": "Running Shoes"}),
            Action(name="updateProductPrice", kwargs={"product_id": "6938111410", "item_id": "4153505238", "new_price": 200}),

        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_05",
instruction="As a quality control manager, oversee the quality control on supply orders. Analyze all pending supply orders, pinpoint the ones with quantities below 10 units, and raise their quantities to 25 for quality sampling and verify the increment. Amend supply order #SO6035 to a quantity of 65 units. Subsequently, retrieve the updated supply order details and confirm whether the supplier has adequate stock levels for the pending order.",
        actions=[
            Action(name="listSupplyOrdersByStatus", kwargs={"status": "pending"}),
            Action(name="updateSupplyOrderQuantity", kwargs={"supply_order_id": "#SO5993", "new_quantity": 25}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="updateSupplyOrderQuantity", kwargs={"supply_order_id": "#SO6035", "new_quantity": 65}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_06",
        instruction="You are in charge of product management. Handle the setup of the supply chain for an upcoming product launch. Look into the top-selling products to gain insight into market trends. Specifically, address the Laptop category by retrieving information on the most expensive laptop model, then adjust its price to $3200 to reflect a premium positioning. Identify the supplier details for this laptop and initiate a new supply order for 50 units of the premium laptop at a cost of $2000 each, confirming that the order has been successfully placed. Update their email contact to: premium@worldelectronics.com and confirm the change.",
        actions=[
            Action(name="getTopSellingProducts", kwargs={"category": "Laptop"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="updateProductPrice", kwargs={"product_id": "4760268021", "item_id": "1657832319", "new_price": 3200}),
            Action(name="getSupplierInfo", kwargs={"product_id": "4760268021"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "1657832319", "quantity": 50, "unit_cost": 2000}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0002", "email": "premium@worldelectronics.com"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_auditor",
        user_id="sc_task_20",
        instruction="As a supply chain analyst, your task is to coordinate a thorough audit of the supply chain across all suppliers. Examine all suppliers and recognize the one with the most varied product portfolios, then review their order histories. Produce supply orders item: 8997785118 (50 units at $1500 each), make sure the order is verified, and modify the supplier email to audit@worldelectronics.com, ensuring the update is confirmed.",
        actions=[
            Action(name="listAllSuppliers", kwargs={}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getProductByItemId", kwargs={"item_id": "8997785118"}),
            Action(name="getProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "8997785118", "quantity": 50, "unit_cost": 1500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0002", "email": "audit@worldelectronics.com"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="generator",
        user_id="TASK_80",
        instruction="You are a fulfillment coordinator. Customer 'Noah Muller' requires immediate delivery of a 15 inch Laptop i7 1TB SSD within the USA. Look into delivery estimates for express shipping. Locate a courier service and generate a pending order for him, then assign the quickest available courier.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Noah Muller"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="createPendingOrder", kwargs={"user_id": "noah_muller_6097", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_5721095", "shipping_address": {
                                                                          "address1": "668 Spruce Street",
                                                                          "address2": "Suite 237",
                                                                          "city": "Portland",
                                                                          "country": "USA",
                                                                          "state": "OR",
                                                                          "zip": "98128"
                                                                        }}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="fulfillment_manager",
        user_id="TASK_81",
instruction="You are a fulfillment manager handling pending orders. Locate all pending orders for user 'Sofia Russo', identify order #W5918442, update it to 'processing', assess the user, assign a courier, and change the tracking status to 'dispatched'.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Sofia Russo"}),
            Action(name="getUserOrders", kwargs={"user_id": "sofia_russo_8776", "status": "pending"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#W5918442", "new_status": "processing"}),
            Action(name="analyzeCustomerPurchaseHistory",kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W5918442", "courier_id": "#COU0001"}),
            Action(name="updateTrackingStatus", kwargs={"tracking_id": "fd520c73", "status": "dispatched"})
        ],
        outputs=[]
    ),


    Task(
        annotator="customer_service_agent",
        user_id="TASK_82",
instruction="Coordinate an extensive customer service case for user William Li. Investigate his delivered orders, locate his latest completed order # W4435622, process a return for the Hiking Boots item marked as 'defective', review his complete purchase history, and create recommendations. Initiate a promotional campaign named: Loyal Customer Appreciation, providing a 15% discount for loyal customers on the 'water bottle category'.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "William Li"}),
            Action(name="getUserOrders", kwargs={"user_id": "william_li_5688", "status": "delivered"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W4435622"}),
            Action(name="processReturn", kwargs={"order_id": "#W4435622", "item_ids": ["4694984344"], "reason": "defective product"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "william_li_5688"}),
            Action(name="createRecommendations", kwargs={"user_id": "william_li_5688", "preferred_category": "Water Bottle"}),
            Action(name="createPromotionalCampaign", kwargs={"campaign_name": "Loyal Customer Appreciation", "target_category": "Water Bottle", "discount_percentage": 15})
        ],
        outputs=[]
    ),

    Task(
        annotator="account_manager",
        user_id="TASK_85",
        instruction="Administer user accounts. Locate user Raleigh Moore (Raleigh.moore6020@example.com), amend her address to '123 New Street, Houston, NM, 78701, USA', incorporate a new PayPal payment method, review her revenue summary, cancel an item from her pending order, and eventually, search for her once more to verify the updates.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "charlotte.moore6020@example.com"}),
            Action(name="updateUserAddress", kwargs={"user_id": "charlotte_moore_2033", "address": {"address1": "123 New Street", "address2": "", "city": "Houston", "state": "NM", "zip": "78701", "country": "USA"}}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "charlotte_moore_2033", "payment_method": {"source": "paypal"}}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="getUserOrders", kwargs={"user_id": "charlotte_moore_2033", "status": "pending"}),
            Action(name="cancelOrderItem", kwargs={"order_id": "#W4135875", "item_id": "7535423717"}),
            Action(name="searchUsers", kwargs={"email": "charlotte.moore6020@example.com"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="vendor_manager",
        user_id="TASK_86",
instruction="Handle vendor relationships by obtaining supplier details for Tech Supplies Inc (# SUP0001), assess the pending supply orders, mark the oldest order as 'completed', and verify the stock level of the item in the order to ensure it reflects the update. Then, generate a new supply order for 200 units at $25 each for items with the lowest inventory, excluding any items that are out of stock. Fetch all pending orders once more to validate the changes.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "new_status": "completed"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "9612497925"}),
            Action(name="getProductByItemId", kwargs={"item_id": "9973034634"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 25}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_87",
        instruction="Coordinate an analysis of customer behavior by searching for user Sofia Russo, evaluating her purchase history, and generating recommendations for her in her favored category. Additionally, identify the best-selling products within her preferred category, estimate express delivery times, explore all delivery options offered by couriers for her area, and design a targeted promotional campaign titled: 'Sofia's Action Camera Collection', providing her a 20% discount for the Action Camera category.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Sofia Russo"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="createRecommendations", kwargs={"user_id": "sofia_russo_8776", "preferred_category": "Action Camera"}),
            Action(name="getTopSellingProducts", kwargs={"category": "Action Camera"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="createPromotionalCampaign", kwargs={"campaign_name": "Sofia's Action Camera Collection", "target_category": "Action Camera", "discount_percentage": 20})
        ],
        outputs=[]
    ),


    Task(
        annotator="shipping_coordinator",
        user_id="TASK_88",
instruction="Handle shipment coordination. Obtain tracking information for order #W2611340. Update tracking status to 'in_transit', retrieve courier information, confirm delivery estimates, adjust tracking to 'out_for_delivery', then to 'delivered', and ultimately mark the order status as 'completed'."
        actions=[
            Action(name="getTrackingInfo", kwargs={"order_id": "#W2611340"}),
            Action(name="updateTrackingStatus", kwargs={"tracking_id": "357962501027", "status": "in_transit"}),
            Action(name="getCourierInfo", kwargs={"courier_id": "#COU0003"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="updateTrackingStatus", kwargs={"tracking_id": "357962501027", "status": "out_for_delivery"}),
            Action(name="updateTrackingStatus", kwargs={"tracking_id": "357962501027", "status": "delivered"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#W2611340", "new_status": "completed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="operations_manager",
        user_id="TASK_89",
        instruction="Manage efficient processing of multiple orders. Retrieve the pending orders with a limit of 5, pick the top 3 order IDs, update them all to 'processing' status through bulk processing, verify the updates by retrieving their information, assign fulfillment to each, get revenue summary by product, and create inventory alerts for items with stock at or below 25.",
        actions=[
            Action(name="getOrdersByStatus", kwargs={"status": "pending", "limit": 5}),
            Action(name="bulkOrderProcessing", kwargs={"order_ids": ["#W9962383", "#W9933266", "#W9929926"], "new_status": "processing"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9962383"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9933266"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9929926"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W9962383", "courier_id": "#COU0001"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W9933266", "courier_id": "#COU0001"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W9929926", "courier_id": "#COU0001"}),
            Action(name="getRevenueSummary", kwargs={"group_by": "product"}),
            Action(name="inventoryAlert", kwargs={"threshold": 25})
        ],
        outputs=[]
    ),

    Task(
        annotator="catalog_manager",
        user_id="TASK_90",
        instruction="Handle the management of the product catalog. Locate Laptop products under $2500, verify the availability of the least expensive option, authenticate order items for it, initiate a pending order for user isabella_thompson_1219, apply payment to finalize it. Request estimates for express delivery and coordinate fulfillment to obtain the tracking info.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop", "max_price": 2500}),
            Action(name="checkProductAvailability", kwargs={"item_id": "6017636844"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["6017636844"], "quantities": [1]}),
            Action(name="searchUsers", kwargs={"user_id": "isabella_thompson_1219"}),
            Action(name="createPendingOrder", kwargs={"user_id": "isabella_thompson_1219", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_3999493", "shipping_address": {"address1": "208 Cedar Street", "address2": "Suite 993", "city": "Oakland", "country": "USA", "state": "NV", "zip": "95119"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option":"express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_6017636844"})

        ],
        outputs=[]
    ),

    Task(
        annotator="loyalty_manager",
        user_id="TASK_91",
        instruction="Oversee customer loyalty management. Locate user Isabella Thompson, review her purchase history and revenue overview, apply a specific discount by modifying her pending order item: 4953074738 price to $200, amend the payment and change the status to processing. Subsequently, invoke the create_recommendations API to generate recommendations for the user in the Hiking Boots category.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Isabella Thompson"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "isabella_thompson_1219"}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "isabella_thompson_1219"}),
            Action(name="getUserOrders", kwargs={"user_id": "isabella_thompson_1219", "status": "pending"}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#W6975922", "item_id": "4953074738", "new_price": 200}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#W6975922", "payment_method_id": "paypal_3999493"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#W6975922", "new_status": "processing"}),
            Action(name="createRecommendations", kwargs={"user_id": "isabella_thompson_1219", "preferred_category": "Hiking Boots"})
        ],
        outputs=[]
    ),


    Task(
        annotator="quality_manager",
        user_id="TASK_92",
instruction="Handle quality issues by locating delivered orders, limiting results to 5, and selecting the order # W9907310. Handle item returns related to 'quality issues' and confirm updated stock quantities. Assess the customer's buying history and develop suggestions for the Water Bottle category."
        actions=[
            Action(name="getOrdersByStatus", kwargs={"status": "delivered", "limit": 5}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9907310"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "6819683148"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "8560156827"}),
            Action(name="processReturn", kwargs={"order_id": "#W9907310", "item_ids": ["5745575001", "8733974883"], "reason": "quality issues"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007", "item_id": "5745575001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0012", "item_id": "8733974883"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "charlotte_moore_4814"}),
            Action(name="createRecommendations", kwargs={"user_id": "charlotte_moore_4814", "preferred_category": "Water Bottle"})
        ],
        outputs=[]
    ),



    Task(
        annotator="customer_scenarios",
        user_id="TASK_93",
        instruction="As Omar Jackson (omar_jackson_3107), coordinate a large order as a valued long-time customer. Purchase 1 T-Shirt and 1 pair of Running Shoes, selecting the lowest-cost option for each. Complete the order through your PayPal account. Due to this loyalty transaction, adjust the Running Shoes price manually to $100. Following that, obtain express delivery estimates and arrange courier shipping.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Omar Jackson"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Running Shoes"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8124970213", "9791469541"], "quantities": [1, 1]}),
            Action(name="createPendingOrder", kwargs={"user_id": "omar_jackson_3107", "item_details": [{"item_id": "8124970213", "quantity": 1}, {"item_id": "9791469541", "quantity": 1}]}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "item_id": "9791469541", "new_price": 100}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "payment_method_id": "paypal_1530316", "shipping_address": {
            "address1": "959 Broadway",
            "address2": "Suite 363",
            "city": "San Diego",
            "country": "USA",
            "state": "NV",
            "zip": "90339"
        }}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_81249702139791469541", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="TASK_94",
instruction="As Mason Lee with the email id: mason.lee9297@example.com, you're managing a situation. Locate your most recently delivered order with ID: # W9710999. Process the return of the Electric Toothbrush due to 'defective product'. Then, review the Electric Toothbrush selections to identify the highest-priced option and add a Water Bottle to this order. Next, place an order for the most expensive Water Bottle. Lastly, as this is for personal use, request expedited shipping to your location."
        actions=[
            Action(name="searchUsers", kwargs={"email": "mason.lee9297@example.com"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9710999"}),
            Action(name="processReturn", kwargs={"order_id": "#W9710999", "item_ids": ["3320557165"], "reason": "defective product"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Electric Toothbrush"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8798690242", "3453331371"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "mason_lee_5696", "item_details": [{"item_id": "8798690242", "quantity": 1}, {"item_id": "3453331371", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_87986902423453331371", "payment_method_id": "credit_card_5809636", "shipping_address":{
                                                                          "address1": "668 Highland Drive",
                                                                          "address2": "Suite 584",
                                                                          "city": "Fort Worth",
                                                                          "country": "USA",
                                                                          "state": "NM",
                                                                          "zip": "76176"
                                                                        }}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_87986902423453331371", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),
    Task(
        annotator="sales_manager",
        user_id="TASK_97",
        instruction="You're tasked with boosting sales growth. Locate user Raj Li (raj.li3320@example.com), assess his purchase history, and develop recommendations based on his preferences. Formulate suggestions for the user in the Smart Thermostat category. Create an order for him, ensure it is shipped to his address, and use a credit card as the payment method, selecting the cheapest thermostat from his recommendations.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "raj.li3320@example.com"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "raj_li_8594"}),
            Action(name="createRecommendations", kwargs={"user_id": "raj_li_8594", "preferred_category": "Smart Thermostat"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smart Thermostat"}),
            Action(name="createPendingOrder", kwargs={"user_id": "raj_li_8594", "item_details": [{"item_id": "4953074738", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_4953074738", "payment_method_id": "credit_card_3425145", "shipping_address": {
                                                                          "address1": "422 Elm Street",
                                                                          "address2": "Suite 893",
                                                                          "city": "Washington",
                                                                          "country": "USA",
                                                                          "state": "DC",
                                                                          "zip": "20369"
                                                                        }}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_4953074738", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="data_privacy_officer",
        user_id="TASK_98",
        instruction="Handle data privacy compliance by locating user Ella Kovacs, and modify her address to 505 Cedar Avenue Updated, Suite 539, city: Jacksonville, country: USA, state: AL, zip: 32118 for data accuracy. Additionally, include a new secure payment method via visa credit card ending with 1234. Retrieve her complete order history and examine purchase patterns.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ella Kovacs"}),
            Action(name="updateUserAddress", kwargs={"user_id": "ella_kovacs_6742", "address": {"address1": "505 Cedar Avenue Updated", "address2": "Suite 539", "city": "Jacksonville", "country": "USA", "state": "AL", "zip": "32118"}}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "ella_kovacs_6742", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "1234"}}),
            Action(name="getUserOrders", kwargs={"user_id": "ella_kovacs_6742"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "ella_kovacs_6742"})
        ],
        outputs=[]
    ),

    Task(
        annotator="integration_specialist",
        user_id="TASK_99",
        instruction="Coordinate order integration across channels. Find Bluetooth Speaker products and generate a pending order for customer luna_wilson_7363 using the least costly variant. Confirm the order items, process the payment with PayPal, and retrieve courier information to manage fulfillment assignment.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Bluetooth Speaker"}),
            Action(name="searchUsers", kwargs={"user_id": "luna_wilson_7363"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["7617930199"], "quantities": [1]}),
            Action(name="createPendingOrder", kwargs={"user_id": "luna_wilson_7363", "item_details": [{"item_id": "7617930199", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_7617930199", "payment_method_id": "paypal_2306935", "shipping_address": {"address1": "723 Park Avenue", "address2": "Suite 802", "city": "Fort Worth", "country": "USA", "state": "NM", "zip": "76112"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_7617930199", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supplier_relations",
        user_id="TASK_96",
instruction="Handle the management of supplier relationships. Retrieve information for supplier # SUP0004, check stock for items below 20 units and place an order for 100 units at $100 each for the item with the least stock, ensuring proper order placement and ignoring out-of-stock items. Change the supply order status to 'confirmed', update inventory, review outstanding orders, and set an inventory alert for 'E-Reader' at a threshold of 20."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0004", "low_stock_threshold": 20}),
            Action(name="getProductByItemId", kwargs={"item_id": "5510402676"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0004", "product_id": "3801771308", "item_id": "5510402676", "quantity": 100, "unit_cost": 100}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-5510402676", "new_status": "confirmed"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0004", "item_id": "5510402676", "adjustment": 100}),
            Action(name="inventoryAlert", kwargs={"threshold": 20, "category_filter": "E-Reader"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_01",
instruction="Coordinate as a supply chain manager addressing urgent stock shortages. Collect all item IDs with inventory under 50 units for supplier # Identify the key item with the lowest inventory, excluding those currently out of stock. Gather complete supplier information and place an order for 200 units of this key item at $35 per unit. Check pending orders to verify the new supply order is included. Change the supply order status to 'confirmed' and recheck pending orders to ensure it is no longer listed, verifying that stock levels have been updated."
        actions=[
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 50}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634"}),
            Action(name="getProductByItemId", kwargs={"item_id": "9973034634"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 35}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-9973034634", "new_status": "confirmed"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634", "adjustment": 200}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_02",
instruction="As a performance analyst, evaluate the performance of the supplier Worldwide Electronics Partners (# Retrieve complete supplier information, review all outstanding supply orders, and analyze their order history. Adjust the price of their most expensive laptop to $2800 and order 200 more units of this item at a unit cost of $2000. Update their contact number to '+1-800-555-UPDATED'.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="updateProductPrice", kwargs={"product_id": "4760268021", "item_id": "3334537816", "new_price": 2800}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "3334537816", "quantity": 200, "unit_cost": 2000}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0002", "phone": "+1-800-555-UPDATED", "email": "info@worldelectronics.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_03",
        instruction="Serving as a supply chain manager, a critical issue of product availability has arisen. Verify the stock level of the T-shirt item '5253880258', which customers are indicating is out of stock. Look into its supplier details, present stock levels, and any pending supply orders. Adjust the inventory to 0 to mirror the current situation, then issue an urgent supply order for 300 units at $25 each, and promptly change its status to 'rush'.",
        actions=[
            Action(name="getProductByItemId", kwargs={"item_id": "5253880258"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 0}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 300, "unit_cost": 25}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-5253880258", "new_status": "rush"})

        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_04",
instruction="As the warehouse manager, coordinate a stock rebalancing operation among multiple suppliers. Review stock levels for suppliers #SUP0001, #SUP0002, and # Identify items #SUP0001, #SUP0002, and #SUP0003 with stock levels under 20 units. For the item with the least stock (considering out of stock as a stock level of 0), if there are multiple candidates, choose the one with the lowest ID from each supplier and create supply orders for 150 units at a cost of $30 per unit. Update all suppliers' contact details to change their email domains to 'PRIORITY SUPPLIER', formatting",
        actions=[
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 20}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002", "low_stock_threshold": 20}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0003", "low_stock_threshold": 20}),
            Action(name="getProductByItemId", kwargs={"item_id": "2791467853"}),
            Action(name="getProductByItemId", kwargs={"item_id": "3915604618"}),
            Action(name="getProductByItemId", kwargs={"item_id": "4410138384"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "4896585277", "item_id": "2791467853", "quantity": 150, "unit_cost": 30}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4794339885", "item_id": "3915604618", "quantity": 150, "unit_cost": 30}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0003", "product_id": "7471004230", "item_id": "4410138384", "quantity": 150, "unit_cost": 30}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0001",  "email": "priority@digitalsolutions.com"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0002", "email": "priority@worldelectronics.com"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0003", "email": "priority@techcorp.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_07",
instruction="As an ecommerce customer relations manager, address an urgent stock redistribution. A key customer requires an immediate supply of T-shirt. Inspect current stock levels for supplier # SUP0001, retrieve all T-shirt variants with inventory exceeding 100 units. Modify the stock for item '1176194968' by reducing it by 50 units (for emergency reasons). Place a restock order for 100 units at $40 each and verify the order confirmation."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt", "min_stock": 100}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "1176194968"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "1176194968", "adjustment": -50}),
            Action(name="getProductByItemId", kwargs={"item_id": "1176194968"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "1176194968", "quantity": 100, "unit_cost": 40}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),


    Task(
        annotator="5",
        user_id="sc_task_08",
instruction="You are a warehouse manager. Handle the supplier diversification analysis. Obtain a full list of all suppliers and evaluate the order history and products of supplier # SUP0004. Assess their inventory situation and create a new purchase order for the previously canceled order (20 units at $45 each). Revise their contact information to phone: +1-800-555-1234."
        actions=[
            Action(name="listAllSuppliers", kwargs={}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="getProductDetails", kwargs={"product_id": "5426915165"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0004", "product_id": "5426915165", "item_id": "9956648681", "quantity": 20, "unit_cost": 45}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0004", "phone": "+1-800-555-1234"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="5",
        user_id="TASK_09",
        instruction="You are an inventory manager, Coordinate seasonal inventory planning for winter products. Verify the availability of seasonal items (Smart Thermostat, Fleece Jacket). Retrieve their supplier details, and arrange supply orders to increase inventory: 75 Smart Thermostats, purchase the most expensive model at $120 each, and adjust the price of the priciest Fleece Jacket to $200 for seasonal premium. Ensure the thermostat supply order and jacket price adjustment are accurately documented.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Smart Thermostat"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Fleece Jacket"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "4896585277"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "8560156827"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "4896585277", "item_id": "3377900078", "quantity": 75, "unit_cost": 120}),
            Action(name="updateProductPrice", kwargs={"product_id": "8560156827", "item_id": "7528037711", "new_price": 200}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Fleece Jacket"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_10",
instruction="As a supply chain analyst, coordinate the optimization of supply chain costs. Examine the product and order history of supplier # SUP0006. Set the maximum price for Running Shoes to $150, check their inventory status, and place an order for 40 units at a cost of $130 each. Confirm the pending order.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getProductDetails", kwargs={"product_id": "6938111410"}),
            Action(name="updateProductPrice", kwargs={"product_id": "6938111410", "item_id": "4153505238", "new_price": 150}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "6938111410", "item_id": "4153505238", "quantity": 40, "unit_cost": 130}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    # # # SUPPLY CHAIN TASK 11 - Interdepartmental Supply Evaluation
    Task(
        annotator="supply_chain_director",
        user_id="sc_task_11",
        instruction="In your role as a supply chain analyst, undertake a thorough cross-functional supply analysis and obtain a product-supplier summary for T-shirts. Scrutinize the supplier's full order history, assess stock levels among various items, and refresh the inventory for a recently received shipment comprising 2 variants with id's 9647292434 - 25 units and id 8349118980 - 30 units. Additionally, formulate a strategic supply order for 120 units at a premium price of $50 each for the least costly item and confirm the order's placement.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="getProductSupplierSummary", kwargs={"product_id": "9523456873"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9647292434", "adjustment": 25}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "8349118980", "adjustment": 30}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "3234800602", "quantity": 120, "unit_cost": 50}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    # # # SUPPLY CHAIN TASK 12 - Enhancing Vendor Performance
    Task(
        annotator="vendor_manager",
        user_id="sc_task_12",
instruction="You are an operation manager and need to enhance vendor performance for Workplace Solutions Center (# Evaluate the supplier information, analyze their product offerings, and check existing stock levels. Develop enhancement plans by setting the price of the most expensive LED Light Bulb to $45.99. Place an order for 60 units at a rate of $35 per bulb, update their phone number to +1-800-555-0000, and verify the order placement.)",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getProductDetails", kwargs={"product_id": "2696197613"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="updateProductPrice", kwargs={"product_id": "2696197613", "item_id": "5570660360", "new_price": 45.99}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0008", "product_id": "2696197613", "item_id": "5570660360", "quantity": 60, "unit_cost": 35}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0008", "phone": "+1-800-555-0000"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0008"})
        ],
        outputs=[]
    ),

    # # # TASK 13 - Management of Supply Chain Risks
    Task(
        annotator="risk_manager",
        user_id="sc_task_13",
instruction="As a supply chain risk analyst, set up supply chain risk management protocols. Evaluate product portfolios for #SUP0009, #SUP0010, #SUP0011. For suppliers SUP0009, SUP0010, and SUP0011, collect order histories, assess product offerings, and create a risk mitigation order of 35 units at a unit cost of 28 for the item with the least stock from the supplier that has the fewest products. Exclude out-of-stock items and ensure the order is confirmed. Update the email address for the supplier with the least products to hello@athleticequipment.com."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0011"}),
            Action(name="getProductByItemId", kwargs={"item_id": "7907773809"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "7907773809", "quantity": 35, "unit_cost": 28}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0010", "email": "hello@athleticequipment.com"})
        ],
        outputs=[]
    ),

    # SUPPLY CHAIN TASK 14 - Management of Technology Product Lifecycle
    Task(
        annotator="product_lifecycle_manager",
        user_id="sc_task_14",
instruction="As a tech product lifecycle manager, handle the lifecycle of technology products for Electronics suppliers. Concentrate on Tech Supplies Inc. (#SUP0001) and Worldwide Electronics Partners (#SUP0002). Evaluate the technology products from SUP0001 and Worldwide Electronics Partners (#SUP0002) (Digital Camera, Laptop), lower the price of the most expensive Digital Camera model to $2200 as it approaches end-of-life, and place a supply order for 25 units of the latest Laptop item 1684786391 at $1500, ensuring confirmation of the order."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getProductDetails", kwargs={"product_id": "8940227892"}),
            Action(name="getProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="updateProductPrice", kwargs={"product_id": "8940227892", "item_id": "9644439410", "new_price": 2200}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "1684786391", "quantity": 25, "unit_cost": 1500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="global_operations_manager",
        user_id="sc_task_15",
        instruction="In your role as a global supply chain operations manager, examine the top 10 best-selling products from all categories to identify global demand trends. Concentrate on the leading 3 products, obtain their supplier details, and coordinate strategic supply orders of 100 units each at $100 for White low S size helmet, $42 for jigsaw puzzle animal theme beginner available variant, and $350 for bookshelf black glass 5ft variant per unit price and confirm the placement of these orders.",
        actions=[
            Action(name="getTopSellingProducts", kwargs={"limit": 10}),
            Action(name="searchProductsByCategory", kwargs={"category": "Cycling Helmet"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Jigsaw Puzzle"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Bookshelf"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "7765186836"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "1808611083"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "8600330539"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "1596993217", "quantity": 100, "unit_cost": 100}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "9665100170", "quantity": 100, "unit_cost": 42}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "4900661478", "quantity": 100, "unit_cost": 350}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0007"}),
        ],
        outputs=[]
    ),


    Task(
        annotator="emergency_coordinator",
        user_id="sc_task_16",
instruction="As an emergency coordinator, a crisis has occurred with a vital supplier (# SUP0007) caused by disruption. Assess their product range and inventory levels, identify essential items needing immediate attention (the lowest ID out-of-stock item). Place an urgent order for 80 units of that item from Style Trend Distributors at $250 each, confirm the order, and upon receipt, mark it as delivered and update the inventory and stock levels accordingly.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name ="getProductByItemId", kwargs={"item_id": "1111254697"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "1111254697", "quantity": 80, "unit_cost": 250}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-1111254697", "new_status": "delivered"}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SOfd520c73-1111254697"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0007", "item_id": "1111254697", "adjustment": 80}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007", "item_id": "1111254697"})
        ],
        outputs=[]
    ),

    # # # SUPPLY CHAIN TASK 17 - Development of Strategic Partnerships
    Task(
        annotator="partnership_manager",
        user_id="sc_task_17",
instruction="Act as a strategic partnership manager. Turn your attention to Supplier # SUP0009 - analyze the product lineup, monitor order history, and explore growth opportunities. Reassess pricing by establishing the cost of the highest-priced Tea Kettle model at $85, then place a strategic order for 45 units of that model at $65 each and confirm it."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Tea Kettle"}),
            Action(name="getProductDetails", kwargs={"product_id": "9832717871"}),
            Action(name="updateProductPrice", kwargs={"product_id": "9832717871", "item_id": "9647374798", "new_price": 85}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0009", "product_id": "9832717871", "item_id": "9647374798", "quantity": 45, "unit_cost": 65}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0009"})
        ],
        outputs=[]
    ),


    Task(
        annotator="quality_assurance_manager",
        user_id="sc_task_18",
instruction="As a quality assurance specialist, handle the examination of Athletic Equipment Co. (# Evaluate current supply orders, modify the price of the top-tier cycling helmet to $250 to account for quality premiums, and create a quality-centric order for 100 units at $150 each. Confirm the order and update the supplier contact to include quality assurance stipulations at quality@athleticequipment.com."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getProductDetails", kwargs={"product_id": "7765186836"}),
            Action(name="updateProductPrice", kwargs={"product_id": "7765186836", "item_id": "9013366374", "new_price": 250}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "9013366374", "quantity": 100, "unit_cost": 150}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0010", "email": "quality@athleticequipment.com"})

        ],
        outputs=[]
    ),

    # # # SUPPLY CHAIN TASK 19 - Digital Transformation in Supply Chain
    Task(
        annotator="digital_transformation_lead",
        user_id="sc_task_19",
instruction="As a digital consultant, direct attention to the supplier with ID: # SUP0006 to implement digital workflows. Review the product catalog with a focus on Vacuum Cleaners and Bluetooth Speakers. The supplier has requested a price modification for item 5967152432 to $299. Also, enable tech-driven supply orders for item 4602305039 (50 units at $500 each) and item 5967152432 (30 units at $200 each), while updating their systems with the new email digital@livingcomfort.com. Confirm the supply order and contact information updates."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getProductDetails", kwargs={"product_id": "1762337868"}),
            Action(name="getProductDetails", kwargs={"product_id": "4768869376"}),
            Action(name="updateProductPrice", kwargs={"product_id": "4768869376", "item_id": "5967152432", "new_price": 299}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "1762337868", "item_id": "4602305039", "quantity": 50, "unit_cost": 500}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "5967152432", "quantity": 30, "unit_cost": 200}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0006", "email": "digital@livingcomfort.com"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_manager",
        user_id="TASK_21",
instruction="As a supply manager facing critical stock deficiencies, identify all item IDs with inventory under 20 units for supplier # SUP0006, omitting items that are entirely out of stock. Gather detailed supplier information, then place an order for 150 units of the item with the least inventory at $2500 each. Verify the order. After receipt of the product, update the order status to delivered and revise the inventory to reflect the new stock levels.",
        actions=[
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0006", "low_stock_threshold": 20}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468"}),
            Action(name="getProductByItemId", kwargs={"item_id": "4772738468"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "4772738468", "quantity": 150, "unit_cost": 2500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-4772738468", "new_status": "delivered"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468", "adjustment": 150}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0006", "item_id": "4772738468"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_analyst",
        user_id="sc_task_22",
instruction="As an analyst for an ecommerce site, assess the performance of (# Fetch their details and review all outstanding supply orders and history. Adjust the price of their most expensive item to $180 and order 200 more units of this item at $100 each. Confirm the order and update their contact number to '+1-800-555-9100')."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="getProductDetails", kwargs={"product_id": "8560156827"}),
            Action(name="updateProductPrice", kwargs={"product_id": "8560156827", "item_id": "9385662952", "new_price": 180}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 200, "unit_cost": 100}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0012", "phone": "+1-800-555-9100"})
        ],
        outputs=[]
    ),

    Task(
        annotator="warehouse_operator",
        user_id="sc_task_23",
        instruction="As a supply chain manager, Handle the review of T-shirt item '5253880258' that customers have reported as out of stock. Look into its supplier information, assess current stock levels, and verify if there are any pending supply orders. Should the stock be low (under 10), adjust the inventory to 0 to match the actual status, then organize an urgent supply order for 300 units at $25 each, and promptly change its status to 'rush'.",
        actions=[
            Action(name="getProductByItemId", kwargs={"item_id": "5253880258"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 0}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 300, "unit_cost": 25}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-5253880258", "new_status": "rush"})

        ],
        outputs=[]
    ),


    Task(
        annotator="inventory_manager",
        user_id="sc_task_24",
instruction="Serving as inventory manager, Verify stock levels for suppliers #SUP0008, #SUP0006, and # Identify items with stock fewer than 10 units for SUP0008, #SUP0006, and #SUP0012. For each supplier's item with the lowest stock, excluding those that are out of stock, arrange orders for 150 units at $80 each. Update all suppliers' contact information to include 'PRIORITY SUPPLIER' by changing their email domains to priority@<domain>.com."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0008", "low_stock_threshold": 10}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0006", "low_stock_threshold": 10}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0012", "low_stock_threshold": 10}),
            Action(name="getProductByItemId", kwargs={"item_id": "9829827210"}),
            Action(name="getProductByItemId", kwargs={"item_id": "4772738468"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0008", "product_id": "6679515468", "item_id": "9829827210", "quantity": 150, "unit_cost": 80}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "4772738468", "quantity": 150, "unit_cost": 80}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0008",  "email": "priority@workplacesolutions.com"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0006", "email": "priority@livingcomfort.com"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0012", "email": "priority@culinarybasics.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="shipping manager",
        user_id="sc_task_25",
        instruction="As a shipping control manager, examine the supply orders waiting for processing and pinpoint those with quantities fewer than 10 units. Adjust their quantities to 50 to optimize shipping costs. Arrange a supply order of 150 units priced at $120 each for item 9385662952, as it is currently out of stock, and confirm that the order placement and supplier mapping were executed accurately.",
        actions=[
            Action(name="listSupplyOrdersByStatus", kwargs={"status": "pending"}),
            Action(name="updateSupplyOrderQuantity", kwargs={"supply_order_id": "#SO5993", "new_quantity": 50}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="getProductByItemId", kwargs={"item_id": "9385662952"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 150, "unit_cost": 120}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SOfd520c73-9385662952"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0012"})
        ],
        outputs=[]
    ),


    Task(
        annotator="drop_shipping_manager",
        user_id="sc_task_26",
        instruction="As a drop shipping manager, analyze the top 20 selling products to gain insight into market trends. Concentrate on high-value items like Espresso Machine and the digital camera category. Gather information on the priciest model of espresso and digital cameras, order 20 units of the highest-priced item among these two products at $1500 each. Ensure the order is confirmed and revise the supplier contact details to include dropshipping@<domain>.com.",
        actions=[
            Action(name="getTopSellingProducts", kwargs={"limit": 20}),
            Action(name="searchProductsByCategory", kwargs={"category": "Espresso Machine"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Digital Camera"}),
            Action(name="getProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="getProductDetails", kwargs={"product_id": "8940227892"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0009", "product_id": "4354588079", "item_id": "3951031513", "quantity": 20, "unit_cost": 1500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0009", "email": "dropshipping@animalcare.com"})
        ],
        outputs=[]
    ),

    Task(
        annotator="logistics_coordinator",
        user_id="sc_task_27",
instruction="As an ecommerce customer relations manager, it is your responsibility to address an emergency stock redistribution. A key customer requires an immediate supply of Cycling Helmet. Start by checking the current stock levels for supplier # Retrieve all Cycling Helmet variants with inventory greater than 100 units. The supplier requires an inventory update, so decrease the stock of item '5537798301' by 50 units for emergency allocation. Create a replenishment order for 100 units at $40 each for this item, mark the order status as 'urgent', and confirm the stock adjustment."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Cycling Helmet", "min_stock": 100}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301", "adjustment": -50}),
            Action(name="getProductByItemId", kwargs={"item_id": "5537798301"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "5537798301", "quantity": 100, "unit_cost": 40}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-5537798301", "new_status": "urgent"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0010", "item_id": "5537798301"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="analyst",
        user_id="sc_task_28",
instruction="Your role as a warehouse manager involves obtaining a list of all suppliers, and conducting an analysis of supplier # Update the pending supply order for SUP0007 to confirmed status as the items have arrived, then proceed with the inventory update. Verify that both updates are executed successfully. Also, revise their contact information to include phone: +1-800-555-1245."
        actions=[
            Action(name="listAllSuppliers", kwargs={}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SO4238", "new_status": "confirmed"}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SO4238"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0007", "item_id": "8018699955", "adjustment": 91}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0007", "phone": "+1-800-555-1245"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="me",
        user_id="sc_task_29",
        instruction="As a demand manager, handle seasonal inventory planning for the summer season. Review product availability for seasonal items \"Cotton T-shirt\" and \"Air Purifiers\". Determine if there are any pending orders for the purple cotton XL T-shirt; if none exist, create supply orders to build inventory: 75 purple Cotton T-shirts of size XL, each priced at $10. Update the price of the most expensive Air purifier to $2000 and ensure that both the supply order and price increase are accurately recorded.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Air Purifier"}),
            Action(name="getProductDetails", kwargs={"product_id": "9523456873"}),
            Action(name="getProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "8124970213", "quantity": 75, "unit_cost": 10}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateProductPrice", kwargs={"product_id": "3821016478", "item_id": "8302289002", "new_price": 2000}),
            Action(name="getProductDetails", kwargs={"product_id": "3821016478"})
        ],
        outputs=[]
    ),

    Task(
        annotator="cost_analyst",
        user_id="sc_task_30",
instruction="As a cost specialist analyst, coordinate supply chain cost optimization. Examine supplier # Order history and product catalog for SUP0009. Decrease the price of the highest-priced item by $50, check its inventory level, and create a supply order for 40 units at $1300 each for that item. Confirm the pending order for accuracy."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="getProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="updateProductPrice", kwargs={"product_id": "4354588079", "item_id": "3951031513", "new_price": 3239.46}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0009", "product_id": "4354588079", "item_id": "3951031513", "quantity": 40, "unit_cost": 1300}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0009"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_director",
        user_id="sc_task_31",
        instruction="You are a supply chain analyst. Coordinate a comprehensive cross-functional supply overview for Skateboard. Assemble a summary of product suppliers, including the complete order history and current stock levels for all items. Additionally, we have received a shipment for item 3098764622; mark that supply order as fulfilled and update the inventory accordingly. Furthermore, prepare a supply order for 120 units of the least expensive Skateboard priced at $150, and verify that the order has been placed successfully.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Skateboard"}),
            Action(name="getProductSupplierSummary", kwargs={"product_id": "1968349452"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SO6767"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6767", "new_status": "fulfilled"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0005", "item_id": "3098764622", "adjustment": 39}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0005", "product_id": "1968349452", "item_id": "6843647669", "quantity": 120, "unit_cost": 150}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0005"})
        ],
        outputs=[]
    ),

    Task(
        annotator="vendor_manager",
        user_id="sc_task_32",
instruction="You are an operations manager. Improve vendor performance for # SUP0007. Begin by examining the supplier profile, product catalog, and existing inventory levels. Develop improvement strategies by setting the price of the premium Wristwatch to $2200. Place a supply order for 60 units of that wristwatch at $1500 each, update their contact number to +1-800-555-0110, and confirm that the order has been successfully processed."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getProductDetails", kwargs={"product_id": "6066914160"}),
            Action(name="updateProductPrice", kwargs={"product_id": "6066914160", "item_id": "4510078629", "new_price": 2200}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "6066914160", "item_id": "4510078629", "quantity": 60, "unit_cost": 1500}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0007", "phone": "+1-800-555-0110"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="lifecycle_manager",
        user_id="sc_task_34",
instruction="As a product lifecycle manager, handle the lifecycle processes for suppliers, particularly #SUP0007 and # Retrieve product details and inventory for SUP0007 and SUP0008. Analyze their product categories—Bookshelf and Desklamp. Lower the price of the priciest Bookshelf to $500. Place a supply order for 25 units of the Desk lamp with variant ID: 4385534692 at $100 each, ensuring successful order placement."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getProductDetails", kwargs={"product_id": "8600330539"}),
            Action(name="getProductDetails", kwargs={"product_id": "6817146515"}),
            Action(name="updateProductPrice", kwargs={"product_id": "8600330539", "item_id": "1768466237", "new_price": 500}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0008", "product_id": "6817146515", "item_id": "4385534692", "quantity": 25, "unit_cost": 100}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0008"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="global_operations_manager",
        user_id="TASK_35",
        instruction="In your role as a global supply chain operations manager, evaluate the top 10 selling products across all categories to assess global demand patterns. Concentrate on the top 3 products, collect their supplier details, inspect their availability, and plan strategic supply orders of 100 units each at a unit cost of $100 for helmets, $42 for jigsaw puzzles, and $350 for bookshelves. Order the least costly variant for each product and confirm order placement.",
        actions=[
            Action(name="getTopSellingProducts", kwargs={"limit": 10}),
            Action(name="getProductSupplierSummary", kwargs={"product_id": "7765186836"}),
            Action(name="getProductSupplierSummary", kwargs={"product_id": "1808611083"}),
            Action(name="getProductSupplierSummary", kwargs={"product_id": "8600330539"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "1596993217", "quantity": 100, "unit_cost": 100}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "1808611083", "item_id": "9665100170", "quantity": 100, "unit_cost": 42}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "8600330539", "item_id": "8479046075", "quantity": 100, "unit_cost": 350}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0007"}),
        ],
        outputs=[]
    ),

    Task(
        annotator="Supply chain emergency coordinator",
        user_id="sc_task_36",
instruction="As a Supply Chain Emergency Coordinator, handle the disruption impacting Supplier # SUP0012. Review the product inventory and current stock levels to find out-of-stock items. For each affected product, place an order for 80 units at $50 per unit and verify the order confirmation. Once the shipment is received, mark the order as delivered, update the inventory records, and adjust the stock quantities accordingly."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0012", "product_id": "8560156827", "item_id": "9385662952", "quantity": 80, "unit_cost": 50}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SOfd520c73-9385662952", "new_status": "delivered"}),
            Action(name="getSupplyOrderDetails", kwargs={"supply_order_id": "#SOfd520c73-9385662952"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952", "adjustment": 80}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952"})
        ],
        outputs=[]
    ),

    Task(
        annotator="me",
        user_id="sc_task_37",
instruction="In the role of a global supply chain manager, assess Supplier # SUP0006 by analyzing their product lineup, assessing order history, and considering growth opportunities. Revise terms by adjusting the cost of their most expensive Bluetooth Speaker model to $300. Additionally, arrange a supply order for 150 units at $150 each for variants currently out of stock, and confirm the order has been successfully processed."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Bluetooth Speaker"}),
            Action(name="updateProductPrice", kwargs={"product_id": "4768869376", "item_id": "7751905257", "new_price": 300}),
            Action(name="searchProductsByCategory", kwargs={"category": "Bluetooth Speaker", "min_stock": 0, "max_stock": 0}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "2635605237", "quantity": 150, "unit_cost": 150}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "1052700637", "quantity": 150, "unit_cost": 150}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0006", "product_id": "4768869376", "item_id": "4716977452", "quantity": 150, "unit_cost": 150}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0006"})
        ],
        outputs=[]
    ),

    Task(
        annotator="quality_assurance_manager",
        user_id="sc_task_38",
instruction="Handle quality assurance tasks by evaluating Suppliers # SUP0003. It is crucial to assess their product assortment, quality benchmarks, and inventory status. Analyze the existing supply orders and modify the price of the most expensive Tablet to $1500 to accurately represent its quality value. Place an order for 100 units of this specific Tablet model at $500 each, prioritizing quality, and ensure the order is confirmed. Revise the supplier's contact information to include quality assurance instructions at quality@techcorp.com."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="getProductDetails", kwargs={"product_id": "8024098596"}),
            Action(name="updateProductPrice", kwargs={"product_id": "8024098596", "item_id": "2235648106", "new_price": 1500}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0003", "product_id": "8024098596", "item_id": "2235648106", "quantity": 100, "unit_cost": 500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0003", "email": "quality@techcorp.com"})

        ],
        outputs=[]
    ),

    Task(
        annotator="lead",
        user_id="sc_task_39",
instruction="Coordinate with Style Trend Distributors (ID: # SUP0007) to improve their digital workflows. Review the product catalog focusing on Air Purifiers and Headphones. Set the Air Purifier price (Item ID: 8302289002) to $499. Organize tech-enabled supply orders for Item ID: 3104857380 for 50 units at $300 each and Item ID: 8302289002 for 30 units at $300 each. Update their system records by changing the contact email to digital@styletrend.com and ensure all data is synchronized.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Air Purifier"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Headphones"}),
            Action(name="updateProductPrice", kwargs={"product_id": "3821016478", "item_id": "8302289002", "new_price": 499}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "6992792935", "item_id": "3104857380", "quantity": 50, "unit_cost": 300}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0007", "product_id": "3821016478", "item_id": "8302289002", "quantity": 30, "unit_cost": 300}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0007"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0007", "email": "digital@styletrend.com"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0007"})
        ],
        outputs=[]
    ),

    Task(
        annotator="supply_chain_auditor",
        user_id="sc_task_40",
        instruction="As a supply chain analyst, manage a comprehensive audit of the entire supply chain for all suppliers. Assess each supplier to determine the one with the most varied product range, review their order history, and utilize the findings from the audit to enhance supply ordering. Proceed to place an order for Item ID: 8997785118 — 50 units at $1,500 each — confirm the placement of the order, and update the supplier's record with the email audit@worldelectronics.com for audit compliance. Ensure the contact update has been applied successfully.",
        actions=[
            Action(name="listAllSuppliers", kwargs={}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getSupplierOrderHistory", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="getProductByItemId", kwargs={"item_id": "8997785118"}),
            Action(name="getProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0002", "product_id": "4760268021", "item_id": "8997785118", "quantity": 50, "unit_cost": 1500}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0002", "email": "audit@worldelectronics.com"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0002"}),
        ],
        outputs=[]
    ),



    Task(
        annotator="generator",
        user_id="medium_05_update_address_and_get_delivery_estimate",
        instruction="You are Ethan Wilson. Having relocated to Mexico, start by updating your address to 123 Maple St, Toronto, ON, M5H 2N2, Mexico. Next, ascertain the standard delivery estimate pertinent to your new country.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ethan Wilson"}),
            Action(name="updateUserAddress", kwargs={"user_id": "ethan_wilson_6181", "address": {"address1": "123 Maple St", "address2": "", "city": "Toronto", "country": "Mexico", "state": "ON", "zip": "M5H 2N2"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico", "delivery_option": "standard"})
        ],
        outputs=[]
    ),

    Task(
        annotator="generator",
        user_id="hard_01_full_order_workflow",
        instruction="Assume the role of customer Ethan Wilson. Your aim is to buy the 15-inch, i7, 32GB RAM, 1TB SSD Laptop (item ID '6017636844'). Initiate an order, use your PayPal account ('paypal_5727330') for payment, ship to your default address, and choose the best courier to deliver within the USA. Can you provide the final tracking ID?",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ethan Wilson"}),
            Action(name="createPendingOrder", kwargs={"user_id": "ethan_wilson_6181", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_5727330", "shipping_address": {"address1": "986 Sunset Drive", "address2": "Suite 259", "city": "Phoenix", "country": "USA", "state": "AZ", "zip": "80279"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_02_multi_item_return_and_stock_check",
instruction="As the manager of the returns department, handle the return process for customer Raleigh Moore, who is sending back a 'Water Bottle' and 'Hiking Boots' from order #W4817420. The return reason is 'no longer needed'. After completing the return, verify the updated stock level for the returned hiking boots, which fall under the management of supplier # W4817420. The reason for return is 'no longer needed'. Once the return is processed, check the revised stock quantity for the returned hiking boots managed by supplier #SUP0002."
        actions=[
            Action(name="searchUsers", kwargs={"name": "Raleigh Moore"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="processReturn", kwargs={"order_id": "#W4817420", "item_ids": ["6777246137", "3812493782"], "reason": "no longer needed"}),
            Action(name="getSupplierInfo", kwargs={"product_id": "7363354090"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_03_low_stock_analysis_and_reorder",
instruction="As a supply chain director, begin by identifying all products from supplier 'Tech Supplies Inc.' with supplier ID: # Identify SUP0001 items with stock below 40, excluding those that are entirely out of stock. Collect supplier details and create a new order for each item to restock to 200 units at $30 per unit. Confirm successful order placement."
        actions=[
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0001", "low_stock_threshold": 40}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getProductByItemId", kwargs={"item_id": "1804581713"}),
            Action(name="getProductByItemId", kwargs={"item_id": "9973034634"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "1804581713", "quantity": 163, "unit_cost": 30}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 164, "unit_cost": 30}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_05_manual_inventory_correction_and_validation",
        instruction="You are tasked with being an inventory auditor. After conducting a physical inventory check, it has been determined that for supplier '#SUP0002', item '8997785118' possesses 50 units instead of 51. Amend this in the system. Subsequently, for further accuracy, modify the inventory of item '4241599783' by adding an extra 10 units.",
        actions=[
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002", "item_id": "8997785118"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0002", "item_id": "8997785118", "new_stock": 50}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0002", "item_id": "4241599783", "adjustment": 10})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_06_add_payment_and_place_order",
        instruction="You are Mia Martinez. Your task is to add a fresh PayPal account to your profile. Afterward, purchase a black, size S, polyester, crew neck T-Shirt. Utilize the newly added PayPal account for payment and arrange shipment to your default address via Priority Shipping Co.. What is the new order's ID?",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Mia Martinez"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "mia_martinez_3271", "payment_method": {"source": "paypal"}}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="createPendingOrder", kwargs={"user_id": "mia_martinez_3271", "item_details": [{"item_id": "1176194968", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_1176194968", "payment_method_id": "paypal_fd520c73", "shipping_address": {"address1": "615 Laurel Lane", "address2": "Suite 552", "city": "Pittsburgh", "country": "USA", "state": "OH", "zip": "19036"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_1176194968", "courier_id": "#COU0003"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_07_price_adjustment_and_recalculation",
        instruction="As a sales manager, update the price for the Garden Hose in the pending order of user 'mei_ahmed_5058' due to a pricing mistake, setting it to $100.00. Charge the price difference to the user's PayPal account, designate a courier, and proceed with shipping. Finally, gather the revised order details and verify the adjusted total revenue for this user.",
        actions=[
            Action(name="searchUsers", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="getUserOrders", kwargs={"user_id": "mei_ahmed_5058", "status": "pending"}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#W2631563", "item_id": "5753502325", "new_price": 100.00}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#W2631563", "payment_method_id": "paypal_7160322"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W2631563", "courier_id": "#COU0001"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W2631563"}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "mei_ahmed_5058"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_08_resolve_discontinued_stock_issue",
        instruction="As an inventory specialist, observe that item '5253880258' from supplier '#SUP0001' is marked as 'out_of_stock'. Manually adjust the stock level for '5253880258' to 50 units and confirm the update in the supplier data. Next, place a supply order for 100 units of this item with the same supplier at $25 per unit and ensure the order has been entered successfully.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258", "new_stock": 50}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getProductByItemId", kwargs={"item_id": "5253880258"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "9523456873", "item_id": "5253880258", "quantity": 100, "unit_cost": 25}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="hard_09_cross_border_shipping_coordination",
        instruction="As a logistics planner, Customer 'Mia Martinez' needs a 15inch Laptop i7 1TB SSD shipped to Mexico. First, evaluate delivery timelines for Mexico. Then, select an appropriate courier. Ultimately, generate a pending order for her, process the payment using the user's credit card, and allocate the courier. Currently, register the order under her default US address, focusing primarily on getting the courier assignment for the accurate destination.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Mia Martinez"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "Mexico"}),
            Action(name="createPendingOrder", kwargs={"user_id": "mia_martinez_3271", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_8955149", "shipping_address": {"address1": "615 Laurel Lane", "address2": "Suite 552", "city": "Pittsburgh", "country": "USA", "state": "OH", "zip": "19036"}}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_01",

instruction="Act as a customer service manager. A customer named William Li has informed us that order # W2611340 has been delivered, but the Office Chair (item_id: 8426249116) is damaged. Process a return for the damaged chair using 'Item arrived damaged' as the reason and credit her account. Check the stock level for the returned chair. Additionally, assess her total spending history to see if she qualifies for a loyalty discount voucher."
        actions=[
            Action(name="searchUsers", kwargs={"name": "William Li"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="processReturn", kwargs={"order_id": "#W2611340", "item_ids": ["8426249116"], "reason": "Item arrived damaged"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="checkProductAvailability", kwargs={"item_id": "8426249116"}),
            Action(name="getProductByItemId", kwargs={"item_id": "8426249116"}),
            Action(name="getStockLevels", kwargs={"item_id": "8426249116", "supplier_id": "#SUP0002"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "william_li_5688"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_03",
        instruction="Assume the role of Noah Anderson. You need to modify your shipping address. Check if there are any orders in a pending state. If so, cancel those orders and update the address to 123 Pine St, Apt 4B, Boulder, AZ, 80302, USA. Once updated, locate the most recent order, check its tracking status, and identify the courier. Lastly, find all couriers that serve the updated address for future deliveries and obtain the delivery estimates for both standard and express shipping options to the new address.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Noah Anderson"}),
            Action(name="getUserOrders", kwargs={"user_id": "ethan_wilson_6181", "status": "pending"}),
            Action(name="updateUserAddress", kwargs={"user_id": "ethan_wilson_6181", "address": {"address1": "123 Pine St", "address2": "Apt 4B", "city": "Boulder", "state": "AZ", "zip": "80302", "country": "USA"}}),
            Action(name="searchUsers", kwargs={"user_id": "ethan_wilson_6181"}),
            Action(name="getUserOrders", kwargs={"user_id": "ethan_wilson_6181"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#W7678072"}),
            Action(name="getCourierInfo", kwargs={"courier_id": "#COU0007"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "standard"})

        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="medium_task_04",
        instruction="As a marketing analyst, begin by compiling a list of all 'pending' and 'processing' orders in the system to grasp the current workload. Afterward, for a designated user, Lucas Rodriguez (lucas.rodriguez3158@example.com), assess his purchase history to verify if Garden hose ranks among his preferred categories. Relying on this category, launch a new promotional campaign named campaign1 providing a 15% discount.",
        actions=[
            Action(name="getOrdersByStatus", kwargs={"status": "pending"}),
            Action(name="getOrdersByStatus", kwargs={"status": "processing"}),
            Action(name="searchUsers", kwargs={"email": "lucas.rodriguez3158@example.com"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "lucas_rodriguez_6635"}),
            Action(name="createPromotionalCampaign", kwargs={"campaign_name": "campaign1", "target_category": "Garden Hose", "discount_percentage": 15}),

        ],
        outputs=[]
    ),



    Task(
        annotator="generator_01",
        user_id="high_task_02",

        instruction="As a supply chain manager, initiate a crucial inventory alert for items in the Cycling Helmet category with stock under 50. For the item identified with the smallest stock, determine its supplier. Subsequently, review all pending supply orders for that supplier. If there are no pending orders for this particular critical item, you must initiate a new supply order for 200 units at $25 each. Lastly, search for any 'cancelled' supply orders for that supplier, update their status to 'archived', and prepare a comprehensive revenue summary categorized by product.",
        actions=[
            Action(name="inventoryAlert", kwargs={"threshold": 50, "category_filter": "Cycling Helmet"}),

            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="getProductByItemId", kwargs={"item_id": "7907773809"}),

            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0010", "product_id": "7765186836", "item_id": "7907773809", "quantity": 200, "unit_cost": 25.00}),

            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0010"}),

            Action(name="listSupplyOrdersByStatus", kwargs={"supplier_id": "#SUP0010", "status": "cancelled"}),

            Action(name="getRevenueSummary", kwargs={"group_by": "product"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="5",
        user_id="high_task_03",

instruction=("As a VIP customer executive, one of the customers, Raleigh Moore (Raleigh.moore6020@example.com), intends to cancel the 'Hiking Boots' from her order # W4817420. Although the order status shows 'delivered', you need to start a return with the reason 'Item no longer needed'. Then, help her by checking her purchase history to suggest a new pair of boots, making sure the specific variant (size 8) is in stock, and add a new PayPal payment method to her account for future purchases.")
        actions=[
            Action(name="searchUsers", kwargs={"email": "charlotte.moore6020@example.com"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="processReturn", kwargs={"order_id": "#W4817420", "item_ids": ["3812493782"], "reason": "Item no longer needed"}),
            Action(name="createRecommendations", kwargs={"user_id": "charlotte_moore_2033", "preferred_category": "Hiking Boots"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Hiking Boots"}),
            Action(name="checkProductAvailability", kwargs={"item_id": "3613716226"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "charlotte_moore_2033", "payment_method": {"source": "paypal"}}),
        ],
        outputs=[]
    )
    ,

    Task(
        annotator="generator_01",
        user_id="high_task_07",

instruction=("As a logistics coordinator, the fulfillment for order #W2611340 has been dispatched. Adjust its tracking status to 'in_transit' and ensure the update is verified. Next, identify the courier in charge of this delivery. After finding the courier, examine the countries they deliver to. Finally, locate all supply orders from supplier # W2611340 has been shipped. Update its tracking status to 'in_transit' and confirm the change. Next, determine the courier responsible for this shipment. After identifying the courier, review the countries they service. Lastly, find all supply orders from supplier #SUP0001 and cancel any that are still 'pending'. Generate a revenue summary by product to assess the impact of these cancellations.")
        actions=[
            Action(name="getTrackingInfo", kwargs={"order_id": "#W2611340"}),

            Action(name="updateTrackingStatus", kwargs={"tracking_id": "357962501027", "status": "in_transit"}),

            Action(name="getTrackingInfo", kwargs={"tracking_id": "357962501027"}),

            Action(name="getCourierInfo", kwargs={"courier_id": "#COU0003"}),

            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"}),

            Action(name="updateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "new_status": "cancelled"}),

            Action(name="getRevenueSummary", kwargs={"group_by": "product"}),

        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="high_task_11",

instruction="As an operations specialist, identify all orders with the 'delivered' status. From this selection, retrieve the first two orders, obtain their details, and shift them to 'archived' status via a bulk update. Subsequently, locate user 'William Li' and review his purchase history. Based on his past transactions, create new product recommendations. Lastly, verify any outstanding supply orders from 'Tech Supplies Inc.' (# SUP0001)."
        actions=[
            Action(name="getOrdersByStatus", kwargs={"status": "delivered"}),

            Action(name="getOrderDetails", kwargs={"order_id": "#W9994227"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9980894"}),
            Action(name="bulkOrderProcessing", kwargs={"order_ids": ["#W9994227", "#W9980894"], "new_status": "archived"}),
            Action(name="searchUsers", kwargs={"name": "William Li"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "william_li_5688"}),
            Action(name="createRecommendations", kwargs={"user_id": "william_li_5688", "preferred_category": "Water Bottle"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="high_task_12",

instruction="As a customer service agent, you are managing a detailed request from 'Raleigh Moore' (Raleigh.moore6020@example.com). She wishes to return the 'Bookshelf' from order # W4817420 states 'Item does not fit' as the reason for return. Handle the return process accordingly. She plans to buy a specific T-shirt (item_id: 9612497925). Create a new pending order for this T-shirt. Additionally, she has a new address. Update her address to '999 Lakeview Dr, Houston, NM, 78701, USA'. Finally, check delivery times for express shipping to her updated address."
        actions=[
            Action(name="searchUsers", kwargs={"email": "charlotte.moore6020@example.com"}),

            Action(name="getOrderDetails", kwargs={"order_id": "#W4817420"}),

            Action(name="processReturn", kwargs={"order_id": "#W4817420", "item_ids": ["4900661478"], "reason": "Item does not fit"}),

            Action(name="getOrderDetails", kwargs={"order_id": "#W4817420"}),

            Action(name="validateOrderItems", kwargs={"item_ids": ["9612497925"]}),

            Action(name="createPendingOrder", kwargs={"user_id": "charlotte_moore_2033", "item_details": [{"item_id": "9612497925", "quantity": 1}]}),

            Action(name="updateUserAddress", kwargs={"user_id": "charlotte_moore_2033", "address": {"address1": "999 Lakeview Dr", "address2": "", "city": "Houston", "state": "NM", "zip": "78701", "country": "USA"}}),

            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),


        ],
        outputs=[]
    ),

     Task(
        annotator="generator_01",
        user_id="high_task_15",

        instruction="As a marketing manager planning a campaign for 'Laptops', begin by identifying all laptops priced below $2700. Next, locate the supplier of the most expensive laptop from that selection. Update the inventory for that particular laptop by manually increasing it with 20 units. Conclude by retrieving a revenue summary organized by product, search for user 'William Li', and scrutinize his purchasing history to craft personalized recommendations for him. Additionally, verify the shipping estimate to Mexico.",
        actions=[
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop", "max_price": 2700}),

            Action(name="getSupplierInfo", kwargs={"product_id": "4760268021"}),

            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638"}),

            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638", "adjustment": 20}),

            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0002", "item_id": "5052031638"}),

            Action(name="getRevenueSummary", kwargs={"group_by": "product"}),

            Action(name="searchUsers", kwargs={"name": "William Li"}),

            Action(name="getUserOrders", kwargs={"user_id": "william_li_5688"}),

            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "william_li_5688"}),

            Action(name="createRecommendations", kwargs={"user_id": "william_li_5688", "preferred_category": "Water Bottle"}),

            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico"}),

        ],
        outputs=[]
    ),

    # Advanced E-commerce Customer Operations - Complicated Situations
    Task(
        annotator="customer_scenarios",
        user_id="bulk_purchase_discount_workflow",
        instruction="As Ava Martinez (ava.martinez9791@example.com), a business proprietor purchasing Office Chairs (item_id: 8426249116), initiate the order and apply the gift card for payment. Realize the total overshoots the gift card balance by $5, then register a new Visa credit card with the last 4 digits 1234 to your account to settle the remaining amount. Arrange shipment to your address using any available courier. Lastly, considering the customer’s long-term status, an adjustment is made by manually setting one chair's price to $400 to implement a discount, subsequently readjusting the payment.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "ava.martinez9791@example.com"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8426249116"], "quantities": [1]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ava_martinez_1101", "item_details": [{"item_id": "8426249116", "quantity": 1}]}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_8426249116", "item_id": "8426249116", "new_price": 400}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_8426249116", "payment_method_id": "gift_card_9450778", "shipping_address": {"address1": "197 Elm Street", "address2": "Suite 737", "city": "San Antonio", "country": "USA", "state": "NM", "zip": "78263"}}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "ava_martinez_1101", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "1234"}}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#Wfd520c73_8426249116", "payment_method_id": "credit_card_fd520c73"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#Wfd520c73_8426249116", "new_status": "processing"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_8426249116", "courier_id": "#COU0001"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#Wfd520c73_8426249116"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="address_change_shipping_crisis",
instruction="You are Ella Anderson, relocating to another state to visit someone. You've just made order # W7381650 needs to be updated due to a change of address to '456 Ocean Ave, Miami, AL, 33101, USA'. Please cancel the Air Purifier from the order and update the delivery address. Place a new order for the canceled item to be sent to the new address. The rest of the items can be delivered to the old address. Keep track of the new order."
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ella Anderson"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W7381650"}),
            Action(name="cancelOrderItem", kwargs={"order_id": "#W7381650", "item_id": "8302289002"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W7381650"}),
            Action(name="updateUserAddress", kwargs={"user_id": "ella_anderson_8460", "address": {"address1": "456 Ocean Ave", "address2": "", "city": "Miami", "state": "AL", "zip": "33101", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "standard"}),
            Action(name="createPendingOrder", kwargs={"user_id": "ella_anderson_8460", "item_details": [{"item_id": "8302289002", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_8302289002", "payment_method_id": "gift_card_8931217", "shipping_address": {"address1": "456 Ocean Ave", "address2": "", "city": "Miami", "state": "AL", "zip": "33101", "country": "USA"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_8302289002", "courier_id": "#COU0001"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_8302289002"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="international_shipping_complication",
        instruction="You are Ethan Patel with email id: ethan.patel9232@example.com, intending to send a Laptop (15-inch, i9, 32GB RAM, 512GB SSD) to your friend in Mexico as a gift. Organize the order using your PayPal account, but provide a special international shipping address: '123 Revolucion Ave, Mexico City, CDMX, 01000, Mexico'. Verify the delivery estimate for express service. However, after placing the order, you realize that the laptop might face import restrictions. Investigate if there's a similar yet less expensive laptop option under $2300, cancel the initial laptop from your order, and substitute it with the alternative to ship using express courier.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "ethan.patel9232@example.com"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["2913673670"]}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico", "delivery_option": "express"}),
            Action(name="createPendingOrder", kwargs={"user_id": "ethan_patel_1311", "item_details": [{"item_id": "2913673670", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_2913673670", "payment_method_id": "paypal_3720127", "shipping_address": {"address1": "123 Revolucion Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="cancelOrderItem", kwargs={"order_id": "#Wfd520c73_2913673670", "item_id": "2913673670"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop", "max_price": 2300}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico", "delivery_option": "express"}),
            Action(name="createPendingOrder", kwargs={"user_id": "ethan_patel_1311", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_3720127", "shipping_address": {"address1": "123 Revolucion Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "Mexico"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="wedding_shopping_spree_coordination",
        instruction="Assume you are Amelia Jackson (amelia.jackson3271@example.com) arranging for your wedding. Acquire various items: 2 Water Bottles for the bridal party, 1 Smart Thermostat for your new residence, and 1 Office Chair for your work-from-home setup. Procure the priciest options available for each item. Assemble the order utilizing your credit card ending in 8902. Nevertheless, ensure the thermostat is delivered to your new residence at '789 Wedding Lane, Houston, NM, 78701, USA' while other items reach your current location. Divide this into two distinct orders, handle the payments properly, and confirm both receive express delivery. Subsequently, integrate a PayPal account to your profile for subsequent purchases.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "amelia.jackson3271@example.com"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smart Thermostat"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Office Chair"}),
            Action(name="createPendingOrder", kwargs={"user_id": "amelia_jackson_6490", "item_details": [{"item_id": "3453331371", "quantity": 2}, {"item_id": "4274709903", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_34533313714274709903", "payment_method_id": "credit_card_8897086", "shipping_address": {"address1": "710 Sunset Drive", "address2": "Suite 176", "city": "Tucson", "country": "USA", "state": "AZ", "zip": "85034"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_34533313714274709903", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="createPendingOrder", kwargs={"user_id": "amelia_jackson_6490", "item_details": [{"item_id": "3377900078", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_3377900078", "payment_method_id": "credit_card_8897086", "shipping_address": {"address1": "789 Wedding Lane", "address2": "", "city": "Houston", "state": "NM", "zip": "78701", "country": "USA"}}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_3377900078", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "amelia_jackson_6490", "payment_method": {"source": "paypal"}}),
            Action(name="getUserOrders", kwargs={"user_id": "amelia_jackson_6490", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="tech_enthusiast_upgrade_path",
        instruction="Assign yourself as Omar Costa (omar.costa4147@example.com), a tech enthusiast eager to upgrade your equipment. You desire the priciest Laptop and Smartphone available. Nonetheless, begin by examining your purchase history to ascertain your total spending, then ensure these products are in stock. Compose the order, but note that your gift card ($68) is insufficient. Set up a new PayPal account, then methodically arrange the payment to involve both the gift card and PayPal, subsequently completing with express shipping.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "omar.costa4147@example.com"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "omar_costa_7446"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smartphone"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["1657832319", "1507389580"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "omar_costa_7446", "item_details": [{"item_id": "1657832319", "quantity": 1}, {"item_id": "1507389580", "quantity": 1}]}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "omar_costa_7446", "payment_method": {"source": "paypal"}}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "payment_method_id": "gift_card_5540683", "shipping_address": {"address1": "510 Hickory Lane", "address2": "Suite 712", "city": "San Diego", "country": "USA", "state": "NV", "zip": "92107"}}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "payment_method_id": "paypal_fd520c73"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_16578323191507389580", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="family_relocation_shopping",
        instruction="As Fatima Anderson (fatima.anderson5906@example.com), who is relocating to Portland, you must purchase items for your new residence: 1 Air Purifier, 1 Bookshelf, and 2 Office Chairs. Opt for the most expensive versions of each product. Begin by updating your address to '100 Portland Ave, Portland, OR, 98101, USA'. Proceed to create the order and pay with your credit card. Additionally, remember you need express delivery as your move is in 2 days. Obtain the express delivery estimates and dispatch the order. Update the shipping method and confirm the tracking details.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Fatima Anderson"}),
            Action(name="updateUserAddress", kwargs={"user_id": "fatima_anderson_6873", "address": {"address1": "100 Portland Ave", "address2": "", "city": "Portland", "state": "OR", "zip": "98101", "country": "USA"}}),
            Action(name="searchProductsByCategory", kwargs={"category": "Air Purifier"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Bookshelf"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Office Chair"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8302289002", "1768466237", "4274709903"], "quantities": [1, 1, 2]}),
            Action(name="createPendingOrder", kwargs={"user_id": "fatima_anderson_6873", "item_details": [{"item_id": "8302289002", "quantity": 1}, {"item_id": "1768466237", "quantity": 1}, {"item_id": "4274709903", "quantity": 2}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903", "payment_method_id": "credit_card_9557278", "shipping_address": {"address1": "100 Portland Ave", "address2": "", "city": "Portland", "state": "OR", "zip": "98101", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_830228900217684662374274709903"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="loyalty_customer_large_order",
        instruction="Being Isabella Thompson, a dedicated customer planning a significant purchase, you're interested in buying 3 T-Shirts, 2 Running Shoes, and 1 Laptop, ensuring to select the least costly version of each item. Start by reviewing your purchase history and revenue summary to assess your loyalty status, then create the order using your PayPal account. Due to the size of this order, adjust the laptop price to $2000 as a loyalty incentive. Calculate the estimates for express delivery and proceed to courier the package.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Isabella Thompson"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "isabella_thompson_1219"}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "isabella_thompson_1219"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Running Shoes"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8124970213", "9791469541", "6017636844"], "quantities": [3, 2, 1]}),
            Action(name="createPendingOrder", kwargs={"user_id": "isabella_thompson_1219", "item_details": [{"item_id": "8124970213", "quantity": 3}, {"item_id": "9791469541", "quantity": 2}, {"item_id": "6017636844", "quantity": 1}]}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "item_id": "6017636844", "new_price": 2000}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "payment_method_id": "paypal_3999493", "shipping_address": {"address1": "208 Cedar Street", "address2": "Suite 993", "city": "Oakland", "country": "USA", "state": "NV", "zip": "95119"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_812497021397914695416017636844", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="gift_return_exchange_workflow",
        instruction="You are Ava Martinez with email id: ava.martinez1495@example.com handling a gift situation. You've received a Bookshelf as a gift order with just one item in the order, but it's not the right size/style. Return the Bookshelf citing the reason 'gift exchange'. Next, explore available Bookshelves to identify the most expensive one and initiate a new order with your chosen Bookshelf. Nevertheless, you decide to also add a Water Bottle to this new order. Cancel the previous order and place a new one to include both items, opting for the most expensive water bottle. Use your credit card to make the payment. Lastly, since this is for personal use, apply for express delivery to your address.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "ava.martinez1495@example.com"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9336725"}),
            Action(name="processReturn", kwargs={"order_id": "#W9336725", "item_ids": ["7154215719"], "reason": "gift exchange"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Bookshelf"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["1768466237"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ava_martinez_5025", "item_details": [{"item_id": "1768466237", "quantity": 1}]}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="cancelOrderItem", kwargs={"order_id": "#Wfd520c73_1768466237", "item_id": "1768466237"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["1768466237", "3453331371"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ava_martinez_5025", "item_details": [{"item_id": "1768466237", "quantity": 1}, {"item_id": "3453331371", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_17684662373453331371", "payment_method_id": "credit_card_4147840", "shipping_address":{"address1":"418 Park Avenue","address2":"Suite 351","city":"Washington","country":"USA","state":"DC","zip":"20156"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_17684662373453331371", "courier_id": "#COU0001", "delivery_options": "express"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="subscription_business_bulk_order",
        instruction="You are Ahmad Russo coordinating a subscription box business. You require a bulk purchase of: 10 cotton T-Shirts of size M, and 2 least expensive 500ml stainless steel green color Water Bottles. Coordinate this bulk order with your credit card. Because this is for business, negotiate to bring down each T-shirt to $35 and each Water Bottle to $35. Determine if you qualify for bulk discounts by examining the top-selling products. Arrange for standard delivery. Track the order to ensure the continuity of business operations.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ahmad Russo"}),
            Action(name="getTopSellingProducts", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["9612497925", "7533802601"], "quantities": [10,2]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ahmad_russo_9620", "item_details": [{"item_id": "9612497925", "quantity": 10}, {"item_id": "7533802601", "quantity": 2}]}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "item_id": "9612497925", "new_price": 35}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "item_id": "7533802601", "new_price": 35}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "payment_method_id": "credit_card_9513926", "shipping_address": {"address1": "763 Broadway", "address2": "Suite 135", "city": "Pittsburgh", "country": "USA", "state": "OH", "zip": "19122"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_96124979257533802601", "courier_id": "#COU0001"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_96124979257533802601"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="emergency_replacement_order",
        instruction="Assume the role of Mason Martin with email : mason.martin9081@example.com who is experiencing an equipment emergency at work. Your Laptop has malfunctioned and requires replacement; procure the most cost-effective option. Since you're traveling, ensure it is delivered to a temporary address: '555 Hotel Drive, Las Vegas, NV, 89101, USA'. Search for a laptop priced under $2800, execute the purchase using your credit card. Obtain express delivery estimates and arrange for shipping. Additionally, due to the urgent nature, you are prepared to pay an additional $200 as an expedite fee. Ultimately, incorporate your PayPal into the user's profile as a payment method.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "mason.martin9081@example.com"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop", "max_price": 2800}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["6017636844"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "mason_martin_7882", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_6017636844", "item_id": "6017636844", "new_price": 2492.37}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "mason_martin_7882", "payment_method": {"source": "paypal"}}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "credit_card_3261838", "shipping_address": {"address1": "555 Hotel Drive", "address2": "", "city": "Las Vegas", "state": "NV", "zip": "89101", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#Wfd520c73_6017636844"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_6017636844"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="multi_gift_recipient_management",
        instruction="Act as Emma Thompson email: emma.thompson5798@example.com, coordinating holiday gifts for 3 distinct individuals. Assemble individual orders: 1) A Laptop for your brother (deliver to '111 Brother St, Detroit, MI, 48201, USA'), 2) Running Shoes for your sister (deliver to '222 Sister Ave, Boston, MA, 02101, USA'), and 3) A T-Shirt and Water Bottle combo for your friend (deliver to '333 Friend Rd, Portland, OR, 97201, USA'). Select the most affordable options, utilize your gift card for the T-shirt combo if feasible; otherwise, apply PayPal, and employ PayPal for the laptop. Ensure express shipping is used for all orders and monitor each shipment separately.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "emma.thompson5798@example.com"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Running Shoes"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="createPendingOrder", kwargs={"user_id": "emma_thompson_2250", "item_details": [{"item_id": "6017636844", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "payment_method_id": "paypal_2031016", "shipping_address": {"address1": "111 Brother St", "address2": "", "city": "Detroit", "state": "MI", "zip": "48201", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_6017636844", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="createPendingOrder", kwargs={"user_id": "emma_thompson_2250", "item_details": [{"item_id": "9791469541", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_9791469541", "payment_method_id": "paypal_2031016", "shipping_address": {"address1": "222 Sister Ave", "address2": "", "city": "Boston", "state": "MA", "zip": "02101", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_9791469541", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="createPendingOrder", kwargs={"user_id": "emma_thompson_2250", "item_details": [{"item_id": "8124970213", "quantity": 1}, {"item_id": "5758737025", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "payment_method_id": "gift_card_5715854", "shipping_address": {"address1": "333 Friend Rd", "address2": "", "city": "Portland", "state": "OR", "zip": "97201", "country": "USA"}}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "payment_method_id": "paypal_2031016"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_81249702135758737025", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getUserOrders", kwargs={"user_id": "emma_thompson_2250", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="post_purchase_customer_service",
        instruction="You are Ella Walker managing a problematic order. You placed an order for 3 items but need to return the Water Bottle because of a 'defective product'. Handle the return process to obtain a refund. Then, you wish to reorder a replacement water bottle, opting for the most expensive one. Browse through the available water bottles, coordinate a new order for your desired replacement, and set up standard shipping. As you are relocating next month, update your address to '999 New Home Blvd, Portland, OR, 98199, USA' before completing the new order. Additionally, review your overall purchase history to determine if you are eligible for loyalty benefits.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ella Walker"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W6798117"}),
            Action(name="processReturn", kwargs={"order_id": "#W6798117", "item_ids": ["8538875209"], "reason": "defective product"}),
            Action(name="updateUserAddress", kwargs={"user_id": "ella_walker_7541", "address": {"address1": "999 New Home Blvd", "address2": "", "city": "Portland", "state": "OR", "zip": "98199", "country": "USA"}}),
            Action(name="searchProductsByCategory", kwargs={"category": "Water Bottle"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["3453331371"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ella_walker_7541", "item_details": [{"item_id": "3453331371", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_3453331371", "payment_method_id": "paypal_9734841", "shipping_address": {"address1": "999 New Home Blvd", "address2": "", "city": "Portland", "state": "OR", "zip": "98199", "country": "USA"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_3453331371", "courier_id": "#COU0001"}),
            Action(name="analyzeCustomerPurchaseHistory", kwargs={"user_id": "ella_walker_7541"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="seasonal_inventory_shopping",
        instruction="You are Olivia Wilson organizing a home office setup for the winter season. You require several items but prefer to confirm their availability first. Browse and verify: 2 Office Chairs, 1 Laptop, 1 Air Purifier, and 1 Smart Thermostat. Proceed to order the least expensive options available. If any item is not in stock, locate alternatives within the same category. Execute the order using your PayPal account.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Olivia Wilson"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Office Chair"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Air Purifier"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smart Thermostat"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["4168944673", "6017636844", "9534205511", "4953074738"], "quantities": [2, 1, 1, 1]}),
            Action(name="createPendingOrder", kwargs={"user_id": "olivia_wilson_8847", "item_details": [{"item_id": "4168944673", "quantity": 2}, {"item_id": "6017636844", "quantity": 1}, {"item_id": "9534205511", "quantity": 1}, {"item_id": "4953074738", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_4168944673601763684495342055114953074738", "payment_method_id": "paypal_9039769", "shipping_address": {"address1": "984 Hickory Lane", "address2": "Suite 834", "city": "Jacksonville", "country": "USA", "state": "AL", "zip": "32165"}}),
            # Action(name="getDeliveryEstimate", kwargs={"country": "USA", "option": "express"}),
            # Action(name="retrieveCourierDetails", kwargs={"service_region": "USA"}),
            # Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_4168944673601763684495342055114953074738", "courier_id": "# Action(name="assignOrderFulfillment", kwargs={"order_id": "#Wfd520c73_4168944673601763684495342055114953074738", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="social_media_influencer_unboxing",
        instruction="As Ava Simpson (ava.simpson1498@example.com), a social media influencer planning on unboxing videos, obtain the top 10 best-selling products. You need to arrange products for content creation: 1 premium Laptop (highest priced available), 2 different Smartphones (least 2 priced ones), 1 Action Camera (most expensive one). Start by examining the top-selling products to grasp trends. Place the order using PayPal, but since this is for business content, opt for premium service - manually raise each laptop and smartphone price by $50 as 'content creation fee'. After adjusting the prices, rebalance the payment and request express delivery with a courier service. Track the order for content planning.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Ava Simpson"}),
            Action(name="getTopSellingProducts", kwargs={"limit": 10}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smartphone"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Action Camera"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["1657832319", "5339029584", "1507389580", "7523669277"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ava_simpson_2370", "item_details": [{"item_id": "1657832319", "quantity": 1}, {"item_id": "5339029584", "quantity": 1}, {"item_id": "1507389580", "quantity": 1}, {"item_id": "7523669277", "quantity": 1}]}),
            Action(name="getOrderDetails", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277"}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "1657832319", "new_price": 2779.32}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "5339029584", "new_price": 1178.99}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "item_id": "1507389580", "new_price": 1207.86}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "payment_method_id": "paypal_3738584", "shipping_address": {"address1": "464 Main Street", "address2": "Suite 450", "city": "Washington", "country": "USA", "state": "DC", "zip": "20171"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_1657832319533902958415073895807523669277"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="corporate_account_setup",
        instruction="As William Dean, set up a corporate account for your startup. You require office supplies: 5 Office Chairs, 3 Laptops. Order the highest priced office chair and 3 units of the single lowest priced laptop. Formulate this large corporate order and add a new corporate visa credit card with 9999 as the last 4 digits to your account. Given this is B2B, negotiate volume pricing by decreasing the office chair price to $350 each and laptop prices to $2000 each. Organize standard delivery but confirm all items are shipped to your business address: '777 Startup Lane, Houston, NM, 78702, USA'.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "William Dean"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Office Chair"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Laptop"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["4274709903", "6017636844"], "quantities": [5, 3]}),
            Action(name="createPendingOrder", kwargs={"user_id": "william_dean_7213", "item_details": [{"item_id": "4274709903", "quantity": 5}, {"item_id": "6017636844", "quantity": 3}]}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "william_dean_7213", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "9999"}}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "item_id": "4274709903", "new_price": 350}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "item_id": "6017636844", "new_price": 2000}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "payment_method_id": "credit_card_fd520c73", "shipping_address": {"address1": "777 Startup Lane", "address2": "", "city": "Houston", "state": "NM", "zip": "78702", "country": "USA"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_42747099036017636844", "courier_id": "#COU0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="cross_border_family_shopping",
        instruction="You are Raleigh Simpson email: Raleigh.simpson3664@example.com shopping for family members across different countries. Handle the creation of 2 separate international orders: 1) Smartphone to Mexico ('100 Maple St, Toronto, ON, M5H 2N2, Mexico'), 2) Running Shoes to Mexico ('200 Centro Ave, Mexico City, CDMX, 01000, Mexico'). Select the least expensive variant of each product. First, check delivery estimates for international shipping and ensure shipping for Mexico and Mexico orders. Track each order separately and verify international courier assignments.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "charlotte.simpson3664@example.com"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "Mexico"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smartphone"}),
            Action(name="searchProductsByCategory", kwargs={"category": "Running Shoes"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["5339029584", "9791469541"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "charlotte_simpson_2175", "item_details": [{"item_id": "5339029584", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_5339029584", "payment_method_id": "paypal_6262583", "shipping_address": {"address1": "100 Maple St", "address2": "", "city": "Toronto", "state": "ON", "zip": "M5H 2N2", "country": "Mexico"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "Mexico"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_5339029584", "courier_id": "#COU0002"}),
            Action(name="createPendingOrder", kwargs={"user_id": "charlotte_simpson_2175", "item_details": [{"item_id": "9791469541", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_9791469541", "payment_method_id": "paypal_6262583", "shipping_address": {"address1": "200 Centro Ave", "address2": "", "city": "Mexico City", "state": "CDMX", "zip": "01000", "country": "Mexico"}}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "Mexico"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_9791469541", "courier_id": "#COU0001"}),
            Action(name="getUserOrders", kwargs={"user_id": "charlotte_simpson_2175", "status": "processed"})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="damaged_shipment_emergency_reorder",
instruction="You are Liam Williams managing a shipping calamity. Your order # W7016806 sustained damage during shipping. The items are urgently required for a presentation tomorrow. Return the Bookshelf and Water Bottle, stating 'shipping damage' as the reason. Promptly reorder these items with overnight express shipping. Use your credit card for the transaction. Ship to your office address: '888 Business Plaza, Portland, OR, 98102, USA'. Monitor the order status. Ensure your gift card is set as a backup payment method for future purchases.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Liam Williams"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W7016806"}),
            Action(name="processReturn", kwargs={"order_id": "#W7016806", "item_ids": [ "5758737025", "4894369688"], "reason": "shipping damage"}),
            Action(name="validateOrderItems", kwargs={"item_ids": [ "5758737025", "4894369688"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "liam_williams_2067", "item_details": [{"item_id": "5758737025", "quantity": 1}, {"item_id": "4894369688", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_57587370254894369688", "payment_method_id": "credit_card_3956549", "shipping_address": {"address1": "888 Business Plaza", "address2": "", "city": "Portland", "state": "OR", "zip": "98102", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_57587370254894369688", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_57587370254894369688"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "liam_williams_2067", "payment_method": {"source": "gift_card"}})
        ],
        outputs=[]
    ),

    Task(
        annotator="customer_scenarios",
        user_id="last_minute_gift_coordination",
        instruction="You are Chen Williams with only 2 hours to organize a last-minute birthday gift. Arrange for a 6.5-inch black Smartphone and S size roundneck polyester T-Shirt combo to be delivered today to your friend's address: '123 Birthday Lane, Miami, AL, 33130, USA'. Verify product availability and place the order. Due to the high urgency, adjust the pricing by adding $300 to the smartphone and $50 to the T-shirt. Include the express courier option. Notice your PayPal lacks sufficient funds, so add your visa credit card with 7777 as the final 4 digits as a backup payment method and proceed with it.",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Chen Johnson"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "chen_johnson_8425", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "7777"}}),
            Action(name="searchProductsByCategory", kwargs={"category": "Smartphone"}),
            Action(name="searchProductsByCategory", kwargs={"category": "T-Shirt"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["5339029584", "1176194968"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "chen_johnson_8425", "item_details": [{"item_id": "5339029584", "quantity": 1}, {"item_id": "1176194968", "quantity": 1}]}),
            Action(name="getOrderDetails", kwargs={"order_id": "#Wfd520c73_53390295841176194968"}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "item_id": "5339029584", "new_price": 1428.99}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "item_id": "1176194968", "new_price": 102.88}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "payment_method_id": "credit_card_fd520c73", "shipping_address": {"address1": "123 Birthday Lane", "address2": "", "city": "Miami", "state": "AL", "zip": "33130", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_53390295841176194968", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#Wfd520c73_53390295841176194968"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_76",
        instruction="You are Evelyn Dean. You intend to add a new visa credit card ending with 6798 to your profile. You also plan to purchase a blue color, S size Cycling Helmet. Utilize your new credit card for the transaction and ensure it is shipped to your default address using Priority Shipping Co.. What is the new order's ID?",
        actions=[
            Action(name="searchUsers", kwargs={"name": "Evelyn Dean"}),
            Action(name="addPaymentMethodToUser", kwargs={"user_id": "evelyn_dean_4338", "payment_method": {"source": "credit_card", "brand": "visa", "last_four": "6798"}}),
            Action(name="searchProductsByCategory", kwargs={"category": "Cycling Helmet"}),
            Action(name="createPendingOrder", kwargs={"user_id": "evelyn_dean_4338", "item_details": [{"item_id": "5886093635", "quantity": 1}]}),
            Action(name="applyPaymentToOrder", kwargs={"order_id": "#Wfd520c73_5886093635", "payment_method_id": "credit_card_fd520c73", "shipping_address":  {
                                                                          "address1": "250 River Road",
                                                                          "address2": "Suite 668",
                                                                          "city": "Raleigh",
                                                                          "country": "USA",
                                                                          "state": "NC",
                                                                          "zip": "28230"
                                                                        }}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#Wfd520c73_5886093635", "courier_id": "#COU0003"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_77",
        instruction="You are a shipping manager. Retrieve the list of pending orders for user evelyn_dean_4338. Change their status to processing and calculate the estimate for express delivery along with the couriers who deliver to the address, then ship it. Also, obtain the total revenue for that user and acquire the tracking information for the shipped order.",
        actions=[
            Action(name="searchUsers", kwargs={"user_id": "evelyn_dean_4338"}),
            Action(name="getUserOrders", kwargs={"user_id": "evelyn_dean_4338", "status": "pending"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#W7634667", "new_status": "processing"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W7634667", "courier_id": "#COU0001", "delivery_options": "express"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W7634667"}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "evelyn_dean_4338"}),
            Action(name="getTrackingInfo", kwargs={"order_id": "#W7634667"})
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_78",
        instruction="You are a customer service representative. Implement a loyalty discount on a pending order for user 'aarav_rodriguez_2259', decreasing the price of the Vacuum Cleaner to $600.00. Process the refund to his PayPal account, update the order status to processing, get estimates for shipping, and assign a courier for shipment. Finally, verify the updated total revenue for this user.",
        actions=[
            Action(name="searchUsers", kwargs={"user_id": "aarav_rodriguez_2259"}),
            Action(name="getUserOrders", kwargs={"user_id": "aarav_rodriguez_2259", "status": "pending"}),
            Action(name="updateOrderItemPrice", kwargs={"order_id": "#W9672333", "item_id": "1345513440", "new_price": 600.00}),
            Action(name="adjustOrderPayment", kwargs={"order_id": "#W9672333", "payment_method_id": "paypal_7664977"}),
            Action(name="updateOrderStatus", kwargs={"order_id": "#W9672333", "new_status": "processing"}),
            Action(name="getCourierInfo", kwargs={"coverage_area": "USA"}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA"}),
            Action(name="assignFulfillmentToOrder", kwargs={"order_id": "#W9672333", "courier_id": "#COU0001"}),
            Action(name="getUserRevenueSummary", kwargs={"user_id": "aarav_rodriguez_2259"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator",
        user_id="TASK_79",
        instruction="As a purchasing manager, you've observed that item '9973034634' from supplier '#SUP0001' has only 36 units left. Boost the current inventory to 100 units to satisfy demand. Next, arrange a supply order for 200 units from this supplier at $30 per unit to maintain sufficient stock levels.",
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="updateInventory", kwargs={"supplier_id": "#SUP0001", "item_id": "9973034634", "new_stock": 100}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="getProductByItemId", kwargs={"item_id": "9973034634"}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0001", "product_id": "8940227892", "item_id": "9973034634", "quantity": 200, "unit_cost": 30}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0001"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_101",

        instruction="In your role as an operations specialist, identify all orders labeled 'cancelled'. Select the first 3 orders from this list, examine their details, and apply a bulk update to shift them to 'archived' status.",
        actions=[
            Action(name="getOrdersByStatus", kwargs={"status": "cancelled"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9978601"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9931224"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W9711842"}),
            Action(name="bulkOrderProcessing", kwargs={"order_ids": ["#W9978601", "#W9931224", "#W9711842"], "new_status": "archived"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="generator_01",
        user_id="TASK_102",

        instruction="As a customer service agent, you are tasked with managing a complex request from 'Ahmad Campbell' (ahmad.campbell2399@example.com). He needs to return the 'T-Shirt' from his delivered order as it 'Item does not fit'. Process this return. Following that, he intends to purchase a specific T-shirt (item_id: 8124970213). Set up a new pending order for this T-shirt. Additionally, he informs you of his relocation. Update his address to '999 Lakeview Dr, Houston, NM, 78701, USA'. Lastly, check the delivery estimates for an express shipment to his updated address.",
        actions=[
            Action(name="searchUsers", kwargs={"email": "ahmad.campbell2399@example.com"}),
            Action(name="getUserOrders", kwargs={"user_id": "ahmad_campbell_8900", "status":"delivered"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W1679211"}),
            Action(name="processReturn", kwargs={"order_id": "#W1679211", "item_ids": ["9612497925"], "reason": "Item does not fit"}),
            Action(name="getOrderDetails", kwargs={"order_id": "#W1679211"}),
            Action(name="validateOrderItems", kwargs={"item_ids": ["8124970213"]}),
            Action(name="createPendingOrder", kwargs={"user_id": "ahmad_campbell_8900", "item_details": [{"item_id": "8124970213", "quantity": 1}]}),
            Action(name="updateUserAddress", kwargs={"user_id": "ahmad_campbell_8900", "address": {"address1": "999 Lakeview Dr", "address2": "", "city": "Houston", "state": "NM", "zip": "78701", "country": "USA"}}),
            Action(name="getDeliveryEstimate", kwargs={"destination_country": "USA", "delivery_option": "express"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="5",
        user_id="TASK_103",
instruction="As a vendor manager, it is your responsibility to evaluate the performance for # SUP0003. Start by reviewing the supplier profile, product catalog, and existing inventory. Develop enhancement strategies by setting the price of the highest-priced Sneakers to $200. Order 60 units of that sneaker model at $150 each, update their contact number to +1-800-555-0010, and verify that the order placement is successfully confirmed."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="getProductDetails", kwargs={"product_id": "7471004230"}),
            Action(name="updateProductPrice", kwargs={"product_id": "7471004230", "item_id": "9727387530", "new_price": 200}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0003", "product_id": "7471004230", "item_id": "9727387530", "quantity": 60, "unit_cost": 150}),
            Action(name="updateSupplierContact", kwargs={"supplier_id": "#SUP0003", "phone": "+1-800-555-0010"}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0003"})
        ],
        outputs=[]
    ),

    Task(
        annotator="5",
        user_id="TASK_104",
instruction="As a product lifecycle manager, evaluate suppliers #SUP0012 and # Retrieve details, available products, and stock levels for SUP0012 and #SUP0008. Analyze their product offerings — Fleece Jacket and Desklamp. Set the price of the highest-priced Fleece Jacket to $150 and place a supply order for 25 units of the Desk lamp variant id: 4385534692 at $100 each, then confirm the order placement."
        actions=[
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="getSupplierInfo", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="listProductsBySupplier", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="getStockLevels", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="getProductDetails", kwargs={"product_id": "8560156827"}),
            Action(name="getProductDetails", kwargs={"product_id": "6817146515"}),
            Action(name="updateProductPrice", kwargs={"product_id": "8560156827", "item_id": "9385662952", "new_price": 150}),
            Action(name="createSupplyOrder", kwargs={"supplier_id": "#SUP0008", "product_id": "6817146515", "item_id": "4385534692", "quantity": 25, "unit_cost": 100}),
            Action(name="getPendingSupplyOrders", kwargs={"supplier_id": "#SUP0008"}),
        ],
        outputs=[]
    )
]