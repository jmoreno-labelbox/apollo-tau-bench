from domains.dto import Task, Action

TASKS = [

    Task(
        annotator="0",
        user_id="USER_001",
        instruction="As a manager, you are auditing a delivered order, #W4817420, for customer Ava Moore (user ID: ava_moore_2033). The audit requires a full review of the customer's payment history for the order and the full logistics trail, including the courier. During the product audit, you discover that two items from the order have since been discontinued by their suppliers: the 'Action Camera' (item #6700049080) and the 'Hiking Boots' (item #3812493782). You must update the availability for both of these items in the product catalog to prevent future sales. As a final step, you have decided to adjust the price of a different, high-stock item from the order, the 'Water Bottle' (item #6777246137), to $45.00.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W4817420"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W4817420"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0005"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7363354090", "item_id": "3812493782", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="update_variant_price", kwargs={"product_id": "8310926033", "item_id": "6777246137", "price": 45.00})
        ],
        outputs={
            "audited_order_id": "#W4817420",
            "discontinued_item_1": "6700049080",
            "discontinued_item_2": "3812493782",
            "price_updated_item": "6777246137",
            "new_price": 45.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction="You are a logistics manager reviewing a system-flagged order, #W7303089, for customer Mei Gonzalez (ZIP: 95170). The order was successfully delivered, but the tracking data from the courier, 'FastTrack Couriers' (#COU0001), needs to be audited for accuracy and the customer's payment details must be verified. Your task is to conduct a full audit by retrieving the customer's details, all their associated payment methods, and the specific payment transaction for this order. You must also trace the full delivery history. As a final step, because you notice the 'Pet Bed' (item #7381052709) in her order has a low profit margin, update its price in the product catalog to $199.99 to improve profitability.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "zip": "95170"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_variant_price", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99}),
            Action(name="get_variant_details", kwargs={"item_id": "7381052709"})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "order_id": "#W7303089",
            "tracking_id": "889070895653",
            "payment_method_id": "credit_card_4387170",
            "price_updated_item_id": "7381052709",
            "new_price": 199.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction="You are a customer service manager handling a stalled order, #W7619352, for Sofia Thomas (user ID: sofia_thomas_1518). The order is delayed due to an out-of-stock 'Portable Charger' (item #7903094618). Your task is to resolve the issue by expediting a pending supply order for that supplier (#SO6372). As part of a supplier audit, you've also decided to discontinue a different product from them, the 'red olefin Patio Umbrella' (product #9743693396, item #8170914468), by updating its stock and availability. Finally, ship the available items from the customer's order using new tracking ID 181292856236 from 'QuickShip Logistics' and update the order's status to reflect the partial shipment.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W7619352"}),
            Action(name="get_user_details", kwargs={"user_id": "sofia_thomas_1518"}),
            Action(name="get_product_details", kwargs={"product_id": "6942297802"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "7903094618"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "9743693396"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "9743693396", "item_id": "8170914468", "available": False}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W7619352", "tracking_ids": ["181292856236"], "item_ids": ["2757705742", "3526747930", "8798690242"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W7619352", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "sofia_thomas_1518",
            "stalled_order_id": "#W7619352",
            "out_of_stock_item_id": "7903094618",
            "expedited_supply_order_id": "#SO6372",
            "discontinued_item_id": "8170914468",
            "new_tracking_id": "181292856236",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction="You are a returns manager processing a return from customer Ava Moore (user ID: ava_moore_2033) for her delivered order #W4817420. She is returning the 'Hiking Boots' (item #3812493782). Your task is to process this return by restocking the item with its supplier. While doing so, you identify an obsolete cancelled supply order (#SO5813) for that supplier that must be deleted. As part of a promotional campaign, you also need to adjust the price of the 'Action Camera' (item #6700049080) from her original order to $450.00. Finally, update the order status to 'partially_returned' and verify the price change was successful.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="update_variant_price", kwargs={"product_id": "3377618313", "item_id": "6700049080", "price": 450.00}),
            Action(name="get_variant_details", kwargs={"item_id": "6700049080"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "processed_order_id": "#W4817420",
            "returned_item_id": "3812493782",
            "new_stock_level": 24,
            "deleted_supply_order_id": "#SO5813",
            "price_updated_item_id": "6700049080",
            "new_price": 450.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction="You are a manager handling a return from customer Omar Khan (user ID: omar_khan_2363) for his order #W6304490. He is returning the 'Dumbbell Set' (item #2194493783). Since this product line has ongoing quality issues, discontinue it by removing it from active stock and making it unavailable in the catalog. In addition, review Omar Khan's account details as part of the return audit. To clear remaining inventory from the same supplier ('Sports Gear Suppliers'), reduce the price of the '30-50 lbs urethane adjustable' set (item #4422467033) to $479.99. Finally, audit their fulfilled supply order #SO5817 and mark the customer's order status as 'partially_returned'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_user_details", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "2194493783", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7233192239", "item_id": "2194493783", "available": False}),
            Action(name="get_variant_details", kwargs={"item_id": "4422467033"}),
            Action(name="update_variant_price", kwargs={"product_id": "7233192239", "item_id": "4422467033", "price": 479.99}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="update_order_status", kwargs={"order_id": "#W6304490", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "omar_khan_2363",
            "processed_order_id": "#W6304490",
            "discontinued_item_id": "2194493783",
            "price_updated_item_id": "4422467033",
            "new_price": 479.99,
            "audited_supply_order_id": "#SO5817",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_006",
        instruction="As a senior manager, you are handling a complex request for customer Sofia Rossi (user ID: sofia_rossi_8776) regarding her pending order, #W5918442. She wishes to cancel her entire from the order, and also wants to update her address to 456 Market St, San Francisco, CA, 94105. Your task is to process this. You must cancel and update her address. Then, you must perform a full inventory reconciliation for all items in the cancelled order. This involves restocking them with their correct suppliers, and also correcting a data error you discover for the 'Action Camera', which is incorrectly marked as discontinued; you must set its stock to 1 and make it available.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="update_user_address", kwargs={"user_id": "sofia_rossi_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "CA", "zip": "94105", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "6858788497"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 1}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "cancelled_order_id": "#W5918442",
            "updated_zip_code": "94105",
            "data_corrected_item_id": "1586641416",
            "restocked_items_count": 4
        }
    ),
    Task(
        annotator="0",
        user_id="USER_007",
        instruction="You are a logistics manager auditing a shipment with tracking ID 367478070474. Your task is to perform a full trace on this shipment, which includes identifying the courier and the associated order (#W9549057) and customer (Mason Johansson). You need to review the customer's full details and payment methods. During your audit of the order's items, you notice the 'T-Shirt' (item #5253880258) is from a supplier with an obsolete fulfilled supply order (#SO6503) that needs to be deleted. You also decide that the 'Makeup Kit' (item #7736359414) from the order should be discontinued. Please update its stock status and availability. Finally, update the customer's order status to 'audit_complete'.",
        actions=[
            Action(name="find_courier_by_tracking_id", kwargs={"tracking_id": "367478070474"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9549057"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9549057"}),
            Action(name="get_user_details", kwargs={"user_id": "mason_johansson_2485"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mason_johansson_2485"}),
            Action(name="get_product_details", kwargs={"product_id": "9523456873"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO6503"}),
            Action(name="get_product_details", kwargs={"product_id": "5149340237"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "5149340237", "item_id": "7736359414", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W9549057", "status": "audit_complete"})
        ],
        outputs={
            "audited_tracking_id": "367478070474",
            "customer_user_id": "mason_johansson_2485",
            "deleted_supply_order_id": "#SO6503",
            "discontinued_item_id": "7736359414",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_008",
        instruction="As a senior manager, you are conducting a full audit of the supplier 'Global Tech Distributors' (#SUP0002). Your task is to get a complete list of their products and review the available variants for their 'Office Chair' product line. During the audit, you discover that the 'black fabric fixed standard' chair (item #8426249116) is incorrectly marked as available and must be updated. You also find an unnecessary pending supply order, #SO6035, which needs to be cancelled. Concurrently, you must review customer order #W2611340, which contains an item from this supplier, to check its payment and tracking history. Finally, update the order's status to 'audit_complete'.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="list_available_variants", kwargs={"product_id": "4794339885"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4794339885", "item_id": "8426249116", "available": False}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6035", "status": "cancelled"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W2611340"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W2611340"}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "audit_complete"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0002",
            "data_corrected_item_id": "8426249116",
            "cancelled_supply_order": "#SO6035",
            "audited_customer_order": "#W2611340",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_009",
        instruction="You are a senior analyst investigating a data anomaly related to a fulfilled supply order, #SO5897. Your task is to trace this order to its supplier and product, and correct the inventory for the 'Electric Kettle' (item #9472539378), which is incorrectly marked as having zero stock, by setting its stock to 81 units and making it available. This investigation leads you to a customer order, #W4817420, which contains a different kettle from the same supplier. You must review the full details of this customer order. During the review, you decide to adjust the price of the 'Hiking Boots' (item #3812493782) in that order to $250.00 and delete an unrelated, obsolete supply order (#SO5813) for its supplier.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5897"}),
            Action(name="get_product_details", kwargs={"product_id": "1075968781"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9472539378"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9472539378", "value": 81}),
            Action(name="update_variant_availability", kwargs={"product_id": "1075968781", "item_id": "9472539378", "available": True}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="update_variant_price", kwargs={"product_id": "7363354090", "item_id": "3812493782", "price": 250.00}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="get_variant_details", kwargs={"item_id": "9472539378"})
        ],
        outputs={
            "audited_supply_order": "#SO5897",
            "corrected_item_id": "9472539378",
            "new_stock_level": 81,
            "audited_customer_order": "#W4817420",
            "price_updated_item": "3812493782",
            "new_price": 250.00,
            "deleted_supply_order": "#SO5813"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_010",
        instruction="You are a logistics manager handling a 'lost in transit' claim for order #W9077205 from customer Amelia Wilson (user ID: amelia_wilson_4614). Your goal is to resolve this completely. The investigation requires you to trace the original shipment's tracking history and identify the courier. You must then check the stock for both items in her order to determine if a re-shipment is feasible. Since one item is in stock while the other is not, you will need to arrange a partial re-shipment for the available 'Dumbbell Set' using the new tracking ID 682308736931 from 'FastTrack Couriers' (COU0001). You must also address the stockout of the 'Jigsaw Puzzle' by finding the related pending supply order, #SO6372, and expediting it. Finally, update the customer's order status to reflect the partial re-shipment.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9077205"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0009"}),
            Action(name="get_product_details", kwargs={"product_id": "1808611083"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6372"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="assign_courier_to_order", kwargs={"order_id": "#W9077205", "courier_id": "#COU0001", "tracking_ids": ["682308736931"], "item_ids": ["3877338112"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "lost_order_id": "#W9077205",
            "original_courier_id": "#COU0009",
            "out_of_stock_item_id": "9370300555",
            "reshipped_item_id": "3877338112",
            "expedited_supply_order_id": "#SO6372",
            "new_tracking_id": "682308736931",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_011",
        instruction="You are a logistics manager auditing a shipment with tracking ID 343374055447. Your task is to perform a full trace on this shipment, which includes identifying the courier and the associated order (#W8935389) and customer (Raj Li). You need to review the customer's full details and payment methods. During your audit of the order's items, you notice the 'Espresso Machine' (item #3714494375) is from a supplier with an obsolete cancelled supply order (#SO1273) that needs to be deleted. You also decide that the 'Smart Thermostat' (item #8722653925) from the order should be discontinued. Please update its stock status and availability. Finally, update the customer's order status to 'audit_complete'.",
        actions=[
            Action(name="find_courier_by_tracking_id", kwargs={"tracking_id": "343374055447"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W8935389"}),
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_user_details", kwargs={"user_id": "raj_li_8594"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "raj_li_8594"}),
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="get_product_details", kwargs={"product_id": "4896585277"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "8722653925"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "8722653925", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4896585277", "item_id": "8722653925", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs={
            "audited_tracking_id": "343374055447",
            "customer_user_id": "raj_li_8594",
            "deleted_supply_order_id": "#SO1273",
            "discontinued_item_id": "8722653925",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_012",
        instruction="As a manager, you are performing a full audit on a pending order, #W9318778, for customer Lucas Martin (user ID: lucas_martin_4549). Your task is to investigate the customer's account, including all payment methods, and determine the cause of the delay by checking the product's stock status. You find that the 'Air Purifier' (item #5669664287) is out of stock. To resolve this, you must investigate a related cancelled supply order (#SO4853) and reactivate it. As part of a pricing review, you also need to update the price of the 'Mechanical Keyboard' (item #6342039236) in his order to $250.00. Finally, update the order status to 'awaiting_inventory'.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "lucas_martin_4549"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "lucas_martin_4549"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9318778"}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO4853"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO4853", "status": "pending"}),
            Action(name="get_product_details", kwargs={"product_id": "1656367028"}),
            Action(name="update_variant_price", kwargs={"product_id": "1656367028", "item_id": "6342039236", "price": 250.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W9318778", "status": "awaiting_inventory"})
        ],
        outputs={
            "audited_customer_id": "lucas_martin_4549",
            "stalled_order_id": "#W9318778",
            "out_of_stock_item": "5669664287",
            "reactivated_supply_order": "#SO4853",
            "price_updated_item": "6342039236",
            "new_price": 250.00,
            "final_order_status": "awaiting_inventory"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_013",
        instruction="You are a senior manager conducting an audit on 'Pet Supplies World' (#SUP0009). Your task is to get a complete list of their products and review the available variants for their 'Coffee Maker' product line. During the audit, you discover that the '4 cups drip stainless steel' variant (item #3039787582) is incorrectly marked as available and must be updated. You also find a redundant pending supply order, #SO6035, which needs to be cancelled. Concurrently, you must review a customer order, #W8935389, which contains items from this supplier, to check its payment and tracking history. Finally, update the price of the 'manual 1L Espresso Machine' (item #3714494375) from the order to $2750.00.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="get_product_details", kwargs={"product_id": "7996920482"}),
            Action(name="list_available_variants", kwargs={"product_id": "7996920482"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7996920482", "item_id": "3039787582", "available": False}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6035", "status": "cancelled"}),
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W8935389"}),
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="update_variant_price", kwargs={"product_id": "4354588079", "item_id": "3714494375", "price": 2750.00})
        ],
        outputs={
            "audited_supplier_id": "#SUP0009",
            "data_corrected_item_id": "3039787582",
            "cancelled_supply_order": "#SO6035",
            "audited_customer_order": "#W8935389",
            "price_updated_item": "3714494375",
            "new_price": 2750.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_014",
        instruction="As a senior manager, you are conducting an audit of the supplier 'Green Grocers' (#SUP0005). Your task is to get a complete overview of their product lines and list the available variants for their 'Bicycle' product (product ID: 9783735446). During your work, you are alerted to a stalled customer order, #W9318778, which contains an out-of-stock 'Air Purifier' from a different supplier. You must investigate the supply chain for the problematic item by reviewing the pending supply order #SO4238 and expediting it. To resolve the customer's issue, you must then ship the four available items from their order using tracking ID 836251433228 and update the order status to 'partially_shipped'.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="list_available_variants", kwargs={"product_id": "9783735446"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9318778"}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO4238"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO4238", "status": "expedited"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9318778", "tracking_ids": ["836251433228"], "item_ids": ["2143041831", "6342039236", "9850781806", "3076708684"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9318778", "status": "partially_shipped"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0005",
            "stalled_order_id": "#W9318778",
            "out_of_stock_item": "5669664287",
            "expedited_supply_order": "#SO4238",
            "new_tracking_id": "836251433228",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_015",
        instruction="You are a customer service manager handling a multi-part request for Ava Moore (ZIP: 78234) regarding her delivered order, #W4817420. She wants to return the 'Hiking Boots' (item #3812493782) and update her shipping address to 101 Pine St, San Antonio, TX, 78234. Your task is to process this. First, restock the returned boots with their supplier. While investigating the order, you notice the 'Action Camera' (item #6700049080) is out of stock, and its supply order (#SO6998) was cancelled. To prevent future stockouts, you must reactivate this supply order. As a final step, update the customer's address on file and change the order's status to 'partially_returned'.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="update_user_address", kwargs={"user_id": "ava_moore_2033", "address": {"address1": "101 Pine St", "address2": "", "city": "San Antonio", "state": "TX", "zip": "78234", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "processed_order_id": "#W4817420",
            "returned_item_id": "3812493782",
            "new_stock_level": 24,
            "updated_zip_code": "78234",
            "reactivated_supply_order_id": "#SO6998",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_016",
        instruction="As a senior manager, you are conducting a full audit of the supplier 'Tech Supplies Inc.' (#SUP0001), triggered by a stockout issue affecting customer Mason Johansson's order, #W9549057. Your task is to investigate the customer's order and account, review the supplier's product catalog, and perform necessary data cleanup. First, get the full details for the customer and their order. Then, investigate the 'T-Shirt' (product #9523456873) to confirm the stock status of the item in the order. You must also cancel the supplier's pending supply order #SO9359, as the item is no longer required. Following this, you must discontinue the 'blue cotton crew neck' T-shirt (item #9612497925) from the same supplier by updating its stock and availability. To clear out remaining inventory of another T-shirt, update the price of the 'black cotton crew neck XXL' (item #3799046073) to $50.00. Finally, mark the customer's original order as 'audit_complete'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W9549057"}),
            Action(name="get_user_details", kwargs={"user_id": "mason_johansson_2485"}),
            Action(name="get_product_details", kwargs={"product_id": "9523456873"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "9612497925", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "9523456873", "item_id": "9612497925", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "9523456873", "item_id": "3799046073", "price": 50.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W9549057", "status": "audit_complete"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0001",
            "cancelled_supply_order_id": "#SO9359",
            "discontinued_item_id": "9612497925",
            "audited_order_id": "#W9549057",
            "price_updated_item_id": "3799046073",
            "new_price": 50.00,
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_017",
        instruction="You are a customer service manager handling a return and address change for Ava Lopez (user ID: ava_lopez_2676) regarding her pending order #W8327915. She is returning the '17-inch black i7 Laptop' (item #1684786391) and needs to update her address to 229 Lakeview Drive, Suite 400, Chicago, IL, 60637. Your task is to process this partial return by restocking the item with its supplier. While reviewing the supplier's records, you identify an obsolete cancelled supply order (#SO5813) that needs to be deleted. You also decide to increase the price of the 'black polarized plastic Sunglasses' (item #4358482460) from her order to $295.00. Finalize the process by updating the customer's address and marking the order as 'partially_returned'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W8327915"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_lopez_2676"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1684786391"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1684786391", "value": 111}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="update_user_address", kwargs={"user_id": "ava_lopez_2676", "address": {"address1": "229 Lakeview Drive", "address2": "Suite 400", "city": "Chicago", "state": "IL", "zip": "60637", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "7314138884"}),
            Action(name="update_variant_price", kwargs={"product_id": "7314138884", "item_id": "4358482460", "price": 295.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W8327915", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "ava_lopez_2676",
            "returned_item_id": "1684786391",
            "new_stock_level": 111,
            "deleted_supply_order_id": "#SO5813",
            "updated_zip_code": "60637",
            "price_updated_item_id": "4358482460",
            "new_price": 295.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_018",
        instruction="As a product manager, you're performing a data cleanup and strategic update for 'Tech Haven Supplies' (#SUP0004). First, get a list of all products they supply. For their 'Wireless Earbuds' product line (product #9924732112), you need to ensure the 'black 8-hour' variant (item #2499294441) is marked as unavailable, as it has been discontinued. You also need to delete an obsolete cancelled supply order (#SO9426) for this supplier. To boost sales of a different product, update the price of the '7-inch Wi-Fi + Cellular' E-Reader (item #4273929280) to a promotional price of $240.00. Verify all your changes by retrieving the final details for both modified variants.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_product_details", kwargs={"product_id": "9924732112"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0004", "item_id": "2499294441"}),
            Action(name="update_variant_availability", kwargs={"product_id": "9924732112", "item_id": "2499294441", "available": False}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO9426"}),
            Action(name="get_product_details", kwargs={"product_id": "3801771308"}),
            Action(name="update_variant_price", kwargs={"product_id": "3801771308", "item_id": "4273929280", "price": 240.00}),
            Action(name="get_variant_details", kwargs={"item_id": "2499294441"}),
            Action(name="get_variant_details", kwargs={"item_id": "4273929280"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0004",
            "discontinued_item_id": "2499294441",
            "deleted_supply_order_id": "#SO9426",
            "price_updated_item_id": "4273929280",
            "new_price": 240.00
        }
    ),
        Task(
        annotator="0",
        user_id="USER_019",
        instruction="As a senior manager, you are handling a complex inventory and pricing update for 'Global Tech Distributors' (#SUP0002) following the cancellation of a large laptop supply order (#SO5813). Your task is to adjust the catalog to reflect this. You must make the '17-inch silver i9' laptop (item #3265035808) unavailable for purchase. To compensate for potential lost revenue, you will increase the price of the '15-inch black i9' laptop (item #2913673670) to $2750.00 and the '13-inch black i7' laptop (item #1657832319) to $2750.00. Concurrently, you must process a customer return for order #W9077205, which contains an item from a different supplier. Restock the 'Dumbbell Set' and update the order status to 'completed_return'.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4760268021", "item_id": "3265035808", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "4760268021", "item_id": "2913673670", "price": 2750.00}),
            Action(name="update_variant_price", kwargs={"product_id": "4760268021", "item_id": "1657832319", "price": 2750.00}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "completed_return"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0002",
            "item_made_unavailable": "3265035808",
            "price_updated_item_1": "2913673670",
            "price_updated_item_2": "1657832319",
            "returned_order_id": "#W9077205",
            "restocked_item_id": "3877338112",
            "final_order_status": "completed_return"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_020",
        instruction="You are a retail manager resolving a customer complaint from Mei Gonzalez (user ID: mei_gonzalez_4785) about her order #W7303089. The 'Backpack' (item #2492465580) she received is the wrong size. She is returning it, and you have also been asked to correct her address on file to 858 Elm Street, Suite 912, San Jose, CA, 95170. Your task is to process the return by restocking the backpack with its supplier. While doing so, you notice the 'green leather' backpack (item #7251508981) from the same supplier is discontinued; you need to make it unavailable in the product catalog. After updating the customer's address, you must also expedite a pending supply order (#SO5398) for the other item in her order, the 'Pet Bed', and finally, update the order status to 'partially_returned'.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="update_user_address", kwargs={"user_id": "mei_gonzalez_4785", "address": {"address1": "858 Elm Street", "address2": "Suite 912", "city": "San Jose", "state": "CA", "zip": "95170", "country": "USA"}}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": 189}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "7251508981", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="update_order_status", kwargs={"order_id": "#W7303089", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "updated_zip_code": "95170",
            "returned_item_id": "2492465580",
            "new_stock_level": 189,
            "discontinued_item_id": "7251508981",
            "expedited_supply_order": "#SO5398",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_021",
        instruction="As a product manager, you're conducting a pricing and availability audit of the 'Espresso Machine' product line (product #4354588079) from supplier #SUP0009. You have decided to discontinue the '1L manual' variant (item #3714494375) and must update its stock status and availability accordingly. To clear out remaining inventory of another model, the '2L manual' variant (item #7774234341), you are reducing its price to a promotional $2700.00. While reviewing this supplier, you must also clean up their data by deleting the obsolete cancelled supply order #SO7642. Finally, verify all your changes by retrieving the final details for both of the espresso machine variants you modified.",
        actions=[
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "3714494375"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "3714494375", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4354588079", "item_id": "3714494375", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "4354588079", "item_id": "7774234341", "price": 2700.00}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO7642"}),
            Action(name="get_variant_details", kwargs={"item_id": "3714494375"}),
            Action(name="get_variant_details", kwargs={"item_id": "7774234341"})
        ],
        outputs={
            "discontinued_item_id": "3714494375",
            "price_updated_item_id": "7774234341",
            "new_price": 2700.00,
            "deleted_supply_order_id": "#SO7642"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_022",
        instruction="As a senior manager, you are handling a request from Lucas Martin (user ID: lucas_martin_4549) regarding his pending order #W9318778. He wants to cancel two items, the 'Bicycle' (#2143041831) and the 'Wall Clock' (#9850781806), and update his address to 758 Lakeview Drive, Suite 400, Washington, DC, 20517. Your task is to process this partial cancellation by restocking both items with their correct suppliers. During the process, you notice another 'Wall Clock' variant (#6508153405) is mispriced and must be corrected to $195.00. Finally, update the customer's address and change the order's status to reflect the partial cancellation.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W9318778"}),
            Action(name="get_product_details", kwargs={"product_id": "9783735446"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2143041831"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2143041831", "value": 123}),
            Action(name="get_product_details", kwargs={"product_id": "2344688344"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "9850781806"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "9850781806", "value": 90}),
            Action(name="update_variant_price", kwargs={"product_id": "2344688344", "item_id": "6508153405", "price": 195.00}),
            Action(name="update_user_address", kwargs={"user_id": "lucas_martin_4549", "address": {"address1": "758 Lakeview Drive", "address2": "Suite 400", "city": "Washington", "state": "DC", "zip": "20517", "country": "USA"}}),
            Action(name="update_order_status", kwargs={"order_id": "#W9318778", "status": "partially_cancelled"})
        ],
        outputs={
            "customer_user_id": "lucas_martin_4549",
            "order_id": "#W9318778",
            "cancelled_item_count": 2,
            "updated_zip_code": "20517",
            "price_updated_item_id": "6508153405",
            "new_price": 195.00,
            "final_order_status": "partially_cancelled"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_023",
        instruction="You are a senior manager conducting a full audit of the supplier 'Tech Supplies Inc.' (#SUP0001). Your task is to get a complete list of their product lines and review the available variants for their 'Digital Camera' product. During the audit, you discover that the '30MP, 5x zoom' variant (item #6384525445) is incorrectly marked as available and must be updated to unavailable. You also find an unnecessary pending supply order, #SO9359, which needs to be cancelled. Concurrently, you must review customer order #W8935389, which contains other items from this supplier, to check its payment and tracking history. Finally, update the order's status to 'audit_complete'.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="get_product_details", kwargs={"product_id": "8940227892"}),
            Action(name="list_available_variants", kwargs={"product_id": "8940227892"}),
            Action(name="update_variant_availability", kwargs={"product_id": "8940227892", "item_id": "6384525445", "available": False}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W8935389"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W8935389"}),
            Action(name="update_order_status", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0001",
            "data_corrected_item_id": "6384525445",
            "cancelled_supply_order": "#SO9359",
            "audited_customer_order": "#W8935389",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_024",
        instruction="As a customer service manager, you're assisting Mei Ahmed (user ID: mei_ahmed_5058) with her pending order #W2631563. She needs to update her address to 833 Hickory Lane, Suite 1000, Columbus, OH, 43197. After updating her address, you notice the 'Smart Thermostat' in her order is out of stock, causing the delay. To resolve this, you must find the related pending supply order from the supplier (#SO9359) and expedite it. You also notice the 'Garden Hose' (item #5753502325) is mispriced; correct it to $99.99. Finally, ship the available 'Garden Hose' from her order using tracking ID 349832798095 and update the order status to reflect the partial shipment.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="update_user_address", kwargs={"user_id": "mei_ahmed_5058", "address": {"address1": "833 Hickory Lane", "address2": "Suite 1000", "city": "Columbus", "state": "OH", "zip": "43197", "country": "USA"}}),
            Action(name="get_order_details", kwargs={"order_id": "#W2631563"}),
            Action(name="get_product_details", kwargs={"product_id": "4896585277"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "2791467853"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "6679515468"}),
            Action(name="update_variant_price", kwargs={"product_id": "6679515468", "item_id": "5753502325", "price": 99.99}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W2631563", "tracking_ids": ["349832798095"], "item_ids": ["5753502325"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W2631563", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "mei_ahmed_5058",
            "out_of_stock_item": "2791467853",
            "expedited_supply_order": "#SO9359",
            "price_updated_item": "5753502325",
            "new_tracking_id": "349832798095",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_025",
        instruction="As a senior analyst, you are auditing a fulfilled supply order, #SO6503, for 'Tech Supplies Inc.' (#SUP0001) to ensure inventory accuracy. Your task is to identify the item from the supply order, check its current stock level, and update it to reflect the delivered quantity of 35 units. During the audit, you also notice a pending supply order for the same supplier, #SO9359, which is now redundant and needs to be cancelled. Concurrently, you must investigate a related customer order, #W8935389, which contains a different product from this supplier. Your investigation should include a full review of the customer's details, the order's payment history, and an update of the order's status to 'audit_complete'.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6503"}),
            Action(name="get_product_details", kwargs={"product_id": "8940227892"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "7255224608"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "7255224608", "value": 35}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_user_details", kwargs={"user_id": "raj_li_8594"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W8935389"}),
            Action(name="update_order_status", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs={
            "audited_supply_order": "#SO6503",
            "inventory_corrected_item": "7255224608",
            "new_stock_level": 35,
            "cancelled_supply_order": "#SO9359",
            "audited_customer_order": "#W8935389",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_026",
        instruction="As a senior analyst, you are auditing customer Ethan Lopez (user ID: ethan_lopez_6291) and his pending order #W6779827. You must retrieve his full user details, all associated payment methods, and his complete order history. During a review of the pending order's items, you identify a pricing error on the 'Dumbbell Set' (item #7896397433) and must update it to $460.00. You also notice the 'Coffee Maker' (item #1323134954) is out of stock; make this item unavailable in the product catalog to prevent further orders. Finally, since the order is now stalled due to the stockout, update its status to 'awaiting_inventory'.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "ethan_lopez_6291"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "ethan_lopez_6291"}),
            Action(name="get_user_orders", kwargs={"user_id": "ethan_lopez_6291"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6779827"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="update_variant_price", kwargs={"product_id": "7233192239", "item_id": "7896397433", "price": 460.00}),
            Action(name="get_product_details", kwargs={"product_id": "7996920482"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "1323134954"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7996920482", "item_id": "1323134954", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W6779827", "status": "awaiting_inventory"})
        ],
        outputs={
            "audited_customer_id": "ethan_lopez_6291",
            "audited_order_id": "#W6779827",
            "price_updated_item": "7896397433",
            "new_price": 460.00,
            "unavailable_item_id": "1323134954",
            "final_order_status": "awaiting_inventory"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_027",
        instruction="As a senior operations manager, you are auditing a delivered order, #W4817420, for customer Ava Moore (ZIP: 78234), who has now reported that the 'Action Camera' (item #6700049080) she received is defective. Your goal is to process a return and investigate the root cause of the stock issue. You need to trace the product to its supplier, verify its stock status, and examine the related cancelled supply order, #SO6998, that has caused this stockout. To prevent further issues, you must reactivate the supply order, update the product's availability in the catalog to reflect its out-of-stock status, and finally, update the customer's order to 'pending_return' to officially log the return.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "order_id": "#W4817420",
            "defective_item_id": "6700049080",
            "supplier_id": "#SUP0011",
            "reactivated_supply_order": "#SO6998",
            "final_availability": False,
            "final_order_status": "pending_return"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_028",
        instruction="As a logistics manager, you are auditing shipment with tracking ID 889070895653. Your task is to perform a full trace on this shipment, identify the associated order (#W7303089) and customer (Mei Gonzalez), and review the customer's complete order history. The audit reveals that the 'Pet Bed' (item #7381052709) in the order is from a supplier, 'Books and More', who has an unrelated, obsolete cancelled supply order (#SO6998) on file that needs to be deleted. You also notice the 'Backpack' from the same order is underpriced; update the price of variant #2492465580 to $210.00. Finally, mark the customer's order as 'audit_complete'.",
        actions=[
            Action(name="find_courier_by_tracking_id", kwargs={"tracking_id": "889070895653"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_orders", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_price", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 210.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W7303089", "status": "audit_complete"})
        ],
        outputs={
            "audited_tracking_id": "889070895653",
            "audited_order_id": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "deleted_supply_order_id": "#SO6998",
            "price_updated_item": "2492465580",
            "new_price": 210.00,
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_029",
        instruction="You are a customer service manager handling a return request from Ava Moore (user ID: ava_moore_2033) for her order #W4817420. She is returning the 'Hiking Boots' (item #3812493782) and has also requested to update her address to 996 Cedar Street, Suite 700, San Antonio, TX, 78234. Your task is to process the return by restocking the boots with their supplier. While doing so, you discover an obsolete cancelled supply order (#SO5813) for that supplier that must be deleted. After updating the customer's address, you also need to adjust the price of another item from her original order, the 'Bookshelf' (item #4900661478), to $475.00. Finally, update the order status to 'partially_returned'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="update_user_address", kwargs={"user_id": "ava_moore_2033", "address": {"address1": "996 Cedar Street", "address2": "Suite 700", "city": "San Antonio", "state": "TX", "zip": "78234", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "8600330539"}),
            Action(name="update_variant_price", kwargs={"product_id": "8600330539", "item_id": "4900661478", "price": 475.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "processed_order_id": "#W4817420",
            "returned_item_id": "3812493782",
            "new_stock_level": 24,
            "updated_zip_code": "78234",
            "deleted_supply_order_id": "#SO5813",
            "price_updated_item_id": "4900661478",
            "new_price": 475.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction="You are a manager processing a return for customer Raj Li (user ID: raj_li_8594) from his order #W8935389. He is returning the 'Tablet' (item #4803681337). Your task is to process the return by restocking the item with its supplier. While reviewing the supplier's records, you identify an obsolete pending supply order (#SO5993) which should be deleted. To help drive sales for another product from the same supplier, you decide to lower the price of the 'gray leather sneakers' (item #2509076505) to $185.00. Finally, update the original order's status to 'partially_returned' to complete the process.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_user_details", kwargs={"user_id": "raj_li_8594"}),
            Action(name="get_product_details", kwargs={"product_id": "8024098596"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0003", "item_id": "4803681337"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0003", "item_id": "4803681337", "value": 194}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="get_product_details", kwargs={"product_id": "7471004230"}),
            Action(name="update_variant_price", kwargs={"product_id": "7471004230", "item_id": "2509076505", "price": 185.00}),
            Action(name="update_order_status", kwargs={"order_id": "#W8935389", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "raj_li_8594",
            "returned_item_id": "4803681337",
            "new_stock_level": 194,
            "deleted_supply_order_id": "#SO5993",
            "price_updated_item_id": "2509076505",
            "new_price": 185.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_0031",
        instruction="You are a logistics manager reviewing a 'lost in transit' claim for order #W9549057 from customer Mason Johansson (user ID: mason_johansson_2485). Conduct a full investigation by reviewing the order details, the customer's payment history, and the original tracking information. You must then check the stock for both items in the order. Since the 'T-Shirt' (item #5253880258) is out of stock, you need to find its pending supply order (#SO9359) and expedite it. For the available 'Makeup Kit', arrange an immediate re-shipment using new tracking ID 202468403681 and update the order status to 'partially_shipped'.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mason_johansson_2485"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9549057"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W9549057"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9549057"}),
            Action(name="get_product_details", kwargs={"product_id": "9523456873"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "5149340237"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9549057", "tracking_ids": ["202468403681"], "item_ids": ["7736359414"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9549057", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "mason_johansson_2485",
            "order_id": "#W9549057",
            "out_of_stock_item_id": "5253880258",
            "expedited_supply_order_id": "#SO9359",
            "reshimpped_item_id": "7736359414",
            "new_tracking_id": "202468403681",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction="You are a manager conducting a full audit of customer Mei Gonzalez (user ID: mei_gonzalez_4785) and her delivered order #W7303089. The audit requires a complete review of her account, payment methods, and the full logistics trail of the shipment. During the product review, you decide to discontinue the 'Backpack' (item #2492465580) she ordered. You also need to address an inventory discrepancy for the other item in her order, a 'Pet Bed' (item #7381052709), by correcting its stock level to 35 units. Finally, you must update the price of the Pet Bed to a new promotional price of $189.99.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "7381052709", "value": 35}),
            Action(name="update_variant_price", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 189.99})
        ],
        outputs={
            "audited_customer_id": "mei_gonzalez_4785",
            "audited_order_id": "#W7303089",
            "discontinued_item_id": "2492465580",
            "stock_corrected_item_id": "7381052709",
            "new_stock_level": 35,
            "new_price": 189.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction="You are a senior manager conducting a full audit of customer Mei Gonzalez (user ID: mei_gonzalez_4785) and her delivered order #W7303089. The audit requires a complete review of her account, payment methods, and the full logistics trail of the shipment. During the product review, you decide to discontinue the 'Backpack' (item #2492465580) she ordered. Concurrently, you notice a data error: the 'Pet Bed' (item #7381052709) from her order is priced at $193.22, which is incorrect. You must correct the price to $199.99, while also carrying out the discontinuation of the backpack by updating its stock status and availability.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_variant_price", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99})
        ],
        outputs={
            "audited_customer_id": "mei_gonzalez_4785",
            "audited_order_id": "#W7303089",
            "discontinued_item_id": "2492465580",
            "price_updated_item_id": "7381052709",
            "new_price": 199.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction="As a senior manager, you are auditing the supplier 'Kitchen Essentials Co.' (#SUP0012). Your task is to get a complete overview of their products and review the available variants for their 'Fleece Jacket' product line. You notice that the 'L black full-zip' variant (item #9385662952) is marked as available in the product catalog but is listed as out of stock by the supplier; you must correct this data inconsistency. You also need to delete an obsolete cancelled supply order, #SO7147, associated with this supplier. To complete your audit, review the full order history of a related customer, Amelia Wilson (user ID: amelia_wilson_4614), and then update the status of her most recent order, #W9077205, to 'audit_pending'.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_product_details", kwargs={"product_id": "8560156827"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952"}),
            Action(name="update_variant_availability", kwargs={"product_id": "8560156827", "item_id": "9385662952", "available": False}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="get_user_details", kwargs={"user_id": "amelia_wilson_4614"}),
            Action(name="get_user_orders", kwargs={"user_id": "amelia_wilson_4614"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "audit_pending"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0012",
            "data_corrected_item_id": "9385662952",
            "deleted_supply_order_id": "#SO7147",
            "audited_customer_id": "amelia_wilson_4614",
            "audited_order_id": "#W9077205",
            "final_order_status": "audit_pending"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction="You are a customer service manager handling a return from Ava Moore (user ID: ava_moore_2033) for her delivered order, #W4817420. She is returning the 'Electric Kettle' (item #9624127908) and would also like to update her address to 996 Cedar Street, Suite 700, San Antonio, TX, 78234. Your task is to process this return by restocking the item with its supplier. While doing so, you identify an obsolete cancelled supply order (#SO5813) for the supplier of another item in her order, which must be deleted. As a goodwill gesture, you also decide to adjust the price of the 'Bookshelf' (item #4900661478) from her original order to $450.00. Before finalizing the return, review the tracking history of the order to confirm delivery and return events. Finally, update her address and mark the order as 'partially_returned'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_product_details", kwargs={"product_id": "1075968781"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908", "value": 194}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="update_user_address", kwargs={"user_id": "ava_moore_2033", "address": {"address1": "996 Cedar Street", "address2": "Suite 700", "city": "San Antonio", "state": "TX", "zip": "78234", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "8600330539"}),
            Action(name="update_variant_price", kwargs={"product_id": "8600330539", "item_id": "4900661478", "price": 450.00}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W4817420"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "returned_item_id": "9624127908",
            "new_stock_level": 194,
            "deleted_supply_order_id": "#SO5813",
            "updated_zip_code": "78234",
            "price_updated_item_id": "4900661478",
            "new_price": 450.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction="You are a product manager performing a strategic overhaul of the 'Fleece Jacket' product line (product #8560156827) from supplier 'Kitchen Essentials Co.' (#SUP0012). Your goal is to discontinue several variants and adjust pricing on the remaining ones. You must make the 'red half-zip' (item #5992316252) and the 'navy full-zip' (item #8161321868) jackets unavailable for purchase by updating their stock status. You also need to delete the related obsolete cancelled supply order #SO7147. To boost sales of the remaining jackets, you must then reduce the price of the 'navy half-zip' variant (item #8590708195) to $155.00. As a final step, please verify all of your changes by retrieving the final details for the three variants you modified.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="get_product_details", kwargs={"product_id": "8560156827"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0012", "item_id": "5992316252", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "8560156827", "item_id": "5992316252", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0012", "item_id": "8161321868", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "8560156827", "item_id": "8161321868", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "8560156827", "item_id": "8590708195", "price": 155.00}),
            Action(name="get_variant_details", kwargs={"item_id": "5992316252"}),
            Action(name="get_variant_details", kwargs={"item_id": "8161321868"}),
            Action(name="get_variant_details", kwargs={"item_id": "8590708195"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0012",
            "deleted_supply_order_id": "#SO7147",
            "discontinued_item_count": 2,
            "price_updated_item_id": "8590708195",
            "new_price": 155.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction="You are a manager handling a data integrity project. You need to investigate and clean up records related to the supplier 'Tech Haven Supplies' (#SUP0004). This requires a full review of their product catalog and the deletion of an obsolete cancelled supply order, #SO9426. During your product review, you decide to discontinue the '4-piece red hardshell' Luggage Set (item #9956648681). You must also handle an unrelated customer issue for Omar Khan (user ID: omar_khan_2363) whose order, #W6304490, which contains a product from a different supplier, has been flagged for a final audit. You need to verify that customer's full details and the complete shipping history of his order. Finally, you must update the status of his order to 'audit_complete'.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_product_details", kwargs={"product_id": "5426915165"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO9426"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0004", "item_id": "9956648681", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "5426915165", "item_id": "9956648681", "available": False}),
            Action(name="get_user_details", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W6304490"}),
            Action(name="update_order_status", kwargs={"order_id": "#W6304490", "status": "audit_complete"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0004",
            "deleted_supply_order_id": "#SO9426",
            "discontinued_item_id": "9956648681",
            "audited_customer_id": "omar_khan_2363",
            "audited_order_id": "#W6304490",
            "final_order_status": "audit_complete"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction="You are a senior manager handling a complex customer service and logistics issue for order #W4817420. The customer, Ava Moore (user ID: ava_moore_2033), has reported that the entire shipment was lost, and she requires a replacement. The original order contains multiple items from different suppliers. Your task is to conduct a full investigation, confirm which items are still in stock, and organize a re-shipment for only the available items using 'SwiftMove Couriers' (#COU0004) and tracking ID 757848843226. For the item that is out of stock (the 'Action Camera'), you must find the related cancelled supply order, #SO6998, and reactivate it to resolve the inventory problem. Finally, you must update the customer's order to reflect that a partial re-shipment is on its way.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_user_details", kwargs={"user_id": "ava_moore_2033"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6777246137"}),
            Action(name="get_product_details", kwargs={"product_id": "8600330539"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "4900661478"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="get_product_details", kwargs={"product_id": "1075968781"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908"}),
            Action(name="get_product_details", kwargs={"product_id": "7363354090"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="assign_courier_to_order", kwargs={"order_id": "#W4817420", "courier_id": "#COU0004", "tracking_ids": ["757848843226"], "item_ids": ["6777246137", "4900661478", "9624127908", "3812493782"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partial_reshipment_pending"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "lost_order_id": "#W4817420",
            "out_of_stock_item_id": "6700049080",
            "reactivated_supply_order": "#SO6998",
            "new_tracking_id": "757848843226",
            "final_order_status": "partial_reshipment_pending"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction="You are handling a multi-part request for customer James Li (ZIP: 10083). He is returning the 'Office Chair' (#8426249116) from order #W2611340 and wants to update his address to 215 River Road, Suite 1000, New York, NY, 10083. Process the return by restocking the chair with its supplier, 'Global Tech Distributors'. While doing so, you notice this supplier had a supply order for a 'Laptop' (#SO5813) cancelled. To mitigate a potential stockout of that laptop (item #3265035808), increase its price to $2550.00 and make it temporarily unavailable. Finally, update the customer's address and change the original order's status to 'partially_returned'.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "James", "last_name": "Li", "zip": "10083"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="update_user_address", kwargs={"user_id": "james_li_5688", "address": {"address1": "215 River Road", "address2": "Suite 1000", "city": "New York", "state": "NY", "zip": "10083", "country": "USA"}}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="update_variant_price", kwargs={"product_id": "4760268021", "item_id": "3265035808", "price": 2550.00}),
            Action(name="update_variant_availability", kwargs={"product_id": "4760268021", "item_id": "3265035808", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "james_li_5688",
            "processed_order_id": "#W2611340",
            "returned_item_id": "8426249116",
            "new_stock_level": 158,
            "updated_zip_code": "10083",
            "price_updated_item_id": "3265035808",
            "new_price": 2550.00,
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction="You are a manager auditing a delivered order, #W6304490, for customer Omar Khan (user ID: omar_khan_2363). The audit requires a full review of the customer's payment history for the order and the full logistics trail, including the courier. During the product audit, you discover that two items from the order have since been discontinued by their suppliers: the 'Skateboard' (item #6956751343) and the 'Smart Thermostat' (item #4983901480). You must update the availability for both of these items in the product catalog to prevent future sales. As a final step, you have decided to adjust the price of a different, high-stock item from the order, the 'Garden Hose' (item #5753502325), to $90.00.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W6304490"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W6304490"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0010"}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="update_variant_availability", kwargs={"product_id": "1968349452", "item_id": "6956751343", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "4896585277"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": False}),
            Action(name="get_product_details", kwargs={"product_id": "6679515468"}),
            Action(name="update_variant_price", kwargs={"product_id": "6679515468", "item_id": "5753502325", "price": 90.00})
        ],
        outputs={
            "audited_order_id": "#W6304490",
            "discontinued_item_1": "6956751343",
            "discontinued_item_2": "4983901480",
            "price_updated_item": "5753502325",
            "new_price": 90.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction="You are a manager resolving a complex return for customer Amelia Wilson (user ID: amelia_wilson_4614) regarding her order #W9077205. She is returning two items: the 'Jigsaw Puzzle' (item #9370300555) and the 'Dumbbell Set' (item #3877338112). While processing the return, you notice that the supplier for the dumbbell set, 'Sports Gear Suppliers', has a fulfilled supply order (#SO5817) that was never correctly logged in inventory. Your task is to process the customer's return by restocking both items with their respective suppliers, and also to correct the inventory error by adding the units from the fulfilled supply order to the appropriate item stock.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "completed_return"}),
            Action(name="get_product_details", kwargs={"product_id": "1808611083"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555", "value": 72}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813", "value": 142})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "processed_order_id": "#W9077205",
            "returned_item_1": "9370300555",
            "returned_item_2": "3877338112",
            "corrected_supply_order_id": "#SO5817",
            "inventory_corrected_item_id": "8591113813",
            "new_stock_level": 142
        }
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction="You are a manager conducting a full audit of a delivered order, #W7303089, for customer Mei Gonzalez (user ID: mei_gonzalez_4785). The audit requires a complete verification of the customer's payment methods, the order's financial transaction, and the full shipment details, including the courier responsible. During your analysis of the order's items, you've been alerted that the 'Backpack' (item #2492465580) is part of a product line being discontinued. You must update its stock status to 'discontinued' with its supplier and make it unavailable in the public product catalog.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"})
        ],
        outputs={
            "audited_order_id": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "courier_id": "#COU0001",
            "discontinued_item_id": "2492465580",
            "final_stock_status": "discontinued"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction="You are a product manager performing a strategic review of the 'Office Supplies Hub' supplier (#SUP0008). Your goal is to get a complete overview of their catalog and clean up their associated data. You must retrieve a list of all products they supply and review the available variants for their 'Desk Lamp' product line. During the review, you decide to discontinue the 'black AC adapter' lamp (item #7624783998) due to poor performance. You must update its stock status and availability. You also find two obsolete cancelled supply orders (#SO5916, #SO1037) for this supplier that need to be deleted from the system. Finally, to understand the sales performance of this supplier, you need to conduct a full review of a customer order, #W2611340, which contains an item from a different supplier but was placed by a customer who also buys 'Office Supplies Hub' products.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="list_available_variants", kwargs={"product_id": "6817146515"}),
            Action(name="get_variant_details", kwargs={"item_id": "7624783998"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "6817146515", "item_id": "7624783998", "available": False}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5916"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO1037"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_user_details", kwargs={"user_id": "james_li_5688"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0008",
            "discontinued_item_id": "7624783998",
            "deleted_supply_order_count": 2,
            "audited_customer_order": "#W2611340"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction="As a senior manager, you are resolving a lost shipment claim for customer Amelia Wilson (user ID: amelia_wilson_4614) regarding her delivered order #W9077205. She has also requested to update her shipping address to 388 Elm Avenue, Suite 500, Dallas, TX, 75215. Your task is to conduct a full investigation of the original shipment, including the courier involved, and then organize a complete replacement. After verifying that all items are in stock, you must also address a low-stock alert for the 'Jigsaw Puzzle' by expediting its pending supply order (#SO6372). Finally, you must update the customer's address and assign a new courier, 'FastTrack Couriers', with tracking ID 682308736931 to ship the replacement order.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_user_details", kwargs={"user_id": "amelia_wilson_4614"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9077205"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0009"}),
            Action(name="get_product_details", kwargs={"product_id": "1808611083"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(
                name="update_user_address",
                kwargs={
                    "user_id": "amelia_wilson_4614",
                    "address": {
                        "address1": "388 Elm Avenue",
                        "address2": "Suite 500",
                        "city": "Dallas",
                        "state": "TX",
                        "zip": "75215",
                        "country": "USA"
                    }
                }
            ),
            Action(name="find_courier_by_tracking_id", kwargs={"tracking_id": "682308736931"}),
            Action(
                name="assign_courier_to_order",
                kwargs={
                    "order_id": "#W9077205",
                    "courier_id": "#COU0001",
                    "tracking_ids": ["682308736931"],
                    "item_ids": ["9370300555", "3877338112"]
                }
            ),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "processing"})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "original_order_id": "#W9077205",
            "updated_zip_code": "75215",
            "expedited_supply_order": "#SO6372",
            "new_tracking_id": "682308736931",
            "final_order_status": "processing"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_045",
        instruction="You are a manager resolving a customer issue for Mei Gonzalez (user ID: mei_gonzalez_4785). She has received her order #W7303089, but the 'Backpack' (item #2492465580) is the wrong color. She wishes to return it. Your task is to process this partial return and handle all related inventory and data updates. You must trace the item to its supplier and restock it. You've also noticed the customer's address on file is incomplete and must be updated to '858 Elm Street, Suite 912, San Jose, CA, 95170'. While reviewing the supplier's other products, you decide to discontinue the 'green leather backpack' (item #7251508981) due to quality concerns, which requires updating its stock status and availability. Finally, you must update the original order's status to reflect the completed partial return.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="update_user_address", kwargs={"user_id": "mei_gonzalez_4785", "address": {"address1": "858 Elm Street", "address2": "Suite 912", "city": "San Jose", "state": "CA", "zip": "95170", "country": "USA"}}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": 189}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "7251508981", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "7251508981", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W7303089", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "updated_zip_code": "95170",
            "returned_item_id": "2492465580",
            "new_stock_level": 189,
            "discontinued_item_id": "7251508981",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction="As a senior operations analyst, you are performing a full audit of a delivered customer order, #W7303089. Your task is to investigate the entire lifecycle of this order, including customer details, payment history, and the full logistics trail from the courier. During your investigation into the products ordered, you must address two separate issues. First, you need to resolve a supply chain bottleneck for the supplier of the 'Pet Bed' by expediting their pending supply order, #SO5398. Second, you must process the discontinuation of the 'Backpack' variant (item #2492465580) from the order by updating its stock status and making it unavailable for future purchase.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5398"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False})
        ],
        outputs={
            "audited_order_id": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "courier_id": "#COU0001",
            "expedited_supply_order_id": "#SO5398",
            "discontinued_item_id": "2492465580"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="You are a manager conducting a full audit of customer Mei Gonzalez (user ID: mei_gonzalez_4785) and her account activity. You need to retrieve her complete order history and all registered payment methods. For her delivered order #W7303089, you must perform a deep dive, analyzing the full shipping history and identifying the courier. As part of a product line review related to this order, you decide to discontinue the 'Backpack' variant she purchased (item #2492465580). You also need to address an inventory discrepancy for the other item in her order, a 'Pet Bed' (item #7381052709), by correcting its stock level to 35 units.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_orders", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "7381052709", "value": 35})
        ],
        outputs={
            "audited_customer_id": "mei_gonzalez_4785",
            "audited_order_id": "#W7303089",
            "discontinued_item_id": "2492465580",
            "stock_corrected_item_id": "7381052709",
            "new_stock_level": 35
        }
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction="As a senior manager, you are resolving a multi-part request for customer Sofia Rossi (user ID: sofia_rossi_8776) regarding her pending order, #W5918442. She wishes to cancel this entire order and has also requested to update her address on file to '456 Market St, San Francisco, CA, 94105'. Your task is to execute these requests and perform a full inventory reconciliation. You must cancel the order, update her profile, and then restock every item from the cancelled order with its correct supplier. During this process, you will discover an 'Action Camera' (item #1586641416) is incorrectly marked as discontinued; you must correct this data error by setting its stock to 10 units and making it available for sale.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="get_user_details", kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="update_user_address", kwargs={"user_id": "sofia_rossi_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "CA", "zip": "94105", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "6858788497"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "cancelled_order_id": "#W5918442",
            "updated_zip_code": "94105",
            "data_corrected_item_id": "1586641416",
            "restocked_items_count": 4
        }
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction="As a senior manager, you are handling a cancellation request for order #W8327915 from customer Ava Lopez (user ID: ava_lopez_2676). She wants to cancel the 'Skateboard' (item #6956751343) from her order. Your task is to process this partial cancellation by restocking the item with its supplier. While reviewing the order, you discover that the 'Air Purifier' (item #1327854740) is discontinued, so you must make it unavailable in the product catalog. You also need to delete an obsolete supply order (#SO6767) for the skateboard's supplier. Finally, ship the remaining available items from her order using tracking ID '956166462388' and update the order status to 'partially_shipped'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W8327915"}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "6956751343"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "6956751343", "value": 35}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="update_variant_availability", kwargs={"product_id": "3821016478", "item_id": "1327854740", "available": False}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO6767"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W8327915", "tracking_ids": ["956166462388"], "item_ids": ["2025713343", "1684786391", "4358482460"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W8327915", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "ava_lopez_2676",
            "cancelled_item_id": "6956751343",
            "new_stock_level": 35,
            "discontinued_item_id": "1327854740",
            "deleted_supply_order_id": "#SO6767",
            "new_tracking_id": "956166462388",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction="As a senior manager, you are conducting a full audit of the supplier 'Home Essentials Co.' (#SUP0006). Your task is to get a complete overview of their product catalog, including all available variants for their 'Patio Umbrella' line, and to perform necessary data cleanup. This includes removing an obsolete cancelled supply order, #SO3933. You must also correct an inventory data error for their 'red olefin' patio umbrella (item #8170914468) by updating its stock to 50 units. To complete your audit, you will also analyze the full order history of a related customer, Yusuf Khan (user ID: yusuf_khan_7091), and review the details of his order #W1787190.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="get_product_details", kwargs={"product_id": "9743693396"}),
            Action(name="list_available_variants", kwargs={"product_id": "9743693396"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468", "value": 50}),
            Action(name="get_user_details", kwargs={"user_id": "yusuf_khan_7091"}),
            Action(name="get_user_orders", kwargs={"user_id": "yusuf_khan_7091"}),
            Action(name="get_order_details", kwargs={"order_id": "#W1787190"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0006",
            "deleted_supply_order_id": "#SO3933",
            "inventory_corrected_item_id": "8170914468",
            "new_stock_level": 50,
            "audited_customer_id": "yusuf_khan_7091"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction="You are a senior analyst conducting a full review of the supplier 'Office Supplies Hub' (#SUP0008). Your task is to get a complete list of all products they supply and review the available variants for their 'Desk Lamp' product line. During your audit, you discover that their pending supply order #SO5771 is for an item with low demand. To better allocate resources, you must cancel this supply order. Subsequently, you need to review the full order history of a customer, Sofia Rossi (user ID: sofia_rossi_8776), who has previously purchased items from this supplier, and investigate the details of her order #W5918442 to understand sales performance. Finally, you have decided to discontinue the 'green latex garden hose' (item #3230708338) from this supplier; you must update its stock status and make it unavailable for purchase.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="list_available_variants", kwargs={"product_id": "6817146515"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5771", "status": "cancelled"}),
            Action(name="get_user_orders", kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="get_product_details", kwargs={"product_id": "6679515468"}),
            Action(name="update_variant_availability", kwargs={"product_id": "6679515468", "item_id": "3230708338", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "3230708338", "value": "discontinued"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0008",
            "cancelled_supply_order_id": "#SO5771",
            "audited_customer_id": "sofia_rossi_8776",
            "discontinued_item_id": "3230708338",
            "final_stock_status": "discontinued"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction="As a senior manager, you are conducting a full audit centered on a key customer, Mei Gonzalez (user ID: mei_gonzalez_4785), and her delivered order, #W7303089. Your task is to get a complete picture of her account, including all payment methods, and the full logistics trail of her order. The audit must then extend to the suppliers of the items she purchased. For the supplier of the 'Backpack', you are required to list their entire product catalog. For the supplier of the 'Pet Bed', you need to perform a data cleanup by deleting their obsolete cancelled supply order, #SO6998.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO6998"})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "audited_order_id": "#W7303089",
            "supplier_of_first_item": "#SUP0005",
            "supplier_of_second_item": "#SUP0011",
            "deleted_supply_order_id": "#SO6998"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction="You are a customer service lead handling a complex request from a VIP customer, Sofia Rossi (user ID: sofia_rossi_8776). Her recent order, #W5918442, is pending, but she wants to completely change it. She wants to cancel the entire order and also update her address on file to 456 Market St, San Francisco, CA, 94105. Your task is to process this multi-part request. You must cancel her order, update her user profile with the new address, and then perform a full inventory reconciliation for every item in the cancelled order, restocking each one with its correct supplier, with the exception of any items that are already discontinued.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="get_user_details", kwargs={"user_id": "sofia_rossi_8776"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="update_user_address", kwargs={"user_id": "sofia_rossi_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "CA", "zip": "94105", "country": "USA"}}),
            Action(name="get_product_details", kwargs={"product_id": "6858788497"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "cancelled_order_id": "#W5918442",
            "updated_zip_code": "94105",
            "restocked_items_count": 3,
            "not_restocked_item_id": "1586641416"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction="As a senior manager, you are performing a dual role today. First, conduct a full audit of the supplier 'Green Grocers' (#SUP0005). This requires you to get a complete list of their product lines and review all available variants for their 'Bicycle' product. While auditing, you must also clean up their historical data by deleting the obsolete cancelled supply order #SO2516. Separately, you need to resolve a stalled customer order, #W9318778, which is pending due to an out-of-stock item from a different supplier. You must ship the available items from this order immediately using tracking ID 836251433228 and update the order's status.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="list_available_variants", kwargs={"product_id": "9783735446"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9318778"}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9318778", "tracking_ids": ["836251433228"], "item_ids": ["2143041831", "6342039236", "9850781806", "3076708684"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9318778", "status": "partially_shipped"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0005",
            "deleted_supply_order": "#SO2516",
            "stalled_order_id": "#W9318778",
            "out_of_stock_item": "5669664287",
            "new_tracking_id": "836251433228",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction="As a product manager, you are conducting an audit of the 'Tech Haven Supplies' supplier (#SUP0004). Your task is to get a full overview of their product lines and then, for their 'Luggage Set' product (product #5426915165), you need to list all available variants. During this review, you decide to discontinue one of the variants, the '4-piece red hardshell' (item #9956648681), due to poor sales. You must update its stock status and make it unavailable. Concurrently, you need to resolve an issue with a customer order, #W9077205, which contains a different product from another supplier that was returned. You must process this return by restocking the 'Dumbbell Set' (item #3877338112) with its correct supplier.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="get_product_details", kwargs={"product_id": "5426915165"}),
            Action(name="list_available_variants", kwargs={"product_id": "5426915165"}),
            Action(name="update_variant_availability", kwargs={"product_id": "5426915165", "item_id": "9956648681", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0004", "item_id": "9956648681", "value": "discontinued"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65})
        ],
        outputs={
            "audited_supplier_id": "#SUP0004",
            "discontinued_item_id": "9956648681",
            "final_availability": False,
            "restocked_item_id": "3877338112",
            "new_stock_level": 65
        }
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction="You are a product manager performing an audit of the supplier 'Sports Gear Suppliers' (#SUP0010). Your goal is to get a complete overview of their product catalog and clean up obsolete records. You must retrieve a list of all products they supply and then list all available variants for their 'Dumbbell Set' product line. During your review, you discover that an old, cancelled supply order (#SO5817) is still in the system for a different product and needs to be deleted. You also decide to discontinue the '55-75 lbs iron fixed' dumbbell set (item #2444431651) due to low sales. Finally, you need to update the price of the 'adjustable 5-25 lbs rubber' dumbbell set (item #7896397433) to $475.00.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="list_available_variants", kwargs={"product_id": "7233192239"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7233192239", "item_id": "2444431651", "available": False}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "2444431651", "value": "discontinued"}),
            Action(name="update_variant_price", kwargs={"product_id": "7233192239", "item_id": "7896397433", "price": 475.00})
        ],
        outputs={
            "audited_supplier_id": "#SUP0010",
            "supplier_product_count": 3,
            "deleted_supply_order_id": "#SO5817",
            "discontinued_item_id": "2444431651",
            "price_updated_item_id": "7896397433",
            "new_price": 475.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction="You are a product manager conducting a full audit and data refresh for all products supplied by 'Initech' (#SUP0003). Your goal is to ensure all their product listings are accurate. You must retrieve a full list of products they supply and, for their 'Tablet' product line (product #8024098596), you need to get a list of all currently available variants. During your audit, you notice that a specific tablet variant (item #2235648106) is priced incorrectly. You must update its price to $1099.99. You also find an old, pending supply order (#SO5993) for 'Initech' that is no longer needed and must be deleted from the system.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_product_details", kwargs={"product_id": "8024098596"}),
            Action(name="list_available_variants", kwargs={"product_id": "8024098596"}),
            Action(name="get_variant_details", kwargs={"item_id": "2235648106"}),
            Action(name="update_variant_price", kwargs={"product_id": "8024098596", "item_id": "2235648106", "price": 1099.99}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="get_variant_details", kwargs={"item_id": "2235648106"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0003",
            "supplier_product_count": 2,
            "audited_product_id": "8024098596",
            "price_corrected_item": "2235648106",
            "new_price": 1099.99,
            "deleted_supply_order_id": "#SO5993"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="As a supplier relationship manager, you are conducting a full performance audit of a niche supplier, 'Initech' (#SUP0003). Your goal is to get a complete picture of their offerings and sales footprint. You need to list all products they supply and all currently available variants for their 'Sneakers' product line. To understand customer engagement with this supplier, you must also review the full order history for a relevant customer, Mei Ahmed (user ID: mei_ahmed_5058), and investigate the details of her most recent order, #W2631563. Based on your audit, you have decided to increase the price of the 'black synthetic sneaker' (item #6477915553) to $199.99. Please apply this change and verify it.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="get_supplier_products", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="list_available_variants", kwargs={"product_id": "7471004230"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="get_user_orders", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="get_order_details", kwargs={"order_id": "#W2631563"}),
            Action(name="get_variant_details", kwargs={"item_id": "6477915553"}),
            Action(name="update_variant_price", kwargs={"product_id": "7471004230", "item_id": "6477915553", "price": 199.99}),
            Action(name="get_variant_details", kwargs={"item_id": "6477915553"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0003",
            "supplier_product_count": 2,
            "audited_customer_id": "mei_ahmed_5058",
            "customer_order_count": 2,
            "price_updated_item": "6477915553",
            "new_price": 199.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="As a senior logistics manager, you are resolving a lost shipment for order #W2611340, belonging to customer James Li (user ID: james_li_5688). Your goal is to investigate the original shipment and organize a replacement. Please examine the order to identify all items and their suppliers, and then check current inventory levels to confirm what can be re-shipped. As part of a supplier performance audit, you must retrieve the full details for the supplier of the in-stock item. Finally, you need to assign a new courier, 'FastTrack Couriers' (#COU0001), with tracking ID 403338127473 for the available portion of the order and update the order status accordingly.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W2611340"}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="assign_courier_to_order", kwargs={"order_id": "#W2611340", "courier_id": "#COU0001", "tracking_ids": ["403338127473"], "item_ids": ["8426249116"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "partially_shipped"})
        ],
        outputs={
            "original_order_id": "#W2611340",
            "customer_user_id": "james_li_5688",
            "out_of_stock_item": "6469567736",
            "reshipped_item": "8426249116",
            "audited_supplier_id": "#SUP0002",
            "new_courier_id": "#COU0001",
            "new_tracking_id": "403338127473",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction="You are a logistics manager conducting a full audit of a delivered order, #W7303089, for Mei Gonzalez (user ID: mei_gonzalez_4785). The audit requires a complete verification of the customer's payment methods, the order's financial transaction, and the full shipment details, including the courier responsible. During the product audit, you discover that the supplier for the 'Pet Bed' (item #7381052709) has a pending supply order, #SO5398, that needs to be expedited to ensure future stock availability. Additionally, you've decided the 'Backpack' (item #2492465580) from her order is underpriced and must be updated to $229.99.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_price", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 229.99}),
            Action(name="get_variant_details", kwargs={"item_id": "2492465580"})
        ],
        outputs={
            "audited_order_id": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "expedited_supply_order": "#SO5398",
            "price_updated_item": "2492465580",
            "new_price": 229.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction="You are a logistics manager conducting a full audit of 'Global Express Couriers' (#COU0010). Your task is to start with one of their shipments (tracking ID 574237175837) and perform a complete trace. This includes identifying the customer, Omar Khan, reviewing his full order history and payment methods, and examining all items in his order #W6304490. During the product review, you notice the 'Skateboard' (#6956751343) is from a supplier with an obsolete cancelled supply order (#SO2516) that needs to be deleted. You also find that the 'Smart Thermostat' (#4983901480) from the order is out of stock; please make it unavailable. As a final step, update the price of the 'Air Purifier' (#9375701158) in his order to $480.00.",
        actions=[
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0010"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W6304490"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_user_details", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_user_orders", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="get_product_details", kwargs={"product_id": "4896585277"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "3821016478", "item_id": "9375701158", "price": 480.00})
        ],
        outputs={
            "audited_courier_id": "#COU0010",
            "audited_order_id": "#W6304490",
            "customer_user_id": "omar_khan_2363",
            "deleted_supply_order": "#SO2516",
            "item_made_unavailable": "4983901480",
            "price_updated_item": "9375701158",
            "new_price": 480.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction="You are a product manager performing an audit and update on the 'Running Shoes' product line (product #6938111410) from supplier #SUP0006. Due to a cancelled supply order (#SO3933), you have decided to discontinue the 'yellow synthetic' variant (item #9791469541). You must update the catalog to make it unavailable. To drive sales on remaining inventory, you are also creating a promotion. First, verify the current stock and price of the 'red leather' variant (#4153505238) and the 'white mesh' variant (#9635758562). Then, update the price for both the red leather and white mesh variants to a new promotional price of $149.99. Finally, confirm all your changes by retrieving the details for all three variants you interacted with.",
        actions=[
            Action(name="get_product_details", kwargs={"product_id": "6938111410"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="update_variant_availability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="get_variant_details", kwargs={"item_id": "4153505238"}),
            Action(name="get_variant_details", kwargs={"item_id": "9635758562"}),
            Action(name="update_variant_price", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 149.99}),
            Action(name="update_variant_price", kwargs={"product_id": "6938111410", "item_id": "9635758562", "price": 149.99}),
            Action(name="get_variant_details", kwargs={"item_id": "9791469541"}),
            Action(name="get_variant_details", kwargs={"item_id": "4153505238"}),
            Action(name="get_variant_details", kwargs={"item_id": "9635758562"})
        ],
        outputs={
            "product_id": "6938111410",
            "supplier_id": "#SUP0006",
            "discontinued_item_id": "9791469541",
            "promotion_item_1": "4153505238",
            "promotion_item_2": "9635758562",
            "new_price": 149.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction="As a senior manager, please handle a cancellation request for order #W2611340 from customer James Li (user ID: james_li_5688). Your task is to cancel the order and perform a full inventory reconciliation for all items. This requires tracing each item to its supplier and restocking it, but do not restock any items currently listed as 'out_of_stock'. Because one of the items is out of stock, you must also investigate the supplier's pipeline by reviewing their pending supply order #SO5771 and expediting it. To complete the process, you must also retrieve the customer's full user and payment details for the refund team.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_user_details", kwargs={"user_id": "james_li_5688"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "james_li_5688"}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "cancelled"}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158})
        ],
        outputs={
            "cancelled_order_id": "#W2611340",
            "customer_user_id": "james_li_5688",
            "investigated_item_id": "6469567736",
            "restocked_item_id": "8426249116",
            "expedited_supply_order_id": "#SO5771",
            "new_stock_level": 158
        }
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction="You are a senior manager conducting a full audit of the 'Tech Supplies Inc.' supplier (#SUP0001). Your investigation starts with their pending supply order, #SO9359. You need to verify its details and, due to its importance, upgrade its status to 'expedited'. As part of the audit, you must also review a delivered customer order, #W7303089, which contains an item from a different supplier but was handled by a courier, 'FastTrack Couriers', that you are also evaluating. Your task involves a deep dive into this customer order, including verifying the customer's details and payment methods, the full tracking history, and the courier's information. Finally, after your review, you've decided the 'Backpack' (item #2492465580) from this order is priced too low and must be updated to $225.00.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_variant_price", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 225.00}),
            Action(name="get_variant_details", kwargs={"item_id": "2492465580"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0001",
            "expedited_supply_order": "#SO9359",
            "audited_customer_order": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "audited_courier_id": "#COU0001",
            "price_updated_item": "2492465580",
            "new_price": 225.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction="As the operations manager, you need to process a full cancellation for a pending order, #W5918442, for customer Sofia Rossi (ZIP: 78784), who no longer needs the items. Your task is to cancel the order and then perform a complete inventory reconciliation. For every item in her order, you must trace it back to its specific supplier and add the quantity back to their inventory. However, do not restock any items that are already marked as 'discontinued' by the supplier.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="get_product_details", kwargs={"product_id": "6858788497"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "cancelled_order_id": "#W5918442",
            "final_order_status": "cancelled",
            "not_restocked_item": "1586641416",
            "restocked_items_count": 3
        }
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction="You are a manager auditing the 'Global Tech Distributors' supplier (#SUP0002). Your audit begins with their cancelled supply order, #SO3880. You need to investigate the product involved, confirm its stock status, and ensure it is marked as unavailable in the public catalog. Your audit must then expand to review a separate, successfully fulfilled customer order, #W2611340, which contains a different product from the same supplier. For this customer order, you need to verify the customer's full details, the payment transaction, and the complete tracking history. Finally, you have decided that the 'Office Chair' (item #8426249116) from that customer's order needs a price adjustment, so please update it to $500.00.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO3880"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4794339885", "item_id": "8426249116", "available": False}),
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_user_details", kwargs={"user_id": "james_li_5688"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W2611340"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W2611340"}),
            Action(name="update_variant_price", kwargs={"product_id": "4794339885", "item_id": "8426249116", "price": 500.00})
        ],
        outputs={
            "audited_supplier_id": "#SUP0002",
            "cancelled_supply_order": "#SO3880",
            "impacted_item_id": "8426249116",
            "related_customer_order": "#W2611340",
            "new_price": 500.00,
            "final_availability": False
        }
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction="As an inventory manager, you're conducting a full audit and data correction for the 'Espresso Machine' product line (product #4354588079) from supplier #SUP0009. You've discovered that a cancelled supply order, #SO1273, for one of the variants (item #6200867091) is obsolete and needs to be removed from the system. Furthermore, you've decided to discontinue this specific variant. You must update its stock status and make it unavailable for purchase. As a final step in the audit, you need to verify the price of another active variant, the 'manual 2L' model (item #7774234341), and update it to a new standardized price of $2725.00.",
        actions=[
            Action(name="get_product_details", kwargs={"product_id": "4354588079"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "6200867091"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "6200867091", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4354588079", "item_id": "6200867091", "available": False}),
            Action(name="get_variant_details", kwargs={"item_id": "7774234341"}),
            Action(name="update_variant_price", kwargs={"product_id": "4354588079", "item_id": "7774234341", "price": 2725.00}),
            Action(name="get_variant_details", kwargs={"item_id": "6200867091"}),
            Action(name="get_variant_details", kwargs={"item_id": "7774234341"})
        ],
        outputs={
            "product_id": "4354588079",
            "supplier_id": "#SUP0009",
            "deleted_supply_order_id": "#SO1273",
            "discontinued_item_id": "6200867091",
            "price_updated_item_id": "7774234341",
            "new_price": 2725.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction="As the product manager for laptops (product #4760268021), you are performing a catalog cleanup for the supplier 'Global Tech Distributors'. You need to discontinue the '13-inch silver i7' model (item #2768401027) by updating its stock status and making it unavailable. You also need to remove an obsolete, cancelled supply order (#SO5813) from the system to clean up historical data. Finally, to drive sales for a current model, please apply a promotional price of $2650.00 to the '15-inch black i9' laptop (item #2913673670) and verify the update.",
        actions=[
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "2768401027"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "2768401027", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4760268021", "item_id": "2768401027", "available": False}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="delete_supply_order", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="get_variant_details", kwargs={"item_id": "2913673670"}),
            Action(name="update_variant_price", kwargs={"product_id": "4760268021", "item_id": "2913673670", "price": 2650.00}),
            Action(name="get_variant_details", kwargs={"item_id": "2913673670"})
        ],
        outputs={
            "product_id": "4760268021",
            "discontinued_item_id": "2768401027",
            "deleted_supply_order_id": "#SO5813",
            "price_updated_item_id": "2913673670",
            "new_price": 2650.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction="You are a retail operations manager handling a complex return and exchange for customer Ava Moore (user ID: ava_moore_2033), regarding her order #W4817420. She is returning the 'Action Camera' (item #6700049080) because it was defective. Since that specific model is now out of stock, she has agreed to an exchange for a different model, the 'silver' Action Camera (item #6117189161). Your task is to process this. First, you must update the stock for the returned defective item to 'discontinued'. Then, verify that the replacement camera is in stock. Finally, arrange for the shipment of the new camera using tracking ID 757848843226 from 'SwiftMove Couriers' and update the original order's status to 'exchange_shipped'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W4817420", "tracking_ids": ["757848843226"], "item_ids": ["6117189161"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "exchange_shipped"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "order_id": "#W4817420",
            "returned_item_id": "6700049080",
            "exchanged_item_id": "6117189161",
            "exchange_tracking_id": "757848843226",
            "final_order_status": "exchange_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction="As a senior manager, you are resolving an issue for customer James Li (user ID: james_li_5688) whose order, #W2611340, was lost in transit and must be cancelled. The order contains items from multiple suppliers. Your task is to process the cancellation and perform a full inventory reconciliation. You must trace each item in his order back to its respective supplier and restock the items by adding the quantities from his order back to the supplier's inventory counts. Do not attempt to restock any item that is already listed as 'out_of_stock' or 'discontinued'. After adjusting the inventory, finalize the process by updating the customer's order status.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W2611340"}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "cancelled"})
        ],
        outputs={
            "order_id": "#W2611340",
            "customer_user_id": "james_li_5688",
            "item_not_restocked": "6469567736",
            "item_restocked": "8426249116",
            "new_stock_level": 158,
            "final_order_status": "cancelled"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction="You are a product line manager for 'Running Shoes' (product #6938111410) from supplier #SUP0006. You've decided to phase out the 'yellow synthetic' variant (item #9791469541) due to a cancelled supply order (#SO3933). Your task is to update the product catalog to reflect this change by making the item unavailable. Concurrently, you need to adjust the pricing for two other variants from the same product line to optimize sales: the 'black synthetic' shoe (item #4107812777) should be updated to $159.99, and the 'red leather' shoe (item #4153505238) should be updated to $165.99. Please verify the final details of all three variants you have modified.",
        actions=[
            Action(name="get_product_details", kwargs={"product_id": "6938111410"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="update_variant_availability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "6938111410", "item_id": "4107812777", "price": 159.99}),
            Action(name="update_variant_price", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 165.99}),
            Action(name="get_variant_details", kwargs={"item_id": "9791469541"}),
            Action(name="get_variant_details", kwargs={"item_id": "4107812777"}),
            Action(name="get_variant_details", kwargs={"item_id": "4153505238"})
        ],
        outputs={
            "product_id": "6938111410",
            "supplier_id": "#SUP0006",
            "discontinued_item_id": "9791469541",
            "price_update_item_1": "4107812777",
            "new_price_1": 159.99,
            "price_update_item_2": "4153505238",
            "new_price_2": 165.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction="As a senior manager, you are conducting a full audit of a delivered order, #W3113816, for customer Emma Santos (user ID: emma_santos_9753). Your investigation requires a complete overview of the transaction and its supply chain. Please verify the customer's full details, including all payment methods on her account, and the specifics of the payment for this order. You must also trace the order's shipment history to identify the courier. During your audit, you discover that a key item in her order, a 'Laptop' (item #3265035808, product #4760268021), is now low in stock. To prevent future fulfillment issues, find the related cancelled supply order, #SO5813, and reactivate it by updating its status to 'pending'.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "emma_santos_9753"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "emma_santos_9753"}),
            Action(name="get_order_details", kwargs={"order_id": "#W3113816"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W3113816"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W3113816"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0002"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "3265035808"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5813", "status": "pending"})
        ],
        outputs={
            "customer_user_id": "emma_santos_9753",
            "audited_order_id": "#W3113816",
            "courier_id": "#COU0002",
            "audited_item_id": "3265035808",
            "item_stock_level": 96,
            "reactivated_supply_order": "#SO5813"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction="You are an inventory manager performing a pricing and availability audit on the 'Laptop' product line from supplier 'Global Tech Distributors' (#SUP0002). Your audit has revealed that the variant with item ID #8997785118 is incorrectly marked as available in some systems. You must correct this by formally updating its availability status to False. Concurrently, you've decided to run a promotion on another variant, the '17-inch silver laptop' (item #3265035808), by reducing its price to $2499.99. After making these data corrections, please verify them by retrieving the final details for both of the variants you updated.",
        actions=[
            Action(name="get_supplier_by_id", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="get_product_details", kwargs={"product_id": "4760268021"}),
            Action(name="get_variant_details", kwargs={"item_id": "8997785118"}),
            Action(name="update_variant_availability", kwargs={"product_id": "4760268021", "item_id": "8997785118", "available": False}),
            Action(name="get_variant_details", kwargs={"item_id": "3265035808"}),
            Action(name="update_variant_price", kwargs={"product_id": "4760268021", "item_id": "3265035808", "price": 2499.99}),
            Action(name="get_variant_details", kwargs={"item_id": "8997785118"}),
            Action(name="get_variant_details", kwargs={"item_id": "3265035808"})
        ],
        outputs={
            "supplier_id": "#SUP0002",
            "product_id": "4760268021",
            "availability_corrected_item": "8997785118",
            "final_availability": False,
            "price_corrected_item": "3265035808",
            "new_price": 2499.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction="As a logistics manager, you are resolving a 'lost in transit' claim for order #W9549057 from customer Mason Johansson (user ID: mason_johansson_2485). You must conduct a full investigation into the original shipment, including its tracking history and courier details. Then, you need to check the inventory levels for all items in the original order to determine if a re-shipment is possible. Since one of the items is out of stock, you must arrange for an immediate partial shipment of only the available 'Makeup Kit' using a new tracking ID, 180694848020, and update the order's status to reflect this.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mason_johansson_2485"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9549057"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9549057"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0010"}),
            Action(name="get_product_details", kwargs={"product_id": "9523456873"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="get_product_details", kwargs={"product_id": "5149340237"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9549057", "tracking_ids": ["180694848020"], "item_ids": ["7736359414"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9549057", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "mason_johansson_2485",
            "order_id": "#W9549057",
            "original_tracking_id": "367478070474",
            "out_of_stock_item": "5253880258",
            "shipped_item": "7736359414",
            "new_tracking_id": "180694848020",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction="You are a senior customer support manager handling a return for Amelia Wilson (ZIP: 75215) from her delivered order, #W9077205. She is returning the 'Jigsaw Puzzle' (item #9370300555). During the conversation, she also asks you to update her address on file to '388 Elm Avenue, Suite 500, Dallas, TX, 75215'. Your task is to process the return by restocking the item with its correct supplier, update her address as requested, and perform a final audit by reviewing the details of the courier who handled the original shipment. Finally, update the order status to reflect the partial return.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_product_details", kwargs={"product_id": "1808611083"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555", "value": 72}),
            Action(name="update_user_address", kwargs={"user_id": "amelia_wilson_4614", "address": {"address1": "388 Elm Avenue", "address2": "Suite 500", "city": "Dallas", "state": "TX", "zip": "75215", "country": "USA"}}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9077205"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0009"}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "partially_returned"})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "order_id": "#W9077205",
            "returned_item_id": "9370300555",
            "new_stock_level": 72,
            "updated_address_zip": "75215",
            "audited_courier_id": "#COU0009",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction="As an inventory manager, you're conducting an audit on supplier #SUP0008 after identifying a data discrepancy related to the fulfilled supply order #SO1037. Your task is to correct the inventory and pricing for the 'Desk Lamp' (item #7624783998). You must investigate the original supply order to determine the quantity that should have been added to inventory, and then update the supplier's stock to the correct level. You also need to adjust the item's price to $159.99. As part of the broader supplier review, please also investigate their other pending supply order, #SO5771, and expedite it. Confirm all your updates by fetching the final variant details.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO1037"}),
            Action(name="get_product_details", kwargs={"product_id": "6817146515"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998", "value": 44}),
            Action(name="update_variant_price", kwargs={"product_id": "6817146515", "item_id": "7624783998", "price": 159.99}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="get_variant_details", kwargs={"item_id": "7624783998"})
        ],
        outputs={
            "audited_supply_order": "#SO1037",
            "corrected_item_id": "7624783998",
            "supplier_id": "#SUP0008",
            "corrected_stock_level": 44,
            "new_price": 159.99,
            "expedited_supply_order": "#SO5771"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction="You are a logistics manager handling a 'lost in transit' claim for order #W9077205 from customer Amelia Wilson (ZIP: 75215). Your goal is to resolve the customer's issue while simultaneously addressing a related supply chain concern. Please investigate the original shipment's tracking history and identify the courier. Before arranging a new shipment, you must check the stock for both items in her order. You know the supplier for the 'Jigsaw Puzzle' has been unreliable, so please also investigate their pending supply order #SO6372 and expedite it. Once your investigation is complete, send a replacement shipment for both original items using the new tracking ID 682308736931 and update the order status.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W9077205"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0009"}),
            Action(name="get_product_details", kwargs={"product_id": "1808611083"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9077205", "tracking_ids": ["682308736931"], "item_ids": ["9370300555", "3877338112"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "processing"})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "order_id": "#W9077205",
            "original_tracking_id": "882867966563",
            "original_courier_id": "#COU0009",
            "expedited_supply_order": "#SO6372",
            "new_tracking_id": "682308736931",
            "final_order_status": "processing"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction="As a manager, you are performing a full audit on an order, #W5694685, for customer Evelyn Kovacs (ZIP: 32117) which has been flagged as pending for too long. Your task is to investigate the customer's account, including all payment methods, and determine the cause of the delay by checking the product's stock status. You've also been notified that the 'Tea Kettle' (item #3909406921) in her order is mispriced. Please correct its price to $95.00 in the product catalog. Once the audit is complete and the data is corrected, proceed to ship the order using tracking ID 870596657470 from FastTrack Couriers and update the order's status to 'processing'.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Evelyn", "last_name": "Kovacs", "zip": "32117"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "evelyn_kovacs_6742"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5694685"}),
            Action(name="get_product_details", kwargs={"product_id": "9832717871"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "3909406921"}),
            Action(name="update_variant_price", kwargs={"product_id": "9832717871", "item_id": "3909406921", "price": 95.00}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W5694685", "tracking_ids": ["870596657470"], "item_ids": ["3909406921"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W5694685", "status": "processing"})
        ],
        outputs={
            "customer_user_id": "evelyn_kovacs_6742",
            "order_id": "#W5694685",
            "item_id": "3909406921",
            "new_price": 95.00,
            "item_stock_level": 49,
            "new_tracking_id": "870596657470",
            "final_order_status": "processing"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction="You are a senior manager reviewing customer accounts. You need to perform a full audit on the account of customer Omar Khan (user ID: omar_khan_2363). Your task is to get a complete picture of his activity. This involves retrieving his full user details, all of his payment methods, and a list of all orders he has placed. For his most recent order, #W6304490, you must also pull the complete payment history and tracking details, including identifying the courier. As a final action, you've noticed that the price for the 'Skateboard' (item #6956751343) in his order is lower than the new company standard, and you need to update it to $225.00.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_user_orders", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W6304490"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W6304490"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0010"}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="update_variant_price", kwargs={"product_id": "1968349452", "item_id": "6956751343", "price": 225.00})
        ],
        outputs={
            "customer_user_id": "omar_khan_2363",
            "audited_order_id": "#W6304490",
            "payment_method_id": "credit_card_4420174",
            "courier_id": "#COU0010",
            "price_updated_item": "6956751343",
            "new_price": 225.00
        }
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction="You are a returns specialist handling a request from James Li (user ID: james_li_5688) regarding order #W2611340. He wishes to return the 'Office Chair' (item #8426249116). Your task is to process this return and simultaneously address a potential inventory issue. Please trace the returned chair to its supplier and add it back to their stock. While reviewing the order, you should also investigate the stock status of the other item, a 'Water Bottle', and proactively expedite a related pending supply order (#SO5771) for that supplier. Finally, update the customer's order status to reflect the partial return.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="update_order_status", kwargs={"order_id": "#W2611340", "status": "partially_returned"})
        ],
        outputs={
            "order_id": "#W2611340",
            "returned_item_id": "8426249116",
            "restocked_supplier_id": "#SUP0002",
            "new_stock_level": 158,
            "investigated_item_id": "6469567736",
            "expedited_supply_order": "#SO5771",
            "final_order_status": "partially_returned"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction="As a senior retail analyst, you are investigating the financial and logistical performance related to customer Mei Gonzalez (user ID: mei_gonzalez_4785). Your task is to conduct a full audit of her delivered order, #W7303089. This includes verifying her personal and payment details, analyzing the order's payment history, and tracing the full shipment history to identify the courier. During your analysis of the order's items, you've been alerted that the 'Backpack' (item #2492465580) is part of a product line being discontinued. Please update its stock status to 'discontinued' with its supplier and make it unavailable in the public product catalog.",
        actions=[
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2524789262"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "audited_order_id": "#W7303089",
            "payment_method_id": "credit_card_4387170",
            "courier_id": "#COU0001",
            "discontinued_item_id": "2492465580",
            "supplier_id": "#SUP0005",
            "final_stock_status": "discontinued",
            "final_availability": False
        }
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction="You are a logistics manager investigating a delivery exception for shipment with tracking ID 889070895653. You must conduct a full audit of this shipment, identify the associated customer and order, and verify all of the customer's payment methods on file. While reviewing the order's contents, you notice one of the items is sourced from a supplier with known delays. To mitigate future issues, please investigate that supplier's pending supply order #SO5398 and expedite it. To resolve the customer's immediate issue, you must then re-assign the entire original order for a new shipment using tracking ID 443521489581 with 'QuickShip Logistics'.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5398"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W7303089", "tracking_ids": ["443521489581"], "item_ids": ["2492465580", "7381052709"]})
        ],
        outputs={
            "original_tracking_id": "889070895653",
            "order_id": "#W7303089",
            "customer_user_id": "mei_gonzalez_4785",
            "expedited_supply_order": "#SO5398",
            "new_tracking_id": "443521489581"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction="As a senior manager, you are addressing a defective item report from Ava Moore (ZIP: 78234) for her order #W4817420 regarding an 'Action Camera' (item #6700049080). Your goal is to process the return while also performing a quick audit of the supplier. Please investigate the product to identify its supplier and confirm the current stock status. You should then address the underlying supply chain failure by rectifying the status of the related cancelled supply order, #SO6998. While reviewing this supplier, you have also been asked to correct the price of their 'Electric Toothbrush' (item #6164262152, product id 7352963235) to $219.99. Finally, update the customer's order to reflect that the return process has been initiated.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="get_product_details", kwargs={"product_id": "7352963235"}),
            Action(name="update_variant_price", kwargs={"product_id": "7352963235", "item_id": "6164262152", "price": 219.99}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "original_order_id": "#W4817420",
            "defective_item_id": "6700049080",
            "supplier_id": "#SUP0011",
            "reactivated_supply_order": "#SO6998",
            "price_corrected_item": "6164262152",
            "final_order_status": "pending_return"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction="As an operations manager, please conduct a full investigation into a stalled order, #W9318778, for customer Lucas Martin with zip code 20517. The order has been pending for an unusually long time. You need to identify the root cause of the delay by examining the order's items and their stock levels with the appropriate suppliers. If a stock issue is found, you must also investigate the supplier's recent supply orders, such as #SO4853, to identify and correct any supply chain disruptions. After addressing the supply issue, please update the customer's order status to accurately reflect the situation.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Lucas", "last_name": "Martin", "zip": "20517"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9318778"}),
            Action(name="get_product_details", kwargs={"product_id": "3821016478"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO4853"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO4853", "status": "pending"}),
            Action(name="update_order_status", kwargs={"order_id": "#W9318778", "status": "awaiting_inventory"})
        ],
        outputs={
            "customer_user_id": "lucas_martin_4549",
            "stalled_order_id": "#W9318778",
            "out_of_stock_item": "5669664287",
            "reactivated_supply_order": "#SO4853",
            "final_order_status": "awaiting_inventory"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction="You are a senior manager handling a damaged item report from James Li (user ID: james_li_5688) for his order #W2611340. He reports that the 'Office Chair' (item #8426249116) was damaged. While processing his replacement, you also need to conduct a quick supply chain health check on the other item in his order, a 'Water Bottle'. Your task is to verify the stock for the replacement chair, arrange a new shipment for it using tracking ID 403338127473, and simultaneously investigate the supply status of the water bottle. You are aware of a pending supply order, #SO5771, for that water bottle's supplier; please expedite it to prevent future stockouts.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W2611340"}),
            Action(name="get_product_details", kwargs={"product_id": "4794339885"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W2611340", "tracking_ids": ["403338127473"], "item_ids": ["8426249116"]}),
            Action(name="get_product_details", kwargs={"product_id": "8310926033"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO5771", "status": "expedited"})
        ],
        outputs={
            "customer_user_id": "james_li_5688",
            "order_id": "#W2611340",
            "damaged_item_id": "8426249116",
            "replacement_tracking_id": "403338127473",
            "investigated_item_id": "6469567736",
            "item_stock_status": "out_of_stock",
            "expedited_supply_order": "#SO5771"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction="You are a senior retail manager handling a complex customer issue. Ava Moore (ZIP: 78234) has an order, #W4817420, that was delivered but contained a defective 'Action Camera' (item #6700049080). She has requested a replacement. Your task is to manage the entire replacement process. You must first investigate her order and trace the defective product to its supplier. Upon finding the item is out of stock, you need to resolve the supply issue by finding the related cancelled supply order (#SO6998) and reactivating it. To finalize the customer's request, you will then ship the *other* four items from her original order as a gesture of goodwill, using tracking ID 757848843226 from 'SwiftMove Couriers', and update her order status to 'partially_shipped'.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W4817420", "tracking_ids": ["757848843226"], "item_ids": ["6777246137", "4900661478", "9624127908", "3812493782"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "order_id": "#W4817420",
            "defective_item_id": "6700049080",
            "item_stock_status": "out_of_stock",
            "reactivated_supply_order": "#SO6998",
            "new_tracking_id": "757848843226",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction="You are a logistics manager reviewing a system-flagged order, #W7303089, for customer Mei Gonzalez (ZIP: 95170). The order was successfully delivered, but the tracking data from the courier, 'FastTrack Couriers' (#COU0001), needs to be audited for accuracy and the customer's payment details must be verified. Your task is to conduct a full audit by retrieving the customer's details, all their associated payment methods, and the specific payment transaction for this order. You must also trace the full delivery history. As a final step, because you notice the 'Pet Bed' (item #7381052709) in her order has a low profit margin, update its price in the product catalog to $199.99 to improve profitability.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "zip": "95170"}),
            Action(name="get_user_details", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_user_payment_methods", kwargs={"user_id": "mei_gonzalez_4785"}),
            Action(name="get_order_details", kwargs={"order_id": "#W7303089"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W7303089"}),
            Action(name="get_courier_by_id", kwargs={"courier_id": "#COU0001"}),
            Action(name="get_product_details", kwargs={"product_id": "2747247837"}),
            Action(name="update_variant_price", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99}),
            Action(name="get_variant_details", kwargs={"item_id": "7381052709"})
        ],
        outputs={
            "customer_user_id": "mei_gonzalez_4785",
            "order_id": "#W7303089",
            "tracking_id": "889070895653",
            "payment_method_id": "credit_card_4387170",
            "price_updated_item_id": "7381052709",
            "new_price": 199.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_088",
        instruction="As the inventory and customer relations manager, you are handling the full cancellation of a pending order, #W5918442, for Sofia Rossi (ZIP: 78784). Her order contains multiple products from different suppliers. Your task is to process the cancellation and then perform a complete inventory reconciliation for every item in that order by returning them to their respective supplier's stock. During this process, you notice that an 'Action Camera' (item #1586641416) is listed as 'discontinued' by its supplier, which you know to be a data error. You must correct this inventory record by setting its stock to 10 units and ensure it is marked as available for future sales in the main product catalog.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="get_product_details", kwargs={"product_id": "6858788497"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="get_product_details", kwargs={"product_id": "1968349452"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "order_id": "#W5918442",
            "final_order_status": "cancelled",
            "corrected_item_id": "1586641416",
            "corrected_item_new_stock": 10,
            "restocked_items": [
                "1725100896",
                "5312063289",
                "6117189161"
            ]
        }
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction="You are a supply chain analyst conducting a review of a supplier, 'Pet Supplies World' (#SUP0009), following the cancellation of a key supply order, #SO7642. Your goal is to assess the impact and ensure our product catalog is up-to-date. Please investigate the cancelled supply order to identify the specific product involved and confirm its current stock level. Since this replenishment was cancelled, you must update the item's public availability in the product catalog to prevent new sales. To complete your supplier review, please also examine a successfully delivered customer order, #W8935389, which contains other products from the same supplier, and pull its complete tracking and payment history.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO7642"}),
            Action(name="get_product_details", kwargs={"product_id": "7996920482"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "9862136885"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7996920482", "item_id": "9862136885", "available": False}),
            Action(name="get_order_details", kwargs={"order_id": "#W8935389"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W8935389"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W8935389"})
        ],
        outputs={
            "audited_supplier_id": "#SUP0009",
            "cancelled_supply_order": "#SO7642",
            "discontinued_item_id": "9862136885",
            "related_customer_order": "#W8935389",
            "related_order_tracking_id": "343374055447",
            "related_order_payment": 3996.14
        }
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction="As a senior customer support agent, you are handling an inquiry from Fatima Muller (ZIP: 60644) about her long-pending order, #W9962383. Your goal is to resolve her issue and correct any underlying data problems you find. Please investigate her order to determine the cause of the shipping delay. While examining the items, you notice a pricing error on the out-of-stock 'Tea Kettle' and should correct it to $99.99. To resolve the customer's wait, please ship the available portion of her order immediately using tracking ID 444712814730 from SpeedyShip Couriers and update the order status to reflect that a partial shipment has been made.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Fatima", "last_name": "Muller", "zip": "60644"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9962383"}),
            Action(name="get_product_details", kwargs={"product_id": "1656367028"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "1421289881"}),
            Action(name="get_product_details", kwargs={"product_id": "9832717871"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "4238115171"}),
            Action(name="update_variant_price", kwargs={"product_id": "9832717871", "item_id": "4238115171", "price": 99.99}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9962383", "tracking_ids": ["444712814730"], "item_ids": ["1421289881"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9962383", "status": "partially_shipped"})
        ],
        outputs={
            "customer_user_id": "fatima_muller_6713",
            "order_id": "#W9962383",
            "out_of_stock_item": "4238115171",
            "shipped_item": "1421289881",
            "new_tracking_id": "444712814730",
            "corrected_price": 99.99,
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction="As a customer service manager, you're looking into a complaint from Fatima Muller (ZIP: 60644) regarding her order #W9962383. The order has been pending for an unusually long time. Please investigate the cause of the delay. Your goal is to identify which item is holding up the shipment by checking stock levels for everything in her order, trace the out-of-stock item back to its supplier, and take corrective action. Since the item is unavailable, update the product catalog to reflect this, preventing further backorders. Then, proceed to ship the available portion of her order using the tracking ID 403338127473 from FastTrack Couriers and update the order status to reflect that it has been partially shipped.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Fatima", "last_name": "Muller", "zip": "60644"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9962383"}),
            Action(name="get_product_details", kwargs={"product_id": "1656367028"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "1421289881"}),
            Action(name="get_product_details", kwargs={"product_id": "9832717871"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0009", "item_id": "4238115171"}),
            Action(name="add_order_fulfillment", kwargs={"order_id": "#W9962383", "tracking_ids": ["403338127473"], "item_ids": ["1421289881"]}),
            Action(name="update_order_status", kwargs={"order_id": "#W9962383", "status": "partially_shipped"}),
            Action(name="update_variant_availability", kwargs={"product_id": "9832717871", "item_id": "4238115171", "available": False})
        ],
        outputs={
            "customer_user_id": "fatima_muller_6713",
            "order_id": "#W9962383",
            "out_of_stock_item": "4238115171",
            "shipped_item": "1421289881",
            "new_tracking_id": "403338127473",
            "final_order_status": "partially_shipped"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction="As an inventory manager, you are conducting a routine audit. You have noticed that supply order #SO5817 for a 'Cycling Helmet' was recently fulfilled with a quantity of 15 units. However, the online inventory may not have been updated correctly. Please investigate this. You need to identify the specific item and supplier from the supply order, check the current recorded stock, and update it to the correct value of 142 units. While reviewing the product, you've also determined that its current price is too low, so please update it to $199.99 and ensure the item is marked as available for purchase.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813", "value": 142}),
            Action(name="get_product_details", kwargs={"product_id": "7765186836"}),
            Action(name="get_variant_details", kwargs={"item_id": "8591113813"}),
            Action(name="update_variant_price", kwargs={"product_id": "7765186836", "item_id": "8591113813", "price": 199.99}),
            Action(name="update_variant_availability", kwargs={"product_id": "7765186836", "item_id": "8591113813", "available": True}),
            Action(name="get_variant_details", kwargs={"item_id": "8591113813"})
        ],
        outputs={
            "supply_order_id": "#SO5817",
            "item_id": "8591113813",
            "supplier_id": "#SUP0010",
            "corrected_stock_level": 142,
            "new_price": 199.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction="You are a returns manager processing a return from customer Amelia Wilson (ZIP: 75215) for her order #W9077205. She has returned the 'Dumbbell Set' (item #3877338112). After inspecting the item, you have decided that due to recurring quality issues from the supplier, this product line should be discontinued. Please process the return by tracing the product to its supplier, updating the item's stock status to 'discontinued' in the supplier's inventory, and making the product variant unavailable in the main product catalog. Finally, update the customer's order status to confirm the return is complete.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="get_order_details", kwargs={"order_id": "#W9077205"}),
            Action(name="get_product_details", kwargs={"product_id": "7233192239"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": "discontinued"}),
            Action(name="update_variant_availability", kwargs={"product_id": "7233192239", "item_id": "3877338112", "available": False}),
            Action(name="update_order_status", kwargs={"order_id": "#W9077205", "status": "completed_return"})
        ],
        outputs={
            "customer_user_id": "amelia_wilson_4614",
            "order_id": "#W9077205",
            "returned_item_id": "3877338112",
            "supplier_id": "#SUP0010",
            "item_final_stock_status": "discontinued",
            "final_order_status": "completed_return"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction="You are a manager reviewing a flagged pending order, #W5918442, for Sofia Rossi (ZIP: 78784), which was paused due to a payment failure. Your first step is to cancel the order. During the post-cancellation audit, you notice that one of the items in her failed order, an 'Action Camera' (item #1586641416), is incorrectly marked as 'discontinued' in the supplier's inventory system, which is likely a data entry error. Please correct this by updating its stock count to 10 units and making it available in the product catalog so that other customers can purchase it.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5918442"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "cancelled_order_id": "#W5918442",
            "corrected_item_id": "1586641416",
            "supplier_id": "#SUP0011",
            "new_stock_level": 10,
            "final_availability": True
        }
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction="You are an inventory manager investigating a stockout of the popular 'Action Camera' (item #6700049080) that is affecting customer Ava Moore's order (#W4817420). Your goal is to resolve the stock issue at its source. You need to trace the item from the customer's order to its supplier and confirm the inventory shortage. Upon discovering the stockout, your investigation should lead you to the related, cancelled supply order #SO6998. To fix the supply chain, you must reactivate this supply order and then update the product's availability in the main catalog to ensure it can be sold once replenished.",
        actions=[
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="update_supply_order_status", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="update_variant_availability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": True}),
            Action(name="get_variant_details", kwargs={"item_id": "6700049080"})
        ],
        outputs={
            "customer_order_id": "#W4817420",
            "out_of_stock_item_id": "6700049080",
            "supplier_id": "#SUP0011",
            "corrected_supply_order_id": "#SO6998",
            "supply_order_new_status": "pending",
            "final_variant_availability": True
        }
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction="You are a customer service manager assisting Omar Khan (ZIP: 75203). He is happy with his recent delivered order, #W6304490, and wants to buy another 'Smart Thermostat' (item #4983901480), but can't find it on the website. Your task is to resolve this. Investigate his original order to identify the product and its supplier. After discovering the item is out of stock, check on other pending supply orders for that supplier, like #SO9359, to assess their general fulfillment status. Then, perform a manual inventory correction by updating the thermostat's stock count to 50 units, mark it as available for purchase, and finally, verify that the variant details now reflect the correct price and availability.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Omar", "last_name": "Khan", "zip": "75203"}),
            Action(name="get_order_details", kwargs={"order_id": "#W6304490"}),
            Action(name="get_product_details", kwargs={"product_id": "4896585277"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "4983901480"}),
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0001", "item_id": "4983901480", "value": 50}),
            Action(name="update_variant_availability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": True}),
            Action(name="get_variant_details", kwargs={"item_id": "4983901480"})
        ],
        outputs={
            "customer_user_id": "omar_khan_2363",
            "order_id": "#W6304490",
            "item_id": "4983901480",
            "supplier_id": "#SUP0001",
            "final_stock_level": 50,
            "final_availability": True
        }
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction="As the inventory manager, you're addressing a potential stockout issue. You've been alerted that the supply order #SO3933 for our yellow running shoes was cancelled, and you need to mitigate the impact on sales. Please investigate the product details for these shoes to identify the supplier and assess the current stock of a related alternative, the red leather running shoes (item #4153505238), from the same supplier. To prevent unfulfillable orders, update the availability of the yellow running shoes (item #9791469541) to make them unavailable. To manage demand for the remaining stock, increase the price of the red leather variant to $162.99.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="get_product_details", kwargs={"product_id": "6938111410"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "9791469541"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0006", "item_id": "4153505238"}),
            Action(name="update_variant_availability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="update_variant_price", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 162.99})
        ],
        outputs={
            "cancelled_supply_order": "#SO3933",
            "product_id": "6938111410",
            "unavailable_item_id": "9791469541",
            "price_updated_item_id": "4153505238",
            "new_price": 162.99
        }
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction="You are an inventory manager conducting a stock audit. You've noticed that supply order #SO5722 for a 'Wristwatch' was marked as 'fulfilled', but the inventory count seems off. Your task is to resolve this discrepancy. First, retrieve the details of the supply order to confirm the quantity received. Then, use the product information to identify the correct supplier. Check the current recorded stock for this item with the supplier. After confirming the discrepancy, update the supplier's stock to the correct count of 153 units. Finally, ensure the product variant is marked as available for customers.",
        actions=[
            Action(name="get_supply_order_details", kwargs={"supply_order_id": "#SO5722"}),
            Action(name="get_product_details", kwargs={"product_id": "6066914160"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "9949163720"}),
            Action(name="update_item_stock", kwargs={"supplier_id": "#SUP0007", "item_id": "9949163720", "value": 153}),
            Action(name="update_variant_availability", kwargs={"product_id": "6066914160", "item_id": "9949163720", "available": True})
        ],
        outputs={
            "supply_order_id": "#SO5722",
            "product_id": "6066914160",
            "item_id": "9949163720",
            "supplier_id": "#SUP0007",
            "corrected_stock_level": 153
        }
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction="You are a customer service manager handling a complaint from Ava Moore (ZIP: 78234) about her delivered order, #W4817420. She claims the 'Action Camera' (item_id: 6700049080) is defective. Your task is to conduct a full investigation. First, verify her user and order details. Then, retrieve the product details to identify its supplier. Check the original courier and tracking history for the delivery. Afterwards, check the current stock for the Action Camera with the identified supplier to see if a replacement is possible. Based on your findings, update the order status to 'pending_return' to initiate the return process.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="get_order_details", kwargs={"order_id": "#W4817420"}),
            Action(name="get_tracking_history", kwargs={"order_id": "#W4817420"}),
            Action(name="get_product_details", kwargs={"product_id": "3377618313"}),
            Action(name="get_item_stock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="update_order_status", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs={
            "customer_user_id": "ava_moore_2033",
            "order_id": "#W4817420",
            "defective_item_id": "6700049080",
            "supplier_id": "#SUP0011",
            "item_stock_status": "out_of_stock",
            "final_order_status": "pending_return"
        }
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction="You are a retail manager handling a payment issue for customer Sofia Rossi from ZIP code 78784. Her recent order, #W5918442, is stuck in 'pending' status due to a reported payment failure. Your task is to investigate the order's payment history to confirm the issue, cancel the order in the system since the payment did not go through, and then verify that the order's status has been successfully updated to 'cancelled'.",
        actions=[
            Action(name="find_user_id_by_name_zip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="get_order_payment_history", kwargs={"order_id": "#W5918442"}),
            Action(name="update_order_status", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="get_order_status", kwargs={"order_id": "#W5918442"})
        ],
        outputs={
            "customer_user_id": "sofia_rossi_8776",
            "order_id": "#W5918442",
            "final_status": "cancelled"
        }
    ),
]
