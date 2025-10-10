from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_0001",
        instruction="You are Henry Adams. It's 2025-07-20T16:35:00Z. A customer, Ava Thompson, returns a defective UltraVision 55\" 4K Smart TV to STORE-001. After processing the refund, update the product status to 'inactive', and create a 10% discount called 'Return Discount - Ava Thompson' for their next purchase, only applicable to the same product for the next month.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Ava Thompson"}, "info_items": ["customer_id", "email"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "UltraVision 55\" 4K Smart TV"}, "info_items": ["sku"]}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": 1, "current_time": "2025-07-20T16:35:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}, "info_items": ["transaction_id"]}),
            Action(name="create_refund_transaction", kwargs={"sku": "ELEC-4KTV55", "quantity": 1, "employee_id": "EMP-1020", "current_time": "2025-07-20T16:35:00Z", "original_transaction_id": "TXN-0001"}),
            Action(name="edit_products_db", kwargs={"sku": "ELEC-4KTV55", "status": "inactive", "current_time": "2025-07-20T16:35:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Return Discount - Ava Thompson", "type": "percentage", "discount_value": 10.0, "applicable_skus": ["ELEC-4KTV55"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0002",
        instruction="A new shipment of 20 BrewMaster 12-Cup Coffee Makers arrives at STORE-003. It's 2025-07-20T16:35:00Z. Create a new inventory item for them and add the new stock to it. Charlie Brown is the Delivery Driver and would like to be added to the employee database so that he can make use of the 'Employee Discount', which gives a discount of 10% off the coffee maker for the next year. You notice the discount hasn't been added to the database yet, so you create it.",
        actions=[
            # Get the product SKU for BrewMaster 12-Cup Coffee Maker
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "BrewMaster 12-Cup Coffee Maker"}, "info_items": ["sku"]}),
            # Create new inventory item for BrewMaster 12-Cup Coffee Maker in STORE-003 using edit_inventory_db
            Action(name="edit_inventory_db", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "quantity": 20, "current_time": "2025-07-20T16:35:00Z"}),
            # Add Charlie Brown as an employee
            Action(name="edit_employees_db", kwargs={"name": "Charlie Brown", "role": "Delivery Driver", "store_id": "STORE-003"}),
            # Create the 'Employee Discount' promotion for BrewMaster 12-Cup Coffee Maker
            Action(name="edit_promotions_db", kwargs={"name": "Employee Discount", "type": "percentage", "discount_value": 10.0, "applicable_skus": ["HOM-COFMKR12"], "start_date": "2025-07-20", "end_date": "2026-07-20"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0003",
        instruction="You are Amelia Lee. The time is 2025-07-20T16:35:00Z. A customer, Ava Thompson, purchases a GigaPlay 15\" Gaming Laptop from STORE-002 using her credit_card. The 1500 loyalty points from this purchase upgrades her to a platinum membership. Document the purchase and update her membership status and loyalty points, get her email address in order to send a congratulatory email.",
        actions=[
            # Get Ava Thompson's customer ID, email and loyalty points
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Ava Thompson"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            # Get the GigaPlay 15" Gaming Laptop SKU
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "GigaPlay 15\" Gaming Laptop"}, "info_items": ["sku"]}),
            # Get Amelia Lee's employee ID
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Create purchase transaction for Ava Thompson
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5001", "employee_id": "EMP-1032", "items": {"ELEC-GAMLP15": 1}, "store_id": "STORE-002","payment_method": "credit_card","current_time": "2025-07-20T16:35:00Z",}),
            # Update stock
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T16:35:00Z"}),
            # Update Ava Thompson's loyalty points and membership status
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "loyalty_points": 2740, "membership_level": "platinum", "current_time": "2025-07-20T16:35:00Z"}),
        ],
        outputs=[{"email": "ava.thompson@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0004",
        instruction="A new employee, Jack Thomas is hired as 'Customer Experience Specialist' for STORE-005. Add them to the employee database at 2025-07-20T16:41:00Z. They also want to purchase a WaveSound All-Weather Bluetooth Speaker from the store, so you add them as a customer, using their new employee email address. You then help log the purchase, which is made using both their customer_id and their employee_id, and a paid with a debit_card. You also want Jack's email so they can make a note of it.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Jack Thomas", "role": "Customer Experience Specialist", "store_id": "STORE-005"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Jack Thomas"}, "info_items": ["employee_id", "email"]}),
            Action(name="edit_customers_db", kwargs={"name": "Jack Thomas", "email": "jack.thomas@retailpos.com", "current_time": "2025-07-20T16:41:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "WaveSound All-Weather Bluetooth Speaker"}, "info_items": ["sku"]}),
            Action(name="create_purchase_transaction", kwargs={"employee_id": "EMP-1013", "customer_id": "CUST-5013", "items": {"AUDIO-BTSPKR02": 1}, "store_id": "STORE-005", "current_time": "2025-07-20T16:41:00Z", "payment_method": "debit_card"}),
            # reduce inventory for WaveSound All-Weather Bluetooth Speaker
            Action(name="update_inventory_item", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005", "quantity_change": -1, "current_time": "2025-07-20T16:41:00Z"}),
        ],
        outputs=[{"email":"jack.thomas@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0005",
        instruction="You are Grace Miller. The time is 2025-07-20T16:35:00Z in STORE-001. A customer, Olivia Patel is moving to a new address: 123 Elm St, Springfield, IL. Update their profile, get their email so you can send a confirmation email, but they would like to opt-out of marketing emails as they will be some distance from a store. Olivia would like to buy LumiLux LED Desk Lamp and use all of her loyalty points to reduce the price by 1 cent per loyalty point, and pay the rest via credit_card. You should create the transaction as normal, then update it, adding the loyalty points discount to the discount total and reduce the price accordingly.",
        actions=[
            # Get customer_id and email, and loyalty points for olivia patel
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Olivia Patel"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            # Update address and marketing opt_in
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5003", "address": "123 Elm St, Springfield, IL", "opt_in_marketing": False, "current_time": "2025-07-20T16:35:00Z"}),
            # Get sku for LumiLux LED Desk lamp
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "LumiLux LED Desk Lamp"}, "info_items": ["sku", "price"]}),
            # Get employee_id for Grace Miller
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Grace Miller"}, "info_items": ["employee_id"]}),
            # Create a purchase transaction
            Action(name="create_purchase_transaction", kwargs={"employee_id": "EMP-1002", "customer_id": "CUST-5003", "items": {"HOME-DESKLMP01": 1}, "store_id": "STORE-001", "current_time": "2025-07-20T16:36:00Z", "payment_method": "credit_card"}),
            # Update the inventory for LumiLux LED Desk Lamp
            Action(name="update_inventory_item", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001", "quantity_change": -1, "current_time": "2025-07-20T16:37:00Z"}),
            # Edit the purchase transaction discount_total and total_price (460 loyalty points = $4.60 discount)
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-1013", "discount_total": 7.40, "total_amount": 30.48, "current_time": "2025-07-20T16:37:00Z"}),
            # Remove 460 loyalty points from Olivia Patel's account
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5003", "loyalty_points": 0, "current_time": "2025-07-20T16:37:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0006",
        instruction="You are Megan Young. The time is 2025-04-30T16:40:00Z in STORE-002. You want to check if any customers have their birthday today. If any do, get their email address so later you can send them a information about a birthday discount. Create the discount with 20% off all products for today only, and call it '<customer_name> Birthday Discount'. This reminds you that it is your cousin, Frank Mitchell's, birthday today, so you want to make him an account using his email 'frank@email.com' and buy him something from the 'Electronics' section of the store from the 'QuietTone' brand. You make the purchase using your employee_id, and pay with a credit_card and are sure to reduce the inventory count.",
        actions=[
            Action(name="get_customers_with_birthday_today", kwargs={"current_day": "04-30"}),
            # Get the customer email address
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email", "name"]}),
            # Create the birthday discount
            Action(name="edit_promotions_db", kwargs={"name": "William Zhang Birthday Discount", "type":"percentage", "discount_value": 20, "applicable_skus":[],"start_date": "2025-04-30", "end_date": "2025-04-30"}),
            #create Frank Mitchell's customer account
            Action(name="edit_customers_db", kwargs={"name": "Frank Mitchell", "email": "frank@email.com", "current_time": "2025-04-30T16:40:00Z"}),
            # Get the QuietTone brand products in Electronics
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"brand": "QuietTone", "category": "Electronics"}, "info_items": ["sku"]}),
            # Get Megan Young's employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["employee_id"]}),
            # Create the purchase transaction for Frank Mitchell
            Action(name="create_purchase_transaction", kwargs={"employee_id": "EMP-1045", "customer_id": "CUST-5013", "items": {"AUDIO-NCEBUDS01": 1}, "store_id": "STORE-002", "current_time": "2025-04-30T16:40:00Z", "payment_method": "credit_card"}),
            # Update the inventory for the purchased product
            Action(name="update_inventory_item", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-04-30T16:40:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0007",
        instruction="You are Natalie Cooper. It is 2025-07-20T16:45:00Z. You receive a call from a customer, Liam Nguyen, who wants to return a defective ProSlice 8\" Chef Knife product, and be completely removed from your database. You need to process the return and update the inventory. Then, because you are fed up with the defective knives, you set the reorder level for the knife to 0 and change the status to 'last_stock'. To sell them faster you also create a promotion called 'End of stock Discount' for 15% off the knives, valid for the next year. You also want to get Liam's email address so you can send him a confirmation email.",
        actions=[
            # Get Liam Nguyen's customer_id
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Liam Nguyen"}, "info_items": ["customer_id", "email"]}),
            # Get the product SKU for ProSlice 8" Chef Knife
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "ProSlice 8\" Chef Knife"}, "info_items": ["sku"]}),
            # Get the transaction ID for the purchase of ProSlice 8" Chef Knife
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5002", "sku": "KITCH-CHEFKNF8"}, "info_items": ["transaction_id"]}),
            # Get Natalie Cooper's employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["employee_id"]}),
            # Process the return using create_refund_transaction
            Action(name="create_refund_transaction", kwargs={"sku": "KITCH-CHEFKNF8", "quantity": 1, "employee_id": "EMP-1004", "original_transaction_id": "TXN-0002", "current_time": "2025-07-20T16:45:00Z"}),
            # Remove the customer from the database
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5002", "delete": True}),
            # Update the inventory
            Action(name="update_inventory_item", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002", "quantity_change": 1, "current_time": "2025-07-20T16:45:00Z"}),
            # Set reorder level to 0 and change status to 'last_stock'
            Action(name="edit_inventory_db", kwargs={"id": "INV-0011", "status": "last_stock", "reorder_level": 0, "current_time": "2025-07-20T16:45:00Z"}),
            # Create the promotion 'End of stock Discount'
            Action(name="edit_promotions_db", kwargs={"name": "End of stock Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["KITCH-CHEFKNF8"], "start_date": "2025-07-20", "end_date": "2026-07-20"}),
        ],
        outputs=["liam.nguyen@example.com"]
    ),
    Task(
        annotator="0",
        user_id="task_0008",
        instruction= "The current time is 2025-07-02T07:30:00Z. You are Grace Miller and want to reward customers who have spent more than $1500 in your shop. You decide the best way to do this is to give them a 20% discount on the KITCH-CHEFKNF8 product in the next month. You would like to create this promotion and call it 'My Favourite Customers' then get the email addresses of the customers who qualify for it so they can be made aware of the deal.",
        actions=[
            # Get all customers who have spent more than $1500 using GetCustomersAboveXSpend
            Action(name="get_customers_above_x_spend", kwargs={"amount": 1500}),
            # Create the promotion 'My Favourite Customers'
            Action(name="edit_promotions_db", kwargs={"name": "My Favourite Customers", "type": "percentage", "discount_value": 20, "applicable_skus": ["KITCH-CHEFKNF8"], "start_date": "2025-07-02", "end_date": "2025-08-02"}),
            # Get the email addresses of these customers
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5005"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"emma.garcia@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0009",
        instruction="You are Daniel Perez. The time is 2025-07-20T16:50:00Z. A customer, Charlotte Dubois, wants to return 10 defective UltraSoft Cotton Bath Towels that she bought from this store. You need to process the return, update the inventory, and get her email address to send a confirmation email. Check if the towels are in the store inventory, if not, make an item for them and add the returns to it. After that, you want to create a promotion called 'Bath Towel Return Discount' for 10% off on the purchase of the bath towel product for the next year.",
        actions=[
            # Get Charlotte Dubois's customer_id
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id"]}),
            # Get the product SKU for UltraSoft Cotton Bath Towel
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "UltraSoft Cotton Bath Towel"}, "info_items": ["sku"]}),
            # Get the transaction ID for the purchase of UltraSoft Cotton Bath Towel
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5009", "sku": "HOME-BTHTWL01"}, "info_items": ["transaction_id"]}),
            # Get Daniel Perez's employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Daniel Perez"}, "info_items": ["employee_id"]}),
            # Process the return using create_refund_transaction
            Action(name="create_refund_transaction", kwargs={"sku": "HOME-BTHTWL01", "quantity": 10, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0009", "current_time": "2025-07-20T16:50:00Z"}),
            # Check if the product is in the inventory
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "HOME-BTHTWL01", "store_id": "STORE-004"}, "info_items": ["sku"]}),
            # If not in inventory, create a new inventory item for UltraSoft Cotton
            Action(name="edit_inventory_db", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-004", "quantity": 10, "current_time": "2025-07-20T16:50:00Z"}),
            # Create the promotion 'Bath Towel Return Discount' using edit_promotions_db
            Action(name="edit_promotions_db", kwargs={"name": "Bath Towel Return Discount", "type": "percentage", "discount_value": 10, "applicable_skus": ["HOME-BTHTWL01"], "start_date": "2025-07-20", "end_date": "2026-07-20"}),
            # Get Charlotte Dubois's email address
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"charlotte.dubois@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0010",
        instruction="You are Oliver Diaz. The time is 2025-07-20T16:55:00Z. A new employee, Ava Thompson, has joined as a Sales Associate working in the 'Home & Kitchen' section in STORE-001. Add her to the employee database. Also, create a promotion called 'New Employee Welcome Discount' for 15% off on any product in the 'Home & Kitchen' category for the next month. Then get Ava's email address so you can send her a welcome email.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Ava Thompson", "role": "Sales Associate", "store_id": "STORE-001"}),
            # Get Home & Kitchen products
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Home & Kitchen"}, "info_items": ["sku"]}),
            # Create the promotion 'New Employee Welcome Discount'
            Action(name="edit_promotions_db", kwargs={"name": "New Employee Welcome Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
            # Get Ava's email address
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Ava Thompson"}, "info_items": ["email"]})
        ],
        outputs=[{"email":"ava.thompson@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0011",
        instruction="A new product, 'EcoBrew Reusable Coffee Filter', has recently become available. The time is 2025-07-20T16:55:00Z. You want to document it in the product database using the information the manufacturer provided. The product is described as:'An eco-friendly reusable coffee filter made from organic cotton, designed to fit most standard coffee makers.' It is from the same suppliers as the 'BrewMaster 12-Cup Coffee Maker', weighs 100 grams and costs $3.50 for the store to buy, so you price it at $5.99. You have ordered 100 units of this product to stock in the 'Kitchen & Dining' section of STORE-001. Then get all of the names and email addresses of customers who have purchased the 'BrewMaster 12-Cup Coffee Maker', so you can send them an email about the new product.",
        actions=[
            # Get the supplier_id for BrewMaster 12-Cup Coffee Maker
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "BrewMaster 12-Cup Coffee Maker"}, "info_items": ["supplier_id", "sku"]}),
            Action(name="edit_products_db", kwargs={"name": "EcoBrew Reusable Coffee Filter", "description": "An eco-friendly reusable coffee filter made from organic cotton, designed to fit most standard coffee makers.", "supplier_id": "SUP-1002", "weight_kg": 0.1, "cost": 3.50, "price": 5.99, "current_time": "2025-07-20T16:55:00Z"}),
            # get the SKU for the new product
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "EcoBrew Reusable Coffee Filter"}, "info_items": ["sku"]}),
            # Add the new product to the inventory in STORE-001
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity": 100, "current_time": "2025-07-20T16:55:00Z", "location": "Kitchen & Dining"}),
            # Get the email addresses of customers who have purchased BrewMaster 12-Cup Coffee Maker using GetCustomerPurchaseCountBySku
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            # Get the email addresses of these customers
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["name", "email"]})
        ],
        outputs=[{"name": "Liam Nguyen", "email": "liam.nguyen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0012",
        instruction="There has been a robbery and the whole inventory of the top 3 most expensive products in STORE-003 have been stolen. The time is 2025-07-20T16:56:00Z. Update the inventory to reflect this and set the status of the inventory items to 'stolen'. Then perform a low stock check. For any item in the store that has the status 'low_stock' or 'critical', change the product to remove any discount. Then find the email addresses of the Floor Supervisor of the store so they can be notified.",
        actions=[
            # Get the top 3 most expensive products in STORE-003
            Action(name="get_top_n_most_expensive_products_by_store", kwargs={"store_id": "STORE-003", "n": 3}),
            # get inventory ids for these products
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": ["KITCH-FRYPAN10", "OFFC-ERGCHR01", "ELEC-RCHAA04"], "store_id": "STORE-003"}, "info_items": ["id"]}),
            # Update the inventory to reflect the stolen products
            Action(name="edit_inventory_db", kwargs={"id": "INV-0023", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0014", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0020", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            # Perform a low stock check
            Action(name="check_low_stock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T16:56:00Z"}),
            # Remove discounts for low stock or critical items
            Action(name="edit_products_db", kwargs={"sku": "KITCH-FRYPAN10", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="edit_products_db", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="edit_products_db", kwargs={"sku": "ELEC-RCHAA04", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            # Find the email addresses of the Floor Supervisor
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003", "position": "Floor Supervisor"}, "info_items": ["email"]})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0013",
        instruction="You are Jack Robinson. The time is 2025-07-20T16:57:00Z. You want to create a 'Loyalty point multiplier' type promotion for for the next 7 days, where loyalty points are worth 5 times as much as normal (normally 1 cent per point, so now 5 cents per point). A customer, Sophia Rossi, wants to purchase PowerPlus Rechargeable AA Batteries (4 Pack) from STORE-003 using her loyalty points. You need to create the transaction, update the inventory. Then use the total amount to calculate the amount of loyalty points it cost (rounding up any fractions), and update Sophia's record with the loyalty points taken off. Then get her email address to send a confirmation email.",
        actions=[
            # Create the 'Loyalty point multiplier' promotion
            Action(name="edit_promotions_db", kwargs={"name": "Loyalty point multiplier", "type": "loyalty_multiplier", "discount_value": 5, "start_date": "2025-07-20", "end_date": "2025-07-27", "applicable_skus": []}),
            # Get Sophia's email, customer_id and loyalty points
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Sophia Rossi"}, "info_items": ["customer_id","email", "loyalty_points"]}),
            # Get Jacks employee ID
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            # Get the SKU for PowerPlus Rechargeable AA Batteries (4 Pack)
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}, "info_items": ["sku"]}),
            # Create the transaction
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5007", "items": {"ELEC-RCHAA04":1}, "store_id": "STORE-003", "employee_id": "EMP-1034", "current_time": "2025-07-20T16:57:00Z", "payment_method": "loyalty_points"}),
            # Update the inventory
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T16:57:00Z"}),
            # Might need to make an API function for the maths here
            # Edit Sophia's loyalty points to reflect the purchase
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5007", "loyalty_points": 26, "current_time": "2025-07-20T16:57:00Z"}),  # Assuming the cost is fully covered by loyalty points
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0014",
        instruction="You are Emma Garcia. The time is 2025-07-06T16:58:00Z. You want to check the current percentage type promotions. If there is a promotion called 'Summer Electronics Sale', you want to update it to add 10% to the discount value. If it doesn't exist, create a new promotion called 'Summer Sale' with a 25% discount on all products for the next month. Then get the email addresses of customers who have purchased products during the last month so you can notify them about the updated promotion.",
        actions=[
            # Check if the 'Summer Electronics Sale' promotion exists
            Action(name="get_promotions_info_by_param", kwargs={"filter_params": {"name": "Summer Electronics Sale"}, "info_items": ["promotion_id", "discount_value"]}),
            # Update the promotion
            Action(name="edit_promotions_db", kwargs={"promotion_id": "PROMO-001", "discount_value": 20}),
            # Get customer_ids and timestamps of purchases
            Action(name="get_transactions_info_by_param", kwargs={"filter_params":{}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates":{ "CUST-5001": "2025-06-05", "CUST-5002": "2025-06-05", "CUST-5003": "2025-06-05", "CUST-5004": "2025-06-05", "CUST-5005": "2025-06-05", "CUST-5006": "2025-06-05", "CUST-5007": "2025-06-05", "CUST-5008": "2025-06-05", "CUST-5009": "2025-06-05", "CUST-5010": "2025-06-05", "CUST-5011": "2025-06-06", "CUST-5012": "2025-06-06"},"filter_start_date": "2025-06-06", "filter_end_date": "2025-07-06"}),
            # Get email addresses of customers who purchased during the last month
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5011", "CUST-5012"]}, "info_items": ["email"]}),
        ],
        outputs=[
            {"emails": ["mia.kim@example.com", "logan.smith@example.com"]}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_0015",
        instruction="You are Liam Nguyen. The time is 2025-07-20T16:59:00Z. You want to check the inventory quantity information of all products in STORE-004. If any product has a quantity below 5, you order 10 more and add these to the quantity and mark it's status as 'in_stock'. Additionally, you want to get the email addresses of all employees from the store so you can inform them of the order.",
        actions=[
            # Get all products in STORE-004 with their inventory levels
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "quantity"]}),
            # Filter products with quantity below 5
            Action(name="edit_inventory_db", kwargs={"id": "INV-0009", "quantity": 14, "status": "in_stock", "current_time": "2025-07-20T16:59:00Z"}),
            # Get the email addresses of all employees in STORE-004
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"amelia.lee@retailpos.com"}, {"email":"jack.robinson@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0016",
        instruction="You are Olivia Patel. The time is 2025-07-20T17:00:00Z. You want to check the sales performance of STORE-002. If the total all time sales are below $10,000, you want to create a promotion called 'Sales Boost' with a 15% discount on all products for the next two weeks. Then, get the email addresses of customers who have purchased products in STORE-002 so you can notify them about the new promotion.",
        actions=[
            # Get all transactions in for STORE-002
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["total_amount", "customer_id"]}),
            # Get total sales for STORE-002 in the last month

            # Create the appropriate promotion based on sales performance
            Action(name="edit_promotions_db", kwargs={"name": "Sales Boost", "type": "percentage", "discount_value": 15, "start_date": "2025-07-20", "end_date": "2025-08-03", "applicable_skus": []}),
            # Get email addresses of customers who purchased in STORE-002 during the last month
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5011", "CUST-5002", "CUST-5006"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "mia.kim@example.com"}, {"email": "william.zhang@example.com"}, {"email": "liam.nguyen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0017",
        instruction="You are Henry Adams. The time is 2025-07-20T17:00:00Z at STORE-003. You just found that 40 of the 'High-Protein Granola Bars (12 Pack)' were eaten by mice overnight. Update the inventory to reflect this. Then perform a low stock check on the inventory of STORE-003. If any item is low_stock, find the name and email of the Inventory Specialist for the store and then removed them from the employee database as they are fired. Return their name and email and phone number so they can be informed. Change your role to 'Inventory Specialist' to replace them and update your employee record with the new role.",
        actions=[
            # Get the SKU for High-Protein Granola Bars (12 Pack)
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "High-Protein Granola Bars (12 Pack)"}, "info_items": ["sku"]}),
            # Update the inventory to reflect the eaten products
            Action(name="update_inventory_item", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -40, "current_time": "2025-07-20T17:00:00Z"}),
            # Perform a low stock check
            Action(name="check_low_stock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T17:00:00Z"}),
            # Get the Inventory Specialist's name and email
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Inventory Specialist"}, "info_items": ["name", "email", "phone_number", "employee_id"]}),
            # Remove the Inventory Specialist from the employee database
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1015", "delete": True}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1020", "role": "Inventory Specialist"}),
        ],
        outputs=[{"name": "Zoe Martinez", "email": "zoe.martinez@retailpos.com", "phone_number": "+1-555-210-1015"}]
    ),
    Task(
        annotator="0",
        user_id="task_0018",
        instruction="You are Emma Garcia. The time is 2025-07-20T17:01:00Z. You want to edit a transaction in the database. The transaction ID is TXN-0012, and you want to change the total amount to $150.00. Additionally, you want to get the email address of the customer associated with this transaction so you can notify them about the change.",
        actions=[
            # Get the transaction details by transaction ID
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"transaction_id": "TXN-0012"}, "info_items": ["customer_id"]}),
            # Edit the transaction total amount
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0012", "total_amount": 150.00, "current_time": "2025-07-20T17:01:00Z"}),
            # Get the customer email address associated with the transaction
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["email"]}),
        ],
        outputs=[{"logan.smith@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0019",
        instruction="You are Liam Nguyen. The time is 2025-07-20T17:02:00Z. You want to create a new product in the database. The product details are as follows: Name: 'Wireless Mouse', Price: $25.00, leave the other values as default. You have received 100 units of this product to stock in the 'Electronics' location of STORE-001. Create the inventory item accordingly. If store STORE-002 has stock of the product with SKU 'AUDIO-NCEBUDS01', then half of the 'Wireless Mouse' stock is moved to STORE-002. Create an inventory item for STORE-002 to document this and keeping other information the same, and update the quantity in STORE-001 ",
        actions=[
            # Create the new product in the database
            Action(name="edit_products_db", kwargs={"name": "Wireless Mouse", "price": 25.00, "current_time": "2025-07-20T17:02:00Z"}),
            # Create inventory for product
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity": 100, "current_time": "2025-07-20T17:02:00Z", "location": "Electronics"}),
            # Check if STORE-002 has stock of AUDIO-NCEBUDS01
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01"}, "info_items": ["quantity"]}),
            # If it does, move half of the stock to STORE-002
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021", "store_id": "STORE-002", "quantity": 50, "current_time": "2025-07-20T17:02:00Z", "location": "Electronics"}),
            # If it does, update the quantity in STORE-001
            Action(name="update_inventory_item", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity_change": -50, "current_time": "2025-07-20T17:02:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0020",
        instruction="You are Amelia Lee. The time is 2025-07-20T17:03:00Z. You want to create a new promotion for all products in the 'Books'. The promotion details are as follows: Name: 'Back to School Sale', Type: 'percentage', Discount Value: 20, Start Date: 2025-08-01, End Date: 2025-08-31. Additionally, you want to get the email addresses of any customer that has bought a book product so you can notify them about the new promotion.",
        actions=[
            # Get all book products
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Books"}, "info_items": ["sku"]}),
            # Create the new promotion in the database
            Action(name="edit_promotions_db", kwargs={"name": "Back to School Sale", "type": "percentage", "discount_value": 20, "start_date": "2025-08-01", "end_date": "2025-08-31", "applicable_skus": ["BOOK-KDSSTY01"]}),
            # Get the email addresses of customers who have purchased book products
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "BOOK-KDSSTY01"}),
            # Create a list of customer IDs who have purchased books
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5008"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "james.oconnor@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0021",
        instruction="The time is 2025-07-20T17:04:00Z. You want to get a list of customers who have spent more than $750. Additionally, you want to get their email addresses so you can notify them about an upcoming sale. Then create a promotion called 'VIP Customer Sale' with a 10% discount on all products for the next month.",
        actions=[
            # Get customers who have spent more than $750
            Action(name="get_customers_above_x_spend", kwargs={"amount": 750.0}),
            # Get the email addresses of these customers
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001","CUST-5005"]}, "info_items": ["email"]}),
            # Create the 'VIP Customer Sale' promotion
            Action(name="edit_promotions_db", kwargs={"name": "VIP Customer Sale", "type": "percentage", "discount_value": 10, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[{"email": "emma.garcia@example.com"}, {"email": "ava.thompson@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0022",
        instruction="You are Oliver Diaz. The time is 2025-07-20T17:05:00Z. You want to check the inventory quantity levels of all products in STORE-001. If any product has a quantity below 10, you want to return the SKU and quantity of that product so it can be reordered. You also want to update the last_stock_count to today for the items that are reordered. Find how many employees work in STORE-001, if it is less than 10, add you friend 'Marty Skipper' as a new employee in the role of 'Inventory Specialist' at the store.",
        actions=[
            # Get all products in STORE-001 with their inventory levels
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["id","sku", "quantity"]}),
            # Update last stock count for items that need to be reordered
            Action(name="edit_inventory_db", kwargs={"id": "INV-0001", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:05:00Z"}),
            # Check the number of employees in STORE-001
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["employee_id"]}),
            # If less than 10 employees, add Marty Skipper as a new employee
            Action(name="edit_employees_db", kwargs={"name": "Marty Skipper", "role": "Inventory Specialist", "store_id": "STORE-001"}),

        ],
        outputs=[{"sku": "ELEC-4KTV55","quantity": 8,}]
    ),
    Task(
        annotator="0",
        user_id="task_0023",
        instruction="You are Natalie Cooper. The time is 2025-07-20T17:06:00Z. You want to analyze your customer base and find if there is a link between the the top customer by loyalty points and the customer who bought your store's most expensive product the most. You work at STORE-003. You want to get the email addresses of the 'Floor Supervisor' and return it so you can email them your analysis later. If the top customer by loyalty points is not the same as the one that bought the most expensive product the most times, you want to create a purchase transaction to buy yourself the 'High-Protein Granola Bars (12 Pack)' with your credit_card to console yourself. If you are not on the customer database, you want to add yourself as a customer first using your employee email address.",
        actions=[
            # Get the top customer by loyalty points
            Action(name="get_top_n_customers_by_loyalty_points", kwargs={"n": 1}),
            # Get the store's most expensive product
            Action(name="get_top_n_most_expensive_products_by_store", kwargs={"store_id": "STORE-003", "n": 1}),
            # Get the customer who bought the most of the most expensive product
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            # check if Natalie Cooper is in the customer database
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["customer_id"]}),
            # Get Natalie Cooper's employee email address to use
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["email"]}),
            # If not, add Natalie Cooper as a customer
            Action(name="edit_customers_db", kwargs={"name": "Natalie Cooper", "email": "natalie.cooper@retailpos.com", "current_time": "2025-07-20T17:06:00Z"}),
            # Create a purchase transaction for Natalie Cooper if she is not the same as the top customer by loyalty points
            # get product SKU for High-Protein Granola Bars (12 Pack)
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "High-Protein Granola Bars (12 Pack)"}, "info_items": ["sku"]}),
            # get Natalie Cooper's employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["employee_id"]}),
            # Create the purchase transaction
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5013", "items": {"GROC-GRNLBR12": 1}, "store_id": "STORE-003", "employee_id": "EMP-1004", "current_time": "2025-07-20T17:06:00Z", "payment_method": "credit_card"}),
            # Update the inventory for the purchase
            Action(name="update_inventory_item", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T17:06:00Z"}),
            # Get the email address of the Department Manager
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Floor Supervisor"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "henry.adams@retailpos.com"}]
    ),
    # task that looks at the current promotions
    Task(
        annotator="0",
        user_id="task_0024",
        instruction="You are Mia Johnson. The time is 2025-07-20T17:07:00Z. You want to analyze the current promotions. Specifically, you want to identify which products have the 'bogo_percentage' type promotions. Find transactions involving these products. Get the most recent of these transactions, then promote the employee that made that transaction to the role of 'Manager'.",
        actions=[
            # Get all percentage promotions
            Action(name="get_promotions_info_by_param", kwargs={"filter_params": {"type": "bogo_percentage"}, "info_items": ["applicable_skus"]}),
            # Find transactions with these products
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": "SPORT-YOGMAT01"}, "info_items": ["transaction_id", "timestamp"]}),
            # Get the most recent transaction using filter_and_sort_ids_by_date
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"TXN-0004": "2025-06-05T12:48:11Z"}, "top_n": 1, "sort_order": "newest"}),
            # Find employee who made the transaction
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"transaction_id": "TXN-0004"}, "info_items": ["employee_id"]}),
            # Promote the employee to Manager
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1032", "role": "Manager"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0025",
        instruction="You are Megan Young. The time is 2025-07-20T17:08:00Z. You want to edit a transaction to change the payment method from 'credit_card' to 'loyalty_points', the total amount to $50.00, and mark the employee as you and update the timestamp. The transaction ID is TXN-0010, and the total amount is $50.00. After changing the transaction, you want to calculate the loyalty points earned (1 point per $1 spent) from the new total and add them to the customer's account. Finally, get the email address of the customer associated with this transaction so you can notify them about the loyalty points added.",
        actions=[
            # Get employee ID for Megan Young
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["employee_id"]}),
            # edit the transaction to change the payment method and total amount
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0010", "payment_method": "loyalty_points", "total_amount": 50.00, "employee_id": "EMP-1045", "current_time": "2025-07-20T17:08:00Z"}),
            # Get the transaction details by transaction ID
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"transaction_id": "TXN-0010"}, "info_items": ["customer_id", "total_amount"]}),
            # Get customer loyalty points
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["loyalty_points"]}),
            # Add loyalty points to customer's account
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5010", "loyalty_points": 1075, "current_time": "2025-07-20T17:08:00Z"}),
            # Get the customer email address associated with the transaction
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0026",
        instruction="You are Megan Young. The time is 2025-07-20T17:09:00Z. You want to create a new employee account for John Doe in the role of 'Chief Cheerleader', with a hire date of today. After creating the account, you want to get a list of inventory items that are 'low_stock' status. Then update the 'last_stock_count' field for those items. Finally, you want to get your employee email address and John's email address so John can contact you for help.",
        actions=[
            # Create a new employee account
            Action(name="edit_employees_db", kwargs={"name": "John Doe", "role": "Chief Cheerleader", "hire_date": "2025-07-20"}),
            # Get a list of inventory items that need to be restocked
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"status": ["low_stock"]}, "info_items": ["id"]}),
            # Update the last stock count for these items
            Action(name="edit_inventory_db", kwargs={"id": "INV-0009", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:09:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0022", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:09:00Z"}),
            # Get the employee email address
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["email"]}),
            # Get John's email address
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "John Doe"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"},{"email": "john.doe@retailpos.com"}]
    ),
    # Task 27: Inventory Management and Customer Notification
    Task(
        annotator="0",
        user_id="task_0027",
        instruction="You are Isabella Rossi. The time is 2025-07-20T17:10:00Z. Check all inventory items in STORE-002 that have quantity below 20. For each item found, increase the quantity by 25 and update the status to 'in_stock'. Then get the email addresses of all customers who have purchased these items so you can notify them about the restocking.",
        actions=[
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["id", "sku", "quantity"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0013", "quantity": 28, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0019", "quantity": 40, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0022", "quantity": 31, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["ELEC-GAMLP15","SMRT-THERM02","CLTH-WINJKT01"]}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5005","CUST-5011"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "emma.garcia@example.com"},{"email": "mia.kim@example.com"}]
    ),
    # Task 28: Product Analysis and Promotion Creation
    Task(
        annotator="0",
        user_id="task_0028",
        instruction="You are Marcus Chen. The time is 2025-07-20T17:11:00Z. Find all products in the 'Sports & Outdoors' category that cost more than $50. Create a promotion called 'Sports Premium Sale' with 25% discount on these products valid for the next 3 weeks. Then get the names, email addresses and phone numbers of customers who have platinum membership level so they can be notified first. Change your role in the employee database to 'Head of Promotions'.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku", "name", "price"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Sports Premium Sale", "type": "percentage", "discount_value": 25, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20", "end_date": "2025-08-10"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": "platinum"}, "info_items": ["name", "email", "phone_number"]}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1008", "role": "Head of Promotions"}),
        ],
        outputs=[{"name": "Noah Johnson","email": "noah.johnson@example.com","phone_number": "+1-555-0987-654"}]
    ),
    # Task 29: Employee Performance Tracking
    Task(
        annotator="0",
        user_id="task_0029",
        instruction="You are Henry Adams. The time is 2025-07-20T17:12:00Z. Add a purchase transaction for customer CUST-5004 to buy 1 product with SKU CLTH-SLFJEAN34, using credit_card, in STORE-002 and entered by employee EMP-1032. You want to analyze which employee has processed the most transactions. Find the employee who appears most frequently in transactions, then promote them to 'Senior Sales Associate' and get their email address to send a congratulations message.",
        actions=[
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5004", "employee_id": "EMP-1032", "items": {"CLTH-SLFJEAN34": 1}, "store_id": "STORE-002", "current_time": "2025-07-20T17:12:00Z", "payment_method": "credit_card"}),
            Action(name="update_inventory_item", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T17:12:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {}, "info_items": ["employee_id"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"employee_id": "EMP-1032"}, "info_items": ["name", "email"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1032", "role": "Senior Sales Associate"}),
        ],
        outputs=[{"name": "Amelia Lee", "email": "amelia.lee@retailpos.com"}]
    ),
    # Task 30: Customer Birthday Campaign
    Task(
        annotator="0",
        user_id="task_0030",
        instruction="You are Grace Miller. The time is 2025-02-27T17:13:00Z. Check if any customers have their birthday today. If found, create a special birthday promotion called '<Customer Name> Birthday Special' with 30% off all products for today only. Add 100 bonus loyalty points to their account and get their email to send birthday wishes. Change your role to 'Customer Relations Manager' in the employee database.",
        actions=[
            Action(name="get_customers_with_birthday_today", kwargs={"current_day": "02-27"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5003"}, "info_items": ["name", "email", "loyalty_points"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Olivia Patel Birthday Special", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-02-27", "end_date": "2025-02-27"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5003", "loyalty_points": 560, "current_time": "2025-02-27T17:13:00Z"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Grace Miller"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1002", "role": "Customer Relations Manager"}),
        ],
        outputs=[{"name": "Olivia Patel", "email": "olivia.patel@example.com"}]
    ),
    # Task 31: Inventory Audit and Low Stock Alert
    Task(
        annotator="0",
        user_id="task_0031",
        instruction="You are Zoe Martinez. The time is 2025-07-20T17:14:00Z. Set the reorder level to 60 for inventory item INV-0023. Then check if any inventory items in STORE-003 have a quantity below their reorder level. If so mark their status as 'low_stock' and add 60 additional units and update the last_stock_count to today. Create a promotion called 'Low Stock Clearance' with 20% off these items for a week. Get the store Inventory Specialist's email to notify them of the situation.",
        actions=[
            Action(name="edit_inventory_db", kwargs={"id": "INV-0023", "reorder_level": 60, "current_time": "2025-07-20T17:14:00Z"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["id", "sku", "quantity", "reorder_level"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0023", "quantity": 100, "status": "low_stock", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:14:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Low Stock Clearance", "type": "percentage", "discount_value": 20, "applicable_skus": ["KITCH-FRYPAN10"], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Inventory Specialist"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 32: Product Return and Quality Control
    Task(
        annotator="0",
        user_id="task_0032",
        instruction="You are Daniel Perez. The time is 2025-07-20T17:15:00Z. A customer Noah Johnson wants to return a defective TrailGuard Mountain Bike Helmet. Process the refund, mark the product as 'quality_issue' status, and create a promotion called 'Helmet Safety Check' offering 15% off all Sports & Outdoors items for the next 2 weeks. Get Noah's email for confirmation.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Noah Johnson"}, "info_items": ["customer_id", "email"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5004", "sku": "SPORT-BIKHLM01"}, "info_items": ["transaction_id"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Daniel Perez"}, "info_items": ["employee_id"]}),
            Action(name="create_refund_transaction", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 1, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0004", "current_time": "2025-07-20T17:15:00Z"}),
            Action(name="edit_products_db", kwargs={"sku": "SPORT-BIKHLM01", "status": "quality_issue", "current_time": "2025-07-20T17:15:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Helmet Safety Check", "type": "percentage", "discount_value": 15, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20", "end_date": "2025-08-03"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}]
    ),
    # Task 33: Loyalty Program Enhancement
    Task(
        annotator="0",
        user_id="task_0033",
        instruction="You are Oliver Diaz. The time is 2025-07-20T17:16:00Z. Identify the top 2 customers by loyalty points. Upgrade their membership level to 'platinum' if not already, add 500 bonus points to their accounts, and create a VIP promotion called 'Platinum Elite Benefits' with 35% off all electronics valid for a month from today. Get their email addresses for VIP program notifications.",
        actions=[
            Action(name="get_top_n_customers_by_loyalty_points", kwargs={"n": 2}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["membership_level", "loyalty_points", "email"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004", "membership_level": "platinum", "loyalty_points": 2020, "current_time": "2025-07-20T17:16:00Z"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5001"}, "info_items": ["membership_level", "loyalty_points", "email"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "membership_level": "platinum", "loyalty_points": 1740, "current_time": "2025-07-20T17:16:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Platinum Elite Benefits", "type": "percentage", "discount_value": 35, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}, {"email": "ava.thompson@example.com"}]
    ),
    # Task 34: Supplier Quality Assessment
    Task(
        annotator="0",
        user_id="task_0034",
        instruction="You are Amelia Lee. The time is 2025-07-20T17:17:00Z. Find all products from supplier 'SUP-1001' and check their cost. If any products have a cost over $100, create a promotion called 'Supplier Quality Clearance' with 40% off these products. Update the inventory for these products to mark them as 'clearance' status. Change your role to 'Supplier Relations Manager' in the employee database.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"supplier_id": "SUP-1001"}, "info_items": ["sku", "name", "cost"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Supplier Quality Clearance", "type": "percentage", "discount_value": 40, "applicable_skus": ["ELEC-4KTV55"], "start_date": "2025-07-20"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "ELEC-4KTV55"}, "info_items": ["id"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0001", "status": "clearance", "current_time": "2025-07-20T17:17:00Z"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1032", "role": "Supplier Relations Manager"}),
        ],
        outputs=[]
    ),
    # Task 35: Customer Engagement Campaign
    Task(
        annotator="0",
        user_id="task_0035",
        instruction="You are Jack Robinson. The time is 2025-07-20T17:18:00Z. Find customers with a gold level membership who have opted out of marketing emails but have made purchases. Create a special promotion called 'We Miss You' with 25% off any product they have previously purchased. Update their marketing preference to opt-in and get their email addresses for re-engagement. Change your role to 'Customer Engagement Specialist' in the employee database.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"opt_in_marketing": False, "membership_level": "gold"}, "info_items": ["customer_id", "email"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["line_items"]}),
            Action(name="edit_promotions_db", kwargs={"name": "We Miss You", "type": "percentage", "discount_value": 25, "applicable_skus": ["AUDIO-BTSPKR02", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True, "current_time": "2025-07-20T17:18:00Z"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1034", "role": "Customer Engagement Specialist"}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    # Task 36: Seasonal Inventory Preparation
    Task(
        annotator="0",
        user_id="task_0036",
        instruction="You are Megan Young. The time is 2025-07-20T17:19:00Z. Prepare for back-to-school season by checking inventory of all 'Office Supplies' category products across all stores. If any store has less than 30 units, order 50 more and create a promotion called 'Back to School Ready' with 20% off products in the 'Office Supplies' category for 6 weeks.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku", "name"]}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "store_id", "quantity"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0014", "quantity": 60, "current_time": "2025-07-20T17:19:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Back to School Ready", "type": "percentage", "discount_value": 20, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20", "end_date": "2025-08-31"}),
        ],
        outputs=[]
    ),
    # Task 37: Employee Training and Development
    Task(
        annotator="0",
        user_id="task_0037",
        instruction="You are Natalie Cooper. The time is 2025-07-20T17:20:00Z. Add a new employee 'Sarah Williams' as a 'Training Coordinator' for STORE-001, who was hired today. Create a training promotion called 'Staff Training Special' with 50% off any item. Get email addresses of all employees in STORE-001 to notify them about the training program.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Sarah Williams", "role": "Training Coordinator", "store_id": "STORE-001", "hire_date": "2025-07-20"}),
            Action(name="edit_promotions_db", kwargs={"name": "Staff Training Special", "type": "percentage", "discount_value": 50, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "grace.miller@retailpos.com"}, {"email": "daniel.perez@retailpos.com"}, {"email": "natalie.cooper@retailpos.com"}, {"email": "sarah.williams@retailpos.com"}]
    ),
    # Task 38: Product Bundle Creation
    Task(
        annotator="0",
        user_id="task_0038",
        instruction="You are Marcus Chen. The time is 2025-07-20T17:21:00Z. Create a new bundle type promotion called 'Kitchen Essentials Bundle' offering 30% off when customers buy both BrewMaster 12-Cup Coffee Maker and ProSlice 8\" Chef Knife together. Find customers who have purchased either item and get their emails to notify them about the bundle deal.",
        actions=[
            # get the SKUs for the products
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": ["BrewMaster 12-Cup Coffee Maker", "ProSlice 8\" Chef Knife"]}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Kitchen Essentials Bundle", "type": "bundle", "discount_value": 30, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8"], "start_date": "2025-07-20"}),
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["email"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "liam.nguyen@example.com"}, {"email": "mia.kim@example.com"}]
    ),
    # Task 39: Quality Control and Customer Satisfaction
    Task(
        annotator="0",
        user_id="task_0039",
        instruction="You are Grace Miller. The time is 2025-07-20T17:22:00Z. A customer Charlotte Dubois reports that her UltraSoft Cotton Bath Towel is shedding excessively. Process a refund, add the returned towel to the inventory of STORE-001, update the product status to 'quality_review', and create a 'Quality Assurance' type promotion called 'Quality Guarantee' offering free returns on all Home & Kitchen items for 90 days (set the discount value to 0). Get Charlotte's email for follow-up.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id", "email"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "UltraSoft Cotton Bath Towel"}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5009", "sku": "HOME-BTHTWL01"}, "info_items": ["transaction_id"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Grace Miller"}, "info_items": ["employee_id"]}),
            Action(name="create_refund_transaction", kwargs={"sku": "HOME-BTHTWL01", "quantity": 1, "employee_id": "EMP-1002", "original_transaction_id": "TXN-0009", "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-001", "quantity_change": 1, "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="edit_products_db", kwargs={"sku": "HOME-BTHTWL01", "status": "quality_review", "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Home & Kitchen"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Quality Guarantee", "type": "Quality Assurance", "discount_value": 0, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10", "HOME-BTHTWL01", "HOME-DESKLMP01"], "start_date": "2025-07-20", "end_date": "2025-10-20"}),
        ],
        outputs=[{"email": "charlotte.dubois@example.com"}]
    ),
    # Task 40: Store Performance Analysis
    Task(
        annotator="0",
        user_id="task_0040",
        instruction="You are Henry Adams. The time is 2025-07-20T17:23:00Z. Analyze STORE-003 performance by checking total transaction amounts. If the store has made less than $5000 in sales, create an urgent promotion called 'Store Boost Mega Sale' with 45% off all products for 1 week. Get email addresses of all employees in the store to mobilize the sales team.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["total_amount"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Store Boost Mega Sale", "type": "percentage", "discount_value": 45, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "henry.adams@retailpos.com"}, {"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 41: Customer Retention Program
    Task(
        annotator="0",
        user_id="task_0041",
        instruction="You are Isabella Rossi. The time is 2025-07-20T17:24:00Z. Find customers who have loyalty points above 1000 but haven't made any purchases in the last 30 days. Create a win-back promotion called 'Come Back Special' with 30% off their next purchase. Update their membership status to 'valued_customer' and get their emails for retention campaign.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {}, "info_items": ["customer_id","loyalty_points", "email"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004", "CUST-5010"]}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5001": "2025-06-05", "CUST-5004": "2025-06-05", "CUST-5010": "2025-06-05"}, "filter_end_date": "2025-06-20"}),
            Action(name="edit_promotions_db", kwargs={"name": "Come Back Special", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5010", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
        ],
        outputs=[{"email": "ava.thompson@example.com"}, {"email": "noah.johnson@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 42: Emergency Stock Transfer
    Task(
        annotator="0",
        user_id="task_0042",
        instruction="You are Oliver Diaz. The time is 2025-07-20T17:25:00Z. STORE-005 is running critically low on PowerPlus Rechargeable AA Batteries (4 Pack). Create an inventory listing for the batteries for STORE-005, but set the quantity to 0. Then check inventory across all stores and transfer 20 units from the store with highest stock to STORE-005. Update inventory accordingly and create an emergency promotion 'Battery Emergency Sale' with 10% off to clear remaining stock.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}, "info_items": ["sku"]}),
            Action(name="edit_inventory_db", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-005", "quantity": 0, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "ELEC-RCHAA04"}, "info_items": ["store_id", "quantity"]}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -20, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-005", "quantity_change": 20, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Battery Emergency Sale", "type": "percentage", "discount_value": 10, "applicable_skus": ["ELEC-RCHAA04"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 43: Customer Service Excellence
    Task(
        annotator="0",
        user_id="task_0043",
        instruction="You are Amelia Lee. The time is 2025-07-20T17:26:00Z. A VIP customer Noah Johnson wants to exchange his FlexFit Premium Yoga Mat for the TrailGuard Mountain Bike Helmet due to a change in fitness routine. Noah returned the Yoga Mat to STORE-001 inventory but collects the helmet from the STORE-004 inventory.Process the exchange (refund original, new purchase) and update the inventories of the relevant stores. Then upgrade his membership to platinum, add 200 bonus loyalty points, and get his email for VIP service confirmation.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Noah Johnson"}, "info_items": ["customer_id", "email", "loyalty_points", "membership_level"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "FlexFit Premium Yoga Mat"}, "info_items": ["sku"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5004", "sku": "SPORT-YOGMAT01"}, "info_items": ["transaction_id"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            Action(name="create_refund_transaction", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 1, "employee_id": "EMP-1032", "original_transaction_id": "TXN-0004", "current_time": "2025-07-20T17:26:00Z"}),
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5004", "employee_id": "EMP-1032", "items": {"SPORT-BIKHLM01": 1}, "store_id": "STORE-004", "payment_method": "credit_card", "current_time": "2025-07-20T17:26:00Z"}),
            # update inventory of yoga mat in store-001
            Action(name="update_inventory_item", kwargs={"sku":"SPORT-YOGMAT01", "store_id":"STORE-001", "quantity_change": 1, "current_time": "2025-07-20T17:26:00Z"}),
            # update inventory of helmet in store-004
            Action(name="update_inventory_item", kwargs={"sku":"SPORT-BIKHLM01", "store_id":"STORE-004", "quantity_change": -1, "current_time": "2025-07-20T17:26:00Z"}),
            # upgrade membership and add loyalty points
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004", "membership_level": "platinum", "loyalty_points": 1720, "current_time": "2025-07-20T17:26:00Z"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}]
    ),
    # Task 44: Technology Upgrade Campaign
    Task(
        annotator="0",
        user_id="task_0044",
        instruction="You are Jack Robinson. The time is 2025-07-20T17:27:00Z. A delivery truck has broken down and 75 units of GigaPlay 15\" Gaming Laptops need to be redistributed to other stores that already stock the item. Check which store has the laptop in their inventory and transfer the 75 units to them. Create a promotion called 'Laptop Distribution Special' with 15% off gaming laptops for the next 10 days. Get the email addresses of employees who are Store Managers to coordinate the redistribution.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "GigaPlay 15\" Gaming Laptop"}, "info_items": ["sku"]}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "ELEC-GAMLP15"}, "info_items": ["store_id", "quantity"]}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002", "quantity_change": 75, "current_time": "2025-07-20T17:27:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Laptop Distribution Special", "type": "percentage", "discount_value": 15, "applicable_skus": ["ELEC-GAMLP15"], "start_date": "2025-07-20", "end_date": "2025-07-30"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"role": "Store Manager"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"}]
    ),
    # Task 45: Sustainability Initiative
    Task(
        annotator="0",
        user_id="task_0045",
        instruction="You are Megan Young. The time is 2025-07-20T17:28:00Z. Launch a sustainability initiative by adding a new product 'Bamboo Water Bottle' priced at $15.99 from the brand 'EcoSmart' and stock 100 units in STORE-005. Create a new promotion 'Green Living' with 20% off products from 'EcoSmart'. Get email addresses of customers who have purchased an EcoSmart product before to notify them about the green initiative.",
        actions=[
            Action(name="edit_products_db", kwargs={"name": "Bamboo Water Bottle", "price": 15.99, "brand": "EcoSmart", "current_time": "2025-07-20T17:28:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"brand": "EcoSmart"}, "info_items": ["name", "sku"]}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021", "store_id": "STORE-005", "quantity": 100, "current_time": "2025-07-20T17:28:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Green Living", "type": "percentage", "discount_value": 20, "applicable_skus": ["SKU-1021", "SMRT-THERM02"], "start_date": "2025-07-20"}),
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "SMRT-THERM02"}),
            Action(name="get_customer_purchase_counts_by_sku", kwargs={"sku": "SKU-1021"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "mia.kim@example.com"}]
    ),
    # Task 46: Holiday Preparation Campaign
    Task(
        annotator="0",
        user_id="task_0046",
        instruction="You are Natalie Cooper. The time is 2025-07-20T17:29:00Z. Prepare for the upcoming holiday season by creating a promotion 'Early Bird Holiday Sale' with 30% off everything. Check inventory quantity of top 3 most expensive products in STORE-001 and add 10 more units if stock is below 15. Get email addresses of customers with gold and platinum memberships for early access notification.",
        actions=[
            Action(name="edit_promotions_db", kwargs={"name": "Early Bird Holiday Sale", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="get_top_n_most_expensive_products_by_store", kwargs={"store_id": "STORE-001", "n": 3}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": ["ELEC-4KTV55", "HOM-COFMKR12", "HOME-DESKLMP01"], "store_id": "STORE-001"}, "info_items": ["sku", "quantity"]}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": 10, "current_time": "2025-07-20T17:29:00Z"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": ["gold","platinum"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ava.thompson@example.com"},{"email": "ben.cohen@example.com"}, {"email": "noah.johnson@example.com"}]
    ),
    # Task 47: Supplier Relationship Management
    Task(
        annotator="0",
        user_id="task_0047",
        instruction="You are Isabella Rossi. The time is 2025-07-20T17:30:00Z. Check all products from supplier SUP-1002 that are priced over $36 and create a volume discount promotion called 'Kitchen Partner Discount' with 15% off their products. Find customers who purchased these products in the last year and get their emails to notify them about the special supplier deal.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"supplier_id": "SUP-1002"}, "info_items": ["sku", "name", "price"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Kitchen Partner Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8"], "start_date": "2025-07-20"}),
            # Get the dates of the purchases
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["HOM-COFMKR12", "KITCH-CHEFKNF8"]}, "info_items": ["customer_id", "timestamp", "line_items"]}),
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5002": "2025-06-05", "CUST-5011": "2025-06-06"}, "filter_start_date": "2024-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["email"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "liam.nguyen@example.com"}, {"email": "mia.kim@example.com"}]
    ),
    # Task 48: Store Transfer and Optimization
    Task(
        annotator="0",
        user_id="task_0048",
        instruction="You are Marcus Chen. The time is 2025-07-20T17:31:00Z. STORE-004 has very low stock of TrailGuard Mountain Bike Helmet. Create an inventory item for 20 helmets that were found in a corner of STORE-005, then transfer 15 units from STORE-005 to STORE-004 and update both inventory records. Create a flash sale 'Sports Transfer Deal' with 20% off this helmet to end in 3 days time.",
        actions=[
            # Get helmet SKU
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="edit_inventory_db", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-005", "quantity": 20, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "SPORT-BIKHLM01","store_id": "STORE-005", "quantity_change": -15, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "SPORT-BIKHLM01","store_id": "STORE-004", "quantity_change": 15, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Sports Transfer Deal", "type": "percentage", "discount_value": 20, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20", "end_date": "2025-07-23"}),
        ],
        outputs=[]
    ),
    # Task 49: New Employee Onboarding and Training
    Task(
        annotator="0",
        user_id="task_0049",
        instruction="You are Grace Miller. The time is 2025-07-20T17:32:00Z. Add a new employee 'David Wilson' as a 'Sales Associate' to STORE-002 starting today. Create a new customer entry for him with email 'david.wilson@retailpos.com' and give him a staff discount promotion 'Employee Welcome Discount' with 40% off one purchase valid for one month.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "David Wilson", "role": "Sales Associate", "store_id": "STORE-002", "hire_date": "2025-07-20"}),
            Action(name="edit_customers_db", kwargs={"name": "David Wilson", "email": "david.wilson@retailpos.com", "current_time": "2025-07-20T17:32:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Employee Welcome Discount", "type": "percentage", "discount_value": 40, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-08-19"}),
        ],
        outputs=[{"email": "david.wilson@retailpos.com"}]
    ),
    # Task 50: Customer Loyalty Tier Adjustment
    Task(
        annotator="0",
        user_id="task_0050",
        instruction="You are Henry Adams. The time is 2025-07-20T17:33:00Z. Review customers with over 800 loyalty points and upgrade them to gold level if they're currently silver. Add 200 bonus points to newly upgraded customers and get their emails for tier upgrade congratulations.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level":"silver"}, "info_items": ["customer_id", "loyalty_points", "membership_level", "email"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1075, "current_time": "2025-07-20T17:33:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5006", "loyalty_points": 1180, "membership_level": "gold", "current_time": "2025-07-20T17:33:00Z"}),
        ],
        outputs=[{"email":"liam.nguyen@example.com"}, {"email": "william.zhang@example.com"}]
    ),
    # Task 51: Expired Product Management
    Task(
        annotator="0",
        user_id="task_0051",
        instruction="You are Zoe Martinez. The time is 2025-07-20T17:34:00Z. Check all grocery products for upcoming expiry dates. For Organic Almond Butter which expires in early 2026, create a clearance promotion 'Fresh & Natural Sale' with 30% off and update inventory status to 'clearance' to move stock faster. Change your role to 'Head Grocer'in the system.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Grocery"}, "info_items": ["sku", "name", "expiry_date"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Fresh & Natural Sale", "type": "percentage", "discount_value": 30, "applicable_skus": ["GROC-ALMBTR500"], "start_date": "2025-07-20"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "GROC-ALMBTR500"}, "info_items": ["id"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0007", "status": "clearance", "current_time": "2025-07-20T17:34:00Z"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Zoe Martinez"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1015", "role": "Head Grocer"}),
        ],
        outputs=[]
    ),
    # Task 52: High-Value Customer Reward Program
    Task(
        annotator="0",
        user_id="task_0052",
        instruction="You are Amelia Lee. The time is 2025-07-20T17:35:00Z. Find customers who have spent over $1000 total across all their transactions. Create an exclusive promotion 'VIP Spender Rewards' with 25% off all electronics and give these customers 200 bonus loyalty points. Get their emails for VIP program invitation.",
        actions=[
            Action(name="get_customers_above_x_spend", kwargs={"amount": 1000}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "VIP Spender Rewards", "type": "percentage", "discount_value": 25, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5005"}, "info_items": ["email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5005", "loyalty_points": 495, "current_time": "2025-07-20T17:35:00Z"}),
        ],
        outputs=[{"email": "emma.garcia@example.com"}]
    ),
    # Task 53: Seasonal Clothing Clearance
    Task(
        annotator="0",
        user_id="task_0053",
        instruction="You are Oliver Diaz. The time is 2025-07-20T17:36:00Z. Summer is ending soon, so create a 'Summer Clearance Blowout' promotion with 45% off all apparel items. Check current inventory of Men's Slim Fit Jeans - 34W 32L in STORE-002 and set the products discount rate to 55% if stock is over 25 units.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Apparel"}, "info_items": ["sku", "name"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Summer Clearance Blowout", "type": "percentage", "discount_value": 45, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"], "start_date": "2025-07-20"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}, "info_items": ["quantity"]}),
            Action(name="edit_products_db", kwargs={"sku": "CLTH-SLFJEAN34", "discount_rate": 0.55, "current_time": "2025-07-20T17:36:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["CLTH-SLFJEAN34","CLTH-WINJKT01"]}, "info_items": ["customer_id"]})
        ],
        outputs=[{"email": "liam.nguyen@example.com"}]
    ),
    # Task 54: Smart Home Technology Push
    Task(
        annotator="0",
        user_id="task_0054",
        instruction="You are Jack Robinson. The time is 2025-07-20T17:37:00Z. Create a new promotion 'Smart Living Revolution' with 18% off all products in the 'Smart Home' category for the next 2 months. Check which customers have bought products from the Electronics category before and are likely interested in smart home tech. Get their emails for targeted marketing.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Smart Home"}, "info_items": ["sku", "name"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Smart Living Revolution", "type": "percentage", "discount_value": 18, "applicable_skus": ["SMRT-THERM02"], "start_date": "2025-07-20", "end_date": "2025-09-20"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["ELEC-4KTV55","AUDIO-BTSPKR02","ELEC-GAMLP15","AUDIO-NCEBUDS01","ELEC-RCHAA04"]}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001","CUST-5005", "CUST-5010"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ava.thompson@example.com"}, {"email": "emma.garcia@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 55: Book Club Customer Engagement
    Task(
        annotator="0",
        user_id="task_0055",
        instruction="You are Natalie Cooper. The time is 2025-07-20T17:38:00Z. Launch a book club initiative by creating a promotion 'Reading Circle Special' with 20% off all books. Add new customer 'Literary Club Admin' with email 'bookclub@retailpos.com' to manage the program. Find customers who bought books and invite them to join.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Books"}, "info_items": ["sku", "name"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Reading Circle Special", "type": "percentage", "discount_value": 20, "applicable_skus": ["BOOK-KDSSTY01"], "start_date": "2025-07-20"}),
            Action(name="edit_customers_db", kwargs={"name": "Literary Club Admin", "email": "bookclub@retailpos.com", "current_time": "2025-07-20T17:38:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": "BOOK-KDSSTY01"}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5008"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "bookclub@retailpos.com"}, {"email": "james.oconnor@example.com"}]
    ),
    # Task 56: Damaged Goods Management
    Task(
        annotator="0",
        user_id="task_0056",
        instruction="You are Daniel Perez. The time is 2025-07-20T17:39:00Z. Customer Benjamin Cohen reports her WaveSound All-Weather Bluetooth Speaker is defective. Process a refund transaction, mark the product status as 'quality_issue', and create a quality assurance promotion 'Sound Quality Guarantee' with 15% off all Electronics products for customer confidence.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Benjamin Cohen"}, "info_items": ["customer_id", "email"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "WaveSound All-Weather Bluetooth Speaker"}, "info_items": ["sku"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Daniel Perez"}, "info_items": ["employee_id"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}, "info_items": ["transaction_id"]}),
            Action(name="create_refund_transaction", kwargs={"sku": "AUDIO-BTSPKR02", "quantity": 1, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0010", "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005", "quantity_change": 1, "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="edit_products_db", kwargs={"sku": "AUDIO-BTSPKR02", "status": "quality_issue", "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Sound Quality Guarantee", "type": "percentage", "discount_value": 15, "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    # Task 57: Store Manager Performance Review
    Task(
        annotator="0",
        user_id="task_0057",
        instruction="You are Megan Young. The time is 2025-07-20T17:40:00Z. As store manager, promote Ethan Walker to 'Senior Cashier' due to excellent performance. Create a customer account using his work email, and give him 50 bonus loyalty points as an employee reward and create a staff motivation promotion 'Team Excellence Discount' with 35% off for one week. Get emails of all employees in STORE-002 to notify them about the promotion.",
        actions=[
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Ethan Walker"}, "info_items": ["employee_id", "email"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1011", "role": "Senior Cashier"}),
            Action(name="edit_customers_db", kwargs={"name": "Ethan Walker", "email": "ethan.walker@retailpos.com", "loyalty_points": 50, "current_time": "2025-07-20T17:40:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Team Excellence Discount", "type": "percentage", "discount_value": 35, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ethan.walker@retailpos.com"}, {"email": "marcus.chen@retailpos.com"}, {"email": "isabella.rossi@retailpos.com"}]
    ),
    # Task 58: Inventory Audit and Restock
    Task(
        annotator="0",
        user_id="task_0058",
        instruction="You are Isabella Rossi. The time is 2025-07-20T17:41:00Z. Conduct a comprehensive inventory audit for STORE-002. Check all products with status 'critical' and increase their quantities by 50 units. Update all last_stock_count dates to today and create an 'Inventory Fresh Stock' promotion with 10% off newly restocked items. In the employee database, change your role to 'Stock Manager'.",
        actions=[
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-002", "status": "critical"}, "info_items": ["id", "sku", "quantity"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0013", "quantity": 53, "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:41:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Inventory Fresh Stock", "type": "percentage", "discount_value": 10, "applicable_skus": ["ELEC-GAMLP15"], "start_date": "2025-07-20"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Isabella Rossi"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1009", "role": "Stock Manager"}),
        ],
        outputs=[]
    ),
    # Task 59: Customer Address Update Service
    Task(
        annotator="0",
        user_id="task_0059",
        instruction="You are Grace Miller. The time is 2025-07-20T17:42:00Z. Customer Charlotte Dubois has moved and needs to update her address to '456 Royal Street, New Orleans, LA, 70130'. Update her record, give her 75 loyalty points for keeping information current, and get her email to confirm the address change. You also sell her QuietTone Wireless Earbuds at STORE-002 using her credit_card and enter the purchase transaction into the system",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5009", "address": "456 Royal Street, New Orleans, LA, 70130", "loyalty_points": 750, "current_time": "2025-07-20T17:42:00Z"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Grace Miller"}, "info_items": ["employee_id"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "QuietTone Wireless Earbuds"}, "info_items": ["sku"]}),
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5009", "employee_id": "EMP-1002", "items": {"AUDIO-NCEBUDS01": 1}, "store_id": "STORE-002", "payment_method": "credit_card", "current_time": "2025-07-20T17:42:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T17:42:00Z"}),
        ],
        outputs=[{"email": "charlotte.dubois@example.com"}]
    ),
    # Task 60: Flash Sale Weekend Event
    Task(
        annotator="0",
        user_id="task_0060",
        instruction="You are Marcus Chen. The time is 2025-07-20T17:43:00Z. Organize a weekend flash sale called 'Saturday Surprise Special' with 50% off office supplies for Saturday only. Check which customers have purchased office items before and send them early notification emails. Also, change your role to 'Weekend Sales Manager' in the system.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku", "name"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Saturday Surprise Special", "type": "percentage", "discount_value": 50, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-26", "end_date": "2025-07-26"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email"]}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1008", "role": "Weekend Sales Manager"}),
        ],
        outputs=[{"email": "william.zhang@example.com"}]
    ),
    # Task 61: Membership Program Overhaul
    Task(
        annotator="0",
        user_id="task_0061",
        instruction="You are Henry Adams. The time is 2025-07-20T17:44:00Z. A new 'Diamond' membership level has been suggested for exceptional customers. Upgrade Noah Johnson to this new tier, add 300 bonus loyalty points, and create an exclusive 'Diamond Elite Access' promotion with 40% off everything. You promote yourself to the role of 'Membership Program Director' and log it in the system.",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Noah Johnson"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004", "membership_level": "diamond", "loyalty_points": 1820, "current_time": "2025-07-20T17:44:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Diamond Elite Access", "type": "percentage", "discount_value": 40, "applicable_skus": [], "start_date": "2025-07-20"}),
            # get employee_id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1020", "role": "Membership Program Director"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}]
    ),
    # Task 62: Product Bundle Innovation
    Task(
        annotator="0",
        user_id="task_0062",
        instruction="You are Amelia Lee. The time is 2025-07-20T17:45:00Z. Create an innovative 'Home Office Complete', 'bundle' type promotion with 35% off when customers buy both the ErgoPro Adjustable Office Chair and LumiLux LED Desk Lamp together. Find customers either of these products and notify them about this workspace bundle deal. Change your role to 'Product Innovation Manager' in the system.",
        actions=[
            # Get skus
            Action(name="get_products_info_by_param", kwargs={"filter_params":{"name":["ErgoPro Adjustable Office Chair","LumiLux LED Desk Lamp"]}, "info_items":["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Home Office Complete", "type": "bundle", "discount_value": 35, "applicable_skus": ["OFFC-ERGCHR01", "HOME-DESKLMP01"], "start_date": "2025-07-20"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["OFFC-ERGCHR01","HOME-DESKLMP01"]}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1032", "role": "Product Innovation Manager"}),
        ],
        outputs=[{"email": "william.zhang@example.com"}]
    ),
    # Task 63: Return Customer Win-Back
    Task(
        annotator="0",
        user_id="task_0063",
        instruction="You are Oliver Diaz. The time is 2025-07-20T17:46:00Z. Identify customers who made purchases on June 6th, 2025 in STORE-001. Create a 'We Want You Back' promotion with 30% off their next purchase and update their status to 'win_back_target'. Get emails of these customers for the re-engagement campaign.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5001": "2025-06-05", "CUST-5008": "2025-06-05", "CUST-5012": "2025-06-06"}, "filter_start_date": "2025-06-06", "filter_end_date": "2025-06-06"}),
            Action(name="edit_promotions_db", kwargs={"name": "We Want You Back", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5012", "status": "win_back_target", "current_time": "2025-07-20T17:46:00Z"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 64: Cross-Store Inventory Balancing
    Task(
        annotator="0",
        user_id="task_0064",
        instruction="You are Zoe Martinez. The time is 2025-07-20T17:47:00Z. Create a stock of 3 ErgoPro Adjustable Office Chairs at STORE-001. Check ErgoPro Adjustable Office Chair stock across all stores. Transfer 5 units from the store with highest stock to stores with lowest stock, update inventory records, and create a 'Store Balance Special' promotion with 12% off these chairs.",
        actions=[
            Action(name="edit_inventory_db", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity": 3, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "store_id", "quantity"]}),
            Action(name="update_inventory_item", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": -5, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity_change": 5, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Store Balance Special", "type": "percentage", "discount_value": 12, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 65: Employee Recognition Program
    Task(
        annotator="0",
        user_id="task_0065",
        instruction="You are Natalie Cooper. The time is 2025-07-20T17:48:00Z. Recognize top-performing employees by finding who processed the single transaction with the highest total amount. Give them 'Employee of the Month' status, add them as customers with 500 loyalty points, and create a 'Staff Appreciation Sale' with 45% off for all employees across all stores.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {}, "info_items": ["employee_id", "total_amount"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"employee_id": "EMP-1045"}, "info_items": ["name", "email"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1045", "status": "employee_of_month"}),
            Action(name="edit_customers_db", kwargs={"name": "Megan Young", "email": "megan.young@retailpos.com", "membership_level": "employee", "loyalty_points": 500, "current_time": "2025-07-20T17:48:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Staff Appreciation Sale", "type": "percentage", "discount_value": 45, "applicable_skus": [], "start_date": "2025-07-20"}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"}]
    ),
    # Task 66: Product Category Performance Analysis
    Task(
        annotator="0",
        user_id="task_0066",
        instruction="You are Jack Robinson. The time is 2025-07-20T17:49:00Z. Analyze electronics category performance by creating a mega promotion 'Electronics Mega Sale' with 28% off all electronics. Find customers who bought electronics in past transactions and increase their loyalty points by 150 as electronics loyalty bonus. Get their emails for exclusive electronics deals.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku", "name"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Electronics Mega Sale", "type": "percentage", "discount_value": 28, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5005", "CUST-5010"]}, "info_items": ["email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "loyalty_points": 1390, "current_time": "2025-07-20T17:49:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5005", "loyalty_points": 445, "current_time": "2025-07-20T17:49:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5010", "loyalty_points": 1175, "current_time": "2025-07-20T17:49:00Z"}),
        ],
        outputs=[{"email": "ava.thompson@example.com"}, {"email": "emma.garcia@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 67: Customer Birthday Promotions Launch
    Task(
        annotator="0",
        user_id="task_0067",
        instruction="You are Natalie Cooper. The time is 2025-01-19T18:00:00Z. It's customer appreciation month! Find all customers with birthdays today (01-19) and create a special 'Birthday Bash Bonanza' promotion with 30% off all products. Get their phone number so you can send them birthday wishes and upgrade each birthday customer bronze membership level if they are still on basic.",
        actions=[
            Action(name="get_customers_with_birthday_today", kwargs={"current_day": "01-19"}),
            Action(name="edit_promotions_db", kwargs={"name": "Birthday Bash Bonanza", "type": "percentage", "discount_value": 30.0, "applicable_skus": [], "start_date": "2025-01-19"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["membership_level", "phone_number"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5012", "membership_level": "bronze", "current_time": "2025-01-19T18:00:00Z"}),
        ],
        outputs=[]
    ),
    # Task 68: Emergency Inventory Restock Protocol
    Task(
        annotator="0",
        user_id="task_0068",
        instruction="You are Zoe Martinez. The time is 2025-07-20T18:01:00Z. STORE-004 has experienced unexpected high demand and you must triple the reorder level on all its inventory items. Make this change to the inventory and then check which items are below the new reorder level. For any inventory item below the new level, set their status to 'critical' and add then 10 units to the quantity. Get the phone number of all 'Store Managers' so they can be notified",
        actions=[
            # get inventory items from store-004
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "quantity", "reorder_level"]}),
            # update reorder level
            Action(name="edit_inventory_db", kwargs={"id": "INV-0009", "reorder_level": 18,"status": "critical", "quantity": 14,"current_time": "2025-07-20T18:01:00Z"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"role": "Store Manager"}, "info_items": ["phone_number"]})
        ],
        outputs=[]
    ),
    # Task 69: New Product Launch Campaign
    Task(
        annotator="0",
        user_id="task_0069",
        instruction="You are Marcus Chen. The time is 2025-07-20T18:02:00Z. Launch the new 'TechWave Wireless Earbuds Pro' at with a price of $199.99. Create initial inventory across all stores (STORE-001 to STORE-005) with 25 units each. Then create a launch promotion 'Wireless Freedom Week' that last for a week from now, with 15% off, and get the phone number of all platinum and gold members so you can notify themabout this exclusive new arrival.",
        actions=[
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id"]}),
            Action(name="edit_products_db", kwargs={"name": "TechWave Wireless Earbuds Pro", "price": 199.99, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021","store_id": "STORE-001", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021","store_id": "STORE-002", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021","store_id": "STORE-003", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021","store_id": "STORE-004", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021","store_id": "STORE-005", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Wireless Freedom Week", "type": "percentage", "discount_value": 15.0, "applicable_skus": ["SKU-1021"], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": ["platinum", "gold"]}, "info_items": ["phone_number"]})
        ],
        outputs=[{"phone_number": "+1-555-0123-456"}, {"phone_number": "+1-555-0999-888"}, {"phone_number": "+1-555-0987-654"}]
    ),
    # Task 70: Customer Loyalty Tier Analysis
    Task(
        annotator="0",
        user_id="task_0070",
        instruction="You are Isabella Rossi. The time is 2025-07-20T18:03:00Z. Find the top 2 customers by loyalty points, review their purchase history to find what products they have previously bought. Then create an exclusive 'VIP Elite Circle' promotion on those products with 45% off. Additionally, if they have a difference in their loyalty points of less than 500, ensure both of their membership levels are'platinum'.",
        actions=[
            Action(name="get_top_n_customers_by_loyalty_points", kwargs={"n": 2}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004"]}, "info_items": ["line_items"]}),
            Action(name="edit_promotions_db", kwargs={"name": "VIP Elite Circle", "type": "percentage", "discount_value": 45.0, "start_date": "2025-07-20", "applicable_skus": ["ELEC-4KTV55", "ELEC-RCHAA04", "SPORT-BIKHLM01", "SPORT-YOGMAT01"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004"]}, "info_items": ["customer_id", "loyalty_points", "membership_level"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "membership_level": "platinum", "current_time": "2025-07-20T18:03:00Z"}),
        ],
        outputs=[]
    ),
    # Task 71: Seasonal Product Clearance Strategy
    Task(
        annotator="0",
        user_id="task_0071",
        instruction="You are Oliver Diaz. The time is 2025-07-20T18:04:00Z. Summer inventory needs clearing to make room for fall products. Create a 'Summer's End Clearance' promotion with tiered discounts: 40% off 'Sports & Outdoors' products first and then 35% off 'Apparel' products. Check inventory levels of Apparel inventory items and set the status to 'slow_moving'if their quantity is more than double their safety stock.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Summer's End Clearance", "type": "percentage", "discount_value": 40.0, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Apparel"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Summer's End Clearance", "type": "percentage", "discount_value": 35.0, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"], "start_date": "2025-07-20"}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"]}, "info_items": ["id","quantity", "safety_stock"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0005", "status": "slow_moving", "current_time": "2025-07-20T18:04:00Z"}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0022", "status": "slow_moving", "current_time": "2025-07-20T18:04:00Z"}),
        ],
        outputs=[]
    ),
    # Task 72: Employee Performance Recognition Program
    Task(
        annotator="0",
        user_id="task_0072",
        instruction="You are Megan Young. The time is 2025-07-20T18:05:00Z. Recognize outstanding employee performance by finding the employee who processed the most recent cash transaction. Create them a customer account with 1000 loyalty points, promote them to 'Senior Sales Associate' in their role, and establish a 'Team Champion Discount' with 25% off all products.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"payment_method": "cash"}, "info_items": ["transaction_id", "timestamp", "employee_id"]}),
            # sort transactions by timestamp to find the most recent one
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"TXN-0002": "2025-06-05T11:42:00Z", "TXN-0007": "2025-06-05T14:22:18Z", "TXN-0008":"2025-06-05T15:03:09Z"}, "sort_order": "newest", "top_n": 1}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"employee_id": "EMP-1004"}, "info_items": ["name", "email"]}),
            Action(name="edit_customers_db", kwargs={"name": "Natalie Cooper", "email": "natalie.cooper@retailpos.com", "loyalty_points": 1000, "current_time": "2025-07-20T18:05:00Z"}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1004", "role": "Senior Sales Associate"}),
            Action(name="edit_promotions_db", kwargs={"name": "Team Champion Discount", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 73: Cross-Store Inventory Optimization
    Task(
        annotator="0",
        user_id="task_0073",
        instruction="You are Henry Adams. The time is 2025-07-20T18:06:00Z. STORE-003 is downsizing and needs to given half of its inventory to STORE-001. Create inventory items in STORE-001 for all products from STORE-003, setting the quantity to half of that in STORE-003, as none of the products were previously stocked in STORE-001. Update STORE-003s inventory records to show the half-quantity stock, and create a 'Freshly Stocked' promotion for recently transferred items with 12% off.",
        actions=[
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["sku", "quantity"]}),
            Action(name="edit_inventory_db", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity": 5, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-001", "quantity": 40, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-001", "quantity": 45, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "KITCH-FRYPAN10", "store_id": "STORE-001", "quantity": 20, "current_time": "2025-07-20T18:06:00Z"}),

            Action(name="update_inventory_item", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": -5, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -40, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -45, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="update_inventory_item", kwargs={"sku": "KITCH-FRYPAN10", "store_id": "STORE-003", "quantity_change": -20, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Freshly Stocked", "type": "percentage", "discount_value": 12.0, "applicable_skus": ["OFFC-ERGCHR01", "GROC-GRNLBR12", "ELEC-RCHAA04", "KITCH-FRYPAN10"], "start_date": "2025-07-20"})
        ],
        outputs=[]
    ),
    # Task 74: Customer Retention Emergency Response
    Task(
        annotator="0",
        user_id="task_0074",
        instruction="You are Amelia Lee. The time is 2025-07-20T18:07:00Z. Customer retention metrics show concerning trends. Identify customers who have transactions with a 'returned' status, update their customer status to 'at_risk', create a 'Come Back Strong' promotion with 50% off any purchase, and get the email address of these customers so you can personally reach out to them. Change your role to 'Customer Retention Specialist' in the system.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"status": "returned"}, "info_items": ["customer_id"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5012", "status": "at_risk", "current_time": "2025-07-20T18:07:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Come Back Strong", "type": "percentage", "discount_value": 50.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1032", "role": "Customer Retention Specialist"}),
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 75: Supplier Relations and New Product Integration
    Task(
        annotator="0",
        user_id="task_0075",
        instruction="You are Jack Robinson. The time is 2025-07-20T18:08:00Z. A new brand 'TechForward Inc.' is providing us with 'SmartFit Activity Tracker' at which we are pricing at $149.99. Create the product entry, establish initial inventory of 50 units at STORE-004, set up a 'Future Fitness' launch promotion with 20% off this product, and get the phone number of customers who previously bought the 'FlexFit Premium Yoga Mat' so they can be told about the new product.",
        actions=[
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            Action(name="edit_products_db", kwargs={"name": "SmartFit Activity Tracker", "price": 149.99, "brand": "TechForward Inc.", "current_time": "2025-07-20T18:08:00Z"}),
            Action(name="edit_inventory_db", kwargs={"sku": "SKU-1021", "store_id": "STORE-004", "quantity": 50, "current_time": "2025-07-20T18:08:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Future Fitness", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SKU-1021"], "start_date": "2025-07-20"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "FlexFit Premium Yoga Mat"}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["SPORT-YOGMAT01"]}, "info_items": ["customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5004"]}, "info_items": ["phone_number"]})
        ],
        outputs=[{"phone_number": "+1-555-0987-654"}]
    ),
    # Task 76: Premium Customer Concierge Service
    Task(
        annotator="0",
        user_id="task_0076",
        instruction="You are Daniel Perez. The time is 2025-07-20T18:09:00Z. Create a specialized 'Basics tax free' promotion with exclusive 60% off any products that have a tax rate of 0. Add 500 bonus loyalty points to all platinum members, and establish personal shopping assistance by getting the email of these VIP customers.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"tax_rate": 0}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Basics tax free", "type": "percentage", "discount_value": 60.0, "applicable_skus": ["GROC-GRNLBR12", "BOOK-KDSSTY01","GROC-SPRWAT6P", "GROC-ALMBTR500"], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": "platinum"}, "info_items": ["customer_id", "name", "email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004","loyalty_points": 2020, "current_time": "2025-07-20T18:09:00Z"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}]
    ),
    # Task 77: Theft Prevention and Security Audit
    Task(
        annotator="0",
        user_id="task_0077",
        instruction="You are Grace Miller. The time is 2025-07-20T18:10:00Z. Following security concerns, conduct a comprehensive audit. Find all transactions with 'returned' status and change the status to 'under_review'. Find if there are other transactions entered by the same employee, and if so mark them as 'under_review' as well. Then return the name of the customer that is associated with the returned transaction.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"status": "returned"}, "info_items": ["transaction_id", "customer_id", "employee_id"]}),
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0012", "status": "under_review", "current_time": "2025-07-20T18:10:00Z"}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"employee_id": "EMP-1002"}, "info_items": ["transaction_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["name"]}),
        ],
        outputs=[{"name": "Logan Smith"}]
    ),
    # Task 78: Holiday Preparation and Staff Scheduling
    Task(
        annotator="0",
        user_id="task_0078",
        instruction="You are Ethan Walker. The time is 2025-07-20T18:11:00Z. Check if products in the 'Sports & Outdoors' category have sold more than 20 units. If not, create a 'Holiday Prep Special' promotion with 25% off that category, and get contact information (email and phone) for customers who have bought from that category.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": ["Sports & Outdoors"]}, "info_items": ["sku"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]}, "info_items": ["line_items", "customer_id"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Holiday Prep Special", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5004", "CUST-5012"]}, "info_items": ["email", "phone_number"]})
        ],
        outputs=[{"email": "noah.johnson@example.com", "phone_number": "+1-555-0987-654"}, {"email": "logan.smith@example.com", "phone_number": "+1-555-0667-899"}]
    ),
    # Task 79: Customer Feedback and Product Improvement
    Task(
        annotator="0",
        user_id="task_0079",
        instruction="You are Charlie Brown. The time is 2025-07-20T18:12:00Z. Identify any products that have been returned, update their status to 'quality_review'. Create an improvement-focused 'Quality Promise' promotion with 15% off these products, and get the email addresses of customers who have returned products to notify them about the improvements. Add yourself as an employee with the role of Quality Assurance Specialist.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"status": "returned"}, "info_items": ["line_items", "customer_id"]}),
            Action(name="edit_products_db", kwargs={"sku": "SPORT-BIKHLM01", "status": "quality_review", "current_time": "2025-07-20T18:12:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Quality Promise", "type": "percentage", "discount_value": 15.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
            Action(name="edit_employees_db", kwargs={"name": "Charlie Brown", "role": "Quality Assurance Specialist"})
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 80: Multi-Store Anniversary Celebration
    Task(
        annotator="0",
        user_id="task_0080",
        instruction="You are Sophia Martinez. Add yourself to the employee database with a role of Event Manager and assign yourself to STORE-001. The time is 2025-07-20T18:13:00Z. Celebrate the company's 5th anniversary with a massive cross-store event. Create a '5 Years Strong' promotion with progressive discounts on all products (5% for bronze members, 15% for silver, 25% for gold, 35% for platinum), and get the email of the eldest customer to invite them to celebration.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Sophia Martinez", "role": "Event Manager", "store_id": "STORE-001"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Sophia Martinez"}, "info_items": ["employee_id"]}),
            Action(name="edit_promotions_db", kwargs={"name": "5 Years Strong - Bronze", "type": "percentage", "discount_value": 5.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="edit_promotions_db", kwargs={"name": "5 Years Strong - Silver", "type": "percentage", "discount_value": 15.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="edit_promotions_db", kwargs={"name": "5 Years Strong - Gold", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="edit_promotions_db", kwargs={"name": "5 Years Strong - Platinum", "type": "percentage", "discount_value": 35.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            # get customers birthdate
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {}, "info_items": ["customer_id", "birthdate"]}),
            # sort customers by birthdate and get the eldest customer
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5001": "1990-07-12", "CUST-5002": "1985-11-05", "CUST-5003": "1997-02-27", "CUST-5004": "1982-09-14", "CUST-5005": "1995-12-03", "CUST-5006": "1988-04-30", "CUST-5007": "1993-06-18", "CUST-5008": "1998-10-09", "CUST-5009": "1986-01-25", "CUST-5010": "1983-03-04", "CUST-5011": "1992-08-11", "CUST-5012": "2000-01-19"}, "sort_order": "oldest", "top_n": 1}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["email"]}),
        ],
        outputs=[{"emails": ["noah.johnson@example.com"]}]
    ),
    # Task 81: Eco-Friendly Initiative Launch
    Task(
        annotator="0",
        user_id="task_0081",
        instruction="You are Daniel Perez. The time is 2025-07-20T18:14:00Z. Change your role to Sustainability Manager. Launch a sustainability initiative by identifying products by the brand 'EcoSmart'. Create a 'Green Choice' promotion with 30% off these products and upgrade customers' membership levels if they have bought an EcoSmart product(Order is basic, bronze, silver,gold,platinum from lowest to highest), and get their email addresses to notify these customers about our environmental commitment.",
        actions=[
            # get employee id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Daniel Perez"}, "info_items": ["employee_id"]}),
            # change role to Sustainability Manager
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1003", "role": "Sustainability Manager"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"brand": "EcoSmart"}, "info_items": ["sku"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Green Choice", "type": "percentage", "discount_value": 30.0, "applicable_skus": ["SMRT-THERM02"], "start_date": "2025-07-20"}),
            # get customers who have bought EcoSmart products
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku": "SMRT-THERM02"}, "info_items": ["customer_id"]}),
            # get customer info by customer_id
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["membership_level", "email"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5011", "membership_level": "gold", "current_time": "2025-07-20T18:14:00Z"}),
        ],
        outputs=[{"email": "mia.kim@example.com"}]
    ),
    # Task 82: Emergency Store Support and Crisis Management
    Task(
        annotator="0",
        user_id="task_0082",
        instruction="You are Marcus Chen. The time is 2025-07-20T18:15:00Z. STORE-004 faces equipment failure and needs emergency support. Change your employee role to Crisis Manager, and transfer all of their inventory to nearby STORE-001 by changing the item's store_id. Create a 'Store Support Special' promotion offering 20% off items affected by the transfer, get the email addresses of customers that have made transactions at STORE-004 so you can notify them of the issues.",
        actions=[
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1008", "role": "Crisis Manager"}),
            # Get all inventory items from STORE-004
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "sku"]}),
            # Transfer inventory items to STORE-001
            Action(name="edit_inventory_db", kwargs={"id": "INV-0009", "store_id": "STORE-001", "current_time": "2025-07-20T18:15:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Store Support Special", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"}),
            # get customers who have made transactions at STORE-004
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["customer_id"]}),
            # get customer info by customer_id
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5004", "CUST-5009"]}, "info_items": ["customer_id", "email", "name"]})
        ],
        outputs=[{"email": "noah.johnson@example.com"}, {"email": "charlotte.dubois@example.com"}]
    ),
    # Task 83: Social Media Marketing Integration
    Task(
        annotator="0",
        user_id="task_0083",
        instruction="You are Oliver Diaz. Add Ryan Kim as a Social Media Manager in STORE-002. Create a 'Bargain Electronics' promotion with 25% off the two most expensive Electronics product. Gale Barley is a new customer that wants to be added to the customer database with email 'gale.barley@example.com' and purchase a QuietTone Wireless Earbuds using cash. Ryan Kim puts the purchase into the system.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Ryan Kim", "role": "Social Media Manager", "store_id": "STORE-002"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Ryan Kim"}, "info_items": ["employee_id"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": ["Electronics"]}, "info_items": ["sku", "price"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Bargain Electronics", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15"], "start_date": "2025-07-20"}),
            # create a new customer Gale Barley
            Action(name="edit_customers_db", kwargs={"name": "Gale Barley", "email": "gale.barley@example.com", "current_time": "2025-07-20T18:15:00Z"}),
            # get the customer_id of Gale Barley
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Gale Barley"}, "info_items": ["customer_id"]}),
            # get sku of QuietTone Wireless Earbuds
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "QuietTone Wireless Earbuds"}, "info_items": ["sku"]}),
            # add the purchase of QuietTone Wireless Earbuds
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5013", "items": {"AUDIO-NCEBUDS01":1}, "payment_method": "cash", "store_id": "STORE-002", "employee_id": "EMP-1013", "current_time": "2025-07-20T18:15:00Z"}),
            # update the inventory of QuietTone Wireless Earbuds
            Action(name="update_inventory_item", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T18:15:00Z"})
        ],
        outputs=[]
    ),
    # Task 84: Bulk Purchase Corporate Program
    Task(
        annotator="0",
        user_id="task_0084",
        instruction="You are Anna Wilson. The time is 2025-07-20T18:17:00Z. Establish a corporate bulk purchase program. Find customers who made a transaction for a total quantity of more than 10 items at once. Get their email addresses, and add 100 loyalty points.",
        actions=[
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {}, "info_items": ["transaction_id", "line_items", "customer_id"]}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5009"]}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5009", "loyalty_points": 775, "current_time": "2025-07-20T18:17:00Z"})
        ],
        outputs=[{"email": ["charlotte.dubois@example.com"]}]
    ),
    # Task 85: Technology Upgrade and Digital Transformation
    Task(
        annotator="0",
        user_id="task_0085",
        instruction="The time is 2025-10-09T18:18:00Z. James O'Connor comes into the store. He says it is his birthday and he would like to experience working in a shop for a day. Check to see if it is his birthday today, if it is, add him as an employee using his customer email address, and set his role to 'Temporary Sales Associate'. Create a 'Birthday Bash' promotion with 30% off all products with a start and end date of today. His dad, Connor O'Connor, would like to be added to the customer database with email 'connor.oconnor@example.com'.",
        actions=[
            # Get customers with birthdate today
            Action(name="get_customers_with_birthday_today", kwargs={"current_day": "2025-10-09"}),
            # Get customer info for James O'Connor
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "James O'Connor"}, "info_items": ["customer_id", "email"]}),
            # Add James O'Connor as an employee
            Action(name="edit_employees_db", kwargs={"name": "James O'Connor", "email": "james.oconnor@example.com", "role": "Temporary Sales Associate"}),
            # Create 'Birthday Bash' promotion
            Action(name="edit_promotions_db", kwargs={"name": "Birthday Bash", "type": "percentage", "discount_value": 30.0, "applicable_skus": [], "start_date": "2025-10-09", "end_date": "2025-10-09"}),
            # Add Connor O'Connor to customer database
            Action(name="edit_customers_db", kwargs={"name": "Connor O'Connor", "email": "connor.oconnor@example.com", "current_time": "2025-10-09T18:18:00Z"}),
        ],
        outputs=[]
    ),
    # Task 86: Employee Training Program Management
    Task(
        annotator="0",
        user_id="task_0086",
        instruction="You are Sandra Mitchell. Add yourself to the employee database with your role as Training Coordinator and set your store ID to 'STORE-003'. The time is 2025-07-20T18:19:00Z. Check inventory levels of products in the 'Office Supplies' category and add 10 units to the quantity if it is below 20. Create a 'Team Learning' promotion with 20% off the 'Office Supplies' products.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Sandra Mitchell", "role": "Training Coordinator", "store_id": "STORE-003"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Sandra Mitchell"}, "info_items": ["employee_id"]}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku"]}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "quantity"]}),
            Action(name="update_inventory_item", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": 10, "current_time": "2025-07-20T18:19:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Team Learning", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 87: Inventory Security and Loss Prevention
    Task(
        annotator="0",
        user_id="task_0087",
        instruction="You are Marcus Chen. The time is 2025-07-20T18:20:00Z. Implement enhanced security measures for high-value inventory items. Update your role to Security Manager, identify products with a price greater than $1400. You move the inventory quantity and add it to the safety stock for safe keeping overnight. Update the inventory to show the move and set the status to 'high_security'. Get the email address of employees with the role of Inventory Specialist to notify them about the new security protocols.",
        actions=[
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id"]}),
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1008", "role": "Security Manager"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {}, "info_items": ["sku", "price"]}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": ["ELEC-GAMLP15"]}, "info_items": ["id","sku", "store_id", "quantity", "safety_stock"]}),
            Action(name="edit_inventory_db", kwargs={"id": "INV-0013", "quantity": 0, "safety_stock": 5, "status": "high_security", "current_time": "2025-07-20T18:20:00Z"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"role": "Inventory Specialist"}, "info_items": ["email"]})
        ],
        outputs=[{"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 88: Local Community Engagement Initiative
    Task(
        annotator="0",
        user_id="task_0088",
        instruction="You are a grumpy manager. You decide that there have been promotions that have been running for too long. Find the 3 promotions that started the longest time ago, and delete them. You also want to move Henry Adams to STORE-005 because you dont like working in the same store as him.",
        actions=[
            # Get all promotions
            Action(name="get_promotions_info_by_param", kwargs={"filter_params": {}, "info_items": ["promotion_id", "start_date"]}),
            # Sort promotions by start date and get the 3 oldest
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"PROMO-001": "2025-06-01", "PROMO-002": "2025-05-15", "PROMO-003": "2025-06-10", "PROMO-004": "2025-09-05", "PROMO-005": "2025-04-01", "PROMO-006": "2025-05-20", "PROMO-007": "2025-06-14"}, "sort_order": "oldest", "top_n": 3}),
            # Delete the 3 oldest promotions
            Action(name="edit_promotions_db", kwargs={"promotion_id": "PROMO-005", "delete": True}),
            Action(name="edit_promotions_db", kwargs={"promotion_id": "PROMO-002", "delete": True}),
            Action(name="edit_promotions_db", kwargs={"promotion_id": "PROMO-006", "delete": True}),
            # Get employee info for Henry
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Move Henry Adams to STORE-005
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1020", "store_id": "STORE-005"})
        ],
        outputs=[]
    ),
    # Task 89: Customer Feedback Response System
    Task(
        annotator="0",
        user_id="task_0089",
        instruction="You are Rachel Anderson. The time is 2025-07-20T18:22:00Z. Add yourself to the employee database with a role of Customer Relations Manager, identify customers who have made returns, create a 'We Listen' promotion with 25% off all products to encourage return visits, and gather their email addresses for follow-up surveys.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Rachel Anderson", "role": "Customer Relations Manager"}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Rachel Anderson"}, "info_items": ["employee_id"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"status": "returned"}, "info_items": ["customer_id"]}),
            Action(name="edit_promotions_db", kwargs={"name": "We Listen", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["email"]})
        ],
        outputs=[{"emails": ["logan.smith@example.com"]}]
    ),
    # Task 90: Student and Education Discount Program
    Task(
        annotator="0",
        user_id="task_0090",
        instruction="You are Daniel Perez. The time is 2025-07-20T18:23:00Z. Create a 'Student Success' promotion with 40% off all electronics and books. Identify the youngest customer that has a basic membership, and change their membership level to 'student'.",
        actions=[
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": ["Electronics", "Books"]}, "info_items": ["sku", "name", "category"]}),
            Action(name="edit_promotions_db", kwargs={"name": "Student Success", "type": "percentage", "discount_value": 40.0, "applicable_skus": ["ELEC-4KTV55","AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04", "BOOK-KDSSTY01"], "start_date": "2025-07-20"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": "basic"}, "info_items": ["customer_id", "birthdate"]}),
            # Sort customers by birthdate to find the youngest
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5008":"1998-10-09", "CUST-5012": "2000-01-19"}, "sort_order": "newest", "top_n": 1}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5012", "membership_level": "student", "current_time": "2025-07-20T18:23:00Z"}),
        ],
        outputs=[]
    ),
    # Task 91: Product Quality Assurance Initiative
    Task(
        annotator="0",
        user_id="task_0091",
        instruction="Some bad people have just got access to the database. Find all customers that have bought products, and delete their customer records to protect their privacy. Then delete all transactions made with credit cards.",
        actions=[
            # get all customers who have made transactions
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {}, "info_items": ["customer_id"]}),
            # delete customer records using edit_customers_db
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5001", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5002", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5003", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5004", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5005", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5006", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5007", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5008", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5009", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5010", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5011", "delete": True}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5012", "delete": True}),
            # get all transactions made with credit cards
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"payment_method": "credit_card"}, "info_items": ["transaction_id"]}),
            # delete transactions made with credit cards using edit_transactions_db
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0001", "delete": True}),
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0004", "delete": True}),
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0005", "delete": True}),
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0009", "delete": True}),
            Action(name="edit_transactions_db", kwargs={"transaction_id": "TXN-0012", "delete": True})
            ],
        outputs=[]
    ),
    # Task 92: Seasonal Inventory Optimization
    Task(
        annotator="0",
        user_id="task_0092",
        instruction="You are Patricia Davis. The time is 2025-07-20T18:25:00Z. Create your employee record with a role to Inventory Optimization Manager at STORE-003, check for low stock for all items at your store. Then, for apparel and office supplies category products, create a 'Back to School Ready' promotion with 30% off these products. Find the 'Floor Supervisor' at your store and change their role to 'Assistant to the Floor Supervisor'.",
        actions=[
            Action(name="edit_employees_db", kwargs={"name": "Patricia Davis", "role": "Inventory Optimization Manager", "store_id": "STORE-003"}),
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"category": ["Apparel", "Office Supplies"]}, "info_items": ["sku"]}),
            # check for low stock with check_low_stock
            Action(name="check_low_stock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T18:25:00Z"}),
            Action(name="edit_promotions_db", kwargs={"name": "Back to School Ready", "type": "percentage", "discount_value": 30.0, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01", "OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
            # get employees info by role
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"role": "Floor Supervisor", "store_id": "STORE-003"}, "info_items": ["employee_id"]}),
            # change role to Assistant to the Floor Supervisor
            Action(name="edit_employees_db", kwargs={"employee_id": "EMP-1020", "role": "Assistant to the Floor Supervisor"})
        ],
        outputs=[]
    ),
    # Task 93: Mobile App Integration and Digital Rewards
    Task(
        annotator="0",
        user_id="task_0093",
        # promo for products bought by people that opt in
        instruction="You are Natalie Cooper. The time is 2025-07-20T18:25:00Z. Find which products have been bought by customers that have opted in to marketing communications. Create a 'Marketing Opt-In' promotion with 25% off these products (if the same product appears multiple times, only list it once in the promotion applicable_skus list).",
        actions=[
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"opt_in_marketing": True}, "info_items": ["customer_id"]}),
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5003", "CUST-5004", "CUST-5006", "CUST-5008", "CUST-5009", "CUST-5011"]}, "info_items": ["line_items"]}),
            # create promotion for products bought by customers that opted in
            Action(name="edit_promotions_db", kwargs={"name": "Marketing Opt-In", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["ELEC-4KTV55","ELEC-RCHAA04","GROC-GRNLBR12","GROC-SPRWAT6P","SPORT-BIKHLM01","SPORT-YOGMAT01","OFFC-ERGCHR01","HOME-DESKLMP01","BOOK-KDSSTY01","HOME-BTHTWL01","KITCH-CHEFKNF8","SMRT-THERM02"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 94: Family and Group Shopping Experience
    Task(
        annotator="0",
        user_id="task_0094",
        # reduce stock of products bought by the youngest 2 customers
        instruction="Find any products that have been bought by the youngest gold level membership customer in the system. As store owner you decide to be generous and give out one of each of these products for free. Adjust the inventory accordingly.",
        actions=[
            # get customers info by birthdate
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"membership_level": "gold"}, "info_items": ["customer_id", "birthdate"]}),
            # sort customers by birthdate to find the youngest
            Action(name="filter_and_sort_ids_by_date", kwargs={"ids_dates": {"CUST-5001": "1990-07-12", "CUST-5010": "1983-03-04"}, "sort_order": "newest", "top_n":1}),
            # get transactions info by customer_id
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"customer_id": "CUST-5001"}, "info_items": ["line_items"]}),
            # get inventory information of 4K TV
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "ELEC-4KTV55"}, "info_items": ["sku", "store_id"]}),
            # reduce stock of 4K TV by 1
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": -1, "current_time": "2025-07-20T18:26:00Z"}),
            # get inventory information of rechargeable battery
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": "ELEC-RCHAA04"}, "info_items": ["sku", "store_id"]}),
            Action(name="update_inventory_item", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T18:26:00Z"}),
        ],
        outputs=[]
    ),
    # Task 95: Cross-Store Collaboration Enhancement
    Task(
        annotator="0",
        user_id="task_0095",
        instruction="You are Zoe Martinez. The time is 2025-07-20T18:28:00Z. You are building an online store containing all the stock from STORE-004. For all items in STORE-004s inventory, create a similar inventory item with a store id 'ONLINE'. It should have the same sku and quantity as the original item. Set the product status of products affected to 'online'. Then create a promotion called 'Online Launch' with 20% off all products in the online store. ",
        actions=[
            # get all inventory items from STORE-004
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "sku", "quantity"]}),
            # create new inventory items in ONLINE store
            Action(name="edit_inventory_db", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 4, "store_id": "ONLINE", "current_time": "2025-07-20T18:28:00Z"}),
            # edit product status to online
            Action(name="edit_products_db", kwargs={"sku": "SPORT-BIKHLM01", "status": "online", "current_time": "2025-07-20T18:28:00Z"}),
            # create the promotion
            Action(name="edit_promotions_db", kwargs={"name": "Online Launch", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"})
        ],
        outputs=[]
    ),
    # Task 96: Senior Customer Appreciation Program
    Task(
        annotator="0",
        user_id="task_0096",
        instruction="You are Marcus Chen. Get the 2 most expensive products in your store's inventory. Create a 'Golden Years Special' promotion with 45% off these products, and set the start date to 2025-07-20 and end date to 2025-12-31. Ava Thompson then comes to the store and purchases ProSlice 8\" Chef Knife using her credit card. The time is 2025-07-20T18:29:00Z.",
        actions=[
            # get employee id
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Marcus Chen"}, "info_items": ["employee_id", "store_id"]}),
            # get the 2 most expensive products in STORE-002
            Action(name="get_top_n_most_expensive_products_by_store", kwargs={"store_id": "STORE-002", "n": 2}),
            # create the promotion
            Action(name="edit_promotions_db", kwargs={"name": "Golden Years Special", "type": "percentage", "discount_value": 45.0, "applicable_skus": ["ELEC-GAMLP15", "CLTH-WINJKT01"], "start_date": "2025-07-20", "end_date": "2025-12-31"}),
            # get the customer_id of Ava Thompson
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Ava Thompson"}, "info_items": ["customer_id"]}),
            # get the sku of ProSlice 8\" Chef Knife
            Action(name="get_products_info_by_param", kwargs={"filter_params": {"name": "ProSlice 8\" Chef Knife"}, "info_items": ["sku"]}),
            # Create a purchase transaction for Ava Thompson
            Action(name="create_purchase_transaction", kwargs={"customer_id": "CUST-5001", "employee_id": "EMP-1008", "items":{"KITCH-CHEFKNF8":1}, "payment_method": "credit_card", "store_id": "STORE-002", "current_time": "2025-07-20T18:29:00Z"}),
            # reduce the inventory of ProSlice 8\" Chef Knife by 1
            Action(name="update_inventory_item", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T18:29:00Z"}),
        ],
        outputs=[]
    ),
    # Task 97: Gift Card and Gifting Program Expansion
    Task(
        annotator="0",
        user_id="task_0097",
        instruction="You are Ethan Walker. The time is 2025-07-20T18:30:00Z. Create a 'Perfect Gift Finder' promotion with 25% off products that weigh less than 0.2 kg. Create a new inventory item in STORE-002 called 'Lightweight Gifts', with an SKU of 'LW-GIFTS' and for the quantity calculate and use the total quantity of all products in the promotion across all store inventories.",
        actions=[
            # get all products and their weight
            Action(name="get_products_info_by_param", kwargs={"filter_params": {}, "info_items": ["sku", "weight_kg"]}),
            # create the promotion
            Action(name="edit_promotions_db", kwargs={"name": "Perfect Gift Finder", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            # Get inventory quantities for the promotion items
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"sku": ["AUDIO-NCEBUDS01", "ELEC-RCHAA04"]}, "info_items": ["sku", "quantity"]}),
            # create new inventory item 'Lightweight Gifts'
            Action(name="edit_inventory_db", kwargs={"sku": "LW-GIFTS", "quantity": 112, "store_id": "STORE-002", "current_time": "2025-07-20T18:30:00Z"}),
        ],
        outputs=[]
    ),
    # Task 98: Flash Sale and Limited-Time Offer Strategy
    Task(
        annotator="0",
        user_id="task_0098",
        instruction="You are Amanda Richards. The time is 2025-07-20T18:31:00Z. Execute a surprise flash sale strategy. Create a '1 day Lightning Deal' promotion with 55% off products priced over $500. The promotion should start and end today. Then add a new employee called 'Tom Thomas' with the role 'Sales Associate' to 'STORE-001' to help staff the sales rush.",
        actions=[
            # get all products and their price and sku
            Action(name="get_products_info_by_param", kwargs={"filter_params": {}, "info_items": ["sku", "price"]}),
            Action(name="edit_promotions_db", kwargs={"name": "1 day Lightning Deal", "type": "percentage", "discount_value": 55.0, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15"], "start_date": "2025-07-20", "end_date": "2025-07-20"}),
            # add the new employee
            Action(name="edit_employees_db", kwargs={"name": "Tom Thomas", "role": "Sales Associate", "store_id": "STORE-001"}),
        ],
        outputs=[]
    ),
    # Task 99: Customer Referral and Network Growth
    Task(
        annotator="0",
        user_id="task_0099",
        instruction="Find the promotion that has been used the most amount of times. Double its usage limit and set it to expire this day next year. Find all customers that have purchased products that were part of this promotion and add 50 loyalty points to their accounts. The time is 2025-07-20T18:32:00Z.",
        actions=[
            # get times used for each promotion
            Action(name="get_promotions_info_by_param", kwargs={"filter_params": {}, "info_items": ["promotion_id", "times_used"]}),
            # get the skus from promo-002
            Action(name="get_promotions_info_by_param", kwargs={"filter_params": {"promotion_id": "PROMO-002"}, "info_items": ["applicable_skus", "usage_limit", "end_date"]}),
            # double the usage limit of promo-002 and set it to expire next year
            Action(name="edit_promotions_db", kwargs={"promotion_id": "PROMO-002", "usage_limit": 1000, "end_date": "2026-07-20"}),
            # get all customers that have purchased these skus
            Action(name="get_transactions_info_by_param", kwargs={"filter_params": {"sku":["HOM-COFMKR12", "KITCH-CHEFKNF8"]}, "info_items": ["customer_id"]}),
            # get the loyalty points of these customers
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"customer_id": ["CUST-5002", "CUST-5011"]}, "info_items": ["customer_id", "loyalty_points"]}),
            # add 50 loyalty points to these customers
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5002", "loyalty_points": 925, "current_time": "2025-07-20T18:32:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5011", "loyalty_points": 610, "current_time": "2025-07-20T18:32:00Z"})
        ],
        outputs=[]
    ),
    # Task 100: Data Analytics and Customer Insights Program
    Task(
        annotator="0",
        user_id="task_0100",
        instruction="You are Jack Robinson. Charlie Chaplin comes into your store and wants to buy the store's entire quantity of each inventory item in your store's inventory. Add Charlie to the customer database with email 'charlie.chaplin@example.com' and process the purchase transaction, paid with credit_card. Be sure to update the inventory levels accordingly. The time is 2025-07-20T18:33:00Z. Get the total cost of the transaction and add one loyalty point for every whole dollar spent, ignoring any cents.",
        actions=[
            Action(name="edit_customers_db", kwargs={"name": "Charlie Chaplin", "email": "charlie.chaplin@example.com", "current_time": "2025-07-20T18:33:00Z"}),
            Action(name="get_customers_info_by_param", kwargs={"filter_params": {"name": "Charlie Chaplin"}, "info_items": ["customer_id"]}),
            Action(name="get_employees_info_by_param", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id", "store_id"]}),
            Action(name="get_inventory_info_by_param", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["sku", "quantity"]}),
            Action(name="create_purchase_transaction", kwargs={"employee_id": "EMP-1034", "customer_id": "CUST-5013", "items": {"SPORT-BIKHLM01": 4}, "current_time": "2025-07-20T18:33:00Z", "store_id": "STORE-004", "payment_method": "credit_card"}),
            # update inventory levels
            Action(name="update_inventory_item", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004", "quantity_change": -4, "current_time": "2025-07-20T18:33:00Z"}),
            Action(name="edit_customers_db", kwargs={"customer_id": "CUST-5013", "loyalty_points": 314, "current_time": "2025-07-20T18:33:00Z"})
        ],
        outputs=[]
    ),
]
