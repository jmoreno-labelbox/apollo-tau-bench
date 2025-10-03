from tau_bench.types import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction="Handle marketing management activities. Activate the 'Summer Electronics Sale' (PROMO-001) scheduled to commence on '2025-06-01'. Next, obtain all active promotions to verify the inclusion of 'UltraVision 55\" 4K Smart TV' (SKU: ELEC-4KTV55), and check its current inventory at 'STORE-001'. Lastly, modify the 'times_used' count for PROMO-001 to 10 to initiate usage tracking.",
        actions=[
            Action(
                name="ActivatePromotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "active"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-001", "times_used": 10},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-001", "status": "active", "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "ELEC-RCHAA04"]},
            {"sku": "ELEC-4KTV55", "quantity": 8},
            {"promotion_id": "PROMO-001", "times_used": 10},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_002",
        instruction="Coordinate marketing management actions. Deactivate the 'Clearance Apparel Markdown' promotion (PROMO-005) as its upcoming end date '2025-06-30' nears, and the remaining stock for linked items, 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) at 'STORE-002' and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) at 'STORE-002', is low. After deactivation, confirm its status by listing all inactive promotions and gather the current stock levels for the apparel pieces at 'STORE-002'. Finally, change the 'status' of 'Men's Slim Fit Jeans - 34W 32L' to 'clearance' in the product database to indicate its end-of-life cycle. The current date is '2025-06-28'.",
        actions=[
            Action(
                name="DeactivatePromotion",
                kwargs={"promotion_id": "PROMO-005"},
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "inactive"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "CLTH-SLFJEAN34", "status": "clearance"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-005", "status": "inactive"},
            {"sku": "CLTH-SLFJEAN34", "status": "in_stock", "quantity": 30},
            {"sku": "CLTH-WINJKT01", "status": "low_stock", "quantity": 6},
            {"sku": "CLTH-SLFJEAN34", "status": "clearance"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_003",
        instruction="Oversee marketing management duties. Due to rising demand, extend the 'Summer Electronics Sale' (PROMO-001) until '2025-09-30'. Subsequently, confirm the new end date by accessing the promotion details. Follow up by retrieving all products linked with this promotion to validate their SKUs.",
        actions=[
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-001", "end_date": "2025-09-30"},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-GAMLP15"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-RCHAA04"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-001", "end_date": "2025-09-30"},
            {"sku": "ELEC-4KTV55"},
            {"sku": "AUDIO-BTSPKR02"},
            {"sku": "ELEC-GAMLP15"},
            {"sku": "ELEC-RCHAA04"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_004",
        instruction="Manage marketing management responsibilities. Replace the 'Tax-Free Books Weekend' (PROMO-004) with a new 'Summer Reading Discount' offering 15% off 'Adventures in Sillytown' (BOOK-KDSSTY01) from '2025-08-10' to '2025-08-20'. Begin by deactivating the old promotion (PROMO-004). Then, convert PROMO-004 into the 'Summer Reading Discount', ensuring the `name`, `type`, `discount_value`, `description` ('15% off select children''s books for summer reading.'), `applicable_skus` (['BOOK-KDSSTY01']), `start_date`, `end_date`, and `status` are correctly set. Retrieve product details for 'Adventures in Sillytown' to verify its `is_discountable` status. If necessary, update its `is_discountable` status to `True`. Finally, confirm all changes by reviewing the new 'Summer Reading Discount' promotion details. The current date is '2025-08-05'.",
        actions=[
            Action(
                name="DeactivatePromotion",
                kwargs={"promotion_id": "PROMO-004"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={
                    "promotion_id": "PROMO-004",
                    "name": "Summer Reading Discount",
                    "type": "percentage",
                    "discount_value": 15.0,
                    "description": "15% off select children's books for summer reading.",
                    "applicable_skus": ["BOOK-KDSSTY01"],
                    "start_date": "2025-08-10",
                    "end_date": "2025-08-20",
                    "status": "scheduled"
                },
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "BOOK-KDSSTY01"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "BOOK-KDSSTY01", "is_discountable": True},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-004"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-004", "status": "inactive"},
            {"promotion_id": "PROMO-004", "name": "Summer Reading Discount", "type": "percentage", "discount_value": 15.0, "status": "scheduled"},
            {"sku": "BOOK-KDSSTY01", "is_discountable": True},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_005",
        instruction="Administer marketing management tasks. Recently, 'Smart Home Starter Discount' (PROMO-006) was adjusted to include 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02). Confirm the inclusion of 'WaveSound All-Weather Bluetooth Speaker' among its applicable SKUs. Also, verify the current promotion status and end date. If its 'usage_limit' is not specified, update it to 100. Extend the promotion's 'end_date' to '2025-09-15'. The current date is '2025-07-01'.",
        actions=[
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-01"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-006", "usage_limit": 100, "end_date": "2025-09-15", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-006"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-006", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"], "status": "active", "end_date": "2025-09-15", "usage_limit": 100},
            {"sku": "AUDIO-BTSPKR02", "name": "WaveSound All-Weather Bluetooth Speaker"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_006",
        instruction="Coordinate sales responsibilities alongside associate named 'Jack Robinson'. A customer intends to buy two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) at 'STORE-001'. Initially, check the stock availability at 'STORE-001'. The 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003) is set to commence today, '2025-06-10', so ensure it is activated. Upon activation, obtain the comprehensive product specifications of the yoga mat to validate its attributes. If the promotion is active, determine the total expenditure with the BOGO discount applied. Log the transaction as 'completed' through 'credit_card' for 'Liam Anderson' (CUST-5004). On '2025-06-10', modify the inventory to reflect the quantity sold. Finally, increase the 'times_used' for this promotion by 1 and provide the total payment amount, the discount granted, and the transaction ID.",
        actions=[
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"},
            ),
            Action(
                name="ActivatePromotion",
                kwargs={"promotion_id": "PROMO-003"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "SPORT-YOGMAT01"},
            ),
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Liam Anderson"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Jack Robinson"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0021",
                    "quantity_sold": 2,
                    "last_stock_count_date": "2025-06-10",
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1034",
                    "total_amount": 48.70,
                    "tax_amount": 3.71,
                    "payment_method": "credit_card",
                    "discount_total": 14.995,
                    "customer_id": "CUST-5004",
                    "line_items": [
                        {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                        {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 14.995},
                    ],
                    "status": "completed",
                },
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-003", "times_used": 1},
            ),
        ],
        outputs=["Total amount: 48.70", "Discount applied: 14.995", "Transaction ID: TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction="Oversee marketing management functions. Relaunch a flash sale for Home & Kitchen merchandise. Initially, identify all products presently within the 'Home & Kitchen' category by acquiring specifics for designated SKUs (HOM-COFMKR12, KITCH-CHEFKNF8, HOME-BTHTWL01, HOME-DESKLMP01, KITCH-FRYPAN10) to verify their accurate categorization. Thereafter, modify the 'Weekend Flash Sale - Home & Kitchen' (PROMO-007) by setting its status to 'active' solely for '2025-07-28' and '2025-07-29', set its 'usage_limit' to 50, and revise its description to 'Weekend Special: 18% off Home & Kitchen!'. Lastly, access all active promotions to confirm the flash sale is recorded with updated specifications. Today's date is '2025-07-27'.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOM-COFMKR12"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "KITCH-CHEFKNF8"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOME-DESKLMP01"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "KITCH-FRYPAN10"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={
                    "promotion_id": "PROMO-007",
                    "status": "active",
                    "start_date": "2025-07-28",
                    "end_date": "2025-07-29",
                    "usage_limit": 50,
                    "description": "Weekend Special: 18% off Home & Kitchen!",
                },
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "active"},
            ),
        ],
        outputs=[
            {"sku": "HOM-COFMKR12", "category": "Home & Kitchen"},
            {"sku": "KITCH-CHEFKNF8", "category": "Home & Kitchen"},
            {"sku": "HOME-BTHTWL01", "category": "Home & Kitchen"},
            {"sku": "HOME-DESKLMP01", "category": "Home & Kitchen"},
            {"sku": "KITCH-FRYPAN10", "category": "Home & Kitchen"},
            {"promotion_id": "PROMO-007", "status": "active", "start_date": "2025-07-28", "end_date": "2025-07-29", "usage_limit": 50, "description": "Weekend Special: 18% off Home & Kitchen!"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_008",
        instruction="Manage sales functions with the help of associate 'Sarah Anderson'. A client named 'Noah Tran' seeks to acquire the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) at 'STORE-001'. Verify stock availability by acquiring its inventory information. As of '2025-08-01', ascertain whether the 'Grand Summer Electronics Sale' promotion is operational and if the TV qualifies by inspecting product and promotion specifics. Should the promotion be viable and the product eligible, evaluate the total cost incorporating the discount. If otherwise, employ only the standard pricing. Proceed to execute a transaction for 'Noah Tran' via 'credit_card', updating the inventory's last stock count date to '2025-08-01'. Following the transaction, increase 'Noah Tran's loyalty points by 150. Present the final total, the applied discount, and the transaction ID.",
        actions=[
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Grand Summer Electronics Sale", "query_date": "2025-08-01"},
            ),
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Noah Tran"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Sarah Anderson"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0001",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-08-01",
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1002",
                    "total_amount": 757.74,
                    "tax_amount": 57.75,
                    "payment_method": "credit_card",
                    "discount_total": 0.00,
                    "customer_id": "CUST-5002",
                    "line_items": [
                        {"sku": "ELEC-4KTV55", "quantity": 1, "unit_price": 699.99, "discount": 0.0},
                    ],
                    "status": "completed",
                },
            ),
            Action(
                name="UpdateCustomerLoyaltyPoints",
                kwargs={"customer_id": "CUST-5002", "points_to_add": 150},
            ),
        ],
        outputs=[
            {"total_amount": 757.74},
            {"discount_applied": 0.00},
            {"transaction_id": "TXN-0013"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_009",
        instruction="Conduct marketing management operations. Adjust the 'Smart Home Starter Discount' (PROMO-006) to apply exclusively to 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02) henceforth. Update its description to 'Exclusive discount on smart thermostats.' and exclude 'WaveSound All-Weather Bluetooth Bluetooth Speaker' (AUDIO-BTSPKR02) from its relevant SKUs. Subsequent to this, retrieve the details of the 'WaveSound All-Weather Bluetooth Speaker' and shift its `status` to `limited_availability` to indicate its removal from broad promotions. Also, confirm the SKUs and description reflecting the promotion's adjustments. The date today is '2025-07-10'.",
        actions=[
            Action(
                name="UpdatePromotionDetails",
                kwargs={
                    "promotion_id": "PROMO-006",
                    "description": "Exclusive discount on smart thermostats.",
                    "applicable_skus": ["SMRT-THERM02"],
                },
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "AUDIO-BTSPKR02", "status": "limited_availability"},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-006"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "SMRT-THERM02"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-006", "description": "Exclusive discount on smart thermostats.", "applicable_skus": ["SMRT-THERM02"]},
            {"sku": "AUDIO-BTSPKR02", "status": "limited_availability"},
            {"sku": "SMRT-THERM02", "name": "EcoSmart Wi-Fi Thermostat"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_010",
        instruction="Administer marketing management activities. Introduce a new promotion titled 'Spring Cleaning Sale'. This promotion must offer a 'percentage' discount of 20.0% on 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01) and 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). The promotion's narrative should be '20% off selected home & kitchen items for spring cleaning.'. It should be 'scheduled' to occur from '2026-03-01' to '2026-03-15'. Prior to inauguration, verify the pricing and current 'is_discountable' state of both items. If any are non-discountable, amend their 'is_discountable' status to True. Post-creation of the promotion, retrieve all 'scheduled' promotions to verify its inclusion. Finally, set its 'times_used' to 0 and 'usage_limit' to 500. Access the promotion details by its ID to confirm updates.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "HOME-BTHTWL01", "is_discountable": True},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "KITCH-FRYPAN10"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "KITCH-FRYPAN10", "is_discountable": True},
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Spring Cleaning Sale",
                    "type": "percentage",
                    "discount_value": 20.0,
                    "description": "20% off selected home & kitchen items for spring cleaning.",
                    "applicable_skus": ["HOME-BTHTWL01", "KITCH-FRYPAN10"],
                    "start_date": "2026-03-01",
                    "end_date": "2026-03-15",
                    "status": "scheduled",
                    "usage_limit": None,
                    "times_used": 0
                },
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "scheduled"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-008", "times_used": 0, "usage_limit": 500}, # PROMO-008 is the next ID
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-008"},
            ),
        ],
        outputs=[
            {"sku": "HOME-BTHTWL01", "is_discountable": True},
            {"sku": "KITCH-FRYPAN10", "is_discountable": True},
            {"promotion_id": "PROMO-008", "status": "scheduled", "name": "Spring Cleaning Sale"},
            {"promotion_id": "PROMO-008", "times_used": 0, "usage_limit": 500},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_011",
        instruction="You are a customer service representative and your name is 'Jennifer Williams'. A customer ('Emma Wilson') is inquiring about the 'Summer Electronics Sale' (PROMO-001). The current date is '2025-08-10'. Gather its details, particularly its 'times_used' and 'end_date'. Since its 'end_date' ('2025-08-31') falls within this month or before, promptly deactivate this promotion. Modify its description to 'Promotion expired due to end date.' and change its status to 'expired'. Next, verify if 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) remains an applicable SKU and confirm its latest price and stock status at 'STORE-001'. Finally, obtain the updated promotion details through its ID.",
        actions=[
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="DeactivatePromotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-001", "status": "expired", "description": "Promotion expired due to end date."}, # De instrução
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-001"}, # Para confirmar
            )
        ],
        outputs=[
            {"promotion_id": "PROMO-001", "times_used": 0, "end_date": "2025-08-31"}, # Estado inicial do DB
            {"promotion_id": "PROMO-001", "status": "expired", "description": "Promotion expired due to end date."},
            {"sku": "ELEC-4KTV55", "price": 699.99},
            {"sku": "ELEC-4KTV55", "quantity": 8},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_012",
        instruction="Coordinate marketing management tasks. The 'Buy One Yoga Mat Get 50% Off Second' (PROMO-003) is planned and requires activation on '2025-06-10'. Prior to activating, retrieve product details for 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) to verify its category. If the category isn't 'Sports & Outdoors', adjust it to be 'Sports & Outdoors'. Then, initiate PROMO-003. After initiation, gather all active promotions to confirm its status and list every applicable SKU. Ultimately, increment 'times_used' for PROMO-003 by 1 for an internal evaluation.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "SPORT-YOGMAT01"},
            ),
            Action(
                name="UpdateProductDetails", # Condicional, mas executada para determinismo
                kwargs={"sku": "SPORT-YOGMAT01", "category": "Sports & Outdoors"},
            ),
            Action(
                name="ActivatePromotion",
                kwargs={"promotion_id": "PROMO-003"}, # Agora existe
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "active"},
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-003"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-003", "times_used": 1},
            ),
        ],
        outputs=[
            {"sku": "SPORT-YOGMAT01", "category": "Sports & Outdoors"},
            {"promotion_id": "PROMO-003", "status": "active", "applicable_skus": ["SPORT-YOGMAT01"]},
            {"promotion_id": "PROMO-003", "times_used": 1},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_013",
        instruction="Oversee sales responsibilities with associate name 'Michael Rodriguez'. A Gold level customer, 'Emma Wilson' (CUST-5001), intends to purchase 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02) from 'STORE-005' and 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01) from 'STORE-001'. The transaction will occur at 'STORE-001'. The date today is '2025-07-28'. Initially, obtain inventory details for both products from their respective stores. Next, acquire the complete product details for each. Check if 'Smart Home Starter Discount' (PROMO-006) is applicable for the speaker. *Since PROMO-006 concludes on 2025-07-20, it will not apply on 2025-07-28*. Estimate the total expenses excluding this discount. Process a transaction for 'Emma Wilson' at 'STORE-001' via 'credit_card', updating inventories. Lastly, enhance 'Emma Wilson's loyalty points by 50, and retrieve their updated customer details using their ID.",
        actions=[
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-001"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-28"}, # Esta chamada deve retornar {}, ou uma promoção inativa.
            ),
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Emma Wilson"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Michael Rodriguez"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0010",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-07-28",
                },
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0012",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-07-28",
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1003",
                    "total_amount": 156.41,
                    "tax_amount": 11.92,
                    "payment_method": "credit_card",
                    "discount_total": 0.00, # No discount applied
                    "customer_id": "CUST-5001",
                    "line_items": [
                        {"sku": "AUDIO-BTSPKR02", "quantity": 1, "unit_price": 129.99, "discount": 0.0},
                        {"sku": "HOME-BTHTWL01", "quantity": 1, "unit_price": 14.5, "discount": 0.0},
                    ],
                },
            ),
            Action(
                name="UpdateCustomerLoyaltyPoints",
                kwargs={"customer_id": "CUST-5001", "points_to_add": 50},
            ),
            Action(
                name="GetCustomerDetailsById", # Usar a nova ferramenta
                kwargs={"customer_id": "CUST-5001"},
            ),
        ],
        outputs=[
            {"transaction_id": "TXN-0013"},
            {"customer_id": "CUST-5001", "loyalty_points": 1290}, # 1240 (original) + 50
        ],
    ),
    Task(
        annotator="0",
        user_id="task_014",
        instruction="You are an inventory specialist and your name is 'Zoe Martinez'. Supervise the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) at 'STORE-001'. On '2025-08-01', retrieve its inventory specifics, focusing on 'quantity' and 'safety_stock'. Change the product's 'status' to 'out_of_stock' and the inventory's 'status' to 'out_of_stock' for ELEC-4KTV55 at STORE-001, indicating an immediate stock depletion in this scenario. In addition, irrespective of current stock level, deactivate the 'Summer Electronics Sale' (PROMO-001) if it is still active today, and revise its description to 'Deactivated due to inventory concerns.'. Ultimately, acquire all promotions marked as 'inactive' and the specifics of 'UltraVision 55\" 4K Smart TV' to confirm alterations.",
        actions=[
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-08-01"},
            ),
            Action(
                name="DeactivatePromotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-001", "description": "Deactivated due to inventory concerns.", "status": "inactive"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "ELEC-4KTV55", "status": "out_of_stock"},
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={"inventory_id": "INV-0001", "status": "out_of_stock"},
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "inactive"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
        ],
        outputs=[
            {"promotion_id": "PROMO-001", "status": "inactive", "description": "Deactivated due to inventory concerns."},
            {"sku": "ELEC-4KTV55", "status": "out_of_stock"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_015",
        instruction="Administer marketing management assignments. Adjust the pricing for all 'Grocery' items. Elevate the price for 'Organic Almond Butter 500g' (GROC-ALMBTR500) to 13.99 and 'SparkleLife Sparkling Water 1L (6 Pack)' (GROC-SPRWAT6P) to 8.50. Post-price adjustment, create a new 'fixed_bundle' promotion named 'Healthy Snack Bundle'. This promotion should provide a 5.0 discount when both 'Organic Almond Butter 500g' and 'High-Protein Granola Bars (12 Pack)' (GROC-GRNLBR12) are bought together. Its description must be 'Save on a healthy snack bundle.'. It should be 'active' from '2025-09-01' to '2025-10-31', with no usage limit and 0 times used. Validate the new prices of the revised products, and subsequently confirm the new promotion is listed as 'active' starting '2025-09-01' by extracting its details.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-ALMBTR500"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "GROC-ALMBTR500", "price": 13.99},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-SPRWAT6P"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "GROC-SPRWAT6P", "price": 8.50},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-GRNLBR12"},
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Healthy Snack Bundle",
                    "type": "fixed_bundle",
                    "discount_value": 5.0,
                    "description": "Save on a healthy snack bundle.",
                    "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12"],
                    "start_date": "2025-09-01",
                    "end_date": "2025-10-31",
                    "status": "active",
                    "usage_limit": None,
                    "times_used": 0
                },
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-ALMBTR500"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-SPRWAT6P"},
            ),
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Healthy Snack Bundle", "query_date": "2025-09-01"},
            ),
        ],
        outputs=[
            {"sku": "GROC-ALMBTR500", "price": 13.99},
            {"sku": "GROC-SPRWAT6P", "price": 8.50},
            {"promotion_id": "PROMO-008", "name": "Healthy Snack Bundle", "status": "active"}, # Assuming PROMO-008 is correct due to DB reset
        ],
    ),
    Task(
        annotator="0",
        user_id="task_016",
        instruction="Coordinate sales responsibilities with the associate 'Amanda Romano'. A customer identified as 'Liam Anderson' (CUST-5004), who is a Platinum member, intends to purchase 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) from 'STORE-003' and 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) from 'STORE-001'. The transaction needs to be finalized at 'STORE-001'. The current date is '2025-09-10'. Initially, verify stock for both products at their respective locations. Next, obtain comprehensive details for both items. Activate the 'Weekend Flash Sale - Home & Kitchen' (PROMO-007) for '2025-09-10' and '2025-09-11', and modify its applicable SKUs to incorporate 'OFFC-ERGCHR01' and 'HOME-DESKLMP01', setting the discount rate at 18.0%. Compute the total price, including the given discounts. Process a transaction for 'Liam Anderson' via 'debit_card'. Amend inventory for both items on '2025-09-10'. Conclusively, enhance 'Liam Anderson's loyalty points by 200 and elevate their 'membership_level' to 'diamond' as an exclusive upgrade. Fetch 'Liam Anderson's updated customer information using their ID.",
        actions=[
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "OFFC-ERGCHR01"},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "HOME-DESKLMP01"},
            ),
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Liam Anderson"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Amanda Romano"},
            ),
            Action(
                name="UpdatePromotionDetails", # Activate PROMO-007
                kwargs={"promotion_id": "PROMO-007", "status": "active", "start_date": "2025-09-10", "end_date": "2025-09-11"},
            ),
            Action(
                name="UpdatePromotionDetails", # Add SKUs and set discount value
                kwargs={"promotion_id": "PROMO-007", "applicable_skus": ["OFFC-ERGCHR01", "HOME-DESKLMP01", "HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "KITCH-FRYPAN10"], "discount_value": 18.0}, # Corrected applicable_skus
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0014",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-09-10",
                },
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={
                    "inventory_id": "INV-0015",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-09-10",
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-001",
                    "employee_id": "EMP-1009",
                    "total_amount": 235.21,
                    "tax_amount": 17.93,
                    "payment_method": "debit_card",
                    "discount_total": 47.70,
                    "customer_id": "CUST-5004",
                    "line_items": [
                        {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 41.3982},
                        {"sku": "HOME-DESKLMP01", "quantity": 1, "unit_price": 34.99, "discount": 6.2982},
                    ],
                },
            ),
            Action(
                name="UpdateCustomerLoyaltyPoints",
                kwargs={"customer_id": "CUST-5004", "points_to_add": 200},
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5004", "membership_level": "diamond"},
            ),
            Action(
                name="GetCustomerDetailsById", # Corrected to get full details
                kwargs={"customer_id": "CUST-5004"},
            ),
        ],
        outputs=[
            {"transaction_id": "TXN-0013"}, # Expected next sequential ID
            {"customer_id": "CUST-5004", "loyalty_points": 1720, "membership_level": "diamond"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_017",
        instruction="You are a regional manager. The inventory of 'Apparel' merchandise is substantial in 'STORE-002' and scarce in 'STORE-001'. Initially, ensure all items in the 'Apparel' category are tagged as discountable within the system. Then, arrange for the transfer of 10 units of 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 3 units of 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) from 'STORE-002' to 'STORE-001'. As you create the new inventory entries at the destination, allocate them to the 'Apparel Zone' area. Following the transfers, launch a new 'percentage' promotion titled 'Apparel Off-Season Sale' featuring a 15% discount with the description 'Get our apparel for less during the off-season.'. This promotion should cover all 'Apparel' items and be set from '2025-10-01' to '2025-10-31'. Lastly, verify the promotion's new details by accessing it through its ID.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "CLTH-SLFJEAN34"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True},
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "CLTH-WINJKT01"},
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True},
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001", "location": "Apparel Zone"},
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Apparel Zone"},
            ),
            Action(
                name="ExecuteInventoryTransfer",
                kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 10, "from_store_id": "STORE-002", "to_store_id": "STORE-001"},
            ),
            Action(
                name="ExecuteInventoryTransfer",
                kwargs={"sku": "CLTH-WINJKT01", "quantity": 3, "from_store_id": "STORE-002", "to_store_id": "STORE-001"},
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Apparel Off-Season Sale",
                    "type": "percentage",
                    "discount_value": 15.0,
                    "description": "Get our apparel for less during the off-season.",
                    "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                    "start_date": "2025-10-01",
                    "end_date": "2025-10-31",
                    "status": "scheduled",
                    "usage_limit": None,
                    "times_used": 0
                },
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-008"},
            ),
        ],
        outputs=["PROMO-008"],
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction="As a Marketing Director, orchestrate the launch of a targeted flash sale geared towards our most esteemed customers. To start, pinpoint all the products classified under the 'Electronics' category. Next, identify all 'gold' and 'platinum' customers who have purchased any of these electronics. Upon defining this target group, establish a 'percentage' promotion named 'VIP Electronics Sale' with a 25% discount, set to run from '2025-08-15' to '2025-08-20', described as 'An exclusive electronics offer for our VIPs.'. After setting up the promotion, produce and allocate a distinct, single-use code to each eligible customer. Lastly, update the promotion to necessitate a unique code upon redemption and retrieve the customer details of those who received a code to verify their eligibility.",
        actions=[
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["gold", "platinum"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "VIP Electronics Sale",
                    "type": "percentage",
                    "discount_value": 25.0,
                    "description": "An exclusive electronics offer for our VIPs.",
                    "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                    "start_date": "2025-08-15",
                    "end_date": "2025-08-20",
                    "status": "scheduled",
                    "usage_limit": None,
                    "times_used": 0
                },
            ),
            Action(
                name="GenerateAndAssignPromoCodes",
                kwargs={
                    "customer_ids": ["CUST-5001", "CUST-5010"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5010"},
            ),
        ],
        outputs=["PROMO-008", "CUST-5001", "CUST-5010"],
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction="As a CRM Manager, aim to reward our active 'silver' tier customers. Begin by identifying all products falling under the 'Home & Kitchen' category. Utilize this data to locate all 'silver' members with purchases of these items. For every customer identified, evaluate their current loyalty points. Grant a loyalty bonus by upgrading any customer with over 800 points within this segment to 'gold' membership status without delay. Following the upgrades, obtain the comprehensive details for each upgraded customer to verify their new status.",
        actions=[
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Home & Kitchen"},
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["silver"],
                    "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                },
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5002"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5006"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5009"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5011"},
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5002", "membership_level": "gold"},
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5006", "membership_level": "gold"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5002"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5006"},
            ),
        ],
        outputs=[
            {"customer_id": "CUST-5002", "membership_level": "gold"},
            {"customer_id": "CUST-5006", "membership_level": "gold"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_020",
        instruction="In your capacity as a Marketing Director, embark on a campaign targeted at outdoor enthusiasts. Start by distinguishing all products in the 'Sports & Outdoors' category. Using this information, find all 'gold' and 'platinum' customers who have ever bought any of these items. For this particular group, establish a new 'percentage' promotion dubbed 'VIP Adventure Gear Offer' with a 20% discount, scheduled for the full month of September and described as 'A special offer for our top adventurers.'. Once the promotion is in place, generate unique, one-time-use promo codes for all eligible customers. Ultimately, confirm the information of all customers who were provided with a code.",
        actions=[
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Sports & Outdoors"},
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["gold", "platinum"],
                    "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                },
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "VIP Adventure Gear Offer",
                    "type": "percentage",
                    "discount_value": 20.0,
                    "description": "A special offer for our top adventurers.",
                    "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                    "start_date": "2025-09-01",
                    "end_date": "2025-09-30",
                    "status": "scheduled",
                },
            ),
            Action(
                name="GenerateAndAssignPromoCodes",
                kwargs={
                    "customer_ids": ["CUST-5004"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5004"},
            ),
        ],
        outputs=["PROMO-008", "CUST-5004"],
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction="As a CRM Manager tasked with recognizing top-tier customers, locate all customers classified as 'gold' who have made purchases in the 'Electronics' category. Upon identification, access their detailed records to verify their current loyalty points. If any customer has amassed between 1000 and 2000 loyalty points, offer them an upgrade to 'platinum' membership as a special reward for their loyalty. Once all upgrades are accomplished, recheck the updated customers' records to confirm their new 'platinum' status.",
        actions=[
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["gold"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5010"},
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5001", "membership_level": "platinum"},
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5010", "membership_level": "platinum"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5010"},
            ),
        ],
        outputs=[
            {"customer_id": "CUST-5001", "membership_level": "platinum"},
            {"customer_id": "CUST-5010", "membership_level": "platinum"},
        ],
    ),
    Task(
        annotator="0",
        user_id="task_022",
        instruction="You are serving as a Sales Lead, 'Ethan Walker', at STORE-002, assisting customer 'Noah Tran'. The customer intends to buy a 'ProSlice 8\" Chef Knife' and 'Men's Slim Fit Jeans - 34W 32L'. To facilitate the sale, initialize a 'percentage' promotion titled 'STORE-002 Daily Deal' providing a 20% discount on these specified items, **with the description 'Daily deal on select items.'**, active for the current date. Compute the total cost after applying this discount and proceed with the transaction using a 'credit_card', ensuring to first check the inventory records of the items at your store and update their stock levels accordingly.",
        actions=[
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Noah Tran"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Ethan Walker"},
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "STORE-002 Daily Deal",
                    "type": "percentage",
                    "discount_value": 20.0,
                    "description": "Daily deal on select items.",
                    "applicable_skus": ["KITCH-CHEFKNF8", "CLTH-SLFJEAN34"],
                    "start_date": "2025-07-28",
                    "end_date": "2025-07-28",
                    "status": "active",
                    "times_used": 0,
                },
            ),
            Action(
                name="CalculateTransactionTotals",
                kwargs={
                    "line_items": [
                        {"sku": "KITCH-CHEFKNF8", "quantity": 1},
                        {"sku": "CLTH-SLFJEAN34", "quantity": 1}
                    ],
                    "promotion_ids": ["PROMO-008"],
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-002",
                    "customer_id": "CUST-5002",
                    "employee_id": "EMP-1011",
                    "payment_method": "credit_card",
                    "total_amount": 77.46,
                    "tax_amount": 5.9,
                    "discount_total": 17.89,
                    "line_items": [
                        {"sku": "KITCH-CHEFKNF8", "quantity": 1, "unit_price": 39.95, "discount": 7.99},
                        {"sku": "CLTH-SLFJEAN34", "quantity": 1, "unit_price": 49.50, "discount": 9.90}
                    ],
                },
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0011", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0005", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
        ],
        outputs=["TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction="While working as a sales associate, 'Amelia Lee', at STORE-004, a customer named 'Liam Anderson' wishes to buy two 'TrailGuard Mountain Bike Helmets' and one 'EcoSmart Wi-Fi Thermostat'. Start by replenishing the store inventory with 5 units of the 'EcoSmart Wi-Fi Thermostat', creating a new entry in the 'Smart Home Display' if required. Proceed with processing the customer's purchase. Verify whether the 'Smart Home Starter Discount' is valid for the thermostat on today's date, 2025-07-28. Since the promotion has expired, omit discounts. Complete the sale calculation and process the payment via 'credit_card', making sure to adjust stock levels for both products.",
        actions=[
            Action(
                name="GetCustomerIdByName",
                kwargs={"customer_name": "Liam Anderson"},
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Amelia Lee"},
            ),
            Action(
                name="GetPromotionByNameAndDate",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-28"},
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-004", "location": "Smart Home Display"},
            ),
            Action(
                name="UpdateStockLevel",
                kwargs={"inventory_id": "INV-0025", "quantity_to_add": 5},
            ),
            Action(
                name="CalculateTransactionTotals",
                kwargs={
                    "line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 2}, {"sku": "SMRT-THERM02", "quantity": 1}],
                    "promotion_ids": [],
                },
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-004",
                    "customer_id": "CUST-5004",
                    "employee_id": "EMP-1032",
                    "payment_method": "credit_card",
                    "total_amount": 386.45,
                    "tax_amount": 29.45,
                    "discount_total": 0.0,
                    "line_items": [
                        {"sku": "SPORT-BIKHLM01", "quantity": 2, "unit_price": 89.0, "discount": 0},
                        {"sku": "SMRT-THERM02", "quantity": 1, "unit_price": 179.0, "discount": 0}
                    ],
                },
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-004"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0009", "quantity_sold": 2, "last_stock_count_date": "2025-07-28"},
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
        ],
        outputs=["TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction="As the inventory manager, 'Amelia Lee', at STORE-004, you've observed a low stock of 'TrailGuard Mountain Bike Helmet'. To avoid running out, launch a temporary 'percentage' promotion named 'Helmet Pre-Clearance' offering a 5% discount and described as 'Temporary discount to clear final units.' Activate it for today's date, '2025-07-29', initially setting usage count to zero with no limit on usage. Promptly deactivate it after setup. Proceed to create an inventory record for the helmet at the main warehouse, STORE-001, within the 'Central Stock' area. Transfer all 4 remaining units from your store to the warehouse, ensuring all reservations are canceled. Lastly, modify your store's inventory status to indicate the helmet is out of stock.",
        actions=[
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Amelia Lee"},
            ),
            Action(
                name="GetProductSkuByName",
                kwargs={"product_name": "TrailGuard Mountain Bike Helmet"},
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"},
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Helmet Pre-Clearance",
                    "type": "percentage",
                    "discount_value": 5.0,
                    "description": "Temporary discount to clear final units.",
                    "applicable_skus": ["SPORT-BIKHLM01"],
                    "start_date": "2025-07-29",
                    "end_date": "2025-07-29",
                    "status": "active",
                    "usage_limit": None,
                    "times_used": 0,
                },
            ),
            Action(
                name="DeactivatePromotion",
                kwargs={"promotion_id": "PROMO-008"},
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-001", "location": "Central Stock"},
            ),
            Action(
                name="ExecuteInventoryTransfer",
                kwargs={"sku": "SPORT-BIKHLM01", "quantity": 4, "from_store_id": "STORE-004", "to_store_id": "STORE-001"},
            ),
            Action(
                name="UpdateInventoryReservedQuantity",
                kwargs={"inventory_id": "INV-0009", "change_amount": -1},
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={"inventory_id": "INV-0009", "status": "out_of_stock"},
            ),
        ],
        outputs=[{"inventory_id": "INV-0009", "status": "out_of_stock"}],
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction="In the role of Marketing Specialist, your task is to establish a new 'percentage' promotion entitled 'Back-to-School Tech Sale', providing a 15% reduction on all 'Electronics', with the description '15% off all electronics for the back-to-school season.'. Schedule the promotion to start on '2025-08-18' and conclude on '2025-08-31'. After setting up the promotion, distribute unique promo codes to all 'gold' membership customers who have previously bought products in the 'Electronics' category. Conclude by reviewing the promotion's setup details to ensure it is configured accurately.",
        actions=[
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["gold"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Back-to-School Tech Sale",
                    "type": "percentage",
                    "discount_value": 15.0,
                    "description": "15% off all electronics for the back-to-school season.",
                    "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                    "start_date": "2025-08-18",
                    "end_date": "2025-08-31",
                    "status": "scheduled",
                    "usage_limit": None,
                    "times_used": 0,
                },
            ),
            Action(
                name="GenerateAndAssignPromoCodes",
                kwargs={
                    "customer_ids": ["CUST-5001", "CUST-5010"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="GetPromotionById",
                kwargs={"promotion_id": "PROMO-008"},
            ),
        ],
        outputs=["PROMO-008"],
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction="On '2025-09-05', as a regional manager, you've detected a surplus of 'Apparel' at 'STORE-002'. Your aim is to combine this inventory at 'STORE-001' and start a clearance sale. Initially, mark 'Men's Slim Fit Jeans - 34W 32L' and 'ArcticShield Men's Parka - Large' as eligible for discounts. Next, locate their present stock and reservations at 'STORE-002', then move the whole physical inventory to 'STORE-001', creating fresh inventory records in the 'Apparel Zone' if necessary, while removing any reservations at the origin. After completing the transfer, establish a new 'percentage' promotion titled 'Final Apparel Clearance' offering a 35% reduction, with the description 'Final sale on select apparel items.', set for '2025-09-06' through '2025-09-20', solely applicable to these SKUs. Lastly, verify the updated stock levels at 'STORE-001'.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001", "location": "Apparel Zone"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Apparel Zone"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 30, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0005", "change_amount": -6}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 6, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0022", "change_amount": -1}),
            Action(name="CreatePromotion", kwargs={
                "name": "Final Apparel Clearance", "type": "percentage", "discount_value": 35.0,
                "description": "Final sale on select apparel items.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-06", "end_date": "2025-09-20", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001"}),
        ],
        outputs=[
            {"inventory_id": "INV-0025", "sku": "CLTH-SLFJEAN34", "quantity": 30},
            {"inventory_id": "INV-0026", "sku": "CLTH-WINJKT01", "quantity": 6},
        ]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction="Serving as a CRM Manager on '2025-10-01', your intention is to initiate a focused campaign for 'platinum' members who regularly buy 'Sports & Outdoors' goods. Your objective is to locate these members and present a special offer. Start by identifying all items within the 'Sports & Outdoors' category. Utilize this catalog to find all 'platinum' customers who have bought these products. For this group, set up a new 'percentage' promotion called 'Platinum Adventurer Reward' with a 25% discount, alongside the description 'An exclusive reward for our top adventurers.', planned from '2025-10-02' to '2025-10-16', applicable to all 'Sports & Outdoors' goods. Subsequently, produce unique, single-use promo codes for all eligible customers. In the end, validate the promotion ID and compile a list of customer IDs who received a code.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["platinum"],
                "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]
            }),
            Action(name="CreatePromotion", kwargs={
                "name": "Platinum Adventurer Reward", "type": "percentage", "discount_value": 25.0,
                "description": "An exclusive reward for our top adventurers.",
                "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                "start_date": "2025-10-02", "end_date": "2025-10-16", "status": "scheduled", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={
                "customer_ids": ["CUST-5004"],
                "promotion_id": "PROMO-008"
            }),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5004"}),
        ],
        outputs=["PROMO-008", ["CUST-5004"]]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction="On '2025-07-15', as the customer service lead 'Jennifer Williams', manage a return for 'James O'Connor'. He aims to send back two 'High-Protein Granola Bars (12 Pack)' from transaction 'TXN-0003'. Nevertheless, after inspection, one package is expired. Carry out the return solely for the item that is not expired, providing credit. Due to the inconvenience, locate all 'bronze' members who have acquired 'Grocery' goods and elevate them to 'silver' status. Additionally, deactivate the 'Kitchen Essentials Bundle' promotion as it concludes today and revise its description to 'Promotion has expired.'",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "James O'Connor"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "High-Protein Granola Bars (12 Pack)"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0003", "sku": "GROC-GRNLBR12", "quantity_returned": 1, "unit_price": 14.99}),
            Action(name="GetProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["bronze"],
                "purchase_history_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"]
            }),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5003", "membership_level": "silver"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Kitchen Essentials Bundle", "query_date": "2025-07-15"}),
            Action(name="DeactivatePromotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-002", "description": "Promotion has expired."})
        ],
        outputs=[
            {"customer_id": "CUST-5003", "membership_level": "silver"},
            {"promotion_id": "PROMO-002", "status": "inactive"},
        ]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction="Acting as the inventory manager 'Zoe Martinez' on '2025-06-20', you have to audit the stock for 'BrewMaster 12-Cup Coffee Maker' at 'STORE-001'. Begin by pulling its inventory record. You've manually counted 20 units. Should this count disagree with the system's total (currently 25), adjust the stock levels to match your physical count. Following the adjustment in quantity, establish a new 'percentage' promotion called 'Coffee Lovers Special' granting an 8% discount, paired with the description 'A special deal on BrewMaster coffee makers.' to promote the remaining stock, active from '2025-06-21' to '2025-07-21'.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -5}),
            Action(name="CreatePromotion", kwargs={
                "name": "Coffee Lovers Special", "type": "percentage", "discount_value": 8.0,
                "description": "A special deal on BrewMaster coffee makers.",
                "applicable_skus": ["HOM-COFMKR12"],
                "start_date": "2025-06-21", "end_date": "2025-07-21", "status": "active", "times_used": 0
            })
        ],
        outputs=[
            {"inventory_id": "INV-0003", "quantity": 20},
            {"promotion_id": "PROMO-008", "status": "active"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_030",
        instruction="As 'Robert Zhang' (EMP-1008), a manager at 'STORE-002', you receive a return request from customer 'Mia Kim' (CUST-5011) for one 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) from her transaction 'TXN-0011' because of a defect. This item cannot be resold. Process the return, ensuring the general inventory number is corrected and deduct the 'reserved_quantity' for that item by one. To apologize for the inconvenience, increase her loyalty account by 75 points. She then opts to buy an 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) using her 'credit_card'. Firstly, make this product discountable. Then, create a 10% 'percentage' promotion titled 'Winter Gear Welcome' for this item, effective today (2025-07-29). The promotion's description must read 'A special welcome discount on winter apparel.' and initialize its usage count to zero. Inspect the parka's stock at 'STORE-002', calculate the final price with the new promotion, and process the transaction. Ultimately, update the parka's inventory log to record the sale.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Mia Kim"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ProSlice 8\" Chef Knife"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5011", "sku": "KITCH-CHEFKNF8"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0011", "sku": "KITCH-CHEFKNF8", "quantity_returned": 1, "unit_price": 39.95}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0011", "change_amount": -1}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 75}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="CreatePromotion", kwargs={
                "name": "Winter Gear Welcome", "type": "percentage", "discount_value": 10.0,
                "description": "A special welcome discount on winter apparel.", "applicable_skus": ["CLTH-WINJKT01"],
                "start_date": "2025-07-29", "end_date": "2025-07-29", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 1}], "promotion_ids": ["PROMO-008"]
            }),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Robert Zhang"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1008", "customer_id": "CUST-5011", "payment_method": "credit_card",
                "total_amount": 184.62, "tax_amount": 14.07, "discount_total": 18.95,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 1, "unit_price": 189.5, "discount": 18.95}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction="As the inventory manager, 'Zoe Martinez', you've observed that the 'Apparel' category is stocked too heavily at 'STORE-002' while 'STORE-003' is running low. Specifically, the 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) are affected. The parka is not marked as 'is_discountable'. Begin by updating the parka's product details to permit discounts. Next, relocate 20 units of the jeans and 5 units of the parka from 'STORE-002' to 'STORE-003', ensuring new inventory records at 'STORE-003' in the 'Apparel Dept' location are created beforehand. Once this is done, establish a new 'percentage' promotion titled 'Store 3 Apparel Sale' offering a 20% discount, with the description 'Special sale on newly transferred apparel!', exclusively applicable to these SKUs, scheduled for '2025-08-15' to '2025-08-31'. Finally, verify the refreshed stock levels for both products at 'STORE-003'.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003", "location": "Apparel Dept"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-003", "location": "Apparel Dept"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 20, "from_store_id": "STORE-002", "to_store_id": "STORE-003"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 5, "from_store_id": "STORE-002", "to_store_id": "STORE-003"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Store 3 Apparel Sale", "type": "percentage", "discount_value": 20.0,
                "description": "Special sale on newly transferred apparel!", "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-08-15", "end_date": "2025-08-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-003"})
        ],
        outputs=[
            {"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003", "quantity": 20},
            {"sku": "CLTH-WINJKT01", "store_id": "STORE-003", "quantity": 5}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction="As the sales lead, 'Ethan Walker', at 'STORE-002', you encounter a new customer, 'Dr. Evelyn Reed'. She is a high-value client, so you can directly assign her to the 'platinum' tier. Create an account for 'Dr. Evelyn Reed' with 'platinum' membership, 2000 initial loyalty points, and marketing consent given. She is interested in buying the 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15) and the 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01). First, check the laptop details and you'll see it is not discountable. Adjust the product to be eligible for discounts. Then, verify the stock availability for both products at your location. Additionally, confirm if the 'Summer Electronics Sale' promotion is currently active on '2025-07-29' for either product. Compute the transaction totals, integrating any applicable discounts. Proceed with the payment via 'credit_card', document the transaction using the calculated totals, and adjust stock levels accordingly. Finally, provide the new customer ID and the transaction ID.",
        actions=[
            Action(name="CreateCustomer", kwargs={
                "name": "Dr. Evelyn Reed", "membership_level": "platinum", "opt_in_marketing": True, "loyalty_points": 2000
            }),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "ELEC-GAMLP15", "is_discountable": True}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-07-29"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1}, {"sku": "AUDIO-NCEBUDS01", "quantity": 1}], "promotion_ids": ["PROMO-001"]
            }),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Ethan Walker"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1011", "customer_id": "CUST-5013", "payment_method": "credit_card",
                "total_amount": 1622.76, "tax_amount": 123.67, "discount_total": 149.90,
                "line_items": [
                    {"sku": "ELEC-GAMLP15", "quantity": 1, "unit_price": 1499.0, "discount": 149.90},
                    {"sku": "AUDIO-NCEBUDS01", "quantity": 1, "unit_price": 149.99, "discount": 0.0}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0013", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0016", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=["Customer ID: CUST-5013", "Transaction ID: TXN-0013"]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction="In your role as the Marketing Director, initiate a campaign to motivate customers who have purchased electronics to explore our 'Smart Home' products. Begin by identifying all items within the 'Electronics' category. Next, locate all 'gold' and 'platinum' tier customers who have purchased any of these electronics. Create a new 'percentage' promotion for this audience named 'Smart Home Upgrade', offering a 25% discount on all 'Smart Home' products, with the description 'An exclusive offer to make your home smarter.', scheduled from '2025-09-01' to '2025-09-15'. After establishing the promotion, produce and distribute unique, single-use codes to each qualifying customer. Lastly, update the promotion to necessitate a code and retrieve the customer details to confirm their names and membership statuses.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["gold", "platinum"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]
            }),
            Action(name="GetProductsByCategory", kwargs={"category": "Smart Home"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Smart Home Upgrade", "type": "percentage", "discount_value": 25.0,
                "description": "An exclusive offer to make your home smarter.", "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-09-01", "end_date": "2025-09-15", "status": "scheduled", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-008", "requires_code": True}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[
            {"name": "Emma Wilson", "membership_level": "gold"},
            {"name": "Benjamin Cohen", "membership_level": "gold"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction="As a regional manager, oversee the purchase process for customer 'William Zhang' (CUST-5006), who intends to buy two items located at different stores: 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is at 'STORE-003' and 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) is at 'STORE-002'. The transaction will be handled at 'STORE-002' by employee 'Robert Zhang', and payment will be made using a 'debit_card'. Verify stock availability for each item at their respective locations. Since no promotions are available for these items today (2025-07-29), calculate the final amount without discounts. Execute the transaction at 'STORE-002'. Post-transaction, ensure you update stock levels at BOTH 'STORE-002' and 'STORE-003'. Given the purchase total, upgrade 'William Zhang's' membership from 'silver' to 'gold'. Finally, obtain the complete details of the customer to confirm their new membership level.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "William Zhang"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Robert Zhang"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "OFFC-ERGCHR01", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}]
            }),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1008", "customer_id": "CUST-5006", "payment_method": "debit_card",
                "total_amount": 292.21, "tax_amount": 22.27, "discount_total": 0.0,
                "line_items": [
                    {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 0.0},
                    {"sku": "KITCH-CHEFKNF8", "quantity": 1, "unit_price": 39.95, "discount": 0.0}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0014", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0011", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction="In your capacity as the inventory manager, 'Zoe Martinez', it's been found that there are pricing errors for two key kitchen items. 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) is currently priced at $39.95 but needs to be updated to $42.50. 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10) should be changed from $24.95 to $27.00. Start by retrieving details for both items to verify current pricing, then adjust them to the correct amounts. To counterbalance this increase, promptly create a 'fixed_bundle' promotion called 'Kitchen Starter Duo', offering a $10.00 discount when both items are purchased together. The promotion should state 'Save $10 on our top kitchen tools bundle.', run from '2025-08-01' to '2025-08-31', with an initial use count of 0. Finally, pull the new promotion by its ID to confirm its establishment.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-FRYPAN10"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "KITCH-CHEFKNF8", "price": 42.50}),
            Action(name="UpdateProductDetails", kwargs={"sku": "KITCH-FRYPAN10", "price": 27.00}),
            Action(name="CreatePromotion", kwargs={
                "name": "Kitchen Starter Duo", "type": "fixed_bundle", "discount_value": 10.0,
                "description": "Save $10 on our top kitchen tools bundle.",
                "applicable_skus": ["KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-08-01", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-008", "name": "Kitchen Starter Duo"}]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction="As a Regional Manager, your responsibility involves handling a recall issued for 'PowerPlus Rechargeable AA Batteries (4 Pack)' (ELEC-RCHAA04) due to safety concerns. To begin, locate the inventory record for this product at 'STORE-003' and update its status to 'recalled'. After that, update the main product entry in your system, altering its status to 'discontinued' to halt any future orders. Actively identify customers who have purchased this item before. Allocate 150 loyalty points to each 'gold' or 'platinum' customer identified from these transactions as a form of apology. Lastly, obtain the revised customer details for 'Emma Wilson' to verify her updated point balance.",
        actions=[
            Action(
                name="GetProductSkuByName",
                kwargs={"product_name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003"}
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={"inventory_id": "INV-0020", "status": "recalled"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "ELEC-RCHAA04", "status": "discontinued"}
            ),
            # ACTION CORRIGIDA:
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "purchase_history_skus": ["ELEC-RCHAA04"],
                    "membership_levels": ["gold", "platinum"],
                },
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5001"}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5010"}
            ),
            Action(
                name="UpdateCustomerLoyaltyPoints",
                kwargs={"customer_id": "CUST-5001", "points_to_add": 150}
            ),
            Action(
                name="UpdateCustomerLoyaltyPoints",
                kwargs={"customer_id": "CUST-5010", "points_to_add": 150}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5001"}
            )
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1390}],
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction="As 'Jack Robinson', a sales associate at 'STORE-001', on the date '2025-07-29', you are assisting 'platinum' level customer 'Liam Anderson'. He intends to purchase two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) and one 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55). He refers to the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003), which is currently 'scheduled'. Start by verifying the inventory at 'STORE-001' for at least two yoga mats and one TV to be available. Following this, activate 'PROMO-003'. Once activated, proceed to process the transaction using 'credit_card'. Make sure the transaction reflects a discount_total of $15.00, a tax_amount of $61.46, and a total_amount of $806.43. Finally, update the stock for all three sold items and increment 'times_used' count for the promotion by one.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Liam Anderson"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Jack Robinson"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="ActivatePromotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1034", "customer_id": "CUST-5004", "payment_method": "credit_card",
                "total_amount": 806.43, "tax_amount": 61.46, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00},
                    {"sku": "ELEC-4KTV55", "quantity": 1, "unit_price": 699.99, "discount": 0.0}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0001", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction="As a CRM Manager, your objective is to reintroduce 'bronze' level customers who have solely bought 'Grocery' items and possess fewer than 500 loyalty points. Start by identifying all products within the 'Grocery' category. Utilize this list to spot qualifying 'bronze' customers. Once identified, upgrade their membership to 'silver' as a complimentary incentive. Then, detect all products within the 'Home & Kitchen' category. Develop a new 'percentage' promotion titled 'Welcome to Our Home Section' offering a 25% discount on all 'Home & Kitchen' merchandise. Ensure that the description reads 'A special offer to explore our Home & Kitchen products.' and set its activity span for September 2025, with an initial usage count of 0. Lastly, generate unique single-use promo codes for these promoted customers and verify the new 'silver' status of 'Sophia Singh'.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["bronze"],
                "purchase_history_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"]
            }),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5003", "membership_level": "silver"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Welcome to Our Home Section", "type": "percentage", "discount_value": 25.0,
                "description": "A special offer to explore our Home & Kitchen products.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                "start_date": "2025-09-01", "end_date": "2025-09-30", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5003"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5003"}),
        ],
        outputs=[{"customer_id": "CUST-5003", "membership_level": "silver"}]
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction="As 'Megan Young', Store Manager at 'STORE-005', you've decided to stock a high-value item, the 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15), to boost sales at your location. Presently, your store lacks inventory for this item, but you are aware 'STORE-002' has stock. Start by confirming the laptop's availability at 'STORE-002'. Proceed to create a new inventory record for the laptop at your location ('STORE-005') under the 'Premium Electronics Shelf' section. Then, manage a transfer of one unit from 'STORE-002' to 'STORE-005'. Given that the stock level at your store will be minimal, update the inventory status to 'low_stock' immediately. To promote the new stock, initiate a 'percentage' promotion titled 'STORE-005 Laptop Special' with a 12% discount. The promotion's description must be 'Exclusive deal on our new gaming laptop at STORE-005!' and it should run from '2025-08-01' to '2025-08-15', starting with a usage count of 0. Conclude by retrieving the new inventory record from your store to verify successful transfer completion.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-005", "location": "Premium Electronics Shelf"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-002", "to_store_id": "STORE-005"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "low_stock"}),
            Action(name="CreatePromotion", kwargs={
                "name": "STORE-005 Laptop Special", "type": "percentage", "discount_value": 12.0,
                "description": "Exclusive deal on our new gaming laptop at STORE-005!",
                "applicable_skus": ["ELEC-GAMLP15"],
                "start_date": "2025-08-01", "end_date": "2025-08-15", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-005"})
        ],
        outputs=[{"id": "INV-0025", "sku": "ELEC-GAMLP15", "quantity": 1, "status": "low_stock", "store_id": "STORE-005"}]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction="As a CRM Manager, you need to reward customer 'Liam Anderson' (CUST-5004) following his high-value transaction 'TXN-0004'. Retrieve his customer details using his name to verify his current 'platinum' status and loyalty points. Due to his substantial purchase, elevate his membership to the new 'diamond' tier. Next, discern all products in the 'Office Supplies' category. Establish a new 'percentage' promotion called 'Diamond Member Exclusive', offering a 30% discount applicable to all 'Office Supplies' products. Ensure the promotion's description is 'An exclusive 30% off Office Supplies for our new Diamond members.' Set it to become active for one month starting today, '2025-08-01', with a beginning usage count of 0. Finally, issue a single-use promo code to 'Liam Anderson' for this promotion and retrieve his updated customer details to confirm his new 'diamond' status.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Liam Anderson"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5004"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5004", "membership_level": "diamond"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Office Supplies"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Diamond Member Exclusive", "type": "percentage", "discount_value": 30.0,
                "description": "An exclusive 30% off Office Supplies for our new Diamond members.",
                "applicable_skus": ["OFFC-ERGCHR01"],
                "start_date": "2025-08-01", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[{"customer_id": "CUST-5004", "membership_level": "diamond"}]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction="You are 'Zoe Martinez', an inventory specialist at 'STORE-001'. A physical count of the 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12) indicates only 20 units, although the system lists more. Start by obtaining the inventory record for this item at 'STORE-001' to check the current system quantity. You need to amend the inventory by adjusting the stock level to 20 units. As this new total falls under the 'reorder_level', you are required to change the inventory item's status to 'low_stock'. To sell off the remaining items ahead of a new shipment, initiate a 'percentage' promotion named 'Coffee Maker Clearance' offering a 25% discount. The description must be 'Final clearance on BrewMaster Coffee Makers.' and it should commence today, '2025-08-02', for a one-week duration. Prior to launching the promotion, confirm that the product is eligible for discounting. Finally, access the updated inventory record to verify the new quantity and status.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -5}), # 25 -> 20
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0003", "status": "low_stock"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Coffee Maker Clearance", "type": "percentage", "discount_value": 25.0,
                "description": "Final clearance on BrewMaster Coffee Makers.",
                "applicable_skus": ["HOM-COFMKR12"],
                "start_date": "2025-08-02", "end_date": "2025-08-09", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0003", "quantity": 20, "status": "low_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction="You are 'Jennifer Williams', customer service lead at 'STORE-001'. Today, '2025-07-29', 'Emma Wilson' (CUST-5001) is returning items from transaction 'TXN-0001'. She is returning an 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), which is in mint condition, and a 'PowerPlus Rechargeable AA Batteries (4 Pack)' (ELEC-RCHAA04), which is faulty. Her receipt shows the batteries were bought for $18.95. Process the return for both items: adjust the TV's stock count upwards, but not for the faulty batteries. Calculate the total credit for her. The customer intends to use this credit to buy a 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15). This laptop is absent from your store's stock. First, establish an inventory record for it at 'STORE-001' (location: 'Customer Service Hold') and then arrange a transfer of a unit from 'STORE-002'. Following a successful transfer, compute the final transaction totals for the laptop, applying the total credit. The customer shall pay the remaining amount via 'debit_card'. Create the new transaction and update the laptop's inventory at your store.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Emma Wilson"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "UltraVision 55\" 4K Smart TV"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0001", "sku": "ELEC-4KTV55", "quantity_returned": 1, "unit_price": 699.99}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0001", "sku": "ELEC-RCHAA04", "quantity_returned": 1, "unit_price": 18.95}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-001", "location": "Customer Service Hold"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1}],
                "credit_amount": 718.94
            }),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Jennifer Williams"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1004", "customer_id": "CUST-5001", "payment_method": "debit_card",
                "total_amount": 844.41, "tax_amount": 64.35, "discount_total": 0.0,
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1, "unit_price": 1499.0, "discount": 0.0}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction="You are a Regional Manager overseeing a supplier transition. The supplier 'UrbanEdge' (SUP-1003) is being phased out, and thus all their products, particularly 'Men's Slim Fit Jeans - 34W 32L' and 'ArcticShield Men's Parka - Large', need liquidation. Begin by updating both product records to reflect a 'discontinued' status. Subsequently, gather all remaining physical stocks of the parka from 'STORE-002' (totaling 6 units) by moving them to a new inventory record at 'STORE-001' in the 'Liquidation Center'. Post-transfer, initiate a conclusive, forceful 'percentage' promotion named 'UrbanEdge Final Sale' at a 70% discount for both products. The description of the promotion must be 'Final sale on all discontinued UrbanEdge products.' and its initial usage count must be 0. The promotion needs to be effective from '2025-09-01' to '2025-09-30'. As a successor, you plan to introduce the 'UrbanExplorer Tech Jacket'. Adapt the product record for 'Adventures in Sillytown' (BOOK-KDSSTY01) for this new jacket: update its name, classify it as 'Apparel', set the price to 219.99, and ensure it is discountable. Finally, create new inventory records for this jacket at 'STORE-002' and 'STORE-003' in the 'New Arrivals' area and set their stock levels to 50 units each in preparation for the launch.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-SLFJEAN34", "status": "discontinued"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "status": "discontinued"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Liquidation Center"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 6, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="CreatePromotion", kwargs={
                "name": "UrbanEdge Final Sale", "type": "percentage", "discount_value": 70.0,
                "description": "Final sale on all discontinued UrbanEdge products.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-01", "end_date": "2025-09-30", "status": "active", "times_used": 0
            }),
            Action(name="UpdateProductDetails", kwargs={
                "sku": "BOOK-KDSSTY01", "name": "UrbanExplorer Tech Jacket", "category": "Apparel", "price": 219.99, "is_discountable": True
            }),
            Action(name="CreateInventoryRecord", kwargs={"sku": "BOOK-KDSSTY01", "store_id": "STORE-002", "location": "New Arrivals"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "BOOK-KDSSTY01", "store_id": "STORE-003", "location": "New Arrivals"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0026", "quantity_to_add": 50}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0027", "quantity_to_add": 50})
        ],
        outputs=[
            {"promotion_id": "PROMO-008", "name": "UrbanEdge Final Sale"},
            {"sku": "BOOK-KDSSTY01", "name": "UrbanExplorer Tech Jacket"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction="You are a Marketing Director unveiling a new high-tech product, the 'Smart-Mirror'. Since there is no tool available for creating new products, repurpose a discontinued item: 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Modify its record to rename it as 'Smart-Mirror', categorize it under 'Smart Home', price it at 499.99, and make it eligible for discounts. Following that, establish its initial inventory. With a shipment of 100 units just in at the central warehouse ('STORE-001'), create an inventory record for the mirror there in 'Main Warehouse' and update its stock levels. To ensure prompt distribution, immediately allocate 25 units to 'STORE-002' (first establish its inventory record in 'Premium Tech'). To boost sales, target high-value customers first. Begin by obtaining all SKUs from both the 'Electronics' and 'Smart Home' categories. Utilize these lists to identify all 'gold' and 'platinum' customers who have purchased any of these items. For them, create a new 'percentage' promotion named 'Smart-Mirror Launch Offer' with a 20% reduction. The description must be 'An exclusive 20% off our new Smart-Mirror for top customers.' and should remain active for the next 15 days beginning '2025-08-01'. Lastly, create unique, single-use promo codes for all identified customers.",
        actions=[
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "name": "Smart-Mirror", "category": "Smart Home", "price": 499.99, "is_discountable": True}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Main Warehouse"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 100}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002", "location": "Premium Tech"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 25, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Smart Home"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["gold", "platinum"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04", "SMRT-THERM02"]
            }),
            Action(name="CreatePromotion", kwargs={
                "name": "Smart-Mirror Launch Offer", "type": "percentage", "discount_value": 20.0,
                "description": "An exclusive 20% off our new Smart-Mirror for top customers.",
                "applicable_skus": ["CLTH-WINJKT01"],
                "start_date": "2025-08-01", "end_date": "2025-08-15", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"})
        ],
        outputs=[
            {"codes_generated_for": ["CUST-5001", "CUST-5010"]}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction="You are a CRM Manager and have observed that 'Noah Tran' (CUST-5002), a loyal 'silver' member, has qualified for an upgrade. Start by retrieving his customer details by name to verify his current status. Upgrade his membership level to 'gold' immediately and add 250 bonus loyalty points to his account as recognition. To honor his new status, design a targeted 'percentage' promotion just for him. Initially, find all products under the 'Electronics' category. Then, create a promotion named 'New Gold Member Tech Deal' with a 15% discount applicable across all electronics. The promotion's description must state 'A special 15% off electronics to thank you for your loyalty.' and it should remain active for the next 30 days starting from '2025-08-10', with an initial usage count of 0. Ultimately, produce a unique, single-use promo code for Liam and re-access his customer details to confirm his new status and point balance.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Noah Tran"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 250}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "New Gold Member Tech Deal", "type": "percentage", "discount_value": 15.0,
                "description": "A special 15% off electronics to thank you for your loyalty.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-10", "end_date": "2025-09-09", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[{"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1125}]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction="As an Inventory Manager, you need to address the 'Organic Almond Butter 500g' (GROC-ALMBTR500) at 'STORE-001' nearing its expiration. Begin by accessing the product's inventory record to verify its current stock level. To minimize waste, transition all units to clearance status. Change the main product's status to 'clearance'. Next, launch a special 'percentage' promotion titled 'Almond Butter Final Sale' offering a 50% discount. The description should read '50% off! Must go before expiry.' and it needs to be available for 3 days commencing '2025-08-11'. Set the promotion's initial usage count to 0. Once the promotion is established, adjust the inventory item's status at 'STORE-001' to 'critical' to indicate urgency. Finally, review the updated product details and inventory records to validate both status modifications.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "Organic Almond Butter 500g"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "GROC-ALMBTR500", "status": "clearance"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Almond Butter Final Sale", "type": "percentage", "discount_value": 50.0,
                "description": "50% off! Must go before expiry.",
                "applicable_skus": ["GROC-ALMBTR500"],
                "start_date": "2025-08-11", "end_date": "2025-08-13", "status": "active", "times_used": 0
            }),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0007", "status": "critical"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"})
        ],
        outputs=[
            {"sku": "GROC-ALMBTR500", "status": "clearance"},
            {"id": "INV-0007", "status": "critical"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction="As a Marketing Manager, the 'Clearance Apparel Markdown' promotion (PROMO-005) has concluded and requires decommissioning. Initially, access its details using its ID to verify its current status. Proceed to deactivate the promotion. You will then reuse this promotion ID for a new initiative. Modify its details to launch the 'Back to Office Essentials' sale: update the name, set the type as 'percentage' with a 20% discount, and adjust the description to '20% off select office supplies for your return to work.'. The new applicable product is the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01). Before associating the SKU, obtain the product's information and modify it to be 'is_discountable'. Schedule the new promotion for the full month of September 2025. Finally, retrieve the promotion again by its ID 'PROMO-005' to confirm all adjustments.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-005"}),
            Action(name="DeactivatePromotion", kwargs={"promotion_id": "PROMO-005"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": True}),
            Action(name="UpdatePromotionDetails", kwargs={
                "promotion_id": "PROMO-005",
                "name": "Back to Office Essentials",
                "type": "percentage",
                "discount_value": 20.0,
                "description": "20% off select office supplies for your return to work.",
                "applicable_skus": ["OFFC-ERGCHR01"],
                "start_date": "2025-09-01",
                "end_date": "2025-09-30",
                "status": "scheduled"
            }),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-005"})
        ],
        outputs=[{"promotion_id": "PROMO-005", "name": "Back to Office Essentials", "status": "scheduled"}]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction="As 'Zoe Martinez', an Inventory Specialist at 'STORE-004', an audit reveals the 'TrailGuard Mountain Bike Helmet' (SPORT-BIKHLM01) has a reserved quantity of 1 without any actual reservations. Correct this discrepancy. First, access the complete inventory record for this item at your store. Subsequently, update the reserved quantity to 0; the directive states the adjustment amount is -1. With this correction, the available inventory increases. In accordance with store policy, reassess the item's status. Retrieve the item's `safety_stock` level from its inventory record. Since the total stock (4) now exceeds the `safety_stock` (3), update the inventory status from 'low_stock' to 'in_stock'. Finally, access the inventory record anew to ensure all updates are correct.",
        actions=[
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0009", "change_amount": -1}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0009", "status": "in_stock"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"})
        ],
        outputs=[{"id": "INV-0009", "reserved_quantity": 0, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction="As 'Ethan Walker', a sales lead at 'STORE-002', handle a return from customer 'Mia Kim' (CUST-5011) who wishes to return a 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) received as a gift, lacking a receipt but purchased with transaction 'TXN-0011'. The item is in pristine condition. Start by locating the transaction to verify the purchase. Since the original payment method cannot be refunded without the original card, issue the credit as loyalty points as per store policy. Access the product's current price to calculate the point value; policy dictates rounding up any decimal value to the nearest whole number. Update the customer's loyalty points by this amount. Finally, return the item to inventory. Obtain the inventory ID for the knife at your store and adjust its stock level by adding 1 unit. Retrieve the customer's profile to verify her revised loyalty point balance.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Mia Kim"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ProSlice 8\" Chef Knife"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5011", "sku": "KITCH-CHEFKNF8"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 40}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0011", "quantity_to_add": 1}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[{"customer_id": "CUST-5011", "loyalty_points": 600}]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction="As a Marketing Specialist, you have observed that the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02) is incorrectly categorized as 'Smart Home'. It should belong to the 'Electronics' category. To correct this, first, access the product's details to view its current category. Then, modify the product to correctly place it in the 'Electronics' category. To commemorate this correction, promptly initiate a flash sale. Create a 'percentage' promotion titled 'Thermostat Flash Sale' with a 20% discount. The description should read '24-hour flash sale on our EcoSmart Thermostat!' and must be active solely for today, '2025-08-14', with a starting usage count of 0. Lastly, access all promotions with an 'active' status to confirm your new flash sale is included.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "SMRT-THERM02"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "SMRT-THERM02", "category": "Electronics"}
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Thermostat Flash Sale", "type": "percentage", "discount_value": 20.0,
                    "description": "24-hour flash sale on our EcoSmart Thermostat!",
                    "applicable_skus": ["SMRT-THERM02"],
                    "start_date": "2025-08-14", "end_date": "2025-08-14", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="GetPromotionsByStatus",
                kwargs={"status": "active"}
            )
        ],
        outputs=[[
            {"promotion_id": "PROMO-001", "name": "Summer Electronics Sale", "status": "active"},
            {"promotion_id": "PROMO-002", "name": "Kitchen Essentials Bundle", "status": "active"},
            {"promotion_id": "PROMO-005", "name": "Clearance Apparel Markdown", "status": "active"},
            {"promotion_id": "PROMO-006", "name": "Smart Home Starter Discount", "status": "active"},
            {"promotion_id": "PROMO-008", "name": "Thermostat Flash Sale", "status": "active"}
        ]]
    ),
    Task(
        annotator="0",
        user_id="task_051",
        instruction="You are 'Amanda Romano', a sales lead at 'STORE-002'. Customer 'Emma Wilson' wishes to purchase the 'TrailGuard Mountain Bike Helmet' (SPORT-BIKHLM01). Your store currently lacks stock. Begin by confirming this with a review of your local inventory. Then, examine the inventory at 'STORE-004', where stock is presumed available. Notify the customer that the helmet can be transferred. Prior to the transfer, establish an inventory record for the helmet at 'STORE-002', designating 'Store Transfer Area' as the location. After the transfer of 1 unit from 'STORE-004' is completed, update the inventory status at your store to 'in_stock'. Proceed to finalize the sale for Emma Wilson using 'credit_card'. The guideline dictates payment by 'credit_card'. Ensure no promotions are applied. Calculate the total cost, finalize the transaction, and update your store's inventory using today’s date, '2025-08-12', for the last stock count. Return the transaction ID.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "TrailGuard Mountain Bike Helmet"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-002", "location": "Store Transfer Area"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 1, "from_store_id": "STORE-004", "to_store_id": "STORE-002"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Emma Wilson"}),
            Action(name="CalculateTransactionTotals", kwargs={"line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 1}]}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Amanda Romano"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5001", "payment_method": "credit_card",
                "total_amount": 96.34, "tax_amount": 7.34, "discount_total": 0.0,
                "line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 1, "unit_price": 89.0, "discount": 0.0}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-08-12"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction="You are 'Michael Rodriguez', a customer service representative at 'STORE-001'. 'Benjamin Cohen' (CUST-5010) has called regarding transaction 'TXN-0010'. He suspects he was incorrectly charged for his 'WaveSound All-Weather Bluetooth Speaker', believing the price should have been $125.00. Start by locating the transaction using his customer ID and the product SKU to verify the unit_price he actually paid. Once the price is clarified, as a gesture of goodwill, add 100 loyalty points to his account. Additionally, to ensure his satisfaction, set up a new 'percentage' promotion titled 'Electronics Apology' with a 15% discount on all 'Electronics' category products. The description should be 'A 15% discount on our electronics as a token of our apology.' and it should remain active for 90 days commencing today, '2025-08-13', with zero initial usage count. Finally, issue a unique promo code for Mr. Cohen and confirm his new loyalty points balance by retrieving his customer details.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "WaveSound All-Weather Bluetooth Speaker"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5010", "points_to_add": 100}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Electronics Apology", "type": "percentage", "discount_value": 15.0,
                "description": "A 15% discount on our electronics as a token of our apology.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-13", "end_date": "2025-11-11", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "loyalty_points": 1125}]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction="You are a Regional Manager. It has come to your attention that 'STORE-004' is underperforming in the 'Sports & Outdoors' category. To boost sales, determine to transfer the well-liked 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) from 'STORE-001', which has sufficient stock. Initially, validate the stock at 'STORE-001'. Follow by creating a fresh inventory record for the mat at 'STORE-004', in the 'Featured Products Aisle', and move 25 units. Subsequently, to advertise this new stock, target 'platinum' customers who have previously purchased items from the 'Sports & Outdoors' category. Identify these customers. Thereafter, implement a 'percentage' promotion named 'STORE-004 Sports Special' offering a 25% discount on the yoga mat, exclusive to that store. The description must be 'A special offer for our top sports customers at STORE-004.' and it should be operational for the last week of August 2025, with an initial usage count of 0. Finally, generate unique promo codes for the targeted customers.",
        actions=[
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-004", "location": "Featured Products Aisle"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 25, "from_store_id": "STORE-001", "to_store_id": "STORE-004"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="FindCustomersByCriteria", kwargs={"membership_levels": ["platinum"], "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]}),
            Action(name="CreatePromotion", kwargs={
                "name": "STORE-004 Sports Special", "type": "percentage", "discount_value": 25.0,
                "description": "A special offer for our top sports customers at STORE-004.",
                "applicable_skus": ["SPORT-YOGMAT01"],
                "start_date": "2025-08-25", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"})
        ],
        outputs=[{"codes_generated_for": ["CUST-5004"]}]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction="You are 'Amanda Romano', acting as a sales associate at 'STORE-002'. A new customer, 'David Chen', intends to buy the 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) along with an 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Begin by creating a new customer account for him with a 'basic' membership, starting him off with 0 loyalty points, and ensuring marketing opt-out. Then, check the stock availability for both items in your store. Recall there might be a promotion potentially applicable. Verify any 'active' promotions named 'Clearance Apparel Markdown' for today's date, '2025-06-20'. Should it be active, compute the transaction totals, applying the promotion to both items. The customer will complete the transaction via 'debit_card'. Confirm the sale by finalizing the transaction and adjusting the inventory for the sold items.",
        actions=[
            Action(name="CreateCustomer", kwargs={"name": "David Chen", "membership_level": "basic", "opt_in_marketing": False, "loyalty_points": 0}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-20"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "CLTH-SLFJEAN34", "quantity": 1}, {"sku": "CLTH-WINJKT01", "quantity": 1}],
                "promotion_ids": ["PROMO-005"]
            }),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Amanda Romano"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5013", "payment_method": "debit_card",
                "total_amount": 194.04, "tax_amount": 14.79, "discount_total": 59.75,
                "line_items": [
                    {"sku": "CLTH-SLFJEAN34", "quantity": 1, "unit_price": 49.5, "discount": 12.38},
                    {"sku": "CLTH-WINJKT01", "quantity": 1, "unit_price": 189.5, "discount": 47.38}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0005", "quantity_sold": 1, "last_stock_count_date": "2025-06-20"}),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-06-20"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction="You are a Marketing Manager. The 'Kitchen Essentials Bundle' (PROMO-002) concludes today, '2025-07-15'. Your responsibility is to deactivate it and promptly initiate an upgraded version for the forthcoming holiday season. Start by retrieving the promotion using its ID to assess its 'times_used' count. Proceed by deactivating it. Then, craft a new promotion branded 'Kitchen Upgrade Bundle'. This should be a 'fixed_bundle' promotion featuring an enhanced discount of $20.00. The description required is 'Upgrade your kitchen with this premium bundle for the holidays.'. It will incorporate the original items ('HOM-COFMKR12', 'KITCH-CHEFKNF8') plus the 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). Set the new promotion to be 'scheduled' from '2025-11-01' until '2025-12-31', with an initial usage count of 0. Finally, confirm the creation by retrieving the new promotion by its ID.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="DeactivatePromotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ChefPro Ceramic Fry Pan 10\""}),
            Action(name="CreatePromotion", kwargs={
                "name": "Kitchen Upgrade Bundle", "type": "fixed_bundle", "discount_value": 20.0,
                "description": "Upgrade your kitchen with this premium bundle for the holidays.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-11-01", "end_date": "2025-12-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-002", "status": "inactive"}, {"promotion_id": "PROMO-008", "name": "Kitchen Upgrade Bundle"}]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction="Your role is that of a sales lead, 'Michael Rodriguez'. You've successfully persuaded a loyal customer, 'Benjamin Cohen' (CUST-5010), who had previously chosen not to receive marketing, to now opt in. Start by obtaining his customer information to verify his current opt-out standing. Next, modify his profile to switch 'opt_in_marketing' to true. As a gesture of appreciation for his decision to opt in, your manager has permitted you to create a one-time exclusive discount for him. Identify all products within his preferred category, 'Electronics'. Establish a new 'fixed_amount' promotion named 'Ben's Opt-in Reward' featuring a $25.00 deduction on any of these items. The promotion's description should be 'A special thank you for joining our marketing list.' and remain active for 60 days starting '2025-08-16', initiating with a usage count of 0. Lastly, produce a unique promo code for him and obtain his details once again to ensure his opt-in status is updated.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Ben's Opt-in Reward", "type": "fixed_amount", "discount_value": 25.0,
                "description": "A special thank you for joining our marketing list.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-16", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction="As an Inventory Specialist bracing for the holiday season, you will focus on the 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) anticipated as a leading seller. You've observed the stock is distributed between 'STORE-001' (quantity: 45) and 'STORE-003' (where it is not available at the moment). Your aim is to centralize all inventory at the main warehouse, 'STORE-001'. Begin by creating an inventory entry for the lamp at 'STORE-003' in the 'Overstock' location, as it is required for the movement. Proceed to transfer all 15 units from 'STORE-003' to 'STORE-001'. Before initiating the transfer, acquire the inventory records from both the source and destination to determine their IDs. Post-transfer, update the inventory record at 'STORE-003' to 'discontinued' since it will be empty and is unnecessary. In conclusion, retrieve the inventory record for the lamp at 'STORE-001' to verify its increased inventory.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-003", "location": "Overstock"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 15}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOME-DESKLMP01", "quantity": 15, "from_store_id": "STORE-003", "to_store_id": "STORE-001"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "discontinued"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0015", "quantity": 60}]
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction="As a Data Analyst, you've detected a data integrity problem: the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is incorrectly classified under 'Office Supplies' instead of the more appropriate 'Furniture' category. Your job is to rectify this error. First, access the product via its SKU to check its present category. Update the product's category to 'Furniture'. Given that this is a high-value product, the company intends to ensure it qualifies for all major promotions. Retrieve the product's data again to confirm the change in category, and if the 'is_discountable' indicator is set to false, modify it to true. Lastly, as a validation step, search for all products now within the 'Furniture' category to verify the success of your update.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "OFFC-ERGCHR01", "category": "Furniture"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": True}),
            Action(name="GetProductsByCategory", kwargs={"category": "Furniture"})
        ],
        outputs=[{"sku": "OFFC-ERGCHR01", "category": "Furniture", "is_discountable": True}]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction="As the Inventory Manager of 'STORE-003', you are tasked with introducing stock of the sought-after 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), which is currently housed at the main warehouse, 'STORE-001'. Your objective is to set an initial stock level. Start by confirming the product's availability at 'STORE-001' by reviewing the inventory record. Then, create a fresh inventory record for the coffee maker at your location ('STORE-003') situated in 'Aisle 4'. Once the new record is established, orchestrate a transfer of 15 units from 'STORE-001' to your location. Since this is a newly stocked item, you must subsequently change the status of your inventory record from its default to 'in_stock'. Finally, retrieve the newly created inventory record from your location to ensure that 15 units are accounted for and the status is updated correctly.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "location": "Aisle 4"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 15, "from_store_id": "STORE-001", "to_store_id": "STORE-003"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 15, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction="As 'Amanda Romano', serving as a sales associate at 'STORE-002', you have a customer, 'William Zhang', interested in purchasing your full remaining inventory of 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). First, obtain the inventory record for this item at your store to verify the precise quantity available (which is 6). The customer has also opted to elevate his membership level. Change his customer record from 'silver' to 'gold'. Proceed with processing the purchase for all 6 parkas. The payment method must be 'credit_card'. There is an active promotion, 'Clearance Apparel Markdown' (PROMO-005), which needs to be verified for today's date, '2025-06-25'. Compute the total amount factoring in this discount. After completing the transaction, promptly update the inventory status of the parka to 'out_of_stock'. Lastly, confirm the updated membership status of the customer.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "William Zhang"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-25"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6}],
                "promotion_ids": ["PROMO-005"]
            }),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Amanda Romano"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5006", "payment_method": "credit_card",
                "total_amount": 923.10, "tax_amount": 70.35, "discount_total": 284.25,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6, "unit_price": 189.5, "discount": 47.38}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 6, "last_stock_count_date": "2025-06-25"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0022", "status": "out_of_stock"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
        Task(
        annotator="0",
        user_id="task_107",
        instruction="As 'Jennifer Williams', leading customer service, address a call from 'Sophia Singh' (CUST-5003) who needs to update her personal information. Begin by retrieving her existing customer record to confirm her current details. Following verification, update her record to show her new married name, 'Olivia Williams', and her new address, '456 Oak Avenue, Riverside, IL, 62704'. To thank her for keeping her information up-to-date, offer her a special promotion. Considering her purchase history in the 'Grocery' category, generate a new 'percentage' promotion titled 'Valued Customer Grocery Offer' offering a 15% discount on all items in that category. The description should read: 'A 15% discount on groceries for our valued customers.' Activate the promotion ('PROMO-008') for 30 days starting on '2025-07-30' with a starting usage count of 0. Before finalizing the promotion, confirm all grocery items are eligible for discounts. Lastly, create a unique promo code for Olivia and pull her customer details again to ensure everything is updated correctly.",
        actions=[
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5003"}
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={
                    "customer_id": "CUST-5003",
                    "name": "Olivia Williams",
                    "address": "456 Oak Avenue, Riverside, IL, 62704"
                }
            ),
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Grocery"}
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-ALMBTR500"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "GROC-ALMBTR500", "is_discountable": True}
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Valued Customer Grocery Offer",
                    "type": "percentage",
                    "discount_value": 15.0,
                    "description": "A 15% discount on groceries for our valued customers.",
                    "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"],
                    "start_date": "2025-07-30",
                    "end_date": "2025-08-29",
                    "status": "active",
                    "times_used": 0
                }
            ),
            Action(
                name="GenerateAndAssignPromoCodes",
                kwargs={"customer_ids": ["CUST-5003"], "promotion_id": "PROMO-008"}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5003"}
            )
        ],
        outputs=[
            {
                "customer_id": "CUST-5003",
                "name": "Olivia Williams",
                "address": "456 Oak Avenue, Riverside, IL, 62704"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction="You are 'Sarah Anderson' working at 'STORE-001'. On '2025-06-10', the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003) kicks off. A customer named 'Olivia Romano' desires to purchase two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01). Begin by locating the promotion using its ID and change its status from 'scheduled' to 'active'. Next, verify your store's inventory to ensure at least two mats are available. Proceed to process Sophia's purchase using 'mobile_wallet'. Assemble the transaction with the following details: the cost of one mat is $29.99, a $15.00 discount on the second mat applies, bringing the total to $48.71, including a tax of $3.71 and a $15.00 total discount. Complete the transaction, amend the inventory, and increase the promotion's 'times_used' count by one.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="ActivatePromotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "FlexFit Premium Yoga Mat"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Olivia Romano"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Sarah Anderson"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1002", "customer_id": "CUST-5007", "payment_method": "mobile_wallet",
                "total_amount": 48.71, "tax_amount": 3.71, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-06-10"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction="As the Marketing Director, focus on rewarding top customers in the 'Home & Kitchen' category. Start by collecting all products associated with the 'Home & Kitchen' category. Using this product list, identify all 'silver' customers who have purchased any of these items. Award each of these silver-level customers 200 bonus loyalty points for their patronage. To verify the updates, retrieve the full customer profiles for 'Noah Tran' and 'William Zhang' after their points allocation.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["silver"],
                "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
            }),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 200}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "loyalty_points": 1075},
            {"customer_id": "CUST-5006", "loyalty_points": 1180}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction="You are 'Zoe Martinez', the inventory manager. A system audit has revealed discrepancies in the stock for the 'BrewMaster 12-Cup Coffee Maker'. At 'STORE-001', the system indicates 25 units, but a physical count shows only 22. Additionally, a mis-delivered pallet of 15 units was found at 'STORE-003', where this item usually isn't stocked. Your task is to correct these records. First, adjust the stock at 'STORE-001' to match the physical count. Then, create a new inventory entry for the coffee maker at 'STORE-003' located in the 'Receiving Dock' and update its stock to 15. To aid in moving the corrected stock, establish a new 'fixed_bundle' promotion named 'Morning Brew Bundle' which grants a $10.00 discount. The offer should be described as 'A special deal on our coffee maker and granola bars.' and applies when customers purchase both the 'BrewMaster 12-Cup Coffee Maker' and 'High-Protein Granola Bars (12 Pack)'. Schedule this promotion to run throughout October 2025.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "High-Protein Granola Bars (12 Pack)"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -3}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "location": "Receiving Dock"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 15}),
            Action(name="CreatePromotion", kwargs={
                "name": "Morning Brew Bundle", "type": "fixed_bundle", "discount_value": 10.0,
                "description": "A special deal on our coffee maker and granola bars.",
                "applicable_skus": ["HOM-COFMKR12", "GROC-GRNLBR12"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003"})
        ],
        outputs=[
            {"id": "INV-0003", "quantity": 22},
            {"id": "INV-0025", "quantity": 15}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction="As a CRM Manager, your objective is to conduct a campaign to reactivate dormant 'platinum' customers. Target 'Liam Anderson', noting that his last transaction was 'TXN-0004' on 2025-06-05. Begin by retrieving his customer details with his name to verify his status. Alter his status to 'inactive' to designate him as dormant. To encourage his return, create a personalized offer. Identify all products in his preferred category, 'Sports & Outdoors'. Develop a new 'percentage' promotion titled 'Welcome Back, Noah!' offering a 30% discount on all 'Sports & Outdoors' merchandise. The promotion description must be 'A special 30% off just for you, Noah!'. It should be active from '2025-08-20' to '2025-09-04', commencing with a usage count of 0. Generate a unique promo code for Noah. Finally, change his status back to 'active' and check his updated details to confirm the changes.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Liam Anderson"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5004"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5004", "status": "inactive"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Sports & Outdoors"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Welcome Back, Noah!", "type": "percentage", "discount_value": 30.0,
                "description": "A special 30% off just for you, Noah!",
                "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                "start_date": "2025-08-20", "end_date": "2025-09-04", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5004", "status": "active"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[{"customer_id": "CUST-5004", "status": "active"}]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction="As the Inventory Manager, handle the liquidation of products from supplier 'UrbanEdge' (SUP-1003) who is now out of business. Liquidate their products: 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Begin by changing the status of both main product records to 'discontinued'. Next, locate all inventory records for these products, noting they are available at 'STORE-002'. Modify the status of both inventory records to 'clearance'. Promote rapid sales by introducing a single 'percentage' promotion called 'UrbanEdge Final Liquidation' with a 60% discount. Ensure the description reads 'Everything from UrbanEdge must go! 60% off.' and set it active from '2025-08-21' for one week, starting with a usage count of 0. Lastly, verify both inventory records from 'STORE-002' to check their 'clearance' status.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-SLFJEAN34", "status": "discontinued"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "status": "discontinued"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0005", "status": "clearance"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0022", "status": "clearance"}),
            Action(name="CreatePromotion", kwargs={
                "name": "UrbanEdge Final Liquidation", "type": "percentage", "discount_value": 60.0,
                "description": "Everything from UrbanEdge must go! 60% off.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-08-21", "end_date": "2025-08-28", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0005", "status": "clearance"}, {"id": "INV-0022", "status": "clearance"}]
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction="As the Customer Service Lead, respond to 'Noah Tran' (CUST-5002) regarding transaction 'TXN-0002'. He bought a 'BrewMaster 12-Cup Coffee Maker' and a 'ProSlice 8\" Chef Knife', believing the 'Kitchen Essentials Bundle' promotion (PROMO-002) should have applied but was overlooked. Firstly, access the promotion by its ID to validate its discount of $15.00. Then, search for the customer's details via his name. Since past transactions are immutable, compensate him by awarding loyalty points equivalent to the $15.00 discount. Update his loyalty points accordingly. To further compensate, design a new 'fixed_amount' promotion providing $10.00 off his next purchase. Name it 'We're Sorry Discount', describe it as 'A $10 voucher for our error.', and make it valid for 90 days from '2025-08-22', available for all 'Home & Kitchen' category items. Start with a usage count of 0. Finally, issue him a promo code and confirm his updated loyalty point total.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Noah Tran"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 15}),
            Action(name="GetProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="CreatePromotion", kwargs={
                "name": "We're Sorry Discount", "type": "fixed_amount", "discount_value": 10.0,
                "description": "A $10 voucher for our error.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                "start_date": "2025-08-22", "end_date": "2025-11-20", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[{"customer_id": "CUST-5002", "loyalty_points": 890}]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction="As the Marketing Director, organize a tiered 'Buy More, Save More' weekend sale for the 'Apparel' category, active between '2025-09-05' and '2025-09-07'. Develop two distinct promotions. Initially, gather all SKUs for the 'Apparel' category. The first promotion, titled 'Apparel Deal - 15% Off', should offer a 'percentage' reduction of 15.0% with the description 'Buy 2+ apparel items and get 15% off!'. The second, known as 'Apparel Deal - 25% Off', requires a 'percentage' decrease of 25.0%, described as 'Buy 3+ apparel items and get 25% off!'. Apply both promotions to all apparel SKUs, aligning start/end dates with the sale, and initiate them with usage counts of 0. Once created, extract all promotions exhibiting a 'scheduled' status to confirm accurate creation.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Apparel"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Apparel Deal - 15% Off", "type": "percentage", "discount_value": 15.0,
                "description": "Buy 2+ apparel items and get 15% off!",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-05", "end_date": "2025-09-07", "status": "scheduled", "times_used": 0
            }),
            Action(name="CreatePromotion", kwargs={
                "name": "Apparel Deal - 25% Off", "type": "percentage", "discount_value": 25.0,
                "description": "Buy 3+ apparel items and get 25% off!",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-05", "end_date": "2025-09-07", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetPromotionsByStatus", kwargs={"status": "scheduled"})
        ],
        outputs=[[
            {"promotion_id": "PROMO-003", "name": "Buy One Yoga Mat Get 50% Off Second"},
            {"promotion_id": "PROMO-008", "name": "Apparel Deal - 15% Off"},
            {"promotion_id": "PROMO-009", "name": "Apparel Deal - 25% Off"}
        ]]
    ),
    Task(
        annotator="0",
        user_id="task_069",
        instruction="As 'Michael Rodriguez', a senior customer service representative, offer a resolution for 'Noah Tran', a loyal 'silver' customer, concerning transaction 'TXN-0002'. He finds the benefit from the 'Kitchen Essentials Bundle' promotion insufficient. Begin by verifying the customer's existing details and those of the promotion ('PROMO-002'). To appease him, add 150 bonus loyalty points to his account, noticing this upgrades his total over 1000, thus advancing his membership to 'gold'. To honor his new level, create a special 'percentage' promotion called 'Gold Member Welcome Offer' with a 20% discount on all 'Electronics' items. It should state 'A special electronics discount for our new Gold member.' and remain valid for 60 days starting from '2025-08-01'. Lastly, produce a single-use, unique promo code for Liam and reaffirm his details to guarantee his new standing and point total.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Noah Tran"}),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 150}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Gold Member Welcome Offer", "type": "percentage", "discount_value": 20.0,
                "description": "A special electronics discount for our new Gold member.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-01", "end_date": "2025-09-29", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1025}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction="As 'Megan Young', manager of 'STORE-005', conduct clearance operations for the 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02) and update the contact information for 'Benjamin Cohen', a loyal customer. Initially, obtain the speaker's inventory details at 'STORE-005' to check the quantity. Amend the main product's status to 'clearance'. Next, locate 'Benjamin Cohen' by name and modify his address to '22 Mountain View Rd, Portland, OR, 97205' and phone to '+1-555-0999-1111'. To express appreciation, create an exclusive 'fixed_amount' promotion dubbed 'Valued Customer Credit' worth $20.00 off. Its description should be 'A $20 credit for being a loyal customer.' and remain valid for 30 days from '2025-08-27', starting with a usage count of 0 and limited to the speaker. Lastly, issue a unique promo code to him and reaccess his details to confirm the address update.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "WaveSound All-Weather Bluetooth Speaker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "AUDIO-BTSPKR02", "status": "clearance"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="UpdateCustomerDetails", kwargs={
                "customer_id": "CUST-5010",
                "address": "22 Mountain View Rd, Portland, OR, 97205",
                "phone_number": "+1-555-0999-1111"
            }),
            Action(name="CreatePromotion", kwargs={
                "name": "Valued Customer Credit", "type": "fixed_amount", "discount_value": 20.0,
                "description": "A $20 credit for being a loyal customer.",
                "applicable_skus": ["AUDIO-BTSPKR02"],
                "start_date": "2025-08-27", "end_date": "2025-09-26", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "address": "22 Mountain View Rd, Portland, OR, 97205"}]
    ),
    Task(
        annotator="task_071",
        user_id="task_071",
        instruction="As an Inventory Specialist, handle a data discrepancy discovered during an audit of 'STORE-001' for the 'UltraVision 55\" 4K Smart TV' (INV-0001). The system records 8 units in stock with 2 reserved, yet a physical check finds 9 units, and all reservations are void. Adjust two details: First, increase the stock by 1 unit. Second, modify the reserved count to 0; the required change_amount is -2. After these updates, the new available stock is 9. Reassess the inventory status based on policy. Access the inventory record once more to obtain its 'reorder_level' (3) and 'safety_stock' (2). Given the updated quantity of 9 surpasses these levels, change the item's status to 'in_stock'. At last, retrieve the record to ensure all adjustments are accurate.",
        actions=[
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0001", "change_amount": -2}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0001", "status": "in_stock"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0001", "quantity": 9, "reserved_quantity": 0, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="As a Regional Manager, manage the dispersed stock of the 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01), primarily held at 'STORE-001' with a minor portion at 'STORE-004'. Aim to consolidate all stock at 'STORE-001'. Start by verifying the existence of an inventory record at 'STORE-004' in 'Temp Holding' with a total of 10 units. Then, move the entire 10 units from 'STORE-004' to 'STORE-001'. Once the shift is complete, mark the 'STORE-004' inventory record as empty and update its status to 'discontinued'. To drive sales of the newly accumulated stock, formulate a 'percentage' promotion known as 'Yoga Mat Stock-Up Sale' with a 10% reduction. The description should read 'Freshly stocked! Get our premium yoga mats for 10% off.' Ensure the sale runs for the remainder of the month, beginning today '2025-08-26', with an initial usage tally of 0. Lastly, retrieve the 'STORE-001' inventory record to confirm the increased quantity.",
        actions=[
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-004", "location": "Temp Holding"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 10}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 10, "from_store_id": "STORE-004", "to_store_id": "STORE-001"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "discontinued"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Yoga Mat Stock-Up Sale", "type": "percentage", "discount_value": 10.0,
                "description": "Freshly stocked! Get our premium yoga mats for 10% off.",
                "applicable_skus": ["SPORT-YOGMAT01"],
                "start_date": "2025-08-26", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0021", "quantity": 70}]
    ),
    Task(
        annotator="0",
        user_id="task_105",
        instruction="As a manager, 'Megan Young', orchestrate a product recall for 'PowerPlus Rechargeable AA Batteries (4 Pack)'. Start by amending the main product's status to 'recalled'. Thereafter, locate its inventory record at 'STORE-003' and also set its status to 'recalled'. Subsequently, to preemptively address the issue, detach the recalled SKU from all ongoing promotions. Track down the 'Summer Electronics Sale' promotion, active today, '2025-07-29'. Access its details, particularly its current list of valid SKUs. Next, modify the promotion by erasing the SKU ('ELEC-RCHAA04') of the recalled product from its valid list. Lastly, to redress high-value clients, identify all 'gold' tier customers who have previously acquired the recalled item. Award 500 loyalty points to each identified customer and retrieve the updated details for 'Emma Wilson' for verification.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "ELEC-RCHAA04", "status": "recalled"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0020", "status": "recalled"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-07-29"}),
            Action(name="UpdatePromotionDetails", kwargs={
                "promotion_id": "PROMO-001",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15"]
            }),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["gold"],
                "purchase_history_skus": ["ELEC-RCHAA04"]
            }),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 500}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5010", "points_to_add": 500}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[
            {"customer_id": "CUST-5001", "loyalty_points": 1740}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction="As the Inventory Manager for 'STORE-002', you are tasked with starting to stock the 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), presently available at 'STORE-001'. You have a pre-order for 5 units. Establish the inventory and log the pre-order accordingly. Initially, verify the availability of the item at 'STORE-001'. Proceed to create a fresh inventory record for the coffee maker at 'STORE-002', in 'Aisle 12'. Immediately following the creation, adjust the 'reserved_quantity' on this new record by 5 to account for the pre-order. Then, oversee a transfer of 20 units from 'STORE-001' to your store. Conclude by updating the status of your inventory to 'in_stock' and retrieve it to confirm a quantity of 20 and a reserved quantity of 5.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002", "location": "Aisle 12"}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0025", "change_amount": 5}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 20, "reserved_quantity": 5, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction="As an Inventory Auditor for 'STORE-001', you have conducted a physical stock count and uncovEred several discrepancies with system records. For 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), the physical count is 9 units (system: 8). For 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), the physical count shows 22 units (system: 25). For 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01), the count reveals 58 units (system: 60). Your responsibility is to amend the system quantities to align with physical counts, implementing the following modifications: TV (+1), Coffee Maker (-3), and Yoga Mat (-2). First, access the current inventory data for each SKU at 'STORE-001'. Then, apply these corrections. Finally, verify all three inventory updates to ensure final quantities are 9, 22, and 58 respectively.",
        actions=[
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -3}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0021", "quantity_to_add": -2}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
        ],
        outputs=[
            {"id": "INV-0001", "quantity": 9},
            {"id": "INV-0003", "quantity": 22},
            {"id": "INV-0021", "quantity": 58}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_076",
        instruction="As a Customer Service Lead, a 'gold' tier customer, 'Emma Wilson' (CUST-5001), contacts you with a complaint. She recently completed a purchase ('TXN-0001') involving the 'Summer Electronics Sale' promotion ('PROMO-001') but feels the 10% discount did not adequately acknowledge her loyalty. Your mission is to assure her satisfaction. Begin by retrieving her customer information to verify her status. Then, access the promotion details she used to comprehend its conditions. As a sign of goodwill, allocate 200 bonus loyalty points to her account. Additionally, create a unique 'fixed_amount' promotion exclusively for her, titled 'Valued Gold Member Credit', offering $25.00 off any 'Electronics' product. The description should read 'A $25 credit as a thank you for your loyalty.', and it should be valid for 90 days starting today, '2025-09-02', with an initial usage count of 0. Lastly, generate a distinct promo code for her and fetch her customer details once more to verify her updated point balance.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Emma Wilson"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5001"}),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-001"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 200}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Valued Gold Member Credit", "type": "fixed_amount", "discount_value": 25.00,
                "description": "A $25 credit as a thank you for your loyalty.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-09-02", "end_date": "2025-12-01", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5001"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1440}]
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction="As a Regional Manager, you are coordinating the grand opening of a new location, 'STORE-006'. Your responsibility is to establish its initial inventory by reallocating stock from the main warehouse, 'STORE-001'. The necessary items and quantities are: 5 units of 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), 20 units of 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), and 50 units of 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01). For each of these items, first, create a new inventory record at 'STORE-006' in the 'Main Floor' location. Then, perform the transfer of the specified quantities from 'STORE-001'. Conclude by obtaining all three new inventory records from 'STORE-006' to verify the successful inventory setup.",
        actions=[
            Action(name="CreateInventoryRecord", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "ELEC-4KTV55", "quantity": 5, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOME-BTHTWL01", "quantity": 50, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-006"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-006"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-006"}),
        ],
        outputs=[
            {"id": "INV-0025", "quantity": 5},
            {"id": "INV-0026", "quantity": 20},
            {"id": "INV-0027", "quantity": 50}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_078",
        instruction="As a Data Hygiene Specialist, your task is to update several customer accounts from a specified list. Customer 'James O'Connor' has closed his account; change his status to 'inactive'. Similarly, customer 'Logan Smith' has closed his account and needs his status updated to 'inactive'. Additionally, customer 'Ava Martinez' qualifies for a membership upgrade; modify her membership level to 'silver'. Follow the instruction to locate each customer by name to determine their ID before proceeding with the updates. Finally, retrieve the complete records for 'James O'Connor' and 'Ava Martinez' to confirm their statuses have been correctly updated.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "James O'Connor"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5008", "status": "inactive"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Logan Smith"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5012", "status": "inactive"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Ava Martinez"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5005", "membership_level": "silver"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5005"})
        ],
        outputs=[
            {"customer_id": "CUST-5008", "status": "inactive"},
            {"customer_id": "CUST-5005", "membership_level": "silver"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction="Acting as a Product Safety Manager, a recall has been announced for the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02). Start by designating the main product record as 'recalled'. Then, locate the inventory record for this SKU at its stocking store, 'STORE-002', and tag it as 'recalled' as well. Subsequently, identify all customers of diverse membership levels ('gold', 'platinum', 'silver', 'bronze', 'basic') who have purchased this product. The transaction logs reveal that 'CUST-5011' is one such customer. You must verify her contact eligibility. Retrieve the customer record for 'Mia Kim' (CUST-5011) to assess her marketing opt-in preference. If she has opted out, adjust her 'opt_in_marketing' status to true for safety communication purposes. Finally, check her record once again to confirm her contact status is enabled.",
        actions=[
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "SMRT-THERM02", "status": "recalled"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-002"}
            ),
            Action(
                name="UpdateInventoryStatus",
                kwargs={"inventory_id": "INV-0019", "status": "recalled"}
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "purchase_history_skus": ["SMRT-THERM02"],
                    "membership_levels": ["gold", "platinum", "silver", "bronze", "basic"]
                }
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5011"}
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5011", "opt_in_marketing": True}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5011"}
            )
        ],
        outputs=[{"customer_id": "CUST-5011", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction="As a Data Analyst organizing a site-wide sale, it is your responsibility to ensure all products supplied by 'UrbanEdge' are eligible for discounts. The specified products are 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Your assignment involves examining each product to confirm its discountable status and, if necessary, updating it to 'is_discountable: true'. Finally, review the information for both products again to ensure they are now categorized as discountable.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-WINJKT01"}),
        ],
        outputs=[
            {"sku": "CLTH-SLFJEAN34", "is_discountable": True},
            {"sku": "CLTH-WINJKT01", "is_discountable": True}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction="As a Marketing Analyst, arrange an A/B test by developing two distinct promotions for identical products to evaluate their effectiveness. The products in focus belong to the 'Grocery' category. Start by obtaining the list of grocery SKUs. Promotion A is titled 'Grocery Discount 10%' and should offer a 'percentage' discount of 10.0, with the description 'Test A: 10% off all grocery items.' Promotion B, named 'Grocery Discount $5 Off', must provide a 'fixed_amount' discount of 5.00, described as 'Test B: $5 off your grocery purchase.' Ensure both promotions are 'scheduled' for the same timeframe, from '2025-10-01' to '2025-10-31', starting with a usage count of 0. Once both promotions are created, access all promotions marked 'scheduled' to confirm their readiness.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Grocery"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Grocery Discount 10%", "type": "percentage", "discount_value": 10.0,
                "description": "Test A: 10% off all grocery items.",
                "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="CreatePromotion", kwargs={
                "name": "Grocery Discount $5 Off", "type": "fixed_amount", "discount_value": 5.00,
                "description": "Test B: $5 off your grocery purchase.",
                "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetPromotionsByStatus", kwargs={"status": "scheduled"})
        ],
        outputs=[{"created_promotions": ["PROMO-008", "PROMO-009"]}]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction="While working as a CRM Specialist, aim to motivate customers who have purchased 'Smart Home' devices to broaden their setup. Begin by locating all 'silver' tier clients who bought the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02). For the specific customer, 'Mia Kim' (CUST-5011), design a tailor-made offer. Gather every SKU available in the 'Smart Home' category. Launch a new 'percentage' promotion called 'Smart Home Expansion', granting 15% off on all 'Smart Home' merchandise. The promotion must state, 'Expand your smart home with 15% off.' This offer must remain active for a month commencing on '2025-09-15', with an initial usage count of 0. Formulate a unique promo code for Mia and verify her customer details.",
        actions=[
            Action(name="FindCustomersByCriteria", kwargs={"membership_levels": ["silver"], "purchase_history_skus": ["SMRT-THERM02"]}),
            Action(name="GetProductsByCategory", kwargs={"category": "Smart Home"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Smart Home Expansion", "type": "percentage", "discount_value": 15.0,
                "description": "Expand your smart home with 15% off.",
                "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-09-15", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5011"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[{"customer_id": "CUST-5011"}]
    ),
    Task(
        annotator="0",
        user_id="task_083",
        instruction="You are 'Megan Young', the Store Manager at 'STORE-005'. Customer 'Benjamin Cohen' (CUST-5010) has contacted you about transaction 'TXN-0010' from '2025-06-05'. The transaction includes a mistaken discount application. It lists a 40.0 discount on the 'WaveSound All-Weather Bluetooth Speaker', which should have been derived from the 'Summer Electronics Sale' (PROMO-001), applying 10%. First, locate the transaction and associated promotion details. Discover that the speaker is not eligible for that promo and the discount was an error. Since altering the transaction is not possible, offer compensation by adding loyalty points equal to the speaker's price. Retrieve the speaker's SKU and current price ($129.99). Then, locate the customer by name. As the instructions dictate, round the price to the nearest whole number, resulting in 130 points, and add these to his account. Lastly, adjust the 'Smart Home Starter Discount' (PROMO-006) to include the SKU 'AUDIO-BTSPKR02' for future eligibility to avoid similar errors.",
        actions=[
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-06-05"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5010", "points_to_add": 130}),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-006"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-006", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "loyalty_points": 1155}, {"promotion_id": "PROMO-006", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]}]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction="You are the Marketing Director starting a multi-phase strategy to upsell 'Smart Home' products to 'Electronics' loyalists. PHASE 1: Begin by pinpointing the target customers. Gather all product SKUs listed under the 'Electronics' category. Identify all 'gold' tier clients who have acquired any of these electronic products. The resulting customer IDs list includes 'CUST-5001' and 'CUST-5010'. PHASE 2: Create the promotion next. Collect all product SKUs within the 'Smart Home' category. Roll out a 'percentage' promotion named 'Smart Home Upgrade Offer', offering a 25% cut on all 'Smart Home' products. The description should express 'A special 25% off to expand your smart ecosystem.' and it is to be valid throughout October 2025, starting with a zero usage count. PHASE 3: Disseminate the offer. Formulate unique promo codes for the clients identified in Phase 1. In addition, promptly allocate 100 loyalty points to each of their accounts. PHASE 4: Verify the accuracy of your actions by reviewing the customer information for 'Emma Wilson' to ascertain her updated points balance.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["gold"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]
            }),
            Action(name="GetProductsByCategory", kwargs={"category": "Smart Home"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Smart Home Upgrade Offer", "type": "percentage", "discount_value": 25.0,
                "description": "A special 25% off to expand your smart ecosystem.",
                "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5001", "points_to_add": 100}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5010", "points_to_add": 100}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Emma Wilson"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1340}]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction="Conduct a data integrity audit as a Data Analyst. Identify and rectify errors concerning the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) and its associated promotion, 'Summer Electronics Sale' (PROMO-001). Start by acquiring the TV's details; correct the price to $749.99 and set its status to 'premium'. Reflect these updates in the product's record. Proceed to retrieve the promotion by ID, increase its discount rate to 15.0%, and add 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01) to its applicable SKU list. Adjust the promotion with these modifications. For assessing the financial impact, locate customer 'Emma Wilson', who bought the TV under transaction 'TXN-0001'. The instruction involves recomputing the totals for her initial purchase (1 TV and 2 'PowerPlus Rechargeable AA Batteries (4 Pack)') by applying the revised TV price and the new 15% discount, then presenting the recalculated total amount.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "ELEC-4KTV55", "price": 749.99, "status": "premium"}),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-001"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "QuietTone Wireless Earbuds"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-001", "discount_value": 15.0, "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "ELEC-RCHAA04", "AUDIO-NCEBUDS01"]}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Emma Wilson"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}),
            Action(name="CalculateTransactionTotals", kwargs={
                "line_items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "ELEC-RCHAA04", "quantity": 2}],
                "promotion_ids": ["PROMO-001"]
            })
        ],
        outputs=[{"recalculated_total_amount": 724.96}]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction="As an Inventory Manager at 'STORE-001' on '2025-11-01', handle the 'Organic Almond Butter 500g' (GROC-ALMBTR500), which has an expiration date of '2026-04-15'. The policy necessitates a clearance sale if expiry is within 6 months. Begin by retrieving the core product details to confirm the expiry date. Follow by obtaining its inventory record at your location. Since the policy criteria are fulfilled, adjust the main product's status to 'clearance'. As the item generally cannot be discounted, initially adjust its record to make 'is_discountable' true. Subsequently, generate a 'percentage' promotion named 'Expiry Clearance' with a 75% reduction. Ensure the description reads 'Urgent Sale: 75% off Almond Butter before it expires!'. This promotion should be live from today up until the day before its expiration, '2026-04-14', starting with a usage count of 0. Finally, pinpoint all 'bronze' tier customers who have purchased grocery items historically, as they are the targets for this sale. The list of grocery SKUs is 'GROC-ALMBTR500', 'GROC-GRNLBR12', and 'GROC-SPRWAT6P'.",
        actions=[
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "GROC-ALMBTR500"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "GROC-ALMBTR500", "status": "clearance"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "GROC-ALMBTR500", "is_discountable": True}
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Expiry Clearance", "type": "percentage", "discount_value": 75.0,
                    "description": "Urgent Sale: 75% off Almond Butter before it expires!",
                    "applicable_skus": ["GROC-ALMBTR500"],
                    "start_date": "2025-11-01", "end_date": "2026-04-14", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["bronze"],
                    "purchase_history_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"]
                }
            )
        ],
        outputs=[{"found_customers": [{"customer_id": "CUST-5003"}]}]
    ),
    Task(
        annotator="0",
        user_id="task_087",
        instruction="Your role as 'Robert Zhang', the sales lead at 'STORE-002', involves assisting new customer 'Eleanor Vance' with her initial purchase. She is interested in the 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) and 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01). Start by setting up a new 'basic' customer profile for her with 0 loyalty points and marketing opt-in confirmed. Check the stock of both items at 'STORE-002'. To warmly welcome her, you will set up a new 'percentage' promotion labeled 'New Customer Welcome' with a 10% deduction. The description should be 'A 10% welcome discount for our new customers.' This promotion is valid for today only, '2025-08-29', initiating with a usage of 0, and is applicable to both products. Construct the final transaction utilizing these pre-set values: a total discount of $33.95, a tax component of $25.13, and a grand total of $339.67. Conclude the sale using 'credit_card'. To wrap up, modify the stock for both products and boost the new promotion's 'times_used' count.",
        actions=[
            Action(
                name="CreateCustomer",
                kwargs={"name": "Eleanor Vance", "membership_level": "basic", "opt_in_marketing": True, "loyalty_points": 0}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002"}
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "CLTH-WINJKT01"}
            ),
            Action(
                name="GetProductDetailsBySku",
                kwargs={"sku": "AUDIO-NCEBUDS01"}
            ),
            Action(
                name="UpdateProductDetails",
                kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "New Customer Welcome", "type": "percentage", "discount_value": 10.0,
                    "description": "A 10% welcome discount for our new customers.", "applicable_skus": ["CLTH-WINJKT01", "AUDIO-NCEBUDS01"],
                    "start_date": "2025-08-29", "end_date": "2025-08-29", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Robert Zhang"}
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-002", "employee_id": "EMP-1008", "customer_id": "CUST-5013", "payment_method": "credit_card",
                    "total_amount": 339.67, "tax_amount": 25.13, "discount_total": 33.95,
                    "line_items": [
                        {"sku": "CLTH-WINJKT01", "quantity": 1, "unit_price": 189.50, "discount": 18.95},
                        {"sku": "AUDIO-NCEBUDS01", "quantity": 1, "unit_price": 149.99, "discount": 15.00}
                    ]
                }
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-08-29"}
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0016", "quantity_sold": 1, "last_stock_count_date": "2025-08-29"}
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-008", "times_used": 1}
            )
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_106",
        instruction="In your capacity as 'Amanda Romano', a sales representative at 'STORE-002', assist high-profile client 'Arthur Pendragon' who plans to buy a 'GigaPlay 15\" Gaming Laptop' and an 'ErgoPro Adjustable Office Chair'. Commence by creating a customer account for him with a 'silver' tier, an initial load of 100 loyalty points, and marketing opt-in. Investigate the stock levels for both products. The laptop is available at your location ('STORE-002'), but the chair is located only at 'STORE-003'. Upon the customer's confirmation to proceed with a transfer, you are authorized to initiate a special promotion to secure the purchase. Develop a new 'percentage' promotion dubbed 'Manager's Special' offering a 10% reduction. The description must read 'A special one-time discount for a valued new customer.' It should apply to both items, being active only today, '2025-07-29', launching with an initial usage count of 0. Create a stock record for the chair at your shop ('STORE-002') under 'Customer Holds' and carry out the transfer of one unit from 'STORE-003'. Finalize the entire purchase for Mr. Pendragon via 'credit_card', applying the freshly minted promotion, and refresh the stock entries for all involved items.",
        actions=[
            Action(
                name="CreateCustomer",
                kwargs={"name": "Arthur Pendragon", "membership_level": "silver", "loyalty_points": 100, "opt_in_marketing": True}
            ),
            Action(
                name="GetProductSkuByName",
                kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}
            ),
            Action(
                name="GetProductSkuByName",
                kwargs={"product_name": "ErgoPro Adjustable Office Chair"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Manager's Special", "type": "percentage", "discount_value": 10.0,
                    "description": "A special one-time discount for a valued new customer.",
                    "applicable_skus": ["ELEC-GAMLP15", "OFFC-ERGCHR01"],
                    "start_date": "2025-07-29", "end_date": "2025-07-29", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-002", "location": "Customer Holds"}
            ),
            Action(
                name="ExecuteInventoryTransfer",
                kwargs={"sku": "OFFC-ERGCHR01", "quantity": 1, "from_store_id": "STORE-003", "to_store_id": "STORE-002"}
            ),
            Action(
                name="GetEmployeeIdByName",
                kwargs={"employee_name": "Amanda Romano"}
            ),
            Action(
                name="CreateTransaction",
                kwargs={
                    "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5013", "payment_method": "credit_card",
                    "total_amount": 1684.47, "tax_amount": 128.38, "discount_total": 172.90,
                    "line_items": [
                        {"sku": "ELEC-GAMLP15", "quantity": 1, "unit_price": 1499.0, "discount": 149.90},
                        {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 23.00}
                    ]
                }
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0013", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}
            ),
            Action(
                name="UpdateInventorySale",
                kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}
            )
        ],
        outputs=[
            {"transaction_id": "TXN-0013"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_089",
        instruction="As the Inventory Manager for 'STORE-002', you are tasked with managing a special order for 10 'BrewMaster 12-Cup Coffee Makers' (HOM-COFMKR12), an item not currently stocked by your store. Begin by verifying that 'STORE-001' has a minimum of 10 units available. Next, establish a new inventory record for the coffee maker at your outlet ('STORE-002') in the 'Special Order Shelf' location. Directly after creating the record, adjust its 'reserved_quantity' by 10 to reflect the special order. Execute the transfer of 10 units from 'STORE-001' to your store. Conclusively, modify the status of your new inventory record to 'in_stock' and confirm the quantity and reservation accuracy by retrieving it. All updates are dated '2025-08-28'.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002", "location": "Special Order Shelf"}),
            Action(name="UpdateInventoryReservedQuantity", kwargs={"inventory_id": "INV-0025", "change_amount": 10}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 10, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 10, "reserved_quantity": 10, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction="You serve as a Marketing Manager. The 'Kitchen Essentials Bundle' (PROMO-002) concludes today, '2025-07-15'. Your responsibility is to inactivate it and promptly introduce an enhanced version for the forthcoming holiday season. Begin by retrieving the promotion using its ID to verify its 'times_used' count. Proceed to deactivate it. Next, construct a new promotion titled 'Kitchen Upgrade Bundle'. This is to be a 'fixed_bundle' promotion with a raised discount value of $20.00. The description must state 'Upgrade your kitchen with this premium bundle for the holidays.'. It will encompass the original items ('HOM-COFMKR12', 'KITCH-CHEFKNF8') and add the 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). Schedule this new promotion to be active from '2025-11-01' to '2025-12-31', beginning with a usage count of 0. Ultimately, retrieve the new promotion by its ID to verify its establishment.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="DeactivatePromotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ChefPro Ceramic Fry Pan 10\""}),
            Action(name="CreatePromotion", kwargs={
                "name": "Kitchen Upgrade Bundle", "type": "fixed_bundle", "discount_value": 20.0,
                "description": "Upgrade your kitchen with this premium bundle for the holidays.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-11-01", "end_date": "2025-12-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-002", "status": "inactive"}, {"promotion_id": "PROMO-008", "name": "Kitchen Upgrade Bundle"}]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction="As 'Amanda Romano', a sales associate at 'STORE-002', you need to assist 'William Zhang', who is interested in purchasing your complete stock of the 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Initially, access the inventory record for this parka at your location to verify the current quantity on hand (which is 6). The customer also wishes to enhance his membership. Modify his customer record from 'silver' to 'gold'. Subsequently, manage the sale for all 6 parkas. The accepted payment method is 'credit_card'. Verify the presence of an active 'Clearance Apparel Markdown' promotion (PROMO-005) applicable on '2025-06-25'. Compile the final transaction with these already calculated details: the price of each parka is $189.50, with a $47.38 discount on each. The overall total_amount stands at $923.10, tax_amount at $70.35, and discount_total at $284.25. Once the transaction is complete with these exact totals, update the parka's inventory status to 'out_of_stock'. Lastly, verify the customer's upgraded membership status.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "William Zhang"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-25"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Amanda Romano"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5006", "payment_method": "credit_card",
                "total_amount": 923.10, "tax_amount": 70.35, "discount_total": 284.25,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6, "unit_price": 189.5, "discount": 47.38}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 6, "last_stock_count_date": "2025-06-25"}),
            Action(name="UpdateInventoryStatus", kwargs={"inventory_id": "INV-0022", "status": "out_of_stock"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction="As a customer service representative, facilitate the return process for 'William Zhang' (CUST-5006) at 'STORE-002', who wishes to return an 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) from transaction 'TXN-0006'. The chair is in excellent condition. The return involves the original price of $229.99. The inventory for this chair is maintained at 'STORE-003', so you need to handle the return by identifying the correct inventory record ('INV-0014') and adding 1 unit back into its stock. The customer intends to apply this credit towards purchasing two 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) from 'STORE-002'. Verify the jeans' stock, ascertain their price, then complete the new purchase transaction using the full credit of $229.99. The remaining balance will be credited to his 'debit_card', leading to a final transaction total of -$122.82 and a tax amount of $8.17. The sales associate involved is 'Ethan Walker', and inventory updates should be done by '2025-08-15'.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "William Zhang"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="UpdateStockLevel", kwargs={"inventory_id": "INV-0014", "quantity_to_add": 1}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Ethan Walker"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1011", "customer_id": "CUST-5006", "payment_method": "debit_card",
                "total_amount": -122.82, "tax_amount": 8.17, "discount_total": 0.0,
                "line_items": [{"sku": "CLTH-SLFJEAN34", "quantity": 2, "unit_price": 49.5, "discount": 0.0}]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0005", "quantity_sold": 2, "last_stock_count_date": "2025-08-15"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction="In your role as a sales lead, 'Michael Rodriguez', you've persuaded a long-term customer, 'Benjamin Cohen' (CUST-5010), who previously rejected marketing, to opt in. Begin by accessing his customer information to verify his present opt-out status. Then, adjust his record to mark 'opt_in_marketing' as true. To thank him for joining, your manager permits you to set up a special one-time discount. Identify all items within his preferred category, 'Electronics'. Initiate a new 'fixed_amount' promotion titled 'Ben's Opt-in Reward' that grants a $25.00 discount on any of these electronic products. The description should be 'A special thank you for joining our marketing list.' and it is valid for 60 days starting '2025-08-16', with an initial usage count of 0. Conclude by creating a unique promo code for him and confirm his opt-in status by reviewing his details again.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True}),
            Action(name="GetProductsByCategory", kwargs={"category": "Electronics"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Ben's Opt-in Reward", "type": "fixed_amount", "discount_value": 25.0,
                "description": "A special thank you for joining our marketing list.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-16", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="GenerateAndAssignPromoCodes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction="As you prepare for the holiday season in your role as an Inventory Specialist, the 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) is anticipated to be a bestseller, but all stock is at 'STORE-001'. Your task involves redistributing it. First, establish a new inventory record for the lamp at 'STORE-003' under 'Holiday Gifts'. Then, transfer 20 units from 'STORE-001' to 'STORE-003'. You must retrieve the inventory records at both the source and destination before proceeding, to obtain their IDs. Following the transfer, the stock at 'STORE-001' should decrease. Based on the new policy, initiate a 'percentage' promotion at the original store to clear the remaining lamps. Name it 'Pre-Holiday Lamp Sale', offering a 10% discount, with the description '10% off lamps before our holiday shipment!', active on '2025-08-29', with a usage count of 0.",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-003", "location": "Holiday Gifts"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "HOME-DESKLMP01", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-003"}),
            Action(name="CreatePromotion", kwargs={
                "name": "Pre-Holiday Lamp Sale", "type": "percentage", "discount_value": 10.0,
                "description": "10% off lamps before our holiday shipment!",
                "applicable_skus": ["HOME-DESKLMP01"],
                "start_date": "2025-08-29", "end_date": "2025-08-29", "status": "active", "times_used": 0
            }),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0015", "quantity": 25}]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction="You are 'Sarah Anderson' at 'STORE-001'. It is '2025-06-10', marking the commencement of the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003). A customer, 'Olivia Romano', aims to purchase two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01). Begin by retrieving the promotion via its ID and alter its status from 'scheduled' to 'active'. Next, verify the mat's availability at your store, ensuring at least two in stock. Proceed with managing Sophia's purchase. The specified payment method is 'mobile_wallet'. Composition of the final transaction must mirror these pre-set figures: each mat costs $29.99, the 50% discount on the second mat is $15.00, culminating in a total amount of $48.71, with tax at $3.71 and a total discount of $15.00. Execute the transaction, adjust the inventory for the two mats sold, and increment the promotion's 'times_used' by one.",
        actions=[
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="ActivatePromotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "FlexFit Premium Yoga Mat"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Olivia Romano"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Sarah Anderson"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1002", "customer_id": "CUST-5007", "payment_method": "mobile_wallet",
                "total_amount": 48.71, "tax_amount": 3.71, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-06-10"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction="As a Data Analyst, address the data integrity issue where the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is mistakenly categorized under 'Office Supplies' instead of the more appropriate 'Furniture' category. Start by locating the product via its SKU to check its current categorization. Update its category to 'Furniture'. This high-value item needs to be included in all major sales, so verify the category change by retrieving the product details again. Since the 'is_discountable' flag is set to true, amend it to false according to new company policy for high-value furniture. Lastly, compile a list of all items now categorized under 'Furniture' to ensure the update's success.",
        actions=[
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "OFFC-ERGCHR01", "category": "Furniture"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="UpdateProductDetails", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": False}),
            Action(name="GetProductsByCategory", kwargs={"category": "Furniture"})
        ],
        outputs=[{"sku": "OFFC-ERGCHR01", "category": "Furniture", "is_discountable": False}]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction="As the Marketing Director, aim to acknowledge top customers in the 'Home & Kitchen' category. Begin by gathering all products from this category. With this list, pinpoint all 'silver' customers who purchased these products. For each silver-level customer found (CUST-5002, CUST-5006, CUST-5009, CUST-5011), award them with 200 bonus loyalty points for their patronage. Verify the updates by accessing the complete customer profiles of 'Noah Tran' and 'William Zhang' post-points addition and note their updated loyalty point balances.",
        actions=[
            Action(name="GetProductsByCategory", kwargs={"category": "Home & Kitchen"}),
            Action(name="FindCustomersByCriteria", kwargs={
                "membership_levels": ["silver"],
                "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
            }),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5009", "points_to_add": 200}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5011", "points_to_add": 200}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5002"}),
            Action(name="GetCustomerDetailsById", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "loyalty_points": 1075},
            {"customer_id": "CUST-5006", "loyalty_points": 1180}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction="Being 'Robert Zhang', the manager of 'STORE-002', handle a full return from customer 'William Zhang' (CUST-5006) for transaction 'TXN-0006'. This return consists of one 'ErgoPro Adjustable Office Chair' and one 'LumiLux LED Desk Lamp', initially purchased at $229.99 and $34.99 respectively. First, locate the inventory IDs for these items at 'STORE-003' and 'STORE-001'. Process the return using the specified purchase prices, ensuring the items are restocked correctly. Since the entire transaction is being returned, adjust the usage count of an involved promotion. Access the 'Clearance Apparel Markdown' promotion by its name for the date '2025-06-20', and decrement its 'times_used' count from 87 to 86. Then, confirm the alteration by retrieving the promotion details using its ID ('PROMO-005').",
        actions=[
            Action(name="GetProductSkuByName", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0006", "sku": "OFFC-ERGCHR01", "quantity_returned": 1, "unit_price": 229.99}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0006", "sku": "HOME-DESKLMP01", "quantity_returned": 1, "unit_price": 34.99}),
            Action(name="GetPromotionByNameAndDate", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-20"}),
            Action(name="UpdatePromotionDetails", kwargs={"promotion_id": "PROMO-005", "times_used": 86}),
            Action(name="GetPromotionById", kwargs={"promotion_id": "PROMO-005"})
        ],
        outputs=[{"promotion_id": "PROMO-005", "times_used": 86}]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction="As 'Jennifer Williams', a lead in customer service at 'STORE-001', attend to 'Ava Martinez' and her intricate request. She intends to return a 'GigaPlay 15\" Gaming Laptop' from her prior transaction (TXN-0005). Though the laptop is flawless, it's unavailable at your location. Execute the return and promptly establish a new inventory record for the laptop in the 'Service Returns' section, subsequently transferring it to 'STORE-002', the primary hub for electronics. She desires to apply her return credit towards purchasing an 'ErgoPro Adjustable Office Chair' from 'STORE-003' and a 'LumiLux LED Desk Lamp' from your store's stock. To acknowledge her patience, credit her account with 100 bonus loyalty points and upgrade her status to 'silver'. Conclude by processing the new purchase, redeeming the full return credit, and refunding the remainder to her 'credit_card'.",
        actions=[
            Action(name="GetCustomerIdByName", kwargs={"customer_name": "Ava Martinez"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}),
            Action(name="FindTransactionByCustomerAndSku", kwargs={"customer_id": "CUST-5005", "sku": "ELEC-GAMLP15"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="ProcessItemReturn", kwargs={"transaction_id": "TXN-0005", "sku": "ELEC-GAMLP15", "quantity_returned": 1, "unit_price": 1499.0}),
            Action(name="CreateInventoryRecord", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-001", "location": "Service Returns"}),
            Action(name="ExecuteInventoryTransfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="GetProductSkuByName", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="GetProductDetailsBySku", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="GetInventoryItemBySkuAndStore", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="GetEmployeeIdByName", kwargs={"employee_name": "Jennifer Williams"}),
            Action(name="CreateTransaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1004", "customer_id": "CUST-5005", "payment_method": "credit_card",
                "total_amount": -1212.16, "tax_amount": 21.86, "discount_total": 0.0,
                "line_items": [
                    {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 0.0},
                    {"sku": "HOME-DESKLMP01", "quantity": 1, "unit_price": 34.99, "discount": 0.0}
                ]
            }),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0014", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateInventorySale", kwargs={"inventory_id": "INV-0015", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="UpdateCustomerLoyaltyPoints", kwargs={"customer_id": "CUST-5005", "points_to_add": 100}),
            Action(name="UpdateCustomerDetails", kwargs={"customer_id": "CUST-5005", "membership_level": "silver"})
        ],
        outputs=[{"customer_id": "CUST-5005", "membership_level": "silver", "loyalty_points": 395}]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction="Leading a targeted campaign as the Marketing Director, implement 'Operation Knife Edge' with the intent to centralize all 'ProSlice 8\" Chef Knife' stock at the main warehouse ('STORE-001') for an exclusive flash sale. Initiate by reallocating all knife units from 'STORE-002' to 'STORE-001', ensuring a destination inventory record exists in 'Online Fulfillment'. Define your target demographic as all 'silver' tier customers who previously bought from 'Home & Kitchen'. Develop a 'fixed_amount' promotion dubbed 'Knife Edge Flash Sale', offering a $15 discount on the 'ProSlice 8\" Chef Knife'. The promotion should bear the description, 'A special flash sale for our loyal kitchen enthusiasts.' and remain active from '2025-07-29' to '2025-07-31'. Post-promotion creation, generate unique, one-time use promo codes for eligible customers. Update the promotion to necessitate a code for redemption. Lastly, elevate all targeted customers ('Noah Tran' and 'Mia Kim') to 'gold' membership status and confirm their updated profiles.",
        actions=[
            Action(
                name="GetProductSkuByName",
                kwargs={"product_name": "ProSlice 8\" Chef Knife"}
            ),
            Action(
                name="GetInventoryItemBySkuAndStore",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}
            ),
            Action(
                name="CreateInventoryRecord",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-001", "location": "Online Fulfillment"}
            ),
            Action(
                name="ExecuteInventoryTransfer",
                kwargs={"sku": "KITCH-CHEFKNF8", "quantity": 35, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}
            ),
            Action(
                name="GetProductsByCategory",
                kwargs={"category": "Home & Kitchen"}
            ),
            Action(
                name="FindCustomersByCriteria",
                kwargs={
                    "membership_levels": ["silver"],
                    "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
                }
            ),
            Action(
                name="CreatePromotion",
                kwargs={
                    "name": "Knife Edge Flash Sale", "type": "fixed_amount", "discount_value": 15.0,
                    "description": "A special flash sale for our loyal kitchen enthusiasts.",
                    "applicable_skus": ["KITCH-CHEFKNF8"],
                    "start_date": "2025-07-29", "end_date": "2025-07-31", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="GenerateAndAssignPromoCodes",
                kwargs={"customer_ids": ["CUST-5002", "CUST-5011", "CUST-5009", "CUST-5006"], "promotion_id": "PROMO-008"}
            ),
            Action(
                name="UpdatePromotionDetails",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True}
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}
            ),
            Action(
                name="UpdateCustomerDetails",
                kwargs={"customer_id": "CUST-5011", "membership_level": "gold"}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5002"}
            ),
            Action(
                name="GetCustomerDetailsById",
                kwargs={"customer_id": "CUST-5011"}
            )
        ],
        outputs=[
            {"customer_id": "CUST-5002", "membership_level": "gold"},
            {"customer_id": "CUST-5011", "membership_level": "gold"}
        ]
    )
]
