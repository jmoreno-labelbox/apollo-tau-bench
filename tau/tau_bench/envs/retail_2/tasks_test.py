from tau_bench.types import Action, Task

TASKS = [

    Task(
        annotator="0",
        user_id="USER_001",
        instruction="In your role as a manager, handle the audit of a delivered order, #W4817420, for customer Raleigh Moore (user ID: charlotte_moore_2033). This audit mandates a comprehensive examination of the customer's payment history for the order and the entire logistics chain, including the courier. While conducting the product audit, it's discovered that two items from the order have been phased out by their suppliers: the 'Action Camera' (item #6700049080) and the 'Hiking Boots' (item #3812493782). You need to update the availability for both items in the product catalog to block future sales. Finally, adjust the price of a different high-stock item from the order, the 'Water Bottle' (item # W4817420, pertaining to customer Raleigh Moore (user ID: charlotte_moore_2033). This audit requires a thorough review of the customer's payment history related to the order and the complete logistics process, including the courier service. During the product audit, it was identified that two items from the order have been discontinued by their suppliers: the 'Action Camera' (item #6700049080) and the 'Hiking Boots' (item #3812493782). You must update the availability for both items in the product catalog to block future sales.",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W4817420"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W4817420"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0005"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7363354090", "item_id": "3812493782", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "8310926033", "item_id": "6777246137", "price": 45.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_002",
        instruction="Acting as a logistics manager, oversee a review of an order flagged by the system, #W7303089, for customer Mei Campbell (ZIP: 95170). Although the order was successfully delivered, the tracking details from the 'SpeedWay Delivery' (#COU0001) require an audit for accuracy, and the customer's payment information needs verification. Your responsibility is to perform a thorough audit by accessing the customer's details, all related payment methods, and the specific payment transaction for this order. Additionally, trace the complete delivery history. As a concluding step, given that the 'Pet Bed' (item # W7303089 for customer Mei Campbell (ZIP: 95170) was delivered successfully, but the tracking information from 'SpeedWay Delivery' (#COU0001) needs verification for accuracy, and the payment details must be confirmed. Your task is to conduct a comprehensive audit by reviewing the customer's information, all payment methods, and the specific transaction for this order. Also, trace the entire delivery history. Finally, since the 'Pet Bed' (item #7381052709) has a high stock level, adjust its price.",
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "zip": "95170"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7381052709"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_003",
        instruction="You are a customer service manager addressing a delayed order, #W7619352, for Sofia Martin (user ID: sofia_martin_1518). The delay is a result of an out-of-stock 'Portable Charger' (item #7903094618). Your task is to rectify the situation by speeding up a pending supply order with the supplier (#SO6372). During a supplier audit, you've decided to discontinue offering a different product from them, the 'red olefin Patio Umbrella' (product #9743693396, item # W7619352 pertains to Sofia Martin (user ID: sofia_martin_1518). The delay is due to the 'Portable Charger' (item #7903094618) being out of stock. Your objective is to expedite the pending supply order with the supplier (#SO6372). During a supplier audit, you have opted to remove the 'red olefin Patio Umbrella' (product #9743693396, item #8170914468) from offerings by adjusting its availability.",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7619352"}),
            Action(name="GetUserDetails", kwargs={"user_id": "sofia_martin_1518"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6942297802"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "7903094618"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9743693396"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "9743693396", "item_id": "8170914468", "available": False}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W7619352", "tracking_ids": ["181292856236"], "item_ids": ["2757705742", "3526747930", "8798690242"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W7619352", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_004",
        instruction="You are a returns manager dealing with a return from customer Raleigh Moore (user ID: charlotte_moore_2033) for her delivered order #W4817420. She is returning the 'Hiking Boots' (item #3812493782). Your task is to process the return by restocking the item with its supplier. In the process, you spot an obsolete canceled supply order (#SO5813) for that supplier that must be removed. As part of a promotional campaign, you are also required to revise the price of the 'Action Camera' (item # W4817420. She is returning the 'Hiking Boots' (item #3812493782). Your job is to handle the return by restocking the item with the supplier. During this, you identify a canceled obsolete supply order (#SO5813) for that supplier that needs to be deleted. Additionally, as part of a promotional effort, you need to update the price of the 'Action Camera' (item #6700049080) from her original order to $450.00",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "3377618313", "item_id": "6700049080", "price": 450.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "6700049080"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_005",
        instruction="As a manager, you are overseeing a return from customer Omar Khan (user ID: omar_khan_2363) for his order #W6304490. He is sending back the 'Dumbbell Set' (item #2194493783). Due to persistent quality issues with this product line, remove it from active stock and make it unavailable in the catalog. Additionally, review Omar Khan's account details as part of the return audit. To sell off remaining inventory from the same supplier ('Athletic Equipment Co.'), set the price of the '30-50 lbs urethane adjustable' set (item #4422467033) at $479.99. Finally, audit their fulfilled supply orders.",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetUserDetails", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "2194493783", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7233192239", "item_id": "2194493783", "available": False}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4422467033"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7233192239", "item_id": "4422467033", "price": 479.99}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W6304490", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_006",
instruction="As a senior manager, coordinate a complex request for customer Sofia Russo (user ID: sofia_russo_8776) concerning her pending order, #W5918442. The customer intends to cancel her full order and requires her address to be modified to 456 Market St, San Francisco, NV, 94105. You must proceed with the cancellation and address update. After that, conduct a complete inventory reconciliation for all items in the canceled order, restock them with their appropriate suppliers, and correct a data error for the 'Action Camera,' which is wrongly labeled as discontinued; update its stock to 1 and set it as available.",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "sofia_russo_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "NV", "zip": "94105", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "6858788497"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 1}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_007",
instruction="As a logistics manager auditing a shipment with tracking ID 367478070474, your role involves conducting a complete trace on this shipment. This includes identifying the courier and the related order (#W9549057) and customer (James Andersson). You need to examine the customer's full details and payment methods. While auditing the order's items, you observe that the 'T-Shirt' (item #5253880258) is from a supplier with an outdated fulfilled supply order (#SO6503) that needs deletion. You also decide to discontinue the 'Makeup Kit' (item #7736359414) from the order and update its stock status and availability. Finally, update the customer's order status to 'audit_complete'",
        actions=[
            Action(name="FindCourierByTrackingId", kwargs={"tracking_id": "367478070474"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9549057"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9549057"}),
            Action(name="GetUserDetails", kwargs={"user_id": "james_andersson_2485"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "james_andersson_2485"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9523456873"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO6503"}),
            Action(name="GetProductDetails", kwargs={"product_id": "5149340237"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "5149340237", "item_id": "7736359414", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9549057", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_008",
instruction="As a senior manager performing a comprehensive audit of the supplier 'Worldwide Electronics Partners' (#SUP0002), it is your responsibility to obtain a full list of their products and examine the available variants for their 'Office Chair' product line. During the audit, you find that the 'black fabric fixed standard' chair (item #8426249116) is mistakenly marked as available and must be corrected. You also identify an unnecessary pending supply order, #SO6035, requiring cancellation. In parallel, review customer order #W2611340, which contains an item from this supplier, to confirm its payment",
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "4794339885"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4794339885", "item_id": "8426249116", "available": False}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6035", "status": "cancelled"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_009",
instruction="As a senior analyst, you are responsible for investigating a data anomaly concerning a completed supply order, #SO5897. Your task is to track this order back to its supplier and associated product, and adjust the inventory for the 'Electric Kettle' (item #9472539378), which is erroneously recorded as having zero stock, by setting its stock level to 81 units and ensuring its availability. This investigation directs you to a customer order, #W4817420, that includes a different kettle from the same supplier. It is essential to review the complete information of this customer order. During this review, you opt to adjust the pricing of the 'Hiking Boots' (item #3812493782) in that order to $250.00 and remove an unrelated, outdated supply order (#SO5813).",
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5897"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1075968781"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9472539378"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9472539378", "value": 81}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "1075968781", "item_id": "9472539378", "available": True}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7363354090", "item_id": "3812493782", "price": 250.00}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "9472539378"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_010",
instruction="As a logistics manager, you are managing a 'lost in transit' claim for order #W9077205 involving customer Evelyn Anderson (user ID: evelyn_anderson_4614). Your objective is to fully resolve this issue. The investigation entails tracing the original shipment's tracking history to identify the courier. You need to verify the stock for both items in her order to assess the possibility of a re-shipment. As one item is available while the other is not, you must organize a partial re-shipment for the available 'Dumbbell Set' using the new tracking ID 682308736931 from 'SpeedWay Delivery' (COU0001). Additionally, address the stockout of the 'Jigsaw Puzzle' by locating the related pending supply order, # W9077205 pertains to customer Evelyn Anderson (user ID: evelyn_anderson_4614). Your task is to resolve this issue completely. This involves tracing the tracking history of the original shipment to determine the courier. Check the inventory for both items in her order to evaluate the option for a re-shipment. Since one item is in stock and the other is not, arrange a partial re-shipment for the available 'Dumbbell Set' using the new tracking ID 682308736",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9077205"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0009"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1808611083"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6372"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="AssignCourierToOrder", kwargs={"order_id": "#W9077205", "courier_id": "#COU0001", "tracking_ids": ["682308736931"], "item_ids": ["3877338112"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_011",
instruction="As a logistics manager, you are responsible for inspecting a shipment with tracking ID 343374055447. Your role is to coordinate a complete trace of this shipment, which involves identifying the courier along with the related order (#W8935389) and customer (Raj Li). You need to examine the customer's comprehensive details and payment options. While auditing the order's items, you observe that the 'Espresso Machine' (item #3714494375) belongs to a supplier with an outdated cancelled supply order (#SO1273) that must be removed. Additionally, you decide that the 'Smart Thermostat' (item #8722653925) should be discontinued. Please update its inventory status and availability accordingly. Finally, update the",
        actions=[
            Action(name="FindCourierByTrackingId", kwargs={"tracking_id": "343374055447"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetUserDetails", kwargs={"user_id": "raj_li_8594"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "raj_li_8594"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4896585277"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "8722653925"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "8722653925", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4896585277", "item_id": "8722653925", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_012",
instruction="As a manager, you are tasked with a comprehensive audit on a pending order, #W9318778, for customer Liam Clark (user ID: liam_clark_4549). Your responsibility is to examine the customer's account, including all payment methods, to ascertain the reason for the delay by checking the product's stock status. You discover that the 'Air Purifier' (item #5669664287) is currently unavailable. To address this, you need to review a related cancelled supply order (#SO4853) and reactivate it. In conducting a pricing review, you also need to adjust the price of the 'Mechanical Keyboard' (item # W9318778, for client Liam Clark (user ID: liam_clark_4549). Your task is to investigate the customer's account and payment options to determine the cause of the delay by checking the stock status of the product. You find that the 'Air Purifier' (item #5669664287) is not in stock. To resolve this, review the associated cancelled supply order (#SO4853) and reactivate it. Additionally, adjust the price of the 'Mechanical Keyboard')",
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "liam_clark_4549"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "liam_clark_4549"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9318778"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO4853"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO4853", "status": "pending"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1656367028"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "1656367028", "item_id": "6342039236", "price": 250.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9318778", "status": "awaiting_inventory"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_013",
instruction="As a senior manager, you're handling an audit of 'Animal Care Worldwide' (#SUP0009). Your responsibility is to obtain a comprehensive list of their products and examine the variants available for their 'Coffee Maker' product line. During the audit, you identify that the '4 cups drip stainless steel' variant (item #3039787582) is mistakenly listed as available, and it should be updated. Additionally, a redundant pending supply order, #SO6035, must be cancelled. Simultaneously, you need to review a customer order, #W8935389, which includes items from this supplier, to verify its payment and tracking history. Lastly, adjust the price of the 'manual 1L Espresso Machine' (item #4354588079) to reflect current market conditions.",
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0009"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7996920482"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "7996920482"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7996920482", "item_id": "3039787582", "available": False}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6035"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6035", "status": "cancelled"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4354588079", "item_id": "3714494375", "price": 2750.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_014",
instruction="Coordinate an audit of the supplier 'Fresh Market Co.' (#SUP0005) while acting as a senior manager. Your task includes getting a comprehensive overview of their product lines and listing the available variants for their 'Bicycle' product (product ID: 9783735446). During your work, a stalled customer order, #W9318778, is brought to your attention, which involves an out-of-stock 'Air Purifier' from another supplier. You have to investigate the supply chain issues with this item by reviewing and hastening the pending supply order #SO4238. To resolve the customer's issue, ship the four",
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "9783735446"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9318778"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO4238"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO4238", "status": "expedited"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9318778", "tracking_ids": ["836251433228"], "item_ids": ["2143041831", "6342039236", "9850781806", "3076708684"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9318778", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_015",
instruction="Handle a multi-part request from Raleigh Moore (ZIP: 78234) concerning her delivered order, #W4817420, as a customer service manager. She wishes to return the 'Hiking Boots' (item #3812493782) and change her shipping address to 101 Pine St, San Antonio, NM, 78234. Your responsibility is to execute this process. Initiate by restocking the boots with their supplier. Upon examining the order, it becomes evident that the 'Action Camera' (item #6700049080) is out of stock, with its supply order",
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "charlotte_moore_2033", "address": {"address1": "101 Pine St", "address2": "", "city": "San Antonio", "state": "NM", "zip": "78234", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_016",
instruction="Coordinate a comprehensive audit of the supplier 'Tech Supplies Inc.' (#SUP0001) as a senior manager, prompted by a stockout problem impacting customer James Andersson's order, #W9549057. Your job is to examine the customer's order and account, assess the supplier's product catalog, and execute essential data cleanup. Start by retrieving full details of the customer and their order. Next, probe the 'T-Shirt' (product #9523456873) to verify the stock status of the item in the order. You also need to cancel the supplier's pending supply order #SO9359, as the item is unnecessary. Subsequent to this, you should remove the 'blue cotton crew neck' T-shirt (item #9612497925) from the same supplier by adjusting its stock and availability. To dispose of remaining inventory of another T-shirt, modify the price of the 'black cotton crew neck XXL' (item #3799046073). As a senior manager, address the stockout issue affecting customer James Andersson's order, #W9549057. Begin by reviewing the customer's order and account, then check the supplier's product catalog and perform necessary data cleanup. First, gather complete information on the customer and their order. Next, investigate the stock status of the 'T-Shirt' (product #9523456873) included in the order. Cancel the pending supply order #SO9359 from the supplier, as the item is unnecessary.",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9549057"}),
            Action(name="GetUserDetails", kwargs={"user_id": "james_andersson_2485"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9523456873"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "9612497925", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "9523456873", "item_id": "9612497925", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "9523456873", "item_id": "3799046073", "price": 50.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9549057", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_017",
instruction="As a customer service manager, manage a return and address modification for Raleigh Jackson (user ID: charlotte_jackson_2676) related to her ongoing order #W8327915. She is sending back the '17-inch black i7 Laptop' (item #1684786391) and requires her address to be updated to 229 Lakeview Drive, Suite 400, Milwaukee, IN, 60637. Your role is to process this partial return by restocking the item with its supplier. Upon reviewing the supplier's records, you identify an outdated cancelled supply order (#SO5813) that needs removal. Additionally, decide to increase the price of the 'black polarized plastic Sunglasses' (item #4358482460).",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8327915"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_jackson_2676"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1684786391"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1684786391", "value": 111}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "charlotte_jackson_2676", "address": {"address1": "229 Lakeview Drive", "address2": "Suite 400", "city": "Milwaukee", "state": "IN", "zip": "60637", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "7314138884"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7314138884", "item_id": "4358482460", "price": 295.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8327915", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_018",
instruction="In your role as a product manager, coordinate a data cleanup and strategic update for 'Digital Paradise Distributors' (#SUP0004). Start by obtaining a list of all products they supply. For their 'Wireless Earbuds' product line (product #9924732112), ensure the 'black 8-hour' variant (item #2499294441) is indicated as unavailable, as it is discontinued. You also need to remove an outdated cancelled supply order (#SO9426) for this supplier. To enhance sales of another product, change the price of the '7-inch Wi-Fi + Cellular' E-Reader (item #4273929280) to 240.00.",
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9924732112"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0004", "item_id": "2499294441"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "9924732112", "item_id": "2499294441", "available": False}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO9426"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3801771308"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "3801771308", "item_id": "4273929280", "price": 240.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2499294441"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4273929280"})
        ],
        outputs=[]
    ),
        Task(
        annotator="0",
        user_id="USER_019",
instruction="In your role as senior manager, coordinate a complex inventory and pricing update for 'Worldwide Electronics Partners' (#SUP0002) due to the cancellation of a substantial laptop supply order (#SO5813). Your responsibility is to modify the catalog to reflect this change. Mark the '17-inch silver i9' laptop (item #3265035808) as unavailable for purchase. In order to offset potential revenue loss, raise the price of the '15-inch black i9' laptop (item #2913673670) to $2750.00 and the '13-inch black i7' laptop (item #1657832319) to $2750.00. Simultaneously, handle a customer return for order #W9077205.",
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4760268021", "item_id": "3265035808", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4760268021", "item_id": "2913673670", "price": 2750.00}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4760268021", "item_id": "1657832319", "price": 2750.00}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "completed_return"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_020",
instruction="As a retail manager, you are resolving a customer complaint from Mei Campbell (user ID: mei_campbell_4785) regarding her order #W7303089. She received a 'Backpack' (item #2492465580) that is the incorrect size and will return it. Additionally, you need to update her address to 858 Elm Street, Suite 912, Oakland, NV, 95170. Process the return by coordinating the restocking of the backpack with its supplier. During this task, it becomes evident that the 'green leather' backpack (item #7251508981) from the same supplier is discontinued; make this item unavailable in the product catalog. After the customer's address is updated, ensure to expedite a pending supply order (#SO5398).",
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "mei_campbell_4785", "address": {"address1": "858 Elm Street", "address2": "Suite 912", "city": "Oakland", "state": "NV", "zip": "95170", "country": "USA"}}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": 189}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "7251508981", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W7303089", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_021",
instruction="As a product manager, you're handling a pricing and availability audit of the 'Espresso Machine' product line (product #4354588079) from supplier #SUP0009. You have opted to discontinue the '1L manual' variant (item #3714494375) and must update its stock status and availability accordingly. To clear out remaining inventory of another model, shift the price of the '2L manual' variant (item #7774234341) to a promotional $2700.00. While reviewing this supplier, also ensure data cleanliness by removing the obsolete cancelled supply order #SO7642. Finally, verify all changes by retrieving the final details for both modified espresso machine variants.",
        actions=[
            Action(name="GetProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "3714494375"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "3714494375", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4354588079", "item_id": "3714494375", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4354588079", "item_id": "7774234341", "price": 2700.00}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO7642"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "3714494375"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7774234341"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_022",
instruction="As a senior manager, you are managing a request from Liam Clark (user ID: liam_clark_4549) regarding his pending order #W9318778. He intends to cancel two items, the 'Bicycle' (#2143041831) and the 'Wall Clock' (#9850781806), and update his address to 758 Lakeview Drive, Suite 400, Washington, DC, 20517. Your responsibility is to process this partial cancellation by restocking both items with their original suppliers. During the process, you notice another 'Wall Clock' variant (#6508153405) that has a pricing error and",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9318778"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9783735446"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2143041831"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2143041831", "value": 123}),
            Action(name="GetProductDetails", kwargs={"product_id": "2344688344"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "9850781806"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "9850781806", "value": 90}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2344688344", "item_id": "6508153405", "price": 195.00}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "liam_clark_4549", "address": {"address1": "758 Lakeview Drive", "address2": "Suite 400", "city": "Washington", "state": "DC", "zip": "20517", "country": "USA"}}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9318778", "status": "partially_cancelled"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_023",
instruction="As a senior manager, you are handling a comprehensive audit of the supplier 'Tech Supplies Inc.' (#SUP0001). Your task is to compile a complete list of their product lines and examine the available variants for their 'Digital Camera' product. During this audit, you identify that the '30MP, 5x zoom' variant (item #6384525445) is incorrectly marked as available and must be updated to unavailable. Additionally, you come across an unnecessary pending supply order, #SO9359, which requires cancellation. Simultaneously, you need to inspect customer order #W8935389, which includes other items from this supplier, to assess its payment and tracking details.",
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8940227892"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "8940227892"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "8940227892", "item_id": "6384525445", "available": False}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_024",
instruction="In your role as a customer service manager, you are assisting Mei Ahmed (user ID: mei_ahmed_5058) with her pending order #W2631563. She needs her address updated to 833 Hickory Lane, Suite 1000, Columbus, OH, 43197. Upon updating her address, you realize the 'Smart Thermostat' in her order is out of stock, resulting in the delay. To address this, locate the related pending supply order from the supplier (#SO9359) and expedite it. You also discover that the 'Garden Hose' (item #5753502325) is incorrect; change it to $99.99.",
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "mei_ahmed_5058", "address": {"address1": "833 Hickory Lane", "address2": "Suite 1000", "city": "Columbus", "state": "OH", "zip": "43197", "country": "USA"}}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2631563"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4896585277"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "2791467853"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6679515468"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6679515468", "item_id": "5753502325", "price": 99.99}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W2631563", "tracking_ids": ["349832798095"], "item_ids": ["5753502325"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2631563", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_025",
instruction="As a senior analyst, your responsibility involves auditing a fulfilled supply order, #SO6503, for 'Tech Supplies Inc.' (#SUP0001) to verify the accuracy of the inventory. The task requires you to locate the item in the supply order, examine its current stock level, and adjust it to indicate the delivered quantity of 35 units. While performing the audit, you come across a pending supply order for the identical supplier, #SO9359, which is now superfluous and should be cancelled. In parallel, you need to explore a related customer order, #SO6503, for 'Tech Supplies Inc.' (#SUP0001), is tasked with confirming inventory accuracy. You must find the item in the supply order, check its current stock level, and update it to reflect a delivery of 35 units. During the audit, you will encounter a pending order from the same supplier, #SO9359, which is now unnecessary and needs to be cancelled. Additionally, investigate a related customer order, #W8935389, that contains a different product from",
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6503"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8940227892"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "7255224608"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "7255224608", "value": 35}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "cancelled"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetUserDetails", kwargs={"user_id": "raj_li_8594"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8935389", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_026",
instruction="As a senior analyst, your role is to audit customer Noah Jackson (user ID: noah_jackson_6291) along with his pending order #W6779827. It is essential to retrieve his complete user information, all linked payment methods, and his entire order history. In reviewing the items in the pending order, you detect a pricing mistake on the 'Dumbbell Set' (item #7896397433) and need to adjust it to $460.00. Furthermore, you find that the 'Coffee Maker' (item #1323134954) is out of stock; ensure this item is flagged as unavailable in the product catalog to avoid future orders. Lastly",
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "noah_jackson_6291"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "noah_jackson_6291"}),
            Action(name="GetUserOrders", kwargs={"user_id": "noah_jackson_6291"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6779827"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7233192239", "item_id": "7896397433", "price": 460.00}),
            Action(name="GetProductDetails", kwargs={"product_id": "7996920482"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "1323134954"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7996920482", "item_id": "1323134954", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W6779827", "status": "awaiting_inventory"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_027",
instruction="As a senior operations manager, your responsibility involves examining a delivered order, #W4817420, for customer Raleigh Moore (ZIP: 78234), who has reported that the 'Action Camera' (item #6700049080) she received is defective. Your objective is to manage a return and determine the underlying cause of the stock issue. You need to trace the product back to its supplier, verify its stock status, and inspect the related cancelled supply order, #W4817420, regarding customer Raleigh Moore (ZIP: 78234), who has reported a defect in the 'Action Camera' (item #6700049080) received. Your task is to process the return and investigate the stock issue. Trace the product to its supplier, check its stock status, and review the cancelled supply order, #SO6998, responsible for the stockout. To prevent further complications, reactivate the supply order, update the product catalog to reflect its out-of-stock status.",
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_028",
instruction="As a logistics manager, your task involves reviewing the shipment with tracking ID 889070895653. You are to conduct a full trace on this shipment, identify the associated order (#W7303089) and customer (Mei Campbell), and examine the customer's entire order history. During the audit, it is revealed that the 'Pet Bed' (item #7381052709) in the order is sourced from a supplier, 'Literature Plus', who has a redundant, obsolete cancelled supply order (#SO6998) on file that must be removed. You also observe the 'Backpack' from the same order is priced too low; adjust the price of variant #2492465580 to $210.00. Lastly, update the customer's order status to 'audit_complete'",
        actions=[
            Action(name="FindCourierByTrackingId", kwargs={"tracking_id": "889070895653"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserOrders", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 210.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W7303089", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_029",
instruction="As a customer service manager, you are overseeing a return request from Raleigh Moore (user ID: charlotte_moore_2033) for her order #W4817420. She intends to return the 'Hiking Boots' (item #3812493782) and has asked to update her address to 996 Cedar Street, Suite 700, San Antonio, NM, 78234. Your responsibility is to process the return by coordinating the restocking of the boots with their supplier. During this process, you find an obsolete cancelled supply order (#SO5813) for that supplier that needs to be removed. Upon updating the customer's address, you must also adjust the price of another item from her initial order, the 'Bookshelf' (item # W4817420). The customer plans to return the 'Hiking Boots' (item #3812493782) and requests her address be changed to 996 Cedar Street, Suite 700, San Antonio, NM, 78234. You are tasked with processing the return by arranging the restocking of the boots with the supplier. During this, you discover an obsolete canceled supply order (#SO5813) for that supplier that needs deletion. After updating the customer's address, also revise the price",
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782", "value": 24}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "charlotte_moore_2033", "address": {"address1": "996 Cedar Street", "address2": "Suite 700", "city": "San Antonio", "state": "NM", "zip": "78234", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "8600330539"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "8600330539", "item_id": "4900661478", "price": 475.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_030",
        instruction="You're managing a return for customer Raj Li (user ID: raj_li_8594) from his order #W8935389. He wants to return the 'Tablet' (item #4803681337). Your role is to process the return by coordinating the restocking of the item with its supplier. While reviewing the supplier's documentation, you notice an obsolete pending supply order (#SO5993) that ought to be removed. To encourage sales for another product from the same supplier, you opt to reduce the price of the 'gray leather sneakers' (item # W8935389 intends to return the 'Tablet' (item #4803681337). Your task is to manage the return by coordinating the item's restocking with the supplier. During your review of the supplier's records, you identify an outdated pending supply order (#SO5993) that should be deleted. To boost sales for another product from the same supplier, you decide to lower the price of the 'gray leather sneakers' (item #2509076505) to $185.00."
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetUserDetails", kwargs={"user_id": "raj_li_8594"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8024098596"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0003", "item_id": "4803681337"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0003", "item_id": "4803681337", "value": 194}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7471004230"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7471004230", "item_id": "2509076505", "price": 185.00}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8935389", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_0031",
        instruction="As a logistics manager, you are tasked with evaluating a 'lost in transit' claim for order #W9549057 from customer James Andersson (user ID: james_andersson_2485). Handle a comprehensive investigation by examining the order specifics, the customer's payment history, and the initial tracking details. Subsequently, verify the inventory for both items in the order. Since the 'T-Shirt' (item #5253880258) is currently unavailable, locate its supply order (# W9549057 from customer James Andersson (user ID: james_andersson_2485). Conduct a thorough review of the order details, payment history, and initial tracking information. Next, check the inventory for both ordered items. As the 'T-Shirt' (item #5253880258) is out of stock, find its supply order (#SO9359) and give it priority. For the 'Makeup Kit' in stock, arrange for an immediate re-shipment using the"
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "james_andersson_2485"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9549057"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W9549057"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9549057"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9523456873"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "5149340237"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9549057", "tracking_ids": ["202468403681"], "item_ids": ["7736359414"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9549057", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_032",
        instruction="As a manager, you will perform a thorough audit of customer Mei Campbell (user ID: mei_campbell_4785) and her delivered order #W7303089. This audit involves a detailed examination of her account, payment options, and the complete logistics trail of the shipment. When reviewing the products, decide to discontinue the 'Backpack' (item #2492465580) she ordered. Additionally, resolve an inventory inconsistency for the other item in her order, a 'Pet Bed' (item # W7303089. This audit requires a thorough assessment of her account, payment methods, and the entire shipping logistics. Upon evaluating the products, opt to remove the 'Backpack' (item #2492465580) from her order. Furthermore, address a stock discrepancy for the 'Pet Bed' (item #7381052709) by modifying its inventory count to 35 units. Lastly, revise the Pet Bed's price to the new promotional rate of $189.99."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "7381052709", "value": 35}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 189.99})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_033",
        instruction="As a senior manager, you are tasked with conducting a thorough audit of customer Mei Campbell (user ID: mei_campbell_4785) and her delivered order #W7303089. This involves an extensive examination of her account, payment methods, as well as the full logistics trail of the shipment. During the product review, you decide to discontinue the 'Backpack' (item #2492465580) that she ordered. At the same time, you come across a pricing discrepancy: the 'Pet Bed' (item # W7303089. This requires a thorough review of her account, payment options, and the complete shipment logistics. During the product assessment, you opt to remove the 'Backpack' (item #2492465580) from the order. Additionally, you identify a pricing error: the 'Pet Bed' (item #7381052709) is incorrectly priced at $193.22 and should be corrected to $199.99. You need to update the price and also modify the stock status"
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_034",
        instruction="You are required, as a senior manager, to conduct an audit of the supplier 'Kitchen Essentials Co.' (#SUP0012). The assignment involves obtaining a complete overview of their products and reviewing the available variations within their 'Fleece Jacket' product line. You detect that the 'L black full-zip' variant (item #9385662952) is shown as available in the product catalog but is reported as out of stock by the supplier; you need to resolve this inconsistency. Moreover, you have to remove an outdated cancelled supply order, #SO7147, related to this supplier. To finalize your audit, examine the full order history of a related customer, Evelyn Anderson (user ID: evelyn_anderson_4614), and subsequently update the status of her latest order, # The task requires a comprehensive review of their products, specifically the variations in the 'Fleece Jacket' line. It has been noted that the 'L black full-zip' option (item #9385662952) is listed as available in the catalog but is marked out of stock by the supplier, necessitating resolution of this discrepancy. Additionally, an obsolete cancelled supply order, #SO7147, associated with this supplier should be removed. To complete the audit, analyze the full order history for"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8560156827"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0012", "item_id": "9385662952"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "8560156827", "item_id": "9385662952", "available": False}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="GetUserDetails", kwargs={"user_id": "evelyn_anderson_4614"}),
            Action(name="GetUserOrders", kwargs={"user_id": "evelyn_anderson_4614"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "audit_pending"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_035",
        instruction="As a customer service manager, your duty involves managing a return for Raleigh Moore (user ID: charlotte_moore_2033) regarding her order, #W4817420. She intends to return the 'Electric Kettle' (item #9624127908) and also wishes to modify her address to 996 Cedar Street, Suite 700, San Antonio, NM, 78234. Your role is to facilitate this return by coordinating with the supplier to restock the item. During this process, you come across an outdated cancelled supply order (#SO5813) related to another item from her purchase, which needs to be eliminated. To show goodwill, decide on reducing the price of the 'Bookshelf' (item # W4817420. She plans to return the 'Electric Kettle' (item #9624127908) and update her address to 996 Cedar Street, Suite 700, San Antonio, NM, 78234. Your task is to coordinate with the supplier to restock the item. During this, you find an obsolete canceled supply order (#SO5813) related to another item from her order that needs to be removed. As a gesture of goodwill, reduce the price of the '"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1075968781"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908", "value": 194}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "charlotte_moore_2033", "address": {"address1": "996 Cedar Street", "address2": "Suite 700", "city": "San Antonio", "state": "NM", "zip": "78234", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "8600330539"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "8600330539", "item_id": "4900661478", "price": 450.00}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W4817420"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_036",
        instruction="Acting as a product manager, your task involves revamping the 'Fleece Jacket' product line (product #8560156827) from 'Kitchen Essentials Co.' (#SUP0012). The objective is to phase out select variants and modify the prices of those remaining. It's essential to render the 'red half-zip' (item #5992316252) and the 'navy full-zip' (item #8161321868) jackets as unavailable for purchase by altering their stock status. Additionally, remove the outdated cancelled supply order #SO7147. To enhance sales of the leftover jackets, decrease the price of the 'navy half-zip' variant (item # The goal is to discontinue certain variants and adjust prices for the remaining ones. Set the 'red half-zip' (item #5992316252) and 'navy full-zip' (item #8161321868) jackets to unavailable by changing their stock status. Also, eliminate the obsolete cancelled supply order #SO7147. To boost sales of the remaining jackets, lower the price of the 'navy half-zip' variant (item #8590708195) to $"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0012"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8560156827"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO7147"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0012", "item_id": "5992316252", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "8560156827", "item_id": "5992316252", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0012", "item_id": "8161321868", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "8560156827", "item_id": "8161321868", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "8560156827", "item_id": "8590708195", "price": 155.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "5992316252"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8161321868"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8590708195"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_037",
        instruction="As a manager overseeing a data integrity initiative, it is your task to probe and rectify records associated with the supplier 'Digital Paradise Distributors' (#SUP0004). This necessitates a comprehensive assessment of their product catalog and the elimination of an outdated cancelled supply order, #SO9426. Upon reviewing their products, decide to cease the '4-piece red hardshell' Luggage Set (item #9956648681). Additionally, you must address a separate customer issue involving Omar Khan (user ID: omar_khan_2363) whose order, # SUP0004). This requires a thorough evaluation of their product list and the removal of a discontinued supply order, #SO9426. After reviewing their products, decide to discontinue the '4-piece red hardshell' Luggage Set (item #9956648681). Additionally, resolve a separate customer issue with Omar Khan (user ID: omar_khan_2363) regarding his order, #W6304490, which includes an item from a different supplier and is pending a final"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetProductDetails", kwargs={"product_id": "5426915165"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO9426"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0004", "item_id": "9956648681", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "5426915165", "item_id": "9956648681", "available": False}),
            Action(name="GetUserDetails", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W6304490", "status": "audit_complete"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_038",
        instruction="Being a senior manager tackling a complex customer service and logistics issue concerning order #W4817420, you must handle Raleigh Moore's (user ID: charlotte_moore_2033) claim that her entire shipment was lost, prompting the need for a replacement. The original order consists of several items from multiple suppliers. Execute a comprehensive investigation, verify which items remain in stock, and coordinate a re-shipment for only those available, using 'AgileTransport Services' (#COU0004) with tracking ID 757848843226. For the out-of-stock item, the 'Action Camera', locate the related cancelled supply order, # W4817420, address Raleigh Moore's (user ID: charlotte_moore_2033) claim of a lost shipment requiring a replacement. The original order includes multiple items from various suppliers. Conduct a thorough investigation, confirm stock availability, and arrange a re-shipment for available items using 'AgileTransport Services' (#COU0004) with tracking ID 757848843226. For the out-of-stock 'Action Camera', find the associated cancelled supply order, #SO699"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetUserDetails", kwargs={"user_id": "charlotte_moore_2033"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6777246137"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8600330539"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "4900661478"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1075968781"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9624127908"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7363354090"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3812493782"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="AssignCourierToOrder", kwargs={"order_id": "#W4817420", "courier_id": "#COU0004", "tracking_ids": ["757848843226"], "item_ids": ["6777246137", "4900661478", "9624127908", "3812493782"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partial_reshipment_pending"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_039",
        instruction="You are managing a multi-part request for customer William Li (ZIP: 10083). He is returning the 'Office Chair' (#8426249116) from order #W2611340 and needs his address updated to 215 River Road, Suite 1000, Brooklyn, CT, 10083. Handle the return by restocking the chair with its supplier, 'Worldwide Electronics Partners'. While doing this, you notice a supply order for a 'Laptop' (#SO5813) from this supplier was cancelled. To avoid a potential stockout of that laptop (item # Update the address for order #W2611340 to 215 River Road, Suite 1000, Brooklyn, CT, 10083. Restock the chair with the supplier 'Worldwide Electronics Partners'. Note that a supply order for a 'Laptop' (#SO5813) from this supplier was cancelled; to prevent stockout for the laptop (item #3265035808), increase its price to $2550.00 and mark it as temporarily unavailable. Finally, update the customer's address and"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "James", "last_name": "Li", "zip": "10083"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "william_li_5688", "address": {"address1": "215 River Road", "address2": "Suite 1000", "city": "Brooklyn", "state": "CT", "zip": "10083", "country": "USA"}}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4760268021", "item_id": "3265035808", "price": 2550.00}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4760268021", "item_id": "3265035808", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_040",
        instruction="You are a manager conducting an audit on a delivered order, #W6304490, for customer Omar Khan (user ID: omar_khan_2363). This audit necessitates a comprehensive review of the customer's payment history for the order and the complete logistics trail, including the courier. During the product audit, you discover that two items from the order have been discontinued by their suppliers: the 'Skateboard' (item #6956751343) and the 'Smart Thermostat' (item #4983901480). You need to update the availability for both of these items in the product catalog to prevent future sales. As a final measure, you have decided to adjust the price of another high-stock item in the order, the 'Garden Hose' (item # W6304490, for customer Omar Khan (user ID: omar_khan_2363). This audit requires a thorough evaluation of the customer's payment history for the order and the entire logistics process, including the courier. During the product audit, it was found that two items from the order have been discontinued by their suppliers: the 'Skateboard' (item #6956751343) and the 'Smart Thermostat' (item #4983901480). You must update the product"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0010"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "1968349452", "item_id": "6956751343", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "4896585277"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": False}),
            Action(name="GetProductDetails", kwargs={"product_id": "6679515468"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6679515468", "item_id": "5753502325", "price": 90.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_041",
        instruction="As a manager, your responsibility is to resolve a complicated return for customer Evelyn Anderson (user ID: evelyn_anderson_4614) concerning her order #W9077205. The return involves two items: the 'Jigsaw Puzzle' (item #9370300555) and the 'Dumbbell Set' (item #3877338112). During the return process, you observe that 'Athletic Equipment Co.', the provider for the dumbbell set, fulfilled a supply order (# W9077205. The return includes two products: the 'Jigsaw Puzzle' (item #9370300555) and the 'Dumbbell Set' (item #3877338112). While processing the return, you note that 'Athletic Equipment Co.', the supplier for the dumbbell set, completed a supply order (#SO5817) that was not accurately logged in the inventory. Your task is to manage the customer's return by restocking both items with their respective suppliers and to"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "completed_return"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1808611083"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555", "value": 72}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813", "value": 142})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_042",
        instruction="As a manager, your task is to oversee a thorough audit of a completed order, #W7303089, for customer Mei Campbell (user ID: mei_campbell_4785, ZIP: 75208). The audit involves a comprehensive review of the customer's payment methods, the financial transaction related to the order (payment_id: credit_card_4785), and all shipment details, including identifying the responsible courier (#COU0001). While reviewing the order's items, you are informed that the 'Backpack' (product: 2524789262, item #2492465580, supplier: # W7303089, regarding customer Mei Campbell (user ID: mei_campbell_4785, ZIP: 75208). The audit entails a thorough examination of the customer’s payment methods, the financial transaction for the order (payment_id: credit_card_4785), and all shipping details, including the assigned courier (#COU0001). During the review of the order items, it is noted that the 'Backpack' (product: 2524789262, item #249"
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_043",
        instruction="As a product manager, you are coordinating a strategic review for the supplier 'Workplace Solutions Center' (#SUP0008). Your aim is to gain a comprehensive understanding of their catalog and tidy up their related data. You are required to obtain a list of all products they offer and examine the available variants for their 'Desk Lamp' product series. During the review, you decide to discontinue the 'black AC adapter' lamp (item #7624783998) because of its low performance. You need to update its stock status and availability. Additionally, you identify two outdated canceled supply orders (#SO5916, #SO1037) for this supplier that must be removed from the system. Lastly, to comprehend the sales performance of this supplier, you are to carry out a comprehensive review of a customer order, # Your objective is to thoroughly analyze their product catalog and organize the associated data. You must compile a list of all available products and investigate the variants for the 'Desk Lamp' line. Upon review, you decide to phase out the 'black AC adapter' lamp (item #7624783998) due to its poor performance, necessitating an update to its stock status and availability. Additionally, you identify and need to delete two obsolete canceled supply orders (#SO5916, #SO1037) from"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "6817146515"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7624783998"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6817146515", "item_id": "7624783998", "available": False}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5916"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO1037"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetUserDetails", kwargs={"user_id": "william_li_5688"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_044",
        instruction="As a senior manager, you are tasked with handling a lost shipment claim for customer Ella White (user ID: evelyn_anderson_4614) about her delivered order #W9077205. She has also requested an update to her shipping address to 388 Elm Avenue, Suite 500, Houston, NM, 75215. Your responsibility involves conducting a thorough investigation of the original shipment, including identifying the courier involved, and then arranging a full replacement. After confirming that all items are in stock, you must also respond to a low-stock alert for the 'Jigsaw Puzzle' by speeding up its pending supply order (# W9077205. The customer has requested to change her shipping address to 388 Elm Avenue, Suite 500, Houston, NM, 75215. You are tasked with thoroughly investigating the original shipment, determining the courier involved, and arranging a complete replacement. Once you verify that all items are available, you must expedite the supply order (#SO6372) for the low-stock 'Jigsaw Puzzle'. Lastly, update the customer's address and assign 'SpeedWay Delivery' as the new courier,"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetUserDetails", kwargs={"user_id": "evelyn_anderson_4614"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9077205"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0009"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1808611083"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(
                name="UpdateUserAddress",
                kwargs={
                    "user_id": "evelyn_anderson_4614",
                    "address": {
                        "address1": "388 Elm Avenue",
                        "address2": "Suite 500",
                        "city": "Houston",
                        "state": "NM",
                        "zip": "75215",
                        "country": "USA"
                    }
                }
            ),
            Action(name="FindCourierByTrackingId", kwargs={"tracking_id": "682308736931"}),
            Action(
                name="AssignCourierToOrder",
                kwargs={
                    "order_id": "#W9077205",
                    "courier_id": "#COU0001",
                    "tracking_ids": ["682308736931"],
                    "item_ids": ["9370300555", "3877338112"]
                }
            ),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "processing"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_045",
        instruction="As a manager, you are tasked with resolving a customer issue for Mei Campbell (user ID: mei_campbell_4785). She has received her order #W7303089, but the 'Backpack' (item #2492465580) is in the wrong color, prompting her to wish for a return. Your responsibility is to manage this partial return and take care of all associated inventory and data updates. You need to trace the item back to its supplier and ensure it is restocked. Additionally, you've identified that the customer's address on file is incomplete and needs updating to '858 Elm Street, Suite 912, Oakland, NV, 95170'. While reviewing the supplier's other offerings, you have decided to discontinue the 'green leather backpack' (item # W7303089, however, the 'Backpack' (item #2492465580) is the incorrect color, leading her to request a return. You must handle this partial return and manage all related inventory and data changes. It is necessary to trace the item back to its supplier for restocking. Furthermore, the customer's recorded address is incomplete and must be updated to '858 Elm Street, Suite 912, Oakland, NV, 95170'. Upon reviewing the supplier’s other products,"
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "mei_campbell_4785", "address": {"address1": "858 Elm Street", "address2": "Suite 912", "city": "Oakland", "state": "NV", "zip": "95170", "country": "USA"}}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": 189}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "7251508981", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "7251508981", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W7303089", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_046",
        instruction="Acting as a senior operations analyst, you are tasked with conducting a full audit of a delivered customer order, #W7303089. Your assignment is to examine the complete lifecycle of this order, covering customer details, payment history, and the thorough logistics trail from the courier. In addressing the products ordered, you need to tackle two distinct issues. Firstly, resolve a supply chain bottleneck for the supplier of the 'Pet Bed' by accelerating their pending supply order, #SO5398. Secondly, you must manage the discontinuation of the 'Backpack' variant (item # W7303089. Your task is to analyze the entire lifecycle of this order, including customer information, payment records, and a detailed logistics overview from the courier. Regarding the ordered products, you need to address two separate concerns. First, eliminate a supply chain delay for the 'Pet Bed' supplier by expediting their outstanding supply order, #SO5398. Second, handle the removal of the 'Backpack' variant (item #2492465580) from the order by modifying its stock"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5398"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_047",
        instruction="As a manager, you will handle a thorough audit of customer Mei Campbell (user ID: mei_campbell_4785) and her account activities. Begin by gathering her entire order history and all payment methods on file. For delivered order #W7303089, you will need to conduct an in-depth analysis of the complete shipping history and pinpoint the courier involved. In a product line evaluation related to this order, you have decided to cease offering the 'Backpack' variant she bought (item #2492465580). Additionally, you are required to rectify an inventory inconsistency for the other product in her order, a 'Pet Bed' (item # W7303089, perform a thorough examination of the entire shipping history and identify the courier used. In the product line review for this order, you have opted to discontinue the 'Backpack' variant purchased (item #2492465580). Furthermore, you must resolve an inventory discrepancy for the other product in her order, a 'Pet Bed' (item #7381052709), by updating its stock to 35 units."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserOrders", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "7381052709", "value": 35})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_048",
        instruction="Holding a senior management role, you are tasked with coordinating a multi-faceted request from customer Sofia Russo (user ID: sofia_russo_8776) about her pending order #W5918442. She is looking to cancel the entire order and has also asked for her file address to be updated to '456 Market St, San Francisco, NV, 94105'. It is your responsibility to fulfill these requests and perform a comprehensive inventory reconciliation. You must eliminate the order, revise her profile, and subsequently restock each item from the canceled order with its appropriate supplier. During these tasks, you'll find that an 'Action Camera' (item # W5918442 wishes to cancel her entire order and update her file address to '456 Market St, San Francisco, NV, 94105'. You are tasked with completing these requests and conducting a full inventory reconciliation. This includes canceling the order, updating her profile, and restocking each item from the canceled order with the correct supplier. Additionally, you will notice that an 'Action Camera' (item #1586641416) has been mistakenly marked as discontinued; correct this error by resetting"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="GetUserDetails", kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "sofia_russo_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "NV", "zip": "94105", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "6858788497"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_049",
        instruction="In your role as a senior manager, handle a cancellation request for order #W8327915 from customer Raleigh Jackson (user ID: charlotte_jackson_2676). She wishes to cancel the 'Skateboard' (item #6956751343) from her purchase. Your responsibility is to coordinate this partial cancellation by restocking the item with the supplier. Upon reviewing the order, you notice that the 'Air Purifier' (item #1327854740) is no longer in production, requiring you to mark it as unavailable in the product catalog. You also have to remove an outdated supply order (# W8327915 from customer Raleigh Jackson (user ID: charlotte_jackson_2676) requests to cancel the 'Skateboard' (item #6956751343) from her order. You need to facilitate this partial cancellation by restocking the item with the supplier. Upon checking the order, you find that the 'Air Purifier' (item #1327854740) is discontinued, so it should be marked as unavailable in the product catalog. Additionally, remove the obsolete supply"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8327915"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "6956751343"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "6956751343", "value": 35}),
            Action(name="GetProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3821016478", "item_id": "1327854740", "available": False}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO6767"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W8327915", "tracking_ids": ["956166462388"], "item_ids": ["2025713343", "1684786391", "4358482460"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W8327915", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_050",
        instruction="As a senior manager, you are tasked with carrying out a comprehensive audit of the supplier 'Home Essentials Co.' (#SUP0006). Your objective is to obtain a full overview of their product catalog, including all existing variants in their 'Patio Umbrella' range, and to conduct the necessary data cleanup. This involves eliminating an outdated cancelled supply order, #SO3933. You need to rectify an inventory data mistake for their 'red olefin' patio umbrella (item #8170914468) by adjusting its stock level to 50 units. To complete the audit, you will also review the complete order history of a related customer, Ahmad Khan (user ID: ahmad_khan_7091), and assess the specifics of his order # Your task is to acquire a comprehensive understanding of their product catalog, focusing on all variants in the 'Patio Umbrella' line, and perform the necessary data cleansing. This includes removing an obsolete cancelled supply order, #SO3933. Additionally, correct the inventory discrepancy for the 'red olefin' patio umbrella (item #8170914468) by updating its stock to 50 units. Lastly, review the entire order history for customer Ahmad Khan (user ID: ahmad_khan_"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0006"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9743693396"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "9743693396"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "8170914468", "value": 50}),
            Action(name="GetUserDetails", kwargs={"user_id": "ahmad_khan_7091"}),
            Action(name="GetUserOrders", kwargs={"user_id": "ahmad_khan_7091"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W1787190"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_051",
        instruction="As a senior analyst, you are tasked with a comprehensive review of the supplier 'Workplace Solutions Center' (#SUP0008). Your job is to obtain a full list of all products they offer and evaluate the available variants for their 'Desk Lamp' product line. During the audit, you identify that the pending supply order #SO5771 involves an item with low demand. To optimize resource allocation, you are required to cancel this supply order. Following this, examine the entire order history of a customer, Sofia Russo (user ID: sofia_russo_8776), who has previously bought items from this supplier, and delve into the specifics of her order #W5918442 to assess sales performance. Lastly, you have decided to remove the 'green latex garden hose' (item # Your task is to compile a comprehensive list of all products offered and assess the variants available for the 'Desk Lamp' line. During the audit, you notice that supply order #SO5771 contains an item with low demand, necessitating its cancellation to enhance resource allocation. Next, review the complete order history of customer Sofia Russo (user ID: sofia_russo_8776), who has previously made purchases from this supplier, and analyze the details of order #W5918442 to evaluate"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0008"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "6817146515"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5771", "status": "cancelled"}),
            Action(name="GetUserOrders", kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6679515468"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6679515468", "item_id": "3230708338", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "3230708338", "value": "discontinued"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_052",
        instruction="As a senior manager, your responsibility is to perform a complete audit targeting a key customer, Mei Campbell (user ID: mei_campbell_4785), and her delivered order, #W7303089. Your objective is to gain a thorough understanding of her account, covering all payment methods, and trace the full logistics path of her order. The audit should then broaden to include the suppliers of the purchased items. Regarding the supplier of the 'Backpack', you need to compile their entire product catalog. As for the supplier of the 'Pet Bed', you are to conduct a data cleanup by removing their outdated cancelled supply order, # W7303089. Your task is to comprehensively analyze her account, encompassing all payment options, and track the complete logistics flow of her order. The audit should also extend to the suppliers of the purchased products. For the 'Backpack' supplier, gather their complete product catalog. For the 'Pet Bed' supplier, perform data maintenance by eliminating their obsolete cancelled supply order, #SO6998."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO6998"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_053",
        instruction="As a customer service lead, manage a detailed request from VIP customer Sofia Russo (user ID: sofia_russo_8776). Her latest order, # W5918442 is pending, and she aims to completely modify it. She wants to cancel the order and update her address to 456 Market St, San Francisco, NV, 94105. You need to fulfill this combined request: cancel the order, update her profile with the new address, and conduct a full inventory reconciliation for all items in the cancelled order, assigning each to its correct supplier, omitting any unavailable items."
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="GetUserDetails", kwargs={"user_id": "sofia_russo_8776"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "sofia_russo_8776", "address": {"address1": "456 Market St", "address2": "", "city": "San Francisco", "state": "NV", "zip": "94105", "country": "USA"}}),
            Action(name="GetProductDetails", kwargs={"product_id": "6858788497"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_054",
        instruction="As a senior manager, you are coordinating a dual role today. Begin by carrying out a comprehensive audit of the supplier 'Fresh Market Co.' (#SUP0005). This entails acquiring a complete list of their product lines and examining all available variants for their 'Bicycle' product. During the audit, you must also organize their historical data by removing the outdated cancelled supply order #SO2516. In a separate task, you need to address a paused customer order, # This requires obtaining a comprehensive list of their product lines and reviewing all variations of the 'Bicycle' product. During the audit, ensure to sort their historical data by deleting the obsolete cancelled supply order #SO2516. Additionally, you need to resolve the halted customer order #W9318778, which is pending due to an out-of-stock item from a different supplier. Dispatch the available items from this order right away using tracking ID 836251433228 and update the order's status."
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0005"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "9783735446"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9318778"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9318778", "tracking_ids": ["836251433228"], "item_ids": ["2143041831", "6342039236", "9850781806", "3076708684"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9318778", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_055",
        instruction="As a product manager, it is your duty to handle an audit of the 'Digital Paradise Distributors' supplier (#SUP0004). Your responsibility involves obtaining a comprehensive overview of their product lines and then listing all available variants for their 'Luggage Set' product (product #5426915165). During this review, you make the decision to discontinue the '4-piece red hardshell' variant (item #9956648681) due to inadequate sales. You are required to update its stock status and render it unavailable. Simultaneously, an issue with customer order #W9077205 arises, involving a returned product from a different supplier. You must manage this return by restocking the 'Dumbbell Set' (item # Your task is to gather a detailed summary of their product offerings and compile a list of all variants for the 'Luggage Set' (product #5426915165). As part of this assessment, you decide to phase out the '4-piece red hardshell' variant (item #9956648681) due to poor sales performance. You need to update its inventory status to unavailable. Additionally, there is a return issue with customer order #W9077205, which involves a product from"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0004"}),
            Action(name="GetProductDetails", kwargs={"product_id": "5426915165"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "5426915165"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "5426915165", "item_id": "9956648681", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0004", "item_id": "9956648681", "value": "discontinued"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": 65})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_056",
        instruction="As a product manager, you are tasked with coordinating an audit of the 'Athletic Equipment Co.' supplier (#SUP0010). Your objective is to gain a full understanding of their product catalog and eliminate outdated records. You need to compile a list of all products they provide and subsequently list all available variants for their 'Dumbbell Set' product line. During your examination, you find that an old, cancelled supply order (#SO5817) for a different product remains in the system and needs removal. You also opt to discontinue the '55-75 lbs iron fixed' dumbbell set (item #2444431651) due to unsatisfactory sales. Ultimately, you must adjust the price of the 'adjustable 5-25 lbs rubber' dumbbell set (item # Your task is to thoroughly review their product catalog and remove any obsolete entries. Compile a comprehensive list of all products offered and detail the variants for the 'Dumbbell Set' line. During your review, identify and delete an outdated supply order (#SO5817) for a different item. Additionally, decide to phase out the '55-75 lbs iron fixed' dumbbell set (item #2444431651) due to poor sales performance. Finally, update the price of the 'adjustable"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0010"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "7233192239"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7233192239", "item_id": "2444431651", "available": False}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "2444431651", "value": "discontinued"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7233192239", "item_id": "7896397433", "price": 475.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_057",
        instruction="As a product manager, handle a comprehensive audit and update the data for all products provided by 'TechCorp' (#SUP0003). Your objective is to verify that all their product entries are correct. Obtain a complete list of the products they supply and, specifically for their 'Tablet' product line (product #8024098596), acquire a list of all currently available models. During your review, you observe that a particular tablet variant (item #2235648106) has an incorrect price, and you need to adjust its price to $1099.99. Additionally, there is an outdated, pending supply order (# Your task is to confirm the accuracy of all product entries. Gather a full list of the products offered, and specifically for the 'Tablet' line (product #8024098596), compile a list of all available models. During your assessment, you find that a specific tablet variant (item #2235648106) has an incorrect price that needs to be updated to $1099.99. Furthermore, eliminate the obsolete pending supply order (#SO5993) for 'TechCorp' as it"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8024098596"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "8024098596"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2235648106"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "8024098596", "item_id": "2235648106", "price": 1099.99}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5993"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2235648106"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="As a senior logistics manager, manage a lost shipment for order #W2611340, linked to customer William Li (user ID: william_li_5688). Your task is to inquire into the original shipment details and coordinate a replacement. Examine the order to determine all items and associated suppliers, and verify current inventory to ascertain what can be re-shipped. As part of a supplier performance review, obtain complete information on the supplier of the stocked item. Lastly, designate 'SpeedWay Delivery' (# W2611340 is associated with customer William Li (user ID: william_li_5688). Your objective is to investigate the initial shipment details and arrange for a replacement. Review the order to identify all items and their respective suppliers, and check current inventory to see what can be re-shipped. For the supplier performance evaluation, gather comprehensive information on the supplier of the stocked item. Finally, assign 'SpeedWay Delivery' (#COU0001) with tracking ID 403338127473 for"
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="GetSupplierProducts", kwargs={"supplier_id": "#SUP0003"}),
            Action(name="ListAvailableVariants", kwargs={"product_id": "7471004230"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="GetUserOrders", kwargs={"user_id": "mei_ahmed_5058"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2631563"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "6477915553"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7471004230", "item_id": "6477915553", "price": 199.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "6477915553"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_058",
        instruction="As a senior logistics manager, manage a lost shipment for order #W2611340, linked to customer William Li (user ID: william_li_5688). Your task is to inquire into the original shipment details and coordinate a replacement. Examine the order to determine all items and associated suppliers, and verify current inventory to ascertain what can be re-shipped. As part of a supplier performance review, obtain complete information on the supplier of the stocked item. Lastly, designate 'SpeedWay Delivery' (# W2611340 pertains to customer William Li (user ID: william_li_5688). Please investigate the original shipment details and arrange for a replacement. Review the order to identify all items and their suppliers, and check current inventory to see what can be re-shipped. As part of evaluating supplier performance, gather comprehensive information on the supplier of the stocked item. Finally, assign 'SpeedWay Delivery' (#COU0001) with tracking ID 403338127473 for the re-shipped"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="AssignCourierToOrder", kwargs={"order_id": "#W2611340", "courier_id": "#COU0001", "tracking_ids": ["403338127473"], "item_ids": ["8426249116"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_060",
        instruction="Act as a logistics manager performing a comprehensive audit of delivered order #W7303089 for Mei Campbell (user ID: mei_campbell_4785, ZIP: 75208). Ensure thorough verification of the customer's payment methods (payment: credit_card_4785), the order's financial transaction, and all shipping details, including the courier involved. While auditing the products, you identify that the supplier for the 'Pet Bed' (product: 2747247837, item #7381052709) has a pending supply order, #SO5398, requiring expediting (status: expedited) to maintain future inventory levels. Furthermore, you've resolved that the 'Backpack' (product: 2524789262, item # W7303089 for Mei Campbell (user ID: mei_campbell_4785, ZIP: 75208). Confirm the customer's payment methods (payment: credit_card_4785), the order's financial transaction, and all shipping details, including the courier. During product auditing, you found that the supplier for the 'Pet Bed' (product: 2747247837, item #7381052709) has an outstanding supply order, #SO5398, that needs to be"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 229.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2492465580"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_061",
        instruction="As a logistics manager auditing 'International Speed Services' (#COU0010), begin by reviewing one shipment (tracking ID 574237175837) and complete a full trace. This involves confirming the customer, Omar Khan, analyzing his comprehensive order history and payment methods, and inspecting all items in order #W6304490. During this review, note that the 'Skateboard' (#6956751343) is from a supplier with an outdated cancelled supply order (#SO2516) requiring deletion. Additionally, the 'Smart Thermostat' (#4983901480) is out of stock; make it unavailable. Conclude by adjusting the price of the 'Air Purifier' (# COU0010), start by examining the shipment (tracking ID 574237175837) and perform a complete trace. This includes verifying the customer, Omar Khan, reviewing his full order history and payment options, and checking all items in order #W6304490. Note that the 'Skateboard' (#6956751343) is linked to a supplier with a cancelled supply order (#SO2516) that needs to be removed. Furthermore, the 'Smart Thermostat' (#498"
        actions=[
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0010"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetUserDetails", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetUserOrders", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO2516"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4896585277"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "3821016478", "item_id": "9375701158", "price": 480.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_062",
        instruction="As a product manager carrying out an audit and update on the 'Running Shoes' product line (product #6938111410) from supplier #SUP0006, due to a cancelled supply order (#SO3933), discontinue the 'yellow synthetic' variant (item #9791469541) and update the catalog to reflect its unavailability. To boost sales of the existing stock, initiate a promotional campaign. Start by checking the current stock and pricing of the 'red leather' variant (#4153505238) and the 'white mesh' variant (# Remove the 'yellow synthetic' variant (item #9791469541) from supplier #SUP0006 due to the cancellation of supply order (#SO3933) and update the catalog to indicate it is unavailable. To increase sales for the remaining stock, launch a promotional campaign. First, assess the current stock and pricing for the 'red leather' variant (#4153505238) and the 'white mesh' variant (#9635758562). Then, adjust the prices of both the red leather"
        actions=[
            Action(name="GetProductDetails", kwargs={"product_id": "6938111410"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4153505238"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "9635758562"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 149.99}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6938111410", "item_id": "9635758562", "price": 149.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "9791469541"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4153505238"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "9635758562"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_063",
        instruction="As a senior manager, please coordinate the processing of a cancellation request for order #W2611340 from customer William Li (user ID: william_li_5688). Your duty is to cancel the order and execute a comprehensive inventory reconciliation for all items. This involves tracking each item to its supplier and restocking it, ensuring not to restock any items that are currently marked as 'out_of_stock'. Since one of the items is currently out of stock, you must also look into the supplier's pipeline by examining their pending supply order # W2611340 from client William Li (user ID: william_li_5688). Your task is to annul the order and perform a thorough inventory reconciliation for all products. This requires tracing each item back to its supplier for restocking, while avoiding restocking any items labeled as 'out_of_stock'. Given that one item is out of stock, you should also review the supplier's pipeline by checking their pending supply order #SO5771 and prioritize it. Lastly, collect the customer's full user and"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetUserDetails", kwargs={"user_id": "william_li_5688"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "william_li_5688"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "cancelled"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_064",
        instruction="As a senior manager, you are tasked with conducting a comprehensive audit of the 'Tech Supplies Inc.' supplier (#SUP0001). Your investigation begins with their pending supply order, #SO9359. You are required to confirm its details and, given its significance, change its status to 'expedited'. As part of the audit, you will also need to examine a delivered customer order, #W7303089, which includes an item from another supplier but was managed by a courier, 'SpeedWay Delivery', whom you are also assessing. Your role involves thoroughly examining this customer order, including verifying the customer's information and payment methods, the complete tracking history, and the courier's details. Ultimately, after your assessment, you've concluded that the 'Backpack' (item # Your investigation starts with the pending supply order, #SO9359. You must verify its details and change its status to 'expedited' due to its importance. Additionally, you will review a delivered customer order, #W7303089, which contains an item from a different supplier and was handled by 'SpeedWay Delivery', which is also under evaluation. Your task includes a comprehensive review of this customer order, confirming the customer’s information and payment methods, the full tracking history, and details about"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO9359", "status": "expedited"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2524789262", "item_id": "2492465580", "price": 225.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2492465580"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_065",
        instruction="As the operations manager, your responsibility is to handle a complete cancellation for a pending order, # W5918442, related to customer Sofia Russo (ZIP: 78784), who has canceled her order. Please proceed to cancel the order and conduct a complete inventory reconciliation. For each item, trace it back to the supplier and adjust their stock levels accordingly, but do not restock items marked as 'discontinued' by the supplier."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6858788497"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_066",
        instruction="As a manager conducting an audit of the 'Worldwide Electronics Partners' supplier (#SUP0002), your audit starts with their cancelled supply order, #SO3880. You must verify the involved product, confirm its stock status, and ensure it is listed as unavailable in the public catalog. Your audit should then continue to examine a different, successfully completed customer order, #W2611340, which includes another product from the same supplier. For this customer order, you are required to verify the customer's full details, the payment transaction, and the complete tracking history. Lastly, you have determined that the 'Office Chair' (item # Begin your audit with the cancelled supply order #SO3880. Verify the associated product, check its stock status, and confirm it is marked as unavailable in the public catalog. Next, review a different, successfully completed customer order #W2611340, which contains another product from the same supplier. For this order, validate the customer's complete information, the payment transaction, and the full tracking history. Finally, you have identified that the 'Office Chair' (item #8426249116) in"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO3880"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4794339885", "item_id": "8426249116", "available": False}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetUserDetails", kwargs={"user_id": "william_li_5688"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4794339885", "item_id": "8426249116", "price": 500.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_067",
        instruction="In your role as inventory manager, you are handling a full audit and data correction for the 'Espresso Machine' product line (product #4354588079) from supplier #SUP0009. You have found that a previously cancelled supply order, #SO1273, for one of the options (item #6200867091), is redundant and should be eliminated from the system. Additionally, you have opted to phase out this specific option. You need to adjust its stock status to make it unavailable for purchase. Finally, as part of the audit, confirm the price of another active option, the 'manual 2L' model (item # Remove the redundant supply order #SO1273 for item #6200867091, which has been previously cancelled. Additionally, discontinue this option and update its stock status to unavailable for purchase. As part of the audit, verify the price of the active 'manual 2L' model (item #7774234341) and change it to a new standard price of $2725.00."
        actions=[
            Action(name="GetProductDetails", kwargs={"product_id": "4354588079"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO1273"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "6200867091"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "6200867091", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4354588079", "item_id": "6200867091", "available": False}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7774234341"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4354588079", "item_id": "7774234341", "price": 2725.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "6200867091"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7774234341"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_068",
        instruction="As the product manager for laptops (product #4760268021), you are coordinating a catalog cleanup for the supplier 'Worldwide Electronics Partners'. You must end the availability of the '13-inch silver i7' model (item #2768401027) by modifying its stock status to make it inaccessible for purchase. Additionally, you need to remove an obsolete, cancelled supply order (#SO5813) from the system to streamline historical data. Lastly, to boost sales for an existing model, apply a promotional price of $2650.00 to the '15-inch black i9' laptop (item # You are overseeing a catalog cleanup for the supplier 'Worldwide Electronics Partners'. Change the stock status of the '13-inch silver i7' model (item #2768401027) to make it unavailable for purchase. Also, delete the outdated, cancelled supply order (#SO5813) to tidy up historical records. Finally, to enhance sales for an active model, set a promotional price of $2650.00 for the '15-inch black i9' laptop (item #2913673670"
        actions=[
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "2768401027"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "2768401027", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4760268021", "item_id": "2768401027", "available": False}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="DeleteSupplyOrder", kwargs={"supply_order_id": "#SO5813"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2913673670"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4760268021", "item_id": "2913673670", "price": 2650.00}),
            Action(name="GetVariantDetails", kwargs={"item_id": "2913673670"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_069",
        instruction="You are a retail operations manager addressing a complex return and exchange for customer Raleigh Moore (user ID: charlotte_moore_2033), regarding her order #W4817420. She is returning the 'Action Camera' (item #6700049080) due to a defect. Since that specific model is now unavailable, she has agreed to exchange it for a different model, the 'silver' Action Camera (item # W4817420 is returning the 'Action Camera' (item #6700049080) due to a defect. As this model is no longer available, she has consented to an exchange for the 'silver' Action Camera (item #6117189161). You need to carry out the following steps: update the status of the defective item to 'discontinued', verify the availability of the replacement camera, and arrange for the new camera's delivery using tracking ID 757848843226 through"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": False}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W4817420", "tracking_ids": ["757848843226"], "item_ids": ["6117189161"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "exchange_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_070",
        instruction="As a senior manager, you are addressing an issue for customer William Li (user ID: william_li_5688, ZIP: 43198, payment: paypal_5688) whose order, #W2611340, was lost during transit and needs to be cancelled. The order includes items from various suppliers (#SUP0008, # Order W2611340 was lost during shipping and must be canceled. It contains products from multiple suppliers (#SUP0008, #SUP0002). You are tasked with handling the cancellation and performing a full inventory reconciliation. Trace each product (IDs: 8310926033, 4794339885; items: 6469567736, 8426249116) back to their respective suppliers and restore the quantities (stock: 158) from this order to the suppliers' inventory records"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W2611340"}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "cancelled"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_071",
        instruction="As a product line manager for 'Running Shoes' (product #6938111410) from supplier #SUP0006, you have opted to discontinue the 'yellow synthetic' variant (item #9791469541) due to a cancelled supply order (#SO3933). Your responsibility is to update the product catalog to reflect this change by marking the item as unavailable. Simultaneously, adjust the pricing for two other variations within the same product line to boost sales: set the price of the 'black synthetic' shoe (item #4107812777) to $159.99, and the 'red leather' shoe (item # You have chosen to remove the 'yellow synthetic' variant (item #9791469541) from supplier #SUP0006 due to the cancellation of supply order #SO3933. Please update the product catalog to indicate that this item is now unavailable. Additionally, revise the prices of the two remaining variants to enhance sales: set the 'black synthetic' shoe (item #4107812777) at $159.99, and the 'red leather' shoe (item #4153505238"
        actions=[
            Action(name="GetProductDetails", kwargs={"product_id": "6938111410"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6938111410", "item_id": "4107812777", "price": 159.99}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 165.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "9791469541"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4107812777"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4153505238"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_072",
        instruction="In your role as a senior manager, you are overseeing a comprehensive audit of the order #W3113816 delivered to customer Olivia Rodriguez (user ID: olivia_rodriguez_9753). Your task involves obtaining a complete overview of the transaction and its supply chain. Ensure that you verify the customer's full details, including all payment methods stored on her account, and specifics about the payment for this particular order. Additionally, you must track the shipment history of the order to determine the courier. During your audit, it becomes apparent that a crucial item in her order, a 'Laptop' (item #3265035808, product #4760268021), is low on stock. To avoid future fulfillment complications, locate the associated cancelled supply order, # W3113816 has been delivered to customer Olivia Rodriguez (user ID: olivia_rodriguez_9753). Your assignment is to gather a comprehensive overview of the transaction and its supply chain. Confirm the customer's complete information, including all payment methods linked to her account, as well as the payment details for this specific order. Additionally, track the order's shipment history to identify the courier. During your review, you will notice that a key item in her order, a 'Laptop' ("
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "olivia_rodriguez_9753"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "olivia_rodriguez_9753"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W3113816"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W3113816"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W3113816"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0002"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "3265035808"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5813", "status": "pending"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_073",
        instruction="You are an inventory manager responsible for coordinating a pricing and availability examination on the 'Laptop' product line (product: Laptop, product_id: 4760268021) from supplier 'Worldwide Electronics Partners' (supplier: #SUP0002, supplier_id: #SUP0002). In your audit, you discovered that the item with ID #8997785118 is wrongly listed as available (available: False) in certain systems. You need to correct this by updating its availability status to False. Simultaneously, you have opted to initiate a promotion on a different variant, the '17-inch silver laptop' (item # For supplier SUP0002, it was found that item ID #8997785118 is incorrectly marked as available (available: False) in some systems. This needs to be rectified by updating its availability status to False. Additionally, a promotion will be launched for another variant, the '17-inch silver laptop' (item #3265035808), by setting its price to $2499.99. After making these changes, verify their correctness by retrieving the final details for both updated variants."
        actions=[
            Action(name="GetSupplierById", kwargs={"supplier_id": "#SUP0002"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4760268021"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8997785118"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4760268021", "item_id": "8997785118", "available": False}),
            Action(name="GetVariantDetails", kwargs={"item_id": "3265035808"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "4760268021", "item_id": "3265035808", "price": 2499.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8997785118"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "3265035808"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_074",
        instruction="As a logistics manager, your task is to address a 'lost in transit' claim for order # W9549057 from client James Andersson (user ID: james_andersson_2485). Conduct a thorough review of the initial shipment, focusing on its tracking history and courier details. Subsequently, check the inventory for all products in the original order to assess the possibility of reshipping. Since one item is out of stock, arrange an immediate partial shipment for the available 'Makeup Kit' with the new tracking ID, 180694848020, and update the order status accordingly."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "james_andersson_2485"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9549057"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9549057"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0010"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9523456873"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "5253880258"}),
            Action(name="GetProductDetails", kwargs={"product_id": "5149340237"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "7736359414"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9549057", "tracking_ids": ["180694848020"], "item_ids": ["7736359414"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9549057", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_075",
        instruction="As a senior customer support manager, you are in charge of processing a return for Evelyn Anderson (ZIP: 75215) concerning her delivered order, #W9077205. The returned item is the 'Jigsaw Puzzle' (item # W9077205. The item being returned is the 'Jigsaw Puzzle' (item #9370300555). Additionally, she has requested to update her address on record to '388 Elm Avenue, Suite 500, Houston, NM, 75215'. Your tasks involve restocking the item with the correct supplier, updating her address as requested, and completing an audit by examining the courier details from the initial shipment. Finally, update the order status to reflect the partial return."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1808611083"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555", "value": 72}),
            Action(name="UpdateUserAddress", kwargs={"user_id": "evelyn_anderson_4614", "address": {"address1": "388 Elm Avenue", "address2": "Suite 500", "city": "Houston", "state": "NM", "zip": "75215", "country": "USA"}}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9077205"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0009"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_076",
        instruction="As an inventory manager, your role involves conducting an audit on supplier #SUP0008 after detecting a data inconsistency related to the filled supply order #SO1037. Your objectives are to rectify the inventory and pricing for the 'Desk Lamp' (item #7624783998). This includes researching the original supply order to ascertain the correct quantity for inventory addition and updating the supplier's stock accurately. Additionally, adjust the price of the item to $159.99. In the course of the comprehensive supplier review, look into their other pending supply order, # SUP0008 identified a data inconsistency with supply order #SO1037. Your tasks are to correct the inventory and pricing for the 'Desk Lamp' (item #7624783998), which involves verifying the original supply order for the accurate quantity to adjust inventory and updating the supplier's stock. Also, revise the item's price to $159.99. During the supplier review, expedite the processing of the other pending supply order, #SO5771. Confirm all updates by retrieving the final variant"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO1037"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6817146515"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "7624783998", "value": 44}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6817146515", "item_id": "7624783998", "price": 159.99}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7624783998"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_077",
        instruction="As a logistics manager, you are managing a 'lost in transit' claim concerning order #W9077205 from customer Ella White (ZIP: 75215). Your aim is to resolve the customer's problem while also addressing a related supply chain issue. Investigate the original shipment's tracking history to identify the courier involved. Before initiating a new shipment, verify stock availability for both items in her order. The supplier for 'Jigsaw Puzzle' is known to be unreliable, so please review their pending supply order # W9077205 from customer Ella White (ZIP: 75215). Your goal is to resolve the customer's issue while also tackling a related supply chain concern. Check the tracking history of the original shipment to determine the courier used. Prior to sending a new shipment, confirm that both items in her order are in stock. The supplier for 'Jigsaw Puzzle' is unreliable, so please assess their pending supply order #SO6372 and expedite it. After your investigation, dispatch replacements for both original items"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W9077205"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0009"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1808611083"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9370300555"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6372", "status": "expedited"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9077205", "tracking_ids": ["682308736931"], "item_ids": ["9370300555", "3877338112"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "processing"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_078",
        instruction="As a manager, you are tasked with coordinating a comprehensive audit on order #W5694685 for customer Ella Kovacs (ZIP: 32117) as it has been marked as pending for an extended period. Your role is to examine the customer's account, including all payment methods, and identify the cause of the delay by checking the product's stock status. You have also received notification that the 'Tea Kettle' (item # W5694685 for customer Ella Kovacs (ZIP: 32117) has been pending for a prolonged period. Your task is to review the customer’s account and all payment methods to determine the cause of the delay by verifying the stock status of the product. Additionally, the 'Tea Kettle' (item #3909406921) in her order is incorrectly priced; please update its price to $95.00 in the catalog. Once the audit and necessary corrections are completed, ship the"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Evelyn", "last_name": "Kovacs", "zip": "32117"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "ella_kovacs_6742"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5694685"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9832717871"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "3909406921"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "9832717871", "item_id": "3909406921", "price": 95.00}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W5694685", "tracking_ids": ["870596657470"], "item_ids": ["3909406921"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5694685", "status": "processing"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_079",
        instruction="As a senior manager conducting a review of customer accounts, your task is to conduct a complete audit of customer Omar Khan's account (user ID: omar_khan_2363). You need to compile a comprehensive overview of his activities. This requires gathering his full user profile, all associated payment methods, and a list of every order he has made. For his latest order, #W6304490, you also need to obtain the entire payment history and delivery tracking details, including identifying the courier. Lastly, it has been observed that the price for the 'Skateboard' (item # W6304490, please ensure you gather the complete payment history and delivery tracking information, including the courier's identity. Additionally, note that the price for the 'Skateboard' (item #6956751343) in this order is below the revised company standard, and it needs to be updated to $225.00."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetUserOrders", kwargs={"user_id": "omar_khan_2363"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W6304490"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0010"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "1968349452", "item_id": "6956751343", "price": 225.00})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_080",
        instruction="Serving as a returns specialist, you are tasked with managing a request from William Li (user ID: william_li_5688, ZIP: 43198, payment: paypal_5688) concerning order #W2611340. He aims to return the 'Office Chair' (product: 4794339885, item #8426249116, supplier: #SUP0002, stock: 158, Office, Chair). Your responsibility is to process this return while simultaneously resolving a possible inventory discrepancy. Track the journey of the returned chair back to the supplier and reintegrate it into their inventory. While auditing the order, also examine the stock status of another item, a 'Water Bottle' (product: 8310926033, item: 6469567736, supplier: #SUP0008), and proactively accelerate (expedited) a pending supply order (#SO5771, supply_order_id: # W2611340 is processing a return for the 'Office Chair' (product: 4794339885, item #8426249116, supplier: #SUP0002, stock: 158). Handle the return while addressing any inventory discrepancies. Monitor the return shipment to the supplier and update their inventory accordingly. Additionally, check the stock for the 'Water Bottle' (product: 8310926033, item: 6469567736, supplier: #SUP0008) and"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116", "value": 158}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5771", "status": "expedited"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W2611340", "status": "partially_returned"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_081",
        instruction="In your role as a senior retail analyst, your responsibility involves assessing the financial and logistical performance associated with customer Mei Campbell (user ID: mei_campbell_4785). Your task involves conducting a comprehensive audit of her delivered order, #W7303089. This should include confirming her personal and payment information, evaluating the order's payment history, and tracking the complete shipment path to determine the courier. During your review of the order's items, it has been brought to your attention that the 'Backpack' (item # W7303089. This involves verifying her personal and payment details, assessing the payment history of the order, and monitoring the entire shipment route to identify the courier. While reviewing the order items, it was noted that the 'Backpack' (item #2492465580) is part of a product line set for discontinuation. Please update its stock status to 'discontinued' with the supplier and ensure it is listed as unavailable in the public product catalog."
        actions=[
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2524789262"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "2492465580", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "2524789262", "item_id": "2492465580", "available": False})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_082",
        instruction="As a logistics manager, your role is to investigate a delivery exception concerning the shipment with tracking ID 889070895653. You need to perform a thorough audit of this shipment, determine the linked customer and order, and verify all of the customer's saved payment methods. Upon reviewing the order's items, one of them appears to be from a supplier with known delays. To prevent future complications, please look into that supplier's pending supply order # SO5398 and expedite its handling. To quickly resolve the customer's issue, reassign the original order for a new shipment with tracking ID 443521489581 via 'RapidTransit Solutions'."
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5398"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5398", "status": "expedited"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W7303089", "tracking_ids": ["443521489581"], "item_ids": ["2492465580", "7381052709"]})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_083",
        instruction="As a senior manager, you are tasked with handling a defective item report from Raleigh Moore (ZIP: 78234) for her order #W4817420 concerning an 'Action Camera' (item #6700049080). Your objective is to manage the return and coordinate a swift audit of the supplier. Investigate the item to ascertain its supplier and verify current stock status. Address the primary failure in the supply chain by rectifying the status of the associated cancelled supply order, #SO6998. Additionally, while evaluating this supplier, you are required to adjust the price of their 'Electric Toothbrush' (item # W4817420 pertains to an 'Action Camera' (item #6700049080). Your task is to oversee the return and facilitate a prompt audit of the supplier. Examine the item to identify its supplier and confirm the current inventory level. Tackle the main issue in the supply chain by updating the status of the related cancelled supply order, #SO6998. Furthermore, while assessing this supplier, you must revise the price of their 'Electric Toothbrush' (item #6164262152"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7352963235"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7352963235", "item_id": "6164262152", "price": 219.99}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_084",
        instruction="As an operations manager, it is your responsibility to conduct a comprehensive investigation into a delayed order, #W9318778, for customer Liam Clark with zip code 20517. The order has been pending for an unusual duration. Determine the root cause of the delay by reviewing the order's items and their stock levels with relevant suppliers. If a stock issue is discovered, investigate the supplier's recent supply orders, such as # W9318778, associated with customer Liam Clark in zip code 20517, has been pending longer than expected. Analyze the order items and stock availability with suppliers to identify the cause of the delay. If a stock problem is found, examine recent supplier orders, like #SO4853, to address any supply chain issues. Once the supply problem is resolved, update the customer's order status to reflect the current situation accurately."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Lucas", "last_name": "Martin", "zip": "20517"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9318778"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3821016478"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "5669664287"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO4853"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO4853", "status": "pending"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9318778", "status": "awaiting_inventory"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_085",
        instruction="As a senior manager, your responsibility includes addressing a damaged item report filed by William Li (user ID: william_li_5688) for his order #W2611340. He states that the 'Office Chair' (item #8426249116) arrived damaged. Along with processing his replacement, you are tasked with conducting a brief evaluation of the supply chain status for another item in his order, a 'Water Bottle'. Your duties involve confirming stock availability for the replacement chair, arranging a new shipment with tracking ID 403338127473, and simultaneously assessing the supply situation for the water bottle. You are informed of a pending supply order, # W2611340 reports that the 'Office Chair' (item #8426249116) was delivered damaged. While processing the replacement, you must also review the supply chain status for the 'Water Bottle' in the same order. Your responsibilities include verifying the stock for the replacement chair, organizing a new shipment with tracking ID 403338127473, and concurrently evaluating the supply status for the water bottle. There is a pending supply order, #SO5771, from the water bottle supplier;"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W2611340"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4794339885"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "8426249116"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W2611340", "tracking_ids": ["403338127473"], "item_ids": ["8426249116"]}),
            Action(name="GetProductDetails", kwargs={"product_id": "8310926033"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0008", "item_id": "6469567736"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5771"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO5771", "status": "expedited"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_086",
        instruction="As a senior retail manager, you need to tackle a challenging customer issue. Raleigh Moore (ZIP: 78234) has received her order, #W4817420, which includes a defective 'Action Camera' (item #6700049080). She has requested a replacement. It is your duty to oversee the entire replacement process. Begin by investigating her order to trace the defective item back to its supplier. Upon discovering the item is out of stock, address the supply concern by locating the associated cancelled supply order (# W4817420 includes a faulty 'Action Camera' (item #6700049080), for which a replacement has been requested. You are responsible for managing the replacement process. Start by reviewing her order to trace the defective item to its supplier. If the item is out of stock, resolve the issue by finding the related cancelled supply order (#SO6998) and reactivating it. To fulfill the customer's request, ship the remaining four items from her original order as a goodwill gesture, using"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W4817420", "tracking_ids": ["757848843226"], "item_ids": ["6777246137", "4900661478", "9624127908", "3812493782"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_087",
        instruction="Act as a logistics manager who is evaluating an order flagged by the system, #W7303089, for customer Mei Campbell (ZIP: 95170). The order was delivered without issues, but verification is required for the tracking data provided by 'SpeedWay Delivery' (#COU0001) and the payment information of the customer. Your objective is to execute a thorough audit by acquiring all customer details, their payment methods, and the specific transaction related to this order. Additionally, review the delivery timeline thoroughly. As a concluding action, since the 'Pet Bed' (item # W7303089, pertaining to customer Mei Campbell (ZIP: 95170). The order has been successfully delivered, but it is necessary to validate the tracking information from 'SpeedWay Delivery' (#COU0001) and the customer's payment details. Your task is to conduct a comprehensive audit by gathering all customer information, payment methods, and the transaction for this order. Furthermore, analyze the delivery timeline in detail. Lastly, as the 'Pet Bed' (item #7381052709)"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Mei", "last_name": "Gonzalez", "zip": "95170"}),
            Action(name="GetUserDetails", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetUserPaymentMethods", kwargs={"user_id": "mei_campbell_4785"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W7303089"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W7303089"}),
            Action(name="GetCourierById", kwargs={"courier_id": "#COU0001"}),
            Action(name="GetProductDetails", kwargs={"product_id": "2747247837"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "2747247837", "item_id": "7381052709", "price": 199.99}),
            Action(name="GetVariantDetails", kwargs={"item_id": "7381052709"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_088",
        instruction="In your role as the inventory and customer relations manager, your responsibility is to oversee the complete cancellation of a pending order, #W5918442, for Sofia Russo (ZIP: 78784). This order includes several products from various suppliers. Your task is to facilitate the cancellation and then coordinate a comprehensive inventory reconciliation for each item by restocking them with their respective suppliers. During this activity, you observe that the 'Action Camera' (item # Order W5918442 for Sofia Russo (ZIP: 78784) contains multiple items from different suppliers. Your responsibility is to process the cancellation and conduct a thorough inventory reconciliation for each product by restocking them with the corresponding suppliers. While performing this task, you notice that the 'Action Camera' (item #1586641416) is incorrectly labeled as 'discontinued' by the supplier. You must correct this inventory entry by updating the stock to 10 units and confirming it stays available for"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6858788497"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0002", "item_id": "1725100896", "value": 18}),
            Action(name="GetProductDetails", kwargs={"product_id": "1968349452"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0005", "item_id": "5312063289", "value": 138}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6117189161", "value": 135})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_089",
        instruction="You are a supply chain analyst tasked with reviewing a supplier, 'Animal Care Worldwide' (#SUP0009), due to the cancellation of a crucial supply order, #SO7642. Your objective is to evaluate the impact and ensure our product catalog remains accurate. Investigate the cancelled supply order to pinpoint the specific product affected and check its current stock level. As this replenishment was cancelled, you need to update the item's public availability in the product catalog to avoid new sales. To finalize your supplier review, also inspect a successfully delivered customer order, # SUP0009) involves assessing the repercussions of the cancelled supply order, #SO7642. Your task is to determine the effects on our product catalog's accuracy. Examine the cancelled order to identify the impacted product and verify its stock status. Since this replenishment is no longer active, update the product's public availability to prevent further sales. Additionally, for the supplier review, analyze a successfully fulfilled customer order, #W8935389, which contains other items from the same supplier, and collect its"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO7642"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7996920482"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "9862136885"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7996920482", "item_id": "9862136885", "available": False}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W8935389"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W8935389"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W8935389"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_090",
        instruction="As a senior customer support agent, your responsibility is to handle an inquiry from Fatima Muller (ZIP: 60644) regarding her overdue order, # W9962383. Your goal is to resolve her issue and correct any data inconsistencies found. Examine her order to determine the cause of the shipping delay. During the review, you find a pricing mistake on the 'Tea Kettle' which is out of stock, requiring an update to $99.99. To address the customer's delay, quickly send the available items from her order using tracking ID 444712814730 via FleetFast Delivery and update the order status to reflect that a partial shipment"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Fatima", "last_name": "Muller", "zip": "60644"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9962383"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1656367028"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "1421289881"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9832717871"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "4238115171"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "9832717871", "item_id": "4238115171", "price": 99.99}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9962383", "tracking_ids": ["444712814730"], "item_ids": ["1421289881"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9962383", "status": "partially_shipped"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_091",
        instruction="As a customer service manager, you need to address a complaint from Fatima Muller (ZIP: 60644) related to her order # W9962383. The order has been in a pending state longer than anticipated. Conduct an investigation to identify the cause of the delay. Focus on identifying the item responsible for the shipping hold by checking stock levels for all products in the order, tracing the missing item back to its supplier, and implementing corrective actions. Since the item is not in stock, update the product catalog to reflect this status to prevent further backorders. Afterward, use tracking ID 403338127473 from SpeedWay Delivery"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Fatima", "last_name": "Muller", "zip": "60644"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9962383"}),
            Action(name="GetProductDetails", kwargs={"product_id": "1656367028"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "1421289881"}),
            Action(name="GetProductDetails", kwargs={"product_id": "9832717871"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0009", "item_id": "4238115171"}),
            Action(name="AddOrderFulfillment", kwargs={"order_id": "#W9962383", "tracking_ids": ["403338127473"], "item_ids": ["1421289881"]}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9962383", "status": "partially_shipped"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "9832717871", "item_id": "4238115171", "available": False})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_092",
        instruction="In your role as an inventory manager, you are performing a standard audit. You've observed that supply order # SO5817 for a 'Cycling Helmet' has been fulfilled with 15 units; however, there might be an inconsistency in the online inventory. You need to examine this issue. Determine the specific item and supplier linked to the supply order, confirm the current stock level, and modify it to show 142 units accurately. During your assessment of the product, you've found that the price is too low, so update it to $199.99 and ensure the item is listed as available for sale"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5817"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "8591113813", "value": 142}),
            Action(name="GetProductDetails", kwargs={"product_id": "7765186836"}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8591113813"}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "7765186836", "item_id": "8591113813", "price": 199.99}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7765186836", "item_id": "8591113813", "available": True}),
            Action(name="GetVariantDetails", kwargs={"item_id": "8591113813"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_093",
        instruction="As a returns manager, handle a return from customer Ella White (ZIP: 75215) concerning her order #W9077205. The returned item is the 'Dumbbell Set' (item # W9077205. The item returned is the 'Dumbbell Set' (item #3877338112). Upon inspection, it is clear that ongoing quality problems from the supplier necessitate the discontinuation of this product line. Please trace the item back to the supplier, mark its stock status as 'discontinued' in their inventory, and remove the product variant from the main catalog. Finally, update the customer's order status to indicate the return has been completed."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Amelia", "last_name": "Wilson", "zip": "75215"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W9077205"}),
            Action(name="GetProductDetails", kwargs={"product_id": "7233192239"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0010", "item_id": "3877338112", "value": "discontinued"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "7233192239", "item_id": "3877338112", "available": False}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W9077205", "status": "completed_return"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_094",
        instruction="As a manager, address a flagged pending order, #W5918442, for Sofia Russo (ZIP: 78784), halted due to a payment failure. Begin by canceling this order. During the post-cancellation review, it appears that an item in her failed order, an 'Action Camera' (item # Order W5918442 for Sofia Russo (ZIP: 78784) has been paused due to a payment issue. First, proceed to cancel the order. Upon reviewing the cancellation, it seems that the 'Action Camera' (item #1586641416) in her failed order is incorrectly marked as 'discontinued' in the supplier's inventory, likely due to an input error. Rectify this by adjusting its stock to 10 units and making it available in the product catalog for customers."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W5918442"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W5918442"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "1586641416", "value": 10}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "1586641416", "available": True})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_095",
        instruction="As an inventory manager, you are tasked with examining a stockout issue concerning the popular 'Action Camera' (item #6700049080), which is impacting customer Raleigh Moore's order (#W4817420). Your objective is to address the root cause of the stock problem. You should track the item from the customer's order back to its supplier to verify the inventory shortage. Upon identifying the stockout, your investigation should uncover the associated, cancelled supply order # 6700049080) is affecting customer Raleigh Moore’s order (#W4817420). Your task is to identify the underlying issue causing the stock shortage. Trace the item from the customer’s order to the supplier to confirm the inventory deficit. Once the stockout is identified, your analysis should reveal the linked, cancelled supply order #SO6998. To resolve the supply chain issue, you must reactivate this supply order and update the product's availability in the main catalog to ensure it can be sold"
        actions=[
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO6998"}),
            Action(name="UpdateSupplyOrderStatus", kwargs={"supply_order_id": "#SO6998", "status": "pending"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "3377618313", "item_id": "6700049080", "available": True}),
            Action(name="GetVariantDetails", kwargs={"item_id": "6700049080"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_096",
        instruction="As a customer service manager, your role is to assist Omar Khan (ZIP: 75203). He is satisfied with his recently delivered order, #W6304490, and wishes to purchase another 'Smart Thermostat' (item #4983901480), but is unable to locate it on the website. Your task is to address this issue. Examine his original order to ascertain the product and its supplier. After confirming that the item is out of stock, review other pending supply orders like # W6304490 wants to buy another 'Smart Thermostat' (item #4983901480) but can't find it online. Your job is to resolve this issue. Check the original order to identify the product and supplier. After confirming the item is out of stock, assess other pending orders, such as #SO9359, for that supplier to check their fulfillment status. Then, manually adjust the inventory by setting the thermostat stock to 50 units, mark it as available for purchase, and"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Omar", "last_name": "Khan", "zip": "75203"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W6304490"}),
            Action(name="GetProductDetails", kwargs={"product_id": "4896585277"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "4983901480"}),
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO9359"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0001", "item_id": "4983901480", "value": 50}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "4896585277", "item_id": "4983901480", "available": True}),
            Action(name="GetVariantDetails", kwargs={"item_id": "4983901480"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_097",
        instruction="As the inventory manager, you are tasked with handling a potential stockout concern. You've received a notification that the supply order #SO3933 for our yellow running shoes was cancelled, and you must mitigate the effect on sales. Please explore the product specifics for these shoes to determine the supplier and evaluate the present stock of a related alternative, the red leather running shoes (item #4153505238), from the same supplier. To prevent unfulfillable orders, adjust the availability of the yellow running shoes (item # The SO3933 for our yellow running shoes has been canceled, necessitating a sales mitigation strategy. Investigate the details of these shoes to identify the supplier and assess the current inventory of a comparable alternative, the red leather running shoes (item #4153505238), from the same supplier. To avoid unfulfillable orders, set the yellow running shoes (item #9791469541) to unavailable. To regulate demand for the remaining stock, raise the price of the red leather variant to $"
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO3933"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6938111410"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "9791469541"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0006", "item_id": "4153505238"}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6938111410", "item_id": "9791469541", "available": False}),
            Action(name="UpdateVariantPrice", kwargs={"product_id": "6938111410", "item_id": "4153505238", "price": 162.99})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_098",
        instruction="As an inventory manager performing a stock audit, you've observed that supply order # SO5722 for a 'Wristwatch' is marked as 'fulfilled', but the inventory count seems inaccurate. Your task is to address this issue. Start by checking the supply order details to verify the received quantity. Next, use the product information to find the correct supplier. Confirm the current stock recorded for this item with the supplier. After identifying the discrepancy, adjust the supplier's stock to the correct total of 153 units. Finally, ensure the product variant is listed as available for customers."
        actions=[
            Action(name="GetSupplyOrderDetails", kwargs={"supply_order_id": "#SO5722"}),
            Action(name="GetProductDetails", kwargs={"product_id": "6066914160"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "9949163720"}),
            Action(name="UpdateItemStock", kwargs={"supplier_id": "#SUP0007", "item_id": "9949163720", "value": 153}),
            Action(name="UpdateVariantAvailability", kwargs={"product_id": "6066914160", "item_id": "9949163720", "available": True})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_099",
        instruction="As a customer service manager, your responsibility is to address a complaint from Raleigh Moore (ZIP: 78234) regarding the delivered order, # W4817420. The user claims that the 'Action Camera' (item_id: 6700049080) is defective. Your task is to conduct a thorough investigation. Start by confirming her user and order information. Then, gather product details to identify the supplier. Check the original courier and tracking information for the delivery. After that, assess the current stock of the Action Camera with the identified supplier to see if a replacement is possible. Based on your findings, update the order status to '"
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Ava", "last_name": "Moore", "zip": "78234"}),
            Action(name="GetOrderDetails", kwargs={"order_id": "#W4817420"}),
            Action(name="GetTrackingHistory", kwargs={"order_id": "#W4817420"}),
            Action(name="GetProductDetails", kwargs={"product_id": "3377618313"}),
            Action(name="GetItemStock", kwargs={"supplier_id": "#SUP0011", "item_id": "6700049080"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W4817420", "status": "pending_return"})
        ],
        outputs=[]
    ),
    Task(
        annotator="0",
        user_id="USER_100",
        instruction="As a retail manager, you need to resolve a payment problem for customer Sofia Russo (first_name: Sofia, last_name: Rossi, user: sofia_russo_8329, sofia_russo_8776) from ZIP code 78784. Her most recent order, # W5918442 is in 'pending' status (status: cancelled) because of a reported payment problem. Your responsibilities include reviewing the order's payment history to identify the issue, canceling the order in the system due to the failed payment, and ensuring the order status is correctly updated to 'cancelled'."
        actions=[
            Action(name="FindUserIdByNameZip", kwargs={"first_name": "Sofia", "last_name": "Rossi", "zip": "78784"}),
            Action(name="GetOrderPaymentHistory", kwargs={"order_id": "#W5918442"}),
            Action(name="UpdateOrderStatus", kwargs={"order_id": "#W5918442", "status": "cancelled"}),
            Action(name="GetOrderStatus", kwargs={"order_id": "#W5918442"})
        ],
        outputs=[]
    ),
]