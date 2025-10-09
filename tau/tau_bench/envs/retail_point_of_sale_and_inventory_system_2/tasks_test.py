from tau_bench.types import Action, Task

TASKS = [

    # Customer Service

    Task(
        annotator="lucas",
        user_id="lucas_task_001_customer_service",
        instruction="Gather customer information for CUST-5001 to evaluate current status. If the membership tier is not 'gold', change it to 'gold'. Review loyalty points for CUST-5001 to gauge customer value. If the email is not 'customer.updated@email.com', modify it for enhanced communication. Compile transactions for CUST-5001 to review purchase history. If the phone number is not '+1-555-123-4567', adjust it for better contact information. Retrieve transaction details for TXN-0001 only if it appears in the customer's transaction history. Compile transactions for CUST-5001 once more to confirm all updates were executed successfully.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5001", "new_email": "customer.updated@email.com"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-123-4567"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[]
    ),

    # Product Management

    Task(
        annotator="lucas",
        user_id="lucas_task_002_product_management",
        instruction="Acquire product information for CLTH-SLFJEAN34 to evaluate current pricing strategy. If the present price exceeds $55, adjust the price of CLTH-SLFJEAN34 to $54.95 for competitive pricing. Compile a list of all products with a limit of 25 to assess overall inventory status. Obtain inventory for CLTH-SLFJEAN34 and verify if stock is under 75. If CLTH-SLFJEAN34 stock is under 75, change stock for CLTH-SLFJEAN34 to 80 to ensure sufficient supply. List products categorized as 'Apparel' to check category inventory management. Retrieve total sales for date 2025-06-06 to evaluate business performance. If total sales surpass $800, retrieve product information for CLTH-SLFJEAN34 again to confirm the price and inventory updates were completed successfully.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="ListAllProducts", kwargs={"limit": 25}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 80}),
            Action(name="ListProductsByCategory", kwargs={"category": "Apparel"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"})
        ],
        outputs=[]
    ),

    # Omnichannel Customer Journey

    Task(
        annotator="lucas",
        user_id="lucas_task_003_omnichannel_customer_journey",
        instruction="Execute a comprehensive omnichannel customer journey for CUST-5001: retrieve customer information, update email to omnichannel.customer@email.com, modify phone number to +1-555-111-2222, change address to 100 Omnichannel Ave, City, ST 12345, verify loyalty points, upgrade membership to platinum, compile transactions, retrieve transaction details for TXN-0001, record a sale with 1 ELEC-4KTV55 using a credit card, record a sale with 2 CLTH-SLFJEAN34 using a debit card, enhance loyalty points by adding 200, update membership to VIP, list all products with a limit of 50, obtain product information for HOM-COFMKR12, adjust product price to $109.99, determine inventory level, increase stock to 60, retrieve total sales for date 2025-06-05, and confirm all updates were effective.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5001", "new_email": "omnichannel.customer@email.com"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-111-2222"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5001", "new_address": "100 Omnichannel Ave, City, ST 12345"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "CLTH-SLFJEAN34", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 200}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "VIP"}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 109.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[]
    ),

    # Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_004_inventory",
        instruction="Identify products with low stock at a threshold of 20 to highlight critical inventory items. Check inventory level for KITCH-CHEFKNF8 and confirm if it's under 50. If KITCH-CHEFKNF8 stock is under 50, adjust it to 40. Compile a list of products categorized as 'Home & Kitchen' to assess category inventory. Check inventory level for HOM-COFMKR12 to see if restocking is necessary. List all products with a cap of 20 to verify inventory status. Retrieve total sales for date 2025-06-05 to evaluate business performance. If total sales exceed $1000, enhance loyalty points for customer CUST-5003 by adding 50 points as a performance incentive.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 20}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="ListAllProducts", kwargs={"limit": 20}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 50})
        ],
        outputs=[]
    ),

    # Sales Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_005_sales",
        instruction="Facilitate a sale for customer CUST-5004 involving 2 GROC-ALMBTR500 using a debit card. Retrieve total sales for date 2025-06-05. Obtain customer information for CUST-5004. Review customer loyalty points for CUST-5004. Compile a list of transactions for CUST-5004. Retrieve transaction details for TXN-0004. Obtain total sales for date 2025-06-06 to compare with previous totals.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5004"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "GROC-ALMBTR500", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5004"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"})
        ],
        outputs=[]
    ),

    # Product Category Management

    Task(
        annotator="lucas",
        user_id="lucas_task_006_product_category",
        instruction="Survey products categorized as 'Electronics', retrieve product information for ELEC-GAMLP15, adjust the price of ELEC-GAMLP15 to $599.99, compile a list of products categorized as 'Home & Kitchen', obtain inventory for KITCH-CHEFKNF8, modify product stock for KITCH-CHEFKNF8 to 45, retrieve total sales for date 2025-06-06, enhance customer loyalty points for CUST-5006 by adding 100 points, and compile a list of all products with a limit of 30.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-GAMLP15", "new_price": 599.99}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 45}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 100}),
            Action(name="ListAllProducts", kwargs={"limit": 30})
        ],
        outputs=[]
    ),

    # Return Processing

    Task(
        annotator="lucas",
        user_id="lucas_task_007_return_processing",
        instruction="Process return for transaction TXN-0001 only if the purchase date is within the last 90 days with the reason 'Customer return'. If so, increase customer loyalty points for CUST-5001 by adding 25 points, compile transactions for CUST-5001, obtain inventory level for ELEC-RCHAA04, modify product stock for ELEC-RCHAA04 to 25, and retrieve total sales for date 2025-06-05.",
        actions=[
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="ProcessReturn", kwargs={"original_transaction_id": "TXN-0001", "items_to_return": [{"sku": "ELEC-RCHAA04", "quantity": 1}], "reason": "Customer return"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 25}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-RCHAA04"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-RCHAA04", "new_stock_quantity": 25}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Return Management

    Task(
        annotator="lucas",
        user_id="lucas_task_008_return_management",
        instruction="Administer return for transaction TXN-0002 only if the purchase date is within the last 90 days with the reason 'Customer return'. If so, adjust inventory for product KITCH-CHEFKNF8 to a stock level of 55, enhance customer loyalty points for CUST-5002 by adding 30 points as a service reward, and compile transactions for CUST-5002.",
        actions=[
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="ProcessReturn", kwargs={"original_transaction_id": "TXN-0002", "items_to_return": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "reason": "Customer return"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 55}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 30}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[]
    ),

    # Product Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_009_product_inventory_management",
        instruction="Access product information for ELEC-4KTV55 to evaluate current pricing. If the existing price exceeds $300, modify the price of ELEC-4KTV55 to $299.99 for competitive pricing. Compile a list of all products with a limit of 30 to assess inventory status. Obtain inventory for ELEC-4KTV55 and verify if stock is under 50. If ELEC-4KTV55 stock is under 50, adjust stock for ELEC-4KTV55 to 60 to ensure sufficient supply. List products categorized as 'Electronics' to verify category inventory. Retrieve total sales for date 2025-06-07 to evaluate business performance. If total sales exceed $1000, access product information for ELEC-4KTV55 again to verify the price update was completed successfully and that inventory is properly managed.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 299.99}),
            Action(name="ListAllProducts", kwargs={"limit": 30}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 60}),
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-07"})
        ],
        outputs=[]
    ),

    # Product Category Management
    Task(
        annotator="lucas",
        user_id="lucas_task_010_product_category",
        instruction="Compile a list of products categorized as 'Home & Kitchen' to assess category inventory. Obtain product information for HOM-COFMKR12 to evaluate current pricing. If the current price exceeds $90, modify the price of HOM-COFMKR12 to $89.99 for competitive pricing. List products categorized as 'Grocery' to confirm category inventory status. Acquire inventory for GROC-ALMBTR500 and check if stock is under 120. If GROC-ALMBTR500 stock is under 120, adjust product stock for GROC-ALMBTR500 to 100 to ensure sufficient supply. Retrieve total sales for date 2025-06-08 to evaluate business performance. If total sales surpass $600, enhance customer loyalty points for CUST-5007 by adding 50 points as a performance incentive. Compile a list of all products with a limit of 25 to verify overall inventory status.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 100}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-08"}),
            Action(name="ListAllProducts", kwargs={"limit": 25})
        ],
        outputs=[]
    ),

    # Return Processing Management

    Task(
        annotator="lucas",
        user_id="lucas_task_011_return_processing_management",
        instruction="Handle return for transaction TXN-0003 only if the purchase date falls within the last 90 days with reason 'Customer return'. If that is the case, return 1 GROC-GRNLBR12 with reason 'Customer preference', update inventory for the returned product to 15, retrieve customer details for CUST-5003, increase customer loyalty points for CUST-5003 by 15 points, obtain transaction details for TXN-0003, and list transactions for CUST-5003.",
        actions=[
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="ProcessReturn", kwargs={"original_transaction_id": "TXN-0003", "items_to_return": [{"sku": "GROC-GRNLBR12", "quantity": 1}], "reason": "Customer preference"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 15}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 15}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"})
        ],
        outputs=[]
    ),

    # Advanced Customer Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_012_advanced_customer_analytics",
        instruction="Coordinate extensive customer analytics for multiple customers at once. Retrieve customer details for CUST-5001, CUST-5002, CUST-5003, and CUST-5004. Evaluate loyalty points for all four customers. Adjust membership levels based on the analysis: CUST-5001 to 'platinum', CUST-5002 to 'gold', CUST-5003 to 'silver', CUST-5004 to 'bronze'. Compile transaction history for all customers. Obtain transaction details for TXN-0001, TXN-0002, TXN-0003, and TXN-0004. Update customer loyalty points: CUST-5001 +300, CUST-5002 +200, CUST-5003 +150, CUST-5004 +100. Document strategic sales: CUST-5001 purchases 1 ELEC-4KTV55, CUST-5002 purchases 2 AUDIO-BTSPKR02, CUST-5003 purchases 1 HOM-COFMKR12, CUST-5004 purchases 3 GROC-ALMBTR500. Acquire total sales for dates 2025-06-05 and 2025-06-06 for analysis. Confirm all customer updates were executed successfully.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5004"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5004"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5002", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5003", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5004", "new_membership_level": "bronze"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 300}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 150}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5004", "points_to_add": 100}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "HOM-COFMKR12", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "cash"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[]
    ),

    # Strategic Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_013_strategic_inventory_management",
        instruction="Implement comprehensive strategic inventory management across various product categories. Identify low stock products with a threshold of 20. Evaluate inventory levels for ELEC-4KTV55, AUDIO-BTSPKR02, HOM-COFMKR12, KITCH-CHEFKNF8, GROC-ALMBTR500, and CLTH-SLFJEAN34. Strategically update product stock: ELEC-4KTV55 to 45, AUDIO-BTSPKR02 to 35, HOM-COFMKR12 to 55, KITCH-CHEFKNF8 to 40, GROC-ALMBTR500 to 80, CLTH-SLFJEAN34 to 50. Retrieve product details for all six products. Adjust product prices based on market analysis: ELEC-4KTV55 to $799.99, AUDIO-BTSPKR02 to $169.99, HOM-COFMKR12 to $89.99, KITCH-CHEFKNF8 to $199.99, GROC-ALMBTR500 to $12.99, CLTH-SLFJEAN34 to $79.99. Sort products by category 'Electronics', 'Home & Kitchen', 'Grocery', and 'Apparel'. Introduce new product 'Strategic Inventory Monitor' in Electronics category with description 'Advanced inventory monitoring and optimization system' priced at $299.99 and with stock quantity of 25. Gather total sales for dates 2025-06-05 and 2025-06-06. Increase customer loyalty points for CUST-5005 by 400 points. Verify that all inventory updates were effectively executed.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 20}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 45}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 55}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 80}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 50}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 799.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 169.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 199.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "GROC-ALMBTR500", "new_price": 12.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 79.99}),
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Apparel"}),
            Action(name="AddNewProduct", kwargs={"name": "Strategic Inventory Monitor", "description": "Advanced inventory monitoring and optimization system", "category": "Electronics", "price": 299.99, "stock_quantity": 25}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 400}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"})
        ],
        outputs=[]
    ),

    # Inventory Restocking Management

    Task(
        annotator="lucas",
        user_id="lucas_task_014_inventory_restocking_management",
        instruction="Identify low stock products with a threshold of 15 to highlight critical inventory items. Verify if HOM-COFMKR12 appears on the low stock list. Retrieve its inventory level and increase product stock for HOM-COFMKR12 to 40. Obtain product details for HOM-COFMKR12 to confirm current pricing. Adjust price of HOM-COFMKR12 to $79.99. Sort products by category 'Home & Kitchen' to examine category inventory status. Verify if KITCH-CHEFKNF8 is also categorized as low stock. Retrieve inventory for KITCH-CHEFKNF8 and increase product stock for KITCH-CHEFKNF8 to 30. Gather total sales for date 2025-06-09 to evaluate business performance and determine restocking effectiveness.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 15}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 40}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 79.99}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 30}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-09"})
        ],
        outputs=[]
    ),

    # Sales

    Task(
        annotator="lucas",
        user_id="lucas_task_015_sales",
        instruction="Retrieve total sales for date 2025-06-05, increase loyalty points for CUST-5002 by adding 50 points, get customer details for CUST-5002, compile transactions for CUST-5002, acquire transaction details for TXN-0002, update transaction status for TXN-0002 to 'completed', check inventory for HOM-COFMKR12, and raise product stock for HOM-COFMKR12 to 35.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 50}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 35})
        ],
        outputs=[]
    ),

    # Employee Performance Management

    Task(
        annotator="lucas",
        user_id="lucas_task_016_employee_performance",
        instruction="Retrieve employee details for EMP-1002. If EMP-1002 is currently inactive, change status to 'active'. Introduce new employee Lisa Martinez as Sales Associate at STORE-001 whose phone number is +1-555-210-1015 and email is lisa.martinez@retailpos.com. If EMP-1003 is present, eliminate employee EMP-1003. Retrieve employee details for EMP-1008 to confirm the final state, and update employee status for EMP-1008 to 'active'.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            # if EMP-1002 is not currently active:
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Lisa Martinez", "role": "Sales Associate", "store_id": "STORE-001", "email": "lisa.martinez@retailpos.com", "phone_number": "+1-555-210-1015"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1003"}),
            # if EMP-1003 exists:
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            # always update EMP-1008 to active:
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "active"})
        ],
        outputs=[]
    ),

    # Customer Segmentation Analysis

    Task(
        annotator="lucas",
        user_id="lucas_task_017_customer_segmentation",
        instruction="Retrieve customer details for CUST-5006, acquire customer loyalty points for CUST-5006. Retrieve customer details for CUST-5007, obtain customer loyalty points for CUST-5007. Increase customer loyalty points for CUST-5001 by adding 50 points. Get customer details for CUST-5001. Compile transactions for CUST-5001. Acquire transaction details for TXN-0001. Adjust customer membership level for CUST-5001 to 'platinum'. Gather total sales for date 2025-06-05 to analyze customer spending behavior.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Innovation Growth Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_018_employee_management",
        instruction="Retrieve employee details for EMP-1002. If EMP-1003 is currently active, eliminate employee EMP-1003. Introduce new employee Sarah Wilson as Sales Associate at STORE-001 whose phone number is +1-555-210-1016 and email is sarah.wilson@retailpos.com. Change employee status for EMP-1004 to 'on_leave' if it is not already set. Obtain employee details for EMP-1008 to verify the final state.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1003"}),
            # if EMP-1003 is active:
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="AddEmployee", kwargs={"name": "Sarah Wilson", "role": "Sales Associate", "store_id": "STORE-001", "email": "sarah.wilson@retailpos.com", "phone_number": "+1-555-210-1016"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            # if EMP-1004 is not already on_leave:
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "on_leave"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"})
        ],
        outputs=[]
    ),

    # Inventory Audit and Reconciliation

    Task(
        annotator="lucas",
        user_id="lucas_task_019_product_innovation",
        instruction="Sort products by category 'Electronics', introduce new product 'Smart Watch Pro' in the Electronics category with description 'Advanced fitness tracking smartwatch with GPS' priced at $299.99 and with a stock quantity of 30, retrieve product details for the newly added Smart Watch Pro (ELEC-0006), increase product stock for ELEC-0006 to 30, compile all products with a limit of 50, and adjust product price for ELEC-0006 to $319.99.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Watch Pro", "description": "Advanced fitness tracking smartwatch with GPS", "category": "Electronics", "price": 299.99, "stock_quantity": 30}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-0006"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 30}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-0006", "new_price": 319.99})
        ],
        outputs=[]
    ),
    # Customer Lifecycle Management

    Task(
        annotator="lucas",
        user_id="lucas_task_020_innovation_growth",
        instruction="Sort products by category 'Sports & Outdoors' to assess current count. If the category comprises 2 or fewer products, introduce a new product 'Premium Yoga Mat' in the Sports & Outdoors category with description 'Non-slip premium yoga mat with alignment lines' priced at $89.99 and with a stock quantity of 40. Retrieve product details for the newly added Premium Yoga Mat using SKU SPOR-0003. Compile all products with a limit of 50 (within policy constraints), and gather total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="AddNewProduct", kwargs={"name": "Premium Yoga Mat", "description": "Non-slip premium yoga mat with alignment lines", "category": "Sports & Outdoors", "price": 89.99, "stock_quantity": 40}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "SPOR-0003"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Employee Management

    Task(
        annotator="lucas",
        user_id="lucas_task_021_employee",
        instruction="Retrieve employee details for EMP-1003. Should the employee status not be 'active', change it to 'active'. Enumerate all employees and count how many are present in STORE-001. If more than 2 employees work in STORE-001, introduce new employee Michael Brown as Sales Associate at STORE-002 with email michael.brown@retailpos.com and phone +1-555-210-2002. If EMP-1004 is present and has 'active' status, terminate employee EMP-1004. List all employees again and check for the existence of EMP-1008. If EMP-1008 exists and is 'active', modify the status of employee EMP-1008 to 'on_leave'. Finally, list all employees to confirm the final status.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1003"}),
            # if status != 'active':
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1003", "new_status": "active"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="AddEmployee", kwargs={"name": "Michael Brown", "role": "Sales Associate", "store_id": "STORE-002", "email": "michael.brown@retailpos.com", "phone_number": "+1-555-210-2002"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            # if EMP-1004 exists and status == 'active':
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1004"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            # if EMP-1008 exists and status == 'active':
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "on_leave"}),
            Action(name="ListAllEmployees", kwargs={})
        ],
        outputs=[]
    ),

    # Multi Store Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_022_multi_store_operations",
        instruction="Process a sale for customer CUST-5006 with 3 GROC-ALMBTR500 using a credit card. Retrieve total sales for the date 2025-06-07. Acquire customer details for CUST-5006. Determine customer loyalty points for CUST-5006. Obtain customer details for CUST-5001. Increase customer loyalty points for CUST-5001 by adding 50 points. List transactions for CUST-5001. Retrieve transaction details for TXN-0001. Change transaction status for TXN-0001 to 'completed'. Obtain total sales for date 2025-06-08 to compare with the previous total.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "credit_card"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-07"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0001", "new_status": "completed"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-08"})
        ],
        outputs=[]
    ),

    # Sales Performance Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_023_sales_performance_analytics",
        instruction="Acquire total sales for the date 2025-06-08 to evaluate daily performance. Add 150 points to customer loyalty points for CUST-5008 as a performance reward. Fetch customer details for CUST-5008 to check their status. Retrieve customer loyalty points for CUST-5008 to assess current balance. Get customer details for CUST-5002 to investigate another customer's profile. List transactions for CUST-5002 to comprehend their purchase history. Acquire transaction details for TXN-0002 to validate its status. Change transaction status for TXN-0002 to 'completed' to conclude the sale. Obtain inventory level for ELEC-4KTV55 to evaluate stock status. Adjust product stock for ELEC-4KTV55 to 48 to ensure sufficient supply. Get total sales for date 2025-06-09 to analyze performance and sales trends between the two days.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-08"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008", "points_to_add": 150}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 48}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-09"})
        ],
        outputs=[]
    ),

    # Multi Product Sales

    Task(
        annotator="lucas",
        user_id="lucas_task_024_multi_product_sales",
        instruction="Retrieve inventory for ELEC-4KTV55. If current stock is below 20, modify it to 15. Get product specifics for AUDIO-BTSPKR02. If the current price is below $140, adjust it to $139.99. Collect sales analytics for the date 2025-06-05. If the sales total surpasses $1000, increase customer loyalty points for CUST-5005 by adding 75 points. Seek customer details for CUST-5005. If this customer has fewer than 400 loyalty points, add 50 more points. Enumerate low stock products with a threshold of 10 to assess inventory needs.",
        actions=[
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            # if current_stock < 20:
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 15}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            # if current_price < 140:
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 139.99}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            # if sales_total > 1000:
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 75}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5005"}),
            # if customer.loyalty_points < 400:
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 50}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 10})
        ],
        outputs=[]
    ),

    # Cross-Segment Loyalty Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_025_cross_segment_loyalty_optimization",
        instruction="Enhance loyalty and engagement for CUST-5003: change email to loyalty3@email.com, alter phone number to +1-555-333-3333, revise address to 3 Loyalty Ave, City, ST 12345, and modify membership to VIP. Record a sale for CUST-5003 with 2 AUDIO-BTSPKR02 using a debit card, add 100 loyalty points to CUST-5003, change product price for AUDIO-BTSPKR02 to $99.99, and retrieve the latest quantity for AUDIO-BTSPKR02.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5003", "new_email": "loyalty3@email.com"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-333-3333"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5003", "new_address": "3 Loyalty Ave, City, ST 12345"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5003", "new_membership_level": "VIP"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 100}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 99.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
        ],
        outputs=[]
    ),

    # Inventory Management Complex
    Task(
        annotator="lucas",
        user_id="lucas_task_026_inventory_complex",
        instruction="Obtain inventory level for ELEC-4KTV55, assess if stock is below 30 and update it to 25 only if necessary, gather product details for ELEC-4KTV55, adjust product price for ELEC-4KTV55 to $899.99 only if the current price differs, acquire inventory level for AUDIO-BTSPKR02, modify product stock for AUDIO-BTSPKR02 to 40 only if the current stock varies, record a sale for customer CUST-5003 with 1 ELEC-4KTV55 using a credit card, and acquire total sales for the date 2025-06-05.",
        actions=[
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 25}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 899.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Customer Account Management

    Task(
        annotator="lucas",
        user_id="lucas_task_027_customer_account",
        instruction="Retrieve customer details for CUST-5007, modify customer address for CUST-5007 to '123 New Street, Updated City, UC 12345', change customer phone number for CUST-5007 to '+1-555-123-4567', obtain customer loyalty points for CUST-5007, enhance loyalty points for CUST-5007 by adding 200 points, upgrade membership level for CUST-5007 to 'gold', list transactions for CUST-5007, acquire transaction details for TXN-0005, and change customer email for CUST-5007 to 'updated.customer@email.com'.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5007", "new_address": "123 New Street, Updated City, UC 12345"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5007", "new_phone_number": "+1-555-123-4567"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007", "points_to_add": 200}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5007", "new_membership_level": "gold"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5007"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0005"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5007", "new_email": "updated.customer@email.com"})
        ],
        outputs=[]
    ),

    # Multi Store Employee Coordination

    Task(
        annotator="lucas",
        user_id="lucas_task_028_multi_store_employees",
        instruction="Acquire employee details for EMP-1004, alter employee status for EMP-1004 to 'active', onboard new employee Carlos Rodriguez as Store Manager at STORE-001 with email carlos.rodriguez@retailpos.com and phone +1-555-210-1017, enumerate all employees to confirm the addition, obtain employee details for EMP-1009, modify employee status for EMP-1009 to 'on_leave', gather employee details for EMP-1011, and change employee status for EMP-1011 to 'active'.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Carlos Rodriguez", "role": "Store Manager", "store_id": "STORE-001", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-1017"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "on_leave"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1011"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1011", "new_status": "active"})
        ],
        outputs=[]
    ),

    # Complex Sales Transaction

    Task(
        annotator="lucas",
        user_id="lucas_task_029_customer_service_workflow",
        instruction="Retrieve customer details for CUST-5012, present transactions for CUST-5012, obtain transaction details for TXN-0012, change transaction status for TXN-0012 to 'refunded', enhance customer loyalty points for CUST-5012 by adding 50 points, modify customer membership level for CUST-5012 to 'silver', update customer email for CUST-5012 to 'service.customer@email.com', reacquire customer details for CUST-5012, and change customer phone number for CUST-5012 to '+1-555-999-8888'.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0012", "new_status": "refunded"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 50}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5012", "new_email": "service.customer@email.com"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-999-8888"})
        ],
        outputs=[]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_030_advanced_customer",
        instruction="Retrieve customer details for CUST-5001, revise customer address for CUST-5001 to '456 Advanced Street, Customer City, CC 45678', modify customer phone number for CUST-5001 to '+1-555-456-7890', obtain customer loyalty points for CUST-5001, increase loyalty points for CUST-5001 by adding 400 points, upgrade membership level for CUST-5001 to 'platinum', list transactions for CUST-5001, collect transaction details for TXN-0001, and update customer email for CUST-5001 to 'advanced.customer@email.com'.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5001", "new_address": "456 Advanced Street, Customer City, CC 45678"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5001", "new_phone_number": "+1-555-456-7890"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 400}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5001", "new_email": "advanced.customer@email.com"})
        ],
        outputs=[]
    ),

    # Inventory Optimization
    Task(
        annotator="lucas",
        user_id="lucas_task_031_inventory_optimization",
        instruction="Identify products with low stock at a threshold of 35, retrieve inventory level for CLTH-SLFJEAN34, set product stock for CLTH-SLFJEAN34 to 60, obtain product details for CLTH-SLFJEAN34, change product price for CLTH-SLFJEAN34 to $89.99, retrieve inventory level for KITCH-CHEFKNF8, adjust product stock for KITCH-CHEFKNF8 to 50, categorize products under 'Sports & Outdoors', and register a sale for customer CUST-5010 with 1 CLTH-SLFJEAN34 using cash.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 35}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 60}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 89.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 50}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5010", "items": [{"sku": "CLTH-SLFJEAN34", "quantity": 1}], "payment_method": "cash"})
        ],
        outputs=[]
    ),

    # Employee Training Program

    Task(
        annotator="lucas",
        user_id="lucas_task_032_employee_training",
        instruction="Retrieve details for employee EMP-1032, change employee status for EMP-1032 to 'training', onboard new employee Lisa Martinez as Trainer at STORE-005 with email lisa.martinez@retailpos.com and phone +1-555-210-2007, obtain employee details for EMP-1034, change employee status for EMP-1034 to 'certified', list all employees, terminate employee EMP-1015, re-list all employees, and retrieve details for employee EMP-1020.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1032"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1032", "new_status": "training"}),
            Action(name="AddEmployee", kwargs={"name": "Lisa Martinez", "role": "Trainer", "store_id": "STORE-005", "email": "lisa.martinez@retailpos.com", "phone_number": "+1-555-210-2007"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1034"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1034", "new_status": "certified"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1015"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[]
    ),

    # Multi Category Sales Analysis

    Task(
        annotator="lucas",
        user_id="lucas_task_033_customer_loyalty_enhancement",
        instruction="Retrieve details for customer CUST-5012, check loyalty points for CUST-5012, increase loyalty points for CUST-5012 by 250 points, elevate membership level for CUST-5012 to 'gold', update customer email for CUST-5012 to 'loyalty.customer@email.com', list transactions for CUST-5012, obtain transaction details for TXN-0001, change transaction status for TXN-0001 to 'completed', and register a sale for CUST-5012 with 1 GROC-ALMBTR500 using debit card.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 250}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5012", "new_email": "loyalty.customer@email.com"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0001", "new_status": "completed"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "GROC-ALMBTR500", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[]
    ),

    # Comprehensive Store Audit
    Task(
        annotator="lucas",
        user_id="lucas_task_034_comprehensive_audit",
        instruction="Compile a list of all employees, fetch details for employee EMP-1002, change employee status for EMP-1002 to 'audited', list all products capping at 50 (within policy limit), retrieve inventory level for HOM-COFMKR12, adjust product stock for HOM-COFMKR12 to 80, acquire product details for HOM-COFMKR12, update product price for HOM-COFMKR12 to $24.99, fetch total sales for date 2025-06-05, retrieve details for customer CUST-5001, and acquire product details for ELEC-4KTV55.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "audited"}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 80}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 24.99}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"})
        ],
        outputs=[]
    ),

    # Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_035_customer_relationship",
        instruction="Retrieve details for customer CUST-5002, change customer address for CUST-5002 to '789 Relationship Street, Customer City, RC 78901', update customer phone number for CUST-5002 to '+1-555-789-0123', check customer loyalty points for CUST-5002, increase loyalty points for CUST-5002 by adding 350 points, elevate membership level for CUST-5002 to 'platinum', list transactions for CUST-5002, and register a sale for CUST-5002 with 1 ELEC-4KTV55 using credit card.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5002", "new_address": "789 Relationship Street, Customer City, RC 78901"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5002", "new_phone_number": "+1-555-789-0123"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 350}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5002", "new_membership_level": "platinum"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"})
        ],
        outputs=[]
    ),

    # Inventory Rebalancing Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_036_inventory_rebalancing",
        instruction="Identify low stock products at a threshold of 40, retrieve inventory level for AUDIO-BTSPKR02, set product stock for AUDIO-BTSPKR02 to 60, obtain product details for AUDIO-BTSPKR02, change product price for AUDIO-BTSPKR02 to $189.99, retrieve inventory level for KITCH-CHEFKNF8, adjust product stock for KITCH-CHEFKNF8 to 45, and register a sale for customer CUST-5010 with 1 AUDIO-BTSPKR02 using debit card.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 40}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 60}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 189.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 45}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5010", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[]
    ),

    # Customer Data Migration

    Task(
        annotator="lucas",
        user_id="lucas_task_037_customer_migration",
        instruction="Coordinate comprehensive migration of customer data for CUST-5003: retrieve customer details, update email to migrated.customer@newdomain.com, change address to 456 Migration Street, New City, NC 45678, update phone to +1-555-456-7890, check loyalty points, add 75 points if below 1000, adjust membership to silver, list transactions, obtain transaction details for TXN-0003, list transactions by customer, retrieve customer details again, check customer loyalty points again, and confirm all migration updates.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5003", "new_email": "migrated.customer@newdomain.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5003", "new_address": "456 Migration Street, New City, NC 45678"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-456-7890"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 75}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5003", "new_membership_level": "silver"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003"})
        ],
        outputs=[]
    ),

    # Staff Reorganization Management

    Task(
        annotator="lucas",
        user_id="lucas_task_038_staff_reorganization",
        instruction="Retrieve employee details for EMP-1008, update employee status for EMP-1008 to 'active', onboard new employee Maria Garcia as Senior Sales Associate at STORE-001 with email maria.garcia@retailpos.com and phone +1-555-210-1019, verify the addition by listing all employees, retrieve employee details for EMP-1011, change employee status for EMP-1011 to 'promoted', obtain employee details for EMP-1015, and update employee status for EMP-1015 to 'active'.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Maria Garcia", "role": "Senior Sales Associate", "store_id": "STORE-001", "email": "maria.garcia@retailpos.com", "phone_number": "+1-555-210-1019"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1011"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1011", "new_status": "promoted"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1015", "new_status": "active"})
        ],
        outputs=[]
    ),

    # Complex Return Processing

    Task(
        annotator="lucas",
        user_id="lucas_task_039_complex_return",
        instruction="Retrieve customer details for CUST-5011, list transactions for CUST-5011, obtain transaction details for TXN-0011, change transaction status for TXN-0011 to 'refunded', increase customer loyalty points for CUST-5011 by adding 50 points, change customer membership level for CUST-5011 to 'silver', update customer email for CUST-5011 to 'return.customer@email.com', retrieve customer details for CUST-5011 again, and change customer phone number for CUST-5011 to '+1-555-777-6666'.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5011"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5011"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0011"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0011", "new_status": "refunded"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 50}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5011", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5011", "new_email": "return.customer@email.com"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5011"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5011", "new_phone_number": "+1-555-777-6666"})
        ],
        outputs=[]
    ),

       # Product Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_040_product_expansion",
        instruction="Categorize products under 'Home & Kitchen' to assess current inventory. Due to the presence of more than 3 products in the category, assess customer data and sales performance instead. Obtain details for customers CUST-5001 and CUST-5002, increase customer loyalty points for CUST-5001 by adding 50 points, augment customer loyalty points for CUST-5002 by adding 75 points, list transactions for both customers, obtain transaction details for TXN-0001 and TXN-0002, and gather total sales for dates 2025-06-05 and 2025-06-06 to assess performance.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 75}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"})
        ],
        outputs=[]
    ),

     # Seasonal Inventory Management

    Task(
        annotator="lucas",
        user_id="lucas_task_041_seasonal_inventory",
        instruction="Identify low stock products with a threshold of 45, retrieve the inventory level for SPORT-BIKHLM01, adjust product stock for SPORT-BIKHLM01 to 75, obtain product details for SPORT-BIKHLM01, revise product price for SPORT-BIKHLM01 to $69.99, retrieve inventory level for CLTH-SLFJEAN34, adjust product stock for CLTH-SLFJEAN34 to 55, and document a sale for customer CUST-5011 with 1 SPORT-BIKHLM01 using a debit card.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 45}),
            Action(name="GetInventoryLevel", kwargs={"sku": "SPORT-BIKHLM01"}),
            Action(name="UpdateProductStock", kwargs={"sku": "SPORT-BIKHLM01", "new_stock_quantity": 75}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "SPORT-BIKHLM01"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "SPORT-BIKHLM01", "new_price": 69.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 55}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5011", "items": [{"sku": "SPORT-BIKHLM01", "quantity": 1}], "payment_method": "debit_card"})
        ],
        outputs=[]
    ),

    # Employee Performance Review
    Task(
        annotator="lucas",
        user_id="lucas_task_042_performance_review",
        instruction="Retrieve employee details for EMP-1008. Modify employee status for EMP-1008 to 'under_review'. Retrieve employee details for EMP-1009. Modify employee status for EMP-1009 to 'excellent'. Appoint Carlos Rodriguez as Performance Analyst at STORE-003 with email carlos.rodriguez@retailpos.com and phone +1-555-210-1017. Compile a full list of employees to verify the workforce. Retrieve employee details for EMP-1032. Modify employee status for EMP-1032 to 'on_leave'. Compile a full list of employees once more to confirm changes. Retrieve employee details for EMP-1020 for the final review.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "under_review"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "excellent"}),
            Action(name="AddEmployee", kwargs={"name": "Carlos Rodriguez", "role": "Performance Analyst", "store_id": "STORE-003", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-1017"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1032"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1032", "new_status": "on_leave"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[]
    ),

    # Cross Category Sales Campaign

    Task(
        annotator="lucas",
        user_id="lucas_task_043_cross_category_campaign",
        instruction="Compile products categorized under 'Electronics', compile products categorized under 'Grocery', retrieve product details for GROC-ALMBTR500, adjust product price for GROC-ALMBTR500 to $9.99, retrieve inventory level for GROC-ALMBTR500, adjust product stock for GROC-ALMBTR500 to 85, document a sale for customer CUST-5009 with 1 ELEC-4KTV55 and 3 GROC-ALMBTR500 using a credit card, update customer loyalty points for CUST-5009 by adding 175 points, and retrieve customer details for CUST-5009.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "GROC-ALMBTR500", "new_price": 9.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 85}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "GROC-ALMBTR500", "quantity": 3}], "payment_method": "credit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 175}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5009"})
        ],
        outputs=[]
    ),

    # Employee Management

    Task(
        annotator="lucas",
        user_id="lucas_task_044_product_distribution",
        instruction="Compile products categorized under 'Sports & Outdoors', retrieve inventory level for CLTH-SLFJEAN34, adjust product stock for CLTH-SLFJEAN34 to 45, retrieve product details for CLTH-SLFJEAN34, revise product price for CLTH-SLFJEAN34 to $94.99, introduce a new product 'Sports Water Bottle' in the Sports & Outdoors category with description 'Insulated stainless steel water bottle' at a price of $19.99 and stock quantity of 50, compile a list of products in 'Sports & Outdoors' again to confirm the addition, and retrieve inventory level for SPORT-BIKHLM01 to verify the existing product stock.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 45}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 94.99}),
            Action(name="AddNewProduct", kwargs={"name": "Sports Water Bottle", "description": "Insulated stainless steel water bottle", "category": "Sports & Outdoors", "price": 19.99, "stock_quantity": 50}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "SPORT-BIKHLM01"})
        ],
        outputs=[]
    ),

    # Advanced Transaction Management

    Task(
        annotator="lucas",
        user_id="lucas_task_045_transaction_management",
        instruction="Retrieve customer details for CUST-5012, compile a list of transactions for CUST-5012, retrieve transaction details for TXN-0001, modify transaction status for TXN-0001 to 'pending', compile a list of transactions for CUST-5012 again, retrieve transaction details for TXN-0012, update customer loyalty points for CUST-5012 by adding 60 points, retrieve customer details for CUST-5012 again, obtain customer loyalty points for CUST-5012 to verify the update, compile a list of low stock products with a threshold of 30, and calculate total sales for the date 2025-06-05.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0001", "new_status": "pending"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 60}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012"}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 30}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),
    # Comprehensive Business Intelligence

    Task(
        annotator="lucas",
        user_id="lucas_task_046_business_intelligence",
        instruction="Compile a list of all employees, compile a list of all products with a limit of 50 (within policy limit), identify low stock products with a threshold of 70, calculate total sales for the date 2025-06-05, retrieve customer details for CUST-5001, retrieve customer details for CUST-5002. Update customer loyalty points for CUST-5001 by adding 150 points. Update customer loyalty points for CUST-5002 by adding 100 points. Calculate total sales for the date 2025-06-05 again to compare with the initial total. Obtain customer loyalty points for CUST-5001. Retrieve product details for ELEC-4KTV55 and update customer loyalty points for CUST-5002 by adding 200 points.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 70}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 150}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 100}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 200})
        ],
        outputs=[]
    ),

    # Strategic Resource Reallocation

    Task(
        annotator="lucas",
        user_id="lucas_task_047_strategic_reallocation",
        instruction="Compile a list of all employees, retrieve employee details for EMP-1008, modify employee status for EMP-1008 to 'promoted', add a new employee David Wilson as Strategic Analyst at STORE-001 with email david.wilson@retailpos.com and phone +1-555-210-1020, compile a list of all employees to confirm the addition, retrieve employee details for EMP-1011, modify employee status for EMP-1011 to 'active' only if not already active, modify employee status for EMP-1015 to 'terminated' only if currently active, and retrieve employee details for EMP-1020 to confirm the final state.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="AddEmployee", kwargs={"name": "David Wilson", "role": "Strategic Analyst", "store_id": "STORE-001", "email": "david.wilson@retailpos.com", "phone_number": "+1-555-210-1020"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1011"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1011", "new_status": "active"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1015", "new_status": "terminated"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[]
    ),

    # Customer Journey Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_048_customer_journey",
        instruction="Retrieve customer details for CUST-5004, modify customer email for CUST-5004 to 'journey.customer@optimized.com', update customer address for CUST-5004 to '789 Journey Lane, Optimized City, OC 78901', obtain customer loyalty points for CUST-5004, adjust loyalty points for CUST-5004 by adding 400 points, elevate membership level for CUST-5004 to 'platinum', document a sale for customer CUST-5004 with 1 ELEC-4KTV55 using a debit card, compile transactions for CUST-5004, and retrieve customer details for CUST-5004 again.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5004"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5004", "new_email": "journey.customer@optimized.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5004", "new_address": "789 Journey Lane, Optimized City, OC 78901"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5004"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5004", "points_to_add": 400}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5004", "new_membership_level": "platinum"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5004", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5004"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[]
    ),

    # Workforce Development Program

    Task(
        annotator="lucas",
        user_id="lucas_task_049_workforce_development",
        instruction="Retrieve employee details for EMP-1015. Modify employee status for EMP-1015 to 'active'. Add a new employee Jennifer Garcia as Training Coordinator at STORE-001 with email jennifer.garcia@retailpos.com and phone +1-555-210-1018. Compile a list of all employees to confirm the addition. Retrieve employee details for EMP-1020. Modify employee status for EMP-1020 to 'certified'. Retrieve employee details for EMP-1032. Modify employee status for EMP-1032 to 'active'.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1015", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Jennifer Garcia", "role": "Training Coordinator", "store_id": "STORE-001", "email": "jennifer.garcia@retailpos.com", "phone_number": "+1-555-210-1018"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1020", "new_status": "certified"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1032"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1032", "new_status": "active"})
        ],
        outputs=[]
    ),

    # Advanced Return Processing
    Task(
        annotator="lucas",
        user_id="lucas_task_050_advanced_return",
        instruction="Conduct comprehensive advanced return processing for transaction TXN-0012: retrieve transaction details, obtain customer details for CUST-5012, compile transactions by customer, process return if within 90 days with reason 'Customer return', modify transaction status to refunded, adjust customer membership level to silver, update customer phone number to +1-555-555-4444, update customer loyalty points by adding 50, retrieve customer details again, obtain customer loyalty points, update customer email to return.customer@email.com, update customer address to 789 Return Street, Return City, RC 78901, compile transactions by customer again, retrieve transaction details again, adjust customer membership level to silver, update customer loyalty points by adding 25 more points, and confirm all return processing updates.",
        actions=[
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="ProcessReturn", kwargs={"original_transaction_id": "TXN-0012", "items_to_return": [{"sku": "SPORT-BIKHLM01", "quantity": 1}], "reason": "Customer return"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0012", "new_status": "refunded"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-555-4444"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 50}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5012", "new_email": "return.customer@email.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5012", "new_address": "789 Return Street, Return City, RC 78901"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0012"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 25})
        ],
        outputs=[]
    ),

    # Product Innovation Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_051_customer_lifecycle",
        instruction="Handle thorough customer lifecycle management for CUST-5007 and CUST-5008: retrieve customer details for CUST-5007, elevate membership level to platinum, acquire loyalty points for CUST-5007, supplement 500 points if below 1000, revise phone number to +1-555-444-3333, retrieve customer details for CUST-5008, elevate membership level to gold, document sale for CUST-5007 with 1 ELEC-4KTV55 using credit card, compile transactions for CUST-5007, obtain transaction details for TXN-0007, update customer email for CUST-5007 to lifecycle.customer@email.com, modify customer address for CUST-5007 to 456 Lifecycle Ave, Lifecycle City, LC 45678, amend customer loyalty points for CUST-5007 by adding 100 more points, adjust customer membership level for CUST-5008 to gold, fetch customer details for CUST-5007 again, and confirm all lifecycle updates.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5007", "new_membership_level": "platinum"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007", "points_to_add": 500}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5007", "new_phone_number": "+1-555-444-3333"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5007"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0007"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5007", "new_email": "lifecycle.customer@email.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5007", "new_address": "456 Lifecycle Ave, Lifecycle City, LC 45678"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007", "points_to_add": 100}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"})
        ],
        outputs=[]
    ),

    # Supply Chain Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_052_supply_chain",
        instruction="Compile all products with a limit of 50, fetch product details for ELEC-4KTV55, modify product price for ELEC-4KTV55 to $799.99, acquire inventory level for ELEC-4KTV55, revise product stock for ELEC-4KTV55 to 45, introduce new product 'Smart Thermostat' in Electronics category with description 'WiFi-enabled smart thermostat with energy saving features' and price $199.99 and stock quantity 25, and retrieve product details for the newly introduced Smart Thermostat.",
        actions=[
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 799.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 45}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Thermostat", "description": "WiFi-enabled smart thermostat with energy saving features", "category": "Electronics", "price": 199.99, "stock_quantity": 25}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-0006"})
        ],
        outputs=[]
    ),

    # Employee Excellence Program

    Task(
        annotator="lucas",
        user_id="lucas_task_053_employee_excellence",
        instruction="Retrieve employee details for EMP-1009, modify employee status for EMP-1009 to 'excellence_program', fetch employee details for EMP-1008, change employee status for EMP-1008 to 'top_performer', enlist new employee Patricia Davis as Excellence Coach at STORE-001 with email patricia.davis@retailpos.com and phone +1-555-210-1019, compile all employees, eliminate employee EMP-1009, compile all employees once more, and retrieve employee details for EMP-1020.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "excellence_program"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "top_performer"}),
            Action(name="AddEmployee", kwargs={"name": "Patricia Davis", "role": "Excellence Coach", "store_id": "STORE-001", "email": "patricia.davis@retailpos.com", "phone_number": "+1-555-210-1019"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1009"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"})
        ],
        outputs=[]
    ),

    # Market Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_054_market_expansion",
        instruction="Retrieve customer details for CUST-5009. Change membership level for CUST-5009 to 'platinum'. Enhance customer loyalty points for CUST-5009 by adding 400 points. Revise customer email for CUST-5009 to 'expansion.customer@market.com'. Alter customer address for CUST-5009 to '789 Expansion Blvd, Market City, MC 78901'. Compile transactions for CUST-5009. Obtain transaction details for TXN-0009. Acquire customer loyalty points for CUST-5009. Adjust customer loyalty points for CUST-5009 by adding 100 more points. Retrieve customer details for CUST-5009 again to validate all updates.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5009"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5009", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 400}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5009", "new_email": "expansion.customer@market.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5009", "new_address": "789 Expansion Blvd, Market City, MC 78901"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5009"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0009"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 100}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5009"})
        ],
        outputs=[]
    ),



    # Customer Experience Enhancement

    Task(
        annotator="lucas",
        user_id="lucas_task_055_customer_experience",
        instruction="Acquire customer details for CUST-5008, revise customer email for CUST-5008 to 'experience.customer@enhanced.com', modify customer address for CUST-5008 to '456 Experience Street, Enhanced City, EC 45678', obtain customer loyalty points for CUST-5008, enhance loyalty points for CUST-5008 by adding 350 points, adjust membership level for CUST-5008 to 'gold', document sale for CUST-5008 with 1 AUDIO-BTSPKR02 using debit card, compile transactions for CUST-5008, and retrieve customer details for CUST-5008 once more.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5008", "new_email": "experience.customer@enhanced.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5008", "new_address": "456 Experience Street, Enhanced City, EC 45678"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008", "points_to_add": 350}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5008", "new_membership_level": "gold"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5008", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5008"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"})
        ],
        outputs=[]
    ),

    # Operational Excellence Audit

    Task(
        annotator="lucas",
        user_id="lucas_task_056_relationship_excellence",
        instruction="Acquire customer details for CUST-5011, obtain customer loyalty points for CUST-5011, amend loyalty points for CUST-5011 by adding 600 points, change membership level for CUST-5011 to 'platinum', modify customer address for CUST-5011 to '321 Excellence Drive, Relationship City, RC 32100', update customer email for CUST-5011 to 'excellence.customer@relationship.com', revise customer phone number for CUST-5011 to '+1-555-333-2222', and retrieve customer details for CUST-5011 again.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5011"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 600}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5011", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5011", "new_address": "321 Excellence Drive, Relationship City, RC 32100"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5011", "new_email": "excellence.customer@relationship.com"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5011", "new_phone_number": "+1-555-333-2222"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[]
    ),



    # Comprehensive Business Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_057_business_analytics",
        instruction="Obtain total sales for date 2025-06-05, compile all employees, list all products with limit 50 (within policy limit), retrieve customer details for CUST-5001, gather customer details for CUST-5005, adjust customer membership level for CUST-5001 to 'platinum', modify customer membership level for CUST-5005 to 'gold', obtain total sales for date 2025-06-05 again, compile low stock products with a threshold of 50, acquire customer loyalty points for CUST-5001 to verify the update, retrieve product details for ELEC-4KTV55, and enhance customer loyalty points for CUST-5005 by adding 150 points.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5005"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5005", "new_membership_level": "gold"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 50}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 150})
        ],
        outputs=[]
    ),

    # Strategic Portfolio Management
    Task(
        annotator="lucas",
        user_id="lucas_task_058_product_expansion",
        instruction="Compile products by category 'Home & Kitchen', introduce new product 'Smart Coffee Maker' in Home & Kitchen category with description 'Programmable coffee maker with smartphone control' and price $199.99 and stock quantity 25, fetch product details for the newly introduced Smart Coffee Maker (HOME-0006), modify product stock for HOME-0006 to 25, compile all products with limit 50 (within policy limit), adjust customer loyalty points for CUST-5005 by adding 200 points, and obtain total sales for date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Coffee Maker", "description": "Programmable coffee maker with smartphone control", "category": "Home & Kitchen", "price": 199.99, "stock_quantity": 25}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOME-0006"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 25}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 200}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Premium Customer Onboarding

    Task(
        annotator="lucas",
        user_id="lucas_task_059_product_innovation",
        instruction="Compile products by category 'Electronics', introduce new product 'Smart Watch Pro' in Electronics category with description 'Advanced fitness tracking smartwatch with GPS' and price $299.99 and stock quantity 30, retrieve product details for the newly introduced Smart Watch Pro, modify product stock for the newly introduced Smart Watch Pro to 30, compile all products with limit 50, adjust customer loyalty points for CUST-5006 by adding 300 points, and obtain total sales for date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Watch Pro", "description": "Advanced fitness tracking smartwatch with GPS", "category": "Electronics", "price": 299.99, "stock_quantity": 30}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-0006"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 30}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 300}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Supply Chain Optimization
    Task(
        annotator="lucas",
        user_id="lucas_task_060_innovation_growth",
        instruction="Compile products by category 'Sports & Outdoors', introduce new product 'Fitness Tracker Pro' in Sports & Outdoors category with description 'Advanced fitness tracking device with heart rate monitor' and price $149.99 and stock quantity 40, fetch product details for the newly introduced Fitness Tracker Pro, modify product stock for the newly introduced Fitness Tracker Pro to 40, adjust product stock for the newly introduced Fitness Tracker Pro to 55, compile all products with limit 50, enhance customer loyalty points for CUST-5012 by adding 250 points, and obtain total sales for date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="AddNewProduct", kwargs={"name": "Fitness Tracker Pro", "description": "Advanced fitness tracking device with heart rate monitor", "category": "Sports & Outdoors", "price": 149.99, "stock_quantity": 40}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "SPOR-0003"}),
            Action(name="UpdateProductStock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 55}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 250}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Strategic Customer Portfolio

    Task(
        annotator="lucas",
        user_id="lucas_task_061_employee_performance",
        instruction="Retrieve employee details for EMP-1002, confirm if EMP-1002 is presently active, compile a list of all employees to verify current counts, onboard a new employee Jennifer Davis as Manager at STORE-001 with email jennifer.davis@retailpos.com and phone +1-555-210-2003 (assign ID EMP-1013), obtain employee details for EMP-1004 and determine if they are on leave, revise employee status for EMP-1004 to 'on_leave' only if they are not already on leave, remove employee EMP-1003 only if they are present, recheck the employee list to confirm changes, and retrieve employee details for EMP-1008 to validate the final state.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="AddEmployee", kwargs={"name": "Jennifer Davis", "role": "Manager", "store_id": "STORE-001", "email": "jennifer.davis@retailpos.com", "phone_number": "+1-555-210-2003"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "on_leave"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"})
        ],
        outputs=[]
    ),

    # Multi Store Employee Operations

    Task(
        annotator="lucas",
        user_id="lucas_task_062_product_expansion",
        instruction="Examine current inventory levels for the Electronics category, subsequently add a new product 'Smart Home Hub' in the Electronics category with description 'Centralized smart home control system with voice assistant', set the price at $399.99, and stock quantity at 15, retrieve product details for the newly added Smart Home Hub (ELEC-0006), adjust product stock for ELEC-0006 to 20, list all products with a limit of 50 (within policy limits), enhance customer loyalty points for CUST-5007 by adding 350 points, and gather total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Home Hub", "description": "Centralized smart home control system with voice assistant", "category": "Electronics", "price": 399.99, "stock_quantity": 15}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-0006"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-0006", "new_stock_quantity": 20}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007", "points_to_add": 350}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Seasonal Inventory Adjustment

    Task(
        annotator="lucas",
        user_id="lucas_task_063_product_innovation",
        instruction="Assess current inventory levels for the Sports & Outdoors category, then introduce a new product 'Premium Yoga Mat' in the Sports & Outdoors category with description 'Non-slip premium yoga mat with alignment lines and carrying strap', price set at $89.99, and stock quantity at 40, obtain product details for the newly introduced Premium Yoga Mat (SPOR-0003), modify product stock for SPOR-0003 to 45, list all products with a cap of 50, augment customer loyalty points for CUST-5008 by adding 150 points, and compile total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="AddNewProduct", kwargs={"name": "Premium Yoga Mat", "description": "Non-slip premium yoga mat with alignment lines and carrying strap", "category": "Sports & Outdoors", "price": 89.99, "stock_quantity": 40}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "SPOR-0003"}),
            Action(name="UpdateProductStock", kwargs={"sku": "SPOR-0003", "new_stock_quantity": 45}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008", "points_to_add": 150}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Supply Chain Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_064_innovation_growth",
        instruction="Inspect current inventory levels for the Home & Kitchen category, then add a new product 'Smart Refrigerator' in the Home & Kitchen category with description 'WiFi-enabled refrigerator with touchscreen and inventory tracking', priced at $1299.99 with a stock quantity of 8, acquire product details for the newly added Smart Refrigerator (HOME-0006), elevate product stock for HOME-0006 to 10, further update product stock for HOME-0006 to 12, compile a list of all products with a limit of 50, increase customer loyalty points for CUST-5010 by adding 500 points, and gather total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="AddNewProduct", kwargs={"name": "Smart Refrigerator", "description": "WiFi-enabled refrigerator with touchscreen and inventory tracking", "category": "Home & Kitchen", "price": 1299.99, "stock_quantity": 8}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOME-0006"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 10}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOME-0006", "new_stock_quantity": 12}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5010", "points_to_add": 500}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Strategic Customer Portfolio

    Task(
        annotator="lucas",
        user_id="lucas_task_065_product_restocking",
        instruction="Compile a list of low stock products with a threshold of 10. Acquire product details for ELEC-RCHAA04. Classify products by category 'Electronics'. Retrieve inventory level for ELEC-4KTV55. Raise product stock for ELEC-4KTV55 to 75. Gather total sales for the date 2025-06-05. Increase customer loyalty points for CUST-5001 by adding 25 points. Obtain customer details for CUST-5001. List transactions for CUST-5001. Retrieve transaction details for TXN-0001. Alter product price for ELEC-RCHAA04 to $18.95. Obtain inventory level for KITCH-CHEFKNF8. Adjust product stock for KITCH-CHEFKNF8 to 40.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 10}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-RCHAA04"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 75}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 25}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-RCHAA04", "new_price": 18.95}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 40})
        ],
        outputs=[]
    ),

    # Customer Loyalty Management

    Task(
        annotator="lucas",
        user_id="lucas_task_066_customer_loyalty_management",
        instruction="Obtain customer details for CUST-5005, check loyalty points for CUST-5005. Modify membership level for CUST-5005 to 'silver'. Retrieve customer details for CUST-5001. Increase customer loyalty points for CUST-5001 by adding 30 points. Get transaction details for TXN-0004. Change customer email for CUST-5005 to 'loyalty.customer@email.com'. Update customer phone number for CUST-5005 to '+1-555-987-6543'. Retrieve customer loyalty points for CUST-5001. List transactions for CUST-5001. Get transaction details for TXN-0001. Change customer membership level for CUST-5001 to 'gold'.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5005"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5005", "new_membership_level": "silver"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 30}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0004"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5005", "new_email": "loyalty.customer@email.com"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5005", "new_phone_number": "+1-555-987-6543"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0001"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5001", "new_membership_level": "gold"})
        ],
        outputs=[]
    ),

    # Employee Performance Management
    Task(
        annotator="lucas",
        user_id="lucas_task_067_employee_performance_management",
        instruction="Obtain employee details for EMP-1002. Change employee status for EMP-1002 to 'active'. Compile a list of all employees. Onboard Jennifer Davis as Manager at STORE-001 with email 'jennifer.davis@store.com' and phone '+1-555-210-2003'. Modify employee status for EMP-1003 to 'active'. Retrieve employee details for EMP-1004. Recheck the employee list to confirm changes. Revise employee status for EMP-1008 to 'on_leave'. List all employees to validate final workforce status. Adjust employee status for EMP-1009 to 'active'.",
        actions=[
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "active"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="AddEmployee", kwargs={"name": "Jennifer Davis", "role": "Manager", "store_id": "STORE-001", "email": "jennifer.davis@store.com", "phone_number": "+1-555-210-2003"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1003", "new_status": "active"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "on_leave"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "active"})
        ],
        outputs=[]
    ),
    # Customer Relationship Excellence
    Task(
        annotator="lucas",
        user_id="lucas_task_068_strategic_portfolio",
        instruction="Handle comprehensive strategic portfolio management for CUST-5003: gather customer details, elevate membership level to platinum, acquire customer loyalty points, increase by 500 points if below 1000, document sale with 1 ELEC-4KTV55 using credit card, list transactions by customer, retrieve transaction details for TXN-0003, change customer email to portfolio.customer@strategic.com, update customer address to 123 Portfolio Street, Strategic City, SC 12345, obtain customer details again, check customer loyalty points again, update customer phone number to +1-555-333-2222, adjust customer loyalty points by adding 200 more points, relist transactions by customer, retrieve transaction details again, elevate customer membership level to platinum, and verify all strategic portfolio updates.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5003", "new_membership_level": "platinum"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 500}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5003", "new_email": "portfolio.customer@strategic.com"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5003", "new_address": "123 Portfolio Street, Strategic City, SC 12345"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5003", "new_phone_number": "+1-555-333-2222"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 200}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0003"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5003", "new_membership_level": "platinum"})
        ],
        outputs=[]
    ),

    # Strategic Inventory Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_069_multi_store_employees",
        instruction="Compile a list of all employees, retrieve employee details for EMP-1008, revise employee status for EMP-1008 to 'promoted', onboard a new employee Sarah Johnson as Supervisor at STORE-002 with email sarah.johnson@retailpos.com and phone +1-555-210-2004, acquire employee details for EMP-1009, adjust employee status for EMP-1009 to 'active', add a new employee Mark Wilson as Sales Associate at STORE-003 with email mark.wilson@retailpos.com and phone +1-555-210-2005, remove employee EMP-1011, recheck the employee list, and retrieve employee details for EMP-1015.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="AddEmployee", kwargs={"name": "Sarah Johnson", "role": "Supervisor", "store_id": "STORE-002", "email": "sarah.johnson@retailpos.com", "phone_number": "+1-555-210-2004"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Mark Wilson", "role": "Sales Associate", "store_id": "STORE-003", "email": "mark.wilson@retailpos.com", "phone_number": "+1-555-210-2005"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1011"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"})
        ],
        outputs=[]
    ),


    # Store Operations Management

    Task(
        annotator="lucas",
        user_id="lucas_task_070_store_operations",
        instruction="Compile a list of all employees, onboard a new employee David Brown as Manager at STORE-004 with email david.brown@retailpos.com and phone +1-555-210-2006, retrieve employee details for EMP-1020, revise employee status for EMP-1020 to 'manager', compile a list of low stock products with a threshold of 30, obtain inventory level for GROC-ALMBTR500, adjust product stock for GROC-ALMBTR500 to 75, retrieve product details for GROC-ALMBTR500, modify product price for GROC-ALMBTR500 to $8.99, and gather total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="AddEmployee", kwargs={"name": "David Brown", "role": "Manager", "store_id": "STORE-004", "email": "david.brown@retailpos.com", "phone_number": "+1-555-210-2006"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1020"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1020", "new_status": "manager"}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 30}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 75}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "GROC-ALMBTR500", "new_price": 8.99}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_071_advanced_customer",
        instruction="Create a new customer 'Premium Customer Corp' with email premium@corp.com, phone +1-555-999-8888, and address '999 Premium Ave, Luxury City, LC 99999', retrieve customer details for the newly created customer (CUST-5013), change the membership level for CUST-5013 to 'platinum', update the loyalty points for CUST-5013 by adding 500 points, document a sale for CUST-5013 with 1 ELEC-4KTV55 using a credit card, list all transactions for CUST-5013, obtain transaction details for the most recent transaction (TXN-0013), and modify the phone number for CUST-5013 to '+1-555-999-7777'.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Premium Customer Corp", "email": "premium@corp.com", "phone_number": "+1-555-999-8888", "address": "999 Premium Ave, Luxury City, LC 99999"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 500}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-999-7777"})
        ],
        outputs=[]
    ),


    # Customer Relationship Building

    Task(
        annotator="lucas",
        user_id="lucas_task_072_customer_relationship",
        instruction="Create a new customer 'VIP Customer Services' with email vip@services.com, phone +1-555-888-7777, and address '888 VIP Boulevard, Elite City, EC 88888', retrieve customer details for the newly created customer (CUST-5013), change the membership level for CUST-5013 to 'platinum', update the loyalty points for CUST-5013 by adding 1000 points, modify the address for CUST-5013 to '888 VIP Boulevard Suite 100, Elite City, EC 88888', document a sale for CUST-5013 with 2 GROC-GRNLBR12 using a credit card, list all transactions for CUST-5013, obtain transaction details for the most recent transaction (TXN-0013), and change the phone number for CUST-5013 to '+1-555-888-6666'.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "VIP Customer Services", "email": "vip@services.com", "phone_number": "+1-555-888-7777", "address": "888 VIP Boulevard, Elite City, EC 88888"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 1000}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5013", "new_address": "888 VIP Boulevard Suite 100, Elite City, EC 88888"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "GROC-GRNLBR12", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-888-6666"})
        ],
        outputs=[]
    ),

    # Advanced Inventory Rebalancing

    Task(
        annotator="lucas",
        user_id="lucas_task_073_inventory_rebalancing",
        instruction="Identify low stock products with a threshold of 45, retrieve the inventory level for KITCH-CHEFKNF8, adjust the product stock for KITCH-CHEFKNF8 to 20, obtain product details for KITCH-CHEFKNF8, change the product price for KITCH-CHEFKNF8 to $299.99, retrieve the inventory level for GROC-GRNLBR12, adjust the product stock for GROC-GRNLBR12 to 90, document a sale for customer CUST-5001 with 1 KITCH-CHEFKNF8 using a credit card, obtain the customer loyalty points for CUST-5001, update the loyalty points for CUST-5001 by adding 150 points, and get total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 45}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 20}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 299.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 90}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 150}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Multi Department Staff Reorganization
    Task(
        annotator="lucas",
        user_id="lucas_task_074_staff_reorganization",
        instruction="Examine the current employee roster, retrieve employee details for EMP-1008, update the employment status for EMP-1008 to 'relocated', introduce new employee Lisa Chen as Regional Manager at STORE-003 with email lisa.chen@retailpos.com and phone +1-555-210-2010, retrieve employee details for EMP-1011, update the employment status for EMP-1011 to 'senior_manager', introduce new employee Carlos Rodriguez as Operations Director at STORE-004 with email carlos.rodriguez@retailpos.com and phone +1-555-210-2011, remove employee EMP-1003, and list all employees again.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "relocated"}),
            Action(name="AddEmployee", kwargs={"name": "Lisa Chen", "role": "Regional Manager", "store_id": "STORE-003", "email": "lisa.chen@retailpos.com", "phone_number": "+1-555-210-2010"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1011"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1011", "new_status": "senior_manager"}),
            Action(name="AddEmployee", kwargs={"name": "Carlos Rodriguez", "role": "Operations Director", "store_id": "STORE-004", "email": "carlos.rodriguez@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="ListAllEmployees", kwargs={})
        ],
        outputs=[]
    ),

    # Product Line Expansion

    Task(
        annotator="lucas",
        user_id="lucas_task_075_premium_onboarding",
        instruction="Create a new customer 'Enterprise Solutions Inc' with email enterprise@solutions.com, phone +1-555-777-6666, and address '777 Enterprise Drive, Business City, BC 77777', retrieve customer details for the newly created customer (CUST-5013), change the membership level for CUST-5013 to 'platinum', update the loyalty points for CUST-5013 by adding 2000 points, modify the email for CUST-5013 to 'premium.enterprise@solutions.com', document a sale for CUST-5013 with 1 ELEC-4KTV55 and 1 KITCH-CHEFKNF8 using a credit card, list all transactions for CUST-5013, obtain transaction details for the most recent transaction (TXN-0013), update the address for CUST-5013 to '777 Enterprise Drive Floor 50, Business City, BC 77777', and retrieve customer details for CUST-5013 once more.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Enterprise Solutions Inc", "email": "enterprise@solutions.com", "phone_number": "+1-555-777-6666", "address": "777 Enterprise Drive, Business City, BC 77777"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 2000}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5013", "new_email": "premium.enterprise@solutions.com"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5013", "new_address": "777 Enterprise Drive Floor 50, Business City, BC 77777"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[]
    ),


    # Multi Store Product Distribution

    Task(
        annotator="lucas",
        user_id="lucas_task_076_product_distribution",
        instruction="List products categorized under 'Sports & Outdoors', retrieve the inventory level for CLTH-SLFJEAN34, adjust the product stock for CLTH-SLFJEAN34 to 45, obtain product details for CLTH-SLFJEAN34, change the product price for CLTH-SLFJEAN34 to $94.99, introduce a new product 'Sports Water Bottle' in the Sports & Outdoors category with description 'Insulated stainless steel water bottle' and price $19.99 with a stock quantity of 50, list products categorized under 'Sports & Outdoors' again for verification, and get total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductStock", kwargs={"sku": "CLTH-SLFJEAN34", "new_stock_quantity": 45}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "CLTH-SLFJEAN34", "new_price": 94.99}),
            Action(name="AddNewProduct", kwargs={"name": "Sports Water Bottle", "description": "Insulated stainless steel water bottle", "category": "Sports & Outdoors", "price": 19.99, "stock_quantity": 50}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),


    # Strategic Inventory Reallocation

    Task(
        annotator="lucas",
        user_id="lucas_task_077_strategic_reallocation",
        instruction="Identify low stock products with a threshold of 75, retrieve the inventory level for KITCH-CHEFKNF8, adjust the product stock for KITCH-CHEFKNF8 to 50, obtain product details for KITCH-CHEFKNF8, change the product price for KITCH-CHEFKNF8 to $12.99, retrieve the inventory level for GROC-GRNLBR12, adjust the product stock for GROC-GRNLBR12 to 120, introduce a new product 'Premium Stapler' in the Office Supplies category with description 'Heavy-duty office stapler with 20-sheet capacity' and price $24.99 with a stock quantity of 50, document a sale for customer CUST-5003 with 1 KITCH-CHEFKNF8 using a credit card, and get total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 75}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 50}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 12.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 120}),
            Action(name="AddNewProduct", kwargs={"name": "Premium Stapler", "description": "Heavy-duty office stapler with 20-sheet capacity", "category": "Office Supplies", "price": 24.99, "stock_quantity": 50}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5003", "items": [{"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),


    # Workforce Development Initiative

    Task(
        annotator="lucas",
        user_id="lucas_task_078_workforce_development",
        instruction="List all employees, retrieve employee details for EMP-1004, update the employment status for EMP-1004 to 'development_program', introduce new employee Angela Thompson as Development Coordinator at STORE-004 with email angela.thompson@retailpos.com and phone +1-555-210-2011, retrieve employee details for EMP-1002, update the employment status for EMP-1002 to 'mentor', introduce new employee James Wilson as Training Specialist at STORE-005 with email james.wilson@retailpos.com and phone +1-555-210-2012, remove employee EMP-1034, and list all employees again.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "development_program"}),
            Action(name="AddEmployee", kwargs={"name": "Angela Thompson", "role": "Development Coordinator", "store_id": "STORE-004", "email": "angela.thompson@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "mentor"}),
            Action(name="AddEmployee", kwargs={"name": "James Wilson", "role": "Training Specialist", "store_id": "STORE-005", "email": "james.wilson@retailpos.com", "phone_number": "+1-555-210-2012"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1034"}),
            Action(name="ListAllEmployees", kwargs={})
        ],
        outputs=[]
    ),

    # Product Innovation Pipeline

    Task(
        annotator="lucas",
        user_id="lucas_task_079_supply_chain",
        instruction="Identify low stock products with a threshold of 80, retrieve the inventory level for HOM-COFMKR12, adjust the product stock for HOM-COFMKR12 to 110, obtain product details for HOM-COFMKR12, change the product price for HOM-COFMKR12 to $29.99, retrieve the inventory level for KITCH-CHEFKNF8, adjust the product stock for KITCH-CHEFKNF8 to 75, list products categorized under 'Home & Kitchen', document a sale for customer CUST-5009 with 2 HOM-COFMKR12 and 1 KITCH-CHEFKNF8 using a debit card, and update the loyalty points for CUST-5009 by adding 120 points.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 80}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 110}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 29.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 75}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "HOM-COFMKR12", "quantity": 2}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 120})
        ],
        outputs=[]
    ),

    # Market Expansion Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_080_market_expansion",
        instruction="List products categorized under 'Books', list products categorized under 'Office Supplies', obtain product details for GROC-ALMBTR500, change the product price for GROC-ALMBTR500 to $16.99, retrieve the inventory level for GROC-ALMBTR500, adjust the product stock for GROC-ALMBTR500 to 55, introduce a new product 'Business Strategy Guide' in the Books category with description 'Comprehensive guide to business strategy and planning' and price $24.99 with a stock quantity of 40, obtain product details for the newly added Business Strategy Guide, list products categorized under 'Books' again for verification, and retrieve customer details for CUST-5010.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Books"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Office Supplies"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "GROC-ALMBTR500", "new_price": 16.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-ALMBTR500", "new_stock_quantity": 55}),
            Action(name="AddNewProduct", kwargs={"name": "Business Strategy Guide", "description": "Comprehensive guide to business strategy and planning", "category": "Books", "price": 24.99, "stock_quantity": 40}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "BOOK-0002"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Books"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[]
    ),

    # Customer Experience Enhancement

    Task(
        annotator="lucas",
        user_id="lucas_task_081_customer_experience",
        instruction="Create a new customer 'Experience Enhancement Corp' with email experience@enhancement.com, phone +1-555-666-5555, and address '666 Experience Blvd, Enhancement City, EC 66666', retrieve customer details for the new customer, upgrade the customer membership level to 'gold', increase loyalty points by adding 750 points, change customer email to 'premium.experience@enhancement.com', document sale for the new customer with 1 HOM-COFMKR12 and 1 KITCH-CHEFKNF8 using credit card, compile transactions for the new customer, obtain transaction details for the latest transaction, change customer phone number to '+1-555-666-4444', and retrieve customer details for the new customer once more.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Experience Enhancement Corp", "email": "experience@enhancement.com", "phone_number": "+1-555-666-5555", "address": "666 Experience Blvd, Enhancement City, EC 66666"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 750}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5013", "new_email": "premium.experience@enhancement.com"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "HOM-COFMKR12", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-666-4444"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[]
    ),

    # Innovation and Growth Strategy

    Task(
        annotator="lucas",
        user_id="lucas_task_082_strategic_portfolio",
        instruction="Create a new customer 'Strategic Portfolio Solutions' with email strategic@portfolio.com, phone +1-555-555-4444, and address '555 Strategic Avenue, Portfolio City, PC 55544', retrieve customer details for the newly established customer (CUST-5013), elevate customer membership level for CUST-5013 to 'platinum', add 1500 loyalty points for CUST-5013, record a sale for customer CUST-5013 with 1 ELEC-4KTV55 and 1 KITCH-CHEFKNF8 using credit card, compile transactions for CUST-5013, get transaction details for the latest transaction (TXN-0013), update customer email for CUST-5013 to 'premium.strategic@portfolio.com', and retrieve customer details for CUST-5013 again.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Strategic Portfolio Solutions", "email": "strategic@portfolio.com", "phone_number": "+1-555-555-4444", "address": "555 Strategic Avenue, Portfolio City, PC 55544"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 1500}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5013", "new_email": "premium.strategic@portfolio.com"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[]
    ),

    # Employee Performance

    Task(
        annotator="lucas",
        user_id="lucas_task_083_multi_store_employees",
        instruction="Compile a list of all employees, retrieve employee details for EMP-1008, change employee status for EMP-1008 to 'promoted', introduce new employee Sarah Johnson as Supervisor at STORE-002 with email sarah.johnson@retailpos.com and phone +1-555-210-2004, obtain employee details for EMP-1009, update employee status for EMP-1009 to 'active', recruit new employee Mark Wilson as Sales Associate at STORE-003 with email mark.wilson@retailpos.com and phone +1-555-210-2005, terminate employee EMP-1011, list all employees once more, and retrieve employee details for EMP-1015.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "promoted"}),
            Action(name="AddEmployee", kwargs={"name": "Sarah Johnson", "role": "Supervisor", "store_id": "STORE-002", "email": "sarah.johnson@retailpos.com", "phone_number": "+1-555-210-2004"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1009"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1009", "new_status": "active"}),
            Action(name="AddEmployee", kwargs={"name": "Mark Wilson", "role": "Sales Associate", "store_id": "STORE-003", "email": "mark.wilson@retailpos.com", "phone_number": "+1-555-210-2005"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1011"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"})
        ],
        outputs=[]
    ),

    # Store Operations Management

    Task(
        annotator="lucas",
        user_id="lucas_task_084_store_operations",
        instruction="Examine current employee roster, introduce new employee Sarah Wilson as Assistant Manager at STORE-003 with email sarah.wilson@retailpos.com and phone +1-555-210-2007, retrieve employee details for EMP-1015, adjust employee status for EMP-1015 to 'assistant_manager', list low stock products with a threshold of 25, acquire inventory level for HOM-COFMKR12, change product stock for HOM-COFMKR12 to 60, obtain product details for HOM-COFMKR12, modify product price for HOM-COFMKR12 to $89.99, and assess total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="AddEmployee", kwargs={"name": "Sarah Wilson", "role": "Assistant Manager", "store_id": "STORE-003", "email": "sarah.wilson@retailpos.com", "phone_number": "+1-555-210-2007"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1015"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1015", "new_status": "assistant_manager"}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 25}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Customer Management

    Task(
        annotator="lucas",
        user_id="lucas_task_085_advanced_customer",
        instruction="Create a new customer 'Premium Customer Corp' with email premium@corp.com, phone +1-555-999-8888, and address '999 Premium Ave, Luxury City, LC 99999', retrieve customer details for the newly established customer (CUST-5013), elevate customer membership level for CUST-5013 to 'platinum', increase loyalty points for CUST-5013 by adding 500 points, document sale for CUST-5013 with 1 ELEC-4KTV55 using credit card, compile transactions for CUST-5013, obtain transaction details for the latest transaction (TXN-0013), and update customer phone number for CUST-5013 to '+1-555-999-7777'.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Premium Customer Corp", "email": "premium@corp.com", "phone_number": "+1-555-999-8888", "address": "999 Premium Ave, Luxury City, LC 99999"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 500}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5013", "new_phone_number": "+1-555-999-7777"})
        ],
        outputs=[]
    ),

    # Advanced Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_086_advanced_customer_relationship",
        instruction="Coordinate advanced customer relationship management for CUST-5012: retrieve details, update email to relationship.customer@email.com, change phone to +1-555-444-5555, revise address to 500 Relationship Blvd, City, ST 54321, check loyalty status, update membership to diamond, and list their transactions. Then, acquire details for TXN-0013, document sale (ELEC-4KTV55), document sale (GROC-GRNLBR12), increase loyalty by adding 400 points, elevate membership to elite, compile a list of all products, obtain product details for HOM-COFMKR12, adjust product price for HOM-COFMKR12 to $129.99, gather inventory, change stock for HOM-COFMKR12 to 80, assess total sales for the date 2025-06-12, and confirm all updates.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5012", "new_email": "relationship.customer@email.com"}),
            Action(name="UpdateCustomerPhoneNumber", kwargs={"customer_id": "CUST-5012", "new_phone_number": "+1-555-444-5555"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5012", "new_address": "500 Relationship Blvd, City, ST 54321"}),
            Action(name="GetCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "platinum"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5012"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5012", "items": [{"sku": "GROC-GRNLBR12", "quantity": 2}], "payment_method": "debit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5012", "points_to_add": 400}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5012", "new_membership_level": "vip"}),
            Action(name="ListAllProducts", kwargs={"limit": 50}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 129.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 80}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-12"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5012"})
        ],
        outputs=[]
    ),

    # Advanced Inventory Rebalancing

    Task(
        annotator="lucas",
        user_id="lucas_task_087_advanced_inventory_rebalancing",
        instruction="Conduct advanced inventory rebalancing: list low stock products with a threshold of 20, acquire inventory for ELEC-4KTV55, AUDIO-BTSPKR02, HOM-COFMKR12, KITCH-CHEFKNF8, update stock levels to 40, 35, 50, 30 respectively, retrieve product details for all, adjust prices to 699.99, 179.99, 99.99, 249.99 respectively, introduce new product 'Inventory Rebalancer Pro' with description 'Automated inventory rebalancing system' priced at 499.99 and stock quantity of 20, obtain total sales for dates 2025-06-13 and 2025-06-14, and confirm all updates.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 20}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 50}),
            Action(name="UpdateProductStock", kwargs={"sku": "KITCH-CHEFKNF8", "new_stock_quantity": 30}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 699.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 179.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 99.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "KITCH-CHEFKNF8", "new_price": 249.99}),
            Action(name="AddNewProduct", kwargs={"name": "Inventory Rebalancer Pro", "description": "Automated inventory rebalancing system", "category": "Electronics", "price": 499.99, "stock_quantity": 20}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-13"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-14"}),
        ],
        outputs=[]
    ),

    # Multi Department Staff Reorganization
    Task(
        annotator="lucas",
        user_id="lucas_task_088_staff_reorganization",
        instruction="Compile a list of all employees, retrieve employee details for EMP-1003, change employee status for EMP-1003 to 'transferred', recruit new employee Robert Johnson as Department Head at STORE-001 with email robert.johnson@retailpos.com and phone +1-555-210-2008, obtain employee details for EMP-1004, change employee status for EMP-1004 to 'promoted', introduce new employee Maria Garcia as Assistant Manager at STORE-002 with email maria.garcia@retailpos.com and phone +1-555-210-2009, terminate employee EMP-1020, and list all employees again.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1003"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1003", "new_status": "transferred"}),
            Action(name="AddEmployee", kwargs={"name": "Robert Johnson", "role": "Department Head", "store_id": "STORE-001", "email": "robert.johnson@retailpos.com", "phone_number": "+1-555-210-2008"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "promoted"}),
            Action(name="AddEmployee", kwargs={"name": "Maria Garcia", "role": "Assistant Manager", "store_id": "STORE-002", "email": "maria.garcia@retailpos.com", "phone_number": "+1-555-210-2009"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1020"}),
            Action(name="ListAllEmployees", kwargs={})
        ],
        outputs=[]
    ),

    # Product Line Expansion

    Task(
        annotator="lucas",
        user_id="lucas_task_089_seasonal_inventory",
        instruction="List low stock products with a threshold of 40, obtain inventory level for GROC-GRNLBR12, adjust product stock for GROC-GRNLBR12 to 85, retrieve product details for GROC-GRNLBR12, change product price for GROC-GRNLBR12 to $3.99, acquire inventory level for HOM-COFMKR12, update product stock for HOM-COFMKR12 to 65, document sale for customer CUST-5002 with 3 GROC-GRNLBR12 using cash, increase customer loyalty points for CUST-5002 by adding 30 points, and assess total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 40}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 85}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "GROC-GRNLBR12", "new_price": 3.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 65}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "GROC-GRNLBR12", "quantity": 3}], "payment_method": "cash"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 30}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Workforce Development Initiative

    Task(
        annotator="lucas",
        user_id="lucas_task_091_workforce_development",
        instruction="Compile a list of all employees, retrieve employee details for EMP-1002, change employee status for EMP-1002 to 'training', bring on new employee Jennifer Wilson as Training Coordinator at STORE-001 with email jennifer.wilson@retailpos.com and phone +1-555-210-2011, obtain employee details for EMP-1008, adjust employee status for EMP-1008 to 'mentor', hire new employee Michael Brown as Development Specialist at STORE-002 with email michael.brown@retailpos.com and phone +1-555-210-2012, terminate employee EMP-1015, and list all employees again.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "training"}),
            Action(name="AddEmployee", kwargs={"name": "Jennifer Wilson", "role": "Training Coordinator", "store_id": "STORE-001", "email": "jennifer.wilson@retailpos.com", "phone_number": "+1-555-210-2011"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "mentor"}),
            Action(name="AddEmployee", kwargs={"name": "Michael Brown", "role": "Development Specialist", "store_id": "STORE-002", "email": "michael.brown@retailpos.com", "phone_number": "+1-555-210-2012"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1015"}),
            Action(name="ListAllEmployees", kwargs={})
        ],
        outputs=[]
    ),

    # Product Innovation Pipeline

    Task(
        annotator="lucas",
        user_id="lucas_task_092_supply_chain",
        instruction="Identify low stock products with a threshold of 50, retrieve inventory level for AUDIO-BTSPKR02, verify if AUDIO-BTSPKR02 stock falls below 40 and adjust to 35 if necessary, obtain product details for AUDIO-BTSPKR02, modify product price for AUDIO-BTSPKR02 to $159.99, retrieve inventory level for HOM-COFMKR12, check if HOM-COFMKR12 stock is below 80 and set it to 70 if needed, introduce a new product 'Supply Chain Monitor' in the Electronics category with the description 'Real-time supply chain monitoring device' priced at $199.99 with a stock quantity of 25, obtain product details for the newly introduced Supply Chain Monitor (ELEC-0006), register a sale for customer CUST-5007 with 1 AUDIO-BTSPKR02 using a debit card, and retrieve total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 50}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 159.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 70}),
            Action(name="AddNewProduct", kwargs={"name": "Supply Chain Monitor", "description": "Real-time supply chain monitoring device", "category": "Electronics", "price": 199.99, "stock_quantity": 25}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-0006"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "debit_card"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Innovation and Growth Strategy
    Task(
        annotator="lucas",
        user_id="lucas_task_093_strategic_portfolio",
        instruction="Register new customer 'Strategic Partners LLC' with email strategic@partners.com, phone +1-555-666-5555, and address '666 Strategic Way, Portfolio City, PC 66666', obtain customer details for the newly registered customer (CUST-5013), enhance customer membership level for CUST-5013 to 'platinum', increase loyalty points for CUST-5013 by adding 1500 points, update customer email for CUST-5013 to 'premium.strategic@partners.com', register a sale for CUST-5013 with 1 ELEC-4KTV55 and 1 AUDIO-BTSPKR02 using a credit card, list transactions for CUST-5013, retrieve transaction details for the most recent transaction (TXN-0013), update customer address for CUST-5013 to '666 Strategic Way Suite 200, Portfolio City, PC 66666', and obtain customer details for CUST-5013 once more.",
        actions=[
            Action(name="AddNewCustomer", kwargs={"name": "Strategic Partners LLC", "email": "strategic@partners.com", "phone_number": "+1-555-666-5555", "address": "666 Strategic Way, Portfolio City, PC 66666"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5013", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5013", "points_to_add": 1500}),
            Action(name="UpdateCustomerEmail", kwargs={"customer_id": "CUST-5013", "new_email": "premium.strategic@partners.com"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5013", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "AUDIO-BTSPKR02", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5013"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0013"}),
            Action(name="UpdateCustomerAddress", kwargs={"customer_id": "CUST-5013", "new_address": "666 Strategic Way Suite 200, Portfolio City, PC 66666"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5013"})
        ],
        outputs=[]
    ),

    # Inventory Optimization

    Task(
        annotator="lucas",
        user_id="lucas_task_094_inventory_optimization",
        instruction="Identify low stock products with a threshold of 30, retrieve inventory level for ELEC-4KTV55, obtain inventory level for AUDIO-BTSPKR02, retrieve inventory level for HOM-COFMKR12, modify product stock for ELEC-4KTV55 to 25, adjust product stock for AUDIO-BTSPKR02 to 40, update product stock for HOM-COFMKR12 to 35, fetch product details for ELEC-4KTV55, obtain product details for AUDIO-BTSPKR02, retrieve product details for HOM-COFMKR12, modify product price for ELEC-4KTV55 to $599.99, adjust product price for AUDIO-BTSPKR02 to $159.99, update product price for HOM-COFMKR12 to $89.99, introduce a new product 'Inventory Optimization Suite' in the Electronics category with the description 'Advanced inventory management and optimization platform' priced at $399.99 with a stock quantity of 20, and retrieve total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListLowStockProducts", kwargs={"threshold": 30}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 25}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 35}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 599.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 159.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 89.99}),
            Action(name="AddNewProduct", kwargs={"name": "Inventory Optimization Suite", "description": "Advanced inventory management and optimization platform", "category": "Electronics", "price": 399.99, "stock_quantity": 20}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Employee Performance Management

    Task(
        annotator="lucas",
        user_id="lucas_task_095_product_portfolio",
        instruction="Categorize products by 'Electronics' to evaluate the current portfolio, then categorize products by 'Home & Kitchen' to enhance portfolio analysis, and categorize products by 'Sports & Outdoors' for a thorough portfolio review. Obtain product details for ELEC-4KTV55 to analyze high-value electronics and adjust product price for ELEC-4KTV55 to $649.99 for premium positioning. Retrieve product details for HOM-COFMKR12 to assess home appliances and modify product price for HOM-COFMKR12 to $94.99 for competitive pricing. Get product details for AUDIO-BTSPKR02 to evaluate audio equipment and update product price for AUDIO-BTSPKR02 to $169.99 for market alignment. Retrieve inventory level for ELEC-4KTV55 for stock status assessment and adjust product stock for ELEC-4KTV55 to 30 for optimal levels. Obtain inventory level for HOM-COFMKR12 to confirm availability and change product stock for HOM-COFMKR12 to 45 for fulfilling demand. Get inventory level for AUDIO-BTSPKR02 to evaluate supply and change product stock for AUDIO-BTSPKR02 to 35 for balanced inventory. Introduce a new product 'Portfolio Analytics Platform' in the Electronics category with description 'Comprehensive product portfolio analysis and management system' priced at $299.99 and stock quantity of 15, and retrieve total sales for the date 2025-06-05 to assess the performance impact on the portfolio.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 649.99}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 94.99}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 169.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 30}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 45}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="AddNewProduct", kwargs={"name": "Portfolio Analytics Platform", "description": "Comprehensive product portfolio analysis and management system", "category": "Electronics", "price": 299.99, "stock_quantity": 15}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Customer Relationship Management

    Task(
        annotator="lucas",
        user_id="lucas_task_096_employee_performance",
        instruction="Enumerate all employees, obtain employee details for EMP-1002, get employee details for EMP-1004, fetch employee details for EMP-1008, adjust employee status for EMP-1002 to 'training', update employee status for EMP-1004 to 'active', modify employee status for EMP-1008 to 'mentor', register a new employee 'Performance Manager' as Performance Specialist at STORE-001 with email performance.manager@retailpos.com and phone +1-555-210-5002, onboard a new employee 'Analytics Coordinator' as Analytics Specialist at STORE-002 with email analytics.coordinator@retailpos.com and phone +1-555-210-5003, remove employee EMP-1003, list all employees again, and fetch employee details for EMP-1002 to confirm final status.",
        actions=[
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1004"}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1008"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1002", "new_status": "training"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1004", "new_status": "active"}),
            Action(name="UpdateEmployeeStatus", kwargs={"employee_id": "EMP-1008", "new_status": "mentor"}),
            Action(name="AddEmployee", kwargs={"name": "Performance Manager", "role": "Performance Specialist", "store_id": "STORE-001", "email": "performance.manager@retailpos.com", "phone_number": "+1-555-210-5002"}),
            Action(name="AddEmployee", kwargs={"name": "Analytics Coordinator", "role": "Analytics Specialist", "store_id": "STORE-002", "email": "analytics.coordinator@retailpos.com", "phone_number": "+1-555-210-5003"}),
            Action(name="RemoveEmployee", kwargs={"employee_id": "EMP-1003"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetEmployeeDetails", kwargs={"employee_id": "EMP-1002"})
        ],
        outputs=[]
    ),

    # Strategic Product Portfolio Management

    Task(
        annotator="lucas",
        user_id="lucas_task_097_customer_relationship",
        instruction="Obtain customer details for CUST-5005, retrieve customer details for CUST-5006, fetch customer details for CUST-5007, list transactions for CUST-5005, list transactions for CUST-5006, adjust customer membership level for CUST-5005 to 'gold', update customer membership level for CUST-5006 to 'silver', adjust customer membership level for CUST-5007 to 'bronze', register a sale for customer CUST-5005 with 1 ELEC-4KTV55 using a credit card, register a sale for customer CUST-5006 with 2 AUDIO-BTSPKR02 using a credit card, update customer loyalty points for CUST-5005 by adding 400 points, update customer loyalty points for CUST-5006 by adding 200 points, and obtain customer details for CUST-5005 once again.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5005"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5005"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5006"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5005", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5006", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5007", "new_membership_level": "bronze"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5005", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 400}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5005"})
        ],
        outputs=[]
    ),

    # Strategic Product Development Innovation

    Task(
        annotator="lucas",
        user_id="lucas_task_098_product_development",
        instruction="Categorize products by 'Electronics', categorize products by 'Home & Kitchen', retrieve product details for ELEC-4KTV55, fetch product details for HOM-COFMKR12, obtain product details for AUDIO-BTSPKR02, adjust product price for ELEC-4KTV55 to $699.99, modify product price for HOM-COFMKR12 to $99.99, update product price for AUDIO-BTSPKR02 to $179.99, retrieve inventory level for ELEC-4KTV55, get inventory level for HOM-COFMKR12, obtain inventory level for AUDIO-BTSPKR02, change product stock for ELEC-4KTV55 to 35, adjust product stock for HOM-COFMKR12 to 50, modify product stock for AUDIO-BTSPKR02 to 40, introduce a new product 'Innovation Hub Platform' in the Electronics category with description 'Advanced product development and innovation management system' priced at $499.99 with a stock quantity of 25, and retrieve total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 699.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 99.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 179.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 35}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 50}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 40}),
            Action(name="AddNewProduct", kwargs={"name": "Innovation Hub Platform", "description": "Advanced product development and innovation management system", "category": "Electronics", "price": 499.99, "stock_quantity": 25}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Strategic Market Analysis Intelligence

    Task(
        annotator="lucas",
        user_id="lucas_task_099_market_intelligence",
        instruction="Enumerate products by category 'Electronics', list products by category 'Sports & Outdoors', categorize products by category 'Books', retrieve product details for ELEC-4KTV55, obtain product details for AUDIO-BTSPKR02, fetch product details for HOM-COFMKR12, modify product price for ELEC-4KTV55 to $749.99, adjust product price for AUDIO-BTSPKR02 to $189.99, update product price for HOM-COFMKR12 to $109.99, retrieve inventory level for ELEC-4KTV55, obtain inventory level for AUDIO-BTSPKR02, fetch inventory level for HOM-COFMKR12, change product stock for ELEC-4KTV55 to 40, adjust product stock for AUDIO-BTSPKR02 to 45, modify product stock for HOM-COFMKR12 to 55, introduce a new product 'Market Intelligence Suite' in the Electronics category with description 'Comprehensive market analysis and competitive intelligence platform' priced at $399.99 with a stock quantity of 20, and retrieve total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Books"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 749.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 189.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 109.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 45}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 55}),
            Action(name="AddNewProduct", kwargs={"name": "Market Intelligence Suite", "description": "Comprehensive market analysis and competitive intelligence platform", "category": "Electronics", "price": 399.99, "stock_quantity": 20}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Customer Success Retention

    Task(
        annotator="lucas",
        user_id="lucas_task_100_customer_success",
        instruction="Obtain customer details for CUST-5008, retrieve customer details for CUST-5009, get customer details for CUST-5010, list transactions for CUST-5008, list transactions for CUST-5009, adjust customer membership level for CUST-5008 to 'platinum', update customer membership level for CUST-5009 to 'gold', modify customer membership level for CUST-5010 to 'silver', register a sale for customer CUST-5008 with 1 ELEC-4KTV55 using a credit card, record sale for customer CUST-5009 with 2 AUDIO-BTSPKR02 using a credit card, increase customer loyalty points for CUST-5008 by adding 800 points, update customer loyalty points for CUST-5009 by adding 500 points, and get customer details for CUST-5008 once more.",
        actions=[
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5009"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5010"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5008"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5009"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5008", "new_membership_level": "platinum"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5009", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5010", "new_membership_level": "silver"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5008", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5009", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5008", "points_to_add": 800}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 500}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"})
        ],
        outputs=[]
    ),

    # Strategic Business Intelligence Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_101_business_intelligence",
        instruction="Retrieve total sales for the date 2025-06-05, obtain total sales for the date 2025-06-06, identify low stock products with a threshold of 25, get inventory level for ELEC-4KTV55, retrieve inventory level for HOM-COFMKR12, obtain inventory level for AUDIO-BTSPKR02, update product stock for ELEC-4KTV55 to 30, adjust product stock for HOM-COFMKR12 to 40, modify product stock for AUDIO-BTSPKR02 to 35, get customer details for CUST-5001, retrieve customer details for CUST-5002, register a sale for customer CUST-5001 with 1 ELEC-4KTV55 using a credit card, record sale for customer CUST-5002 with 2 AUDIO-BTSPKR02 using a credit card, update customer loyalty points for CUST-5001 by adding 700 points, and retrieve total sales for the date 2025-06-05 once again.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"}),
            Action(name="ListLowStockProducts", kwargs={"threshold": 25}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 30}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 40}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 35}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5002"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5001", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5002", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 700}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Strategic Digital Transformation

    Task(
        annotator="lucas",
        user_id="lucas_task_103_digital_transformation",
        instruction="Categorize products into 'Electronics', 'Home & Kitchen', and 'Sports & Outdoors', retrieve product information for ELEC-4KTV55, retrieve product information for HOM-COFMKR12, retrieve product information for AUDIO-BTSPKR02, modify price for ELEC-4KTV55 to $849.99, modify price for HOM-COFMKR12 to $129.99, modify price for AUDIO-BTSPKR02 to $229.99, check inventory quantity for ELEC-4KTV55, check inventory quantity for HOM-COFMKR12, check inventory quantity for AUDIO-BTSPKR02, adjust product stock for ELEC-4KTV55 to 50, adjust product stock for HOM-COFMKR12 to 60, adjust product stock for AUDIO-BTSPKR02 to 55, introduce a new product 'Digital Transformation Suite' in the Electronics category with the description 'Complete digital transformation and modernization platform' priced at $799.99 and stock quantity of 35, and retrieve total sales for the date 2025-06-05.",
        actions=[
            Action(name="ListProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="ListProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductPrice", kwargs={"sku": "ELEC-4KTV55", "new_price": 849.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "HOM-COFMKR12", "new_price": 129.99}),
            Action(name="UpdateProductPrice", kwargs={"sku": "AUDIO-BTSPKR02", "new_price": 229.99}),
            Action(name="GetInventoryLevel", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateProductStock", kwargs={"sku": "ELEC-4KTV55", "new_stock_quantity": 50}),
            Action(name="UpdateProductStock", kwargs={"sku": "HOM-COFMKR12", "new_stock_quantity": 60}),
            Action(name="UpdateProductStock", kwargs={"sku": "AUDIO-BTSPKR02", "new_stock_quantity": 55}),
            Action(name="AddNewProduct", kwargs={"name": "Digital Transformation Suite", "description": "Complete digital transformation and modernization platform", "category": "Electronics", "price": 799.99, "stock_quantity": 35}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Advanced Operational Excellence

    Task(
        annotator="lucas",
        user_id="lucas_task_104_operational_excellence",
        instruction="Retrieve total sales for the date 2025-06-05, compile a list of all employees, obtain customer information for CUST-5006, obtain customer information for CUST-5007, obtain customer information for CUST-5008, elevate customer membership tier for CUST-5006 to 'gold', elevate customer membership tier for CUST-5007 to 'silver', elevate customer membership tier for CUST-5008 to 'bronze', register sale for customer CUST-5006 with 1 ELEC-4KTV55 via credit card, register sale for customer CUST-5007 with 2 AUDIO-BTSPKR02 via credit card, augment customer loyalty points for CUST-5006 by 750 points, augment customer loyalty points for CUST-5007 by 450 points, and retrieve total sales for the date 2025-06-05 once more.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="ListAllEmployees", kwargs={}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5006"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5007"}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5008"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5006", "new_membership_level": "gold"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5007", "new_membership_level": "silver"}),
            Action(name="UpdateCustomerMembershipLevel", kwargs={"customer_id": "CUST-5008", "new_membership_level": "bronze"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5006", "items": [{"sku": "ELEC-4KTV55", "quantity": 1}], "payment_method": "credit_card"}),
            Action(name="RecordSale", kwargs={"customer_id": "CUST-5007", "items": [{"sku": "AUDIO-BTSPKR02", "quantity": 2}], "payment_method": "credit_card"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 750}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5007", "points_to_add": 450}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"})
        ],
        outputs=[]
    ),

    # Sales Analytics

    Task(
        annotator="lucas",
        user_id="lucas_task_107_sales_analytics",
        instruction="Retrieve total sales for the date 2025-06-05 for daily performance evaluation. Retrieve total sales for the date 2025-06-06 to compare with the preceding day's performance. Augment customer loyalty points for CUST-5003 by adding 200 points as a performance incentive. Obtain customer details for CUST-5003 to confirm their status. Compile transactions for CUST-5003 to review their purchase history. Retrieve transaction details for TXN-0002 to ascertain its status. Update status for TXN-0002 to 'completed' to close the sale. Check inventory quantity for GROC-GRNLBR12 to evaluate stock status. Adjust product stock for GROC-GRNLBR12 to 85 to maintain adequate supply. Retrieve total sales for the date 2025-06-07 for business performance assessment.",
        actions=[
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-05"}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-06"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5003", "points_to_add": 200}),
            Action(name="GetCustomerDetails", kwargs={"customer_id": "CUST-5003"}),
            Action(name="ListTransactionsByCustomer", kwargs={"customer_id": "CUST-5003"}),
            Action(name="GetTransactionDetails", kwargs={"transaction_id": "TXN-0002"}),
            Action(name="UpdateTransactionStatus", kwargs={"transaction_id": "TXN-0002", "new_status": "completed"}),
            Action(name="GetInventoryLevel", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="UpdateProductStock", kwargs={"sku": "GROC-GRNLBR12", "new_stock_quantity": 85}),
            Action(name="GetTotalSalesByDate", kwargs={"date": "2025-06-07"})
        ],
        outputs=[]
    ),

]
