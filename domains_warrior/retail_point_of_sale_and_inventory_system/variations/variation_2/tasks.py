from domains.dto import Task, Action

TASKS = [

    # Customer Service

    Task(
        annotator="lucas",
        user_id="lucas_task_001_customer_service",
        instruction="Get customer details for CUST-5001 to assess current status. If the membership level is not 'gold', update it to 'gold'. Check loyalty points for CUST-5001 to understand customer value. If the email is not 'customer.updated@email.com', update it for better communication. List transactions for CUST-5001 to analyze purchase history. If the phone number is not '+1-555-123-4567', update it for improved contact information. Get transaction details for TXN-0001 only if it exists in the customer's transaction history. List transactions for CUST-5001 again to verify all updates were successful.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5001", "new_email": "customer.updated@email.com"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-123-4567"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[
            "Customer details assessed for service needs", "Membership level updated to gold based on current status", "Loyalty points checked for customer value", "Email updated for better communication",
            "Transactions analyzed for purchase history", "Phone number updated for improved contact", "Transaction details retrieved for verification", "Transactions listed again to verify successful updates"
        ]
    ),

    # Product Management

    Task(
        annotator="lucas",
        user_id="lucas_task_002_product_management",
        instruction="Get product details for CLTH-SLFJEAN34 to assess current pricing strategy. If the current price is above $55, update price of CLTH-SLFJEAN34 to $54.95 for competitive pricing. List all products with limit 25 to analyze overall inventory status. Get inventory for CLTH-SLFJEAN34 and check if stock is below 75. If CLTH-SLFJEAN34 stock is below 75, update stock for CLTH-SLFJEAN34 to 80 to ensure adequate supply. List products by category 'Apparel' to verify category inventory management. Get total sales for date 2025-06-06 to assess business performance. If total sales are above $800, get product details for CLTH-SLFJEAN34 again to verify the price and inventory updates were successful.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="list_all_products", kwargs={"limit": 25}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 80}),
            Action(name="list_products_by_category", kwargs={"category": "Apparel"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"})
        ],
        outputs=[
            "Product details for jeans assessed for pricing strategy", "All products listed to analyze inventory status", "Inventory level checked for restocking needs",
            "Stock updated to 80 based on low inventory condition", "Apparel products listed to verify category inventory", "Sales total retrieved for performance assessment"
        ]
    ),

    # Omnichannel Customer Journey

    Task(
        annotator="lucas",
        user_id="lucas_task_003_omnichannel_customer_journey",
        instruction="Execute a full omnichannel customer journey for CUST-5001: get customer details, update email to omnichannel.customer@email.com, update phone to +1-555-111-2222, update address to 100 Omnichannel Ave, City, ST 12345, check loyalty points, update membership to platinum, list transactions, get transaction details for TXN-0001, record sale with 1 ELEC-4KTV55 using credit card, record sale with 2 CLTH-SLFJEAN34 using debit card, update loyalty points by adding 200, update membership to VIP, list all products with limit 50, get product details for HOM-COFMKR12, update product price to $109.99, get inventory level, update stock to 60, get total sales for date 2025-06-05, and verify all updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5001", "new_email": "omnichannel.customer@email.com"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-111-2222"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5001", "new_address": "100 Omnichannel Ave, City, ST 12345"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "CLTH-SLFJEAN34", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 200}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "VIP"}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 109.99}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[
            "Omnichannel journey executed for CUST-5001, all updates verified"
        ]
    ),

    # Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_004_inventory",
        instruction="List low stock products with threshold 20 to identify critical inventory items. Get inventory level for KITCH-CHEFKNF8 and check if it's below 50. If KITCH-CHEFKNF8 stock is below 50, update it to 40. List products by category 'Home & Kitchen' to analyze category inventory. Get inventory level for HOM-COFMKR12 to check if it needs restocking. List all products with limit 20 to verify inventory status. Get total sales for date 2025-06-05 to assess business performance. If total sales are above $1000, update loyalty points for customer CUST-5003 by adding 50 points as a performance reward.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 20}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="list_all_products", kwargs={"limit": 20}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 50})
        ],
        outputs=[
            "Low stock products identified and analyzed", "Kitchen knife inventory level assessed", "Kitchen knife stock updated to 40 based on low stock condition", "Home & Kitchen category inventory analyzed", "Coffee maker inventory level checked for restocking assessment", "All products listed to verify inventory status", "Sales total retrieved for performance assessment", "50 points added to customer CUST-5003 as performance reward"
        ]
    ),

    # Sales Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_005_sales",
        instruction="Record a sale for customer CUST-5004 with 2 GROC-ALMBTR500 using debit card. Get total sales for date 2025-06-05. Get customer details for CUST-5004. Get customer loyalty points for CUST-5004. List transactions for CUST-5004. Get transaction details for TXN-0004. Get total sales for date 2025-06-06 to compare with previous total.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5004"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "GROC-ALMBTR500", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5004"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"})
        ],
        outputs=[
            "Almond butter sale recorded", "Daily sales total retrieved", "Customer details retrieved", "Customer loyalty points retrieved", "Transactions listed", "Transaction details retrieved", "Sales total retrieved again"
        ]
    ),

    # Product Category Management

    Task(
        annotator="lucas",
        user_id="lucas_task_006_product_category",
        instruction="List products by category 'Electronics', get product details for ELEC-GAMLP15, update price of ELEC-GAMLP15 to $599.99, list products by category 'Home & Kitchen', get inventory for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 45, get total sales for date 2025-06-06, update customer loyalty points for CUST-5006 by adding 100 points, and list all products with limit 30.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-GAMLP15", "new_price": 599.99}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 45}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 100}),
            Action(name="list_all_products", kwargs={"limit": 30})
        ],
        outputs=[
            "Electronics products listed", "Gaming laptop details retrieved", "Gaming laptop price updated to $599.99", "Home & Kitchen products listed",
            "Kitchen knife inventory retrieved", "Kitchen knife stock updated to 45", "Sales total retrieved", "Customer loyalty points updated by 100", "All products listed with limit 30"
        ]
    ),

    # Return Processing

    Task(
        annotator="lucas",
        user_id="lucas_task_007_return_processing",
        instruction="Process return for transaction TXN-0001 only if the purchase date is within the last 90 days with reason 'Customer return'. If so, update customer loyalty points for CUST-5001 by adding 25 points, list transactions for CUST-5001, get inventory level for ELEC-RCHAA04, update product stock for ELEC-RCHAA04 to 25, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="process_return", kwargs={"original_transaction_id": "TXN-0001", "items_to_return": [{"sku": "ELEC-RCHAA04", "quantity": 1}], "reason": "Customer return"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 25}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-RCHAA04"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-RCHAA04", "new_stock_quantity": 25}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Return processed for remote control", "25 points added to customer", "Customer transactions listed",
            "Remote control inventory checked", "Remote control stock updated to 25", "Daily sales total retrieved"
        ]
    ),

    # Return Management

    Task(
        annotator="lucas",
        user_id="lucas_task_008_return_management",
        instruction="Process return for transaction TXN-0002 only if the purchase date is within the last 90 days with reason 'Customer return'. If so, update inventory for product KITCH-CHEFKNF8 to stock 55, update customer loyalty points for CUST-5002 by adding 30 points as a service reward, and list transactions for CUST-5002.",
        actions=[
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="process_return", kwargs={"original_transaction_id": "TXN-0002", "items_to_return": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "reason": "Customer return"}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 55}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 30}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[
            "Return processed for kitchen knife", "Kitchen knife stock updated to 55", "30 points added to customer based on active transactions", "Customer transactions analyzed for purchase history and loyalty verification"
        ]
    ),

    # Product Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_009_product_inventory_management",
        instruction="Get product details for ELEC-4KTV55 to assess current pricing. If the current price is above $300, update price of ELEC-4KTV55 to $299.99 for competitive pricing. List all products with limit 30 to analyze inventory status. Get inventory for ELEC-4KTV55 and check if stock is below 50. If ELEC-4KTV55 stock is below 50, update stock for ELEC-4KTV55 to 60 to ensure adequate supply. List products by category 'Electronics' to verify category inventory. Get total sales for date 2025-06-07 to assess business performance. If total sales are above $1000, get product details for ELEC-4KTV55 again to verify the price update was successful and inventory is properly managed.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 299.99}),
            Action(name="list_all_products", kwargs={"limit": 30}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 60}),
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-07"})
        ],
        outputs=[
            "4K TV details assessed for pricing strategy", "Price updated to $299.99 based on competitive analysis", "All products listed to analyze inventory status", "Inventory level checked for restocking needs",
            "Stock updated to 60 based on low inventory condition", "Electronics products listed to verify category inventory", "Sales total retrieved for performance assessment"
        ]
    ),

    # Product Category Management
    Task(
        annotator="lucas",
        user_id="lucas_task_010_product_category",
        instruction="List products by category 'Home & Kitchen' to analyze category inventory. Get product details for HOM-COFMKR12 to assess current pricing. If the current price is above $90, update price of HOM-COFMKR12 to $89.99 for competitive pricing. List products by category 'Grocery' to verify category inventory status. Get inventory for GROC-ALMBTR500 and check if stock is below 120. If GROC-ALMBTR500 stock is below 120, update product stock for GROC-ALMBTR500 to 100 to ensure adequate supply. Get total sales for date 2025-06-08 to assess business performance. If total sales are above $600, update customer loyalty points for CUST-5007 by adding 50 points as a performance reward. List all products with limit 25 to verify overall inventory status.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="list_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 100}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-08"}),
            Action(name="list_all_products", kwargs={"limit": 25})
        ],
        outputs=[
            "Home & Kitchen products analyzed for category inventory", "Coffee maker details assessed for pricing strategy", "Grocery products verified for category inventory status",
            "Almond butter inventory checked for restocking needs", "Almond butter stock updated to 100 based on low inventory condition", "Sales total retrieved for performance assessment", "All products listed to verify overall inventory status"
        ]
    ),

    # Return Processing Management

    Task(
        annotator="lucas",
        user_id="lucas_task_011_return_processing_management",
        instruction="Process return for transaction TXN-0003 only if the purchase date is within the last 90 days with reason 'Customer return'. If so, return 1 GROC-GRNLBR12 with reason 'Customer preference', update inventory for returned product to 15, get customer details for CUST-5003, update customer loyalty points for CUST-5003 by adding 15 points, get transaction details for TXN-0003, and list transactions for CUST-5003.",
        actions=[
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="process_return", kwargs={"original_transaction_id": "TXN-0003", "items_to_return": [{"sku": "GROC-GRNLBR12", "quantity": 1}], "reason": "Customer preference"}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 15}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 15}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"})
        ],
        outputs=[
            "Return processed for green lentils", "Green lentils inventory checked", "Green lentils stock updated to 15",
            "Customer details retrieved", "15 points added to customer", "Transaction details retrieved", "Customer transactions listed"
        ]
    ),

    # Advanced Customer Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_012_advanced_customer_analytics",
        instruction="Conduct comprehensive customer analytics for multiple customers simultaneously. Get customer details for CUST-5001, CUST-5002, CUST-5003, and CUST-5004. Analyze loyalty points for all four customers. Update membership levels based on analytics: CUST-5001 to 'platinum', CUST-5002 to 'gold', CUST-5003 to 'silver', CUST-5004 to 'bronze'. List transaction history for all customers. Get transaction details for TXN-0001, TXN-0002, TXN-0003, and TXN-0004. Update customer loyalty points: CUST-5001 +300, CUST-5002 +200, CUST-5003 +150, CUST-5004 +100. Record strategic sales: CUST-5001 buys 1 ELEC-4KTV55, CUST-5002 buys 2 AUDIO-BTSPKR02, CUST-5003 buys 1 HOM-COFMKR12, CUST-5004 buys 3 GROC-ALMBTR500. Get total sales for date 2025-06-05 and 2025-06-06 for comparison. Verify all customer updates were successful.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5004"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5004"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5002", "new_membership_level": "gold"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5003", "new_membership_level": "silver"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5004", "new_membership_level": "bronze"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 300}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 150}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5004", "points_to_add": 100}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "HOM-COFMKR12", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "cash"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[
            "Comprehensive customer analytics completed for all four customers", "Customer loyalty points analyzed for strategic planning", "Membership levels optimized based on analytics", "Transaction histories analyzed for customer behavior patterns", "Transaction details verified for accuracy", "Strategic loyalty point allocations completed", "Targeted sales recorded for each customer segment", "Customer communication channels updated", "Sales performance comparison completed", "All customer updates verified successfully"
        ]
    ),

    # Strategic Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_013_strategic_inventory_management",
        instruction="Execute comprehensive strategic inventory management across multiple product categories. List low stock products with threshold 20. Analyze inventory levels for ELEC-4KTV55, AUDIO-BTSPKR02, HOM-COFMKR12, KITCH-CHEFKNF8, GROC-ALMBTR500, and CLTH-SLFJEAN34. Update product stock strategically: ELEC-4KTV55 to 45, AUDIO-BTSPKR02 to 35, HOM-COFMKR12 to 55, KITCH-CHEFKNF8 to 40, GROC-ALMBTR500 to 80, CLTH-SLFJEAN34 to 50. Get product details for all six products. Update product prices based on market analysis: ELEC-4KTV55 to $799.99, AUDIO-BTSPKR02 to $169.99, HOM-COFMKR12 to $89.99, KITCH-CHEFKNF8 to $199.99, GROC-ALMBTR500 to $12.99, CLTH-SLFJEAN34 to $79.99. List products by category 'Electronics', 'Home & Kitchen', 'Grocery', and 'Apparel'. Add new product 'Strategic Inventory Monitor' in Electronics category with description 'Advanced inventory monitoring and optimization system' and price $299.99 and stock quantity 25. Get total sales for date 2025-06-05 and 2025-06-06. Update customer loyalty points for CUST-5005 by adding 400 points. Verify all inventory updates were successful.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 20}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 45}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 55}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 80}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 50}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 799.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 169.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="update_product_price", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 199.99}),
            Action(name="update_product_price", kwargs={"sku": "GROC-ALMBTR500", "new_price": 12.99}),
            Action(name="update_product_price", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 79.99}),
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="list_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="list_products_by_category", kwargs={"category": "Apparel"}),
            Action(name="add_new_product", kwargs={"name": "Strategic Inventory Monitor", "description": "Advanced inventory monitoring and optimization system", "category": "Electronics", "price": 299.99, "stock_quantity": 25}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 400}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"})
        ],
        outputs=[
            "Strategic inventory management completed across all product categories", "Low stock products identified and addressed", "Inventory levels optimized for all six products", "Product stock strategically updated based on demand analysis", "Product specifications verified for all items", "Product prices optimized based on market analysis", "Category inventory analysis completed", "Strategic inventory monitor added to product portfolio", "Sales performance comparison completed", "Strategic sales recorded for multiple customers", "Customer loyalty points updated", "All inventory updates verified successfully"
        ]
    ),

    # Inventory Restocking Management

    Task(
        annotator="lucas",
        user_id="lucas_task_014_inventory_restocking_management",
        instruction="List low stock products with threshold 15 to identify critical inventory items. Check if HOM-COFMKR12 is in the low stock list. Get its inventory level and update product stock for HOM-COFMKR12 to 40. Get product details for HOM-COFMKR12 to verify current pricing. Update price of HOM-COFMKR12 to $79.99. List products by category 'Home & Kitchen' to analyze category inventory status. Check if KITCH-CHEFKNF8 is also low stock. Get inventory for KITCH-CHEFKNF8 and update product stock for KITCH-CHEFKNF8 to 30. Get total sales for date 2025-06-09 to assess business performance and determine if restocking was effective.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 15}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 40}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 79.99}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 30}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-09"})
        ],
        outputs=[
            "Critical inventory items identified and analyzed", "Coffee maker inventory level assessed", "Coffee maker stock updated to 40", "Coffee maker product details verified",
            "Coffee maker price updated to $79.99 based on market analysis", "Home & Kitchen category inventory analyzed", "Kitchen knife inventory level assessed", "Kitchen knife stock updated to 30", "Sales performance assessed to evaluate restocking effectiveness"
        ]
    ),

    # Sales

    Task(
        annotator="lucas",
        user_id="lucas_task_015_sales",
        instruction="Get total sales for date 2025-06-05, update loyalty points for CUST-5002 by adding 50 points, get customer details for CUST-5002, list transactions for CUST-5002, get transaction details for TXN-0002, update transaction status for TXN-0002 to 'completed', get inventory for HOM-COFMKR12, and update product stock for HOM-COFMKR12 to 35.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 50}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 35})
        ],
        outputs=[
            "Daily sales total retrieved", "50 points added to customer", "Customer details retrieved",
            "Transactions listed", "Transaction details retrieved", "Transaction status updated", "Inventory level retrieved", "Product stock updated"
        ]
    ),

    # Employee Performance Management

    Task(
        annotator="lucas",
        user_id="lucas_task_016_employee_performance",
        instruction="Get employee details for EMP-1002. If EMP-1002 is not currently active, update status to 'active'. Add new employee Lisa Martinez as Sales Associate at STORE-001 whose phone number is +1-555-210-1015 and email is lisa.martinez@retailpos.com. If EMP-1003 exists, remove employee EMP-1003. Get employee details for EMP-1008 to verify the final state, and update employee status for EMP-1008 to 'active'.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            # if EMP-1002 is not currently active:
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Lisa Martinez", "role": "Sales Associate", "store_id": "STORE-001", "email": "lisa.martinez@retailpos.com", "phone_number": "+1-555-210-1015"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1003"}),
            # if EMP-1003 exists:
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            # always update EMP-1008 to active:
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "active"})
        ],
        outputs=[
            "Employee details for John Smith retrieved", "Employee status checked", "New employee Lisa Martinez added", "All employees listed to verify addition",
            "Employee status checked (already active)", "Employee count verified", "Employee removed", "Employee count verified after removal",
            "Final employee details retrieved", "Employee status updated to active"
        ]
    ),

    # Customer Segmentation Analysis

    Task(
        annotator="lucas",
        user_id="lucas_task_017_customer_segmentation",
        instruction="Get customer details for CUST-5006, get customer loyalty points for CUST-5006. Get customer details for CUST-5007, get customer loyalty points for CUST-5007. Update customer loyalty points for CUST-5001 by adding 50 points. Get customer details for CUST-5001. List transactions for CUST-5001. Get transaction details for TXN-0001. Update customer membership level for CUST-5001 to 'platinum'. Get total sales for date 2025-06-05 to analyze customer spending patterns.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5007"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "First customer details retrieved", "First customer loyalty points checked", "Second customer details retrieved", "Second customer loyalty points checked", "Customer loyalty points updated by 50", "Customer details retrieved", "Transactions listed", "Transaction details retrieved", "Customer membership updated to platinum", "Daily sales total retrieved for analysis"
        ]
    ),

    # Innovation Growth Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_018_employee_management",
        instruction="Get employee details for EMP-1002. If EMP-1003 is active, remove employee EMP-1003. Add new employee Sarah Wilson as Sales Associate at STORE-001 whose phone number is +1-555-210-1016 and email is sarah.wilson@retailpos.com. Update employee status for EMP-1004 to 'on_leave' if not already. Get employee details for EMP-1008 to verify the final state.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1003"}),
            # if EMP-1003 is active:
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="add_employee", kwargs={"name": "Sarah Wilson", "role": "Sales Associate", "store_id": "STORE-001", "email": "sarah.wilson@retailpos.com", "phone_number": "+1-555-210-1016"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            # if EMP-1004 is not already on_leave:
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "on_leave"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"})
        ],
        outputs=[
            "Employee details for John Smith retrieved", "Employee status checked", "New employee Sarah Wilson added", "All employees listed to verify addition",
            "Employee status rechecked", "Employee count verified", "Employee removed", "Employee count verified after removal",
            "Employee status updated to on_leave", "Final employee details retrieved"
        ]
    ),

    # Inventory Audit and Reconciliation

    Task(
        annotator="lucas",
        user_id="lucas_task_019_product_innovation",
        instruction="List products by category 'Electronics', add new product 'Smart Watch Pro' in Electronics category with description 'Advanced fitness tracking smartwatch with GPS' and price $299.99 and stock quantity 30, get product details for the newly added Smart Watch Pro (ELEC-0006), update product stock for ELEC-0006 to 30, list all products with limit 50, and update product price for ELEC-0006 to $319.99.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="add_new_product", kwargs={"name": "Smart Watch Pro", "description": "Advanced fitness tracking smartwatch with GPS", "category": "Electronics", "price": 299.99, "stock_quantity": 30}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-0006"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 30}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-0006", "new_price": 319.99})
        ],
        outputs=[
            "Electronics products listed", "Smart watch pro added with unique SKU", "Smart watch pro details retrieved", "Smart watch pro stock updated to 30",
            "All products listed within limit", "Smart watch pro price updated to $319.99"
        ]
    ),
    # Customer Lifecycle Management

    Task(
        annotator="lucas",
        user_id="lucas_task_020_innovation_growth",
        instruction="List products by category 'Sports & Outdoors' to check current count. If there are 2 or fewer products in the category, add new product 'Premium Yoga Mat' in Sports & Outdoors category with description 'Non-slip premium yoga mat with alignment lines' and price $89.99 and stock quantity 40. Get product details for the newly added Premium Yoga Mat using SKU SPOR-0003. List all products with limit 50 (within policy limit), and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="add_new_product", kwargs={"name": "Premium Yoga Mat", "description": "Non-slip premium yoga mat with alignment lines", "category": "Sports & Outdoors", "price": 89.99, "stock_quantity": 40}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "SPOR-0003"}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Sports & Outdoors products listed and counted", "Premium yoga mat added with SKU SPOR-0003", "Premium yoga mat details retrieved", "Sports & Outdoors products listed again", "All products listed within policy limit of 50", "Sales total retrieved"
        ]
    ),

    # Employee Management

    Task(
        annotator="lucas",
        user_id="lucas_task_021_employee",
        instruction="Get employee details for EMP-1003. If the employee status is not 'active', update it to 'active'. List all employees and count how many are in STORE-001. If there are more than 2 employees in STORE-001, add new employee Michael Brown as Sales Associate at STORE-002 with email michael.brown@retailpos.com and phone +1-555-210-2002. If EMP-1004 exists and has status 'active', remove employee EMP-1004. List all employees again and check if EMP-1008 exists. If EMP-1008 exists and status is 'active', update employee status for EMP-1008 to 'on_leave'. List all employees to verify final state.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1003"}),
            # if status != 'active':
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1003", "new_status": "active"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="add_employee", kwargs={"name": "Michael Brown", "role": "Sales Associate", "store_id": "STORE-002", "email": "michael.brown@retailpos.com", "phone_number": "+1-555-210-2002"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            # if EMP-1004 exists and status == 'active':
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1004"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            # if EMP-1008 exists and status == 'active':
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "on_leave"}),
            Action(name="list_all_employees", kwargs={})
        ],
        outputs=[
            "Employee details retrieved", "Employee status updated to active", "All employees listed and counted", "Michael Brown added as Sales Associate with current hire date",
            "Employee EMP-1004 details checked", "Employee EMP-1004 removed", "All employees listed again", "Employee EMP-1008 details retrieved", "Employee status updated to on_leave", "Final employee list verified"
        ]
    ),

    # Multi Store Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_022_multi_store_operations",
        instruction="Record a sale for customer CUST-5006 with 3 GROC-ALMBTR500 using credit card. Get total sales for date 2025-06-07. Get customer details for CUST-5006. Get customer loyalty points for CUST-5006. Get customer details for CUST-5001. Update customer loyalty points for CUST-5001 by adding 50 points. List transactions for CUST-5001. Get transaction details for TXN-0001. Update transaction status for TXN-0001 to 'completed'. Get total sales for date 2025-06-08 to compare with previous total.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "credit_card"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-07"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0001", "new_status": "completed"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-08"})
        ],
        outputs=[
            "Almond butter sale recorded", "Daily sales total retrieved", "Customer details retrieved", "Customer loyalty points retrieved", "Customer details retrieved for CUST-5001", "50 points added to customer", "Transactions listed", "Transaction details retrieved", "Transaction status updated to completed", "Sales total retrieved for comparison"
        ]
    ),

    # Sales Performance Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_023_sales_performance_analytics",
        instruction="Get total sales for date 2025-06-08 to assess daily performance. Update customer loyalty points for CUST-5008 by adding 150 points as a performance reward. Get customer details for CUST-5008 to verify their status. Get customer loyalty points for CUST-5008 to check current balance. Get customer details for CUST-5002 to analyze another customer's profile. List transactions for CUST-5002 to understand their purchase history. Get transaction details for TXN-0002 to verify its status. Update transaction status for TXN-0002 to 'completed' to finalize the sale. Get inventory level for ELEC-4KTV55 to assess stock status. Update product stock for ELEC-4KTV55 to 48 to ensure adequate supply. Get total sales for date 2025-06-09 to compare performance and analyze sales trends between the two days.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-08"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5008", "points_to_add": 150}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5008"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 48}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-09"})
        ],
        outputs=[
            "Daily sales performance assessed", "150 points added to customer as performance reward", "Customer details verified", "Customer loyalty points balance checked", "Second customer profile analyzed", "Customer purchase history reviewed", "Transaction details verified for status", "Transaction status updated to completed", "4K TV inventory level assessed", "4K TV stock updated to 48", "Sales comparison and trend analysis completed"
        ]
    ),

    # Multi Product Sales

    Task(
        annotator="lucas",
        user_id="lucas_task_024_multi_product_sales",
        instruction="Get inventory for ELEC-4KTV55. If the current stock is below 20, update it to 15. Get product details for AUDIO-BTSPKR02. If the current price is below $140, update it to $139.99. Get sales analytics for date 2025-06-05. If the sales total is above $1000, update customer loyalty points for CUST-5005 by adding 75 points. Get customer details for CUST-5005. If the customer has less than 400 loyalty points, add 50 more points. List low stock products with threshold 10 to analyze inventory needs.",
        actions=[
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            # if current_stock < 20:
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 15}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            # if current_price < 140:
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 139.99}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            # if sales_total > 1000:
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 75}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5005"}),
            # if customer.loyalty_points < 400:
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 50}),
            Action(name="list_low_stock_products", kwargs={"threshold": 10})
        ],
        outputs=[
            "TV inventory level retrieved", "TV stock updated to 15 (if below 20)", "Speaker product details retrieved",
            "Speaker price updated to $139.99 (if below $140)", "Sales analytics retrieved", "75 points added to customer (if sales > $1000)",
            "Customer details retrieved", "50 more points added (if loyalty < 400)", "Low stock products listed for analysis"
        ]
    ),

    # Cross-Segment Loyalty Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_025_cross_segment_loyalty_optimization",
        instruction="Optimize loyalty and engagement for CUST-5003: update email to loyalty3@email.com, update phone number to +1-555-333-3333, update address to 3 Loyalty Ave, City, ST 12345, update membership to VIP. Record sale for CUST-5003 with 2 AUDIO-BTSPKR02 using debit card, add 100 loyalty points to CUST-5003, update product price for AUDIO-BTSPKR02 to $99.99, get the newest quantity for AUDIO-BTSPKR02",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5003", "new_email": "loyalty3@email.com"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-333-3333"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5003", "new_address": "3 Loyalty Ave, City, ST 12345"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5003", "new_membership_level": "VIP"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 100}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 99.99}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
        ],
        outputs=[
            "'total_quantity': 18"
        ]
    ),

    # Inventory Management Complex
    Task(
        annotator="lucas",
        user_id="lucas_task_026_inventory_complex",
        instruction="Get inventory level for ELEC-4KTV55, check if stock is below 30 and update to 25 only if needed, get product details for ELEC-4KTV55, update product price for ELEC-4KTV55 to $899.99 only if current price is different, get inventory level for AUDIO-BTSPKR02, update product stock for AUDIO-BTSPKR02 to 40 only if current stock is different, record sale for customer CUST-5003 with 1 ELEC-4KTV55 using credit card, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 25}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 899.99}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "TV inventory level retrieved and stock updated to 25 if needed", "TV product details retrieved", "TV price updated to $899.99 if different",
            "Speaker inventory level retrieved and stock updated to 40 if needed", "TV sale recorded", "Daily sales total retrieved"
        ]
    ),

    # Customer Account Management

    Task(
        annotator="lucas",
        user_id="lucas_task_027_customer_account",
        instruction="Get customer details for CUST-5007, update customer address for CUST-5007 to '123 New Street, Updated City, UC 12345', update customer phone number for CUST-5007 to '+1-555-123-4567', get customer loyalty points for CUST-5007, update loyalty points for CUST-5007 by adding 200 points, update membership level for CUST-5007 to 'gold', list transactions for CUST-5007, get transaction details for TXN-0005, and update customer email for CUST-5007 to 'updated.customer@email.com'.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5007", "new_address": "123 New Street, Updated City, UC 12345"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5007", "new_phone_number": "+1-555-123-4567"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5007"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5007", "points_to_add": 200}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5007", "new_membership_level": "gold"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5007"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0005"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5007", "new_email": "updated.customer@email.com"})
        ],
        outputs=[
            "Customer details retrieved", "Address updated to new street", "Phone number updated", "Loyalty points checked",
            "200 points added to customer", "Membership level updated to gold", "Transactions listed", "Transaction details retrieved", "Email updated"
        ]
    ),

    # Multi Store Employee Coordination

    Task(
        annotator="lucas",
        user_id="lucas_task_028_multi_store_employees",
        instruction="Get employee details for EMP-1004, update employee status for EMP-1004 to 'active', add new employee Carlos Rodriguez as Store Manager at STORE-001 with email carlos.rodriguez@retailpos.com and phone +1-555-210-1017, list all employees to verify the addition, get employee details for EMP-1009, update employee status for EMP-1009 to 'on_leave', get employee details for EMP-1011, and update employee status for EMP-1011 to 'active'.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Carlos Rodriguez", "role": "Store Manager", "store_id": "STORE-001", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-1017"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "on_leave"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1011"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1011", "new_status": "active"})
        ],
        outputs=[
            "Employee details for Sarah Johnson retrieved", "Employee status updated to active", "New employee Carlos Rodriguez added", "All employees listed to verify addition",
            "Employee details for Michael Brown retrieved", "Employee status updated to on_leave", "Employee details for Emily Davis retrieved", "Employee status updated to active"
        ]
    ),

    # Complex Sales Transaction

    Task(
        annotator="lucas",
        user_id="lucas_task_029_customer_service_workflow",
        instruction="Get customer details for CUST-5012, list transactions for CUST-5012, get transaction details for TXN-0012, update transaction status for TXN-0012 to 'refunded', update customer loyalty points for CUST-5012 by adding 50 points, update customer membership level for CUST-5012 to 'silver', update customer email for CUST-5012 to 'service.customer@email.com', get customer details for CUST-5012 again, and update customer phone number for CUST-5012 to '+1-555-999-8888'.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0012", "new_status": "refunded"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 50}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5012", "new_email": "service.customer@email.com"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-999-8888"})
        ],
        outputs=[
            "Customer details retrieved", "Transactions listed", "Transaction details retrieved", "Transaction status updated to refunded",
            "50 points added to customer", "Membership level updated to silver", "Email updated", "Updated customer details retrieved", "Phone number updated"
        ]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_030_advanced_customer",
        instruction="Get customer details for CUST-5001, update customer address for CUST-5001 to '456 Advanced Street, Customer City, CC 45678', update customer phone number for CUST-5001 to '+1-555-456-7890', get customer loyalty points for CUST-5001, update loyalty points for CUST-5001 by adding 400 points, update membership level for CUST-5001 to 'platinum', list transactions for CUST-5001, get transaction details for TXN-0001, and update customer email for CUST-5001 to 'advanced.customer@email.com'.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5001", "new_address": "456 Advanced Street, Customer City, CC 45678"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-456-7890"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 400}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5001", "new_email": "advanced.customer@email.com"})
        ],
        outputs=[
            "Customer details retrieved", "Address updated to advanced street", "Phone number updated", "Loyalty points checked",
            "400 points added to customer", "Membership level updated to platinum", "Transactions listed", "Transaction details retrieved", "Email updated to advanced customer"
        ]
    ),

    # Inventory Optimization
    Task(
        annotator="lucas",
        user_id="lucas_task_031_inventory_optimization",
        instruction="List low stock products with threshold 35, get inventory level for CLTH-SLFJEAN34, update product stock for CLTH-SLFJEAN34 to 60, get product details for CLTH-SLFJEAN34, update product price for CLTH-SLFJEAN34 to $89.99, get inventory level for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 50, list products by category 'Sports & Outdoors', and record sale for customer CUST-5010 with 1 CLTH-SLFJEAN34 using cash.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 35}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 60}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_price", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 89.99}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 50}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5010", "items": [{"sku": "CLTH-SLFJEAN34", "quantity": 1}], "payment_method": "cash"})
        ],
        outputs=[
            "Low stock products listed", "Jeans inventory retrieved", "Jeans stock updated to 60", "Jeans details retrieved",
            "Jeans price updated to $89.99", "Chef knife inventory retrieved", "Chef knife stock updated to 50", "Sports & Outdoors products listed", "Jeans sale recorded for CUST-5010"
        ]
    ),

    # Employee Training Program

    Task(
        annotator="lucas",
        user_id="lucas_task_032_employee_training",
        instruction="Get employee details for EMP-1032, update employee status for EMP-1032 to 'training', add new employee Lisa Martinez as Trainer at STORE-005 with email lisa.martinez@retailpos.com and phone +1-555-210-2007, get employee details for EMP-1034, update employee status for EMP-1034 to 'certified', list all employees, remove employee EMP-1015, list all employees again, and get employee details for EMP-1020.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1032"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1032", "new_status": "training"}),
            Action(name="add_employee", kwargs={"name": "Lisa Martinez", "role": "Trainer", "store_id": "STORE-005", "email": "lisa.martinez@retailpos.com", "phone_number": "+1-555-210-2007"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1034"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1034", "new_status": "certified"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1015"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[
            "Employee details retrieved", "Employee status updated to training", "Lisa Martinez added as Trainer", "Second employee details retrieved",
            "Second employee status updated to certified", "All employees listed", "Employee removed", "All employees listed again", "Henry Adams details retrieved"
        ]
    ),

    # Multi Category Sales Analysis

    Task(
        annotator="lucas",
        user_id="lucas_task_033_customer_loyalty_enhancement",
        instruction="Get customer details for CUST-5012, get customer loyalty points for CUST-5012, update loyalty points for CUST-5012 by adding 250 points, update membership level for CUST-5012 to 'gold', update customer email for CUST-5012 to 'loyalty.customer@email.com', list transactions for CUST-5012, get transaction details for TXN-0001, update transaction status for TXN-0001 to 'completed', and record sale for CUST-5012 with 1 GROC-ALMBTR500 using debit card.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5012"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 250}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "gold"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5012", "new_email": "loyalty.customer@email.com"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0001", "new_status": "completed"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "GROC-ALMBTR500", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[
            "Customer details retrieved", "Loyalty points checked", "250 points added to customer", "Membership level updated to gold",
            "Email updated to loyalty customer", "Transactions listed", "Transaction details retrieved", "Transaction status updated to completed", "Book sale recorded"
        ]
    ),

    # Comprehensive Store Audit
    Task(
        annotator="lucas",
        user_id="lucas_task_034_comprehensive_audit",
        instruction="List all employees, get employee details for EMP-1002, update employee status for EMP-1002 to 'audited', list all products with limit 50 (within policy limit), get inventory level for HOM-COFMKR12, update product stock for HOM-COFMKR12 to 80, get product details for HOM-COFMKR12, update product price for HOM-COFMKR12 to $24.99, get total sales for date 2025-06-05, get customer details for CUST-5001, and get product details for ELEC-4KTV55.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "audited"}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 80}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 24.99}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to audited", "All products listed within policy limit",
            "Coffee maker inventory retrieved", "Coffee maker stock updated to 80", "Coffee maker details retrieved", "Coffee maker price updated to $24.99", "Daily sales total retrieved", "Customer details retrieved", "TV details retrieved"
        ]
    ),

    # Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_035_customer_relationship",
        instruction="Get customer details for CUST-5002, update customer address for CUST-5002 to '789 Relationship Street, Customer City, RC 78901', update customer phone number for CUST-5002 to '+1-555-789-0123', get customer loyalty points for CUST-5002, update loyalty points for CUST-5002 by adding 350 points, update membership level for CUST-5002 to 'platinum', list transactions for CUST-5002, and record sale for CUST-5002 with 1 ELEC-4KTV55 using credit card.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5002", "new_address": "789 Relationship Street, Customer City, RC 78901"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5002", "new_phone_number": "+1-555-789-0123"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 350}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5002", "new_membership_level": "platinum"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"})
        ],
        outputs=[
            "Customer details retrieved", "Address updated to relationship street", "Phone number updated", "Loyalty points checked",
            "350 points added to customer", "Membership level updated to platinum", "Transactions listed", "TV sale recorded"
        ]
    ),

    # Inventory Rebalancing Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_036_inventory_rebalancing",
        instruction="List low stock products with threshold 40, get inventory level for AUDIO-BTSPKR02, update product stock for AUDIO-BTSPKR02 to 60, get product details for AUDIO-BTSPKR02, update product price for AUDIO-BTSPKR02 to $189.99, get inventory level for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 45, and record sale for customer CUST-5010 with 1 AUDIO-BTSPKR02 using debit card.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 40}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 60}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 189.99}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 45}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5010", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[
            "Low stock products listed", "Speaker inventory retrieved", "Speaker stock updated to 60", "Speaker details retrieved",
            "Speaker price updated to $189.99", "Chef knife inventory retrieved", "Chef knife stock updated to 45", "Speaker sale recorded"
        ]
    ),

    # Customer Data Migration

    Task(
        annotator="lucas",
        user_id="lucas_task_037_customer_migration",
        instruction="Execute comprehensive customer data migration for CUST-5003: get customer details, update email to migrated.customer@newdomain.com, update address to 456 Migration Street, New City, NC 45678, update phone to +1-555-456-7890, get loyalty points, add 75 points if below 1000, update membership to silver, list transactions, get transaction details for TXN-0003, list transactions by customer, get customer details again, get customer loyalty points again, and verify all migration updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5003", "new_email": "migrated.customer@newdomain.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5003", "new_address": "456 Migration Street, New City, NC 45678"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-456-7890"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 75}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5003", "new_membership_level": "silver"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5003"})
        ],
        outputs=[
            "Customer details retrieved for migration", "Email updated to new domain", "Address updated to migration street", "Phone number updated for migration",
            "Loyalty points checked for migration", "75 points added to customer for migration", "Membership level updated to silver for migration", "Transactions listed for migration", "Transaction details retrieved for migration", "Email updated to new domain", "Address updated to migration street", "Phone number updated for migration", "75 points added to customer for migration", "Membership level updated to silver for migration", "Transactions listed for migration", "Updated customer details retrieved for migration", "Updated loyalty points retrieved for migration"
        ]
    ),

    # Staff Reorganization Management

    Task(
        annotator="lucas",
        user_id="lucas_task_038_staff_reorganization",
        instruction="Get employee details for EMP-1008, update employee status for EMP-1008 to 'active', add new employee Maria Garcia as Senior Sales Associate at STORE-001 with email maria.garcia@retailpos.com and phone +1-555-210-1019, list all employees to verify the addition, get employee details for EMP-1011, update employee status for EMP-1011 to 'promoted', get employee details for EMP-1015, and update employee status for EMP-1015 to 'active'.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Maria Garcia", "role": "Senior Sales Associate", "store_id": "STORE-001", "email": "maria.garcia@retailpos.com", "phone_number": "+1-555-210-1019"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1011"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1011", "new_status": "promoted"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1015", "new_status": "active"})
        ],
        outputs=[
            "Employee details for Lisa Martinez retrieved", "Employee status updated to active", "New employee Maria Garcia added", "All employees listed to verify addition",
            "Employee details for Carlos Rodriguez retrieved", "Employee status updated to promoted", "Employee details for Patricia Davis retrieved", "Employee status updated to active"
        ]
    ),

    # Complex Return Processing

    Task(
        annotator="lucas",
        user_id="lucas_task_039_complex_return",
        instruction="Get customer details for CUST-5011, list transactions for CUST-5011, get transaction details for TXN-0011, update transaction status for TXN-0011 to 'refunded', update customer loyalty points for CUST-5011 by adding 50 points, update customer membership level for CUST-5011 to 'silver', update customer email for CUST-5011 to 'return.customer@email.com', get customer details for CUST-5011 again, and update customer phone number for CUST-5011 to '+1-555-777-6666'.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5011"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5011"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0011"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0011", "new_status": "refunded"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 50}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5011", "new_membership_level": "silver"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5011", "new_email": "return.customer@email.com"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5011"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5011", "new_phone_number": "+1-555-777-6666"})
        ],
        outputs=[
            "Customer details retrieved", "Transactions listed", "Transaction details retrieved", "Transaction status updated to refunded",
            "50 points added to customer", "Membership level updated to silver", "Email updated to return customer", "Final customer details retrieved", "Phone number updated"
        ]
    ),

       # Product Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_040_product_expansion",
        instruction="List products by category 'Home & Kitchen' to analyze current inventory. Since there are more than 3 products in the category, analyze customer data and sales performance instead. Get customer details for CUST-5001 and CUST-5002, update customer loyalty points for CUST-5001 by adding 50 points, update customer loyalty points for CUST-5002 by adding 75 points, list transactions for both customers, get transaction details for TXN-0001 and TXN-0002, and get total sales for date 2025-06-05 and 2025-06-06 to analyze performance.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 75}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"})
        ],
        outputs=[
            "Home & Kitchen products analyzed for expansion opportunity", "Customer details retrieved for CUST-5001", "Customer details retrieved for CUST-5002", "Customer loyalty points updated by 50 for CUST-5001", "Customer loyalty points updated by 75 for CUST-5002", "Customer transactions listed for CUST-5001", "Customer transactions listed for CUST-5002", "Transaction details retrieved for TXN-0001", "Transaction details retrieved for TXN-0002", "Daily sales total retrieved for 2025-06-05", "Daily sales total retrieved for 2025-06-06"
        ]
    ),

     # Seasonal Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_041_seasonal_inventory",
        instruction="List low stock products with threshold 45, get inventory level for SPORT-BIKHLM01, update product stock for SPORT-BIKHLM01 to 75, get product details for SPORT-BIKHLM01, update product price for SPORT-BIKHLM01 to $69.99, get inventory level for CLTH-SLFJEAN34, update product stock for CLTH-SLFJEAN34 to 55, and record sale for customer CUST-5011 with 1 SPORT-BIKHLM01 using debit card.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 45}),
            Action(name="get_inventory_level", kwargs={"sku": "SPORT-BIKHLM01"}),
            Action(name="update_product_stock", kwargs={"sku": "SPORT-BIKHLM01", "new_stock_quantity": 75}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "SPORT-BIKHLM01"}),
            Action(name="update_product_price", kwargs={"sku": "SPORT-BIKHLM01", "new_price": 69.99}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 55}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5011", "items": [{"sku": "SPORT-BIKHLM01", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[
            "Low stock products listed", "Bike helmet inventory retrieved", "Bike helmet stock updated to 75", "Bike helmet details retrieved",
            "Bike helmet price updated to $69.99", "Jeans inventory retrieved", "Jeans stock updated to 55", "Bike helmet sale recorded"
        ]
    ),

    # Employee Performance Review
    Task(
        annotator="lucas",
        user_id="lucas_task_042_performance_review",
        instruction="Get employee details for EMP-1008. Update employee status for EMP-1008 to 'under_review'. Get employee details for EMP-1009. Update employee status for EMP-1009 to 'excellent'. Add Carlos Rodriguez as Performance Analyst at STORE-003 with email carlos.rodriguez@retailpos.com and phone +1-555-210-1017. List all employees to verify the workforce. Get employee details for EMP-1032. Update employee status for EMP-1032 to 'on_leave'. List all employees again to verify changes. Get employee details for EMP-1020 for final review.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "under_review"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "excellent"}),
            Action(name="add_employee", kwargs={"name": "Carlos Rodriguez", "role": "Performance Analyst", "store_id": "STORE-003", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-1017"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1032"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1032", "new_status": "on_leave"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[
            "First employee details retrieved", "First employee status updated to under review", "Second employee details retrieved", "Second employee status updated to excellent",
            "Carlos Rodriguez added as Performance Analyst with specified contact info", "All employees listed to verify workforce", "Employee details retrieved", "Employee status updated to on_leave", "All employees listed again to verify changes", "Henry Adams details retrieved for final review"
        ]
    ),

    # Cross Category Sales Campaign

    Task(
        annotator="lucas",
        user_id="lucas_task_043_cross_category_campaign",
        instruction="List products by category 'Electronics', list products by category 'Grocery', get product details for GROC-ALMBTR500, update product price for GROC-ALMBTR500 to $9.99, get inventory level for GROC-ALMBTR500, update product stock for GROC-ALMBTR500 to 85, record sale for customer CUST-5009 with 1 ELEC-4KTV55 and 3 GROC-ALMBTR500 using credit card, update customer loyalty points for CUST-5009 by adding 175 points, and get customer details for CUST-5009.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_price", kwargs={"sku": "GROC-ALMBTR500", "new_price": 9.99}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 85}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "credit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 175}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5009"})
        ],
        outputs=[
            "Electronics products listed", "Grocery products listed", "Almond butter details retrieved", "Almond butter price updated to $9.99",
            "Almond butter inventory retrieved", "Almond butter stock updated to 85", "Cross-category sale recorded", "175 points added to customer", "Customer details retrieved"
        ]
    ),

    # Employee Management

    Task(
        annotator="lucas",
        user_id="lucas_task_044_product_distribution",
        instruction="List products by category 'Sports & Outdoors', get inventory level for CLTH-SLFJEAN34, update product stock for CLTH-SLFJEAN34 to 45, get product details for CLTH-SLFJEAN34, update product price for CLTH-SLFJEAN34 to $94.99, add new product 'Sports Water Bottle' in Sports & Outdoors category with description 'Insulated stainless steel water bottle' and price $19.99 and stock quantity 50, list products by category 'Sports & Outdoors' again to verify the addition, and get inventory level for SPORT-BIKHLM01 to verify existing product stock.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 45}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_price", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 94.99}),
            Action(name="add_new_product", kwargs={"name": "Sports Water Bottle", "description": "Insulated stainless steel water bottle", "category": "Sports & Outdoors", "price": 19.99, "stock_quantity": 50}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_inventory_level", kwargs={"sku": "SPORT-BIKHLM01"})
        ],
        outputs=[
            "Sports & Outdoors products listed", "Jeans inventory retrieved", "Jeans stock updated to 45", "Jeans details retrieved",
            "Jeans price updated to $94.99", "Sports water bottle added", "Sports & Outdoors products listed again to verify addition", "Bike helmet inventory retrieved to verify existing product stock"
        ]
    ),

    # Advanced Transaction Management

    Task(
        annotator="lucas",
        user_id="lucas_task_045_transaction_management",
        instruction="Get customer details for CUST-5012, list transactions for CUST-5012, get transaction details for TXN-0001, update transaction status for TXN-0001 to 'pending', list transactions for CUST-5012 again, get transaction details for TXN-0012, update customer loyalty points for CUST-5012 by adding 60 points, get customer details for CUST-5012 again, get customer loyalty points for CUST-5012 to verify the update, list low stock products with threshold 30, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0001", "new_status": "pending"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 60}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5012"}),
            Action(name="list_low_stock_products", kwargs={"threshold": 30}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Customer details retrieved", "Transactions listed", "Transaction details retrieved", "Transaction status updated to pending",
            "Updated transactions listed", "Transaction details retrieved for TXN-0012", "60 points added to customer", "Updated customer details retrieved", "Customer loyalty points verified", "Low stock products listed", "Daily sales total retrieved"
        ]
    ),
    # Comprehensive Business Intelligence

    Task(
        annotator="lucas",
        user_id="lucas_task_046_business_intelligence",
        instruction="List all employees, list all products with limit 50 (within policy limit), list low stock products with threshold 70, get total sales for date 2025-06-05, get customer details for CUST-5001, get customer details for CUST-5002. Update customer loyalty points for CUST-5001 by adding 150 points. Update customer loyalty points for CUST-5002 by adding 100 points. Get total sales for date 2025-06-05 again to compare with initial total. Get customer loyalty points for CUST-5001. Get product details for ELEC-4KTV55 and update customer loyalty points for CUST-5002 by adding 200 points.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="list_low_stock_products", kwargs={"threshold": 70}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 150}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 100}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 200})
        ],
        outputs=[
            "All employees listed", "All products listed within policy limit of 50", "Low stock products listed", "Initial sales total retrieved",
            "First customer details retrieved", "Second customer details retrieved", "150 points added to first customer", "100 points added to second customer", "Final sales total retrieved for comparison", "Customer loyalty points checked", "Product details retrieved", "200 points added to second customer"
        ]
    ),

    # Strategic Resource Reallocation

    Task(
        annotator="lucas",
        user_id="lucas_task_047_strategic_reallocation",
        instruction="List all employees, get employee details for EMP-1008, update employee status for EMP-1008 to 'promoted', add new employee David Wilson as Strategic Analyst at STORE-001 with email david.wilson@retailpos.com and phone +1-555-210-1020, list all employees to verify the addition, get employee details for EMP-1011, update employee status for EMP-1011 to 'active' only if not already active, update employee status for EMP-1015 to 'terminated' only if currently active, and get employee details for EMP-1020 to verify the final state.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="add_employee", kwargs={"name": "David Wilson", "role": "Strategic Analyst", "store_id": "STORE-001", "email": "david.wilson@retailpos.com", "phone_number": "+1-555-210-1020"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1011"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1011", "new_status": "active"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1015", "new_status": "terminated"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[
            "All employees listed", "Employee details for Lisa Martinez retrieved", "Employee status updated to promoted", "New employee David Wilson added",
            "All employees listed to verify addition", "Employee details for Carlos Rodriguez retrieved", "Employee status updated to active (if not already active)", "Employee details for Patricia Davis retrieved", "Employee status updated to terminated (if currently active)",
            "Final employee details retrieved"
        ]
    ),

    # Customer Journey Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_048_customer_journey",
        instruction="Get customer details for CUST-5004, update customer email for CUST-5004 to 'journey.customer@optimized.com', update customer address for CUST-5004 to '789 Journey Lane, Optimized City, OC 78901', get customer loyalty points for CUST-5004, update loyalty points for CUST-5004 by adding 400 points, update membership level for CUST-5004 to 'platinum', record sale for customer CUST-5004 with 1 ELEC-4KTV55 using debit card, list transactions for CUST-5004, and get customer details for CUST-5004 again.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5004"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5004", "new_email": "journey.customer@optimized.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5004", "new_address": "789 Journey Lane, Optimized City, OC 78901"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5004"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5004", "points_to_add": 400}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5004", "new_membership_level": "platinum"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[
            "Customer details retrieved", "Email updated to journey customer", "Address updated to journey lane", "Loyalty points checked",
            "400 points added to customer", "Membership level updated to platinum", "Gaming laptop sale recorded", "Transactions listed", "Updated customer details retrieved"
        ]
    ),

    # Workforce Development Program

    Task(
        annotator="lucas",
        user_id="lucas_task_049_workforce_development",
        instruction="Get employee details for EMP-1015. Update employee status for EMP-1015 to 'active'. Add new employee Jennifer Garcia as Training Coordinator at STORE-001 with email jennifer.garcia@retailpos.com and phone +1-555-210-1018. List all employees to verify the addition. Get employee details for EMP-1020. Update employee status for EMP-1020 to 'certified'. Get employee details for EMP-1032. Update employee status for EMP-1032 to 'active'.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1015", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Jennifer Garcia", "role": "Training Coordinator", "store_id": "STORE-001", "email": "jennifer.garcia@retailpos.com", "phone_number": "+1-555-210-1018"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1020", "new_status": "certified"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1032"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1032", "new_status": "active"})
        ],
        outputs=[
            "Employee details for Maria Garcia retrieved", "Employee status updated to active", "New employee Jennifer Garcia added with specified contact info", "All employees listed to verify addition",
            "Employee details for David Wilson retrieved", "Employee status updated to certified", "Employee details for Jennifer Garcia retrieved", "Employee status updated to active"
        ]
    ),

    # Advanced Return Processing
    Task(
        annotator="lucas",
        user_id="lucas_task_050_advanced_return",
        instruction="Execute comprehensive advanced return processing for transaction TXN-0012: get transaction details, get customer details for CUST-5012, list transactions by customer, process return if within 90 days with reason 'Customer return', update transaction status to refunded, update customer membership level to silver, update customer phone number to +1-555-555-4444, update customer loyalty points by adding 50, get customer details again, get customer loyalty points, update customer email to return.customer@email.com, update customer address to 789 Return Street, Return City, RC 78901, list transactions by customer again, get transaction details again, update customer membership level to silver, update customer loyalty points by adding 25 more points, and verify all return processing updates.",
        actions=[
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="process_return", kwargs={"original_transaction_id": "TXN-0012", "items_to_return": [{"sku": "SPORT-BIKHLM01", "quantity": 1}], "reason": "Customer return"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0012", "new_status": "refunded"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-555-4444"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 50}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5012"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5012", "new_email": "return.customer@email.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5012", "new_address": "789 Return Street, Return City, RC 78901"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 25})
        ],
        outputs=[
            "Return processed for advanced customer", "Transaction status updated to refunded", "Membership level updated to silver", "Phone number updated for return", "50 points added to customer for return", "Final customer details retrieved for return", "Customer loyalty points checked for return", "Email updated for return customer", "Address updated for return customer", "Transactions listed again for return", "Transaction details retrieved again for return", "Membership level updated to silver for return", "25 additional points added to customer for return"
        ]
    ),

    # Product Innovation Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_051_customer_lifecycle",
        instruction="Execute comprehensive customer lifecycle management for CUST-5007 and CUST-5008: get customer details for CUST-5007, update membership level to platinum, get loyalty points for CUST-5007, add 500 points if below 1000, update phone number to +1-555-444-3333, get customer details for CUST-5008, update membership level to gold, record sale for CUST-5007 with 1 ELEC-4KTV55 using credit card, list transactions for CUST-5007, get transaction details for TXN-0007, update customer email for CUST-5007 to lifecycle.customer@email.com, update customer address for CUST-5007 to 456 Lifecycle Ave, Lifecycle City, LC 45678, update customer loyalty points for CUST-5007 by adding 100 more points, update customer membership level for CUST-5008 to gold, get customer details for CUST-5007 again, and verify all lifecycle updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5007", "new_membership_level": "platinum"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5007"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5007", "points_to_add": 500}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5007", "new_phone_number": "+1-555-444-3333"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5007"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0007"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5007", "new_email": "lifecycle.customer@email.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5007", "new_address": "456 Lifecycle Ave, Lifecycle City, LC 45678"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5007", "points_to_add": 100}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"})
        ],
        outputs=[
            "First customer details retrieved for lifecycle", "First customer membership updated to platinum for lifecycle", "First customer loyalty points checked for lifecycle", "500 points added to first customer for lifecycle",
            "First customer phone number updated for lifecycle", "Second customer details retrieved for lifecycle", "Second customer membership updated to gold for lifecycle", "TV sale recorded for first customer for lifecycle", "First customer transactions listed for lifecycle", "Transaction details retrieved for lifecycle", "Email updated for lifecycle customer", "Address updated for lifecycle customer", "100 additional points added to first customer for lifecycle", "Second customer membership updated to gold for lifecycle", "Updated first customer details retrieved for lifecycle"
        ]
    ),

    # Supply Chain Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_052_supply_chain",
        instruction="List all products with limit 50, get product details for ELEC-4KTV55, update product price for ELEC-4KTV55 to $799.99, get inventory level for ELEC-4KTV55, update product stock for ELEC-4KTV55 to 45, add new product 'Smart Thermostat' in Electronics category with description 'WiFi-enabled smart thermostat with energy saving features' and price $199.99 and stock quantity 25, and get product details for the newly added Smart Thermostat.",
        actions=[
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 799.99}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 45}),
            Action(name="add_new_product", kwargs={"name": "Smart Thermostat", "description": "WiFi-enabled smart thermostat with energy saving features", "category": "Electronics", "price": 199.99, "stock_quantity": 25}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-0006"})
        ],
        outputs=[
            "All products listed", "TV details retrieved", "TV price updated to $799.99", "TV inventory retrieved",
            "TV stock updated to 45", "Smart thermostat added with unique SKU", "Smart thermostat details retrieved"
        ]
    ),

    # Employee Excellence Program

    Task(
        annotator="lucas",
        user_id="lucas_task_053_employee_excellence",
        instruction="Get employee details for EMP-1009, update employee status for EMP-1009 to 'excellence_program', get employee details for EMP-1008, update employee status for EMP-1008 to 'top_performer', add new employee Patricia Davis as Excellence Coach at STORE-001 with email patricia.davis@retailpos.com and phone +1-555-210-1019, list all employees, remove employee EMP-1009, list all employees again, and get employee details for EMP-1020.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "excellence_program"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "top_performer"}),
            Action(name="add_employee", kwargs={"name": "Patricia Davis", "role": "Excellence Coach", "store_id": "STORE-001", "email": "patricia.davis@retailpos.com", "phone_number": "+1-555-210-1019"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1009"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[
            "First employee details retrieved", "First employee status updated to excellence program", "Second employee details retrieved", "Second employee status updated to top performer",
            "Patricia Davis added as Excellence Coach with specified contact info", "All employees listed", "Employee removed", "All employees listed again", "Henry Adams details retrieved"
        ]
    ),

    # Market Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_054_market_expansion",
        instruction="Get customer details for CUST-5009. Update membership level for CUST-5009 to 'platinum'. Update customer loyalty points for CUST-5009 by adding 400 points. Update customer email for CUST-5009 to 'expansion.customer@market.com'. Update customer address for CUST-5009 to '789 Expansion Blvd, Market City, MC 78901'. List transactions for CUST-5009. Get transaction details for TXN-0009. Get customer loyalty points for CUST-5009. Update customer loyalty points for CUST-5009 by adding 100 more points. Get customer details for CUST-5009 again to verify all updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5009"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5009", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 400}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5009", "new_email": "expansion.customer@market.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5009", "new_address": "789 Expansion Blvd, Market City, MC 78901"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5009"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0009"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5009"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 100}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5009"})
        ],
        outputs=[
            "Customer details retrieved", "Membership level updated to platinum", "400 points added to customer", "Email updated to expansion customer",
            "Address updated to expansion blvd", "Transactions listed", "Transaction details retrieved", "Customer loyalty points checked", "Additional 100 points added", "Updated customer details retrieved"
        ]
    ),



    # Customer Experience Enhancement

    Task(
        annotator="lucas",
        user_id="lucas_task_055_customer_experience",
        instruction="Get customer details for CUST-5008, update customer email for CUST-5008 to 'experience.customer@enhanced.com', update customer address for CUST-5008 to '456 Experience Street, Enhanced City, EC 45678', get customer loyalty points for CUST-5008, update loyalty points for CUST-5008 by adding 350 points, update membership level for CUST-5008 to 'gold', record sale for CUST-5008 with 1 AUDIO-BTSPKR02 using debit card, list transactions for CUST-5008, and get customer details for CUST-5008 again.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5008", "new_email": "experience.customer@enhanced.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5008", "new_address": "456 Experience Street, Enhanced City, EC 45678"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5008"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5008", "points_to_add": 350}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5008", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5008"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"})
        ],
        outputs=[
            "Customer details retrieved", "Email updated to experience customer", "Address updated to experience street", "Loyalty points checked",
            "350 points added to customer", "Membership level updated to gold", "Speaker sale recorded", "Transactions listed", "Updated customer details retrieved"
        ]
    ),

    # Operational Excellence Audit

    Task(
        annotator="lucas",
        user_id="lucas_task_056_relationship_excellence",
        instruction="Get customer details for CUST-5011, get customer loyalty points for CUST-5011, update loyalty points for CUST-5011 by adding 600 points, update membership level for CUST-5011 to 'platinum', update customer address for CUST-5011 to '321 Excellence Drive, Relationship City, RC 32100', update customer email for CUST-5011 to 'excellence.customer@relationship.com', update customer phone number for CUST-5011 to '+1-555-333-2222', and get customer details for CUST-5011 again.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5011"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5011"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 600}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5011", "new_membership_level": "platinum"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5011", "new_address": "321 Excellence Drive, Relationship City, RC 32100"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5011", "new_email": "excellence.customer@relationship.com"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5011", "new_phone_number": "+1-555-333-2222"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[
            "Customer details retrieved", "Loyalty points checked", "600 points added to customer", "Membership level updated to platinum",
            "Address updated to excellence drive", "Email updated to excellence customer", "Phone number updated", "Updated customer details retrieved"
        ]
    ),



    # Comprehensive Business Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_057_business_analytics",
        instruction="Get total sales for date 2025-06-05, list all employees, list all products with limit 50 (within policy limit), get customer details for CUST-5001, get customer details for CUST-5005, update customer membership level for CUST-5001 to 'platinum', update customer membership level for CUST-5005 to 'gold', get total sales for date 2025-06-05 again, list low stock products with threshold 50, get customer loyalty points for CUST-5001 to verify the update, get product details for ELEC-4KTV55, and update customer loyalty points for CUST-5005 by adding 150 points.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5005"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5005", "new_membership_level": "gold"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="list_low_stock_products", kwargs={"threshold": 50}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 150})
        ],
        outputs=[
            "Initial sales total retrieved", "All employees listed", "All products listed within policy limit of 50", "First customer details retrieved",
            "Second customer details retrieved", "First customer membership updated to platinum", "Second customer membership updated to gold", "Final sales total retrieved", "Low stock products listed", "First customer loyalty points verified", "TV details retrieved", "150 points added to second customer"
        ]
    ),

    # Strategic Portfolio Management
    Task(
        annotator="lucas",
        user_id="lucas_task_058_product_expansion",
        instruction="List products by category 'Home & Kitchen', add new product 'Smart Coffee Maker' in Home & Kitchen category with description 'Programmable coffee maker with smartphone control' and price $199.99 and stock quantity 25, get product details for the newly added Smart Coffee Maker (HOME-0006), update product stock for HOME-0006 to 25, list all products with limit 50 (within policy limit), update customer loyalty points for CUST-5005 by adding 200 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="add_new_product", kwargs={"name": "Smart Coffee Maker", "description": "Programmable coffee maker with smartphone control", "category": "Home & Kitchen", "price": 199.99, "stock_quantity": 25}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOME-0006"}),
            Action(name="update_product_stock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 25}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 200}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Home & Kitchen products listed", "Smart coffee maker added with unique SKU", "Smart coffee maker details retrieved", "Smart coffee maker stock updated to 25",
            "All products listed within policy limit", "200 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Premium Customer Onboarding

    Task(
        annotator="lucas",
        user_id="lucas_task_059_product_innovation",
        instruction="List products by category 'Electronics', add new product 'Smart Watch Pro' in Electronics category with description 'Advanced fitness tracking smartwatch with GPS' and price $299.99 and stock quantity 30, get product details for the newly added Smart Watch Pro, update product stock for the newly added Smart Watch Pro to 30, list all products with limit 50, update customer loyalty points for CUST-5006 by adding 300 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="add_new_product", kwargs={"name": "Smart Watch Pro", "description": "Advanced fitness tracking smartwatch with GPS", "category": "Electronics", "price": 299.99, "stock_quantity": 30}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-0006"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 30}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 300}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics products listed", "Smart watch pro added with unique SKU", "Smart watch pro details retrieved", "Smart watch pro stock updated to 30",
            "All products listed within limit", "300 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Supply Chain Optimization
    Task(
        annotator="lucas",
        user_id="lucas_task_060_innovation_growth",
        instruction="List products by category 'Sports & Outdoors', add new product 'Fitness Tracker Pro' in Sports & Outdoors category with description 'Advanced fitness tracking device with heart rate monitor' and price $149.99 and stock quantity 40, get product details for the newly added Fitness Tracker Pro, update product stock for the newly added Fitness Tracker Pro to 40, update product stock for the newly added Fitness Tracker Pro to 55, list all products with limit 50, update customer loyalty points for CUST-5012 by adding 250 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="add_new_product", kwargs={"name": "Fitness Tracker Pro", "description": "Advanced fitness tracking device with heart rate monitor", "category": "Sports & Outdoors", "price": 149.99, "stock_quantity": 40}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "SPOR-0003"}),
            Action(name="update_product_stock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 55}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 250}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Sports products listed", "Fitness tracker pro added with unique SKU", "Fitness tracker pro details retrieved", "Fitness tracker pro stock updated to 40",
            "Fitness tracker pro stock updated to 55", "All products listed within limit", "250 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Strategic Customer Portfolio

    Task(
        annotator="lucas",
        user_id="lucas_task_061_employee_performance",
        instruction="Get employee details for EMP-1002, check if EMP-1002 is currently active, list all employees to verify current count, add new employee Jennifer Davis as Manager at STORE-001 with email jennifer.davis@retailpos.com and phone +1-555-210-2003 (assign ID EMP-1013), get employee details for EMP-1004 and check if they are on leave, update employee status for EMP-1004 to 'on_leave' only if not already on leave, remove employee EMP-1003 only if they exist, list all employees again to verify changes, and get employee details for EMP-1008 to confirm final state.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="add_employee", kwargs={"name": "Jennifer Davis", "role": "Manager", "store_id": "STORE-001", "email": "jennifer.davis@retailpos.com", "phone_number": "+1-555-210-2003"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "on_leave"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"})
        ],
        outputs=[
            "Employee details retrieved", "Employee status rechecked", "All employees listed to verify count", "Jennifer Davis added as Manager with ID EMP-1013",
            "Employee status rechecked", "Employee status rechecked again", "Second employee details retrieved", "Second employee status updated to on_leave", "Employee removed", "All employees listed again to verify changes", "Final employee details retrieved"
        ]
    ),

    # Multi Store Employee Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_062_product_expansion",
        instruction="Analyze current inventory levels for Electronics category, then add new product 'Smart Home Hub' in Electronics category with description 'Centralized smart home control system with voice assistant' and price $399.99 and stock quantity 15, get product details for the newly added Smart Home Hub (ELEC-0006), update product stock for ELEC-0006 to 20, list all products with limit 50 (within policy limit), update customer loyalty points for CUST-5007 by adding 350 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="add_new_product", kwargs={"name": "Smart Home Hub", "description": "Centralized smart home control system with voice assistant", "category": "Electronics", "price": 399.99, "stock_quantity": 15}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-0006"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 20}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5007", "points_to_add": 350}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics products analyzed", "Smart home hub added with unique SKU", "Smart home hub details retrieved", "Smart home hub stock updated to 20", "All products listed within policy limit", "350 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Seasonal Inventory Adjustment

    Task(
        annotator="lucas",
        user_id="lucas_task_063_product_innovation",
        instruction="Review current inventory levels for Sports & Outdoors category, then add new product 'Premium Yoga Mat' in Sports & Outdoors category with description 'Non-slip premium yoga mat with alignment lines and carrying strap' and price $89.99 and stock quantity 40, get product details for the newly added Premium Yoga Mat (SPOR-0003), update product stock for SPOR-0003 to 45, list all products with limit 50, update customer loyalty points for CUST-5008 by adding 150 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="add_new_product", kwargs={"name": "Premium Yoga Mat", "description": "Non-slip premium yoga mat with alignment lines and carrying strap", "category": "Sports & Outdoors", "price": 89.99, "stock_quantity": 40}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "SPOR-0003"}),
            Action(name="update_product_stock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 45}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5008", "points_to_add": 150}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Sports & Outdoors products reviewed", "Premium yoga mat added with unique SKU", "Premium yoga mat details retrieved", "Premium yoga mat stock updated to 45", "All products listed within limit", "150 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Supply Chain Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_064_innovation_growth",
        instruction="Evaluate current inventory levels for Home & Kitchen category, then add new product 'Smart Refrigerator' in Home & Kitchen category with description 'WiFi-enabled refrigerator with touchscreen and inventory tracking' and price $1299.99 and stock quantity 8, get product details for the newly added Smart Refrigerator (HOME-0006), update product stock for HOME-0006 to 10, update product stock for HOME-0006 to 12, list all products with limit 50, update customer loyalty points for CUST-5010 by adding 500 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="add_new_product", kwargs={"name": "Smart Refrigerator", "description": "WiFi-enabled refrigerator with touchscreen and inventory tracking", "category": "Home & Kitchen", "price": 1299.99, "stock_quantity": 8}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOME-0006"}),
            Action(name="update_product_stock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 10}),
            Action(name="update_product_stock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 12}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5010", "points_to_add": 500}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Home & Kitchen products evaluated", "Smart refrigerator added with unique SKU", "Smart refrigerator details retrieved", "Smart refrigerator stock updated to 10", "Smart refrigerator stock updated to 12", "All products listed within limit", "500 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Strategic Customer Portfolio

    Task(
        annotator="lucas",
        user_id="lucas_task_065_product_restocking",
        instruction="List low stock products with threshold 10. Get product details for ELEC-RCHAA04. List products by category 'Electronics'. Get inventory level for ELEC-4KTV55. Update product stock for ELEC-4KTV55 to 75. Get total sales for date 2025-06-05. Update customer loyalty points for CUST-5001 by adding 25 points. Get customer details for CUST-5001. List transactions for CUST-5001. Get transaction details for TXN-0001. Update product price for ELEC-RCHAA04 to $18.95. Get inventory level for KITCH-CHEFKNF8. Update product stock for KITCH-CHEFKNF8 to 40.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 10}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-RCHAA04"}),
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 75}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 25}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-RCHAA04", "new_price": 18.95}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40})
        ],
        outputs=[
            "Low stock products listed", "Batteries product details retrieved", "Electronics products listed", "TV inventory level retrieved", "TV stock updated to 75", "Sales total retrieved", "Customer loyalty points updated by 25", "Customer details retrieved", "Transactions listed", "Transaction details retrieved", "Batteries price updated to $18.95", "Kitchen knife inventory retrieved", "Kitchen knife stock updated to 40"
        ]
    ),

    # Customer Loyalty Management

    Task(
        annotator="lucas",
        user_id="lucas_task_066_customer_loyalty_management",
        instruction="Get customer details for CUST-5005, check loyalty points for CUST-5005. Update membership level for CUST-5005 to 'silver'. Get customer details for CUST-5001. Update customer loyalty points for CUST-5001 by adding 30 points. Get transaction details for TXN-0004. Update customer email for CUST-5005 to 'loyalty.customer@email.com'. Update customer phone number for CUST-5005 to '+1-555-987-6543'. Get customer loyalty points for CUST-5001. List transactions for CUST-5001. Get transaction details for TXN-0001. Update customer membership level for CUST-5001 to 'gold'.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5005"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5005"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5005", "new_membership_level": "silver"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 30}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5005", "new_email": "loyalty.customer@email.com"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5005", "new_phone_number": "+1-555-987-6543"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5001", "new_membership_level": "gold"})
        ],
        outputs=[
            "Customer details retrieved", "Loyalty points checked", "Membership level updated to silver", "Customer details retrieved for CUST-5001", "30 points added to customer", "Transaction details retrieved", "Email updated", "Phone number updated", "Customer loyalty points retrieved", "Transactions listed", "Transaction details retrieved", "Membership level updated to gold"
        ]
    ),

    # Employee Performance Management
    Task(
        annotator="lucas",
        user_id="lucas_task_067_employee_performance_management",
        instruction="Get employee details for EMP-1002. Update employee status for EMP-1002 to 'active'. List all employees. Add Jennifer Davis as Manager at STORE-001 with email 'jennifer.davis@store.com' and phone '+1-555-210-2003'. Update employee status for EMP-1003 to 'active'. Get employee details for EMP-1004. List all employees again to verify changes. Update employee status for EMP-1008 to 'on_leave'. List all employees to confirm final workforce status. Update employee status for EMP-1009 to 'active'.",
        actions=[
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "active"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="add_employee", kwargs={"name": "Jennifer Davis", "role": "Manager", "store_id": "STORE-001", "email": "jennifer.davis@store.com", "phone_number": "+1-555-210-2003"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1003", "new_status": "active"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "on_leave"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "active"})
        ],
        outputs=[
            "Employee details retrieved", "Employee status updated to active", "All employees listed", "Jennifer Davis added as Manager with specified contact info",
            "Employee status updated", "Employee details retrieved for EMP-1004", "All employees listed again", "Employee details retrieved for EMP-1008", "Employee status updated to on_leave", "All employees listed", "Employee details retrieved for EMP-1009", "Employee status updated to active"
        ]
    ),
    # Customer Relationship Excellence
    Task(
        annotator="lucas",
        user_id="lucas_task_068_strategic_portfolio",
        instruction="Execute comprehensive strategic portfolio management for CUST-5003: get customer details, update membership level to platinum, get customer loyalty points, add 500 points if below 1000, record sale with 1 ELEC-4KTV55 using credit card, list transactions by customer, get transaction details for TXN-0003, update customer email to portfolio.customer@strategic.com, update customer address to 123 Portfolio Street, Strategic City, SC 12345, get customer details again, get customer loyalty points again, update customer phone number to +1-555-333-2222, update customer loyalty points by adding 200 more points, list transactions by customer again, get transaction details again, update customer membership level to platinum, and verify all strategic portfolio updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5003", "new_membership_level": "platinum"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 500}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5003", "new_email": "portfolio.customer@strategic.com"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5003", "new_address": "123 Portfolio Street, Strategic City, SC 12345"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5003"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-333-2222"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 200}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5003", "new_membership_level": "platinum"})
        ],
        outputs=[
            "Customer details retrieved for strategic portfolio", "Membership level updated to platinum for strategic portfolio", "Loyalty points checked for strategic portfolio", "500 points added to customer for strategic portfolio",
            "TV sale recorded for strategic portfolio", "Transactions listed for strategic portfolio", "Transaction details retrieved for strategic portfolio", "Email updated to portfolio customer for strategic portfolio", "Address updated to portfolio street for strategic portfolio", "Updated customer details retrieved for strategic portfolio", "Updated loyalty points retrieved for strategic portfolio", "Phone number updated for strategic portfolio", "200 additional points added to customer for strategic portfolio", "Transactions listed again for strategic portfolio", "Transaction details retrieved again for strategic portfolio", "Membership level updated to platinum for strategic portfolio"
        ]
    ),

    # Strategic Inventory Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_069_multi_store_employees",
        instruction="List all employees, get employee details for EMP-1008, update employee status for EMP-1008 to 'promoted', add new employee Sarah Johnson as Supervisor at STORE-002 with email sarah.johnson@retailpos.com and phone +1-555-210-2004, get employee details for EMP-1009, update employee status for EMP-1009 to 'active', add new employee Mark Wilson as Sales Associate at STORE-003 with email mark.wilson@retailpos.com and phone +1-555-210-2005, remove employee EMP-1011, list all employees again, and get employee details for EMP-1015.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="add_employee", kwargs={"name": "Sarah Johnson", "role": "Supervisor", "store_id": "STORE-002", "email": "sarah.johnson@retailpos.com", "phone_number": "+1-555-210-2004"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Mark Wilson", "role": "Sales Associate", "store_id": "STORE-003", "email": "mark.wilson@retailpos.com", "phone_number": "+1-555-210-2005"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1011"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to promoted", "Sarah Johnson added as Supervisor",
            "Second employee details retrieved", "Second employee status updated to active", "Mark Wilson added as Sales Associate", "Employee removed", "All employees listed again", "Third employee details retrieved"
        ]
    ),


    # Store Operations Management

    Task(
        annotator="lucas",
        user_id="lucas_task_070_store_operations",
        instruction="List all employees, add new employee David Brown as Manager at STORE-004 with email david.brown@retailpos.com and phone +1-555-210-2006, get employee details for EMP-1020, update employee status for EMP-1020 to 'manager', list low stock products with threshold 30, get inventory level for GROC-ALMBTR500, update product stock for GROC-ALMBTR500 to 75, get product details for GROC-ALMBTR500, update product price for GROC-ALMBTR500 to $8.99, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="add_employee", kwargs={"name": "David Brown", "role": "Manager", "store_id": "STORE-004", "email": "david.brown@retailpos.com", "phone_number": "+1-555-210-2006"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1020"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1020", "new_status": "manager"}),
            Action(name="list_low_stock_products", kwargs={"threshold": 30}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 75}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_price", kwargs={"sku": "GROC-ALMBTR500", "new_price": 8.99}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "All employees listed", "David Brown added as Manager", "Employee details retrieved", "Employee status updated to manager",
            "Low stock products listed", "Almond butter inventory retrieved", "Almond butter stock updated to 75", "Almond butter details retrieved", "Almond butter price updated to $8.99", "Daily sales total retrieved"
        ]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_071_advanced_customer",
        instruction="Add new customer 'Premium Customer Corp' with email premium@corp.com, phone +1-555-999-8888, and address '999 Premium Ave, Luxury City, LC 99999', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 500 points, record sale for CUST-5013 with 1 ELEC-4KTV55 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), and update customer phone number for CUST-5013 to '+1-555-999-7777'.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Premium Customer Corp", "email": "premium@corp.com", "phone_number": "+1-555-999-8888", "address": "999 Premium Ave, Luxury City, LC 99999"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 500}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-999-7777"})
        ],
        outputs=[
            "Premium customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "500 points added to CUST-5013",
            "TV sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Phone number updated for CUST-5013"
        ]
    ),


    # Customer Relationship Building

    Task(
        annotator="lucas",
        user_id="lucas_task_072_customer_relationship",
        instruction="Add new customer 'VIP Customer Services' with email vip@services.com, phone +1-555-888-7777, and address '888 VIP Boulevard, Elite City, EC 88888', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 1000 points, update customer address for CUST-5013 to '888 VIP Boulevard Suite 100, Elite City, EC 88888', record sale for CUST-5013 with 2 GROC-GRNLBR12 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), and update customer phone number for CUST-5013 to '+1-555-888-6666'.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "VIP Customer Services", "email": "vip@services.com", "phone_number": "+1-555-888-7777", "address": "888 VIP Boulevard, Elite City, EC 88888"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 1000}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5013", "new_address": "888 VIP Boulevard Suite 100, Elite City, EC 88888"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "GROC-GRNLBR12", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-888-6666"})
        ],
        outputs=[
            "VIP customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "1000 points added to CUST-5013",
            "Address updated to suite 100 for CUST-5013", "Granola bar sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Phone number updated for CUST-5013"
        ]
    ),

    # Advanced Inventory Rebalancing

    Task(
        annotator="lucas",
        user_id="lucas_task_073_inventory_rebalancing",
        instruction="List low stock products with threshold 45, get inventory level for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 20, get product details for KITCH-CHEFKNF8, update product price for KITCH-CHEFKNF8 to $299.99, get inventory level for GROC-GRNLBR12, update product stock for GROC-GRNLBR12 to 90, record sale for customer CUST-5001 with 1 KITCH-CHEFKNF8 using credit card, get customer loyalty points for CUST-5001, update customer loyalty points for CUST-5001 by adding 150 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 45}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 20}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_price", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 299.99}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 90}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 150}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
        ]
    ),

    # Multi Department Staff Reorganization
    Task(
        annotator="lucas",
        user_id="lucas_task_074_staff_reorganization",
        instruction="Review current employee roster, get employee details for EMP-1008, update employee status for EMP-1008 to 'relocated', add new employee Lisa Chen as Regional Manager at STORE-003 with email lisa.chen@retailpos.com and phone +1-555-210-2010, get employee details for EMP-1011, update employee status for EMP-1011 to 'senior_manager', add new employee Carlos Rodriguez as Operations Director at STORE-004 with email carlos.rodriguez@retailpos.com and phone +1-555-210-2011, remove employee EMP-1003, and list all employees again.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "relocated"}),
            Action(name="add_employee", kwargs={"name": "Lisa Chen", "role": "Regional Manager", "store_id": "STORE-003", "email": "lisa.chen@retailpos.com", "phone_number": "+1-555-210-2010"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1011"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1011", "new_status": "senior_manager"}),
            Action(name="add_employee", kwargs={"name": "Carlos Rodriguez", "role": "Operations Director", "store_id": "STORE-004", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="list_all_employees", kwargs={})
        ],
        outputs=[
            "Employee roster reviewed", "Employee details retrieved", "Employee status updated to relocated", "Lisa Chen added as Regional Manager",
            "Second employee details retrieved", "Second employee status updated to senior manager", "Carlos Rodriguez added as Operations Director", "Employee removed", "All employees listed again"
        ]
    ),

    # Product Line Expansion

    Task(
        annotator="lucas",
        user_id="lucas_task_075_premium_onboarding",
        instruction="Add new customer 'Enterprise Solutions Inc' with email enterprise@solutions.com, phone +1-555-777-6666, and address '777 Enterprise Drive, Business City, BC 77777', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 2000 points, update customer email for CUST-5013 to 'premium.enterprise@solutions.com', record sale for CUST-5013 with 1 ELEC-4KTV55 and 1 KITCH-CHEFKNF8 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), update customer address for CUST-5013 to '777 Enterprise Drive Floor 50, Business City, BC 77777', and get customer details for CUST-5013 again.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Enterprise Solutions Inc", "email": "enterprise@solutions.com", "phone_number": "+1-555-777-6666", "address": "777 Enterprise Drive, Business City, BC 77777"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 2000}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5013", "new_email": "premium.enterprise@solutions.com"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5013", "new_address": "777 Enterprise Drive Floor 50, Business City, BC 77777"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[
            "Enterprise customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "2000 points added to CUST-5013",
            "Email updated to premium enterprise for CUST-5013", "High-value sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Address updated to floor 50 for CUST-5013", "Final customer details retrieved for CUST-5013"
        ]
    ),


    # Multi Store Product Distribution

    Task(
        annotator="lucas",
        user_id="lucas_task_076_product_distribution",
        instruction="List products by category 'Sports & Outdoors', get inventory level for CLTH-SLFJEAN34, update product stock for CLTH-SLFJEAN34 to 45, get product details for CLTH-SLFJEAN34, update product price for CLTH-SLFJEAN34 to $94.99, add new product 'Sports Water Bottle' in Sports & Outdoors category with description 'Insulated stainless steel water bottle' and price $19.99 and stock quantity 50, list products by category 'Sports & Outdoors' again to verify distribution, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_inventory_level", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_stock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 45}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_price", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 94.99}),
            Action(name="add_new_product", kwargs={"name": "Sports Water Bottle", "description": "Insulated stainless steel water bottle", "category": "Sports & Outdoors", "price": 19.99, "stock_quantity": 50}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Sports products listed", "Jeans inventory retrieved", "Jeans stock updated to 45", "Jeans details retrieved",
            "Jeans price updated to $94.99", "Sports water bottle added with unique SKU", "Water bottle stock updated to 100", "Sports products listed again to verify distribution", "Daily sales total retrieved"
        ]
    ),


    # Strategic Inventory Reallocation

    Task(
        annotator="lucas",
        user_id="lucas_task_077_strategic_reallocation",
        instruction="List low stock products with threshold 75, get inventory level for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 50, get product details for KITCH-CHEFKNF8, update product price for KITCH-CHEFKNF8 to $12.99, get inventory level for GROC-GRNLBR12, update product stock for GROC-GRNLBR12 to 120, add new product 'Premium Stapler' in Office Supplies category with description 'Heavy-duty office stapler with 20-sheet capacity' and price $24.99 and stock quantity 50, record sale for customer CUST-5003 with 1 KITCH-CHEFKNF8 using credit card, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 75}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 50}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_price", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 12.99}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 120}),
            Action(name="add_new_product", kwargs={"name": "Premium Stapler", "description": "Heavy-duty office stapler with 20-sheet capacity", "category": "Office Supplies", "price": 24.99, "stock_quantity": 50}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Low stock products listed", "Chef knife inventory retrieved", "Chef knife stock updated to 50", "Chef knife details retrieved",
            "Chef knife price updated to $12.99", "Granola bar inventory retrieved", "Granola bar stock updated to 120", "Premium stapler added with unique SKU", "Chef knife sale recorded", "Daily sales total retrieved"
        ]
    ),


    # Workforce Development Initiative

    Task(
        annotator="lucas",
        user_id="lucas_task_078_workforce_development",
        instruction="List all employees, get employee details for EMP-1004, update employee status for EMP-1004 to 'development_program', add new employee Angela Thompson as Development Coordinator at STORE-004 with email angela.thompson@retailpos.com and phone +1-555-210-2011, get employee details for EMP-1002, update employee status for EMP-1002 to 'mentor', add new employee James Wilson as Training Specialist at STORE-005 with email james.wilson@retailpos.com and phone +1-555-210-2012, remove employee EMP-1034, and list all employees again.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "development_program"}),
            Action(name="add_employee", kwargs={"name": "Angela Thompson", "role": "Development Coordinator", "store_id": "STORE-004", "email": "angela.thompson@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "mentor"}),
            Action(name="add_employee", kwargs={"name": "James Wilson", "role": "Training Specialist", "store_id": "STORE-005", "email": "james.wilson@retailpos.com", "phone_number": "+1-555-210-2012"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1034"}),
            Action(name="list_all_employees", kwargs={})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to development program", "Angela Thompson added as Development Coordinator",
            "Second employee details retrieved", "Second employee status updated to mentor", "James Wilson added as Training Specialist", "Employee removed", "All employees listed again"
        ]
    ),

    # Product Innovation Pipeline

    Task(
        annotator="lucas",
        user_id="lucas_task_079_supply_chain",
        instruction="List low stock products with threshold 80, get inventory level for HOM-COFMKR12, update product stock for HOM-COFMKR12 to 110, get product details for HOM-COFMKR12, update product price for HOM-COFMKR12 to $29.99, get inventory level for KITCH-CHEFKNF8, update product stock for KITCH-CHEFKNF8 to 75, list products by category 'Home & Kitchen', record sale for customer CUST-5009 with 2 HOM-COFMKR12 and 1 KITCH-CHEFKNF8 using debit card, and update customer loyalty points for CUST-5009 by adding 120 points.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 80}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 110}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 29.99}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 75}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "HOM-COFMKR12", "quantity": 2}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 120})
        ],
        outputs=[
            "Low stock products listed", "Coffee maker inventory retrieved", "Coffee maker stock updated to 110", "Coffee maker details retrieved",
            "Coffee maker price updated to $29.99", "Chef knife inventory retrieved", "Chef knife stock updated to 75", "Home & Kitchen products listed", "Multi-item home sale recorded", "120 points added to customer"
        ]
    ),

    # Market Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_080_market_expansion",
        instruction="List products by category 'Books', list products by category 'Office Supplies', get product details for GROC-ALMBTR500, update product price for GROC-ALMBTR500 to $16.99, get inventory level for GROC-ALMBTR500, update product stock for GROC-ALMBTR500 to 55, add new product 'Business Strategy Guide' in Books category with description 'Comprehensive guide to business strategy and planning' and price $24.99 and stock quantity 40, get product details for the newly added Business Strategy Guide, list products by category 'Books' again to verify market expansion, and get customer details for CUST-5010.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Books"}),
            Action(name="list_products_by_category", kwargs={"category": "Office Supplies"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_price", kwargs={"sku": "GROC-ALMBTR500", "new_price": 16.99}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 55}),
            Action(name="add_new_product", kwargs={"name": "Business Strategy Guide", "description": "Comprehensive guide to business strategy and planning", "category": "Books", "price": 24.99, "stock_quantity": 40}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "BOOK-0002"}),
            Action(name="list_products_by_category", kwargs={"category": "Books"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[
            "Books products listed", "Office products listed", "Almond butter details retrieved", "Almond butter price updated to $16.99",
            "Almond butter inventory retrieved", "Almond butter stock updated to 55", "Business strategy guide added with unique SKU", "Business strategy guide details retrieved", "Books products listed again to verify market expansion", "Customer details retrieved for CUST-5010"
        ]
    ),

    # Customer Experience Enhancement

    Task(
        annotator="lucas",
        user_id="lucas_task_081_customer_experience",
        instruction="Add new customer 'Experience Enhancement Corp' with email experience@enhancement.com, phone +1-555-666-5555, and address '666 Experience Blvd, Enhancement City, EC 66666', get customer details for the new customer, update customer membership level to 'gold', update loyalty points by adding 750 points, update customer email to 'premium.experience@enhancement.com', record sale for the new customer with 1 HOM-COFMKR12 and 1 KITCH-CHEFKNF8 using credit card, list transactions for the new customer, get transaction details for the latest transaction, update customer phone number to '+1-555-666-4444', and get customer details for the new customer again.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Experience Enhancement Corp", "email": "experience@enhancement.com", "phone_number": "+1-555-666-5555", "address": "666 Experience Blvd, Enhancement City, EC 66666"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "gold"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 750}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5013", "new_email": "premium.experience@enhancement.com"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "HOM-COFMKR12", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-666-4444"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[
            "Experience enhancement customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to gold for CUST-5013", "750 points added to CUST-5013",
            "Email updated to premium experience for CUST-5013", "Multi-item home sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Phone number updated for CUST-5013", "Final customer details retrieved for CUST-5013"
        ]
    ),

    # Innovation and Growth Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_082_strategic_portfolio",
        instruction="Add new customer 'Strategic Portfolio Solutions' with email strategic@portfolio.com, phone +1-555-555-4444, and address '555 Strategic Avenue, Portfolio City, PC 55544', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 1500 points, record sale for customer CUST-5013 with 1 ELEC-4KTV55 and 1 KITCH-CHEFKNF8 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), update customer email for CUST-5013 to 'premium.strategic@portfolio.com', and get customer details for CUST-5013 again.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Strategic Portfolio Solutions", "email": "strategic@portfolio.com", "phone_number": "+1-555-555-4444", "address": "555 Strategic Avenue, Portfolio City, PC 55544"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 1500}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5013", "new_email": "premium.strategic@portfolio.com"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[
            "Strategic portfolio customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "1500 points added to CUST-5013",
            "High-value electronics sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Email updated to premium strategic for CUST-5013", "Final customer details retrieved for CUST-5013"
        ]
    ),

    # Employee Performance

    Task(
        annotator="lucas",
        user_id="lucas_task_083_multi_store_employees",
        instruction="List all employees, get employee details for EMP-1008, update employee status for EMP-1008 to 'promoted', add new employee Sarah Johnson as Supervisor at STORE-002 with email sarah.johnson@retailpos.com and phone +1-555-210-2004, get employee details for EMP-1009, update employee status for EMP-1009 to 'active', add new employee Mark Wilson as Sales Associate at STORE-003 with email mark.wilson@retailpos.com and phone +1-555-210-2005, remove employee EMP-1011, list all employees again, and get employee details for EMP-1015.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="add_employee", kwargs={"name": "Sarah Johnson", "role": "Supervisor", "store_id": "STORE-002", "email": "sarah.johnson@retailpos.com", "phone_number": "+1-555-210-2004"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1009"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1009", "new_status": "active"}),
            Action(name="add_employee", kwargs={"name": "Mark Wilson", "role": "Sales Associate", "store_id": "STORE-003", "email": "mark.wilson@retailpos.com", "phone_number": "+1-555-210-2005"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1011"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to promoted", "Sarah Johnson added as Supervisor",
            "Second employee details retrieved", "Second employee status updated to active", "Mark Wilson added as Sales Associate", "Employee removed", "All employees listed again", "Third employee details retrieved"
        ]
    ),

    # Store Operations Management

    Task(
        annotator="lucas",
        user_id="lucas_task_084_store_operations",
        instruction="Review current employee roster, add new employee Sarah Wilson as Assistant Manager at STORE-003 with email sarah.wilson@retailpos.com and phone +1-555-210-2007, get employee details for EMP-1015, update employee status for EMP-1015 to 'assistant_manager', list low stock products with threshold 25, get inventory level for HOM-COFMKR12, update product stock for HOM-COFMKR12 to 60, get product details for HOM-COFMKR12, update product price for HOM-COFMKR12 to $89.99, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="add_employee", kwargs={"name": "Sarah Wilson", "role": "Assistant Manager", "store_id": "STORE-003", "email": "sarah.wilson@retailpos.com", "phone_number": "+1-555-210-2007"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1015"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1015", "new_status": "assistant_manager"}),
            Action(name="list_low_stock_products", kwargs={"threshold": 25}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Employee roster reviewed", "Sarah Wilson added as Assistant Manager", "Employee details retrieved", "Employee status updated to assistant manager",
            "Low stock products listed", "Coffee maker inventory retrieved", "Coffee maker stock updated to 60", "Coffee maker details retrieved", "Coffee maker price updated to $89.99", "Daily sales total retrieved"
        ]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_085_advanced_customer",
        instruction="Add new customer 'Premium Customer Corp' with email premium@corp.com, phone +1-555-999-8888, and address '999 Premium Ave, Luxury City, LC 99999', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 500 points, record sale for CUST-5013 with 1 ELEC-4KTV55 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), and update customer phone number for CUST-5013 to '+1-555-999-7777'.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Premium Customer Corp", "email": "premium@corp.com", "phone_number": "+1-555-999-8888", "address": "999 Premium Ave, Luxury City, LC 99999"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 500}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-999-7777"})
        ],
        outputs=[
            "Premium customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "500 points added to CUST-5013",
            "TV sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Phone number updated for CUST-5013"
        ]
    ),

    # Advanced Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_086_advanced_customer_relationship",
        instruction="Execute advanced customer relationship management for CUST-5012: get details, update email to relationship.customer@email.com, update phone to +1-555-444-5555, update address to 500 Relationship Blvd, City, ST 54321, check loyalty, update membership to diamond, list their transactions. Then get details for TXN-0013, record sale (ELEC-4KTV55), record sale (GROC-GRNLBR12), update loyalty by adding 400 points, update membership to elite, list all products, get product details for HOM-COFMKR12, update product price for HOM-COFMKR12 to $129.99, get inventory, update stock for HOM-COFMKR12 to 80, get total sales for date 2025-06-12, and verify all updates.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5012", "new_email": "relationship.customer@email.com"}),
            Action(name="update_customer_phone_number", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-444-5555"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5012", "new_address": "500 Relationship Blvd, City, ST 54321"}),
            Action(name="get_customer_loyalty_points", kwargs={"customer_id": "CUST-5012"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "diamond"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "GROC-GRNLBR12", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5012", "points_to_add": 400}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5012", "new_membership_level": "elite"}),
            Action(name="list_all_products", kwargs={"limit": 50}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 129.99}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 80}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-12"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5012"})
        ],
        outputs=[
            "Advanced customer relationship management executed for CUST-5012, all updates verified"
        ]
    ),

    # Advanced Inventory Rebalancing

    Task(
        annotator="lucas",
        user_id="lucas_task_087_advanced_inventory_rebalancing",
        instruction="Execute advanced inventory rebalancing: list low stock products with threshold 20, get inventory for ELEC-4KTV55, AUDIO-BTSPKR02, HOM-COFMKR12, KITCH-CHEFKNF8, update stock to 40, 35, 50, 30 respectively, get product details for all, update prices to 699.99, 179.99, 99.99, 249.99 respectively, add new product 'Inventory Rebalancer Pro' with description 'Automated inventory rebalancing system' and price 499.99 and stock quantity 20, get total sales for date 2025-06-13 and 2025-06-14, and verify all updates.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 20}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 50}),
            Action(name="update_product_stock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 30}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 699.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 179.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 99.99}),
            Action(name="update_product_price", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 249.99}),
            Action(name="add_new_product", kwargs={"name": "Inventory Rebalancer Pro", "description": "Automated inventory rebalancing system", "category": "Electronics", "price": 499.99, "stock_quantity": 20}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-13"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-14"}),
        ],
        outputs=[
            "Advanced inventory rebalancing executed, all updates verified"
        ]
    ),

    # Multi Department Staff Reorganization
    Task(
        annotator="lucas",
        user_id="lucas_task_088_staff_reorganization",
        instruction="List all employees, get employee details for EMP-1003, update employee status for EMP-1003 to 'transferred', add new employee Robert Johnson as Department Head at STORE-001 with email robert.johnson@retailpos.com and phone +1-555-210-2008, get employee details for EMP-1004, update employee status for EMP-1004 to 'promoted', add new employee Maria Garcia as Assistant Manager at STORE-002 with email maria.garcia@retailpos.com and phone +1-555-210-2009, remove employee EMP-1020, and list all employees again.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1003"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1003", "new_status": "transferred"}),
            Action(name="add_employee", kwargs={"name": "Robert Johnson", "role": "Department Head", "store_id": "STORE-001", "email": "robert.johnson@retailpos.com", "phone_number": "+1-555-210-2008"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "promoted"}),
            Action(name="add_employee", kwargs={"name": "Maria Garcia", "role": "Assistant Manager", "store_id": "STORE-002", "email": "maria.garcia@retailpos.com", "phone_number": "+1-555-210-2009"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1020"}),
            Action(name="list_all_employees", kwargs={})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to transferred", "Robert Johnson added as Department Head",
            "Second employee details retrieved", "Second employee status updated to promoted", "Maria Garcia added as Assistant Manager", "Employee removed", "All employees listed again"
        ]
    ),

    # Product Line Expansion

    Task(
        annotator="lucas",
        user_id="lucas_task_089_seasonal_inventory",
        instruction="List low stock products with threshold 40, get inventory level for GROC-GRNLBR12, update product stock for GROC-GRNLBR12 to 85, get product details for GROC-GRNLBR12, update product price for GROC-GRNLBR12 to $3.99, get inventory level for HOM-COFMKR12, update product stock for HOM-COFMKR12 to 65, record sale for customer CUST-5002 with 3 GROC-GRNLBR12 using cash, update customer loyalty points for CUST-5002 by adding 30 points, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 40}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 85}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_price", kwargs={"sku": "GROC-GRNLBR12", "new_price": 3.99}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 65}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "GROC-GRNLBR12", "quantity": 3}], "payment_method": "cash"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 30}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Low stock products listed", "Granola bar inventory retrieved", "Granola bar stock updated to 85", "Granola bar details retrieved",
            "Granola bar price updated to $3.99", "Desk lamp inventory retrieved", "Desk lamp stock updated to 65", "Granola bar sale recorded", "30 points added to customer", "Daily sales total retrieved"
        ]
    ),

    # Workforce Development Initiative

    Task(
        annotator="lucas",
        user_id="lucas_task_091_workforce_development",
        instruction="List all employees, get employee details for EMP-1002, update employee status for EMP-1002 to 'training', add new employee Jennifer Wilson as Training Coordinator at STORE-001 with email jennifer.wilson@retailpos.com and phone +1-555-210-2011, get employee details for EMP-1008, update employee status for EMP-1008 to 'mentor', add new employee Michael Brown as Development Specialist at STORE-002 with email michael.brown@retailpos.com and phone +1-555-210-2012, remove employee EMP-1015, and list all employees again.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "training"}),
            Action(name="add_employee", kwargs={"name": "Jennifer Wilson", "role": "Training Coordinator", "store_id": "STORE-001", "email": "jennifer.wilson@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "mentor"}),
            Action(name="add_employee", kwargs={"name": "Michael Brown", "role": "Development Specialist", "store_id": "STORE-002", "email": "michael.brown@retailpos.com", "phone_number": "+1-555-210-2012"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1015"}),
            Action(name="list_all_employees", kwargs={})
        ],
        outputs=[
            "All employees listed", "Employee details retrieved", "Employee status updated to training", "Jennifer Wilson added as Training Coordinator",
            "Second employee details retrieved", "Second employee status updated to mentor", "Michael Brown added as Development Specialist", "Employee removed", "All employees listed again"
        ]
    ),

    # Product Innovation Pipeline

    Task(
        annotator="lucas",
        user_id="lucas_task_092_supply_chain",
        instruction="List low stock products with threshold 50, get inventory level for AUDIO-BTSPKR02, check if AUDIO-BTSPKR02 stock is below 40 and update to 35 only if needed, get product details for AUDIO-BTSPKR02, update product price for AUDIO-BTSPKR02 to $159.99, get inventory level for HOM-COFMKR12, check if HOM-COFMKR12 stock is below 80 and update to 70 only if needed, add new product 'Supply Chain Monitor' in Electronics category with description 'Real-time supply chain monitoring device' and price $199.99 and stock quantity 25, get product details for the newly added Supply Chain Monitor (ELEC-0006), record sale for customer CUST-5007 with 1 AUDIO-BTSPKR02 using debit card, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 50}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 159.99}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 70}),
            Action(name="add_new_product", kwargs={"name": "Supply Chain Monitor", "description": "Real-time supply chain monitoring device", "category": "Electronics", "price": 199.99, "stock_quantity": 25}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-0006"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Low stock products listed", "Speaker inventory retrieved", "Speaker stock rechecked", "Speaker stock updated to 35 only if needed", "Speaker details retrieved",
            "Speaker price updated to $159.99", "Desk lamp inventory retrieved", "Desk lamp stock rechecked", "Desk lamp stock updated to 70 only if needed", "Supply chain monitor added with unique SKU", "Supply chain monitor details retrieved", "Speaker sale recorded", "Daily sales total retrieved"
        ]
    ),

    # Innovation and Growth Strategy
    Task(
        annotator="lucas",
        user_id="lucas_task_093_strategic_portfolio",
        instruction="Add new customer 'Strategic Partners LLC' with email strategic@partners.com, phone +1-555-666-5555, and address '666 Strategic Way, Portfolio City, PC 66666', get customer details for the newly created customer (CUST-5013), update customer membership level for CUST-5013 to 'platinum', update loyalty points for CUST-5013 by adding 1500 points, update customer email for CUST-5013 to 'premium.strategic@partners.com', record sale for CUST-5013 with 1 ELEC-4KTV55 and 1 AUDIO-BTSPKR02 using credit card, list transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), update customer address for CUST-5013 to '666 Strategic Way Suite 200, Portfolio City, PC 66666', and get customer details for CUST-5013 again.",
        actions=[
            Action(name="add_new_customer", kwargs={"name": "Strategic Partners LLC", "email": "strategic@partners.com", "phone_number": "+1-555-666-5555", "address": "666 Strategic Way, Portfolio City, PC 66666"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5013", "points_to_add": 1500}),
            Action(name="update_customer_email", kwargs={"customer_id": "CUST-5013", "new_email": "premium.strategic@partners.com"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="update_customer_address", kwargs={"customer_id": "CUST-5013", "new_address": "666 Strategic Way Suite 200, Portfolio City, PC 66666"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[
            "Strategic customer added as CUST-5013", "Customer details retrieved for CUST-5013", "Membership level updated to platinum for CUST-5013", "1500 points added to CUST-5013",
            "Email updated to premium strategic for CUST-5013", "High-value electronics sale recorded for CUST-5013", "Transactions listed for CUST-5013", "Transaction details retrieved for TXN-0013", "Address updated to suite 200 for CUST-5013", "Final customer details retrieved for CUST-5013"
        ]
    ),

    # Inventory Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_094_inventory_optimization",
        instruction="List low stock products with threshold 30, get inventory level for ELEC-4KTV55, get inventory level for AUDIO-BTSPKR02, get inventory level for HOM-COFMKR12, update product stock for ELEC-4KTV55 to 25, update product stock for AUDIO-BTSPKR02 to 40, update product stock for HOM-COFMKR12 to 35, get product details for ELEC-4KTV55, get product details for AUDIO-BTSPKR02, get product details for HOM-COFMKR12, update product price for ELEC-4KTV55 to $599.99, update product price for AUDIO-BTSPKR02 to $159.99, update product price for HOM-COFMKR12 to $89.99, add new product 'Inventory Optimization Suite' in Electronics category with description 'Advanced inventory management and optimization platform' and price $399.99 and stock quantity 20, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_low_stock_products", kwargs={"threshold": 30}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 25}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 35}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 599.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 159.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="add_new_product", kwargs={"name": "Inventory Optimization Suite", "description": "Advanced inventory management and optimization platform", "category": "Electronics", "price": 399.99, "stock_quantity": 20}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Low stock products identified for optimization", "TV inventory level assessed", "Speaker inventory level assessed", "Coffee maker inventory level assessed", "TV stock optimized to 25 units", "Speaker stock optimized to 40 units", "Coffee maker stock optimized to 35 units", "TV product specifications verified", "Speaker product specifications verified", "Coffee maker product specifications verified", "TV price optimized to $599.99", "Speaker price optimized to $159.99", "Coffee maker price optimized to $89.99", "Inventory optimization suite added with unique SKU", "Optimization impact on daily sales measured"
        ]
    ),

    # Advanced Employee Performance Management

    Task(
        annotator="lucas",
        user_id="lucas_task_095_product_portfolio",
        instruction="List products by category 'Electronics' to assess current portfolio, then list products by category 'Home & Kitchen' to expand portfolio analysis, and list products by category 'Sports & Outdoors' for comprehensive portfolio review. Get product details for ELEC-4KTV55 to assess high-value electronics and update product price for ELEC-4KTV55 to $649.99 for premium positioning. Get product details for HOM-COFMKR12 to evaluate home appliances and update product price for HOM-COFMKR12 to $94.99 for competitive pricing. Get product details for AUDIO-BTSPKR02 to analyze audio equipment and update product price for AUDIO-BTSPKR02 to $169.99 for market alignment. Get inventory level for ELEC-4KTV55 to assess stock status and update product stock for ELEC-4KTV55 to 30 for optimal levels. Get inventory level for HOM-COFMKR12 to check availability and update product stock for HOM-COFMKR12 to 45 for demand fulfillment. Get inventory level for AUDIO-BTSPKR02 to evaluate supply and update product stock for AUDIO-BTSPKR02 to 35 for balanced inventory. Add new product 'Portfolio Analytics Platform' in Electronics category with description 'Comprehensive product portfolio analysis and management system' and price $299.99 and stock quantity 15, and get total sales for date 2025-06-05 to measure portfolio performance impact.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 649.99}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 94.99}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 169.99}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 30}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 45}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="add_new_product", kwargs={"name": "Portfolio Analytics Platform", "description": "Comprehensive product portfolio analysis and management system", "category": "Electronics", "price": 299.99, "stock_quantity": 15}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics portfolio analyzed for expansion assessment", "Home & Kitchen portfolio analyzed for comprehensive review", "Sports portfolio analyzed for complete portfolio coverage", "TV product specifications reviewed for premium positioning", "TV price optimized to $649.99 based on market analysis", "Coffee maker product specifications reviewed for competitive pricing", "Coffee maker price optimized to $94.99 based on market assessment", "Speaker product specifications reviewed for market alignment", "Speaker price optimized to $169.99 based on competitive analysis", "TV inventory level assessed for stock optimization", "TV stock optimized to 30 units based on demand analysis", "Coffee maker inventory level assessed for supply optimization", "Coffee maker stock optimized to 45 units based on demand assessment", "Speaker inventory level assessed for supply management", "Speaker stock optimized to 35 units based on demand analysis", "Portfolio analytics platform added with unique SKU", "Portfolio optimization impact on daily sales measured"
        ]
    ),

    # Advanced Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_096_employee_performance",
        instruction="List all employees, get employee details for EMP-1002, get employee details for EMP-1004, get employee details for EMP-1008, update employee status for EMP-1002 to 'training', update employee status for EMP-1004 to 'active', update employee status for EMP-1008 to 'mentor', add new employee 'Performance Manager' as Performance Specialist at STORE-001 with email performance.manager@retailpos.com and phone +1-555-210-5002, add new employee 'Analytics Coordinator' as Analytics Specialist at STORE-002 with email analytics.coordinator@retailpos.com and phone +1-555-210-5003, remove employee EMP-1003, list all employees again, and get employee details for EMP-1002 to verify final status.",
        actions=[
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1004"}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1008"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1002", "new_status": "training"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1004", "new_status": "active"}),
            Action(name="update_employee_status", kwargs={"employee_id": "EMP-1008", "new_status": "mentor"}),
            Action(name="add_employee", kwargs={"name": "Performance Manager", "role": "Performance Specialist", "store_id": "STORE-001", "email": "performance.manager@retailpos.com", "phone_number": "+1-555-210-5002"}),
            Action(name="add_employee", kwargs={"name": "Analytics Coordinator", "role": "Analytics Specialist", "store_id": "STORE-002", "email": "analytics.coordinator@retailpos.com", "phone_number": "+1-555-210-5003"}),
            Action(name="remove_employee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_employee_details", kwargs={"employee_id": "EMP-1002"})
        ],
        outputs=[
            "All employees listed for performance assessment", "Employee performance profile for EMP-1002 retrieved", "Employee performance profile for EMP-1004 retrieved", "Employee performance profile for EMP-1008 retrieved", "EMP-1002 status updated to training", "EMP-1004 status updated to active", "EMP-1008 status updated to mentor", "Performance manager added as specialist", "Analytics coordinator added as specialist", "Underperforming employee removed", "Updated employee roster verified", "Final performance status for EMP-1002 confirmed"
        ]
    ),

    # Strategic Product Portfolio Management

    Task(
        annotator="lucas",
        user_id="lucas_task_097_customer_relationship",
        instruction="Get customer details for CUST-5005, get customer details for CUST-5006, get customer details for CUST-5007, list transactions for CUST-5005, list transactions for CUST-5006, update customer membership level for CUST-5005 to 'gold', update customer membership level for CUST-5006 to 'silver', update customer membership level for CUST-5007 to 'bronze', record sale for customer CUST-5005 with 1 ELEC-4KTV55 using credit card, record sale for customer CUST-5006 with 2 AUDIO-BTSPKR02 using credit card, update customer loyalty points for CUST-5005 by adding 400 points, update customer loyalty points for CUST-5006 by adding 200 points, and get customer details for CUST-5005 again.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5005"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5005"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5006"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5005", "new_membership_level": "gold"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5006", "new_membership_level": "silver"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5007", "new_membership_level": "bronze"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5005", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 400}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5005"})
        ],
        outputs=[
            "Customer relationship profile for CUST-5005 retrieved", "Customer relationship profile for CUST-5006 retrieved", "Customer relationship profile for CUST-5007 retrieved", "Transaction history for CUST-5005 analyzed", "Transaction history for CUST-5006 analyzed", "CUST-5005 upgraded to gold membership", "CUST-5006 upgraded to silver membership", "CUST-5007 upgraded to bronze membership", "Premium electronics sale recorded for CUST-5005", "High-value audio equipment sale recorded for CUST-5006", "400 loyalty points added to CUST-5005", "200 loyalty points added to CUST-5006", "Updated customer relationship profile for CUST-5005 retrieved"
        ]
    ),

    # Strategic Product Development Innovation

    Task(
        annotator="lucas",
        user_id="lucas_task_098_product_development",
        instruction="List products by category 'Electronics', list products by category 'Home & Kitchen', get product details for ELEC-4KTV55, get product details for HOM-COFMKR12, get product details for AUDIO-BTSPKR02, update product price for ELEC-4KTV55 to $699.99, update product price for HOM-COFMKR12 to $99.99, update product price for AUDIO-BTSPKR02 to $179.99, get inventory level for ELEC-4KTV55, get inventory level for HOM-COFMKR12, get inventory level for AUDIO-BTSPKR02, update product stock for ELEC-4KTV55 to 35, update product stock for HOM-COFMKR12 to 50, update product stock for AUDIO-BTSPKR02 to 40, add new product 'Innovation Hub Platform' in Electronics category with description 'Advanced product development and innovation management system' and price $499.99 and stock quantity 25, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 699.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 99.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 179.99}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 35}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 50}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="add_new_product", kwargs={"name": "Innovation Hub Platform", "description": "Advanced product development and innovation management system", "category": "Electronics", "price": 499.99, "stock_quantity": 25}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics product development catalog analyzed", "Home & Kitchen product development catalog analyzed", "TV product specifications reviewed for innovation", "Coffee maker product specifications reviewed for innovation", "Speaker product specifications reviewed for innovation", "TV price optimized to $699.99 for premium positioning", "Coffee maker price optimized to $99.99 for market competitiveness", "Speaker price optimized to $179.99 for value proposition", "TV inventory level assessed for development planning", "Coffee maker inventory level assessed for development planning", "Speaker inventory level assessed for development planning", "TV stock optimized to 35 units for development", "Coffee maker stock optimized to 50 units for development", "Speaker stock optimized to 40 units for development", "Innovation hub platform added with unique SKU", "Product development impact on daily sales measured"
        ]
    ),

    # Strategic Market Analysis Intelligence

    Task(
        annotator="lucas",
        user_id="lucas_task_099_market_intelligence",
        instruction="List products by category 'Electronics', list products by category 'Sports & Outdoors', list products by category 'Books', get product details for ELEC-4KTV55, get product details for AUDIO-BTSPKR02, get product details for HOM-COFMKR12, update product price for ELEC-4KTV55 to $749.99, update product price for AUDIO-BTSPKR02 to $189.99, update product price for HOM-COFMKR12 to $109.99, get inventory level for ELEC-4KTV55, get inventory level for AUDIO-BTSPKR02, get inventory level for HOM-COFMKR12, update product stock for ELEC-4KTV55 to 40, update product stock for AUDIO-BTSPKR02 to 45, update product stock for HOM-COFMKR12 to 55, add new product 'Market Intelligence Suite' in Electronics category with description 'Comprehensive market analysis and competitive intelligence platform' and price $399.99 and stock quantity 20, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="list_products_by_category", kwargs={"category": "Books"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 749.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 189.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 109.99}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 45}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 55}),
            Action(name="add_new_product", kwargs={"name": "Market Intelligence Suite", "description": "Comprehensive market analysis and competitive intelligence platform", "category": "Electronics", "price": 399.99, "stock_quantity": 20}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics market intelligence analyzed", "Sports market intelligence analyzed", "Books market intelligence analyzed", "TV market specifications reviewed", "Speaker market specifications reviewed", "Coffee maker market specifications reviewed", "TV price optimized to $749.99 for market positioning", "Speaker price optimized to $189.99 for market competitiveness", "Coffee maker price optimized to $109.99 for market value", "TV inventory level assessed for market analysis", "Speaker inventory level assessed for market analysis", "Coffee maker inventory level assessed for market analysis", "TV stock optimized to 40 units for market demand", "Speaker stock optimized to 45 units for market demand", "Coffee maker stock optimized to 55 units for market demand", "Market intelligence suite added with unique SKU", "Market intelligence impact on daily sales measured"
        ]
    ),

    # Advanced Customer Success Retention

    Task(
        annotator="lucas",
        user_id="lucas_task_100_customer_success",
        instruction="Get customer details for CUST-5008, get customer details for CUST-5009, get customer details for CUST-5010, list transactions for CUST-5008, list transactions for CUST-5009, update customer membership level for CUST-5008 to 'platinum', update customer membership level for CUST-5009 to 'gold', update customer membership level for CUST-5010 to 'silver', record sale for customer CUST-5008 with 1 ELEC-4KTV55 using credit card, record sale for customer CUST-5009 with 2 AUDIO-BTSPKR02 using credit card, update customer loyalty points for CUST-5008 by adding 800 points, update customer loyalty points for CUST-5009 by adding 500 points, and get customer details for CUST-5008 again.",
        actions=[
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5009"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5010"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5008"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5009"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5008", "new_membership_level": "platinum"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5009", "new_membership_level": "gold"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5010", "new_membership_level": "silver"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5008", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5008", "points_to_add": 800}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 500}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"})
        ],
        outputs=[
            "Customer success profile for CUST-5008 retrieved", "Customer success profile for CUST-5009 retrieved", "Customer success profile for CUST-5010 retrieved", "Transaction history for CUST-5008 analyzed", "Transaction history for CUST-5009 analyzed", "CUST-5008 upgraded to platinum membership", "CUST-5009 upgraded to gold membership", "CUST-5010 upgraded to silver membership", "Premium electronics sale recorded for CUST-5008", "High-value audio equipment sale recorded for CUST-5009", "800 loyalty points added to CUST-5008", "500 loyalty points added to CUST-5009", "Updated customer success profile for CUST-5008 retrieved"
        ]
    ),

    # Strategic Business Intelligence Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_101_business_intelligence",
        instruction="Get total sales for date 2025-06-05, get total sales for date 2025-06-06, list low stock products with threshold 25, get inventory level for ELEC-4KTV55, get inventory level for HOM-COFMKR12, get inventory level for AUDIO-BTSPKR02, update product stock for ELEC-4KTV55 to 30, update product stock for HOM-COFMKR12 to 40, update product stock for AUDIO-BTSPKR02 to 35, get customer details for CUST-5001, get customer details for CUST-5002, record sale for customer CUST-5001 with 1 ELEC-4KTV55 using credit card, record sale for customer CUST-5002 with 2 AUDIO-BTSPKR02 using credit card, update customer loyalty points for CUST-5001 by adding 700 points, and get total sales for date 2025-06-05 again.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"}),
            Action(name="list_low_stock_products", kwargs={"threshold": 25}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 30}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 40}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5002"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 700}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Business intelligence baseline sales for 2025-06-05 established", "Business intelligence comparative sales for 2025-06-06 retrieved", "Low stock products identified for business intelligence", "TV inventory level assessed for business intelligence", "Coffee maker inventory level assessed for business intelligence", "Speaker inventory level assessed for business intelligence", "TV stock optimized to 30 units for business intelligence", "Coffee maker stock optimized to 40 units for business intelligence", "Speaker stock optimized to 35 units for business intelligence", "CUST-5001 customer profile retrieved for business intelligence", "CUST-5002 customer profile retrieved for business intelligence", "Premium electronics sale recorded for CUST-5001", "High-value audio equipment sale recorded for CUST-5002", "700 loyalty points added to CUST-5001", "Updated business intelligence sales for 2025-06-05 measured"
        ]
    ),

    # Strategic Digital Transformation

    Task(
        annotator="lucas",
        user_id="lucas_task_103_digital_transformation",
        instruction="List products by category 'Electronics', list products by category 'Home & Kitchen', list products by category 'Sports & Outdoors', get product details for ELEC-4KTV55, get product details for HOM-COFMKR12, get product details for AUDIO-BTSPKR02, update product price for ELEC-4KTV55 to $849.99, update product price for HOM-COFMKR12 to $129.99, update product price for AUDIO-BTSPKR02 to $229.99, get inventory level for ELEC-4KTV55, get inventory level for HOM-COFMKR12, get inventory level for AUDIO-BTSPKR02, update product stock for ELEC-4KTV55 to 50, update product stock for HOM-COFMKR12 to 60, update product stock for AUDIO-BTSPKR02 to 55, add new product 'Digital Transformation Suite' in Electronics category with description 'Complete digital transformation and modernization platform' and price $799.99 and stock quantity 35, and get total sales for date 2025-06-05.",
        actions=[
            Action(name="list_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="list_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="list_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_price", kwargs={"sku": "ELEC-4KTV55", "new_price": 849.99}),
            Action(name="update_product_price", kwargs={"sku": "HOM-COFMKR12", "new_price": 129.99}),
            Action(name="update_product_price", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 229.99}),
            Action(name="get_inventory_level", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="get_inventory_level", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="get_inventory_level", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="update_product_stock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 50}),
            Action(name="update_product_stock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="update_product_stock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 55}),
            Action(name="add_new_product", kwargs={"name": "Digital Transformation Suite", "description": "Complete digital transformation and modernization platform", "category": "Electronics", "price": 799.99, "stock_quantity": 35}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Electronics digital transformation catalog analyzed", "Home & Kitchen digital transformation catalog analyzed", "Sports digital transformation catalog analyzed", "TV digital transformation specifications reviewed", "Coffee maker digital transformation specifications reviewed", "Speaker digital transformation specifications reviewed", "TV price optimized to $849.99 for digital transformation", "Coffee maker price optimized to $129.99 for digital transformation", "Speaker price optimized to $229.99 for digital transformation", "TV inventory level assessed for digital transformation", "Coffee maker inventory level assessed for digital transformation", "Speaker inventory level assessed for digital transformation", "TV stock optimized to 50 units for digital transformation", "Coffee maker stock optimized to 60 units for digital transformation", "Speaker stock optimized to 55 units for digital transformation", "Digital transformation suite added with unique SKU", "Digital transformation impact on daily sales measured"
        ]
    ),

    # Advanced Operational Excellence

    Task(
        annotator="lucas",
        user_id="lucas_task_104_operational_excellence",
        instruction="Get total sales for date 2025-06-05, list all employees, get customer details for CUST-5006, get customer details for CUST-5007, get customer details for CUST-5008, update customer membership level for CUST-5006 to 'gold', update customer membership level for CUST-5007 to 'silver', update customer membership level for CUST-5008 to 'bronze', record sale for customer CUST-5006 with 1 ELEC-4KTV55 using credit card, record sale for customer CUST-5007 with 2 AUDIO-BTSPKR02 using credit card, update customer loyalty points for CUST-5006 by adding 750 points, update customer loyalty points for CUST-5007 by adding 450 points, and get total sales for date 2025-06-05 again.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="list_all_employees", kwargs={}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5006"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5007"}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5008"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5006", "new_membership_level": "gold"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5007", "new_membership_level": "silver"}),
            Action(name="update_customer_membership_level", kwargs={"customer_id": "CUST-5008", "new_membership_level": "bronze"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="record_sale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 750}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5007", "points_to_add": 450}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"})
        ],
        outputs=[
            "Operational excellence baseline sales for 2025-06-05 established", "All employees listed for operational excellence assessment", "CUST-5006 customer profile retrieved for operational excellence", "CUST-5007 customer profile retrieved for operational excellence", "CUST-5008 customer profile retrieved for operational excellence", "CUST-5006 upgraded to gold membership", "CUST-5007 upgraded to silver membership", "CUST-5008 upgraded to bronze membership", "Premium electronics sale recorded for CUST-5006", "High-value audio equipment sale recorded for CUST-5007", "750 loyalty points added to CUST-5006", "450 loyalty points added to CUST-5007", "Updated operational excellence sales for 2025-06-05 measured"
        ]
    ),

    # Sales Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_107_sales_analytics",
        instruction="Get total sales for date 2025-06-05 to assess daily performance. Get total sales for date 2025-06-06 to compare with previous day's performance. Update customer loyalty points for CUST-5003 by adding 200 points as a performance reward. Get customer details for CUST-5003 to verify their status. List transactions for CUST-5003 to analyze their purchase history. Get transaction details for TXN-0002 to verify its status. Update transaction status for TXN-0002 to 'completed' to finalize the sale. Get inventory level for GROC-GRNLBR12 to assess stock status. Update product stock for GROC-GRNLBR12 to 85 to ensure adequate supply. Get total sales for date 2025-06-07 to assess business performance.",
        actions=[
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-05"}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-06"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5003", "points_to_add": 200}),
            Action(name="get_customer_details", kwargs={"customer_id": "CUST-5003"}),
            Action(name="list_transactions_by_customer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="get_transaction_details", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="update_transaction_status", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="get_inventory_level", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="update_product_stock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 85}),
            Action(name="get_total_sales_by_date", kwargs={"date": "2025-06-07"})
        ],
        outputs=[
            "Sales total for 2025-06-05 assessed for daily performance", "Sales total for 2025-06-06 compared with previous day", "200 points added to customer based on combined sales performance", "Customer details verified for status",
            "Transactions analyzed for purchase history", "Transaction details verified for status", "Transaction status updated to completed", "Granola bar inventory level assessed", "Granola bar stock updated to 85", "Sales performance assessed for business analysis"
        ]
    ),

]
