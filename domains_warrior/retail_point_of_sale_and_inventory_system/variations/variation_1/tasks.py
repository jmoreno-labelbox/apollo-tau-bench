from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="0",
        user_id="task_001",
        instruction="You are a marketing manager. The 'Summer Electronics Sale' (PROMO-001) is planned to start today, '2025-06-01'. Activate this promotion. Then, retrieve all active promotions, confirm 'UltraVision 55\" 4K Smart TV' (SKU: ELEC-4KTV55) is included, and get its current stock at 'STORE-001'. Finally, update the 'times_used' count for PROMO-001 to 10 to reflect initial usage tracking.",
        actions=[
            Action(
                name="activate_promotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="get_promotions_by_status",
                kwargs={"status": "active"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="update_promotion_details",
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
        instruction="You are a marketing manager. Deactivate the 'Clearance Apparel Markdown' promotion (PROMO-005) because its end date '2025-06-30' is approaching and the remaining stock for affected products, 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) at 'STORE-002' and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) at 'STORE-002', is low. After deactivating, verify its status by listing all inactive promotions, then get the current stock status for both apparel items at 'STORE-002'. Finally, update the 'status' of 'Men's Slim Fit Jeans - 34W 32L' to 'clearance' in the product database to reflect its end-of-life cycle. The current date is '2025-06-28'.",
        actions=[
            Action(
                name="deactivate_promotion",
                kwargs={"promotion_id": "PROMO-005"},
            ),
            Action(
                name="get_promotions_by_status",
                kwargs={"status": "inactive"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"},
            ),
            Action(
                name="update_product_details",
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
        instruction="You are a marketing manager. Extend the 'Summer Electronics Sale' (PROMO-001) until '2025-09-30' due to high demand. After this, verify the new end date by retrieving the promotion details. Then, get all products associated with this promotion to confirm their SKUs.",
        actions=[
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-001", "end_date": "2025-09-30"},
            ),
            Action(
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-GAMLP15"},
            ),
            Action(
                name="get_product_details_by_sku",
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
        instruction="You are a marketing manager. We've decided to replace the 'Tax-Free Books Weekend' (PROMO-004) with a new 'Summer Reading Discount' that offers 15% off 'Adventures in Sillytown' (BOOK-KDSSTY01) from '2025-08-10' to '2025-08-20'. First, deactivate the old promotion (PROMO-004). Then, update the details of PROMO-004 to become the 'Summer Reading Discount', ensuring its `name`, `type`, `discount_value`, `description` ('15% off select children''s books for summer reading.'), `applicable_skus` (['BOOK-KDSSTY01']), `start_date`, `end_date`, and `status` are all set. Retrieve the details of the product 'Adventures in Sillytown' to confirm its `is_discountable` status. If it's not discountable, update its `is_discountable` status to `True`. Finally, get the details of the new 'Summer Reading Discount' promotion to confirm all changes. The current date is '2025-08-05'.",
        actions=[
            Action(
                name="deactivate_promotion",
                kwargs={"promotion_id": "PROMO-004"},
            ),
            Action(
                name="update_promotion_details",
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
                name="get_product_details_by_sku",
                kwargs={"sku": "BOOK-KDSSTY01"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "BOOK-KDSSTY01", "is_discountable": True},
            ),
            Action(
                name="get_promotion_by_id",
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
        instruction="You are a marketing manager. The 'Smart Home Starter Discount' (PROMO-006) was recently updated to include 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02). Verify if 'WaveSound All-Weather Bluetooth Speaker' is now part of its applicable SKUs. Also, check the current status and end date of this promotion. If the promotion's 'usage_limit' is null, update it to 100. Then, update the promotion's 'end_date' to '2025-09-15' to extend its duration. The current date is '2025-07-01'.",
        actions=[
            Action(
                name="get_promotion_by_name_and_date",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-01"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-006", "usage_limit": 100, "end_date": "2025-09-15", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]},
            ),
            Action(
                name="get_promotion_by_id",
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
        instruction="You are a sales associate and your name is 'Jack Robinson'. A customer wants to purchase two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) at 'STORE-001'. First, verify the quantity in stock at 'STORE-001'. The 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003) is scheduled to start today, '2025-06-10', so you must activate it. After activating, get the full product details of the yoga mat to confirm its properties. If the promotion is active, calculate the total cost applying the BOGO discount. Record the transaction as 'completed' via 'credit_card' for 'Noah Johnson' (CUST-5004). Update inventory for the product on '2025-06-10' by adjusting the quantity sold. Finally, increment the 'times_used' for this promotion by 1 and provide the total amount, the discount applied, and the transaction ID.",
        actions=[
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"},
            ),
            Action(
                name="activate_promotion",
                kwargs={"promotion_id": "PROMO-003"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "SPORT-YOGMAT01"},
            ),
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Noah Johnson"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Jack Robinson"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0021",
                    "quantity_sold": 2,
                    "last_stock_count_date": "2025-06-10",
                },
            ),
            Action(
                name="create_transaction",
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
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-003", "times_used": 1},
            ),
        ],
        outputs=["Total amount: 48.70", "Discount applied: 14.995", "Transaction ID: TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_007",
        instruction="You are a marketing manager. Reintroduce a flash sale for Home & Kitchen products. First, get all products currently under the 'Home & Kitchen' category by getting details for specific SKUs (HOM-COFMKR12, KITCH-CHEFKNF8, HOME-BTHTWL01, HOME-DESKLMP01, KITCH-FRYPAN10) to ensure they are correctly listed. Then, update the 'Weekend Flash Sale - Home & Kitchen' (PROMO-007) by changing its status to 'active' for '2025-07-28' and '2025-07-29' only, set its 'usage_limit' to 50, and update its description to 'Weekend Special: 18% off Home & Kitchen!'. Finally, get all active promotions to confirm the flash sale is now listed with its updated details. The current date is '2025-07-27'.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOM-COFMKR12"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "KITCH-CHEFKNF8"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOME-DESKLMP01"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "KITCH-FRYPAN10"},
            ),
            Action(
                name="update_promotion_details",
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
                name="get_promotions_by_status",
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
        instruction="You are a sales associate and your name is 'Grace Miller'. A customer named 'Liam Nguyen' wants to purchase the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) at 'STORE-001'. Confirm if there is sufficient stock by getting its inventory details. The current date is '2025-08-01'. Check if the 'Grand Summer Electronics Sale' promotion is active and if the TV is eligible by getting product details and promotion details. If it is active and eligible, calculate the total amount considering the discount. If not, only use the regular price. Then, create a transaction for 'Liam Nguyen' via 'credit_card', updating the inventory's last stock count date to '2025-08-01'. After completing the transaction, update 'Liam Nguyen's loyalty points by 150. Provide the final total amount, the discount applied, and the transaction ID.",
        actions=[
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="get_promotion_by_name_and_date",
                kwargs={"promotion_name": "Grand Summer Electronics Sale", "query_date": "2025-08-01"},
            ),
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Liam Nguyen"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Grace Miller"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0001",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-08-01",
                },
            ),
            Action(
                name="create_transaction",
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
                name="update_customer_loyalty_points",
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
        instruction="You are a marketing manager. We need to update the 'Smart Home Starter Discount' (PROMO-006) to only apply to 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02) moving forward. Change its description to 'Exclusive discount on smart thermostats.' and remove 'WaveSound All-Weather Bluetooth Bluetooth Speaker' (AUDIO-BTSPKR02) from its applicable SKUs. After this, get the details of the 'WaveSound All-Weather Bluetooth Speaker' and change its `status` to `limited_availability` to reflect its removal from general promotions. Also, confirm the promotion's new applicable SKUs and description. The current date is '2025-07-10'.",
        actions=[
            Action(
                name="update_promotion_details",
                kwargs={
                    "promotion_id": "PROMO-006",
                    "description": "Exclusive discount on smart thermostats.",
                    "applicable_skus": ["SMRT-THERM02"],
                },
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "AUDIO-BTSPKR02", "status": "limited_availability"},
            ),
            Action(
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-006"},
            ),
            Action(
                name="get_product_details_by_sku",
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
        instruction="You are a marketing manager. Create a new promotion named 'Spring Cleaning Sale'. This promotion should offer a 'percentage' discount of 20.0% on 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01) and 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). The promotion's description must be '20% off selected home & kitchen items for spring cleaning.'. It should be 'scheduled' to run from '2026-03-01' to '2026-03-15'. Before creating, confirm the price and current 'is_discountable' status of both products. If either is not discountable, update their 'is_discountable' status to True. After creating the promotion, retrieve all 'scheduled' promotions to confirm its addition. Finally, update its 'times_used' to 0 and 'usage_limit' to 500. Retrieve the updated promotion details by its ID.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "HOME-BTHTWL01", "is_discountable": True},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "KITCH-FRYPAN10"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "KITCH-FRYPAN10", "is_discountable": True},
            ),
            Action(
                name="create_promotion",
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
                name="get_promotions_by_status",
                kwargs={"status": "scheduled"},
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-008", "times_used": 0, "usage_limit": 500}, # PROMO-008 is the next ID
            ),
            Action(
                name="get_promotion_by_id",
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
        instruction="You are a customer service representative and your name is 'Natalie Cooper'. A customer ('Ava Thompson') is asking about the 'Summer Electronics Sale' (PROMO-001). The current date is '2025-08-10'. Retrieve its details, specifically its 'times_used' and 'end_date'. Since its 'end_date' ('2025-08-31') is within the current month or earlier, deactivate this promotion immediately. Update its description to 'Promotion expired due to end date.' and set its status to 'expired'. Then, confirm if 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) is still listed as an applicable SKU and confirm its latest price and stock status at 'STORE-001'. Finally, retrieve the updated promotion details by its ID.",
        actions=[
            Action(
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="deactivate_promotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-001", "status": "expired", "description": "Promotion expired due to end date."}, # De instrução
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="get_promotion_by_id",
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
        instruction="You are a marketing manager. The 'Buy One Yoga Mat Get 50% Off Second' (PROMO-003) is scheduled and needs to be activated for '2025-06-10'. Before activating, retrieve the product details for 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) to confirm its category. If its category is not 'Sports & Outdoors', update it to 'Sports & Outdoors'. Then, activate PROMO-003. After activation, get all active promotions to confirm its status and list all its applicable SKUs. Finally, increment 'times_used' for PROMO-003 by 1 for an internal test.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "SPORT-YOGMAT01"},
            ),
            Action(
                name="update_product_details", # Condicional, mas executada para determinismo
                kwargs={"sku": "SPORT-YOGMAT01", "category": "Sports & Outdoors"},
            ),
            Action(
                name="activate_promotion",
                kwargs={"promotion_id": "PROMO-003"}, # Agora existe
            ),
            Action(
                name="get_promotions_by_status",
                kwargs={"status": "active"},
            ),
            Action(
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-003"},
            ),
            Action(
                name="update_promotion_details",
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
        instruction="You are a sales associate and your name is 'Daniel Perez'. A Gold level customer, 'Ava Thompson' (CUST-5001), wants to purchase 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02) from 'STORE-005' and 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01) from 'STORE-001'. The transaction will be processed at 'STORE-001'. The current date is '2025-07-28'. First, get the inventory details for both products from their respective stores. Then, get the full product details for each. Check if 'Smart Home Starter Discount' (PROMO-006) is active for the speaker. *Since PROMO-006 ends on 2025-07-20, it will not apply today, 2025-07-28*. Calculate the total cost without applying that discount. Create a transaction for 'Ava Thompson' at 'STORE-001' via 'credit_card', updating inventories. Finally, update 'Ava Thompson's loyalty points by 50, and get their updated customer details by ID.",
        actions=[
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-001"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "AUDIO-BTSPKR02"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOME-BTHTWL01"},
            ),
            Action(
                name="get_promotion_by_name_and_date",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-28"}, # Esta chamada deve retornar {}, ou uma promoção inativa.
            ),
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Ava Thompson"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Daniel Perez"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0010",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-07-28",
                },
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0012",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-07-28",
                },
            ),
            Action(
                name="create_transaction",
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
                name="update_customer_loyalty_points",
                kwargs={"customer_id": "CUST-5001", "points_to_add": 50},
            ),
            Action(
                name="get_customer_details_by_id", # Usar a nova ferramenta
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
        instruction="You are an inventory specialist and your name is 'Zoe Martinez'. Monitor the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) at 'STORE-001'. The current date is '2025-08-01'. Retrieve its inventory details, specifically its 'quantity' and 'safety_stock'. Update the product's 'status' to 'out_of_stock' and update the inventory's 'status' to 'out_of_stock' for ELEC-4KTV55 at STORE-001, indicating an immediate stock depletion in this scenario. Additionally, regardless of current stock level, deactivate the 'Summer Electronics Sale' (PROMO-001) if it is active today, and update its description to 'Deactivated due to inventory concerns.'. Finally, get all promotions with 'inactive' status and the details of 'UltraVision 55\" 4K Smart TV' to confirm changes.",
        actions=[
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "ELEC-4KTV55"},
            ),
            Action(
                name="get_promotion_by_name_and_date",
                kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-08-01"},
            ),
            Action(
                name="deactivate_promotion",
                kwargs={"promotion_id": "PROMO-001"},
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-001", "description": "Deactivated due to inventory concerns.", "status": "inactive"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "ELEC-4KTV55", "status": "out_of_stock"},
            ),
            Action(
                name="update_inventory_status",
                kwargs={"inventory_id": "INV-0001", "status": "out_of_stock"},
            ),
            Action(
                name="get_promotions_by_status",
                kwargs={"status": "inactive"},
            ),
            Action(
                name="get_product_details_by_sku",
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
        instruction="You are a marketing manager. We need to adjust pricing for all 'Grocery' items. Increase the price of 'Organic Almond Butter 500g' (GROC-ALMBTR500) to 13.99 and 'SparkleLife Sparkling Water 1L (6 Pack)' (GROC-SPRWAT6P) to 8.50. After adjusting prices, create a new 'fixed_bundle' promotion named 'Healthy Snack Bundle'. This promotion should offer a 5.0 discount when both 'Organic Almond Butter 500g' and 'High-Protein Granola Bars (12 Pack)' (GROC-GRNLBR12) are purchased together. Its description must be 'Save on a healthy snack bundle.'. It should be 'active' from '2025-09-01' to '2025-10-31', with no usage limit and 0 times used. Confirm the new prices of the updated products, and then verify the new promotion is listed as 'active' for '2025-09-01' by retrieving its details.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-ALMBTR500"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "GROC-ALMBTR500", "price": 13.99},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-SPRWAT6P"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "GROC-SPRWAT6P", "price": 8.50},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-GRNLBR12"},
            ),
            Action(
                name="create_promotion",
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
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-ALMBTR500"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-SPRWAT6P"},
            ),
            Action(
                name="get_promotion_by_name_and_date",
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
        instruction="You are a sales associate and your name is 'Isabella Rossi'. A customer named 'Noah Johnson' (CUST-5004), a Platinum member, wants to buy 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) from 'STORE-003' and 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) from 'STORE-001'. The transaction will be processed at 'STORE-001'. The current date is '2025-09-10'. First, confirm stock for both items at their respective stores. Then, retrieve full details for both products. Activate the 'Weekend Flash Sale - Home & Kitchen' (PROMO-007) for '2025-09-10' and '2025-09-11', and update its applicable SKUs to include 'OFFC-ERGCHR01' and 'HOME-DESKLMP01', setting its discount value to 18.0%. Calculate the total cost applying relevant discounts. Create a transaction for 'Noah Johnson' via 'debit_card'. Update inventory for both products on '2025-09-10'. Finally, update 'Noah Johnson's loyalty points by 200 and their 'membership_level' to 'diamond' as a special upgrade. Retrieve 'Noah Johnson's updated customer details by ID.",
        actions=[
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "OFFC-ERGCHR01"},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "HOME-DESKLMP01"},
            ),
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Noah Johnson"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Isabella Rossi"},
            ),
            Action(
                name="update_promotion_details", # Activate PROMO-007
                kwargs={"promotion_id": "PROMO-007", "status": "active", "start_date": "2025-09-10", "end_date": "2025-09-11"},
            ),
            Action(
                name="update_promotion_details", # Add SKUs and set discount value
                kwargs={"promotion_id": "PROMO-007", "applicable_skus": ["OFFC-ERGCHR01", "HOME-DESKLMP01", "HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "KITCH-FRYPAN10"], "discount_value": 18.0}, # Corrected applicable_skus
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0014",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-09-10",
                },
            ),
            Action(
                name="update_inventory_sale",
                kwargs={
                    "inventory_id": "INV-0015",
                    "quantity_sold": 1,
                    "last_stock_count_date": "2025-09-10",
                },
            ),
            Action(
                name="create_transaction",
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
                name="update_customer_loyalty_points",
                kwargs={"customer_id": "CUST-5004", "points_to_add": 200},
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5004", "membership_level": "diamond"},
            ),
            Action(
                name="get_customer_details_by_id", # Corrected to get full details
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
        instruction="You are a regional manager. The stock of 'Apparel' products is high in 'STORE-002' and low in 'STORE-001'. First, ensure all products in the 'Apparel' category are marked as discountable in the system. Then, initiate a transfer of 10 units of 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 3 units of 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) from 'STORE-002' to 'STORE-001'. When creating the new inventory records at the destination, assign them to the 'Apparel Zone' location. After the transfers, create a new 'percentage' promotion named 'Apparel Off-Season Sale' with a 15% discount and description 'Get our apparel for less during the off-season.'. The promotion should apply to all 'Apparel' products and be scheduled from '2025-10-01' to '2025-10-31'. Finally, confirm the new promotion's details by retrieving it by its ID.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "CLTH-SLFJEAN34"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True},
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "CLTH-WINJKT01"},
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True},
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001", "location": "Apparel Zone"},
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Apparel Zone"},
            ),
            Action(
                name="execute_inventory_transfer",
                kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 10, "from_store_id": "STORE-002", "to_store_id": "STORE-001"},
            ),
            Action(
                name="execute_inventory_transfer",
                kwargs={"sku": "CLTH-WINJKT01", "quantity": 3, "from_store_id": "STORE-002", "to_store_id": "STORE-001"},
            ),
            Action(
                name="create_promotion",
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
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-008"},
            ),
        ],
        outputs=["PROMO-008"],
    ),
    Task(
        annotator="0",
        user_id="task_018",
        instruction="You are a Marketing Director. We need to launch a targeted flash sale for our most valuable customers. First, identify all products in the 'Electronics' category. Then, find all 'gold' and 'platinum' customers who have purchased any of these electronic items. Once you have this target audience, create a new 'percentage' promotion named 'VIP Electronics Sale' with a 25% discount, scheduled to be active from '2025-08-15' to '2025-08-20', with a description 'An exclusive electronics offer for our VIPs.'. After creating the promotion, generate and assign a unique, single-use code for each qualified customer. Finally, update the promotion to require a unique code for redemption and retrieve the details of the customers who received a code to confirm their status.",
        actions=[
            Action(
                name="get_products_by_category",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["gold", "platinum"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="create_promotion",
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
                name="generate_and_assign_promo_codes",
                kwargs={
                    "customer_ids": ["CUST-5001", "CUST-5010"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5010"},
            ),
        ],
        outputs=["PROMO-008", "CUST-5001", "CUST-5010"],
    ),
    Task(
        annotator="0",
        user_id="task_019",
        instruction="You are a CRM Manager. We want to reward our active 'silver' level customers. First, identify all products within the 'Home & Kitchen' category. Use this information to find all 'silver' members who have purchased any of these items. For all customers found, check their current loyalty points. As a loyalty bonus, any customer in this group with more than 800 points should be immediately upgraded to 'gold' membership status. After performing the updates, retrieve the full details for each of the upgraded customers to confirm their new status.",
        actions=[
            Action(
                name="get_products_by_category",
                kwargs={"category": "Home & Kitchen"},
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["silver"],
                    "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                },
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5002"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5006"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5009"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5011"},
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5002", "membership_level": "gold"},
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5006", "membership_level": "gold"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5002"},
            ),
            Action(
                name="get_customer_details_by_id",
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
        instruction="You are a Marketing Director launching a campaign for outdoor enthusiasts. First, identify all products in the 'Sports & Outdoors' category. With this list, find all 'gold' and 'platinum' customers who have previously purchased any of these items. For this specific audience, create a new 'percentage' promotion named 'VIP Adventure Gear Offer' with a 20% discount, scheduled for the entire month of September, with the description 'A special offer for our top adventurers.'. After creating the promotion, generate unique, single-use promotional codes for all qualified customers. Finally, confirm the details of all customers who were assigned a code.",
        actions=[
            Action(
                name="get_products_by_category",
                kwargs={"category": "Sports & Outdoors"},
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["gold", "platinum"],
                    "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                },
            ),
            Action(
                name="create_promotion",
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
                name="generate_and_assign_promo_codes",
                kwargs={
                    "customer_ids": ["CUST-5004"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5004"},
            ),
        ],
        outputs=["PROMO-008", "CUST-5004"],
    ),
    Task(
        annotator="0",
        user_id="task_021",
        instruction="You are a CRM Manager focusing on rewarding top-tier customers. Identify all 'gold' level customers who have made purchases in the 'Electronics' category. For every customer found, retrieve their detailed information to check their current loyalty points. As a special reward for their continued business, if a customer has accumulated between 1000 and 2000 loyalty points, upgrade their membership level to 'platinum'. After performing all necessary upgrades, retrieve the details of the upgraded customers again to confirm their new 'platinum' status.",
        actions=[
            Action(
                name="get_products_by_category",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["gold"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5010"},
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5001", "membership_level": "platinum"},
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5010", "membership_level": "platinum"},
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5001"},
            ),
            Action(
                name="get_customer_details_by_id",
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
        instruction="You are a Sales Lead, 'Ethan Walker', at STORE-002, assisting customer 'Liam Nguyen'. The customer wants to purchase a 'ProSlice 8\" Chef Knife' and 'Men's Slim Fit Jeans - 34W 32L'. To encourage the sale, create a new 'percentage' promotion named 'STORE-002 Daily Deal' offering 20% off these specific items, **with the description 'Daily deal on select items.'**, and make it active for today's date. Calculate the final transaction total applying the new discount. Process the sale using a 'credit_card', ensuring you first fetch the inventory records for both items at your store before updating their stock levels.",
        actions=[
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Liam Nguyen"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Ethan Walker"},
            ),
            Action(
                name="create_promotion",
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
                name="calculate_transaction_totals",
                kwargs={
                    "line_items": [
                        {"sku": "KITCH-CHEFKNF8", "quantity": 1},
                        {"sku": "CLTH-SLFJEAN34", "quantity": 1}
                    ],
                    "promotion_ids": ["PROMO-008"],
                },
            ),
            Action(
                name="create_transaction",
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
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0011", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0005", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
        ],
        outputs=["TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_023",
        instruction="You are a sales associate, 'Amelia Lee', at STORE-004. A customer, 'Noah Johnson', wants to purchase two 'TrailGuard Mountain Bike Helmets' and one 'EcoSmart Wi-Fi Thermostat'. First, process a new shipment by adding 5 units of the 'EcoSmart Wi-Fi Thermostat' to your store's inventory, creating a new record for it in the 'Smart Home Display' if one doesn't already exist. Then, proceed with the customer's request. Check if the 'Smart Home Starter Discount' is active for the thermostat on today's date, 2025-07-28. Since the promotion is expired, do not apply any discounts. Calculate the final cost and process the transaction with 'credit_card', updating the stock for both products accordingly.",
        actions=[
            Action(
                name="get_customer_id_by_name",
                kwargs={"customer_name": "Noah Johnson"},
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Amelia Lee"},
            ),
            Action(
                name="get_promotion_by_name_and_date",
                kwargs={"promotion_name": "Smart Home Starter Discount", "query_date": "2025-07-28"},
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-004", "location": "Smart Home Display"},
            ),
            Action(
                name="update_stock_level",
                kwargs={"inventory_id": "INV-0025", "quantity_to_add": 5},
            ),
            Action(
                name="calculate_transaction_totals",
                kwargs={
                    "line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 2}, {"sku": "SMRT-THERM02", "quantity": 1}],
                    "promotion_ids": [],
                },
            ),
            Action(
                name="create_transaction",
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
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-004"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0009", "quantity_sold": 2, "last_stock_count_date": "2025-07-28"},
            ),
            Action(
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-07-28"},
            ),
        ],
        outputs=["TXN-0013"],
    ),
    Task(
        annotator="0",
        user_id="task_024",
        instruction="You are the inventory manager, 'Amelia Lee', at STORE-004. You've noticed that the 'TrailGuard Mountain Bike Helmet' is running low. To prevent a stockout, create a temporary 'percentage' promotion named 'Helmet Pre-Clearance' with a 5% discount and the description 'Temporary discount to clear final units.' It should be active for today's date, '2025-07-29', with an initial usage count of zero and no usage limit. You must then immediately deactivate it. Next, create an inventory record for the helmet at the main warehouse, STORE-001, in the 'Central Stock' location. Transfer the entire remaining stock of 4 units from your store to the warehouse, ensuring any reservations are also cleared. Finally, update the inventory status for the helmet at your store to reflect that it is now out of stock.",
        actions=[
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Amelia Lee"},
            ),
            Action(
                name="get_product_sku_by_name",
                kwargs={"product_name": "TrailGuard Mountain Bike Helmet"},
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"},
            ),
            Action(
                name="create_promotion",
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
                name="deactivate_promotion",
                kwargs={"promotion_id": "PROMO-008"},
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-001", "location": "Central Stock"},
            ),
            Action(
                name="execute_inventory_transfer",
                kwargs={"sku": "SPORT-BIKHLM01", "quantity": 4, "from_store_id": "STORE-004", "to_store_id": "STORE-001"},
            ),
            Action(
                name="update_inventory_reserved_quantity",
                kwargs={"inventory_id": "INV-0009", "change_amount": -1},
            ),
            Action(
                name="update_inventory_status",
                kwargs={"inventory_id": "INV-0009", "status": "out_of_stock"},
            ),
        ],
        outputs=[{"inventory_id": "INV-0009", "status": "out_of_stock"}],
    ),
    Task(
        annotator="0",
        user_id="task_025",
        instruction="As a Marketing Specialist, create a new 'percentage' promotion named 'Back-to-School Tech Sale' with a 15% discount on all 'Electronics' and the description '15% off all electronics for the back-to-school season.'. The promotion should be scheduled to run from '2025-08-18' to '2025-08-31'. After creating the promotion, generate unique promotional codes for all customers who have a 'gold' membership level and have previously purchased items from the 'Electronics' category. Finally, retrieve the promotion's details to confirm it has been set up correctly.",
        actions=[
            Action(
                name="get_products_by_category",
                kwargs={"category": "Electronics"},
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["gold"],
                    "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                },
            ),
            Action(
                name="create_promotion",
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
                name="generate_and_assign_promo_codes",
                kwargs={
                    "customer_ids": ["CUST-5001", "CUST-5010"],
                    "promotion_id": "PROMO-008",
                },
            ),
            Action(
                name="get_promotion_by_id",
                kwargs={"promotion_id": "PROMO-008"},
            ),
        ],
        outputs=["PROMO-008"],
    ),
    Task(
        annotator="0",
        user_id="task_026",
        instruction="As a regional manager on '2025-09-05', you've identified an overstock of 'Apparel' at 'STORE-002'. Your goal is to consolidate this stock at 'STORE-001' and initiate a clearance sale. First, ensure the products 'Men's Slim Fit Jeans - 34W 32L' and 'ArcticShield Men's Parka - Large' are marked as discountable. Then, find their current stock and reserved quantities at 'STORE-002' and transfer the entire physical stock to 'STORE-001', creating new inventory records in the 'Apparel Zone' if needed and clearing any reservations at the source. Once the transfer is complete, create a new 'percentage' promotion named 'Final Apparel Clearance' with a 35% discount and description 'Final sale on select apparel items.', scheduled from '2025-09-06' to '2025-09-20', applicable only to these SKUs. Finally, confirm the new stock levels at 'STORE-001'.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001", "location": "Apparel Zone"}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Apparel Zone"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 30, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0005", "change_amount": -6}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 6, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0022", "change_amount": -1}),
            Action(name="create_promotion", kwargs={
                "name": "Final Apparel Clearance", "type": "percentage", "discount_value": 35.0,
                "description": "Final sale on select apparel items.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-06", "end_date": "2025-09-20", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001"}),
        ],
        outputs=[
            {"inventory_id": "INV-0025", "sku": "CLTH-SLFJEAN34", "quantity": 30},
            {"inventory_id": "INV-0026", "sku": "CLTH-WINJKT01", "quantity": 6},
        ]
    ),
    Task(
        annotator="0",
        user_id="task_027",
        instruction="As a CRM Manager on '2025-10-01', you want to run a targeted campaign for 'platinum' members who frequently purchase 'Sports & Outdoors' items. Your goal is to find these customers and offer them a special promotion. First, identify all products in the 'Sports & Outdoors' category. Use this list to find all 'platinum' customers who have purchased these items. For this specific audience, create a new 'percentage' promotion named 'Platinum Adventurer Reward' with a 25% discount, description 'An exclusive reward for our top adventurers.', scheduled from '2025-10-02' to '2025-10-16', applicable to all 'Sports & Outdoors' items. Then, generate unique, single-use promotional codes for all qualified customers. Finally, confirm the promotion ID and the list of customer IDs that received a code.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["platinum"],
                "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]
            }),
            Action(name="create_promotion", kwargs={
                "name": "Platinum Adventurer Reward", "type": "percentage", "discount_value": 25.0,
                "description": "An exclusive reward for our top adventurers.",
                "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                "start_date": "2025-10-02", "end_date": "2025-10-16", "status": "scheduled", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={
                "customer_ids": ["CUST-5004"],
                "promotion_id": "PROMO-008"
            }),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5004"}),
        ],
        outputs=["PROMO-008", ["CUST-5004"]]
    ),
    Task(
        annotator="0",
        user_id="task_028",
        instruction="As the customer service lead 'Natalie Cooper' on '2025-07-15', handle a return for 'James O'Connor'. He wants to return two 'High-Protein Granola Bars (12 Pack)' from transaction 'TXN-0003'. However, upon inspection, one package is expired. Process the return only for the non-expired item, issuing credit. Because of the inconvenience, find all 'bronze' members who have purchased 'Grocery' items and upgrade them to 'silver' status. Also, deactivate the 'Kitchen Essentials Bundle' promotion as it is ending today and update its description to 'Promotion has expired.'",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "James O'Connor"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "High-Protein Granola Bars (12 Pack)"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-GRNLBR12"}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0003", "sku": "GROC-GRNLBR12", "quantity_returned": 1, "unit_price": 14.99}),
            Action(name="get_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["bronze"],
                "purchase_history_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"]
            }),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5003", "membership_level": "silver"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Kitchen Essentials Bundle", "query_date": "2025-07-15"}),
            Action(name="deactivate_promotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-002", "description": "Promotion has expired."})
        ],
        outputs=[
            {"customer_id": "CUST-5003", "membership_level": "silver"},
            {"promotion_id": "PROMO-002", "status": "inactive"},
        ]
    ),
    Task(
        annotator="0",
        user_id="task_029",
        instruction="As the inventory manager 'Zoe Martinez' on '2025-06-20', you need to perform a stock audit for the 'BrewMaster 12-Cup Coffee Maker' at 'STORE-001'. First, retrieve its inventory record. You've physically counted 20 units. If this count doesn't match the system's quantity (currently 25), update the stock level to reflect the physical count. As the quantity is now adjusted, create a new 'percentage' promotion named 'Coffee Lovers Special' with an 8% discount and description 'A special deal on BrewMaster coffee makers.' to help sell the remaining stock, active from '2025-06-21' to '2025-07-21'.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -5}),
            Action(name="create_promotion", kwargs={
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
        instruction="You are 'Marcus Chen' (EMP-1008), a manager at 'STORE-002'. Customer 'Mia Kim' (CUST-5011) is returning one 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) from her transaction 'TXN-0011' due to a defect. The item cannot be resold. Process the return, ensuring the main inventory quantity is updated and the 'reserved_quantity' for that inventory item is also decremented by one. As an apology for the inconvenience, add 75 points to her loyalty account. She then decides to purchase an 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01), and she will use a 'credit_card'. You will need to make this product discountable first. Then, create a new 10% 'percentage' promotion named 'Winter Gear Welcome' for this item, active today (2025-07-29). The promotion's description must be 'A special welcome discount on winter apparel.' and its initial usage count must be set to zero. Check the parka's stock at 'STORE-002', calculate the final price with the new promotion, and create the transaction. Finally, update the parka's inventory record to reflect the sale.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Mia Kim"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ProSlice 8\" Chef Knife"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5011", "sku": "KITCH-CHEFKNF8"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0011", "sku": "KITCH-CHEFKNF8", "quantity_returned": 1, "unit_price": 39.95}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0011", "change_amount": -1}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 75}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="create_promotion", kwargs={
                "name": "Winter Gear Welcome", "type": "percentage", "discount_value": 10.0,
                "description": "A special welcome discount on winter apparel.", "applicable_skus": ["CLTH-WINJKT01"],
                "start_date": "2025-07-29", "end_date": "2025-07-29", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 1}], "promotion_ids": ["PROMO-008"]
            }),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Marcus Chen"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1008", "customer_id": "CUST-5011", "payment_method": "credit_card",
                "total_amount": 184.62, "tax_amount": 14.07, "discount_total": 18.95,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 1, "unit_price": 189.5, "discount": 18.95}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_031",
        instruction="You are the inventory manager, 'Zoe Martinez'. You've noticed that the 'Apparel' category is overstocked at 'STORE-002' but has low stock at 'STORE-003'. Specifically, the products 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). The parka is not marked as 'is_discountable'. First, update the parka's product details to allow discounts. Then, transfer 20 units of the jeans and 5 units of the parka from 'STORE-002' to 'STORE-003', creating new inventory records at 'STORE-003' in the 'Apparel Dept' location before the transfer. Once complete, create a new 'percentage' promotion named 'Store 3 Apparel Sale' with a 20% discount, description 'Special sale on newly transferred apparel!', applicable only to these two SKUs and scheduled for '2025-08-15' to '2025-08-31'. Finally, confirm the new stock levels for both items at 'STORE-003'.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003", "location": "Apparel Dept"}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-003", "location": "Apparel Dept"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-SLFJEAN34", "quantity": 20, "from_store_id": "STORE-002", "to_store_id": "STORE-003"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 5, "from_store_id": "STORE-002", "to_store_id": "STORE-003"}),
            Action(name="create_promotion", kwargs={
                "name": "Store 3 Apparel Sale", "type": "percentage", "discount_value": 20.0,
                "description": "Special sale on newly transferred apparel!", "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-08-15", "end_date": "2025-08-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-003"})
        ],
        outputs=[
            {"sku": "CLTH-SLFJEAN34", "store_id": "STORE-003", "quantity": 20},
            {"sku": "CLTH-WINJKT01", "store_id": "STORE-003", "quantity": 5}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_032",
        instruction="You are the sales lead, 'Ethan Walker', at 'STORE-002'. A new customer, 'Dr. Evelyn Reed', walks in. She is a high-value client, and you have the authority to add her directly at the 'platinum' tier. Create a new account for 'Dr. Evelyn Reed' with 'platinum' membership, 2000 initial loyalty points, and marketing opt-in. She wants to purchase the 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15) and the 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01). Before proceeding, check the details for the laptop and you'll notice it is not discountable. Update the product to make it discountable. Then, check the stock for both products at your store. Also, check if the 'Summer Electronics Sale' promotion is active today (2025-07-29) and applies to either item. Calculate the transaction totals, applying the valid discount. Process the payment via 'credit_card', create the transaction record using the calculated totals, and update stock levels. Finally, return the new customer ID and the transaction ID.",
        actions=[
            Action(name="create_customer", kwargs={
                "name": "Dr. Evelyn Reed", "membership_level": "platinum", "opt_in_marketing": True, "loyalty_points": 2000
            }),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="update_product_details", kwargs={"sku": "ELEC-GAMLP15", "is_discountable": True}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-07-29"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1}, {"sku": "AUDIO-NCEBUDS01", "quantity": 1}], "promotion_ids": ["PROMO-001"]
            }),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Ethan Walker"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1011", "customer_id": "CUST-5013", "payment_method": "credit_card",
                "total_amount": 1622.76, "tax_amount": 123.67, "discount_total": 149.90,
                "line_items": [
                    {"sku": "ELEC-GAMLP15", "quantity": 1, "unit_price": 1499.0, "discount": 149.90},
                    {"sku": "AUDIO-NCEBUDS01", "quantity": 1, "unit_price": 149.99, "discount": 0.0}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0013", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0016", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=["Customer ID: CUST-5013", "Transaction ID: TXN-0013"]
    ),
    Task(
        annotator="0",
        user_id="task_033",
        instruction="You are the Marketing Director. Launch a campaign to encourage customers who bought electronics to try our 'Smart Home' products. First, identify all products in the 'Electronics' category. Then, find all 'gold' and 'platinum' tier customers who have purchased any of these electronics. For this audience, create a new 'percentage' promotion named 'Smart Home Upgrade' with a 25% discount on all 'Smart Home' category products, with the description 'An exclusive offer to make your home smarter.', scheduled for '2025-09-01' to '2025-09-15'. After creating the promotion, generate and assign unique, single-use codes for each qualified customer. Finally, update the promotion to require a code and retrieve the details of the customers who received a code to confirm their names and membership levels.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["gold", "platinum"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]
            }),
            Action(name="get_products_by_category", kwargs={"category": "Smart Home"}),
            Action(name="create_promotion", kwargs={
                "name": "Smart Home Upgrade", "type": "percentage", "discount_value": 25.0,
                "description": "An exclusive offer to make your home smarter.", "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-09-01", "end_date": "2025-09-15", "status": "scheduled", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-008", "requires_code": True}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[
            {"name": "Ava Thompson", "membership_level": "gold"},
            {"name": "Benjamin Cohen", "membership_level": "gold"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_034",
        instruction="You are a regional manager. Customer 'William Zhang' (CUST-5006) wants to purchase two items, but they are at different stores: 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is at 'STORE-003' and 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) is at 'STORE-002'. The transaction will be processed at 'STORE-002' by employee 'Marcus Chen'. The customer will pay using their 'debit_card'. Check the stock for each item at its respective store. As there are no active promotions for these items today (2025-07-29), calculate the total cost without discounts. Create the transaction at 'STORE-002'. After the transaction, it is crucial that you update the stock levels at BOTH stores ('STORE-002' and 'STORE-003'). Based on the total value of this purchase, the customer qualifies for an upgrade. Update 'William Zhang's' membership level from 'silver' to 'gold'. Finally, retrieve the customer's full details to confirm their new membership.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "William Zhang"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Marcus Chen"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "OFFC-ERGCHR01", "quantity": 1}, {"sku": "KITCH-CHEFKNF8", "quantity": 1}]
            }),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1008", "customer_id": "CUST-5006", "payment_method": "debit_card",
                "total_amount": 292.21, "tax_amount": 22.27, "discount_total": 0.0,
                "line_items": [
                    {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 0.0},
                    {"sku": "KITCH-CHEFKNF8", "quantity": 1, "unit_price": 39.95, "discount": 0.0}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0014", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0011", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
    Task(
        annotator="0",
        user_id="task_035",
        instruction="You are the inventory manager, 'Zoe Martinez'. A price audit has revealed incorrect pricing for two key kitchen items. 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) is listed at $39.95 but must be updated to $42.50. 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10) is listed at $24.95 but must be corrected to $27.00. First, get the details for both products to confirm their current prices, then update them to the correct prices. To offset this price increase, immediately create a new 'fixed_bundle' promotion named 'Kitchen Starter Duo' that gives a $10.00 discount when both items are purchased together. The promotion description must be 'Save $10 on our top kitchen tools bundle.', it should be active from '2025-08-01' to '2025-08-31', and its initial usage count should be 0. Finally, retrieve the new promotion by its ID to confirm its creation.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-FRYPAN10"}),
            Action(name="update_product_details", kwargs={"sku": "KITCH-CHEFKNF8", "price": 42.50}),
            Action(name="update_product_details", kwargs={"sku": "KITCH-FRYPAN10", "price": 27.00}),
            Action(name="create_promotion", kwargs={
                "name": "Kitchen Starter Duo", "type": "fixed_bundle", "discount_value": 10.0,
                "description": "Save $10 on our top kitchen tools bundle.",
                "applicable_skus": ["KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-08-01", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-008", "name": "Kitchen Starter Duo"}]
    ),
    Task(
        annotator="0",
        user_id="task_036",
        instruction="You are a Regional Manager. A supplier has issued a recall for 'PowerPlus Rechargeable AA Batteries (4 Pack)' (ELEC-RCHAA04) due to a safety concern. First, find the inventory record for this product at 'STORE-003' and update its status to 'recalled'. Next, update the main product entry in the system to change its status to 'discontinued' to prevent future orders. As a proactive measure, you need to identify all customers who have ever purchased this item. For each 'gold' or 'platinum' customer identified from these transactions, add 150 loyalty points to their account as an apology. Finally, retrieve the updated customer details for 'Ava Thompson' to confirm her new point balance.",
        actions=[
            Action(
                name="get_product_sku_by_name",
                kwargs={"product_name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003"}
            ),
            Action(
                name="update_inventory_status",
                kwargs={"inventory_id": "INV-0020", "status": "recalled"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "ELEC-RCHAA04", "status": "discontinued"}
            ),
            # ACTION CORRIGIDA:
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "purchase_history_skus": ["ELEC-RCHAA04"],
                    "membership_levels": ["gold", "platinum"],
                },
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5001"}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5010"}
            ),
            Action(
                name="update_customer_loyalty_points",
                kwargs={"customer_id": "CUST-5001", "points_to_add": 150}
            ),
            Action(
                name="update_customer_loyalty_points",
                kwargs={"customer_id": "CUST-5010", "points_to_add": 150}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5001"}
            )
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1390}],
    ),
    Task(
        annotator="0",
        user_id="task_037",
        instruction="You are 'Jack Robinson', a sales associate at 'STORE-001'. On today's date, '2025-07-29', a 'platinum' level customer, 'Noah Johnson', wishes to buy two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) and one 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55). He mentions the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003), but you see it is currently 'scheduled'. First, check the inventory at 'STORE-001' to ensure you have at least two yoga mats and one TV in stock. Then, you must activate 'PROMO-003'. After activation, process the sale via 'credit_card'. The transaction must be created with a precise discount_total of $15.00, a tax_amount of $61.46, and a final total_amount of $806.43. Finally, update the inventory for all three items sold and increase the 'times_used' count for the promotion by one.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Noah Johnson"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Jack Robinson"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="activate_promotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1034", "customer_id": "CUST-5004", "payment_method": "credit_card",
                "total_amount": 806.43, "tax_amount": 61.46, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00},
                    {"sku": "ELEC-4KTV55", "quantity": 1, "unit_price": 699.99, "discount": 0.0}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0001", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_038",
        instruction="You are a CRM Manager. Your goal is to re-engage 'bronze' level customers who have only purchased 'Grocery' items and have fewer than 500 loyalty points. First, find all products in the 'Grocery' category. Use this list to find the qualifying 'bronze' customers. For the customers you find, upgrade their membership level to 'silver' as a free incentive. Next, identify all products in the 'Home & Kitchen' category. Create a new 'percentage' promotion named 'Welcome to Our Home Section' with a 25% discount on all 'Home & Kitchen' items. The description must be 'A special offer to explore our Home & Kitchen products.' and it should be active for the month of September 2025, with an initial usage count of 0. Finally, generate unique, single-use promo codes for the upgraded customers and confirm the new 'silver' status of 'Olivia Patel'.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["bronze"],
                "purchase_history_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"]
            }),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5003", "membership_level": "silver"}),
            Action(name="get_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="create_promotion", kwargs={
                "name": "Welcome to Our Home Section", "type": "percentage", "discount_value": 25.0,
                "description": "A special offer to explore our Home & Kitchen products.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                "start_date": "2025-09-01", "end_date": "2025-09-30", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5003"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5003"}),
        ],
        outputs=[{"customer_id": "CUST-5003", "membership_level": "silver"}]
    ),
    Task(
        annotator="0",
        user_id="task_039",
        instruction="You are 'Megan Young', the Store Manager at 'STORE-005'. You've decided that a high-value item, the 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15), should be stocked at your location to boost sales. Currently, your store has no inventory for this item, but you know 'STORE-002' has it. First, confirm the laptop is in stock at 'STORE-002'. Then, create a new inventory record for the laptop at your store ('STORE-005') in the 'Premium Electronics Shelf' location. Proceed to execute a transfer of one unit from 'STORE-002' to 'STORE-005'. Since the new stock quantity at your store will be very low, immediately update the status of this new inventory record to 'low_stock'. To promote the new arrival, create a new 'percentage' promotion named 'STORE-005 Laptop Special' with a 12% discount. The description must be 'Exclusive deal on our new gaming laptop at STORE-005!' This promotion should be active from '2025-08-01' to '2025-08-15', with its initial usage count set to 0. Finally, retrieve the new inventory record from your store to confirm the transfer was successful.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="create_inventory_record", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-005", "location": "Premium Electronics Shelf"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-002", "to_store_id": "STORE-005"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "low_stock"}),
            Action(name="create_promotion", kwargs={
                "name": "STORE-005 Laptop Special", "type": "percentage", "discount_value": 12.0,
                "description": "Exclusive deal on our new gaming laptop at STORE-005!",
                "applicable_skus": ["ELEC-GAMLP15"],
                "start_date": "2025-08-01", "end_date": "2025-08-15", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-005"})
        ],
        outputs=[{"id": "INV-0025", "sku": "ELEC-GAMLP15", "quantity": 1, "status": "low_stock", "store_id": "STORE-005"}]
    ),
    Task(
        annotator="0",
        user_id="task_040",
        instruction="You are a CRM Manager. Customer 'Noah Johnson' (CUST-5004) just completed transaction 'TXN-0004', a high-value purchase. Your task is to reward him. First, retrieve his customer details by his name to confirm his current 'platinum' status and loyalty points. Because of his significant purchase, upgrade his membership to the new 'diamond' tier. Next, identify all products in the 'Office Supplies' category. Create a new 'percentage' promotion named 'Diamond Member Exclusive' with a 30% discount, applicable to all 'Office Supplies' products. The promotion's description must be 'An exclusive 30% off Office Supplies for our new Diamond members.' It should be active for one month starting today, '2025-08-01', with an initial usage count of 0. Finally, generate a single-use promo code for 'Noah Johnson' for this new promotion and retrieve his customer details again to confirm his new 'diamond' status.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Noah Johnson"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5004"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5004", "membership_level": "diamond"}),
            Action(name="get_products_by_category", kwargs={"category": "Office Supplies"}),
            Action(name="create_promotion", kwargs={
                "name": "Diamond Member Exclusive", "type": "percentage", "discount_value": 30.0,
                "description": "An exclusive 30% off Office Supplies for our new Diamond members.",
                "applicable_skus": ["OFFC-ERGCHR01"],
                "start_date": "2025-08-01", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[{"customer_id": "CUST-5004", "membership_level": "diamond"}]
    ),
    Task(
        annotator="0",
        user_id="task_041",
        instruction="You are 'Zoe Martinez', an inventory specialist at 'STORE-001'. A physical count of the 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12) shows only 20 units, but the system shows more. First, get the inventory record for this item at 'STORE-001' to see the current system quantity. You must correct the inventory by updating the stock level to 20 units. Since this new quantity is below the 'reorder_level', you must also update the inventory item's status to 'low_stock'. To clear the remaining items before a new shipment arrives, create a 'percentage' promotion named 'Coffee Maker Clearance' with a 25% discount. The description must be 'Final clearance on BrewMaster Coffee Makers.' and it should be active starting today, '2025-08-02', for one week. Before creating the promotion, you must verify the product is discountable. Finally, retrieve the updated inventory record to confirm the new quantity and status.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -5}), # 25 -> 20
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0003", "status": "low_stock"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOM-COFMKR12"}),
            Action(name="create_promotion", kwargs={
                "name": "Coffee Maker Clearance", "type": "percentage", "discount_value": 25.0,
                "description": "Final clearance on BrewMaster Coffee Makers.",
                "applicable_skus": ["HOM-COFMKR12"],
                "start_date": "2025-08-02", "end_date": "2025-08-09", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0003", "quantity": 20, "status": "low_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_042",
        instruction="You are 'Natalie Cooper', customer service lead at 'STORE-001'. On today's date, '2025-07-29', 'Ava Thompson' (CUST-5001) is returning items from transaction 'TXN-0001'. She is returning one 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), which is in perfect condition, and one 'PowerPlus Rechargeable AA Batteries (4 Pack)' (ELEC-RCHAA04), which is defective. Her receipt confirms the batteries were purchased for $18.95. Process the return for both items: the TV's stock count should be incremented, but the defective batteries should not be. Calculate the total credit. The customer will use this credit to purchase a 'GigaPlay 15\" Gaming Laptop' (ELEC-GAMLP15). You see this laptop is not in stock at your store. You must first create an inventory record for it at 'STORE-001' (location: 'Customer Service Hold') and then transfer a unit from 'STORE-002'. After the transfer succeeds, calculate the final transaction totals for the laptop, applying the full credit. The customer will pay the remaining balance via 'debit_card'. Create the new transaction and update the laptop's inventory at your store.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Ava Thompson"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "UltraVision 55\" 4K Smart TV"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0001", "sku": "ELEC-4KTV55", "quantity_returned": 1, "unit_price": 699.99}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0001", "sku": "ELEC-RCHAA04", "quantity_returned": 1, "unit_price": 18.95}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}),
            Action(name="create_inventory_record", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-001", "location": "Customer Service Hold"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1}],
                "credit_amount": 718.94
            }),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Natalie Cooper"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1004", "customer_id": "CUST-5001", "payment_method": "debit_card",
                "total_amount": 844.41, "tax_amount": 64.35, "discount_total": 0.0,
                "line_items": [{"sku": "ELEC-GAMLP15", "quantity": 1, "unit_price": 1499.0, "discount": 0.0}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_043",
        instruction="You are a Regional Manager handling a supplier transition. The supplier 'UrbanEdge' (SUP-1003) is being phased out. Consequently, all their products, specifically 'Men's Slim Fit Jeans - 34W 32L' and 'ArcticShield Men's Parka - Large', must be liquidated. First, update both product records to a 'discontinued' status. Then, consolidate all remaining physical stock of the parka from 'STORE-002' (a quantity of 6) by transferring it to a new inventory record at 'STORE-001' in the 'Liquidation Center'. After the transfer, create a final, aggressive 'percentage' promotion named 'UrbanEdge Final Sale' with a 70% discount on both items. The promotion's description must be 'Final sale on all discontinued UrbanEdge products.' and its initial usage count must be 0. It must be active from '2025-09-01' to '2025-09-30'. As a replacement, you are launching the 'UrbanExplorer Tech Jacket'. Repurpose the product record for 'Adventures in Sillytown' (BOOK-KDSSTY01) for this new jacket: update its name, category to 'Apparel', price to 219.99, and make it discountable. Finally, create new inventory records for this jacket at 'STORE-002' and 'STORE-003' in the 'New Arrivals' section and update their stock levels to 50 units each to prepare for the launch.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-SLFJEAN34", "status": "discontinued"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "status": "discontinued"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Liquidation Center"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 6, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}),
            Action(name="create_promotion", kwargs={
                "name": "UrbanEdge Final Sale", "type": "percentage", "discount_value": 70.0,
                "description": "Final sale on all discontinued UrbanEdge products.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-01", "end_date": "2025-09-30", "status": "active", "times_used": 0
            }),
            Action(name="update_product_details", kwargs={
                "sku": "BOOK-KDSSTY01", "name": "UrbanExplorer Tech Jacket", "category": "Apparel", "price": 219.99, "is_discountable": True
            }),
            Action(name="create_inventory_record", kwargs={"sku": "BOOK-KDSSTY01", "store_id": "STORE-002", "location": "New Arrivals"}),
            Action(name="create_inventory_record", kwargs={"sku": "BOOK-KDSSTY01", "store_id": "STORE-003", "location": "New Arrivals"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0026", "quantity_to_add": 50}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0027", "quantity_to_add": 50})
        ],
        outputs=[
            {"promotion_id": "PROMO-008", "name": "UrbanEdge Final Sale"},
            {"sku": "BOOK-KDSSTY01", "name": "UrbanExplorer Tech Jacket"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_044",
        instruction="You are a Marketing Director launching a new high-tech product, the 'Smart-Mirror'. Since no tool exists to create products, you must repurpose a discontinued item: 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Update its record to set the name to 'Smart-Mirror', category to 'Smart Home', price to 499.99, and make it discountable. Next, establish its initial inventory. A shipment of 100 units has arrived at the central warehouse ('STORE-001'); create an inventory record for the mirror there in 'Main Warehouse' and update its stock. To ensure widespread availability, immediately transfer 25 of these units to 'STORE-002' (you must create its inventory record first in 'Premium Tech'). To kickstart sales, you need to target high-value customers. First, get all SKUs from both the 'Electronics' and 'Smart Home' categories. Use these lists to find all 'gold' and 'platinum' customers who have ever purchased any of these items. For this target audience, create a new 'percentage' promotion named 'Smart-Mirror Launch Offer' with a 20% discount. The promotion's description must be 'An exclusive 20% off our new Smart-Mirror for top customers.' and it must be active for the next 15 days starting '2025-08-01'. Finally, generate unique, single-use promo codes for all identified customers.",
        actions=[
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "name": "Smart-Mirror", "category": "Smart Home", "price": 499.99, "is_discountable": True}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-001", "location": "Main Warehouse"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 100}),
            Action(name="create_inventory_record", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002", "location": "Premium Tech"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "CLTH-WINJKT01", "quantity": 25, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="get_products_by_category", kwargs={"category": "Smart Home"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["gold", "platinum"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04", "SMRT-THERM02"]
            }),
            Action(name="create_promotion", kwargs={
                "name": "Smart-Mirror Launch Offer", "type": "percentage", "discount_value": 20.0,
                "description": "An exclusive 20% off our new Smart-Mirror for top customers.",
                "applicable_skus": ["CLTH-WINJKT01"],
                "start_date": "2025-08-01", "end_date": "2025-08-15", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"})
        ],
        outputs=[
            {"codes_generated_for": ["CUST-5001", "CUST-5010"]}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_045",
        instruction="You are a CRM Manager. You've noticed that 'Liam Nguyen' (CUST-5002), a loyal 'silver' member, has surpassed the threshold for an upgrade. First, retrieve his customer details by name to confirm his current status. Immediately upgrade his membership level to 'gold' and add 250 bonus loyalty points to his account as a reward. To celebrate his new status, create a targeted 'percentage' promotion just for him. First, find all products in the 'Electronics' category. Then, create a promotion named 'New Gold Member Tech Deal' with a 15% discount applicable to all electronics. The promotion's description must be 'A special 15% off electronics to thank you for your loyalty.' and it must be active for the next 30 days starting from '2025-08-10', with an initial usage count of 0. Finally, generate a unique, single-use promo code for Liam and retrieve his customer details again to confirm his new status and point balance.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Liam Nguyen"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 250}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "New Gold Member Tech Deal", "type": "percentage", "discount_value": 15.0,
                "description": "A special 15% off electronics to thank you for your loyalty.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-10", "end_date": "2025-09-09", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[{"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1125}]
    ),
    Task(
        annotator="0",
        user_id="task_046",
        instruction="You are an Inventory Manager. The 'Organic Almond Butter 500g' (GROC-ALMBTR500) at 'STORE-001' is approaching its expiration date. First, retrieve this product's inventory record to check the current quantity. To prevent waste, you must move all units to clearance. Update the main product's status to 'clearance'. Then, create an aggressive 'percentage' promotion named 'Almond Butter Final Sale' with a 50% discount. The description must be '50% off! Must go before expiry.' and it should be active for 3 days starting today, '2025-08-11'. The promotion's initial usage count must be 0. After setting up the promotion, update the inventory item's status at 'STORE-001' to 'critical' to reflect the urgency. Finally, retrieve the updated product details and inventory details to confirm both status changes.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "Organic Almond Butter 500g"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"}),
            Action(name="update_product_details", kwargs={"sku": "GROC-ALMBTR500", "status": "clearance"}),
            Action(name="create_promotion", kwargs={
                "name": "Almond Butter Final Sale", "type": "percentage", "discount_value": 50.0,
                "description": "50% off! Must go before expiry.",
                "applicable_skus": ["GROC-ALMBTR500"],
                "start_date": "2025-08-11", "end_date": "2025-08-13", "status": "active", "times_used": 0
            }),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0007", "status": "critical"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "GROC-ALMBTR500"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"})
        ],
        outputs=[
            {"sku": "GROC-ALMBTR500", "status": "clearance"},
            {"id": "INV-0007", "status": "critical"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_047",
        instruction="You are a Marketing Manager. The 'Clearance Apparel Markdown' promotion (PROMO-005) has ended and must be decommissioned. First, retrieve its details by its ID to confirm its status. Deactivate the promotion. Now, you will repurpose this promotion ID for a new campaign. Update its details to become the 'Back to Office Essentials' sale: change the name, set the type to 'percentage' with a 20% discount, and update the description to '20% off select office supplies for your return to work.'. The new applicable product will be the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01). Before you add the SKU, you must get the product's details and update it to be 'is_discountable'. Set the new promotion to be 'scheduled' for the entire month of September 2025. Finally, retrieve the promotion by its ID 'PROMO-005' again to verify all the changes.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-005"}),
            Action(name="deactivate_promotion", kwargs={"promotion_id": "PROMO-005"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="update_product_details", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": True}),
            Action(name="update_promotion_details", kwargs={
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
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-005"})
        ],
        outputs=[{"promotion_id": "PROMO-005", "name": "Back to Office Essentials", "status": "scheduled"}]
    ),
    Task(
        annotator="0",
        user_id="task_048",
        instruction="You are an Inventory Specialist, 'Zoe Martinez', at 'STORE-004'. During an audit of 'TrailGuard Mountain Bike Helmet' (SPORT-BIKHLM01), you find that the 'reserved_quantity' is 1, but there are no actual customer reservations. You must correct this data. First, retrieve the full inventory record for this item at your store. Then, update the reserved quantity to 0; the instruction specifies the change amount is -1. After this correction, the available stock is now higher. Based on the store's policy, you must re-evaluate the item's status. Get the item's `safety_stock` level from its inventory record. Since the total quantity (4) is now greater than the `safety_stock` (3), update the inventory status from its current 'low_stock' to 'in_stock'. Finally, retrieve the inventory record again to confirm all changes.",
        actions=[
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0009", "change_amount": -1}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0009", "status": "in_stock"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"})
        ],
        outputs=[{"id": "INV-0009", "reserved_quantity": 0, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_049",
        instruction="You are 'Ethan Walker', a sales lead at 'STORE-002'. Customer 'Mia Kim' (CUST-5011) is in your store to return a 'ProSlice 8\" Chef Knife' (KITCH-CHEFKNF8) she received as a gift. She has no receipt, but she knows it was purchased on transaction 'TXN-0011'. The item is in perfect condition. First, find the transaction to confirm the purchase. Since the original payment method cannot be refunded without the original card, the store policy is to issue the credit as loyalty points. Retrieve the product's current price to determine the point value; the policy specifies rounding any decimal value up to the nearest whole number. Then, update the customer's loyalty points with this amount. Finally, you must return the item to stock. Get the inventory ID for the knife at your store and update its stock level by adding 1 unit. Retrieve the customer's details to confirm her new loyalty point balance.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Mia Kim"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ProSlice 8\" Chef Knife"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5011", "sku": "KITCH-CHEFKNF8"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "KITCH-CHEFKNF8"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 40}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0011", "quantity_to_add": 1}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[{"customer_id": "CUST-5011", "loyalty_points": 600}]
    ),
    Task(
        annotator="0",
        user_id="task_050",
        instruction="You are a Marketing Specialist. You've noticed the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02) is mis-categorized as 'Smart Home'. It should be in the 'Electronics' category. First, retrieve the product's details to see its current category. Then, update the product to place it in the 'Electronics' category. To celebrate the fix, you will immediately launch a flash sale. Create a new 'percentage' promotion named 'Thermostat Flash Sale' with a 20% discount. The description must be '24-hour flash sale on our EcoSmart Thermostat!' and it must be active for today only, '2025-08-14', with an initial usage count of 0. Finally, retrieve all promotions that have an 'active' status flag to ensure your new flash sale is listed.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "SMRT-THERM02"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "SMRT-THERM02", "category": "Electronics"}
            ),
            Action(
                name="create_promotion",
                kwargs={
                    "name": "Thermostat Flash Sale", "type": "percentage", "discount_value": 20.0,
                    "description": "24-hour flash sale on our EcoSmart Thermostat!",
                    "applicable_skus": ["SMRT-THERM02"],
                    "start_date": "2025-08-14", "end_date": "2025-08-14", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="get_promotions_by_status",
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
        instruction="You are 'Isabella Rossi', a sales lead at 'STORE-002'. Customer 'Ava Thompson' wants to buy the 'TrailGuard Mountain Bike Helmet' (SPORT-BIKHLM01). Your store is out of stock. First, confirm this by checking your local inventory. Then, check the inventory at 'STORE-004', where you believe there is stock. Inform the customer you can have it transferred. You must create an inventory record for the helmet at your store ('STORE-002', location 'Store Transfer Area') before executing the transfer of 1 unit from 'STORE-004'. After the transfer succeeds, update the status of the new inventory item at your store to 'in_stock'. Now, process the sale for Ava Thompson using a 'credit_card'. The instruction specifies a payment by 'credit_card'. There are no promotions. Calculate the totals, create the transaction, and update the inventory at your store, using today's date, '2025-08-12', for the last stock count date. Return the transaction ID.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "TrailGuard Mountain Bike Helmet"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-004"}),
            Action(name="create_inventory_record", kwargs={"sku": "SPORT-BIKHLM01", "store_id": "STORE-002", "location": "Store Transfer Area"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "SPORT-BIKHLM01", "quantity": 1, "from_store_id": "STORE-004", "to_store_id": "STORE-002"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Ava Thompson"}),
            Action(name="calculate_transaction_totals", kwargs={"line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 1}]}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Isabella Rossi"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5001", "payment_method": "credit_card",
                "total_amount": 96.34, "tax_amount": 7.34, "discount_total": 0.0,
                "line_items": [{"sku": "SPORT-BIKHLM01", "quantity": 1, "unit_price": 89.0, "discount": 0.0}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0025", "quantity_sold": 1, "last_stock_count_date": "2025-08-12"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_052",
        instruction="You are 'Daniel Perez', a customer service rep at 'STORE-001'. 'Benjamin Cohen' (CUST-5010) calls regarding transaction 'TXN-0010'. He believes he was charged the wrong unit price for his 'WaveSound All-Weather Bluetooth Speaker', thinking it should have been $125.00. Your first step is to find the transaction using his customer ID and the product SKU to verify the unit_price he was actually charged. After clarifying the price, and as an apology for the confusion, add 100 loyalty points to his account. To further ensure his satisfaction, create a new 'percentage' promotion for him named 'Electronics Apology' with a 15% discount applicable to all products in the 'Electronics' category. The description must be 'A 15% discount on our electronics as a token of our apology.' and it must be active for 90 days starting today, '2025-08-13', with an initial usage count of 0. Finally, generate a unique promo code for Mr. Cohen and retrieve his customer details to confirm his new loyalty point balance.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "WaveSound All-Weather Bluetooth Speaker"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5010", "points_to_add": 100}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "Electronics Apology", "type": "percentage", "discount_value": 15.0,
                "description": "A 15% discount on our electronics as a token of our apology.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-13", "end_date": "2025-11-11", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "loyalty_points": 1125}]
    ),
    Task(
        annotator="0",
        user_id="task_053",
        instruction="You are a Regional Manager. You've noticed that 'STORE-004' is underperforming in the 'Sports & Outdoors' category. To boost its sales, you decide to transfer a popular item, the 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01), from 'STORE-001', which has ample stock. First, confirm the stock at 'STORE-001'. Then, create a new inventory record for the mat at 'STORE-004' in location 'Featured Products Aisle' and transfer 25 units. Next, to promote this new stock, you will target 'platinum' customers who have previously purchased 'Sports & Outdoors' items. Find these customers. Then, create a 'percentage' promotion named 'STORE-004 Sports Special' with a 25% discount on the yoga mat, exclusive to that store. The description must be 'A special offer for our top sports customers at STORE-004.' and it must be active for the last week of August 2025, with an initial usage count of 0. Finally, generate unique promo codes for the identified customers.",
        actions=[
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-004", "location": "Featured Products Aisle"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 25, "from_store_id": "STORE-001", "to_store_id": "STORE-004"}),
            Action(name="get_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="find_customers_by_criteria", kwargs={"membership_levels": ["platinum"], "purchase_history_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"]}),
            Action(name="create_promotion", kwargs={
                "name": "STORE-004 Sports Special", "type": "percentage", "discount_value": 25.0,
                "description": "A special offer for our top sports customers at STORE-004.",
                "applicable_skus": ["SPORT-YOGMAT01"],
                "start_date": "2025-08-25", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"})
        ],
        outputs=[{"codes_generated_for": ["CUST-5004"]}]
    ),
    Task(
        annotator="0",
        user_id="task_054",
        instruction="You are 'Isabella Rossi', a sales associate at 'STORE-002'. A new customer, 'David Chen', wants to purchase the 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and an 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). First, create a new customer account for him with 'basic' membership, 0 loyalty points, and marketing opt-out. Next, check the inventory for both items at your store. You recall there might be a promotion. Check for any 'active' promotions by the name 'Clearance Apparel Markdown' for today's date, '2025-06-20'. If it is active, calculate the transaction totals, applying the promotion to both items. The customer will pay with a 'debit_card'. Process the sale by creating the transaction and updating the stock for both items sold.",
        actions=[
            Action(name="create_customer", kwargs={"name": "David Chen", "membership_level": "basic", "opt_in_marketing": False, "loyalty_points": 0}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-20"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "CLTH-SLFJEAN34", "quantity": 1}, {"sku": "CLTH-WINJKT01", "quantity": 1}],
                "promotion_ids": ["PROMO-005"]
            }),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Isabella Rossi"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5013", "payment_method": "debit_card",
                "total_amount": 194.04, "tax_amount": 14.79, "discount_total": 59.75,
                "line_items": [
                    {"sku": "CLTH-SLFJEAN34", "quantity": 1, "unit_price": 49.5, "discount": 12.38},
                    {"sku": "CLTH-WINJKT01", "quantity": 1, "unit_price": 189.5, "discount": 47.38}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0005", "quantity_sold": 1, "last_stock_count_date": "2025-06-20"}),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-06-20"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_055",
        instruction="You are a Marketing Manager. The 'Kitchen Essentials Bundle' (PROMO-002) is ending today, '2025-07-15'. Your task is to deactivate it and immediately launch an enhanced version for the upcoming holiday season. First, retrieve the promotion by its ID to check its 'times_used' count. Then, deactivate it. Next, you will create a new promotion named 'Kitchen Upgrade Bundle'. This will be a 'fixed_bundle' promotion with an increased discount of $20.00. The description must be 'Upgrade your kitchen with this premium bundle for the holidays.'. It will include the original items ('HOM-COFMKR12', 'KITCH-CHEFKNF8') plus the 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). The new promotion should be 'scheduled' to run from '2025-11-01' to '2025-12-31', with an initial usage count of 0. Finally, retrieve the new promotion by its ID to confirm its creation.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="deactivate_promotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ChefPro Ceramic Fry Pan 10\""}),
            Action(name="create_promotion", kwargs={
                "name": "Kitchen Upgrade Bundle", "type": "fixed_bundle", "discount_value": 20.0,
                "description": "Upgrade your kitchen with this premium bundle for the holidays.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-11-01", "end_date": "2025-12-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-002", "status": "inactive"}, {"promotion_id": "PROMO-008", "name": "Kitchen Upgrade Bundle"}]
    ),
    Task(
        annotator="0",
        user_id="task_056",
        instruction="You are a sales lead, 'Daniel Perez'. You have convinced a long-time customer, 'Benjamin Cohen' (CUST-5010), who had previously opted out of marketing, to opt in. Your first action is to retrieve his customer details to confirm his current opt-out status. Then, update his record to set 'opt_in_marketing' to true. As a thank you for opting in, your manager has authorized you to create a special one-time discount for him. Find all products in his favorite category, 'Electronics'. Create a new 'fixed_amount' promotion named 'Ben's Opt-in Reward' that provides a $25.00 discount on any of these electronic items. The description must be 'A special thank you for joining our marketing list.' and it should be active for 60 days starting '2025-08-16', with an initial usage count of 0. Finally, generate a unique promo code for him and retrieve his details again to confirm his opt-in status.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "Ben's Opt-in Reward", "type": "fixed_amount", "discount_value": 25.0,
                "description": "A special thank you for joining our marketing list.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-16", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_057",
        instruction="You are an Inventory Specialist preparing for the holiday season. The 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) is expected to be a top seller. You've noticed that stock is split between 'STORE-001' (quantity: 45) and 'STORE-003' (where it is not currently stocked). Your goal is to consolidate all stock at the main warehouse, 'STORE-001'. First, create an inventory record for the lamp at 'STORE-003' in location 'Overstock', as one is needed for the transfer. Then, transfer all 15 units of the lamp from 'STORE-003' to 'STORE-001'. You must get the inventory records for both the source and destination before the transfer to get their IDs. After the transfer, the inventory record at 'STORE-003' will be empty and is no longer needed; update its status to 'discontinued'. Finally, retrieve the inventory record for the lamp at 'STORE-001' to confirm its new, higher quantity.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-003", "location": "Overstock"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 15}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOME-DESKLMP01", "quantity": 15, "from_store_id": "STORE-003", "to_store_id": "STORE-001"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "discontinued"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0015", "quantity": 60}]
    ),
    Task(
        annotator="0",
        user_id="task_058",
        instruction="You are a Data Analyst. You have found a data integrity issue: the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is in the 'Office Supplies' category, but it should be in a more specific 'Furniture' category. Your task is to correct this. First, retrieve the product by its SKU to verify its current category. Then, update the product's category to 'Furniture'. As this is a high-value item, the company wants to ensure it's eligible for all major sales. Retrieve the product's details again to confirm the category change, and if the 'is_discountable' flag is false, update it to be true. Finally, as a test, find all products that are now in the 'Furniture' category to ensure your update was successful.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="update_product_details", kwargs={"sku": "OFFC-ERGCHR01", "category": "Furniture"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="update_product_details", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": True}),
            Action(name="get_products_by_category", kwargs={"category": "Furniture"})
        ],
        outputs=[{"sku": "OFFC-ERGCHR01", "category": "Furniture", "is_discountable": True}]
    ),
    Task(
        annotator="0",
        user_id="task_059",
        instruction="You are the Inventory Manager for 'STORE-003'. Your store needs to begin stocking the popular 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), which is currently stocked at the main warehouse, 'STORE-001'. Your task is to establish an initial stock level. First, confirm the item is in stock at 'STORE-001' by retrieving its inventory record. Next, create a new inventory record for the coffee maker at your store ('STORE-003') in location 'Aisle 4'. After the new record is created, execute a transfer of 15 units from 'STORE-001' to your store. Because this is a new, fully-stocked item, you must then update the status of your new inventory record from its default to 'in_stock'. Finally, retrieve the new inventory record from your store to confirm that the quantity is 15 and the status is correct.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "location": "Aisle 4"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 15, "from_store_id": "STORE-001", "to_store_id": "STORE-003"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 15, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_060",
        instruction="You are 'Isabella Rossi', a sales associate at 'STORE-002'. A customer, 'William Zhang', wants to buy your entire remaining stock of the 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). First, retrieve the inventory record for this parka at your store to confirm the exact quantity available (which is 6). The customer has also decided to upgrade his membership. Update his customer record from 'silver' to 'gold'. Now, process the sale for all 6 parkas. The payment method must be 'credit_card'. There is an active 'Clearance Apparel Markdown' promotion (PROMO-005) which you must check for today's date, '2025-06-25'. Calculate the total cost including this discount. After creating the transaction, you must immediately update the parka's inventory status to 'out_of_stock'. Finally, confirm the customer's new membership level.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "William Zhang"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-25"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6}],
                "promotion_ids": ["PROMO-005"]
            }),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Isabella Rossi"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5006", "payment_method": "credit_card",
                "total_amount": 923.10, "tax_amount": 70.35, "discount_total": 284.25,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6, "unit_price": 189.5, "discount": 47.38}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 6, "last_stock_count_date": "2025-06-25"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0022", "status": "out_of_stock"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
        Task(
        annotator="0",
        user_id="task_107",
        instruction="You are 'Natalie Cooper', a customer service lead. A customer, 'Olivia Patel' (CUST-5003), is calling to update her personal information. First, retrieve her current customer record to verify her old details. Then, update her record to reflect her new married name, 'Olivia Williams', and her new address, '456 Oak Avenue, Springfield, IL, 62704'. As a thank you for keeping her details current, offer her a special promotion. Based on her purchase history in the 'Grocery' category, create a new 'percentage' promotion named 'Valued Customer Grocery Offer' with a 15% discount on all items in that category. The description must be 'A 15% discount on groceries for our valued customers.' The promotion ('PROMO-008') must be active for the next 30 days starting '2025-07-30' with an initial usage count of 0. Before creating the promotion, you must ensure all grocery items are discountable. Finally, generate a unique promo code for Olivia and retrieve her customer details again to confirm the update.",
        actions=[
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5003"}
            ),
            Action(
                name="update_customer_details",
                kwargs={
                    "customer_id": "CUST-5003",
                    "name": "Olivia Williams",
                    "address": "456 Oak Avenue, Springfield, IL, 62704"
                }
            ),
            Action(
                name="get_products_by_category",
                kwargs={"category": "Grocery"}
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-ALMBTR500"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "GROC-ALMBTR500", "is_discountable": True}
            ),
            Action(
                name="create_promotion",
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
                name="generate_and_assign_promo_codes",
                kwargs={"customer_ids": ["CUST-5003"], "promotion_id": "PROMO-008"}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5003"}
            )
        ],
        outputs=[
            {
                "customer_id": "CUST-5003",
                "name": "Olivia Williams",
                "address": "456 Oak Avenue, Springfield, IL, 62704"
            }
        ]
    ),
    Task(
        annotator="0",
        user_id="task_062",
        instruction="You are 'Grace Miller' at 'STORE-001'. Today is '2025-06-10', the first day of the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003). A customer, 'Sophia Rossi', wants to buy two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01). First, you must get the promotion by its ID and change its status from 'scheduled' to 'active'. Then, check the inventory for the mats at your store to ensure at least two are available. Next, process the sale for Sophia using 'mobile_wallet'. You must construct the final transaction based on the following: the price of one mat is $29.99, the 50% discount on the second mat is $15.00. The final total amount is $48.71, the tax is $3.71, and the total discount is $15.00. Create the transaction, update the inventory, and increment the promotion's 'times_used' count by one.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="activate_promotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "FlexFit Premium Yoga Mat"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Sophia Rossi"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Grace Miller"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1002", "customer_id": "CUST-5007", "payment_method": "mobile_wallet",
                "total_amount": 48.71, "tax_amount": 3.71, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-06-10"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_063",
        instruction="You are the Marketing Director. You want to reward your top customers in the 'Home & Kitchen' category. First, get all products belonging to the 'Home & Kitchen' category. Then, using this list, find all 'silver' customers who have purchased any of these items. For each of the silver-level customers identified, add 200 bonus loyalty points to their accounts as a reward for their business. To confirm the updates, retrieve the full customer details for 'Liam Nguyen' and 'William Zhang' after their points have been added.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["silver"],
                "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
            }),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 200}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "loyalty_points": 1075},
            {"customer_id": "CUST-5006", "loyalty_points": 1180}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_064",
        instruction="You are the inventory manager, 'Zoe Martinez'. A system audit reveals stock discrepancies for the 'BrewMaster 12-Cup Coffee Maker'. At 'STORE-001', the system shows 25 units, but a physical count confirms only 22. At 'STORE-003', the item is not normally stocked, but a mis-delivered pallet of 15 units has been discovered. Your task is to correct the inventory in the system. First, correct the stock at 'STORE-001' to reflect the physical count. Then, create a new inventory record for the coffee maker at 'STORE-003' in location 'Receiving Dock' and update its stock level to 15. To help sell the now correctly accounted-for items, create a new 'fixed_bundle' promotion named 'Morning Brew Bundle' with a $10.00 discount. The description must be 'A special deal on our coffee maker and granola bars.' and it should apply when 'BrewMaster 12-Cup Coffee Maker' and 'High-Protein Granola Bars (12 Pack)' are bought together. Schedule this promotion to be active for the entire month of October 2025.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "High-Protein Granola Bars (12 Pack)"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -3}),
            Action(name="create_inventory_record", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003", "location": "Receiving Dock"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 15}),
            Action(name="create_promotion", kwargs={
                "name": "Morning Brew Bundle", "type": "fixed_bundle", "discount_value": 10.0,
                "description": "A special deal on our coffee maker and granola bars.",
                "applicable_skus": ["HOM-COFMKR12", "GROC-GRNLBR12"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-003"})
        ],
        outputs=[
            {"id": "INV-0003", "quantity": 22},
            {"id": "INV-0025", "quantity": 15}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_065",
        instruction="You are a CRM Manager. You need to run a campaign to reactivate dormant 'platinum' customers. Your target is 'Noah Johnson', whose last transaction was 'TXN-0004' on 2025-06-05. First, retrieve his customer details using his name to confirm his status. Update his status to 'inactive' to mark him as dormant. To win him back, you will create a personalized offer. Find all products in his favorite category, 'Sports & Outdoors'. Create a new 'percentage' promotion named 'Welcome Back, Noah!' with a 30% discount on all 'Sports & Outdoors' products. The description must be 'A special 30% off just for you, Noah!'. It must be active from '2025-08-20' to '2025-09-04', with an initial usage count of 0. Generate a unique promo code for him. Finally, update his status back to 'active' and retrieve his details to confirm.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Noah Johnson"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5004"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5004", "status": "inactive"}),
            Action(name="get_products_by_category", kwargs={"category": "Sports & Outdoors"}),
            Action(name="create_promotion", kwargs={
                "name": "Welcome Back, Noah!", "type": "percentage", "discount_value": 30.0,
                "description": "A special 30% off just for you, Noah!",
                "applicable_skus": ["SPORT-BIKHLM01", "SPORT-YOGMAT01"],
                "start_date": "2025-08-20", "end_date": "2025-09-04", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5004"], "promotion_id": "PROMO-008"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5004", "status": "active"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5004"})
        ],
        outputs=[{"customer_id": "CUST-5004", "status": "active"}]
    ),
    Task(
        annotator="0",
        user_id="task_066",
        instruction="You are an Inventory Manager. Supplier 'UrbanEdge' (SUP-1003) has gone out of business. You must liquidate all their products. Their products are 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). First, update both main product records to change their status to 'discontinued'. Next, find all inventory records for these products; you know they are stocked at 'STORE-002'. Update the status of both inventory records to 'clearance'. To sell the remaining stock quickly, create a single 'percentage' promotion named 'UrbanEdge Final Liquidation' with a 60% discount. The description must be 'Everything from UrbanEdge must go! 60% off.' and it must be active for one week starting today, '2025-08-21', with an initial usage count of 0. Finally, retrieve both inventory records from 'STORE-002' to confirm their 'clearance' status.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-SLFJEAN34", "status": "discontinued"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "status": "discontinued"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0005", "status": "clearance"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0022", "status": "clearance"}),
            Action(name="create_promotion", kwargs={
                "name": "UrbanEdge Final Liquidation", "type": "percentage", "discount_value": 60.0,
                "description": "Everything from UrbanEdge must go! 60% off.",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-08-21", "end_date": "2025-08-28", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0005", "status": "clearance"}, {"id": "INV-0022", "status": "clearance"}]
    ),
    Task(
        annotator="0",
        user_id="task_067",
        instruction="You are the Customer Service Lead. 'Liam Nguyen' (CUST-5002) calls about transaction 'TXN-0002'. He purchased a 'BrewMaster 12-Cup Coffee Maker' and a 'ProSlice 8\" Chef Knife' and believes the 'Kitchen Essentials Bundle' promotion (PROMO-002) should have been applied but was missed by the cashier. First, retrieve the promotion by its ID to confirm its discount value is $15.00. Then, find the customer's details by his name. Since you cannot alter a past transaction, you must compensate him by adding loyalty points equivalent to the missed discount value ($15.00). Update his loyalty points. As a further apology, you will create a new 'fixed_amount' promotion for $10.00 off his next purchase. The promotion should be named 'We're Sorry Discount', with a description 'A $10 voucher for our error.' It should be active for 90 days from today, '2025-08-22', and apply to all products in the 'Home & Kitchen' category. The initial usage count must be 0. Finally, generate a code for him and confirm his new loyalty point total.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Liam Nguyen"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 15}),
            Action(name="get_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="create_promotion", kwargs={
                "name": "We're Sorry Discount", "type": "fixed_amount", "discount_value": 10.0,
                "description": "A $10 voucher for our error.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"],
                "start_date": "2025-08-22", "end_date": "2025-11-20", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[{"customer_id": "CUST-5002", "loyalty_points": 890}]
    ),
    Task(
        annotator="0",
        user_id="task_068",
        instruction="You are the Marketing Director. You are setting up a multi-tiered 'Buy More, Save More' weekend sale for the 'Apparel' category, active from '2025-09-05' to '2025-09-07'. You must create two distinct promotions. First, get all SKUs for the 'Apparel' category. The first promotion, named 'Apparel Deal - 15% Off', must be a 'percentage' discount of 15.0%, with description 'Buy 2+ apparel items and get 15% off!'. The second promotion, named 'Apparel Deal - 25% Off', must be a 'percentage' discount of 25.0%, with description 'Buy 3+ apparel items and get 25% off!'. Both promotions must apply to all apparel SKUs, have a start/end date matching the sale, and have their initial usage counts set to 0. After creating both, retrieve all promotions with a 'scheduled' status to confirm they were created correctly.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Apparel"}),
            Action(name="create_promotion", kwargs={
                "name": "Apparel Deal - 15% Off", "type": "percentage", "discount_value": 15.0,
                "description": "Buy 2+ apparel items and get 15% off!",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-05", "end_date": "2025-09-07", "status": "scheduled", "times_used": 0
            }),
            Action(name="create_promotion", kwargs={
                "name": "Apparel Deal - 25% Off", "type": "percentage", "discount_value": 25.0,
                "description": "Buy 3+ apparel items and get 25% off!",
                "applicable_skus": ["CLTH-SLFJEAN34", "CLTH-WINJKT01"],
                "start_date": "2025-09-05", "end_date": "2025-09-07", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_promotions_by_status", kwargs={"status": "scheduled"})
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
        instruction="You are 'Daniel Perez', a senior customer service representative. A loyal 'silver' tier customer, 'Liam Nguyen', calls regarding his recent transaction, 'TXN-0002'. He feels the discount from the 'Kitchen Essentials Bundle' promotion was not substantial enough. Your goal is to resolve this to his satisfaction. First, confirm the customer's current details and the details of the promotion he used ('PROMO-002'). As a gesture of goodwill, add 150 bonus loyalty points to his account. You notice this pushes his point total over 1000, making him eligible for an upgrade; update his membership level to 'gold'. To celebrate his new status, create a new personalized 'percentage' promotion named 'Gold Member Welcome Offer' with a 20% discount on all 'Electronics' products. The description must be 'A special electronics discount for our new Gold member.' and it must be active for 60 days starting '2025-08-01'. Finally, generate a unique, single-use promo code for Liam and retrieve his customer details again to confirm his new status and point balance.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Liam Nguyen"}),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 150}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "Gold Member Welcome Offer", "type": "percentage", "discount_value": 20.0,
                "description": "A special electronics discount for our new Gold member.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-01", "end_date": "2025-09-29", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5002"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "membership_level": "gold", "loyalty_points": 1025}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_070",
        instruction="You are 'Megan Young', the manager of 'STORE-005'. You are running a clearance on the 'WaveSound All-Weather Bluetooth Speaker' (AUDIO-BTSPKR02) and need to update the contact information for a loyal customer, 'Benjamin Cohen'. First, retrieve the inventory details for the speaker at 'STORE-005' to confirm the current quantity. Then, update the main product's status to 'clearance'. Next, find the customer 'Benjamin Cohen' by name and update his address to '22 Mountain View Rd, Portland, OR, 97205' and his phone number to '+1-555-0999-1111'. As a thank you to this loyal customer, create a new, exclusive 'fixed_amount' promotion for him named 'Valued Customer Credit' for $20.00 off. The description must be 'A $20 credit for being a loyal customer.' and it should be active for 30 days starting '2025-08-27', with an initial usage count of 0 and applicable only to the speaker. Finally, generate a unique promo code for him and retrieve his customer details to confirm the address update.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "WaveSound All-Weather Bluetooth Speaker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "AUDIO-BTSPKR02", "store_id": "STORE-005"}),
            Action(name="update_product_details", kwargs={"sku": "AUDIO-BTSPKR02", "status": "clearance"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="update_customer_details", kwargs={
                "customer_id": "CUST-5010",
                "address": "22 Mountain View Rd, Portland, OR, 97205",
                "phone_number": "+1-555-0999-1111"
            }),
            Action(name="create_promotion", kwargs={
                "name": "Valued Customer Credit", "type": "fixed_amount", "discount_value": 20.0,
                "description": "A $20 credit for being a loyal customer.",
                "applicable_skus": ["AUDIO-BTSPKR02"],
                "start_date": "2025-08-27", "end_date": "2025-09-26", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "address": "22 Mountain View Rd, Portland, OR, 97205"}]
    ),
    Task(
        annotator="task_071",
        user_id="task_071",
        instruction="You are an Inventory Specialist. An audit of 'STORE-001' reveals a data error for the 'UltraVision 55\" 4K Smart TV' (INV-0001). The system shows 8 units in stock with 2 reserved, but a physical count confirms there are actually 9 units, and all reservations have been cancelled. You must make two corrections. First, update the stock level by adding 1 unit. Second, update the reserved quantity to 0; the required change_amount is -2. After these corrections, the available stock is now 9. You must re-evaluate the inventory status based on policy. Retrieve the inventory record again to get its 'reorder_level' (3) and 'safety_stock' (2). Since the new quantity of 9 is well above these thresholds, update the item's status to 'in_stock'. Finally, retrieve the record a last time to confirm all corrections.",
        actions=[
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0001", "change_amount": -2}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0001", "status": "in_stock"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0001", "quantity": 9, "reserved_quantity": 0, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_072",
        instruction="You are a Regional Manager. Stock for the 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01) is fragmented, with the main supply at 'STORE-001' and a small amount at 'STORE-004'. You want to consolidate it all at 'STORE-001'. First, ensure an inventory record exists at 'STORE-004' in location 'Temp Holding' and has a quantity of 10. Then, transfer all 10 units from 'STORE-004' to 'STORE-001'. After the transfer, the inventory record at 'STORE-004' is now empty and obsolete; update its status to 'discontinued'. To boost sales of the newly consolidated stock, create a 'percentage' promotion named 'Yoga Mat Stock-Up Sale' with a 10% discount. The description must be 'Freshly stocked! Get our premium yoga mats for 10% off.' The sale must be active for the rest of the month, starting today '2025-08-26', with an initial usage count of 0. Finally, retrieve the 'STORE-001' inventory record to confirm its new, higher quantity.",
        actions=[
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-004", "location": "Temp Holding"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0025", "quantity_to_add": 10}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "SPORT-YOGMAT01", "quantity": 10, "from_store_id": "STORE-004", "to_store_id": "STORE-001"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "discontinued"}),
            Action(name="create_promotion", kwargs={
                "name": "Yoga Mat Stock-Up Sale", "type": "percentage", "discount_value": 10.0,
                "description": "Freshly stocked! Get our premium yoga mats for 10% off.",
                "applicable_skus": ["SPORT-YOGMAT01"],
                "start_date": "2025-08-26", "end_date": "2025-08-31", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0021", "quantity": 70}]
    ),
    Task(
        annotator="0",
        user_id="task_105",
        instruction="You are a manager, 'Megan Young', handling a product recall for the 'PowerPlus Rechargeable AA Batteries (4 Pack)'. First, you must update the main product's status to 'recalled'. Then, find its inventory record at 'STORE-003' and update its status to 'recalled' as well. Next, as a proactive measure, you must remove the recalled item from any active promotions. Find the 'Summer Electronics Sale' promotion, which is active today, '2025-07-29'. Retrieve its details, including its current list of applicable SKUs. Then, update the promotion by removing the recalled product's SKU ('ELEC-RCHAA04') from its list of applicable SKUs. Finally, to compensate high-value customers, find all 'gold' tier customers who have ever purchased the recalled item. For each customer found, add 500 loyalty points to their account as an apology and retrieve the updated customer details for 'Ava Thompson' to confirm.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "PowerPlus Rechargeable AA Batteries (4 Pack)"}),
            Action(name="update_product_details", kwargs={"sku": "ELEC-RCHAA04", "status": "recalled"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-RCHAA04", "store_id": "STORE-003"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0020", "status": "recalled"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-07-29"}),
            Action(name="update_promotion_details", kwargs={
                "promotion_id": "PROMO-001",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15"]
            }),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["gold"],
                "purchase_history_skus": ["ELEC-RCHAA04"]
            }),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 500}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5010", "points_to_add": 500}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[
            {"customer_id": "CUST-5001", "loyalty_points": 1740}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_074",
        instruction="You are the Inventory Manager for 'STORE-002'. Your store needs to begin stocking the popular 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), which is currently stocked at 'STORE-001'. You already have a pre-order for 5 units. Your task is to establish the inventory and log the pre-order. First, confirm the item is in stock at 'STORE-001'. Next, create a new inventory record for the coffee maker at your store ('STORE-002') in location 'Aisle 12'. Immediately after creation, update this new record's 'reserved_quantity' by an amount of 5 to account for the pre-order. Then, execute a transfer of 20 units from 'STORE-001' to your store. Finally, update the status of your new inventory to 'in_stock' and retrieve it to confirm the final quantity is 20 and reserved quantity is 5.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002", "location": "Aisle 12"}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0025", "change_amount": 5}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 20, "reserved_quantity": 5, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_075",
        instruction="You are an Inventory Auditor for 'STORE-001'. You have completed a physical stock count and found several discrepancies with the system. For 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), the count is 9 units (system: 8). For 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), the count is 22 units (system: 25). For 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01), the count is 58 units (system: 60). Your task is to correct the system's inventory quantities to match the physical count by applying the specified change amounts: TV (+1), Coffee Maker (-3), and Yoga Mat (-2). First, retrieve the current inventory record for each SKU at 'STORE-001'. Then, apply the corrections. Finally, retrieve all three inventory records again to confirm the final quantities are 9, 22, and 58 respectively.",
        actions=[
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0001", "quantity_to_add": 1}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0003", "quantity_to_add": -3}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0021", "quantity_to_add": -2}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
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
        instruction="You are a Customer Service Lead. A 'gold' tier customer, 'Ava Thompson' (CUST-5001), calls to complain. She recently made a purchase ('TXN-0001') where the 'Summer Electronics Sale' promotion ('PROMO-001') was applied, but she feels the 10% discount was not sufficient for her loyalty. Your task is to appease her. First, retrieve her customer details to confirm her status. Then, retrieve the details of the promotion she used to understand its terms. As a gesture of goodwill, add 200 bonus loyalty points to her account. Furthermore, create a new, exclusive 'fixed_amount' promotion just for her, named 'Valued Gold Member Credit', for $25.00 off any 'Electronics' product. The description must be 'A $25 credit as a thank you for your loyalty.', it must be active for 90 days from today, '2025-09-02', with an initial usage count of 0. Finally, generate a unique promo code for her and retrieve her customer details again to confirm her new point balance.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Ava Thompson"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5001"}),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-001"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 200}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "Valued Gold Member Credit", "type": "fixed_amount", "discount_value": 25.00,
                "description": "A $25 credit as a thank you for your loyalty.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-09-02", "end_date": "2025-12-01", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5001"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1440}]
    ),
    Task(
        annotator="0",
        user_id="task_077",
        instruction="You are a Regional Manager preparing for the grand opening of a new location, 'STORE-006'. Your task is to create its initial key inventory by transferring stock from the main warehouse, 'STORE-001'. The required items and quantities are: 5 units of 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55), 20 units of 'BrewMaster 12-Cup Coffee Maker' (HOM-COFMKR12), and 50 units of 'UltraSoft Cotton Bath Towel' (HOME-BTHTWL01). For each of the three items, you must first create a new inventory record at 'STORE-006' in location 'Main Floor'. Then, execute the transfer of the specified quantity from 'STORE-001'. Finally, retrieve all three new inventory records from 'STORE-006' to confirm the successful setup.",
        actions=[
            Action(name="create_inventory_record", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "ELEC-4KTV55", "quantity": 5, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-006", "location": "Main Floor"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOME-BTHTWL01", "quantity": 50, "from_store_id": "STORE-001", "to_store_id": "STORE-006"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "ELEC-4KTV55", "store_id": "STORE-006"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-006"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-BTHTWL01", "store_id": "STORE-006"}),
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
        instruction="You are a Data Hygiene Specialist. Your task is to clean up several customer accounts based on a provided list. Customer 'James O'Connor' has closed his account; you must update his status to 'inactive'. Customer 'Logan Smith' has also closed his account; update his status to 'inactive' as well. Finally, customer 'Emma García' has accumulated enough points for an upgrade; update her membership level to 'silver'. The instruction specifies you must find each customer by their name to get their ID before performing the update. To conclude, retrieve the full records for 'James O'Connor' and 'Emma García' to confirm their new statuses.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "James O'Connor"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5008", "status": "inactive"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Logan Smith"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5012", "status": "inactive"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Emma García"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5005", "membership_level": "silver"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5005"})
        ],
        outputs=[
            {"customer_id": "CUST-5008", "status": "inactive"},
            {"customer_id": "CUST-5005", "membership_level": "silver"}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_079",
        instruction="You are a Product Safety Manager. A recall has been issued for the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02). Your first step is to update the main product record to a status of 'recalled'. Then, find the inventory record for this SKU at its stocking store, 'STORE-002', and update its status to 'recalled' as well. Next, you must identify all customers across all membership levels ('gold', 'platinum', 'silver', 'bronze', 'basic') who have purchased this item. The transaction logs show 'CUST-5011' bought one. You need to ensure you can contact this customer. Retrieve the customer record for 'Mia Kim' (CUST-5011) to check her marketing opt-in status. If she has opted out, you must override this for safety reasons by updating her 'opt_in_marketing' status to true. Finally, retrieve her record again to confirm the contact status has been enabled.",
        actions=[
            Action(
                name="update_product_details",
                kwargs={"sku": "SMRT-THERM02", "status": "recalled"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "SMRT-THERM02", "store_id": "STORE-002"}
            ),
            Action(
                name="update_inventory_status",
                kwargs={"inventory_id": "INV-0019", "status": "recalled"}
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "purchase_history_skus": ["SMRT-THERM02"],
                    "membership_levels": ["gold", "platinum", "silver", "bronze", "basic"]
                }
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5011"}
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5011", "opt_in_marketing": True}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5011"}
            )
        ],
        outputs=[{"customer_id": "CUST-5011", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_080",
        instruction="You are a Data Analyst preparing for a site-wide sale. All products from the supplier 'UrbanEdge' must be marked as discountable. The products are 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) and 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). Your task is to check each product and, if it is not currently discountable, update its status to 'is_discountable: true'. Finally, retrieve the details for both products again to confirm they are both marked as discountable.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-SLFJEAN34", "is_discountable": True}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-WINJKT01"}),
            Action(name="update_product_details", kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-WINJKT01"}),
        ],
        outputs=[
            {"sku": "CLTH-SLFJEAN34", "is_discountable": True},
            {"sku": "CLTH-WINJKT01", "is_discountable": True}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_081",
        instruction="You are a Marketing Analyst setting up an A/B test. You need to create two different promotions for the same set of products to see which is more effective. The target products are all items in the 'Grocery' category. First, get the list of all grocery SKUs. Promotion A, named 'Grocery Discount 10%', should be a 'percentage' discount of 10.0 with the description 'Test A: 10% off all grocery items.' Promotion B, named 'Grocery Discount $5 Off', should be a 'fixed_amount' discount of 5.00 with the description 'Test B: $5 off your grocery purchase.' Both promotions must be 'scheduled' to run for the same period: from '2025-10-01' to '2025-10-31', with an initial usage count of 0. After creating both, retrieve all promotions with the status 'scheduled' to verify they are ready.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Grocery"}),
            Action(name="create_promotion", kwargs={
                "name": "Grocery Discount 10%", "type": "percentage", "discount_value": 10.0,
                "description": "Test A: 10% off all grocery items.",
                "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="create_promotion", kwargs={
                "name": "Grocery Discount $5 Off", "type": "fixed_amount", "discount_value": 5.00,
                "description": "Test B: $5 off your grocery purchase.",
                "applicable_skus": ["GROC-ALMBTR500", "GROC-GRNLBR12", "GROC-SPRWAT6P"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_promotions_by_status", kwargs={"status": "scheduled"})
        ],
        outputs=[{"created_promotions": ["PROMO-008", "PROMO-009"]}]
    ),
    Task(
        annotator="0",
        user_id="task_082",
        instruction="You are a CRM Specialist. You want to encourage customers who buy 'Smart Home' devices to expand their ecosystem. First, find all 'silver' tier customers who have purchased the 'EcoSmart Wi-Fi Thermostat' (SMRT-THERM02). For the customer found, 'Mia Kim' (CUST-5011), you will create a special offer. Get all SKUs in the 'Smart Home' category. Create a new 'percentage' promotion named 'Smart Home Expansion' with 15% off all 'Smart Home' items. The description must be 'Expand your smart home with 15% off.' It must be active for one month starting '2025-09-15', with usage count 0. Generate a unique promo code for Mia and confirm her customer details.",
        actions=[
            Action(name="find_customers_by_criteria", kwargs={"membership_levels": ["silver"], "purchase_history_skus": ["SMRT-THERM02"]}),
            Action(name="get_products_by_category", kwargs={"category": "Smart Home"}),
            Action(name="create_promotion", kwargs={
                "name": "Smart Home Expansion", "type": "percentage", "discount_value": 15.0,
                "description": "Expand your smart home with 15% off.",
                "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-09-15", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5011"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5011"})
        ],
        outputs=[{"customer_id": "CUST-5011"}]
    ),
    Task(
        annotator="0",
        user_id="task_083",
        instruction="You are 'Megan Young', Store Manager at 'STORE-005'. Customer 'Benjamin Cohen' (CUST-5010) calls about transaction 'TXN-0010' from '2025-06-05'. He used a promotion, but it was applied incorrectly. The transaction shows a discount of 40.0 on the 'WaveSound All-Weather Bluetooth Speaker'. The discount should have been from the 'Summer Electronics Sale' (PROMO-001), which is 10%. First find the transaction and the promotion details. You see the speaker is not eligible for that promo. The discount was an error. Since you can't alter the transaction, you will compensate by adding loyalty points equal to the price of the speaker. First, get the speaker's SKU and current price ($129.99). Then, find the customer by name. The instruction specifies that for the points conversion, the price must be rounded to the nearest whole number, resulting in 130 points. Add these points to his account. As a final step, update the 'Smart Home Starter Discount' (PROMO-006), which was likely used by mistake, to now include the speaker's SKU 'AUDIO-BTSPKR02' in its list of applicable SKUs to prevent this error in the future.",
        actions=[
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5010", "sku": "AUDIO-BTSPKR02"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Summer Electronics Sale", "query_date": "2025-06-05"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "AUDIO-BTSPKR02"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5010", "points_to_add": 130}),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-006"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-006", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "loyalty_points": 1155}, {"promotion_id": "PROMO-006", "applicable_skus": ["SMRT-THERM02", "AUDIO-BTSPKR02"]}]
    ),
    Task(
        annotator="0",
        user_id="task_084",
        instruction="You are the Marketing Director. You are launching a multi-phase campaign to cross-sell 'Smart Home' products to loyal 'Electronics' customers. PHASE 1: First, identify your target audience. To do this, get all product SKUs from the 'Electronics' category. Then, find all 'gold' tier customers who have purchased any of these electronic items. The resulting list of customer IDs is 'CUST-5001' and 'CUST-5010'. PHASE 2: Now, create the offer. Get all product SKUs from the 'Smart Home' category. Create a new 'percentage' promotion named 'Smart Home Upgrade Offer' with a 25% discount on all 'Smart Home' products. The description must be 'A special 25% off to expand your smart ecosystem.' and it must be active for all of October 2025, with an initial usage count of 0. PHASE 3: Distribute the offer. Generate unique promo codes for the customers identified in Phase 1. As an immediate incentive, also add 100 bonus loyalty points to each of their accounts. PHASE 4: Verify your work by retrieving the customer details for 'Ava Thompson' to confirm her new point balance.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["gold"],
                "purchase_history_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"]
            }),
            Action(name="get_products_by_category", kwargs={"category": "Smart Home"}),
            Action(name="create_promotion", kwargs={
                "name": "Smart Home Upgrade Offer", "type": "percentage", "discount_value": 25.0,
                "description": "A special 25% off to expand your smart ecosystem.",
                "applicable_skus": ["SMRT-THERM02"],
                "start_date": "2025-10-01", "end_date": "2025-10-31", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5001", "CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5001", "points_to_add": 100}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5010", "points_to_add": 100}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Ava Thompson"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5001"})
        ],
        outputs=[{"customer_id": "CUST-5001", "loyalty_points": 1340}]
    ),
    Task(
        annotator="0",
        user_id="task_085",
        instruction="You are a Data Analyst performing a data integrity audit. You have found several errors related to the 'UltraVision 55\" 4K Smart TV' (ELEC-4KTV55) and its main promotion, 'Summer Electronics Sale' (PROMO-001). First, retrieve the product's details; the instruction states its price should be corrected to $749.99 and its status to 'premium'. Update the product record accordingly. Next, retrieve the promotion by its ID. Its discount is too low and must be updated to 15.0%. Also, another product, 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01), must be added to its list of applicable SKUs. Update the promotion with both changes. To verify the financial impact of these corrections, find the customer 'Ava Thompson', who purchased the TV on transaction 'TXN-0001'. The instruction requires you to re-calculate the totals for her original purchase (1 TV and 2 'PowerPlus Rechargeable AA Batteries (4 Pack)'), applying the new price and the new 15% discount to the TV, and return the new recalculated total amount.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-4KTV55"}),
            Action(name="update_product_details", kwargs={"sku": "ELEC-4KTV55", "price": 749.99, "status": "premium"}),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-001"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "QuietTone Wireless Earbuds"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-001", "discount_value": 15.0, "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "ELEC-RCHAA04", "AUDIO-NCEBUDS01"]}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Ava Thompson"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5001", "sku": "ELEC-4KTV55"}),
            Action(name="calculate_transaction_totals", kwargs={
                "line_items": [{"sku": "ELEC-4KTV55", "quantity": 1}, {"sku": "ELEC-RCHAA04", "quantity": 2}],
                "promotion_ids": ["PROMO-001"]
            })
        ],
        outputs=[{"recalculated_total_amount": 724.96}]
    ),
    Task(
        annotator="0",
        user_id="task_086",
        instruction="You are an Inventory Manager at 'STORE-001' on '2025-11-01'. The 'Organic Almond Butter 500g' (GROC-ALMBTR500) has an expiry date of '2026-04-15'. Policy requires a clearance sale if the expiry is within 6 months. First, retrieve the main product details to verify the expiry date. Then, retrieve its inventory record at your store. As the policy is met, update the main product's status to 'clearance'. Because this item is not normally discountable, you must first update its record to set 'is_discountable' to true. Then, create a 'percentage' promotion named 'Expiry Clearance' with a 75% discount. The description must be 'Urgent Sale: 75% off Almond Butter before it expires!'. The promotion must be active from today until the day before expiry, '2026-04-14', with an initial usage count of 0. Finally, identify all 'bronze' tier customers who have ever bought grocery items, as they are the target for this sale. The list of grocery SKUs is 'GROC-ALMBTR500', 'GROC-GRNLBR12', and 'GROC-SPRWAT6P'.",
        actions=[
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "GROC-ALMBTR500"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "GROC-ALMBTR500", "store_id": "STORE-001"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "GROC-ALMBTR500", "status": "clearance"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "GROC-ALMBTR500", "is_discountable": True}
            ),
            Action(
                name="create_promotion",
                kwargs={
                    "name": "Expiry Clearance", "type": "percentage", "discount_value": 75.0,
                    "description": "Urgent Sale: 75% off Almond Butter before it expires!",
                    "applicable_skus": ["GROC-ALMBTR500"],
                    "start_date": "2025-11-01", "end_date": "2026-04-14", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="find_customers_by_criteria",
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
        instruction="You are 'Marcus Chen', the sales lead at 'STORE-002'. A new customer, 'Eleanor Vance', wants to make her first purchase. She is interested in the 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01) and the 'QuietTone Wireless Earbuds' (AUDIO-NCEBUDS01). First, create a new 'basic' customer account for her with 0 loyalty points and marketing opt-in set to true. Then, check the inventory for both items at 'STORE-002'. To welcome her, you will create a new 'percentage' promotion named 'New Customer Welcome' with a 10% discount. The description must be 'A 10% welcome discount for our new customers.' This promotion is active today only, '2025-08-29', with an initial usage of 0, and applies to both items. You must construct the final transaction using these pre-calculated figures: a total discount of $33.95, a tax amount of $25.13, and a final total of $339.67. Process the sale via 'credit_card'. Finally, update the inventory for both items and increment the new promotion's 'times_used' count.",
        actions=[
            Action(
                name="create_customer",
                kwargs={"name": "Eleanor Vance", "membership_level": "basic", "opt_in_marketing": True, "loyalty_points": 0}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "AUDIO-NCEBUDS01", "store_id": "STORE-002"}
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "CLTH-WINJKT01"}
            ),
            Action(
                name="get_product_details_by_sku",
                kwargs={"sku": "AUDIO-NCEBUDS01"}
            ),
            Action(
                name="update_product_details",
                kwargs={"sku": "CLTH-WINJKT01", "is_discountable": True}
            ),
            Action(
                name="create_promotion",
                kwargs={
                    "name": "New Customer Welcome", "type": "percentage", "discount_value": 10.0,
                    "description": "A 10% welcome discount for our new customers.", "applicable_skus": ["CLTH-WINJKT01", "AUDIO-NCEBUDS01"],
                    "start_date": "2025-08-29", "end_date": "2025-08-29", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Marcus Chen"}
            ),
            Action(
                name="create_transaction",
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
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0022", "quantity_sold": 1, "last_stock_count_date": "2025-08-29"}
            ),
            Action(
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0016", "quantity_sold": 1, "last_stock_count_date": "2025-08-29"}
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-008", "times_used": 1}
            )
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_106",
        instruction="You are 'Isabella Rossi', a sales associate at 'STORE-002'. A new high-value customer, 'Arthur Pendragon', wants to purchase a 'GigaPlay 15\" Gaming Laptop' and an 'ErgoPro Adjustable Office Chair'. First, create a new customer account for him with 'silver' membership, an initial balance of 100 loyalty points, and opting into marketing. Next, check the inventory for both items. You will find the laptop is in stock at your store ('STORE-002'), but the chair is only available at 'STORE-003'. After confirming with the customer that he is willing to wait for a transfer, you are authorized to create a special promotion to close the deal. Create a new 'percentage' promotion named 'Manager's Special' with a 10% discount. The description must be 'A special one-time discount for a valued new customer.' and it should apply to both items, active for today's date only, '2025-07-29', with an initial usage count of 0. Then, create an inventory record for the chair at your store ('STORE-002') in 'Customer Holds' and execute the transfer of one unit from 'STORE-003'. Finally, process the entire sale for Mr. Pendragon via 'credit_card', applying the new promotion, and update the inventory records for both items sold.",
        actions=[
            Action(
                name="create_customer",
                kwargs={"name": "Arthur Pendragon", "membership_level": "silver", "loyalty_points": 100, "opt_in_marketing": True}
            ),
            Action(
                name="get_product_sku_by_name",
                kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}
            ),
            Action(
                name="get_product_sku_by_name",
                kwargs={"product_name": "ErgoPro Adjustable Office Chair"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-002"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}
            ),
            Action(
                name="create_promotion",
                kwargs={
                    "name": "Manager's Special", "type": "percentage", "discount_value": 10.0,
                    "description": "A special one-time discount for a valued new customer.",
                    "applicable_skus": ["ELEC-GAMLP15", "OFFC-ERGCHR01"],
                    "start_date": "2025-07-29", "end_date": "2025-07-29", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-002", "location": "Customer Holds"}
            ),
            Action(
                name="execute_inventory_transfer",
                kwargs={"sku": "OFFC-ERGCHR01", "quantity": 1, "from_store_id": "STORE-003", "to_store_id": "STORE-002"}
            ),
            Action(
                name="get_employee_id_by_name",
                kwargs={"employee_name": "Isabella Rossi"}
            ),
            Action(
                name="create_transaction",
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
                name="update_inventory_sale",
                kwargs={"inventory_id": "INV-0013", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}
            ),
            Action(
                name="update_inventory_sale",
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
        instruction="You are the Inventory Manager for 'STORE-002'. Your store has a special order for 10 'BrewMaster 12-Cup Coffee Makers' (HOM-COFMKR12), but you do not currently stock this item. You must source them from 'STORE-001'. First, confirm that 'STORE-001' has at least 10 units in stock. Then, create a new inventory record for the coffee maker at your store ('STORE-002') in location 'Special Order Shelf'. Immediately after creating the record, update its 'reserved_quantity' by an amount of 10 to log the special order. Then, execute the transfer of 10 units from 'STORE-001' to your store. Finally, update the status of your new inventory record to 'in_stock' and retrieve it to confirm the quantity and reservation are correct. The date for all updates is '2025-08-28'.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "BrewMaster 12-Cup Coffee Maker"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002", "location": "Special Order Shelf"}),
            Action(name="update_inventory_reserved_quantity", kwargs={"inventory_id": "INV-0025", "change_amount": 10}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOM-COFMKR12", "quantity": 10, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0025", "status": "in_stock"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOM-COFMKR12", "store_id": "STORE-002"})
        ],
        outputs=[{"id": "INV-0025", "quantity": 10, "reserved_quantity": 10, "status": "in_stock"}]
    ),
    Task(
        annotator="0",
        user_id="task_090",
        instruction="You are a Marketing Manager. The 'Kitchen Essentials Bundle' (PROMO-002) is ending today, '2025-07-15'. Your task is to deactivate it and immediately launch an enhanced version for the upcoming holiday season. First, retrieve the promotion by its ID to check its 'times_used' count. Then, deactivate it. Next, you will create a new promotion named 'Kitchen Upgrade Bundle'. This will be a 'fixed_bundle' promotion with an increased discount of $20.00. The description must be 'Upgrade your kitchen with this premium bundle for the holidays.'. It will include the original items ('HOM-COFMKR12', 'KITCH-CHEFKNF8') plus the 'ChefPro Ceramic Fry Pan 10\"' (KITCH-FRYPAN10). The new promotion should be 'scheduled' to run from '2025-11-01' to '2025-12-31', with an initial usage count of 0. Finally, retrieve the new promotion by its ID to confirm its creation.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="deactivate_promotion", kwargs={"promotion_id": "PROMO-002"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ChefPro Ceramic Fry Pan 10\""}),
            Action(name="create_promotion", kwargs={
                "name": "Kitchen Upgrade Bundle", "type": "fixed_bundle", "discount_value": 20.0,
                "description": "Upgrade your kitchen with this premium bundle for the holidays.",
                "applicable_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "KITCH-FRYPAN10"],
                "start_date": "2025-11-01", "end_date": "2025-12-31", "status": "scheduled", "times_used": 0
            }),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-008"})
        ],
        outputs=[{"promotion_id": "PROMO-002", "status": "inactive"}, {"promotion_id": "PROMO-008", "name": "Kitchen Upgrade Bundle"}]
    ),
    Task(
        annotator="0",
        user_id="task_091",
        instruction="You are 'Isabella Rossi', a sales associate at 'STORE-002'. A customer, 'William Zhang', wants to buy your entire remaining stock of the 'ArcticShield Men's Parka - Large' (CLTH-WINJKT01). First, retrieve the inventory record for this parka at your store to confirm the exact quantity available (which is 6). The customer has also decided to upgrade his membership. Update his customer record from 'silver' to 'gold'. Now, process the sale for all 6 parkas. The payment method must be 'credit_card'. There is an active 'Clearance Apparel Markdown' promotion (PROMO-005) which you must check for today's date, '2025-06-25'. You must construct the final transaction using these pre-calculated figures: each parka has a unit_price of $189.50 with a per-item discount of $47.38. The final total_amount is $923.10, the tax_amount is $70.35, and the discount_total is $284.25. After creating the transaction with these exact values, you must immediately update the parka's inventory status to 'out_of_stock'. Finally, confirm the customer's new membership level.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ArcticShield Men's Parka - Large"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-WINJKT01", "store_id": "STORE-002"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "William Zhang"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5006", "membership_level": "gold"}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-25"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Isabella Rossi"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1009", "customer_id": "CUST-5006", "payment_method": "credit_card",
                "total_amount": 923.10, "tax_amount": 70.35, "discount_total": 284.25,
                "line_items": [{"sku": "CLTH-WINJKT01", "quantity": 6, "unit_price": 189.5, "discount": 47.38}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0022", "quantity_sold": 6, "last_stock_count_date": "2025-06-25"}),
            Action(name="update_inventory_status", kwargs={"inventory_id": "INV-0022", "status": "out_of_stock"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[{"customer_id": "CUST-5006", "membership_level": "gold"}]
    ),
    Task(
        annotator="0",
        user_id="task_092",
        instruction="You are a customer service rep. 'William Zhang' (CUST-5006) is at 'STORE-002' to return one 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) from transaction 'TXN-0006'. The item is in perfect condition. The instruction specifies the original price was $229.99. The inventory for this chair is at 'STORE-003', so you must process the return against the correct inventory record by first finding it ('INV-0014') and adding 1 unit back to its stock. The customer will use this credit to buy two 'Men's Slim Fit Jeans - 34W 32L' (CLTH-SLFJEAN34) from 'STORE-002'. Check the stock for the jeans, look up their price, then create the transaction for the new purchase, applying the full credit of $229.99. The remaining balance will be refunded to his 'debit_card', resulting in a final transaction total of -$122.82 and a tax amount of $8.17. The sales associate is 'Ethan Walker', and the date for inventory updates is '2025-08-15'.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "William Zhang"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="update_stock_level", kwargs={"inventory_id": "INV-0014", "quantity_to_add": 1}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "Men's Slim Fit Jeans - 34W 32L"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "CLTH-SLFJEAN34"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "CLTH-SLFJEAN34", "store_id": "STORE-002"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Ethan Walker"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-002", "employee_id": "EMP-1011", "customer_id": "CUST-5006", "payment_method": "debit_card",
                "total_amount": -122.82, "tax_amount": 8.17, "discount_total": 0.0,
                "line_items": [{"sku": "CLTH-SLFJEAN34", "quantity": 2, "unit_price": 49.5, "discount": 0.0}]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0005", "quantity_sold": 2, "last_stock_count_date": "2025-08-15"})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_093",
        instruction="You are a sales lead, 'Daniel Perez'. You have convinced a long-time customer, 'Benjamin Cohen' (CUST-5010), who had previously opted out of marketing, to opt in. Your first action is to retrieve his customer details to confirm his current opt-out status. Then, update his record to set 'opt_in_marketing' to true. As a thank you for opting in, your manager has authorized you to create a special one-time discount for him. Find all products in his favorite category, 'Electronics'. Create a new 'fixed_amount' promotion named 'Ben's Opt-in Reward' that provides a $25.00 discount on any of these electronic items. The description must be 'A special thank you for joining our marketing list.' and it should be active for 60 days starting '2025-08-16', with an initial usage count of 0. Finally, generate a unique promo code for him and retrieve his details again to confirm his opt-in status.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Benjamin Cohen"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5010", "opt_in_marketing": True}),
            Action(name="get_products_by_category", kwargs={"category": "Electronics"}),
            Action(name="create_promotion", kwargs={
                "name": "Ben's Opt-in Reward", "type": "fixed_amount", "discount_value": 25.0,
                "description": "A special thank you for joining our marketing list.",
                "applicable_skus": ["ELEC-4KTV55", "AUDIO-BTSPKR02", "ELEC-GAMLP15", "AUDIO-NCEBUDS01", "ELEC-RCHAA04"],
                "start_date": "2025-08-16", "end_date": "2025-10-15", "status": "active", "times_used": 0
            }),
            Action(name="generate_and_assign_promo_codes", kwargs={"customer_ids": ["CUST-5010"], "promotion_id": "PROMO-008"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5010"})
        ],
        outputs=[{"customer_id": "CUST-5010", "opt_in_marketing": True}]
    ),
    Task(
        annotator="0",
        user_id="task_094",
        instruction="You are an Inventory Specialist preparing for the holiday season. The 'LumiLux LED Desk Lamp' (HOME-DESKLMP01) is expected to be a top seller, but its stock is all at 'STORE-001'. Your goal is to distribute it. First, create a new inventory record for the lamp at 'STORE-003' in location 'Holiday Gifts'. Then, transfer 20 units from 'STORE-001' to 'STORE-003'. You must get the inventory records for both the source and destination before the transfer to get their IDs. After the transfer, the inventory at 'STORE-001' is now lower. As per new policy, you must create a 'percentage' promotion for the item at the source store to clear its remaining stock. The promotion should be named 'Pre-Holiday Lamp Sale', with a 10% discount, a description of '10% off lamps before our holiday shipment!', active today, '2025-08-29', with usage count 0.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="create_inventory_record", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-003", "location": "Holiday Gifts"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "HOME-DESKLMP01", "quantity": 20, "from_store_id": "STORE-001", "to_store_id": "STORE-003"}),
            Action(name="create_promotion", kwargs={
                "name": "Pre-Holiday Lamp Sale", "type": "percentage", "discount_value": 10.0,
                "description": "10% off lamps before our holiday shipment!",
                "applicable_skus": ["HOME-DESKLMP01"],
                "start_date": "2025-08-29", "end_date": "2025-08-29", "status": "active", "times_used": 0
            }),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"})
        ],
        outputs=[{"id": "INV-0015", "quantity": 25}]
    ),
    Task(
        annotator="0",
        user_id="task_095",
        instruction="You are 'Grace Miller' at 'STORE-001'. Today is '2025-06-10', the first day of the 'Buy One Yoga Mat Get 50% Off Second' promotion (PROMO-003). A customer, 'Sophia Rossi', wants to buy two 'FlexFit Premium Yoga Mat' (SPORT-YOGMAT01). First, you must get the promotion by its ID and change its status from 'scheduled' to 'active'. Then, check the inventory for the mats at your store to ensure at least two are available. Next, process the sale for Sophia. The instruction specifies that the payment method is 'mobile_wallet'. You must construct the final transaction based on the following pre-calculated figures: the price of one mat is $29.99, the 50% discount on the second mat is $15.00, the final total amount is $48.71, the tax is $3.71, and the total discount is $15.00. Create the transaction, update the inventory for the two mats sold, and increment the promotion's 'times_used' count by one.",
        actions=[
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="activate_promotion", kwargs={"promotion_id": "PROMO-003"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "FlexFit Premium Yoga Mat"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "SPORT-YOGMAT01", "store_id": "STORE-001"}),
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Sophia Rossi"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Grace Miller"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1002", "customer_id": "CUST-5007", "payment_method": "mobile_wallet",
                "total_amount": 48.71, "tax_amount": 3.71, "discount_total": 15.00,
                "line_items": [
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 0.0},
                    {"sku": "SPORT-YOGMAT01", "quantity": 1, "unit_price": 29.99, "discount": 15.00}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0021", "quantity_sold": 2, "last_stock_count_date": "2025-06-10"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-003", "times_used": 1})
        ],
        outputs=[{"transaction_id": "TXN-0013"}]
    ),
    Task(
        annotator="0",
        user_id="task_096",
        instruction="You are a Data Analyst. You have found a data integrity issue: the 'ErgoPro Adjustable Office Chair' (OFFC-ERGCHR01) is in the 'Office Supplies' category, but it should be in a more specific 'Furniture' category. Your task is to correct this. First, retrieve the product by its SKU to verify its current category. Then, update the product's category to 'Furniture'. As this is a high-value item, the company wants to ensure it's eligible for all major sales. Retrieve the product's details again to confirm the category change, and because the 'is_discountable' flag is currently true, you must update it to be false as per a new company policy for high-value furniture. Finally, find all products that are now in the 'Furniture' category to ensure your update was successful.",
        actions=[
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="update_product_details", kwargs={"sku": "OFFC-ERGCHR01", "category": "Furniture"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="update_product_details", kwargs={"sku": "OFFC-ERGCHR01", "is_discountable": False}),
            Action(name="get_products_by_category", kwargs={"category": "Furniture"})
        ],
        outputs=[{"sku": "OFFC-ERGCHR01", "category": "Furniture", "is_discountable": False}]
    ),
    Task(
        annotator="0",
        user_id="task_097",
        instruction="You are the Marketing Director. You want to reward your top customers in the 'Home & Kitchen' category. First, get all products belonging to this category. Then, using this list, find all 'silver' customers who have purchased these items. For each of the silver-level customers identified (CUST-5002, CUST-5006, CUST-5009, CUST-5011), add 200 bonus loyalty points to their accounts as a reward for their business. To confirm the updates, retrieve the full customer details for 'Liam Nguyen' and 'William Zhang' after their points have been added, and provide their new loyalty point totals.",
        actions=[
            Action(name="get_products_by_category", kwargs={"category": "Home & Kitchen"}),
            Action(name="find_customers_by_criteria", kwargs={
                "membership_levels": ["silver"],
                "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
            }),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5002", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5006", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5009", "points_to_add": 200}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5011", "points_to_add": 200}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5002"}),
            Action(name="get_customer_details_by_id", kwargs={"customer_id": "CUST-5006"})
        ],
        outputs=[
            {"customer_id": "CUST-5002", "loyalty_points": 1075},
            {"customer_id": "CUST-5006", "loyalty_points": 1180}
        ]
    ),
    Task(
        annotator="0",
        user_id="task_098",
        instruction="You are 'Marcus Chen', the manager at 'STORE-002'. Customer 'William Zhang' (CUST-5006) is returning his entire purchase from transaction 'TXN-0006'. The instruction states the returned items are one 'ErgoPro Adjustable Office Chair' and one 'LumiLux LED Desk Lamp' and their original purchase prices were $229.99 and $34.99 respectively. First, you need to find the inventory IDs for both products at their respective stocking stores ('STORE-003' and 'STORE-001'). Then, process the return for both items using their stated purchase prices, which will also add them back to the correct inventory records. Because the entire transaction is being returned, a promotion usage count must be rolled back. Retrieve the 'Clearance Apparel Markdown' promotion by name for date '2025-06-20', and then update its 'times_used' count by decrementing it by one, from 87 to 86. Finally, get the promotion's details again by its ID ('PROMO-005') to confirm the change.",
        actions=[
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0006", "sku": "OFFC-ERGCHR01", "quantity_returned": 1, "unit_price": 229.99}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0006", "sku": "HOME-DESKLMP01", "quantity_returned": 1, "unit_price": 34.99}),
            Action(name="get_promotion_by_name_and_date", kwargs={"promotion_name": "Clearance Apparel Markdown", "query_date": "2025-06-20"}),
            Action(name="update_promotion_details", kwargs={"promotion_id": "PROMO-005", "times_used": 86}),
            Action(name="get_promotion_by_id", kwargs={"promotion_id": "PROMO-005"})
        ],
        outputs=[{"promotion_id": "PROMO-005", "times_used": 86}]
    ),
    Task(
        annotator="0",
        user_id="task_099",
        instruction="You are 'Natalie Cooper', a customer service lead at 'STORE-001'. A customer, 'Emma García', is in the store with a complex request. She wants to return a 'GigaPlay 15\" Gaming Laptop' from her past transaction (TXN-0005). The laptop is in perfect condition, but your store does not stock this item. You must process the return and immediately create a new inventory record for the laptop at your store in the 'Service Returns' location, then execute a transfer of the unit to 'STORE-002', the main hub for electronics. She will use the full credit from the return to purchase two other items: one 'ErgoPro Adjustable Office Chair', which you must source from 'STORE-003', and one 'LumiLux LED Desk Lamp' from your own store's stock. As a thank you for her patience, update her account by adding 100 bonus loyalty points and upgrading her membership level to 'silver'. Finally, process the sale of the new items, apply the full credit from the return, and refund the remaining balance to her 'credit_card'.",
        actions=[
            Action(name="get_customer_id_by_name", kwargs={"customer_name": "Emma García"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "GigaPlay 15\" Gaming Laptop"}),
            Action(name="find_transaction_by_customer_and_sku", kwargs={"customer_id": "CUST-5005", "sku": "ELEC-GAMLP15"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "ELEC-GAMLP15"}),
            Action(name="process_item_return", kwargs={"transaction_id": "TXN-0005", "sku": "ELEC-GAMLP15", "quantity_returned": 1, "unit_price": 1499.0}),
            Action(name="create_inventory_record", kwargs={"sku": "ELEC-GAMLP15", "store_id": "STORE-001", "location": "Service Returns"}),
            Action(name="execute_inventory_transfer", kwargs={"sku": "ELEC-GAMLP15", "quantity": 1, "from_store_id": "STORE-001", "to_store_id": "STORE-002"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "ErgoPro Adjustable Office Chair"}),
            Action(name="get_product_sku_by_name", kwargs={"product_name": "LumiLux LED Desk Lamp"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "OFFC-ERGCHR01"}),
            Action(name="get_product_details_by_sku", kwargs={"sku": "HOME-DESKLMP01"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "OFFC-ERGCHR01", "store_id": "STORE-003"}),
            Action(name="get_inventory_item_by_sku_and_store", kwargs={"sku": "HOME-DESKLMP01", "store_id": "STORE-001"}),
            Action(name="get_employee_id_by_name", kwargs={"employee_name": "Natalie Cooper"}),
            Action(name="create_transaction", kwargs={
                "store_id": "STORE-001", "employee_id": "EMP-1004", "customer_id": "CUST-5005", "payment_method": "credit_card",
                "total_amount": -1212.16, "tax_amount": 21.86, "discount_total": 0.0,
                "line_items": [
                    {"sku": "OFFC-ERGCHR01", "quantity": 1, "unit_price": 229.99, "discount": 0.0},
                    {"sku": "HOME-DESKLMP01", "quantity": 1, "unit_price": 34.99, "discount": 0.0}
                ]
            }),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0014", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_inventory_sale", kwargs={"inventory_id": "INV-0015", "quantity_sold": 1, "last_stock_count_date": "2025-07-29"}),
            Action(name="update_customer_loyalty_points", kwargs={"customer_id": "CUST-5005", "points_to_add": 100}),
            Action(name="update_customer_details", kwargs={"customer_id": "CUST-5005", "membership_level": "silver"})
        ],
        outputs=[{"customer_id": "CUST-5005", "membership_level": "silver", "loyalty_points": 395}]
    ),
    Task(
        annotator="0",
        user_id="task_100",
        instruction="You are a Marketing Director launching a targeted campaign called 'Operation Knife Edge'. The goal is to consolidate all stock of the 'ProSlice 8\" Chef Knife' at the main warehouse ('STORE-001') and then run a highly targeted flash sale. First, transfer all units of the knife from 'STORE-002' to 'STORE-001', ensuring you create an inventory record at the destination first in the 'Online Fulfillment' location. Next, identify your target audience: all 'silver' tier customers who have previously purchased any item from the 'Home & Kitchen' category. For this specific audience, create a new 'fixed_amount' promotion named 'Knife Edge Flash Sale' offering a $15 discount on the 'ProSlice 8\" Chef Knife'. The promotion's description must be 'A special flash sale for our loyal kitchen enthusiasts.' and it must be active from '2025-07-29' to '2025-07-31'. After creating the promotion, generate unique, single-use promotional codes for all qualified customers and then update the promotion to require a code for redemption. Finally, as a loyalty bonus, upgrade all identified customers ('Liam Nguyen' and 'Mia Kim') to the 'gold' membership level and retrieve their updated details to confirm the change.",
        actions=[
            Action(
                name="get_product_sku_by_name",
                kwargs={"product_name": "ProSlice 8\" Chef Knife"}
            ),
            Action(
                name="get_inventory_item_by_sku_and_store",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-002"}
            ),
            Action(
                name="create_inventory_record",
                kwargs={"sku": "KITCH-CHEFKNF8", "store_id": "STORE-001", "location": "Online Fulfillment"}
            ),
            Action(
                name="execute_inventory_transfer",
                kwargs={"sku": "KITCH-CHEFKNF8", "quantity": 35, "from_store_id": "STORE-002", "to_store_id": "STORE-001"}
            ),
            Action(
                name="get_products_by_category",
                kwargs={"category": "Home & Kitchen"}
            ),
            Action(
                name="find_customers_by_criteria",
                kwargs={
                    "membership_levels": ["silver"],
                    "purchase_history_skus": ["HOM-COFMKR12", "KITCH-CHEFKNF8", "HOME-BTHTWL01", "HOME-DESKLMP01", "KITCH-FRYPAN10"]
                }
            ),
            Action(
                name="create_promotion",
                kwargs={
                    "name": "Knife Edge Flash Sale", "type": "fixed_amount", "discount_value": 15.0,
                    "description": "A special flash sale for our loyal kitchen enthusiasts.",
                    "applicable_skus": ["KITCH-CHEFKNF8"],
                    "start_date": "2025-07-29", "end_date": "2025-07-31", "status": "active", "times_used": 0
                }
            ),
            Action(
                name="generate_and_assign_promo_codes",
                kwargs={"customer_ids": ["CUST-5002", "CUST-5011", "CUST-5009", "CUST-5006"], "promotion_id": "PROMO-008"}
            ),
            Action(
                name="update_promotion_details",
                kwargs={"promotion_id": "PROMO-008", "requires_code": True}
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5002", "membership_level": "gold"}
            ),
            Action(
                name="update_customer_details",
                kwargs={"customer_id": "CUST-5011", "membership_level": "gold"}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5002"}
            ),
            Action(
                name="get_customer_details_by_id",
                kwargs={"customer_id": "CUST-5011"}
            )
        ],
        outputs=[
            {"customer_id": "CUST-5002", "membership_level": "gold"},
            {"customer_id": "CUST-5011", "membership_level": "gold"}
        ]
    )
]
