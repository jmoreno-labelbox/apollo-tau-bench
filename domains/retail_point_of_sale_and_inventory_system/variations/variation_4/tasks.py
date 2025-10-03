from domains.dto import Task, Action

TASKS = [
    Task(
        annotator="0",
        user_id="task_0001",
        instruction="Assume the role of Henry Adams. The current time is 2025-07-20T16:35:00Z. Emma Wilson has returned a faulty UltraVision 55\" 4K Smart TV to STORE-001. Once you process the refund, change the product's status to 'inactive' and introduce a 10% discount named 'Return Discount - Emma Wilson' for her subsequent purchase, applicable exclusively to the same product within the upcoming month.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Emma Wilson"}, "info_items": ["customer_id", "email"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "UltraVision 55\" 4K Smart TV"}, "info_items": ["sku"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": 1, "current_time": "2025-07-20T16:35:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}, "info_items": ["transaction_id"]}),
            Action(name="CreateRefundTransaction", kwargs={"sku": "ELEC-4KTV55", "quantity": 1, "employee_id": "EMP-1020", "current_time": "2025-07-20T16:35:00Z", "original_transaction_id": "TXN-0001"}),
            Action(name="EditProductsDb", kwargs={"sku": "ELEC-4KTV55", "status": "inactive", "current_time": "2025-07-20T16:35:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Return Discount - Emma Wilson", "type": "percentage", "discount_value": 10.0, "applicable_skus": ["ELEC-4KTV55"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0002",
        instruction="At STORE-003, a new shipment of 20 BrewMaster 12-Cup Coffee Makers has arrived. The time now is 2025-07-20T16:35:00Z. Initiate an inventory entry for these and include the fresh stock. Charlie Brown, the Delivery Driver, requests to be included in the employee database to utilize the 'Employee Discount', granting a 10% reduction on the coffee maker over the coming year. On noticing that the discount isn't in the database, you proceed to create it.",
        actions=[
            # Get the product SKU for BrewMaster 12-Cup Coffee Maker
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "BrewMaster 12-Cup Coffee Maker"}, "info_items": ["sku"]}),
            # Create new inventory item for BrewMaster 12-Cup Coffee Maker in STORE-003 using edit_inventory_db
            Action(name="EditInventoryDb", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "quantity": 20, "current_time": "2025-07-20T16:35:00Z"}),
            # Add Charlie Brown as an employee
            Action(name="EditEmployeesDb", kwargs={"name": "Charlie Brown", "role": "Delivery Driver", "store_id": "STORE-003"}),
            # Create the 'Employee Discount' promotion for BrewMaster 12-Cup Coffee Maker
            Action(name="EditPromotionsDb", kwargs={"name": "Employee Discount", "type": "percentage", "discount_value": 10.0, "applicable_skus": ["HOM-COFMKR12"], "start_date": "2025-07-20", "end_date": "2026-07-20"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0003",
        instruction="Act as Amelia Lee. It's 2025-07-20T16:35:00Z. Customer Emma Wilson purchases a GigaPlay 15\" Gaming Laptop from STORE-002 using her credit_card. The acquisition of 1500 loyalty points elevates her to a platinum membership. Record the purchase, update her membership status and loyalty points, and obtain her email to send a congratulatory email.",
        actions=[
            # Get Emma Wilson's customer ID, email and loyalty points
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Emma Wilson"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            # Get the GigaPlay 15" Gaming Laptop SKU
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "GigaPlay 15\" Gaming Laptop"}, "info_items": ["sku"]}),
            # Get Amelia Lee's employee ID
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Create purchase transaction for Emma Wilson
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5001", "employee_id": "EMP-1032", "items": {"ELEC-GAMLP15": 1}, "store_id": "STORE-002","payment_method": "credit_card","current_time": "2025-07-20T16:35:00Z",}),
            # Update stock
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T16:35:00Z"}),
            # Update Emma Wilson's loyalty points and membership status
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "loyalty_points": 2740, "membership_level": "platinum", "current_time": "2025-07-20T16:35:00Z"}),
        ],
        outputs=[{"email": "emma.wilson@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0004",
        instruction="With the hiring of Jack Thomas as a 'Customer Experience Specialist' for STORE-005, it is essential to add him to the employee database at 2025-07-20T16:41:00Z. Jack is also interested in buying a WaveSound All-Weather Bluetooth Speaker, so register him as a customer using his new employee email address. Log the purchase utilizing both his customer_id and his employee_id, and ensure the transaction is completed with a debit_card. Obtain Jack's email for future reference.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Jack Thomas", "role": "Customer Experience Specialist", "store_id": "STORE-005"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jack Thomas"}, "info_items": ["employee_id", "email"]}),
            Action(name="EditCustomersDb", kwargs={"name": "Jack Thomas", "email": "jack.thomas@retailpos.com", "current_time": "2025-07-20T16:41:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "WaveSound All-Weather Bluetooth Speaker"}, "info_items": ["sku"]}),
            Action(name="CreatePurchaseTransaction", kwargs={"employee_id": "EMP-1013", "customer_id": "CUST-5013", "items": {"AUDIO-BTSPKR02": 1}, "store_id": "STORE-005", "current_time": "2025-07-20T16:41:00Z", "payment_method": "debit_card"}),
            # reduce inventory for WaveSound All-Weather Bluetooth Speaker
            Action(name="UpdateInventoryItem", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005", "quantity_change": -1, "current_time": "2025-07-20T16:41:00Z"}),
        ],
        outputs=[{"email":"jack.thomas@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0005",
        instruction="As Sarah Anderson at STORE-001, the current time is 2025-07-20T16:35:00Z. Customer Sophia Singh is relocating to 123 Elm St, Riverside, IL. It's your task to update her profile and acquire her email for sending a confirmation email. She wishes to use all her loyalty points on a LumiLux LED Desk Lamp to reduce the price by 1 cent per point, paying the remainder by credit_card. Execute the transaction, adjust it with the loyalty points discount, and update the price.",
        actions=[
            # Get customer_id and email, and loyalty points for olivia patel
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Sophia Singh"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            # Update address and marketing opt_in
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5003", "address": "123 Elm St, Riverside, IL", "opt_in_marketing": False, "current_time": "2025-07-20T16:35:00Z"}),
            # Get sku for LumiLux LED Desk lamp
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "LumiLux LED Desk Lamp"}, "info_items": ["sku", "price"]}),
            # Get employee_id for Grace Miller
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sarah Anderson"}, "info_items": ["employee_id"]}),
            # Create a purchase transaction
            Action(name="CreatePurchaseTransaction", kwargs={"employee_id": "EMP-1002", "customer_id": "CUST-5003", "items": {"HOME-DESKLMP01": 1}, "store_id": "STORE-001", "current_time": "2025-07-20T16:36:00Z", "payment_method": "credit_card"}),
            # Update the inventory for LumiLux LED Desk Lamp
            Action(name="UpdateInventoryItem", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001", "quantity_change": -1, "current_time": "2025-07-20T16:37:00Z"}),
            # Edit the purchase transaction discount_total and total_price (460 loyalty points = $4.60 discount)
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-1013", "discount_total": 7.40, "total_amount": 30.48, "current_time": "2025-07-20T16:37:00Z"}),
            # Remove 460 loyalty points from Olivia Patel's account
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5003", "loyalty_points": 0, "current_time": "2025-07-20T16:37:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0006",
        instruction="Playing the role of Megan Young, and it's 2025-04-30T16:40:00Z at STORE-002. Discover if any customers have today's birthday, retrieve their email address to offer a birthday discount. Create a 20% discount for today only called '<customer_name> Birthday Discount'. Also, recognize it's Frank Mitchell's birthday and set up an account for him using 'frank@email.com'. Make a purchase in the 'Electronics' section from 'QuietTone' using your employee_id and credit_card, ensuring inventory is adjusted.",
        actions=[
            Action(name="GetCustomersWithBirthdayToday", kwargs={"current_day": "04-30"}),
            # Get the customer email address
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email", "name"]}),
            # Create the birthday discount
            Action(name="EditPromotionsDb", kwargs={"name": "William Zhang Birthday Discount", "type":"percentage", "discount_value": 20, "applicable_skus":[],"start_date": "2025-04-30", "end_date": "2025-04-30"}),
            #create Frank Mitchell's customer account
            Action(name="EditCustomersDb", kwargs={"name": "Frank Mitchell", "email": "frank@email.com", "current_time": "2025-04-30T16:40:00Z"}),
            # Get the QuietTone brand products in Electronics
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"brand": "QuietTone", "category": "Electronics"}, "info_items": ["sku"]}),
            # Get Megan Young's employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["employee_id"]}),
            # Create the purchase transaction for Frank Mitchell
            Action(name="CreatePurchaseTransaction", kwargs={"employee_id": "EMP-1045", "customer_id": "CUST-5013", "items": {"AUDIO-NCEBUDS01": 1}, "store_id": "STORE-002", "current_time": "2025-04-30T16:40:00Z", "payment_method": "credit_card"}),
            # Update the inventory for the purchased product
            Action(name="UpdateInventoryItem", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-04-30T16:40:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0007",
        instruction="In the persona of Jennifer Williams at 2025-07-20T16:45:00Z. Noah Tran contacts requesting the return of a defective ProSlice 8\" Chef Knife and complete database removal. Manage the return, refresh inventory, and since you're displeased with the knives, set their reorder level to 0 and their status to 'last_stock'. Create a 15% off 'End of stock Discount' on knives for the next year, and collect Liam’s email for sending a confirmation.",
        actions=[
            # Get Liam Nguyen's customer_id
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Noah Tran"}, "info_items": ["customer_id", "email"]}),
            # Get the product SKU for ProSlice 8" Chef Knife
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "ProSlice 8\" Chef Knife"}, "info_items": ["sku"]}),
            # Get the transaction ID for the purchase of ProSlice 8" Chef Knife
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5002", "sku": "KITCH-CHEFKNF8"}, "info_items": ["transaction_id"]}),
            # Get Jennifer Williams's employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["employee_id"]}),
            # Process the return using create_refund_transaction
            Action(name="CreateRefundTransaction", kwargs={"sku": "KITCH-CHEFKNF8", "quantity": 1, "employee_id": "EMP-1004", "original_transaction_id": "TXN-0002", "current_time": "2025-07-20T16:45:00Z"}),
            # Remove the customer from the database
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5002", "delete": True}),
            # Update the inventory
            Action(name="UpdateInventoryItem", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002", "quantity_change": 1, "current_time": "2025-07-20T16:45:00Z"}),
            # Set reorder level to 0 and change status to 'last_stock'
            Action(name="EditInventoryDb", kwargs={"id": "INV-0011", "status": "last_stock", "reorder_level": 0, "current_time": "2025-07-20T16:45:00Z"}),
            # Create the promotion 'End of stock Discount'
            Action(name="EditPromotionsDb", kwargs={"name": "End of stock Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["KITCH-CHEFKNF8"], "start_date": "2025-07-20", "end_date": "2026-07-20"}),
        ],
        outputs=["liam.nguyen@example.com"]
    ),
    Task(
        annotator="0",
        user_id="task_0008",
        instruction= "The date is 2025-07-02T07:30:00Z. You, Grace Miller, aim to reward shoppers spending over $1500 by gifting them a 20% reduction on KITCH-CHEFKNF8 within the next month. Develop the 'My Favourite Customers' promotion and secure the emails of qualified customers to inform them.",
        actions=[
            # Get all customers who have spent more than $1500 using GetCustomersAboveXSpend
            Action(name="GetCustomersAboveXSpend", kwargs={"amount": 1500}),
            # Create the promotion 'My Favourite Customers'
            Action(name="EditPromotionsDb", kwargs={"name": "My Favourite Customers", "type": "percentage", "discount_value": 20, "applicable_skus": ["KITCH-CHEFKNF8"], "start_date": "2025-07-02", "end_date": "2025-08-02"}),
            # Get the email addresses of these customers
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5005"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"emma.garcia@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0009",
        instruction="You, Daniel Perez, are tasked on 2025-07-20T16:50:00Z. Charlotte Dubois wishes to return 10 defective UltraSoft Cotton Bath Towels. Facilitate the return, adjust the inventory, and get her email to confirm the process. If the towels aren't in inventory, establish an entry and include the returned units. Next, create 'Bath Towel Return Discount' at 10% off for one year.",
        actions=[
            # Get Charlotte Dubois's customer_id
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id"]}),
            # Get the product SKU for UltraSoft Cotton Bath Towel
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "UltraSoft Cotton Bath Towel"}, "info_items": ["sku"]}),
            # Get the transaction ID for the purchase of UltraSoft Cotton Bath Towel
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5009", "sku": "HOME-BTHTWL01"}, "info_items": ["transaction_id"]}),
            # Get Michael Rodriguez's employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Michael Rodriguez"}, "info_items": ["employee_id"]}),
            # Process the return using create_refund_transaction
            Action(name="CreateRefundTransaction", kwargs={"sku": "HOME-BTHTWL01", "quantity": 10, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0009", "current_time": "2025-07-20T16:50:00Z"}),
            # Check if the product is in the inventory
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "HOME-BTHTWL01", "store_id": "STORE-004"}, "info_items": ["sku"]}),
            # If not in inventory, create a new inventory item for UltraSoft Cotton
            Action(name="EditInventoryDb", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-004", "quantity": 10, "current_time": "2025-07-20T16:50:00Z"}),
            # Create the promotion 'Bath Towel Return Discount' using edit_promotions_db
            Action(name="EditPromotionsDb", kwargs={"name": "Bath Towel Return Discount", "type": "percentage", "discount_value": 10, "applicable_skus": ["HOME-BTHTWL01"], "start_date": "2025-07-20", "end_date": "2026-07-20"}),
            # Get Charlotte Dubois's email address
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"charlotte.dubois@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0010",
        instruction="In your role as Oliver Diaz, at 2025-07-20T16:55:00Z, Ava Thompson has joined as a Sales Associate in 'Home & Kitchen' at STORE-001. Register her in the employee database and launch a 15% 'New Employee Welcome Discount' on all 'Home & Kitchen' items for a month. Secure Ava's email to send her a welcoming message.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Emma Wilson", "role": "Sales Associate", "store_id": "STORE-001"}),
            # Get Home & Kitchen products
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Home & Kitchen"}, "info_items": ["sku"]}),
            # Create the promotion 'New Employee Welcome Discount'
            Action(name="EditPromotionsDb", kwargs={"name": "New Employee Welcome Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
            # Get Ava's email address
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Ava Thompson"}, "info_items": ["email"]})
        ],
        outputs=[{"email":"ava.thompson@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0011",
        instruction="The time is 2025-07-20T16:55:00Z. Record the new product, 'EcoBrew Reusable Coffee Filter', in the product database using details from the manufacturer. With attributes paralleling 'BrewMaster 12-Cup Coffee Maker', order 100 units for 'Kitchen & Dining' at STORE-001. Then extract names and emails of 'BrewMaster' purchasers to inform them about the launch.",
        actions=[
            # Get the supplier_id for BrewMaster 12-Cup Coffee Maker
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "BrewMaster 12-Cup Coffee Maker"}, "info_items": ["supplier_id", "sku"]}),
            Action(name="EditProductsDb", kwargs={"name": "EcoBrew Reusable Coffee Filter", "description": "An eco-friendly reusable coffee filter made from organic cotton, designed to fit most standard coffee makers.", "supplier_id": "SUP-1002", "weight_kg": 0.1, "cost": 3.50, "price": 5.99, "current_time": "2025-07-20T16:55:00Z"}),
            # get the SKU for the new product
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "EcoBrew Reusable Coffee Filter"}, "info_items": ["sku"]}),
            # Add the new product to the inventory in STORE-001
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity": 100, "current_time": "2025-07-20T16:55:00Z", "location": "Kitchen & Dining"}),
            # Get the email addresses of customers who have purchased BrewMaster 12-Cup Coffee Maker using GetCustomerPurchaseCountBySku
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            # Get the email addresses of these customers
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["name", "email"]})
        ],
        outputs=[{"name": "Liam Nguyen", "email": "liam.nguyen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0012",
        instruction="The current moment, 2025-07-20T16:56:00Z, reveals a robbery affecting STORE-003’s top three costly items. Reflect this in inventory, setting their status to 'stolen', and perform a stock check. Remove discounts from items eligible that are 'low_stock' or 'critical', and obtain the Floor Supervisor's email for notice.",
        actions=[
            # Get the top 3 most expensive products in STORE-003
            Action(name="GetTopNMostExpensiveProductsByStore", kwargs={"store_id": "STORE-003", "n": 3}),
            # get inventory ids for these products
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": ["KITCH-FRYPAN10", "OFFC-ERGCHR01", "ELEC-RCHAA04"], "store_id": "STORE-003"}, "info_items": ["id"]}),
            # Update the inventory to reflect the stolen products
            Action(name="EditInventoryDb", kwargs={"id": "INV-0023", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0014", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0020", "quantity": 0, "status": "stolen", "current_time": "2025-07-20T16:56:00Z"}),
            # Perform a low stock check
            Action(name="CheckLowStock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T16:56:00Z"}),
            # Remove discounts for low stock or critical items
            Action(name="EditProductsDb", kwargs={"sku": "KITCH-FRYPAN10", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="EditProductsDb", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            Action(name="EditProductsDb", kwargs={"sku": "ELEC-RCHAA04", "is_discountable": False, "current_time": "2025-07-20T16:56:00Z"}),
            # Find the email addresses of the Floor Supervisor
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003", "position": "Floor Supervisor"}, "info_items": ["email"]})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0013",
        instruction="Playing Jack Robinson, at 2025-07-20T16:57:00Z. Install a 'Loyalty point multiplier' promotion for 7 days, offering points valued 5 times more (normally 1 cent, now 5 cents per point). Manage Olivia Romano’s purchase of PowerPlus Rechargeable AA Batteries, adjust inventory, tally the loyalty points cost, and adjust Sophia's records. Retrieve her email to confirm the transaction.",
        actions=[
            # Create the 'Loyalty point multiplier' promotion
            Action(name="EditPromotionsDb", kwargs={"name": "Loyalty point multiplier", "type": "loyalty_multiplier", "discount_value": 5, "start_date": "2025-07-20", "end_date": "2025-07-27", "applicable_skus": []}),
            # Get Sophia's email, customer_id and loyalty points
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Olivia Romano"}, "info_items": ["customer_id","email", "loyalty_points"]}),
            # Get Jacks employee ID
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            # Get the SKU for PowerPlus Rechargeable AA Batteries (4 Pack)
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}, "info_items": ["sku"]}),
            # Create the transaction
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5007", "items": {"ELEC-RCHAA04":1}, "store_id": "STORE-003", "employee_id": "EMP-1034", "current_time": "2025-07-20T16:57:00Z", "payment_method": "loyalty_points"}),
            # Update the inventory
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T16:57:00Z"}),
            # Might need to make an API function for the maths here
            # Edit Sophia's loyalty points to reflect the purchase
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5007", "loyalty_points": 26, "current_time": "2025-07-20T16:57:00Z"}),  # Assuming the cost is fully covered by loyalty points
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0014",
        instruction="You are Emma Garcia, handling promotions at 2025-07-06T16:58:00Z. Review existing percentage promotions. If 'Summer Electronics Sale' exists, raise discounts by 10%. Otherwise, start 'Summer Sale' with a 25% reduction for a month. Gather emails from last month's customers to inform about the promotion change.",
        actions=[
            # Check if the 'Summer Electronics Sale' promotion exists
            Action(name="GetPromotionsInfoByParam", kwargs={"filter_params": {"name": "Summer Electronics Sale"}, "info_items": ["promotion_id", "discount_value"]}),
            # Update the promotion
            Action(name="EditPromotionsDb", kwargs={"promotion_id": "PROMO-001", "discount_value": 20}),
            # Get customer_ids and timestamps of purchases
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params":{}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates":{ "CUST-5001": "2025-06-05", "CUST-5002": "2025-06-05", "CUST-5003": "2025-06-05", "CUST-5004": "2025-06-05", "CUST-5005": "2025-06-05", "CUST-5006": "2025-06-05", "CUST-5007": "2025-06-05", "CUST-5008": "2025-06-05", "CUST-5009": "2025-06-05", "CUST-5010": "2025-06-05", "CUST-5011": "2025-06-06", "CUST-5012": "2025-06-06"},"filter_start_date": "2025-06-06", "filter_end_date": "2025-07-06"}),
            # Get email addresses of customers who purchased during the last month
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5011", "CUST-5012"]}, "info_items": ["email"]}),
        ],
        outputs=[
            {"emails": ["mia.kim@example.com", "logan.smith@example.com"]}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_0015",
        instruction="As Noah Tran, it's 2025-07-20T16:59:00Z. Check STORE-004 inventory quantities. For items below 5 units, order 10 more, changing their status to 'in_stock'. Aggregate employee emails to notify them about the order.",
        actions=[
            # Get all products in STORE-004 with their inventory levels
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "quantity"]}),
            # Filter products with quantity below 5
            Action(name="EditInventoryDb", kwargs={"id": "INV-0009", "quantity": 14, "status": "in_stock", "current_time": "2025-07-20T16:59:00Z"}),
            # Get the email addresses of all employees in STORE-004
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["email"]}),
        ],
        outputs=[{"email":"amelia.lee@retailpos.com"}, {"email":"jack.robinson@retailpos.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0016",
        instruction="Taking on the role of Olivia Patel at 2025-07-20T17:00:00Z, inspect STORE-002 sales performance. If lifetime sales are under $10,000, launch 'Sales Boost' at 15% off for two weeks. Retrieve email addresses of STORE-002 shoppers for promotion notification.",
        actions=[
            # Get all transactions in for STORE-002
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["total_amount", "customer_id"]}),
            # Get total sales for STORE-002 in the last month

            # Create the appropriate promotion based on sales performance
            Action(name="EditPromotionsDb", kwargs={"name": "Sales Boost", "type": "percentage", "discount_value": 15, "start_date": "2025-07-20", "end_date": "2025-08-03", "applicable_skus": []}),
            # Get email addresses of customers who purchased in STORE-002 during the last month
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5011", "CUST-5002", "CUST-5006"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "mia.kim@example.com"}, {"email": "william.zhang@example.com"}, {"email": "liam.nguyen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0017",
        instruction="Under the guise of Henry Adams, the inventory crisis at STORE-003 finds 40 'High-Protein Granola Bars (12 Pack)' consumed by mice at 2025-07-20T17:00:00Z. Revise inventory and perform low stock checks. If items register as low, secure the Inventory Specialist’s details, terminate them, and replace yourself as the new specialist.",
        actions=[
            # Get the SKU for High-Protein Granola Bars (12 Pack)
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "High-Protein Granola Bars (12 Pack)"}, "info_items": ["sku"]}),
            # Update the inventory to reflect the eaten products
            Action(name="UpdateInventoryItem", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -40, "current_time": "2025-07-20T17:00:00Z"}),
            # Perform a low stock check
            Action(name="CheckLowStock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T17:00:00Z"}),
            # Get the Inventory Specialist's name and email
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Inventory Specialist"}, "info_items": ["name", "email", "phone_number", "employee_id"]}),
            # Remove the Inventory Specialist from the employee database
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1015", "delete": True}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1020", "role": "Inventory Specialist"}),
        ],
        outputs=[{"name": "Zoe Martinez", "email": "zoe.martinez@retailpos.com", "phone_number": "+1-555-210-1015"}]
    ),
    Task(
        annotator="0",
        user_id="task_0018",
        instruction="As Emma Garcia, with a mission in mind at 2025-07-20T17:01:00Z, target transaction TXN-0012 to modify the total to $150.00. Aim to secure the customer's email tied to this transaction for updates.",
        actions=[
            # Get the transaction details by transaction ID
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"transaction_id": "TXN-0012"}, "info_items": ["customer_id"]}),
            # Edit the transaction total amount
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0012", "total_amount": 150.00, "current_time": "2025-07-20T17:01:00Z"}),
            # Get the customer email address associated with the transaction
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["email"]}),
        ],
        outputs=[{"logan.smith@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0019",
        instruction="In the capacity of Liam Nguyen at 2025-07-20T17:02:00Z, unveil a 'Wireless Mouse' entry. Tag the price at $25.00 and retain other entries as default. Stock 100 units in 'Electronics' of STORE-001. If STORE-002 possesses SKU 'AUDIO-NCEBUDS01', relocate half the 'Wireless Mouse' stock there and craft an inventory entry for STORE-002, reviewing STORE-001 quantities concurrently.",
        actions=[
            # Create the new product in the database
            Action(name="EditProductsDb", kwargs={"name": "Wireless Mouse", "price": 25.00, "current_time": "2025-07-20T17:02:00Z"}),
            # Create inventory for product
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity": 100, "current_time": "2025-07-20T17:02:00Z", "location": "Electronics"}),
            # Check if STORE-002 has stock of AUDIO-NCEBUDS01
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-002", "sku": "AUDIO-NCEBUDS01"}, "info_items": ["quantity"]}),
            # If it does, move half of the stock to STORE-002
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021", "store_id": "STORE-002", "quantity": 50, "current_time": "2025-07-20T17:02:00Z", "location": "Electronics"}),
            # If it does, update the quantity in STORE-001
            Action(name="UpdateInventoryItem", kwargs={"sku": "SKU-1021", "store_id": "STORE-001", "quantity_change": -50, "current_time": "2025-07-20T17:02:00Z"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0020",
        instruction="Acting as Amelia Lee at 2025-07-20T17:03:00Z, devise a new promotion spanning all 'Books'. Label it 'Back to School Sale' with 20% off, operating between 2025-08-01 and 2025-08-31. Extract emails of past book buyers to notify about the offer.",
        actions=[
            # Get all book products
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Books"}, "info_items": ["sku"]}),
            # Create the new promotion in the database
            Action(name="EditPromotionsDb", kwargs={"name": "Back to School Sale", "type": "percentage", "discount_value": 20, "start_date": "2025-08-01", "end_date": "2025-08-31", "applicable_skus": ["BOOK-KDSSTY01"]}),
            # Get the email addresses of customers who have purchased book products
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "BOOK-KDSSTY01"}),
            # Create a list of customer IDs who have purchased books
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5008"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "james.oconnor@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0021",
        instruction="The timestamp is 2025-07-20T17:04:00Z. Compile a list of customers eclipsing $750 in spending. Procure their emails for sale announcements, and launch 'VIP Customer Sale' with a 10% discount for the upcoming month.",
        actions=[
            # Get customers who have spent more than $750
            Action(name="GetCustomersAboveXSpend", kwargs={"amount": 750.0}),
            # Get the email addresses of these customers
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001","CUST-5005"]}, "info_items": ["email"]}),
            # Create the 'VIP Customer Sale' promotion
            Action(name="EditPromotionsDb", kwargs={"name": "VIP Customer Sale", "type": "percentage", "discount_value": 10, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[{"email": "emma.garcia@example.com"}, {"email": "ava.thompson@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0022",
        instruction="Perform as Oliver Diaz at 2025-07-20T17:05:00Z. Investigate inventory levels in STORE-001. For items below a 10-quantity threshold, submit SKU and count for reorder. Check STORE-001’s employee count, appoint Marty Skipper as 'Inventory Specialist' if it’s less than 10.",
        actions=[
            # Get all products in STORE-001 with their inventory levels
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["id","sku", "quantity"]}),
            # Update last stock count for items that need to be reordered
            Action(name="EditInventoryDb", kwargs={"id": "INV-0001", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:05:00Z"}),
            # Check the number of employees in STORE-001
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["employee_id"]}),
            # If less than 10 employees, add Marty Skipper as a new employee
            Action(name="EditEmployeesDb", kwargs={"name": "Marty Skipper", "role": "Inventory Specialist", "store_id": "STORE-001"}),

        ],
        outputs=[{"sku": "ELEC-4KTV55","quantity": 8,}]
    ),
    Task(
        annotator="0",
        user_id="task_0023",
        instruction="In the role of Natalie Cooper at 2025-07-20T17:06:00Z, analyze your clientele, contrasting the top loyalty customer against frequentists of the store’s most costly item. Secure the 'Floor Supervisor’s' email later for survey analysis. If significant variance exists, consider buying yourself 'High-Protein Granola Bars (12 Pack)' with your credit, assuming a customer identity if absent.",
        actions=[
            # Get the top customer by loyalty points
            Action(name="GetTopNCustomersByLoyaltyPoints", kwargs={"n": 1}),
            # Get the store's most expensive product
            Action(name="GetTopNMostExpensiveProductsByStore", kwargs={"store_id": "STORE-003", "n": 1}),
            # Get the customer who bought the most of the most expensive product
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            # check if Jennifer Williams is in the customer database
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Jennifer Williams"}, "info_items": ["customer_id"]}),
            # Get Jennifer Williams's employee email address to use
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Natalie Cooper"}, "info_items": ["email"]}),
            # If not, add Jennifer Williams as a customer
            Action(name="EditCustomersDb", kwargs={"name": "Natalie Cooper", "email": "natalie.cooper@retailpos.com", "current_time": "2025-07-20T17:06:00Z"}),
            # Create a purchase transaction for Jennifer Williams if she is not the same as the top customer by loyalty points
            # get product SKU for High-Protein Granola Bars (12 Pack)
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "High-Protein Granola Bars (12 Pack)"}, "info_items": ["sku"]}),
            # get Jennifer Williams's employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jennifer Williams"}, "info_items": ["employee_id"]}),
            # Create the purchase transaction
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5013", "items": {"GROC-GRNLBR12": 1}, "store_id": "STORE-003", "employee_id": "EMP-1004", "current_time": "2025-07-20T17:06:00Z", "payment_method": "credit_card"}),
            # Update the inventory for the purchase
            Action(name="UpdateInventoryItem", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T17:06:00Z"}),
            # Get the email address of the Department Manager
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Floor Supervisor"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "henry.adams@retailpos.com"}]
    ),
    # task that looks at the current promotions
    Task(
        annotator="0",
        user_id="task_0024",
        instruction="As Mia Johnson at 2025-07-20T17:07:00Z, dissect promotions to identify active 'bogo_percentage' ones. Connect recent deals related to these with relevant transaction employees, promoting them to 'Manager.'",
        actions=[
            # Get all percentage promotions
            Action(name="GetPromotionsInfoByParam", kwargs={"filter_params": {"type": "bogo_percentage"}, "info_items": ["applicable_skus"]}),
            # Find transactions with these products
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": "SPORT-YOGMAT01"}, "info_items": ["transaction_id", "timestamp"]}),
            # Get the most recent transaction using filter_and_sort_ids_by_date
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"TXN-0004": "2025-06-05T12:48:11Z"}, "top_n": 1, "sort_order": "newest"}),
            # Find employee who made the transaction
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"transaction_id": "TXN-0004"}, "info_items": ["employee_id"]}),
            # Promote the employee to Manager
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1032", "role": "Manager"}),
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="task_0025",
        instruction="Embody Megan Young at 2025-07-20T17:08:00Z. Update transaction TXN-0010 by swapping 'credit_card' to 'loyalty_points', adjusting the total to $50.00, and attribute the transaction under your name. Compute and add relevant loyalty points before retrieving the customer's email.",
        actions=[
            # Get employee ID for Megan Young
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["employee_id"]}),
            # edit the transaction to change the payment method and total amount
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0010", "payment_method": "loyalty_points", "total_amount": 50.00, "employee_id": "EMP-1045", "current_time": "2025-07-20T17:08:00Z"}),
            # Get the transaction details by transaction ID
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"transaction_id": "TXN-0010"}, "info_items": ["customer_id", "total_amount"]}),
            # Get customer loyalty points
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["loyalty_points"]}),
            # Add loyalty points to customer's account
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5010", "loyalty_points": 1075, "current_time": "2025-07-20T17:08:00Z"}),
            # Get the customer email address associated with the transaction
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    Task(
        annotator="0",
        user_id="task_0026",
        instruction="Taking the part of Megan Young at 2025-07-20T17:09:00Z, produce an employee account for John Doe under 'Chief Cheerleader', dated today. Gather 'low_stock' items list, refresh 'last_stock_count' entries, and acquire your and John's emails to foster communication.",
        actions=[
            # Create a new employee account
            Action(name="EditEmployeesDb", kwargs={"name": "John Doe", "role": "Chief Cheerleader", "hire_date": "2025-07-20"}),
            # Get a list of inventory items that need to be restocked
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"status": ["low_stock"]}, "info_items": ["id"]}),
            # Update the last stock count for these items
            Action(name="EditInventoryDb", kwargs={"id": "INV-0009", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:09:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0022", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:09:00Z"}),
            # Get the employee email address
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Megan Young"}, "info_items": ["email"]}),
            # Get John's email address
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "John Doe"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"},{"email": "john.doe@retailpos.com"}]
    ),
    # Task 27: Inventory Management and Customer Notification
    Task(
        annotator="0",
        user_id="task_0027",
        instruction="Perform as Amanda Romano at 2025-07-20T17:10:00Z. Check STORE-002 items below 20, add 25 to each identified unit and update their status to 'in_stock.' Collect emails of purchasers who acquired these items for stock notifications.",
        actions=[
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["id", "sku", "quantity"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0013", "quantity": 28, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0019", "quantity": 40, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0022", "quantity": 31, "status": "in_stock", "current_time": "2025-07-20T17:10:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["ELEC-GAMLP15","SMRT-THERM02","CLTH-WINJKT01"]}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5005","CUST-5011"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ava.martinez@example.com"},{"email": "mia.kim@example.com"}]
    ),
    # Task 28: Product Analysis and Promotion Creation
    Task(
        annotator="0",
        user_id="task_0028",
        instruction="In your position as Robert Zhang at 2025-07-20T17:11:00Z, scan 'Sports & Outdoors' for products exceeding $50. Construct the 'Sports Premium Sale' with 25% off for the next 3 weeks. Elevate select customer statuses and switch your job title to 'Head of Promotions.'",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku", "name", "price"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Sports Premium Sale", "type": "percentage", "discount_value": 25, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20", "end_date": "2025-08-10"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": "platinum"}, "info_items": ["name", "email", "phone_number"]}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1008", "role": "Head of Promotions"}),
        ],
        outputs=[{"name": "Liam Anderson","email": "liam.anderson@example.com","phone_number": "+1-555-0987-654"}]
    ),
    # Task 29: Employee Performance Tracking
    Task(
        annotator="0",
        user_id="task_0029",
        instruction="Assume Henry Adams’ role at 2025-07-20T17:12:00Z. Facilitate a transaction for CUST-5004 to purchase SKU CLTH-SLFJEAN34 using credit_card at STORE-002, managed by EMP-1032. Meteor the employee with the most transactions to 'Senior Sales Associate', recording their email for congratulations.",
        actions=[
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5004", "employee_id": "EMP-1032", "items": {"CLTH-SLFJEAN34": 1}, "store_id": "STORE-002", "current_time": "2025-07-20T17:12:00Z", "payment_method": "credit_card"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T17:12:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["employee_id"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"employee_id": "EMP-1032"}, "info_items": ["name", "email"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1032", "role": "Senior Sales Associate"}),
        ],
        outputs=[{"name": "Amelia Lee", "email": "amelia.lee@retailpos.com"}]
    ),
    # Task 30: Customer Birthday Campaign
    Task(
        annotator="0",
        user_id="task_0030",
        instruction="Portray Sarah Anderson at 2025-02-27T17:13:00Z. Verify birthdays today; create '<Customer Name> Birthday Special' at 30% off for a day. Allot 100 bonus points and retrieve emails for greeting. Switch to 'Customer Relations Manager'.",
        actions=[
            Action(name="GetCustomersWithBirthdayToday", kwargs={"current_day": "02-27"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5003"}, "info_items": ["name", "email", "loyalty_points"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Sophia Singh Birthday Special", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-02-27", "end_date": "2025-02-27"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5003", "loyalty_points": 560, "current_time": "2025-02-27T17:13:00Z"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sarah Anderson"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1002", "role": "Customer Relations Manager"}),
        ],
        outputs=[{"name": "Sophia Singh", "email": "sophia.singh@example.com"}]
    ),
    # Task 31: Inventory Audit and Low Stock Alert
    Task(
        annotator="0",
        user_id="task_0031",
        instruction="Be Zoe Martinez at 2025-07-20T17:14:00Z. Set INV-0023’s reorder level to 60. Check STORE-003 for sub-level inventory, designating any inadequacies 'low_stock', adding 60 units. Activate 'Low Stock Clearance' at 20% off for a week.",
        actions=[
            Action(name="EditInventoryDb", kwargs={"id": "INV-0023", "reorder_level": 60, "current_time": "2025-07-20T17:14:00Z"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["id", "sku", "quantity", "reorder_level"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0023", "quantity": 100, "status": "low_stock", "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:14:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Low Stock Clearance", "type": "percentage", "discount_value": 20, "applicable_skus": ["KITCH-FRYPAN10"], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003", "role": "Inventory Specialist"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 32: Product Return and Quality Control
    Task(
        annotator="0",
        user_id="task_0032",
        instruction="Act as Michael Rodriguez at 2025-07-20T17:15:00Z. Liam Anderson's returned defective TrailGuard Mountain Bike Helmet prompts a refund and a status change to 'quality_issue.' Establish 'Helmet Safety Check' offering 15% off Sports & Outdoors for a fortnight and ensure you have Noah’s email.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Noah Johnson"}, "info_items": ["customer_id", "email"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5004", "sku": "SPORT-BIKHLM01"}, "info_items": ["transaction_id"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Daniel Perez"}, "info_items": ["employee_id"]}),
            Action(name="CreateRefundTransaction", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 1, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0004", "current_time": "2025-07-20T17:15:00Z"}),
            Action(name="EditProductsDb", kwargs={"sku": "SPORT-BIKHLM01", "status": "quality_issue", "current_time": "2025-07-20T17:15:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Helmet Safety Check", "type": "percentage", "discount_value": 15, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20", "end_date": "2025-08-03"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}]
    ),
    # Task 33: Loyalty Program Enhancement
    Task(
        annotator="0",
        user_id="task_0033",
        instruction="Assume the Oliver Diaz identity at 2025-07-20T17:16:00Z. Locate top 2 customers by loyalty points, upgrading to 'platinum' when needed. Add 500 points each and dispatch emails with 'Platinum Elite Benefits' details at 35% off electronics for a month.",
        actions=[
            Action(name="GetTopNCustomersByLoyaltyPoints", kwargs={"n": 2}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["membership_level", "loyalty_points", "email"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004", "membership_level": "platinum", "loyalty_points": 2020, "current_time": "2025-07-20T17:16:00Z"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5001"}, "info_items": ["membership_level", "loyalty_points", "email"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "membership_level": "platinum", "loyalty_points": 1740, "current_time": "2025-07-20T17:16:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Platinum Elite Benefits", "type": "percentage", "discount_value": 35, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20", "end_date": "2025-08-20"}),
        ],
        outputs=[{"email": "noah.johnson@example.com"}, {"email": "ava.thompson@example.com"}]
    ),
    # Task 34: Supplier Quality Assessment
    Task(
        annotator="0",
        user_id="task_0034",
        instruction="Under Amelia Lee’s moniker at 2025-07-20T17:17:00Z, pinpoint SUP-1001-sourced products priced over $100. Launch 'Supplier Quality Clearance' with a 40% markdown and set clearance status. Amend your role to 'Supplier Relations Manager.'",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"supplier_id": "SUP-1001"}, "info_items": ["sku", "name", "cost"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Supplier Quality Clearance", "type": "percentage", "discount_value": 40, "applicable_skus": ["ELEC-4KTV55"], "start_date": "2025-07-20"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "ELEC-4KTV55"}, "info_items": ["id"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0001", "status": "clearance", "current_time": "2025-07-20T17:17:00Z"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1032", "role": "Supplier Relations Manager"}),
        ],
        outputs=[]
    ),
    # Task 35: Customer Engagement Campaign
    Task(
        annotator="0",
        user_id="task_0035",
        instruction="Play Jack Robinson at 2025-07-20T17:18:00Z. Identify gold members opting out from marketing but making purchases, and inaugurate 'We Miss You' at 25% off past purchases. Enlist emails, adjust marketing, and set your position to 'Customer Engagement Specialist.'",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"opt_in_marketing": False, "membership_level": "gold"}, "info_items": ["customer_id", "email"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5010"}, "info_items": ["line_items"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "We Miss You", "type": "percentage", "discount_value": 25, "applicable_skus": ["AUDIO-BTSPKR02", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True, "current_time": "2025-07-20T17:18:00Z"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1034", "role": "Customer Engagement Specialist"}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    # Task 36: Seasonal Inventory Preparation
    Task(
        annotator="0",
        user_id="task_0036",
        instruction="You are Megan Young, and the timestamp is 2025-07-20T17:19:00Z. Ready for back-to-school by reviewing 'Office Supplies' inventory. Any below 30 units invite a 50-unit order. Announce 'Back to School Ready' at 20% off for 6 weeks.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku", "name"]}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "store_id", "quantity"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0014", "quantity": 60, "current_time": "2025-07-20T17:19:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Back to School Ready", "type": "percentage", "discount_value": 20, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20", "end_date": "2025-08-31"}),
        ],
        outputs=[]
    ),
    # Task 37: Employee Training and Development
    Task(
        annotator="0",
        user_id="task_0037",
        instruction="Perform as Natalie Cooper at 2025-07-20T17:20:00Z. Add 'Sarah Williams' as 'Training Coordinator' for STORE-001, effective immediately. Open 'Staff Training Special' at 50% off for employee announcements.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Sarah Williams", "role": "Training Coordinator", "store_id": "STORE-001", "hire_date": "2025-07-20"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Staff Training Special", "type": "percentage", "discount_value": 50, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "grace.miller@retailpos.com"}, {"email": "daniel.perez@retailpos.com"}, {"email": "natalie.cooper@retailpos.com"}, {"email": "sarah.williams@retailpos.com"}]
    ),
    # Task 38: Product Bundle Creation
    Task(
        annotator="0",
        user_id="task_0038",
        instruction="Role-playing Marcus Chen at 2025-07-20T17:21:00Z, construct 'Kitchen Essentials Bundle' offering 30% off when pairing BrewMaster coffee maker with ProSlice knife. Identify their prior buyers to inform of this offer.",
        actions=[
            # get the SKUs for the products
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": ["BrewMaster 12-Cup Coffee Maker", "ProSlice 8\" Chef Knife"]}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Kitchen Essentials Bundle", "type": "bundle", "discount_value": 30, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8"], "start_date": "2025-07-20"}),
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["email"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "noah.tran@example.com"}, {"email": "mia.kim@example.com"}]
    ),
    # Task 39: Quality Control and Customer Satisfaction
    Task(
        annotator="0",
        user_id="task_0039",
        instruction="Being Sarah Anderson at 2025-07-20T17:22:00Z involves handling Charlotte Dubois' return of the defective towel. Process a refund, update Store-001 inventory, announce 'Quality Guarantee' offering a 90-day free return on Home & Kitchen products.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id", "email"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "UltraSoft Cotton Bath Towel"}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5009", "sku": "HOME-BTHTWL01"}, "info_items": ["transaction_id"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sarah Anderson"}, "info_items": ["employee_id"]}),
            Action(name="CreateRefundTransaction", kwargs={"sku": "HOME-BTHTWL01", "quantity": 1, "employee_id": "EMP-1002", "original_transaction_id": "TXN-0009", "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-001", "quantity_change": 1, "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="EditProductsDb", kwargs={"sku": "HOME-BTHTWL01", "status": "quality_review", "current_time": "2025-07-20T17:22:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Home & Kitchen"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Quality Guarantee", "type": "Quality Assurance", "discount_value": 0, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10", "HOME-BTHTWL01", "HOME-DESKLMP01"], "start_date": "2025-07-20", "end_date": "2025-10-20"}),
        ],
        outputs=[{"email": "charlotte.dubois@example.com"}]
    ),
    # Task 40: Store Performance Analysis
    Task(
        annotator="0",
        user_id="task_0040",
        instruction="Embody Henry Adams at 2025-07-20T17:23:00Z, examine STORE-003 sales. If realizing under $5000, create a critical 'Store Boost Mega Sale' at 45% off for a week. Collate employee emails for urging mobilization.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["total_amount"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Store Boost Mega Sale", "type": "percentage", "discount_value": 45, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "henry.adams@retailpos.com"}, {"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 41: Customer Retention Program
    Task(
        annotator="0",
        user_id="task_0041",
        instruction="Amanda Romano operates at 2025-07-20T17:24:00Z. Examine loyalty members above 1000 points lacking a 30-day purchase history. Launch 'Come Back Special' at 30% for return appeal and reward loyalty status with 'valued_customer'.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {}, "info_items": ["customer_id","loyalty_points", "email"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004", "CUST-5010"]}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5001": "2025-06-05", "CUST-5004": "2025-06-05", "CUST-5010": "2025-06-05"}, "filter_end_date": "2025-06-20"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Come Back Special", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5010", "status": "valued_customer", "current_time": "2025-07-20T17:24:00Z"}),
        ],
        outputs=[{"email": "emma.wilson@example.com"}, {"email": "liam.anderson@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 42: Emergency Stock Transfer
    Task(
        annotator="0",
        user_id="task_0042",
        instruction="Oliver Diaz manages STORE-005 inventory at 2025-07-20T17:25:00Z. Create PowerPlus AA Batteries with zero stock. Identify and transfer units from surplus holding stores. Initiate 'Battery Emergency Sale' at 10% off for quick clearance.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}, "info_items": ["sku"]}),
            Action(name="EditInventoryDb", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-005", "quantity": 0, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "ELEC-RCHAA04"}, "info_items": ["store_id", "quantity"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -20, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-005", "quantity_change": 20, "current_time": "2025-07-20T17:25:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Battery Emergency Sale", "type": "percentage", "discount_value": 10, "applicable_skus": ["ELEC-RCHAA04"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 43: Customer Service Excellence
    Task(
        annotator="0",
        user_id="task_0043",
        instruction="In the guise of Amelia Lee at 2025-07-20T17:26:00Z, manage Liam Anderson's exchange of his Yoga Mat for a Helmet. Align inventories, boost his membership to platinum, append 200 points, secure his email for VIP affirmation.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Liam Anderson"}, "info_items": ["customer_id", "email", "loyalty_points", "membership_level"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "FlexFit Premium Yoga Mat"}, "info_items": ["sku"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5004", "sku": "SPORT-YOGMAT01"}, "info_items": ["transaction_id"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            Action(name="CreateRefundTransaction", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 1, "employee_id": "EMP-1032", "original_transaction_id": "TXN-0004", "current_time": "2025-07-20T17:26:00Z"}),
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5004", "employee_id": "EMP-1032", "items": {"SPORT-BIKHLM01": 1}, "store_id": "STORE-004", "payment_method": "credit_card", "current_time": "2025-07-20T17:26:00Z"}),
            # update inventory of yoga mat in store-001
            Action(name="UpdateInventoryItem", kwargs={"sku":"SPORT-YOGMAT01", "store_id":"STORE-001", "quantity_change": 1, "current_time": "2025-07-20T17:26:00Z"}),
            # update inventory of helmet in store-004
            Action(name="UpdateInventoryItem", kwargs={"sku":"SPORT-BIKHLM01", "store_id":"STORE-004", "quantity_change": -1, "current_time": "2025-07-20T17:26:00Z"}),
            # upgrade membership and add loyalty points
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004", "membership_level": "platinum", "loyalty_points": 1720, "current_time": "2025-07-20T17:26:00Z"}),
        ],
        outputs=[{"email": "liam.anderson@example.com"}]
    ),
    # Task 44: Technology Upgrade Campaign
    Task(
        annotator="0",
        user_id="task_0044",
        instruction="Act as Jack Robinson at 2025-07-20T17:27:00Z. Allocations from a disabled truck prompt redistributing 75 GigaPlay laptops. Find applicable stocking stores, initiate 'Laptop Distribution Special' at 15% off for 10 days.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "GigaPlay 15\" Gaming Laptop"}, "info_items": ["sku"]}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "ELEC-GAMLP15"}, "info_items": ["store_id", "quantity"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002", "quantity_change": 75, "current_time": "2025-07-20T17:27:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Laptop Distribution Special", "type": "percentage", "discount_value": 15, "applicable_skus": ["ELEC-GAMLP15"], "start_date": "2025-07-20", "end_date": "2025-07-30"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"role": "Store Manager"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"}]
    ),
    # Task 45: Sustainability Initiative
    Task(
        annotator="0",
        user_id="task_0045",
        instruction="As Megan Young, it is 2025-07-20T17:28:00Z. Fostering sustainability, introduce the 'Bamboo Water Bottle' priced at $15.99 with 100 STORE-005 units. Start 'Green Living' at 20% off 'EcoSmart' products. Collect eco-buyer emails for awareness.",
        actions=[
            Action(name="EditProductsDb", kwargs={"name": "Bamboo Water Bottle", "price": 15.99, "brand": "EcoSmart", "current_time": "2025-07-20T17:28:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"brand": "EcoSmart"}, "info_items": ["name", "sku"]}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021", "store_id": "STORE-005", "quantity": 100, "current_time": "2025-07-20T17:28:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Green Living", "type": "percentage", "discount_value": 20, "applicable_skus": ["SKU-1021", "SMRT-THERM02"], "start_date": "2025-07-20"}),
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "SMRT-THERM02"}),
            Action(name="GetCustomerPurchaseCountsBySku", kwargs={"sku": "SKU-1021"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "mia.kim@example.com"}]
    ),
    # Task 46: Holiday Preparation Campaign
    Task(
        annotator="0",
        user_id="task_0046",
        instruction="Jennifer Williams, it's 2025-07-20T17:29:00Z. Anticipate holiday needs with 'Early Bird Holiday Sale' at 30% off. Check STORE-001 top-priced products, refreshing low stock. Mobilize members for early sales.",
        actions=[
            Action(name="EditPromotionsDb", kwargs={"name": "Early Bird Holiday Sale", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="GetTopNMostExpensiveProductsByStore", kwargs={"store_id": "STORE-001", "n": 3}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": ["ELEC-4KTV55", "HOM-COFMKR12", "HOME-DESKLMP01"], "store_id": "STORE-001"}, "info_items": ["sku", "quantity"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": 10, "current_time": "2025-07-20T17:29:00Z"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": ["gold","platinum"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "emma.wilson@example.com"},{"email": "ben.cohen@example.com"}, {"email": "liam.anderson@example.com"}]
    ),
    # Task 47: Supplier Relationship Management
    Task(
        annotator="0",
        user_id="task_0047",
        instruction="As Amanda Romano at 2025-07-20T17:30:00Z, filter SUP-1002 products above $36. Structure 'Kitchen Partner Discount' at 15% off, and seek emails from prior year buyers.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"supplier_id": "SUP-1002"}, "info_items": ["sku", "name", "price"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Kitchen Partner Discount", "type": "percentage", "discount_value": 15, "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8"], "start_date": "2025-07-20"}),
            # Get the dates of the purchases
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["HOM-COFMKR12", "KITCH-CHEFKNF8"]}, "info_items": ["customer_id", "timestamp", "line_items"]}),
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5002": "2025-06-05", "CUST-5011": "2025-06-06"}, "filter_start_date": "2024-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5002"}, "info_items": ["email"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "noah.tran@example.com"}, {"email": "mia.kim@example.com"}]
    ),
    # Task 48: Store Transfer and Optimization
    Task(
        annotator="0",
        user_id="task_0048",
        instruction="Robert Zhang, the scenario evolves at 2025-07-20T17:31:00Z. Surplus helmets relocate from STORE-005 to STORE-004, shaping a 'Sports Transfer Deal' at 20% off lasting 3 days.",
        actions=[
            # Get helmet SKU
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "TrailGuard Mountain Bike Helmet"}, "info_items": ["sku"]}),
            Action(name="EditInventoryDb", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-005", "quantity": 20, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "SPORT-BIKHLM01","store_id": "STORE-005", "quantity_change": -15, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "SPORT-BIKHLM01","store_id": "STORE-004", "quantity_change": 15, "current_time": "2025-07-20T17:31:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Sports Transfer Deal", "type": "percentage", "discount_value": 20, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20", "end_date": "2025-07-23"}),
        ],
        outputs=[]
    ),
    # Task 49: New Employee Onboarding and Training
    Task(
        annotator="0",
        user_id="task_0049",
        instruction="You are Sarah Anderson, current timestamp 2025-07-20T17:32:00Z. Induct 'David Wilson' as a 'Sales Associate' at STORE-002. Craft a customer entry and provision a 'Employee Welcome Discount' for one purchase at 40% off, good for a month.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "David Wilson", "role": "Sales Associate", "store_id": "STORE-002", "hire_date": "2025-07-20"}),
            Action(name="EditCustomersDb", kwargs={"name": "David Wilson", "email": "david.wilson@retailpos.com", "current_time": "2025-07-20T17:32:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Employee Welcome Discount", "type": "percentage", "discount_value": 40, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-08-19"}),
        ],
        outputs=[{"email": "david.wilson@retailpos.com"}]
    ),
    # Task 50: Customer Loyalty Tier Adjustment
    Task(
        annotator="0",
        user_id="task_0050",
        instruction="Implement Henry Adams’ instructions at 2025-07-20T17:33:00Z, elevating customers surmounting 800 loyalty points to gold from silver. Allocate 200 bonus points to upgrades and send congratulatory emails.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level":"silver"}, "info_items": ["customer_id", "loyalty_points", "membership_level", "email"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1075, "current_time": "2025-07-20T17:33:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5006", "loyalty_points": 1180, "membership_level": "gold", "current_time": "2025-07-20T17:33:00Z"}),
        ],
        outputs=[{"email":"noah.tran@example.com"}, {"email": "william.zhang@example.com"}]
    ),
    # Task 51: Expired Product Management
    Task(
        annotator="0",
        user_id="task_0051",
        instruction="In the capacity of Zoe Martinez at 2025-07-20T17:34:00Z, scrutinize grocery expiries. Organic Almond Butter nearing 2026 expiration calls for 'Fresh & Natural Sale' at 30% off, transitioning inventory to 'clearance'.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Grocery"}, "info_items": ["sku", "name", "expiry_date"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Fresh & Natural Sale", "type": "percentage", "discount_value": 30, "applicable_skus": ["GROC-ALMBTR500"], "start_date": "2025-07-20"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "GROC-ALMBTR500"}, "info_items": ["id"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0007", "status": "clearance", "current_time": "2025-07-20T17:34:00Z"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Zoe Martinez"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1015", "role": "Head Grocer"}),
        ],
        outputs=[]
    ),
    # Task 52: High-Value Customer Reward Program
    Task(
        annotator="0",
        user_id="task_0052",
        instruction="As Amelia Lee, it's 2025-07-20T17:35:00Z. Conduct a review identifying customers spending over $1000. Organize 'VIP Spender Rewards' at 25% off electronics coupled with 200 bonus points, notifying winners via email.",
        actions=[
            Action(name="GetCustomersAboveXSpend", kwargs={"amount": 1000}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "VIP Spender Rewards", "type": "percentage", "discount_value": 25, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5005"}, "info_items": ["email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5005", "loyalty_points": 495, "current_time": "2025-07-20T17:35:00Z"}),
        ],
        outputs=[{"email": "ava.martinez@example.com"}]
    ),
    # Task 53: Seasonal Clothing Clearance
    Task(
        annotator="0",
        user_id="task_0053",
        instruction="Operated by Oliver Diaz at 2025-07-20T17:36:00Z, as summer ends initiate 'Summer Clearance Blowout' at 45% off apparel. Assess the Men's Slim Fit Jeans 34W 32L inventory, tweaking discount to 55% if exceeding 25 units.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Apparel"}, "info_items": ["sku", "name"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Summer Clearance Blowout", "type": "percentage", "discount_value": 45, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"], "start_date": "2025-07-20"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}, "info_items": ["quantity"]}),
            Action(name="EditProductsDb", kwargs={"sku": "CLTH-SLFJEAN34", "discount_rate": 0.55, "current_time": "2025-07-20T17:36:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["CLTH-SLFJEAN34","CLTH-WINJKT01"]}, "info_items": ["customer_id"]})
        ],
        outputs=[{"email": "noah.tran@example.com"}]
    ),
    # Task 54: Smart Home Technology Push
    Task(
        annotator="0",
        user_id="task_0054",
        instruction="As Jack Robinson, it's 2025-07-20T17:37:00Z, create a 'Smart Living Revolution' stretching 18% off 'Smart Home' products. Target electronics customers, gathering emails for smart tech promotions.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Smart Home"}, "info_items": ["sku", "name"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Smart Living Revolution", "type": "percentage", "discount_value": 18, "applicable_skus": ["SMRT-THERM02"], "start_date": "2025-07-20", "end_date": "2025-09-20"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["ELEC-4KTV55","AUDIO-BTSPKR02","ELEC-GAMLP15","AUDIO-NCEBUDS01","ELEC-RCHAA04"]}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001","CUST-5005", "CUST-5010"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "emma.wilson@example.com"}, {"email": "ava.martinez@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 55: Book Club Customer Engagement
    Task(
        annotator="0",
        user_id="task_0055",
        instruction="Jennifer Williams at 2025-07-20T17:38:00Z. Build a book club by instating 'Reading Circle Special' at 20% off all books. Integrate 'Literary Club Admin' and rally book buyers for membership.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Books"}, "info_items": ["sku", "name"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Reading Circle Special", "type": "percentage", "discount_value": 20, "applicable_skus": ["BOOK-KDSSTY01"], "start_date": "2025-07-20"}),
            Action(name="EditCustomersDb", kwargs={"name": "Literary Club Admin", "email": "bookclub@retailpos.com", "current_time": "2025-07-20T17:38:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": "BOOK-KDSSTY01"}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5008"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "bookclub@retailpos.com"}, {"email": "james.oconnor@example.com"}]
    ),
    # Task 56: Damaged Goods Management
    Task(
        annotator="0",
        user_id="task_0056",
        instruction="Acting as Michael Rodriguez at 2025-07-20T17:39:00Z, address Benjamin Cohen's defective WaveSound Speaker. Facilitate a refund, set 'quality_issue' status, and roll out 'Sound Quality Guarantee' at 15% off Electronics.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Benjamin Cohen"}, "info_items": ["customer_id", "email"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "WaveSound All-Weather Bluetooth Speaker"}, "info_items": ["sku"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Michael Rodriguez"}, "info_items": ["employee_id"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}, "info_items": ["transaction_id"]}),
            Action(name="CreateRefundTransaction", kwargs={"sku": "AUDIO-BTSPKR02", "quantity": 1, "employee_id": "EMP-1003", "original_transaction_id": "TXN-0010", "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005", "quantity_change": 1, "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="EditProductsDb", kwargs={"sku": "AUDIO-BTSPKR02", "status": "quality_issue", "current_time": "2025-07-20T17:39:00Z"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Sound Quality Guarantee", "type": "percentage", "discount_value": 15, "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
        ],
        outputs=[{"email": "ben.cohen@example.com"}]
    ),
    # Task 57: Store Manager Performance Review
    Task(
        annotator="0",
        user_id="task_0057",
        instruction="Play Megan Young at 2025-07-20T17:40:00Z, promote Ethan Walker to 'Senior Cashier.' Establish his customer account with 50 extra loyalty points, and provide 'Team Excellence Discount' at 35% off for a week, forwarding notifications.",
        actions=[
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Ethan Walker"}, "info_items": ["employee_id", "email"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1011", "role": "Senior Cashier"}),
            Action(name="EditCustomersDb", kwargs={"name": "Ethan Walker", "email": "ethan.walker@retailpos.com", "loyalty_points": 50, "current_time": "2025-07-20T17:40:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Team Excellence Discount", "type": "percentage", "discount_value": 35, "applicable_skus": [], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"store_id": "STORE-002"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "ethan.walker@retailpos.com"}, {"email": "robert.zhang@retailpos.com"}, {"email": "amanda.romano@retailpos.com"}]
    ),
    # Task 58: Inventory Audit and Restock
    Task(
        annotator="0",
        user_id="task_0058",
        instruction="Amanda Romano manages at 2025-07-20T17:41:00Z, with a STORE-002 inventory audit. Enhance 'critical' stock by 50 units, refresh 'last_stock_count', and announce 'Inventory Fresh Stock' at 10% off replenishments.",
        actions=[
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-002", "status": "critical"}, "info_items": ["id", "sku", "quantity"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0013", "quantity": 53, "last_stock_count": "2025-07-20", "current_time": "2025-07-20T17:41:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Inventory Fresh Stock", "type": "percentage", "discount_value": 10, "applicable_skus": ["ELEC-GAMLP15"], "start_date": "2025-07-20"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amanda Romano"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1009", "role": "Stock Manager"}),
        ],
        outputs=[]
    ),
    # Task 59: Customer Address Update Service
    Task(
        annotator="0",
        user_id="task_0059",
        instruction="As Sarah Anderson, the task at 2025-07-20T17:42:00Z involves updating Charlotte Dubois' new address. Award 75 loyalty points, verify with email, and log her QuietTone wireless earbuds purchase via credit_card at STORE-002.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Charlotte Dubois"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5009", "address": "456 Royal Street, New Orleans, LA, 70130", "loyalty_points": 750, "current_time": "2025-07-20T17:42:00Z"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sarah Anderson"}, "info_items": ["employee_id"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "QuietTone Wireless Earbuds"}, "info_items": ["sku"]}),
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5009", "employee_id": "EMP-1002", "items": {"AUDIO-NCEBUDS01": 1}, "store_id": "STORE-002", "payment_method": "credit_card", "current_time": "2025-07-20T17:42:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T17:42:00Z"}),
        ],
        outputs=[{"email": "charlotte.dubois@example.com"}]
    ),
    # Task 60: Flash Sale Weekend Event
    Task(
        annotator="0",
        user_id="task_0060",
        instruction="Robert Zhang conducts at 2025-07-20T17:43:00Z a weekend exclusive, 'Saturday Surprise Special' shaving 50% off office supplies for one day. Pinpoint prior buyers for early notifications and alter your designation to 'Weekend Sales Manager'.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku", "name"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Saturday Surprise Special", "type": "percentage", "discount_value": 50, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-26", "end_date": "2025-07-26"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email"]}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1008", "role": "Weekend Sales Manager"}),
        ],
        outputs=[{"email": "william.zhang@example.com"}]
    ),
    # Task 61: Membership Program Overhaul
    Task(
        annotator="0",
        user_id="task_0061",
        instruction="Position as Henry Adams. Around 2025-07-20T17:44:00Z, escalate Liam Anderson to 'Diamond' membership, bestow 300 bonus points, initiate 'Diamond Elite Access' at 40% off. Record your new post as 'Membership Program Director.'",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Liam Anderson"}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004", "membership_level": "diamond", "loyalty_points": 1820, "current_time": "2025-07-20T17:44:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Diamond Elite Access", "type": "percentage", "discount_value": 40, "applicable_skus": [], "start_date": "2025-07-20"}),
            # get employee_id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1020", "role": "Membership Program Director"}),
        ],
        outputs=[{"email": "liam.anderson@example.com"}]
    ),
    # Task 62: Product Bundle Innovation
    Task(
        annotator="0",
        user_id="task_0062",
        instruction="Portray Amelia Lee at 2025-07-20T17:45:00Z. Design a 'Home Office Complete' bundle deal granting a 35% markdown on ErgoPro Chairs and LumiLux Lamps purchased together. Inform prior buyers and transfer your role to 'Product Innovation Manager.'",
        actions=[
            # Get skus
            Action(name="GetProductsInfoByParam", kwargs={"filter_params":{"name":["ErgoPro Adjustable Office Chair","LumiLux LED Desk Lamp"]}, "info_items":["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Home Office Complete", "type": "bundle", "discount_value": 35, "applicable_skus": ["OFFC-ERGCHR01", "HOME-DESKLMP01"], "start_date": "2025-07-20"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["OFFC-ERGCHR01","HOME-DESKLMP01"]}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5006"}, "info_items": ["email"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            # Change role
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1032", "role": "Product Innovation Manager"}),
        ],
        outputs=[{"email": "william.zhang@example.com"}]
    ),
    # Task 63: Return Customer Win-Back
    Task(
        annotator="0",
        user_id="task_0063",
        instruction="Act as Oliver Diaz. On 2025-07-20T17:46:00Z for STORE-001 June 6th, 2025 buyers, bring forth 'We Want You Back' with 30% off future buys, adjusting their status to 'win_back_target.' Consolidate customer emails for re-engagement.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"store_id": "STORE-001"}, "info_items": ["customer_id", "timestamp"]}),
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5001": "2025-06-05", "CUST-5008": "2025-06-05", "CUST-5012": "2025-06-06"}, "filter_start_date": "2025-06-06", "filter_end_date": "2025-06-06"}),
            Action(name="EditPromotionsDb", kwargs={"name": "We Want You Back", "type": "percentage", "discount_value": 30, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5012", "status": "win_back_target", "current_time": "2025-07-20T17:46:00Z"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 64: Cross-Store Inventory Balancing
    Task(
        annotator="0",
        user_id="task_0064",
        instruction="Embody Zoe Martinez at 2025-07-20T17:47:00Z. Establish a stock of 3 ErgoPro Chairs for STORE-001. Execute a stock transfer of 5 units from top to low inventory stores, then offer 'Store Balance Special' at 12% off.",
        actions=[
            Action(name="EditInventoryDb", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity": 3, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "store_id", "quantity"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": -5, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity_change": 5, "current_time": "2025-07-20T17:47:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Store Balance Special", "type": "percentage", "discount_value": 12, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 65: Employee Recognition Program
    Task(
        annotator="0",
        user_id="task_0065",
        instruction="As Jennifer Williams, the goal on 2025-07-20T17:48:00Z is to recognize high achievers by isolating the largest transaction handler. Velocitate their promotion to 'Employee of the Month,' issue 500 points as customers, and unveil 'Staff Appreciation Sale' at 45% off.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["employee_id", "total_amount"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"employee_id": "EMP-1045"}, "info_items": ["name", "email"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1045", "status": "employee_of_month"}),
            Action(name="EditCustomersDb", kwargs={"name": "Megan Young", "email": "megan.young@retailpos.com", "membership_level": "employee", "loyalty_points": 500, "current_time": "2025-07-20T17:48:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Staff Appreciation Sale", "type": "percentage", "discount_value": 45, "applicable_skus": [], "start_date": "2025-07-20"}),
        ],
        outputs=[{"email": "megan.young@retailpos.com"}]
    ),
    # Task 66: Product Category Performance Analysis
    Task(
        annotator="0",
        user_id="task_0066",
        instruction="As Jack Robinson by 2025-07-20T17:49:00Z, orchestrate an 'Electronics Mega Sale' offering a 28% markdown. Reward past electronics buyers with 150 extra points. Dispatch targeted marketing emails.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Electronics"}, "info_items": ["sku", "name"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Electronics Mega Sale", "type": "percentage", "discount_value": 28, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["ELEC-4KTV55", "ELEC-GAMLP15", "AUDIO-BTSPKR02", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5005", "CUST-5010"]}, "info_items": ["email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "loyalty_points": 1390, "current_time": "2025-07-20T17:49:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5005", "loyalty_points": 445, "current_time": "2025-07-20T17:49:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5010", "loyalty_points": 1175, "current_time": "2025-07-20T17:49:00Z"}),
        ],
        outputs=[{"email": "emma.wilson@example.com"}, {"email": "ava.martinez@example.com"}, {"email": "ben.cohen@example.com"}]
    ),
    # Task 67: Customer Birthday Promotions Launch
    Task(
        annotator="0",
        user_id="task_0067",
        instruction="Acting as Jennifer Williams at 2025-01-19T18:00:00Z, acknowledge Customer Appreciation Month with 'Birthday Bash Bonanza', a 30%-off day for today’s born. Collect phone numbers for congratulatory calls and elevate bronze birthcustomers to a higher membership level.",
        actions=[
            Action(name="GetCustomersWithBirthdayToday", kwargs={"current_day": "01-19"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Birthday Bash Bonanza", "type": "percentage", "discount_value": 30.0, "applicable_skus": [], "start_date": "2025-01-19"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["membership_level", "phone_number"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5012", "membership_level": "bronze", "current_time": "2025-01-19T18:00:00Z"}),
        ],
        outputs=[]
    ),
    # Task 68: Emergency Inventory Restock Protocol
    Task(
        annotator="0",
        user_id="task_0068",
        instruction="As Zoe Martinez at 2025-07-20T18:01:00Z, triple reorder levels for STORE-004 items after witnessing unparalleled demand. Elevate below-threshold inventory states, escalating them to 'critical', then procure Store Managers’ numbers.",
        actions=[
            # get inventory items from store-004
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "quantity", "reorder_level"]}),
            # update reorder level
            Action(name="EditInventoryDb", kwargs={"id": "INV-0009", "reorder_level": 18,"status": "critical", "quantity": 14,"current_time": "2025-07-20T18:01:00Z"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"role": "Store Manager"}, "info_items": ["phone_number"]})
        ],
        outputs=[]
    ),
    # Task 69: New Product Launch Campaign
    Task(
        annotator="0",
        user_id="task_0069",
        instruction="You are Robert Zhang, and as of 2025-07-20T18:02:00Z, introduce 'TechWave Wireless Earbuds Pro' retailing at $199.99. Initiate 25 units across STORE-001 to STORE-005, launching 'Wireless Freedom Week' at 15% off for a week. Use platinum and gold members’ phone numbers for alerts.",
        actions=[
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id"]}),
            Action(name="EditProductsDb", kwargs={"name": "TechWave Wireless Earbuds Pro", "price": 199.99, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021","store_id": "STORE-001", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021","store_id": "STORE-002", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021","store_id": "STORE-003", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021","store_id": "STORE-004", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021","store_id": "STORE-005", "quantity": 25, "current_time": "2025-07-20T18:02:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Wireless Freedom Week", "type": "percentage", "discount_value": 15.0, "applicable_skus": ["SKU-1021"], "start_date": "2025-07-20", "end_date": "2025-07-27"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": ["platinum", "gold"]}, "info_items": ["phone_number"]})
        ],
        outputs=[{"phone_number": "+1-555-0123-456"}, {"phone_number": "+1-555-0999-888"}, {"phone_number": "+1-555-0987-654"}]
    ),
    # Task 70: Customer Loyalty Tier Analysis
    Task(
        annotator="0",
        user_id="task_0070",
        instruction="As Amanda Romano, the venture on 2025-07-20T18:03:00Z involves spotlighting top 2 loyalists for individualized product discounts beneath 'VIP Elite Circle' at 45%. Ascertain they meet a loyalty parity of under 500 point difference, conferring them platinum status.",
        actions=[
            Action(name="GetTopNCustomersByLoyaltyPoints", kwargs={"n": 2}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004"]}, "info_items": ["line_items"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "VIP Elite Circle", "type": "percentage", "discount_value": 45.0, "start_date": "2025-07-20", "applicable_skus": ["ELEC-4KTV55", "ELEC-RCHAA04", "SPORT-BIKHLM01", "SPORT-YOGMAT01"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5004"]}, "info_items": ["customer_id", "loyalty_points", "membership_level"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "membership_level": "platinum", "current_time": "2025-07-20T18:03:00Z"}),
        ],
        outputs=[]
    ),
    # Task 71: Seasonal Product Clearance Strategy
    Task(
        annotator="0",
        user_id="task_0071",
        instruction="You are Oliver Diaz. At 2025-07-20T18:04:00Z, strategize a 'Summer's End Clearance' emphasizing tiered markdowns: 40% on 'Sports & Outdoors' followed by 35% on 'Apparel items.' Assay Apparel stock, flagging slow movers that exceed twice their safe stock.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Sports & Outdoors"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Summer's End Clearance", "type": "percentage", "discount_value": 40.0, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Apparel"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Summer's End Clearance", "type": "percentage", "discount_value": 35.0, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"], "start_date": "2025-07-20"}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"]}, "info_items": ["id","quantity", "safety_stock"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0005", "status": "slow_moving", "current_time": "2025-07-20T18:04:00Z"}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0022", "status": "slow_moving", "current_time": "2025-07-20T18:04:00Z"}),
        ],
        outputs=[]
    ),
    # Task 72: Employee Performance Recognition Program
    Task(
        annotator="0",
        user_id="task_0072",
        instruction="Megan Young is the acting role at 2025-07-20T18:05:00Z, leading the charge for exceptional workforce recognition via the last cash-based transaction handler. Formulate their customer profile receiving 1000 points, promote them, and extend 'Team Champion Discount' at 25%.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"payment_method": "cash"}, "info_items": ["transaction_id", "timestamp", "employee_id"]}),
            # sort transactions by timestamp to find the most recent one
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"TXN-0002": "2025-06-05T11:42:00Z", "TXN-0007": "2025-06-05T14:22:18Z", "TXN-0008":"2025-06-05T15:03:09Z"}, "sort_order": "newest", "top_n": 1}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"employee_id": "EMP-1004"}, "info_items": ["name", "email"]}),
            Action(name="EditCustomersDb", kwargs={"name": "Jennifer Williams", "email": "jennifer.williams@retailpos.com", "loyalty_points": 1000, "current_time": "2025-07-20T18:05:00Z"}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1004", "role": "Senior Sales Associate"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Team Champion Discount", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 73: Cross-Store Inventory Optimization
    Task(
        annotator="0",
        user_id="task_0073",
        instruction="Operate as Henry Adams at 2025-07-20T18:06:00Z for STORE-003 downsizing demands. Transition half-store inventories to STORE-001, establishing STORE-003's reduced stock numbers. Push 'Freshly Stocked' at 12% off on newfound goods.",
        actions=[
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-003"}, "info_items": ["sku", "quantity"]}),
            Action(name="EditInventoryDb", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-001", "quantity": 5, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-001", "quantity": 40, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-001", "quantity": 45, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "KITCH-FRYPAN10", "store_id": "STORE-001", "quantity": 20, "current_time": "2025-07-20T18:06:00Z"}),

            Action(name="UpdateInventoryItem", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": -5, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "GROC-GRNLBR12", "store_id": "STORE-003", "quantity_change": -40, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -45, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "KITCH-FRYPAN10", "store_id": "STORE-003", "quantity_change": -20, "current_time": "2025-07-20T18:06:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Freshly Stocked", "type": "percentage", "discount_value": 12.0, "applicable_skus": ["OFFC-ERGCHR01", "GROC-GRNLBR12", "ELEC-RCHAA04", "KITCH-FRYPAN10"], "start_date": "2025-07-20"})
        ],
        outputs=[]
    ),
    # Task 74: Customer Retention Emergency Response
    Task(
        annotator="0",
        user_id="task_0074",
        instruction="Adopt the Amelia Lee persona for 2025-07-20T18:07:00Z. Track customers marked with 'returned' transactions, adjust their status as 'at_risk'. Promote comeback via 'Come Back Strong' at 50% off, merge with the complement of personal outreach through email.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"status": "returned"}, "info_items": ["customer_id"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5012", "status": "at_risk", "current_time": "2025-07-20T18:07:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Come Back Strong", "type": "percentage", "discount_value": 50.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Amelia Lee"}, "info_items": ["employee_id"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1032", "role": "Customer Retention Specialist"}),
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 75: Supplier Relations and New Product Integration
    Task(
        annotator="0",
        user_id="task_0075",
        instruction="As Jack Robinson in the timeframe 2025-07-20T18:08:00Z, embrace 'TechForward Inc.' with their 'SmartFit Activity Tracker', valued at $149.99, initiating 50 units at STORE-004. Facilitate a 'Future Fitness' promotional thrust at 20%, securing phone contacts of FlexFit Yoga Mat clientele.",
        actions=[
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id"]}),
            Action(name="EditProductsDb", kwargs={"name": "SmartFit Activity Tracker", "price": 149.99, "brand": "TechForward Inc.", "current_time": "2025-07-20T18:08:00Z"}),
            Action(name="EditInventoryDb", kwargs={"sku": "SKU-1021", "store_id": "STORE-004", "quantity": 50, "current_time": "2025-07-20T18:08:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Future Fitness", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SKU-1021"], "start_date": "2025-07-20"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "FlexFit Premium Yoga Mat"}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["SPORT-YOGMAT01"]}, "info_items": ["customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5004"]}, "info_items": ["phone_number"]})
        ],
        outputs=[{"phone_number": "+1-555-0987-654"}]
    ),
    # Task 76: Premium Customer Concierge Service
    Task(
        annotator="0",
        user_id="task_0076",
        instruction="For Michael Rodriguez, as of 2025-07-20T18:09:00Z, engineer a 'Basics tax free' schema providing a 60% discount on untaxed items. Boost platinum loyalty by 500 points and acquire VIP emails for personalized shopping guidance.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"tax_rate": 0}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Basics tax free", "type": "percentage", "discount_value": 60.0, "applicable_skus": ["GROC-GRNLBR12", "BOOK-KDSSTY01","GROC-SPRWAT6P", "GROC-ALMBTR500"], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": "platinum"}, "info_items": ["customer_id", "name", "email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004","loyalty_points": 2020, "current_time": "2025-07-20T18:09:00Z"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["email"]}),
        ],
        outputs=[{"email": "liam.anderson@example.com"}]
    ),
    # Task 77: Theft Prevention and Security Audit
    Task(
        annotator="0",
        user_id="task_0077",
        instruction="Sarah Anderson opts on 2025-07-20T18:10:00Z for a security-scrutiny expedition. All returned-status transactions now read as 'under_review'. Investigate connected entries for collective review, and disclose customer identity concerning returned dealings.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"status": "returned"}, "info_items": ["transaction_id", "customer_id", "employee_id"]}),
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0012", "status": "under_review", "current_time": "2025-07-20T18:10:00Z"}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"employee_id": "EMP-1002"}, "info_items": ["transaction_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["name"]}),
        ],
        outputs=[{"name": "Logan Smith"}]
    ),
    # Task 78: Holiday Preparation and Staff Scheduling
    Task(
        annotator="0",
        user_id="task_0078",
        instruction="Perform as Ethan Walker at 2025-07-20T18:11:00Z, examining 'Sports & Outdoors' sales (over 20 units) with unsold sets triggering 'Holiday Prep Special' at 25% off. Secure contact details for corresponding product customers.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": ["Sports & Outdoors"]}, "info_items": ["sku"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]}, "info_items": ["line_items", "customer_id"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Holiday Prep Special", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5004", "CUST-5012"]}, "info_items": ["email", "phone_number"]})
        ],
        outputs=[{"email": "liam.anderson@example.com", "phone_number": "+1-555-0987-654"}, {"email": "logan.smith@example.com", "phone_number": "+1-555-0667-899"}]
    ),
    # Task 79: Customer Feedback and Product Improvement
    Task(
        annotator="0",
        user_id="task_0079",
        instruction="Your name being Charlie Brown on 2025-07-20T18:12:00Z, detect returned products assigning them 'quality_review' status. Propel a 'Quality Promise' promotion at 15%, accumulating emails from returning customers to notify of refinements. List yourself as a Quality Assurance Specialist.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"status": "returned"}, "info_items": ["line_items", "customer_id"]}),
            Action(name="EditProductsDb", kwargs={"sku": "SPORT-BIKHLM01", "status": "quality_review", "current_time": "2025-07-20T18:12:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Quality Promise", "type": "percentage", "discount_value": 15.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5012"]}, "info_items": ["email"]}),
            Action(name="EditEmployeesDb", kwargs={"name": "Charlie Brown", "role": "Quality Assurance Specialist"})
        ],
        outputs=[{"email": "logan.smith@example.com"}]
    ),
    # Task 80: Multi-Store Anniversary Celebration
    Task(
        annotator="0",
        user_id="task_0080",
        instruction="Sophia Martinez enters the records as an Event Manager for STORE-001. The date: 2025-07-20T18:13:00Z. Mark the firm’s quinquennial using '5 Years Strong' with tiered deductions on products, plus contacting the oldest customer inviting them to festivities.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Sophia Martinez", "role": "Event Manager", "store_id": "STORE-001"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sophia Martinez"}, "info_items": ["employee_id"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "5 Years Strong - Bronze", "type": "percentage", "discount_value": 5.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="EditPromotionsDb", kwargs={"name": "5 Years Strong - Silver", "type": "percentage", "discount_value": 15.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="EditPromotionsDb", kwargs={"name": "5 Years Strong - Gold", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="EditPromotionsDb", kwargs={"name": "5 Years Strong - Platinum", "type": "percentage", "discount_value": 35.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            # get customers birthdate
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {}, "info_items": ["customer_id", "birthdate"]}),
            # sort customers by birthdate and get the eldest customer
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5001": "1990-07-12", "CUST-5002": "1985-11-05", "CUST-5003": "1997-02-27", "CUST-5004": "1982-09-14", "CUST-5005": "1995-12-03", "CUST-5006": "1988-04-30", "CUST-5007": "1993-06-18", "CUST-5008": "1998-10-09", "CUST-5009": "1986-01-25", "CUST-5010": "1983-03-04", "CUST-5011": "1992-08-11", "CUST-5012": "2000-01-19"}, "sort_order": "oldest", "top_n": 1}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5004"}, "info_items": ["email"]}),
        ],
        outputs=[{"emails": ["liam.anderson@example.com"]}]
    ),
    # Task 81: Eco-Friendly Initiative Launch
    Task(
        annotator="0",
        user_id="task_0081",
        instruction="Within Michael Rodriguez's remit at 2025-07-20T18:14:00Z, assume the Sustainability Manager's mantle. Conceive a 'Green Choice' from 'EcoSmart', marking 30% off, converting EcoSmart adherents upwards in membership, via email campaign concerning our green mission.",
        actions=[
            # get employee id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Michael Rodriguez"}, "info_items": ["employee_id"]}),
            # change role to Sustainability Manager
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1003", "role": "Sustainability Manager"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"brand": "EcoSmart"}, "info_items": ["sku"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Green Choice", "type": "percentage", "discount_value": 30.0, "applicable_skus": ["SMRT-THERM02"], "start_date": "2025-07-20"}),
            # get customers who have bought EcoSmart products
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku": "SMRT-THERM02"}, "info_items": ["customer_id"]}),
            # get customer info by customer_id
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5011"}, "info_items": ["membership_level", "email"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5011", "membership_level": "gold", "current_time": "2025-07-20T18:14:00Z"}),
        ],
        outputs=[{"email": "mia.kim@example.com"}]
    ),
    # Task 82: Emergency Store Support and Crisis Management
    Task(
        annotator="0",
        user_id="task_0082",
        instruction="Robert Zhang's trajectory at 2025-07-20T18:15:00Z, amidst STORE-004's crisis necessitates all inventory transfer to nearby STORE-001. Stage 'Store Support Special' at 20% off affected articles, acquire emails from STORE-004 patrons about disruption.",
        actions=[
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1008", "role": "Crisis Manager"}),
            # Get all inventory items from STORE-004
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "sku"]}),
            # Transfer inventory items to STORE-001
            Action(name="EditInventoryDb", kwargs={"id": "INV-0009", "store_id": "STORE-001", "current_time": "2025-07-20T18:15:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Store Support Special", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"}),
            # get customers who have made transactions at STORE-004
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["customer_id"]}),
            # get customer info by customer_id
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5004", "CUST-5009"]}, "info_items": ["customer_id", "email", "name"]})
        ],
        outputs=[{"email": "liam.anderson@example.com"}, {"email": "charlotte.dubois@example.com"}]
    ),
    # Task 83: Social Media Marketing Integration
    Task(
        annotator="0",
        user_id="task_0083",
        instruction="Under Oliver Diaz at 2025-07-20T18:16:00Z, enter Ryan Kim as a Social Media Manager for STORE-002. Initialize a 'Bargain Electronics' event at 25% for top-priced Electronics commodities Acknowledge Gale Barley in the customer database for QuietTone Earbuds acquisition, processed by Ryan Kim.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Ryan Kim", "role": "Social Media Manager", "store_id": "STORE-002"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Ryan Kim"}, "info_items": ["employee_id"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": ["Electronics"]}, "info_items": ["sku", "price"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Bargain Electronics", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15"], "start_date": "2025-07-20"}),
            # create a new customer Gale Barley
            Action(name="EditCustomersDb", kwargs={"name": "Gale Barley", "email": "gale.barley@example.com", "current_time": "2025-07-20T18:15:00Z"}),
            # get the customer_id of Gale Barley
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Gale Barley"}, "info_items": ["customer_id"]}),
            # get sku of QuietTone Wireless Earbuds
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "QuietTone Wireless Earbuds"}, "info_items": ["sku"]}),
            # add the purchase of QuietTone Wireless Earbuds
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5013", "items": {"AUDIO-NCEBUDS01":1}, "payment_method": "cash", "store_id": "STORE-002", "employee_id": "EMP-1013", "current_time": "2025-07-20T18:15:00Z"}),
            # update the inventory of QuietTone Wireless Earbuds
            Action(name="UpdateInventoryItem", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T18:15:00Z"})
        ],
        outputs=[]
    ),
    # Task 84: Bulk Purchase Corporate Program
    Task(
        annotator="0",
        user_id="task_0084",
        instruction="Functioning as Anna Wilson, dated 2025-07-20T18:17:00Z, forge a company bulk program. Identify any customer orchestrating a single 10-item transaction, enlisting emails and assigning 100 loyalty points.",
        actions=[
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["transaction_id", "line_items", "customer_id"]}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5009"]}, "info_items": ["customer_id", "email", "loyalty_points"]}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5009", "loyalty_points": 775, "current_time": "2025-07-20T18:17:00Z"})
        ],
        outputs=[{"email": ["charlotte.dubois@example.com"]}]
    ),
    # Task 85: Technology Upgrade and Digital Transformation
    Task(
        annotator="0",
        user_id="task_0085",
        instruction="At 2025-10-09T18:18:00Z, check for James O’Connor's birthday claim. If true, include him as an employee under his customer email as 'Temporary Sales Associate.' Arrange 'Birthday Bash' 30% indulgences for today, and enroll Connor O’Connor as a customer via email 'connor.oconnor@example.com'.",
        actions=[
            # Get customers with birthdate today
            Action(name="GetCustomersWithBirthdayToday", kwargs={"current_day": "2025-10-09"}),
            # Get customer info for James O'Connor
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "James O'Connor"}, "info_items": ["customer_id", "email"]}),
            # Add James O'Connor as an employee
            Action(name="EditEmployeesDb", kwargs={"name": "James O'Connor", "email": "james.oconnor@example.com", "role": "Temporary Sales Associate"}),
            # Create 'Birthday Bash' promotion
            Action(name="EditPromotionsDb", kwargs={"name": "Birthday Bash", "type": "percentage", "discount_value": 30.0, "applicable_skus": [], "start_date": "2025-10-09", "end_date": "2025-10-09"}),
            # Add Connor O'Connor to customer database
            Action(name="EditCustomersDb", kwargs={"name": "Connor O'Connor", "email": "connor.oconnor@example.com", "current_time": "2025-10-09T18:18:00Z"}),
        ],
        outputs=[]
    ),
    # Task 86: Employee Training Program Management
    Task(
        annotator="0",
        user_id="task_0086",
        instruction="The identity of Sandra Mitchell at 2025-07-20T18:19:00Z underpins your Training Coordinator role at STORE-003. Tweak 'Office Supplies' inventory with additions to below-20 stocks. Rollout 'Team Learning' promos at 20% off.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Sandra Mitchell", "role": "Training Coordinator", "store_id": "STORE-003"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Sandra Mitchell"}, "info_items": ["employee_id"]}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": "Office Supplies"}, "info_items": ["sku"]}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "OFFC-ERGCHR01"}, "info_items": ["id", "quantity"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003", "quantity_change": 10, "current_time": "2025-07-20T18:19:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Team Learning", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 87: Inventory Security and Loss Prevention
    Task(
        annotator="0",
        user_id="task_0087",
        instruction="In the interest of Robert Zhang, guarantee high-rated inventory pieces at or above $1400 security safety. Secure items to safety stock and adjust status to 'high_security' while dual-flagging variants within critical-buying cities.",
        actions=[
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id"]}),
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1008", "role": "Security Manager"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {}, "info_items": ["sku", "price"]}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": ["ELEC-GAMLP15"]}, "info_items": ["id","sku", "store_id", "quantity", "safety_stock"]}),
            Action(name="EditInventoryDb", kwargs={"id": "INV-0013", "quantity": 0, "safety_stock": 5, "status": "high_security", "current_time": "2025-07-20T18:20:00Z"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"role": "Inventory Specialist"}, "info_items": ["email"]})
        ],
        outputs=[{"email": "zoe.martinez@retailpos.com"}]
    ),
    # Task 88: Local Community Engagement Initiative
    Task(
        annotator="0",
        user_id="task_0088",
        instruction="You exhibit managerial discontent as of 2025-07-20T18:21:00Z, terminating the three oldest promotions in circulation, relocating Henry Adams to STORE-005 due to professional preference.",
        actions=[
            # Get all promotions
            Action(name="GetPromotionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["promotion_id", "start_date"]}),
            # Sort promotions by start date and get the 3 oldest
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"PROMO-001": "2025-06-01", "PROMO-002": "2025-05-15", "PROMO-003": "2025-06-10", "PROMO-004": "2025-09-05", "PROMO-005": "2025-04-01", "PROMO-006": "2025-05-20", "PROMO-007": "2025-06-14"}, "sort_order": "oldest", "top_n": 3}),
            # Delete the 3 oldest promotions
            Action(name="EditPromotionsDb", kwargs={"promotion_id": "PROMO-005", "delete": True}),
            Action(name="EditPromotionsDb", kwargs={"promotion_id": "PROMO-002", "delete": True}),
            Action(name="EditPromotionsDb", kwargs={"promotion_id": "PROMO-006", "delete": True}),
            # Get employee info for Henry
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Henry Adams"}, "info_items": ["employee_id"]}),
            # Move Henry Adams to STORE-005
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1020", "store_id": "STORE-005"})
        ],
        outputs=[]
    ),
    # Task 89: Customer Feedback Response System
    Task(
        annotator="0",
        user_id="task_0089",
        instruction="Performing as Rachel Anderson at 2025-07-20T18:22:00Z, associate yourself with the 'Customer Relations Manager' mantle. Discover returners creating a 'We Listen' offer at 25% off all goods, drawing inclusive response feedback.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Rachel Anderson", "role": "Customer Relations Manager"}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Rachel Anderson"}, "info_items": ["employee_id"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"status": "returned"}, "info_items": ["customer_id"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "We Listen", "type": "percentage", "discount_value": 25.0, "applicable_skus": [], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5012"}, "info_items": ["email"]})
        ],
        outputs=[{"emails": ["logan.smith@example.com"]}]
    ),
    # Task 90: Student and Education Discount Program
    Task(
        annotator="0",
        user_id="task_0090",
        instruction="In the name of Michael Rodriguez, on 2025-07-20T18:23:00Z, launch a 'Student Success' mission ensuring electronics and books see a 40% price cut. Reclassify the youngest basic membership holder to the student level.",
        actions=[
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": ["Electronics", "Books"]}, "info_items": ["sku", "name", "category"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "Student Success", "type": "percentage", "discount_value": 40.0, "applicable_skus": ["ELEC-4KTV55","AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04", "BOOK-KDSSTY01"], "start_date": "2025-07-20"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": "basic"}, "info_items": ["customer_id", "birthdate"]}),
            # Sort customers by birthdate to find the youngest
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5008":"1998-10-09", "CUST-5012": "2000-01-19"}, "sort_order": "newest", "top_n": 1}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5012", "membership_level": "student", "current_time": "2025-07-20T18:23:00Z"}),
        ],
        outputs=[]
    ),
    # Task 91: Product Quality Assurance Initiative
    Task(
        annotator="0",
        user_id="task_0091",
        instruction="As unauthorized access has been initiated, expunge all customers who succeeded in purchases, deleting respective credit card transactions to safeguard anonymity.",
        actions=[
            # get all customers who have made transactions
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["customer_id"]}),
            # delete customer records using edit_customers_db
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5001", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5002", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5003", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5004", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5005", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5006", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5007", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5008", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5009", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5010", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5011", "delete": True}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5012", "delete": True}),
            # get all transactions made with credit cards
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"payment_method": "credit_card"}, "info_items": ["transaction_id"]}),
            # delete transactions made with credit cards using edit_transactions_db
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0001", "delete": True}),
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0004", "delete": True}),
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0005", "delete": True}),
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0009", "delete": True}),
            Action(name="EditTransactionsDb", kwargs={"transaction_id": "TXN-0012", "delete": True})
            ],
        outputs=[]
    ),
    # Task 92: Seasonal Inventory Optimization
    Task(
        annotator="0",
        user_id="task_0092",
        instruction="As Patricia Davis at 2025-07-20T18:25:00Z, delineate yourself as 'Inventory Optimization Manager' centered at STORE-003. Spearhead low-stock management across the site, configuring 'Back to School Ready' exchanges at 30% for select Office and Apparel wares. Downgrade 'Floor Supervisor,' granting Assistant.",
        actions=[
            Action(name="EditEmployeesDb", kwargs={"name": "Patricia Davis", "role": "Inventory Optimization Manager", "store_id": "STORE-003"}),
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"category": ["Apparel", "Office Supplies"]}, "info_items": ["sku"]}),
            # check for low stock with check_low_stock
            Action(name="CheckLowStock", kwargs={"store_id": "STORE-003", "current_time": "2025-07-20T18:25:00Z"}),
            Action(name="EditPromotionsDb", kwargs={"name": "Back to School Ready", "type": "percentage", "discount_value": 30.0, "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01", "OFFC-ERGCHR01"], "start_date": "2025-07-20"}),
            # get employees info by role
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"role": "Floor Supervisor", "store_id": "STORE-003"}, "info_items": ["employee_id"]}),
            # change role to Assistant to the Floor Supervisor
            Action(name="EditEmployeesDb", kwargs={"employee_id": "EMP-1020", "role": "Assistant to the Floor Supervisor"})
        ],
        outputs=[]
    ),
    # Task 93: Mobile App Integration and Digital Rewards
    Task(
        annotator="0",
        user_id="task_0093",
        # promo for products bought by people that opt in
        instruction="Undertake Jennifer Williams’s identity throughout 2025-07-20T18:25:00Z. Ascertain products bought by marketing-consent customers leading to 'Marketing Opt-In' materializing at 25%-off product listings.",
        actions=[
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"opt_in_marketing": True}, "info_items": ["customer_id"]}),
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5001", "CUST-5003", "CUST-5004", "CUST-5006", "CUST-5008", "CUST-5009", "CUST-5011"]}, "info_items": ["line_items"]}),
            # create promotion for products bought by customers that opted in
            Action(name="EditPromotionsDb", kwargs={"name": "Marketing Opt-In", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["ELEC-4KTV55","ELEC-RCHAA04","GROC-GRNLBR12","GROC-SPRWAT6P","SPORT-BIKHLM01","SPORT-YOGMAT01","OFFC-ERGCHR01","HOME-DESKLMP01","BOOK-KDSSTY01","HOME-BTHTWL01","KITCH-CHEFKNF8","SMRT-THERM02"], "start_date": "2025-07-20"}),
        ],
        outputs=[]
    ),
    # Task 94: Family and Group Shopping Experience
    Task(
        annotator="0",
        user_id="task_0094",
        # reduce stock of products bought by the youngest 2 customers
        instruction="Designate gold membership's youngest patron’s acquisitions, liberating such inventory as no-charge handouts, amending stock levels accordingly.",
        actions=[
            # get customers info by birthdate
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"membership_level": "gold"}, "info_items": ["customer_id", "birthdate"]}),
            # sort customers by birthdate to find the youngest
            Action(name="FilterAndSortIdsByDate", kwargs={"ids_dates": {"CUST-5001": "1990-07-12", "CUST-5010": "1983-03-04"}, "sort_order": "newest", "top_n":1}),
            # get transactions info by customer_id
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"customer_id": "CUST-5001"}, "info_items": ["line_items"]}),
            # get inventory information of 4K TV
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "ELEC-4KTV55"}, "info_items": ["sku", "store_id"]}),
            # reduce stock of 4K TV by 1
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001", "quantity_change": -1, "current_time": "2025-07-20T18:26:00Z"}),
            # get inventory information of rechargeable battery
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": "ELEC-RCHAA04"}, "info_items": ["sku", "store_id"]}),
            Action(name="UpdateInventoryItem", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003", "quantity_change": -1, "current_time": "2025-07-20T18:26:00Z"}),
        ],
        outputs=[]
    ),
    # Task 95: Cross-Store Collaboration Enhancement
    Task(
        annotator="0",
        user_id="task_0095",
        instruction="In the shoes of Zoe Martinez, 2025-07-20T18:28:00Z, scaffold an online counterbalance of STORE-004's inventory with motley registrations tethered to 'ONLINE'. Actualize 'Online Launch' at 20% for virtual site visitors.",
        actions=[
            # get all inventory items from STORE-004
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["id", "sku", "quantity"]}),
            # create new inventory items in ONLINE store
            Action(name="EditInventoryDb", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 4, "store_id": "ONLINE", "current_time": "2025-07-20T18:28:00Z"}),
            # edit product status to online
            Action(name="EditProductsDb", kwargs={"sku": "SPORT-BIKHLM01", "status": "online", "current_time": "2025-07-20T18:28:00Z"}),
            # create the promotion
            Action(name="EditPromotionsDb", kwargs={"name": "Online Launch", "type": "percentage", "discount_value": 20.0, "applicable_skus": ["SPORT-BIKHLM01"], "start_date": "2025-07-20"})
        ],
        outputs=[]
    ),
    # Task 96: Senior Customer Appreciation Program
    Task(
        annotator="0",
        user_id="task_0096",
        instruction="Leveraging Robert Zhang's approach, the mission at 2025-07-20T18:29:00Z features a 'Golden Years Special' for top-priced inventory, 45% off enforced. Emma Wilson then proceeds to purchase the ProSlice 8\" Chef Knife with her credit card thereafter.",
        actions=[
            # get employee id
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Robert Zhang"}, "info_items": ["employee_id", "store_id"]}),
            # get the 2 most expensive products in STORE-002
            Action(name="GetTopNMostExpensiveProductsByStore", kwargs={"store_id": "STORE-002", "n": 2}),
            # create the promotion
            Action(name="EditPromotionsDb", kwargs={"name": "Golden Years Special", "type": "percentage", "discount_value": 45.0, "applicable_skus": ["ELEC-GAMLP15", "CLTH-WINJKT01"], "start_date": "2025-07-20", "end_date": "2025-12-31"}),
            # get the customer_id of Ava Thompson
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Emma Wilson"}, "info_items": ["customer_id"]}),
            # get the sku of ProSlice 8\" Chef Knife
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {"name": "ProSlice 8\" Chef Knife"}, "info_items": ["sku"]}),
            # Create a purchase transaction for Ava Thompson
            Action(name="CreatePurchaseTransaction", kwargs={"customer_id": "CUST-5001", "employee_id": "EMP-1008", "items":{"KITCH-CHEFKNF8":1}, "payment_method": "credit_card", "store_id": "STORE-002", "current_time": "2025-07-20T18:29:00Z"}),
            # reduce the inventory of ProSlice 8\" Chef Knife by 1
            Action(name="UpdateInventoryItem", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002", "quantity_change": -1, "current_time": "2025-07-20T18:29:00Z"}),
        ],
        outputs=[]
    ),
    # Task 97: Gift Card and Gifting Program Expansion
    Task(
        annotator="0",
        user_id="task_0097",
        instruction="Assuming Ethan Walker's stance at 2025-07-20T18:30:00Z, manufacture 'Perfect Gift Finder' applying a 25% markdown on sub-0.2kg merchandise. Accumulate retailer quantifiable counts as STORE-002’s 'Lightweight Gifts' representation under the SKU 'LW-GIFTS'.",
        actions=[
            # get all products and their weight
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {}, "info_items": ["sku", "weight_kg"]}),
            # create the promotion
            Action(name="EditPromotionsDb", kwargs={"name": "Perfect Gift Finder", "type": "percentage", "discount_value": 25.0, "applicable_skus": ["AUDIO-NCEBUDS01", "ELEC-RCHAA04"], "start_date": "2025-07-20"}),
            # Get inventory quantities for the promotion items
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"sku": ["AUDIO-NCEBUDS01", "ELEC-RCHAA04"]}, "info_items": ["sku", "quantity"]}),
            # create new inventory item 'Lightweight Gifts'
            Action(name="EditInventoryDb", kwargs={"sku": "LW-GIFTS", "quantity": 112, "store_id": "STORE-002", "current_time": "2025-07-20T18:30:00Z"}),
        ],
        outputs=[]
    ),
    # Task 98: Flash Sale and Limited-Time Offer Strategy
    Task(
        annotator="0",
        user_id="task_0098",
        instruction="Run with Amanda Richards's directives at 2025-07-20T18:31:00Z for a surprise strategy: implement '1 Day Lightning Deal' at 55% off skus beyond $500. Induct Tom Thomas to the team as 'Sales Associate' at 'STORE-001' addressing peak hour.",
        actions=[
            # get all products and their price and sku
            Action(name="GetProductsInfoByParam", kwargs={"filter_params": {}, "info_items": ["sku", "price"]}),
            Action(name="EditPromotionsDb", kwargs={"name": "1 day Lightning Deal", "type": "percentage", "discount_value": 55.0, "applicable_skus": ["ELEC-4KTV55", "ELEC-GAMLP15"], "start_date": "2025-07-20", "end_date": "2025-07-20"}),
            # add the new employee
            Action(name="EditEmployeesDb", kwargs={"name": "Tom Thomas", "role": "Sales Associate", "store_id": "STORE-001"}),
        ],
        outputs=[]
    ),
    # Task 99: Customer Referral and Network Growth
    Task(
        annotator="0",
        user_id="task_0099",
        instruction="Pinpoint the most-employed promotion, augment its sanction cap by 200% and cease this day in one year’s time. Enlist customer-specific accounts, bestowing loyalty rewards.",
        actions=[
            # get times used for each promotion
            Action(name="GetPromotionsInfoByParam", kwargs={"filter_params": {}, "info_items": ["promotion_id", "times_used"]}),
            # get the skus from promo-002
            Action(name="GetPromotionsInfoByParam", kwargs={"filter_params": {"promotion_id": "PROMO-002"}, "info_items": ["applicable_skus", "usage_limit", "end_date"]}),
            # double the usage limit of promo-002 and set it to expire next year
            Action(name="EditPromotionsDb", kwargs={"promotion_id": "PROMO-002", "usage_limit": 1000, "end_date": "2026-07-20"}),
            # get all customers that have purchased these skus
            Action(name="GetTransactionsInfoByParam", kwargs={"filter_params": {"sku":["HOM-COFMKR12", "KITCH-CHEFKNF8"]}, "info_items": ["customer_id"]}),
            # get the loyalty points of these customers
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"customer_id": ["CUST-5002", "CUST-5011"]}, "info_items": ["customer_id", "loyalty_points"]}),
            # add 50 loyalty points to these customers
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5002", "loyalty_points": 925, "current_time": "2025-07-20T18:32:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5011", "loyalty_points": 610, "current_time": "2025-07-20T18:32:00Z"})
        ],
        outputs=[]
    ),
    # Task 100: Data Analytics and Customer Insights Program
    Task(
        annotator="0",
        user_id="task_0100",
        instruction="Jack Robinson records reading into 2025-07-20T18:33:00Z as Charlie Chaplin endeavors to own STORE’s stock. Catalog him under 'charlie.chaplin@example.com,' fulfilling credit-based acquisition while reconciling stock and aligning reward directly with transaction figures.",
        actions=[
            Action(name="EditCustomersDb", kwargs={"name": "Charlie Chaplin", "email": "charlie.chaplin@example.com", "current_time": "2025-07-20T18:33:00Z"}),
            Action(name="GetCustomersInfoByParam", kwargs={"filter_params": {"name": "Charlie Chaplin"}, "info_items": ["customer_id"]}),
            Action(name="GetEmployeesInfoByParam", kwargs={"filter_params": {"name": "Jack Robinson"}, "info_items": ["employee_id", "store_id"]}),
            Action(name="GetInventoryInfoByParam", kwargs={"filter_params": {"store_id": "STORE-004"}, "info_items": ["sku", "quantity"]}),
            Action(name="CreatePurchaseTransaction", kwargs={"employee_id": "EMP-1034", "customer_id": "CUST-5013", "items": {"SPORT-BIKHLM01": 4}, "current_time": "2025-07-20T18:33:00Z", "store_id": "STORE-004", "payment_method": "credit_card"}),
            # update inventory levels
            Action(name="UpdateInventoryItem", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004", "quantity_change": -4, "current_time": "2025-07-20T18:33:00Z"}),
            Action(name="EditCustomersDb", kwargs={"customer_id": "CUST-5013", "loyalty_points": 314, "current_time": "2025-07-20T18:33:00Z"})
        ],
        outputs=[]
    ),
]
