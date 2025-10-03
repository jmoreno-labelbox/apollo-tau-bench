from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="1",
        user_id="user_119",
        instruction=(
            "The task is to oversee a multi-stage supply chain process and incorporate its outcomes into a customer order. Begin by handling the pending supply order '#SO9359' from supplier '#SUP0001'. Transition it to 'approved', then 'in_transit', and ultimately handle its receipt and closing, while recording an 'info' event with the note 'Shipment received and verified' upon approval. Following the confirmation of 'T-Shirt' stock, coordinate two consecutive price alterations for the variant (product '9523456873', item '9612497925'): initially raise the price to $55.00, followed by a promotional reduction to $49.99. Conclude by updating the pending order '#W7007896' for customer 'Ahmad Ahmed' (user_id 'ahmad_ahmed_6232') by substituting the item at index 0 with this newly repriced T-Shirt and nullifying the payment at index 0."
        ),
        actions=[
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0001", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Shipment received and verified",
                },
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "in_transit"},
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO9359"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 49.99},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W7007896",
                    "index": 0,
                    "product_id": "9523456873",
                    "item_id": "9612497925",
                },
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W7007896", "index": 0},
            ),
        ],
        outputs=[
            [{"supply_order_id": "#SO9359"}],
            {"supply_order_id": "#SO9359", "status": "approved"},
            {"supply_order_id": "#SO9359", "events_len": 1},
            {"supply_order_id": "#SO9359", "status": "in_transit"},
            {"supply_order_id": "#SO9359", "status": "closed"},
            {"product_id": "9523456873", "item_id": "9612497925", "old_price": 55.00, "new_price": 55.00},
            {"product_id": "9523456873", "item_id": "9612497925", "old_price": 55.00, "new_price": 49.99},
            {"status": "success", "message": "Order #W7007896 was successfully modified in memory."},
            {"order_id": "#W7007896", "removed": True, "payment_history_len": 1},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_106",
        instruction=(
            "The task is to handle a complex account update for customers 'Sofia Hernandez' (user_id 'sofia_hernandez_5364') and 'Mia Martinez' (user_id 'mia_martinez_3271'). For Sofia Hernandez, coordinate an update on her 'processed' order '#W9609649'. Void the payment at index 0, insert one 'Patio Umbrella' (product '9743693396', item '8170914468'), execute a fresh 'payment' of $750.00 with 'pm-sofia-card-3', and change its final status to 'delivered'. For Mia Martinez, focus on reactivating her 'cancelled' order '#W4140680' and arranging it for an integrated shipment. Reopen the order, then attach the existing tracking ID from her 'processed' order '#W6310710' to it. Ultimately, record an 'info' event with the remark 'Order consolidated for shipment' on the shared tracking document and adjust the reopened order's status to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "sofia_hernandez_5364", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W9609649", "index": 0}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W9609649",
                    "transaction_type": "payment",
                    "amount": 750.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W9609649", "status": "delivered"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="FindTrackingByOrder",
                kwargs={"order_id": "#W6310710"},
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W4140680", "tracking_id": "951786982868"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Order consolidated for shipment",
                },
            ),
             Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            [{"order_id": "#W9609649"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W6310710"}],
            {"order_id": "#W9609649", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9609649", "added_count": 1, "items_len": 6},
            {"order_id": "#W9609649", "payment_history_len": 1},
            {"order_id": "#W9609649", "status": "delivered"},
            {"order_id": "#W4140680", "status": "pending"},
            {"tracking_id": ["951786982868"], "order_id": "#W6310710"},
            {"order_id": "#W4140680", "tracking_id": "951786982868", "fulfillments_len": 2},
            {"tracking_id": "951786982868", "new_status": "info"},
            {"order_id": "#W4140680", "status": "processed"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_107",
        instruction=(
            "Handle an entire product lifecycle, from supply chain management to pricing and final sale execution. Initially, you need to oversee the restocking of 'T-Shirt' inventory by managing supply order '#SO7848' with supplier '#SUP0002': ensure you approve it, log an 'info' event 'Stock replenished for campaign', and process its receipt. Next, aim for a company-wide price revision: adjust the 'T-Shirt' (product '9523456873', item '9612497925') to 49.99 USD and the 'Portable Charger' (product '6942297802', item '7903094618') to 89.99 USD. Conclude by applying these modifications to a customer order. For 'Mei Kovacs' (user_id 'mei_kovacs_5767') on her pending order '#W8193638', initially apply a service 'payment' of 15.00 USD utilizing method 'pm_mei_kovacs_card_1'. Following this, substitute the original item at index 0 with the newly updated 'T-Shirt' and 'Portable Charger'. To finalize the fulfillment, associate tracking ID '951786982868', input an 'info' event with note 'Order updated with new products and pricing', and update the order status to 'processed'."
        ),
        actions=[
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO7848", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO7848",
                    "event_type": "info",
                    "message": "Stock replenished for campaign",
                },
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO7848"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 49.99},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "6942297802", "item_id": "7903094618", "new_price": 89.99},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W8193638",
                    "transaction_type": "payment",
                    "amount": 15.00,
                    "payment_method_id": "pm_mei_kovacs_card_1",
                },
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W8193638", "indices": [0]},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [
                        {"product_id": "9523456873", "item_id": "9612497925", "quantity": 1},
                        {"product_id": "6942297802", "item_id": "7903094618", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W8193638", "tracking_id": "951786982868"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Order updated with new products and pricing",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W8193638", "status": "processed"},
            ),
        ],
        outputs=[
            [{"supply_order_id": "#SO6035"}, {"supply_order_id": "#SO7848"}],
            {"supply_order_id": "#SO7848", "status": "approved"},
            {"supply_order_id": "#SO7848", "events_len": 1},
            {"supply_order_id": "#SO7848", "status": "closed"},
            {"product_id": "9523456873", "item_id": "9612497925", "old_price": 50.88, "new_price": 49.99},
            {"product_id": "6942297802", "item_id": "7903094618", "old_price": 90.32, "new_price": 89.99},
            {"order_id": "#W8193638", "payment_history_len": 2},
            {"order_id": "#W8193638", "removed_count": 1, "items_len": 0},
            {"order_id": "#W8193638", "added_count": 2, "items_len": 2},
            {"order_id": "#W8193638", "tracking_id": "951786982868", "fulfillments_len": 1},
            {"tracking_id": "951786982868", "new_status": "info"},
            {"order_id": "#W8193638", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_101",
        instruction=(
            "Coordinate the downstream consequences of a customer return. Initiate by handling a return for 'Aarav Lopez' (user_id 'aarav_lopez_9729') on his delivered order '#W5455653' by canceling it and providing a full 'refund' of $1221.52 to payment method 'credit_card_2690859'. This return impacts inventory levels, necessitating supply chain management. Locate the pending supply order '#SO6035' for the returned item's supplier ('#SUP0002') and approve it with an 'info' event note 'Approved to restock after customer return'. Once the supply order receipt is processed, apply a price update to the restocked 'Gaming Mouse' (product '5713490933', item '8214883393'), setting its new price to $82.50. Finally, reconcile finances on a different customer's ('Olivia Rodriguez', user_id 'olivia_rodriguez_9753') delivered order '#W3113816', affected by the price adjustment, by voiding the payment at index 0 and applying a new 'payment' of $1450.00 using method 'credit_card_5869505'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "aarav_lopez_9729", "status": "delivered"},
            ),
            Action(
                name="CancelOrderAndRefund",
                kwargs={
                    "order_id": "#W5455653",
                    "refund_amount": 1221.52,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Approved to restock after customer return",
                },
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 82.50},
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W3113816"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W3113816",
                    "transaction_type": "payment",
                    "amount": 1450.00,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
        ],
        outputs=[
            [{"order_id": "#W5455653"}],
            {"order_id": "#W5455653", "status": "cancelled", "refund_created": True},
            [{"supply_order_id": "#SO6035"}, {"supply_order_id": "#SO7848"}],
            {"supply_order_id": "#SO6035", "status": "approved"},
            {"supply_order_id": "#SO6035", "events_len": 1},
            {"supply_order_id": "#SO6035", "status": "closed"},
            {"product_id": "5713490933", "item_id": "8214883393", "old_price": 150.58, "new_price": 82.50},
            {"order_id": "#W3113816", "items_total": 0},
            {"order_id": "#W3113816", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3113816", "payment_history_len": 1},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_103",
        instruction=(
            "The goal is to handle a complete account archival for 'William Li' (user_id 'william_li_5688') and address the downstream consequences. The archival policy dictates that all of his 'processed' orders ('#W2611340', '#W3632959') must be cleared by eliminating all items and the primary payment at index 0, then changing their status to 'cancelled'. As this archival process reinstates a 'Smartphone' to stock, you are required to cancel the now-unnecessary pending supply order '#SO9359' for that item and log an 'info' event with the message 'Cancelled: stock returned from customer order #W2611340'. Lastly, you need to cancel a separate pending order '#W9609649' for 'Sofia Hernandez'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W2611340", "indices": [0, 1]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "cancelled"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W3632959", "indices": [0]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3632959", "status": "cancelled"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "cancelled"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Cancelled: stock returned from customer order #W2611340",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9609649", "status": "cancelled"},
            ),
        ],
        outputs=[
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            {"order_id": "#W2611340", "removed_count": 2, "items_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "cancelled"},
            {"order_id": "#W3632959", "removed_count": 1, "items_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "cancelled"},
            {"supply_order_id": "#SO9359", "status": "cancelled"},
            {"supply_order_id": "#SO9359", "events_len": 1},
            {"order_id": "#W9609649", "status": "cancelled"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_001",
        instruction=(
            "The task at hand is to get William Li's account ready for a new audit. You are required to reset both of his orders, '#W2611340' and '#W3632959', by removing their initial payment data and placing them in a 'pending' state for a review."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Both of William Li's orders, #W2611340 and #W3632959, had their initial payments removed and their statuses set to pending as part of the audit preparation."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_002",
        instruction=(
            "Handle a comprehensive account audit for customers 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Your responsibility is to enforce the audit policy on all their orders. Initially, you're required to execute a financial reset by voiding the primary payment at index 0 from every order linked to both users. Any order that is 'cancelled' needs to be reactivated before voiding the payment. After completing the financial reset, you must update the order statuses: all orders of Mia Martinez ('#W6310710', '#W6436609', '#W4140680') must be set to 'processed', whereas William Li's order '#W2611340' should be set to 'pending'. No other status alterations are necessary for William Li's remaining orders."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "cancelled"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W6436609"}],
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "removed": True, "payment_history_len": 2},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6436609", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "processed"},
            {"order_id": "#W6436609", "status": "processed"},
            {"order_id": "#W4140680", "status": "processed"},
            {"order_id": "#W2611340", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_003",
        instruction=(
            "Coordinate a precise account cleanup. For Mia Martinez, ensure order '#W4140680' is fully activated with a 'processed' status, and at the same time, carry out a financial reset on order '#W6310710' by deleting its payment record at index 0. With respect to William Li, transition order '#W3632959' to a 'pending' status for additional review."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
            {"order_id": "#W6310710", "payment_removed_index": 0},
            {"order_id": "#W3632959", "status": "pending"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_004",
        instruction=(
            "You are tasked with handling a high-level status reconciliation. For William Li, your task is to ready his account for audit: change order '#W3632959' to a 'pending' status and remove the payment information at index 0 from order '#W2611340'. Concerning Mia Martinez, your aim is to address the status of her inactive order '#W4140680' by reopening it and labeling it as 'processed'."
        ),
        actions=[
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W2611340", "payment_removed_index": 0},
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_005",
        instruction=(
            "Your responsibility is to coordinate a system-wide audit for a new fiscal period for customers Mia Martinez and William Li. The audit policy requires that all active orders ('#W6310710', '#W2611340', '#W3632959') be financially reset and transitioned to a reviewable 'pending' state. Separately, Mia Martinez's inactive order '#W4140680' should be completely reactivated and completed as 'processed'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "All active orders (#W6310710, #W2611340, #W3632959) had their initial payments removed and were set to pending. The inactive order #W4140680 was reopened and set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_006",
        instruction=(
            "The final initiative for this quarter involves managing a complete account closure and resetting process for clients Mia Martinez and William Li. Focus on their current active orders ('#W6310710', '#W2611340', '#W3632959') by eliminating the initial payment information and updating their status to 'pending' in readiness for the new fiscal term. In contrast, fully reactivate Mia Martinez's cancelled order '#W4140680' and make sure it remains in a 'processed' state."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "A full audit was completed. All active orders had payments removed and were set to pending. Order #W4140680 was reopened and set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_007",
        instruction=(
            "You need to conclude the monthly order documentation for our key clients, William Li and Mia Martinez, by coordinating various status changes and financial revisions. For William Li, ensure his orders are ready for archival: manage order '#W2611340' by deleting its initial payment and switching its status to 'pending'. Additionally, adjust order '#W3632959' by eliminating its payment. For Mia Martinez, resolve her account's only inactive order, '#W4140680', by restoring it online and confirming it remains in a 'processed' status."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "For William Li, order #W2611340 had its payment removed and was set to pending, while order #W3632959 also had its payment removed. For Mia Martinez, order #W4140680 was reopened and set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_008",
        instruction=(
            "Handle a system-wide payment reconciliation. Your task is to coordinate a financial reset on all active orders ('#W6310710', '#W2611340', '#W3632959') by eliminating the initial payment in each order (index 0). After this reset, the account policy mandates that order '#W6310710' should transition to a 'pending' state. Additionally, address the status of Mia Martinez's inactive order '#W4140680' by reopening it and changing its state to 'processed'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
        ],
        outputs=[
            {"order_id": "#W6310710", "payments_removed": [0], "new_status": "pending"},
            {"order_id": "#W2611340", "payments_removed": [0]},
            {"order_id": "#W3632959", "payments_removed": [0]},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_009",
        instruction=(
            "Oversee a pre-audit cleanup for customers Mia Martinez and William Li. The audit policy stipulates that their active orders ('#W2611340' and '#W6310710') should undergo a financial reset and be placed in a 'pending' state for review. For Mia Martinez's dormant order '#W4140680', your aim is distinct: it must be entirely restored to a 'processed' state."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "A pre-audit cleanup was completed. Active orders #W2611340 and #W6310710 had their payments removed and were set to pending. Inactive order #W4140680 was reopened and set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_010",
        instruction=(
            "The last assignment involves quarterly account reconciliation for our main clients. For Mia Martinez, completely reactivate her cancelled order '#W4140680' and make sure it reaches a 'processed' status. Additionally, prepare her active order '#W6310710' for audit by eliminating its payment record at index 0 and transitioning it to 'pending'. For William Li, aim to conclude his active order '#W2611340' for the quarter by executing a financial reset, which involves removing its payment record at index 0 and updating its status to 'processed'."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
            {"order_id": "#W6310710", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_011",
        instruction=(
            "Initiate the preparation of all customer orders for a system-wide data migration. According to the migration policy, it is necessary to financially cleanse and then reset the status of all active orders. Specifically, for standard active orders ('#W6310710', '#W2611340'), remove their payment record at index 0 and change their status to 'pending'. For order '#W3632959', ensure its payment record at index 0 is removed and that it's fully archived with a 'cancelled' status. Additionally, handle the specific case of Mia Martinez's inactive order '#W4140680' by reactivating and finalizing it as 'processed' for the migration."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "cancelled"}
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W3632959", "payment_removed_index": 0, "status": "cancelled"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_012",
        instruction=(
            "As an operations assistant, your task is to conduct a complete financial reconciliation for important clients. The goal is to reset the financial records of all current orders for William Li ('#W2611340', '#W3632959') and Mia Martinez ('#W6310710') by erasing their initial payment information. After executing the financial reset, ensure that both of William Li's orders are changed to a 'pending' status."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "A full financial reconciliation was completed. The initial payments for orders #W2611340, #W3632959, and #W6310710 were removed. Both of William Li's orders were then set to a 'pending' status."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_013",
        instruction=(
            "Undertake an essential account cleanup for William Li and Mia Martinez. For William Li, your responsibility is to reset his two orders, '#W2611340' and '#W3632959', by eliminating their initial payment records and then changing their statuses to 'processed'. For Mia Martinez, you should reactivate her cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[
            "Critical account cleanup completed. William Li's orders #W2611340 and #W3632959 had their payments removed and were set to processed. Mia Martinez's order #W4140680 was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_014",
        instruction=(
            "Your responsibility is to address two urgent customer requests. For customer Mia Martinez, reactivate her cancelled order '#W4140680' and make sure its status is 'processed'. For William Li, you will need to get his orders '#W2611340' and '#W3632959' ready for a new audit by eliminating the initial payment from both orders and setting their status back to 'pending'."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Mia Martinez's order #W4140680 was reopened and processed. William Li's orders #W2611340 and #W3632959 were prepared for audit by removing payments and setting their statuses to pending."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_015",
        instruction=(
            "Your assignment is to perform a complete account cleanup for William Li and Mia Martinez. The task for William Li involves resetting his orders '#W2611340' and '#W3632959' by removing their payment record at index 0 and changing their status to 'processed'. For Mia Martinez, you are required to resolve a billing issue on her active order '#W6310710' by eliminating its payment record at index 0 and also reactivating her cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "processed"},
            {"order_id": "#W3632959", "payment_removed_index": 0, "status": "processed"},
            {"order_id": "#W6310710", "payment_removed_index": 0},
            {"order_id": "#W4140680", "reopened": True},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_016",
        instruction=(
            "Handle the task of preparing customer accounts for an upcoming audit. For Mia Martinez, your objective is to reactivate her cancelled order '#W4140680' and ensure it reaches a 'processed' state, while simultaneously adding a new standard item (product '1801728040', variant '5339029584') to it. In the case of William Li, your task is to reset his orders '#W2611340' and '#W3632959' financially by removing the initial payment records and subsequently placing them in a 'pending' state for review."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Mia Martinez's order #W4140680 was reopened, processed, and had a new item added. William Li's orders #W2611340 and #W3632959 were prepared for audit by removing payments and setting their statuses to pending."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_017",
        instruction=(
            "Coordinate the preparation of all orders for the launch of a new sales campaign. The preparation protocol necessitates a financial reset and status alignment. For each active order linked to Mia Martinez ('#W6310710') and William Li ('#W2611340', '#W3632959'), you need to remove the initial payment record (index 0) and then change their status to 'processed'. Also, attend to Mia Martinez's dormant order '#W4140680', which requires reactivation and should be marked as 'processed'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "status": "processed", "payments_cleared": True},
            {"order_id": "#W2611340", "status": "processed", "payments_cleared": True},
            {"order_id": "#W3632959", "status": "processed", "payments_cleared": True},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed", "reopened": True},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_018",
        instruction=(
            "You are handling a data integrity and segmentation task. Your goal is to audit and reset all orders for our primary customers. The audit policy requires a financial reset of all active orders ('#W6310710', '#W2611340', '#W3632959') by eliminating the payment record at index 0 from each. Following the reset, you need to categorize them by status: high-priority orders '#W2611340' and '#W3632959' should be transferred to 'processed', while order '#W6310710' should be labeled as 'pending' for review. As always, Mia Martinez's inactive order '#W4140680' must be reactivated and completed in a 'processed' state."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "processed"},
            {"order_id": "#W3632959", "payment_removed_index": 0, "status": "processed"},
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_019",
        instruction=(
            "Your task is to coordinate a major account consolidation. You need to handle every order for Mia Martinez and William Li. The consolidation rule mandates that all payment records be removed from their active orders ('#W6310710', '#W2611340', '#W3632959') by eliminating the payment record at index 0 from each. After this, you are to harmonize the status of all these active orders to 'pending'. Your final action is to ensure Mia Martinez's cancelled order '#W4140680' is restored to an active, 'processed' state."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W3632959", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W4140680", "reopened": True, "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_020",
        instruction=(
            "Handle the final cleanup for the quarter. Aim to standardize all customer orders. It is necessary to clear the payment record from every active order for Mia Martinez ('#W6310710') and William Li ('#W2611340', '#W3632959'). Following the cleanup policy, update the status for all of William Li's orders to 'processed', and set Mia Martinez's active order to 'pending'. Additionally, ensure her inactive order '#W4140680' is reopened and retained as 'processed'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "Quarterly cleanup finished. All active orders were financially reset. William Li's orders were set to processed, and Mia Martinez's active order was set to pending. Her inactive order was reopened and processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_021",
        instruction=(
            "Coordinate a multi-part audit for customers 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). For Anya, your objectives are twofold: first, reopen her cancelled order '#W4140680' and add two units of the standard Smartphone (product '1801728040', item '5339029584'). Second, handle her processed order '#W6310710' by voiding its payment at index 0. For William Li, the audit policy mandates processing all of his 'processed' and 'delivered' orders. For each of these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), replace the item at index 0 with the standard Smartphone and void the payment at index 0. After completing the audit, set the status of all four of his orders to 'pending' for review."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 2}],
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W4435622",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
             Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3638028",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 2, "items_len": 5},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"status": "success", "message": "Order #W2611340 was successfully modified in memory."},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"status": "success", "message": "Order #W3632959 was successfully modified in memory."},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"status": "success", "message": "Order #W4435622 was successfully modified in memory."},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"status": "success", "message": "Order #W3638028 was successfully modified in memory."},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_022",
        instruction=(
            "Handle a full audit and reset the status for all orders linked to customers Mia Martinez and William Li. Your goal is to reactivate Mia Martinez's inactive order '#W4140680' and update it to 'processed'. For all other active orders ('#W6310710', '#W2611340', '#W3632959'), the audit policy dictates that you erase their initial payment records and then adjust their statuses: orders '#W6310710' and '#W3632959' should be changed to a 'pending' state, while order '#W2611340' needs to be marked as 'processed'."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "A full audit and status reset was completed. Inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) had their payments cleared and statuses updated according to the audit policy."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_023",
        instruction=(
            "Coordinate an account audit for William Li (user_id 'william_li_5688') and Mia Martinez (user_id 'mia_martinez_3271'). For William Li, the audit policy states you should process all of his 'processed' and 'delivered' orders. For each named order ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), you are required to erase the financial record at index 0 and then update the order's status to 'pending'. For Mia Martinez, the policy dictates you should reactivate her 'cancelled' order '#W4140680' and confirm it is updated to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            [{"order_id": "#W4140680"}],
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_024",
        instruction=(
            "Handle a system-wide reconciliation. According to company policy, you are required to coordinate a financial reset on all active orders for William Li ('#W2611340', '#W3632959') and Mia Martinez ('#W6310710') by removing their primary payment records. After that, reactivate Mia Martinez's dormant order '#W4140680' and subsequently mark its status as 'processed'."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "A system-wide reconciliation was performed. The payment records for all active orders (#W2611340, #W3632959, #W6310710) were cleared. Mia Martinez's dormant order #W4140680 was reactivated and processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_025",
        instruction=(
            "Coordinate a complete financial reset for the new quarter. Your main goal is to eliminate the payment records at index 0 from all active orders (#W6310710, #W2611340, #W3632959) for customers Mia Martinez and William Li, then transition each of these orders into a 'pending' state for re-evaluation. Finally, you need to reactivate Mia Martinez's dormant order #W4140680."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "pending"},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_026",
        instruction=(
            "Your responsibility is a comprehensive account cleanup and order enhancement initiative for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). For Mia Martinez, you need to ready her active order '#W6310710' for archival by removing its financial and item data and setting it to a 'pending' status. Additionally, you must reactivate her inactive order '#W4140680' and initiate a new payment for it of 75.00 USD using 'pm-anya-card-6'. For William Li, your goal is to upgrade his active order '#W2611340' by substituting its first item with the standard Smartphone variant (product '1801728040', item_id '5339029584'), adding an additional unit of the same, introducing a new payment of 300.00 USD via 'pm-james-card-5', and completing the order as 'processed'."
        ),
        actions=[
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W6310710", "indices": [0]},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [
                        {"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}
                    ],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 300.00,
                    "payment_method_id": "pm-james-card-5",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "processed"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-6",
                },
            ),
        ],
        outputs=[
            "For Mia Martinez, order #W6310710 was prepared for archival and order #W4140680 was reactivated with a new payment. "
            "For William Li, order #W2611340 was enhanced with item and payment updates and then processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_027",
        instruction=(
            "Coordinate the end-of-quarter account assessment for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Complying with the review guidelines, you need to clear all active orders (#W6310710, #W2611340, #W3632959) by deleting their primary payment records. Following the clearance, revise their statuses as outlined in the EOD strategy: designate orders #W6310710 and #W3632959 as 'pending', and for order #W2611340, designate it as 'processed' before concluding it as 'pending'. Additionally, address the status of Mia Martinez's dormant order #W4140680 by reactivating it and confirming it stays in a 'processed' state."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_028",
        instruction=(
            "You are required to handle a comprehensive financial reset for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). According to company policy, clear the primary payment record from all their orders in a 'pending', 'processed', or 'delivered' state. For orders that are inactive (i.e., 'cancelled'), reactivate them first so they become eligible for this financial reset policy. Once all financial records are cleared, coordinate the finalization of statuses: place all of William Li's orders in 'pending', while Mia Martinez's former inactive order should be updated to 'processed'."
        ),
        actions=[
            Action(name="FindOrdersByUserAndStatus", kwargs={"user_id": "mia_martinez_3271"}),
            Action(name="FindOrdersByUserAndStatus", kwargs={"user_id": "william_li_5688"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            "A system-wide financial reset was performed. All active and reactivated orders for both customers had their primary payment records cleared. The final statuses were set according to policy: William Li's orders were set to pending, and Mia Martinez's reactivated order was set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_029",
        instruction=(
            "Handle the end-of-quarter account review for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Per the review policy, reset the financial status of all active orders ('#W6310710', '#W2611340', '#W3632959') by eliminating their primary payment records. Following the reset, update their statuses as stipulated in the EOD plan: mark '#W6310710' and '#W3632959' as 'pending', while '#W2611340' should be first marked 'processed' before being finalized as 'pending'. Lastly, address the status of Mia Martinez's inactive order '#W4140680' by reactivating it, ensuring it is left in a 'processed' state."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[
            "End-of-quarter review is complete. Mia Martinez's inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) were financially reset and their statuses updated according to the EOD plan."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_030",
        instruction=(
            "You need to handle a full audit and reset the status for all orders linked to customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). The audit policy stipulates that you clear the initial payment records from all active orders ('#W6310710', '#W2611340', '#W3632959'). After that, update their statuses: orders '#W6310710' and '#W3632959' should be updated to a 'pending' state, whereas order '#W2611340' must be classified as 'processed'. Additionally, reactivate Mia Martinez's inactive order '#W4140680' and set its status to 'processed'."
        ),
        actions=[
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Full audit and status reset is complete. Inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) had their payments cleared and statuses updated according to the audit policy."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_031",
        instruction=(
            "You are required to implement the new financial year-end policy for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). This policy calls for a financial reset on all orders currently in 'pending', 'processed', or 'delivered' status. For the reset, you must remove the primary payment record (index 0) from each of the following orders: #W6310710, #W6436609, #W2611340, #W3632959, #W4435622, and #W3638028. Following the reset, ensure orders '#W6310710', '#W6436609', and '#W2611340' are set to a 'pending' state for a final review, while making sure order '#W3632959' is designated as 'processed'. Do not alter any other orders."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W6436609", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W2611340", "payment_removed_index": 0, "status": "pending"},
            {"order_id": "#W3632959", "payment_removed_index": 0, "status": "processed"},
            {"order_id": "#W4435622", "payment_removed_index": 0},
            {"order_id": "#W3638028", "payment_removed_index": 0},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_032",
        instruction=(
            "Handle a comprehensive data integrity check across the system for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). The audit policy mandates coordinating a complete financial reset on every order labeled as 'pending', 'processed', or 'delivered' by clearing its primary payment record. Upon completing this financial reset, adjust the status of all orders under William Li to 'processed' and ensure all applicable orders for Mia Martinez are set to 'pending'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_033",
        instruction=(
            "Carry out a directive for updating prices and a related account examination for customers 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Initially, apply the company's price change requirement: update the cost for the standard Smartphone variant (product_id '1801728040', item_id '5339029584') to 105.50 USD. After implementing the price update, conduct an audit. Locate all orders placed by William Li with the status 'pending', 'processed', or 'delivered'. For each of these orders, clear the primary payment record (index 0), then reassign them to a 'pending' status. In the case of Mia Martinez, locate her cancelled order, reactivate it, and finalize its status as 'processed'."
        ),
        actions=[
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 105.50},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            {"product_id": "1801728040", "item_id": "5339029584", "new_price": 105.50},
            [{"order_id": "#W2611340", "status": "pending"}],
            [{"order_id": "#W3632959", "status": "processed"}, {"order_id": "#W2611340", "status": "processed"}],
            [{"order_id": "#W4435622", "status": "delivered"}, {"order_id": "#W3638028", "status": "delivered"}],
            [{"order_id": "#W4140680", "status": "cancelled"}],
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_034",
        instruction=(
            "Coordinate a thorough update of all four customer orders. For customer Mia Martinez (user_id 'mia_martinez_3271'), ensure the main item in her active order '#W6310710' is revised to the standard Smartphone variant (product '1801728040', item_id '5339029584') and clear its payment record. Her cancelled order '#W4140680' needs reactivation. For customer William Li (user_id 'william_li_5688'), you should update the primary items in both of his active orders ('#W2611340', '#W3632959') to the standard variant and clear their payment records. After completing these updates, make sure to set the status of all three active orders ('#W6310710', '#W2611340', '#W3632959') to 'pending'."
        ),
        actions=[
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "All four orders were overhauled. All three active orders had their primary item replaced and payment record cleared before being set to 'pending'. The cancelled order was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_035",
        instruction=(
            "Coordinate a thorough update of all four customer orders. For customer Mia Martinez (user_id 'mia_martinez_3271'), ensure the main item in her active order '#W6310710' is revised to the standard Smartphone variant (product '1801728040', item_id '5339029584') and clear its payment record. Her cancelled order '#W4140680' needs reactivation. For customer William Li (user_id 'william_li_5688'), you should update the primary items in both of his active orders ('#W2611340', '#W3632959') to the standard variant and clear their payment records. After completing these updates, make sure to set the status of all three active orders ('#W6310710', '#W2611340', '#W3632959') to 'pending'."
        ),
        actions=[
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "All four orders were overhauled. All three active orders had their primary item replaced and payment record cleared before being set to 'pending'. The cancelled order was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_036",
        instruction=(
            "Handle a system-wide data standardization project for Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). According to company policy, for any order that is currently in a 'processed' status for these customers, ensure that its primary item is standardized to the Smartphone variant (product '1801728040', item_id '5339029584') and remove its initial payment record."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
        ],
        outputs=[
            "System-wide data standardization is complete. For all 'processed' orders belonging to the specified customers, the primary item was updated to the standard variant and the initial payment record was cleared."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_037",
        instruction=(
            "Coordinate a large-scale order enhancement project for Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). This project requires the addition of a new standard Smartphone item (product '1801728040', item_id '5339029584') in a quantity of 1 to all of their active orders ('#W6310710', '#W2611340', '#W3632959'). Simultaneously, initiate a new payment of 100.00 USD for each of these three orders, using payment methods 'pm-anya-card-1', 'pm-james-card-1', and 'pm-james-card-2' respectively. Lastly, reactivate Anya's dormant order '#W4140680' and include a standard Smartphone in it."
        ),
        actions=[
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-james-card-1",
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W3632959",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-james-card-2",
                },
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "added_count": 1, "items_len": 2},
            {"order_id": "#W6310710", "payment_history_len": 2},
            {"order_id": "#W2611340", "added_count": 1, "items_len": 3},
            {"order_id": "#W2611340", "payment_history_len": 2},
            {"order_id": "#W3632959", "added_count": 1, "items_len": 2},
            {"order_id": "#W3632959", "payment_history_len": 2},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_038",
        instruction=(
            "Your task is to handle an archival preparation for the active orders belonging to customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). According to the archival policy, you need to clear all items and the main payment at index 0 from each designated active order. For order '#W6310710', take out one item (index 0). For order '#W2611340', eliminate two items (indices 0, 1). For order '#W3632959', remove one item (index 0). After completing the clearances, ensure all three orders are marked as 'pending'. Finally, reactivate Mia Martinez's cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="RemoveItemsByIndex", kwargs={"order_id": "#W6310710", "indices": [0]}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(
                name="RemoveItemsByIndex", kwargs={"order_id": "#W2611340", "indices": [0, 1]}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemoveItemsByIndex", kwargs={"order_id": "#W3632959", "indices": [0]}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[
            {"order_id": "#W6310710", "removed_count": 1, "items_len": 0},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "pending"},
            {"order_id": "#W2611340", "removed_count": 2, "items_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed_count": 1, "items_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_039",
        instruction=(
            "You are tasked with coordinating a customer retention initiative for Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Include a complimentary standard Smartphone (product_id '1801728040', item_id '5339029584', quantity 1) in each of their orders holding a 'processed' or 'pending' status. For all applicable orders of William Li, delete the payment record at index 0 as a sign of goodwill. In each of Mia Martinez's 'processed' orders, add a service payment of exactly 10.00 USD using payment_method_id 'pm-anya-card-1'. If any of Mia Martinez's orders have a 'cancelled' status, reopen them, include the complimentary smartphone, and adjust them to 'processed'. Employ exactly the specified user_ids, product_ids, item_ids, order_ids, statuses, and index values as they are."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W6436609",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 10.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_040",
        instruction=(
            "Handle a system-wide price update and corresponding financial audit for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Implement the mandated price change for the standard Smartphone variant (product_id '1801728040', item_id '5339029584'), and adjust its price to 115.00 USD. For orders '#W2611340' and '#W6310710', delete the payment record at index 0 and update their statuses to 'processed'. For order '#W3632959', eliminate the payment record at index 0. Finally, reinstate Mia Martinez's cancelled order '#W4140680'. Utilize exactly the provided order_ids, product_ids, item_ids, statuses, and index values without alteration."
        ),
        actions=[
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 115.00},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_041",
        instruction=(
            "Coordinate a system-wide data standardization project for customers 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Begin by applying a data policy to all of their 'processed' orders. For each order ('#W6310710', '#W2611340', '#W3632959'), update the item at index 0 to the standard Smartphone variant (product '1801728040', item '5339029584'). Next, conduct an audit by removing the payment record at index 0 from all three of these processed orders. As a concluding administrative task, you must reactivate Mia Martinez's 'cancelled' order '#W4140680' and ensure its status is finalized as 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            {"status": "success", "message": "Order #W6310710 was successfully modified in memory."},
            {"status": "success", "message": "Order #W2611340 was successfully modified in memory."},
            {"status": "success", "message": "Order #W3632959 was successfully modified in memory."},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_042",
        instruction=(
            "Your goal is to oversee a comprehensive account audit for customers 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Begin by enacting the audit policy across their total set of orders. According to the policy, initiate a financial reset by voiding the primary payment at index 0 from each order linked to both users. For any order marked as 'cancelled', ensure it's reactivated prior to voiding the payment. Once the financial reset is completed, proceed to adjust the order statuses: convert all of Mia Martinez's orders ('#W6310710', '#W6436609', '#W4140680') to 'processed', whereas William Li's order '#W2611340' should be switched to 'pending'. William Li's other orders require no further status modifications."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "cancelled"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W6436609"}],
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "removed": True, "payment_history_len": 2},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6436609", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "processed"},
            {"order_id": "#W6436609", "status": "processed"},
            {"order_id": "#W4140680", "status": "processed"},
            {"order_id": "#W2611340", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_043",
        instruction=(
            "Make sure to handle a full-scope audit and status synchronization for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). For each order with the status 'pending', 'processed', or 'delivered', eliminate the payment record found at index 0 (specifically the primary payment). If an order shows a 'cancelled' status, it must be reopened first, then proceed to remove its payment record at index 0 as well. After payment clearing, adjust the status of all of William Li's orders to 'pending' and ensure all of Mia Martinez's orders are set to 'processed'. Maintain exact usage of the given user_ids, order_ids, statuses, and index values without altering them."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "cancelled"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_044",
        instruction=(
            "Handle the application of the new company-wide pricing policy and coordinate an account audit for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Adjust the price of the standard Smartphone variant (product '1801728040', item_id '5339029584') to 105.50 USD. During the audit, remove the payment records at index 0 from all of William Li's active orders with 'processed' or 'delivered' status and shift them to a 'pending' state. Furthermore, return Mia Martinez's single cancelled order to a state where it is ready for processing."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 105.50},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3632959", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
        ],
        outputs=[
            [{"order_id": "#W4140680", "status": "cancelled"}],
            [{"order_id": "#W2611340", "status": "processed"}, {"order_id": "#W3632959", "status": "processed"}],
            [{"order_id": "#W4435622", "status": "delivered"}, {"order_id": "#W3638028", "status": "delivered"}],
            {"product_id": "1801728040", "item_id": "5339029584", "old_price": 1128.99, "new_price": 105.50},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_045",
        instruction=(
            "Execute an end-of-life order processing and pricing audit for customers William Li (user_id 'william_li_5688') and Mia Martinez (user_id 'mia_martinez_3271'). Begin by applying the revised price of 140.00 USD for the standard Smartphone variant (product '1801728040', item_id '5339029584'). Then, according to the EOL audit policy, eliminate the financial records from all of William Li's orders with a 'delivered' status and transition them to a 'pending' state for evaluation. For Mia Martinez, make sure her cancelled order has its main payment cleared before reinstatement and ready her processed order for review by clearing its payment and setting it to 'pending'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 140.00},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W4140680", "index": 0},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_046",
        instruction=(
            "Handle all 'pending' orders of customer Mia Martinez (user_id 'mia_martinez_3271') by changing their status to 'processed'. Concurrently, take her cancelled order '#W4140680', reactivate it, and initiate a financial reset by deleting its main payment record. Conclude by setting the status of this reactivated order to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_047",
        instruction=(
            "Coordinate a series of urgent modifications for customer Luna Wilson (user_id 'luna_wilson_7363'). Initially, adjust the price of the 'T-Shirt' (product_id '9523456873', item_id '9612497925') to 55.00 USD. Subsequently, for her order '#W2693718', include a new addition: one 'Water Bottle' (product_id '8310926033', item_id '6469567736'). Finally, for the cancelled order '#W3220387' of customer Evelyn Costa, reopen it and incorporate one unit of the same 'Water Bottle' item."
        ),
        actions=[
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W2693718",
                    "items": [{"product_id": "8310926033", "item_id": "6469567736", "quantity": 1}],
                },
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W3220387"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W3220387",
                    "items": [{"product_id": "8310926033", "item_id": "6469567736", "quantity": 1}],
                },
            ),
        ],
        outputs=[
            {
                "product_id": "9523456873",
                "item_id": "9612497925",
                "old_price": 50.88,
                "new_price": 55.00,
            },
            {"order_id": "#W2693718", "added_count": 1, "items_len": 6},
            {"order_id": "#W3220387", "status": "pending"},
            {"order_id": "#W3220387", "added_count": 1, "items_len": 3},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_048",
        instruction=(
            "Handle a complex update for customer Sofia Hernandez (user_id 'sofia_hernandez_5364') ensuring the achievement of all specified objectives: Adjust the cost of the item 'T-Shirt' (product_id '9523456873', item_id '9612497925') to precisely 55.00 USD. Include an additional unit of 'Patio Umbrella' (product_id '9743693396', item_id '8170914468') to her active order '#W9609649'. In the case of order '#W3561391', delete its primary payment record at index 0 and update its status to 'processed'. Concerning order '#W6876713', access its financial information, eliminate its primary payment record at index 0, and incorporate one unit of the product 'Water Bottle' (product_id '8310926033', item_id '6469567736'). Utilize exactly the user_id, product_ids, item_ids, order_ids, and values provided above without changes."
        ),
        actions=[
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 1}],
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3561391", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3561391", "status": "processed"}
            ),
            Action(name="GetOrderFinancials", kwargs={"order_id": "#W6876713"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6876713", "index": 0}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W6876713",
                    "items": [{"product_id": "8310926033", "item_id": "6469567736", "quantity": 1}],
                },
            ),
        ],
        outputs=[
            {
                "product_id": "9523456873",
                "item_id": "9612497925",
                "old_price": 50.88,
                "new_price": 55.00,
            },
            {"order_id": "#W9609649", "added_count": 1, "items_len": 6},
            {"order_id": "#W3561391", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3561391", "status": "processed"},
            {"order_id": "#W6876713", "items_total": 0},
            {"order_id": "#W6876713", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6876713", "added_count": 1, "items_len": 6},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_049",
        instruction=(
            "Coordinate a complete account cleanup for William Li (user_id 'william_li_5688') along with a specific price revision. For William Li, expunge the sole existing payment record (found at index 0) from each of his orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028') and adjust all their statuses to 'pending'. Independently, conduct a company-wide price amendment by altering the cost of the standard Smartphone variant (product '1801728040', item_id '5339029584') to 199.99 USD."
        ),
        actions=[
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 199.99},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_050",
        instruction=(
            "Handle a complex update for customer Mei Kovacs (user_id 'mei_kovacs_5767'). For order '#W8193638', remove the item at index 0 and introduce two new 'T-Shirt' variants: variant '8124970213' and variant '9612497925' (both product_id '9523456873') to the same order. Simultaneously, reopen Evelyn Costa's cancelled order '#W3220387', eliminate the payment at index 0, and adjust its status to 'delivered'. Lastly, adjust the price of the 'T-Shirt' (product_id '9523456873', item_id '9612497925') to exactly 55.00 USD and the price of 'Portable Charger' (product_id '6942297802', item_id '7903094618') to exactly 95.00 USD."
        ),
        actions=[
            Action(name="RemoveItemsByIndex", kwargs={"order_id": "#W8193638", "indices": [0]}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [{"product_id": "9523456873", "item_id": "8124970213", "quantity": 1}],
                },
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [{"product_id": "9523456873", "item_id": "9612497925", "quantity": 1}],
                },
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W3220387"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3220387", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3220387", "status": "delivered"}
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "6942297802", "item_id": "7903094618", "new_price": 95.00},
            ),
        ],
        outputs=[
            {"order_id": "#W8193638", "items_removed": [0]},
            {
                "order_id": "#W8193638",
                "items_added": [
                    {"product_id": "9523456873", "item_id": "8124970213", "quantity": 1},
                    {"product_id": "9523456873", "item_id": "9612497925", "quantity": 1},
                ],
            },
            {"order_id": "#W3220387", "payment_removed_index": 0, "status": "delivered"},
            {"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            {"product_id": "6942297802", "item_id": "7903094618", "new_price": 95.00},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_051",
        instruction=(
            "Coordinate a quarterly audit for customer William Li (user_id 'william_li_5688'). The audit policy mandates that all of his orders currently labeled as 'processed' must undergo a financial reset by removing their primary payment record. Post the financial reset, these orders should be transitioned to a 'pending' state for a final review."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_052",
        instruction=(
            "Handle a comprehensive data integrity audit across the system for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). According to the audit policy, a complete financial reset is necessary for all orders with statuses of 'pending', 'processed', or 'delivered' that belong to either customer by clearing the primary payment record (index 0). Once the financial reset is finished, update the status of William Li's orders to 'processed' and Mia Martinez's orders to 'pending'. Be sure to use exactly the specified user_ids, statuses, and order_ids; do not alter any unrelated records."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_053",
        instruction=(
            "Coordinate a full evaluation and status synchronization for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). Implement the audit policy by clearing the primary payment record for every order with statuses 'pending', 'processed', or 'delivered'. For orders with a status of 'cancelled', reactivate them and also clear the primary payment record. Upon completing all financial resets, adjust the statuses so all of William Li's orders are 'pending' and Mia Martinez's orders are 'processed'. Use only the specified order IDs and parameters explicitly."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "cancelled"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_054",
        instruction=(
            "Handle the end-of-quarter account finalization for Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). For Mia Martinez, your task is to address her single inactive order (status 'cancelled') by ensuring it is reactivated and finalizing its status as 'processed'. For William Li, the requirement is to prepare his 'delivered' orders for archival by clearing their single existing payment record at index 0."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_055",
        instruction=(
            "Coordinate a full-scope audit and status alignment for customers Mia Martinez (user_id 'mia_martinez_3271') and William Li (user_id 'william_li_5688'). For every order associated with either customer with status 'pending', 'processed', or 'delivered', eliminate its payment record at index 0. For orders with status 'cancelled', remove the payment at index 0 and then reopen the order. Once all payments are cleared, set every order status for William Li to 'pending', and for Mia Martinez, set every order status to 'processed'. Use exactly the provided user_ids, statuses, order_ids, and indices; ensure payments are not removed more than once per order."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "cancelled"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W6436609", "status": "pending"}],
            [{"order_id": "#W6310710", "status": "processed"}],
            [{"order_id": "#W4140680", "status": "cancelled"}],
            [{"order_id": "#W2611340", "status": "processed"}, {"order_id": "#W3632959", "status": "processed"}],
            [{"order_id": "#W4435622", "status": "delivered"}, {"order_id": "#W3638028", "status": "delivered"}],
            {"order_id": "#W4140680", "removed": True},
            {"order_id": "#W6310710", "removed": True},
            {"order_id": "#W6436609", "removed": True},
            {"order_id": "#W2611340", "removed": True},
            {"order_id": "#W3632959", "removed": True},
            {"order_id": "#W4435622", "removed": True},
            {"order_id": "#W3638028", "removed": True},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed"},
            {"order_id": "#W6310710", "status": "processed"},
            {"order_id": "#W6436609", "status": "processed"},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "status": "pending"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_056",
        instruction=(
            "Handle the processing of the single pending supply order, '#SO9359', for the supplier with ID '#SUP0001'. According to company policy, start by approving the order. Once approved, log an 'info' event using the exact message 'Approved for immediate shipment.'. Finally, formally receive all items for this order and confirm its status as 'completed'."
        ),
        actions=[
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Approved for immediate shipment.",
                },
            ),
            Action(name="ReceiveSupplyOrderAndClose", kwargs={"supply_order_id": "#SO9359"}),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "completed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_057",
        instruction=(
            "Coordinate the system update to accurately reflect the logistics state for shipment tracking ID '357962501027' linked with order '#W2611340'. Verify that the tracking record indicates courier_name = 'Priority Shipping Co.', includes a custom event with status 'rerouted' and the precise note 'Forwarded to partner carrier for final delivery', and that the shipment's tracking status is marked as 'in_transit'. Use only the provided identifiers and texts (tracking_id '357962501027', order '#W2611340'); do not create new tracking IDs or alter unrelated entities."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "357962501027", "courier_name": "Priority Shipping Co."},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "rerouted",
                    "note": "Forwarded to partner carrier for final delivery",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "357962501027", "status": "in_transit"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_058",
        instruction=(
            "Coordinate the entire return and replacement process for customer Mia Martinez (user_id 'mia_martinez_3271'). Start with the return: archive her order '#W6310710' by clearing the item at index 0 and the payment data at index 0, then change its status to 'cancelled'. Continue with the replacement: reactivate her other cancelled order, '#W4140680', remove all three existing items, insert two new units of the standard Smartphone variant (product '1801728040', item_id '5339029584'), and add a new payment of 240.00 USD using 'pm-anya-card-2'. Finally, gather all orders for this customer that are currently 'pending'."
        ),
        actions=[
            Action(name="RemoveItemsByIndex", kwargs={"order_id": "#W6310710", "indices": [0]}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "cancelled"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="RemoveItemsByIndex", kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]}
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 2}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 240.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
        ],
        outputs=[
            {"order_id": "#W6310710", "removed_count": 1, "items_len": 0},
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "cancelled"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "removed_count": 3, "items_len": 0},
            {"order_id": "#W4140680", "added_count": 2, "items_len": 2},
            {"order_id": "#W4140680", "payment_history_len": 3},
            [
                {"order_id": "#W4140680", "status": "pending"},
                {"order_id": "#W6436609", "status": "pending"},
            ],
        ],
    ),
    Task(
        annotator="1",
        user_id="user_059",
        instruction=(
            "Manage a data consolidation and pricing revision for customers William Li (user_id 'william_li_5688') and Mia Martinez (user_id 'mia_martinez_3271'). For William Li, consolidate the items and payments from his order '#W3632959' into the destination order '#W2611340', making sure the final status of the consolidated order is 'processed'. For Mia Martinez, eliminate the primary payment record from her 'processed' order '#W6310710'. Lastly, implement a company-wide price adjustment for the standard Smartphone variant (product '1801728040', item_id '5339029584'), updating its price to 160.00 USD. Conclude by retrieving all 'processed' orders for William Li."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="MergeOrdersForSameUser",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": True,
                },
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 160.00},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
        ],
        outputs=[[{"order_id": "#W2611340", "status": "processed"}]],
    ),
    Task(
        annotator="1",
        user_id="user_060",
        instruction=(
            "Address a customer request for 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753') who seeks to amend her pending order '#W9903153'. Replace the item located at index 3 with a 'Water Bottle' (product '8310926033', item '6469567736'). Following the replacement, ensure the order's finances are fully reconciled, which includes canceling the original payment and implementing a new payment for the adjusted total using her payment method 'credit_card_5869505'. For logistics purposes, consolidate this shipment with her previous order by associating it with the current tracking ID '443521489581'. Conclude by appending an 'info' type event with the note 'Order #W9903153 added to this shipment. Contents verified.' to the tracking record and process the updated order."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "pending"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 3,
                    "product_id": "8310926033",
                    "item_id": "6469567736",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W9903153"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W9903153",
                    "transaction_type": "payment",
                    "amount": 3437.33,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W9903153", "tracking_id": "443521489581"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Order #W9903153 added to this shipment. Contents verified.",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
        ],
        outputs=[
            [{"order_id": "#W9903153", "status": "pending"}],
            {"status": "success", "message": "Order #W9903153 was successfully modified in memory."},
            {"order_id": "#W9903153", "items_total": 3437.33},
            {"order_id": "#W9903153", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9903153", "payment_history_len": 1},
            {"order_id": "#W9903153", "tracking_id": "443521489581", "fulfillments_len": 1},
            {"tracking_id": "443521489581", "new_status": "info", "history_len": 1},
            {"order_id": "#W9903153", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_061",
        instruction=(
            "Manage a logistics issue with the shipment tracking ID '357962501027'. As per the resolution policy, record a 'delayed' event with the note 'Weather disruption in transit' and ensure delivery is completed by updating its status directly to 'delivered'. Once delivered, confirm that the associated order, '#W2611340', is likewise marked as 'delivered'. Additionally, as a separate preparation task, ready all of Mia Martinez's (user_id 'mia_martinez_3271') orders with a 'pending' status for review by removing their primary payment records located at index 0."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "delayed",
                    "note": "Weather disruption in transit",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "delivered"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6436609", "index": 0}),
        ],
        outputs=[
            [{"order_id": "#W6436609", "status": "pending"}],
            {"tracking_id": "357962501027", "new_status": "delayed"},
            {"tracking_id": "357962501027", "new_status": "delivered"},
            {"order_id": "#W2611340", "status": "delivered"},
            {"order_id": "#W6436609", "removed": True, "payment_history_len": 0},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_062",
        instruction=(
            "Your task is to execute a cross-customer account examination and settlement for 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Start by addressing Anya's account. As per audit policy, initiate her 'processed' order '#W6310710' by reversing the payment at index 0 and adjusting its status to 'pending'. Additionally, reactivate her 'cancelled' order '#W4140680' by reopening it, incorporating one 'Gaming Mouse' (product '5713490933', item '5796612084'), and allocating a new 'payment' of $75.00 with method 'pm-anya-card-2'. Subsequently, review all of William Li's 'processed' and 'delivered' orders. Each of these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028') must have the payment at index 0 voided and the order's status set to 'pending' for further review, according to policy."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_063",
        instruction=(
            "Your task is to handle the entire lifecycle of a customer-amended order for 'Mia Martinez' (user_id 'mia_martinez_3271'). Begin by processing her pending order '#W6436609' through the replacement of the item at index 0 with a 'Smart Watch' (product '6945232052', variant '9408160950'). The next step involves a comprehensive financial reconciliation: annul the original payment at index 0 and apply a new 'payment' for the revised total of $3285.76 using payment method 'pm-anya-card-2'. To finalize the fulfillment procedure, link the present tracking ID '951786982868' and update its status in sequence to 'in_transit' and subsequently 'delivered'. Upon delivery, modify the order status accordingly. Lastly, conclude the customer service process by issuing a partial 'refund' of 20.00 USD to the same payment method, 'pm-anya-card-2'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6436609",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "9408160950",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W6436609"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W6436609", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6436609",
                    "transaction_type": "payment",
                    "amount": 3285.76,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W6436609", "tracking_id": "951786982868"},
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "951786982868", "status": "in_transit"},
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6436609", "status": "delivered"},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6436609",
                    "transaction_type": "refund",
                    "amount": 20.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
        ],
        outputs=[
            [{"order_id": "#W6436609", "status": "pending"}],
            {"status": "success", "message": "Order #W6436609 was successfully modified in memory."},
            {"order_id": "#W6436609", "items_total": 3285.76},
            {"order_id": "#W6436609", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6436609", "payment_history_len": 1},
            {"order_id": "#W6436609", "tracking_id": "951786982868", "fulfillments_len": 1},
            {"tracking_id": "951786982868", "new_status": "in_transit"},
            {"tracking_id": "951786982868", "new_status": "delivered"},
            {"order_id": "#W6436609", "status": "delivered"},
            {"order_id": "#W6436609", "payment_history_len": 2},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_064",
        instruction=(
            "Your task is to handle a fulfillment crisis for customer 'luca_rossi_2745' concerning order '#W3631991'. This involves managing supply order '#SO9359' by documenting a 'note' ('Emergency restock for promotion'), acknowledging its receipt ('Urgent shipment received'), and recording a final 'note' ('Delivery completed successfully'). Simultaneously, you need to update the customer order by adding one unit (quantity 1) of the new stock (product '9523456873', item '9612497925'). Financial policy dictates a reconciliation: apply a 'payment' of $39.99 with method 'pm_002' and void the payment at index 1. To conclude the fulfillment, you must progress the order status first to 'shipped' and ultimately to 'delivered'."
        ),
        actions=[
            Action(name="AppendSupplyOrderEvent", kwargs={
                "supply_order_id": "#SO9359",
                "event_type": "note",
                "message": "Emergency restock for promotion"
            }),
            Action(name="ReceiveSupplyOrderAndClose", kwargs={
                "supply_order_id": "#SO9359",
                "note": "Urgent shipment received"
            }),
            Action(name="AddItemsToOrder", kwargs={
                "order_id": "#W3631991",
                "items": [{"product_id": "9523456873", "item_id": "9612497925", "quantity": 1}]
            }),
            Action(name="AppendPayment", kwargs={
                "order_id": "#W3631991",
                "transaction_type": "payment",
                "amount": 39.99,
                "payment_method_id": "pm_002"
            }),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3631991", "index": 1}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3631991", "status": "shipped"}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3631991", "status": "delivered"}),
            Action(name="AppendSupplyOrderEvent", kwargs={
                "supply_order_id": "#SO9359",
                "event_type": "note",
                "message": "Delivery completed successfully"
            }),
        ],
        outputs=[
            {"supply_order_id": "#SO9359", "events_len": 1},
            {"supply_order_id": "#SO9359", "status": "closed", "events_len": 2},
            {"order_id": "#W3631991", "added_count": 1, "items_len": 3},
            {"order_id": "#W3631991", "payment_history_len": 2},
            {"order_id": "#W3631991", "removed": True, "payment_history_len": 1},
            {"order_id": "#W3631991", "status": "shipped"},
            {"order_id": "#W3631991", "status": "delivered"},
            {"supply_order_id": "#SO9359", "events_len": 3},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_065",
        instruction=(
            "Your responsibility is to resolve an account issue for 'Mia Martinez' (user_id 'mia_martinez_3271') by reactivating her cancelled order '#W4140680'. The objective is to ready this order for shipment by including a 'Smart Watch' (product '6945232052', variant '9408160950') and conducting a 'payment' transaction of 250.00 USD via her payment method 'pm-anya-card-1'. To satisfy the fulfillment requirements, you must consolidate this order's shipment by associating the tracking ID from William Li's order '#W3632959' and then ensure the order is marked as 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "6945232052", "item_id": "9408160950", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 250.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="FindTrackingByOrder",
                kwargs={"order_id": "#W3632959"},
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W4140680", "tracking_id": "474654093386"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
        ],
        outputs=[
            [{"order_id": "#W4140680", "status": "cancelled"}],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"tracking_id": ["474654093386"], "order_id": "#W3632959"},
            {"order_id": "#W4140680", "tracking_id": "474654093386", "fulfillments_len": 2},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_066",
        instruction=(
            "Handle a multi-part operational workflow for customer 'Juan Johnson' (user_id 'juan_johnson_5229'). Begin by updating the shipment with tracking ID '326515289837'. The policy dictates the courier be changed to 'SpeedWay Delivery', an 'info' status event be logged with the note 'Rerouted to new courier', and the tracking status be advanced to 'delivered'. Proceed to coordinate a financial reset on his active orders '#W1429524' and '#W7546247' by removing the payment at index 0 from each, setting their final statuses to 'pending'."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "SpeedWay Delivery",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Rerouted to new courier",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "326515289837", "status": "delivered"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W1429524", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W1429524", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W7546247", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W7546247", "status": "pending"}),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "SpeedWay Delivery"},
            {"tracking_id": "326515289837", "new_status": "info", "history_len": 2},
            {"tracking_id": "326515289837", "new_status": "delivered", "history_len": 3},
            {"order_id": "#W1429524", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1429524", "status": "pending"},
            {"order_id": "#W7546247", "removed": True, "payment_history_len": 0},
            {"order_id": "#W7546247", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_067",
        instruction=(
            "Coordinate a comprehensive account cleanup for customer Olivia Rodriguez (user_id 'olivia_rodriguez_9753'). The policy necessitates finding all her orders for a financial reset and status update. Specifically, for orders '#W3113816' and '#W9903153', the primary payment must be cleared and their status set to 'pending'. For order '#W1620235', clear the payment and change the status to 'delivered'. Lastly, for order '#W2918688', clear the payment and change the status to 'cancelled'."
        ),
        actions=[
            Action(name="FindOrdersByUserAndStatus", kwargs={"user_id": "olivia_rodriguez_9753"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3113816", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3113816", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W9903153", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W9903153", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W1620235", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W1620235", "status": "delivered"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2918688", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W2918688", "status": "cancelled"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_068",
        instruction=(
            "Your task is to manage a detailed account workflow for 'Sofia Hernandez' (user_id 'sofia_hernandez_5364') as part of a full order audit. You need to process three specific orders following policy guidelines. For her pending order '#W9609649', add one 'Electric Kettle' (product '1075968781', item '9624127908'), apply a 'payment' of $120.00 using 'pm-sofia-card-3', and update its status to 'processed'. For her processed order '#W5765741', add two 'Patio Umbrella' items (product '9743693396', item '8170914468'), apply a 'payment' of $1500.00 using 'pm-sofia-card-3', and change its status to 'delivered'. Lastly, for her pending order '#W3561391', remove the payment at index 0 and update its status to 'cancelled'."
        ),
        actions=[
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "1075968781", "item_id": "9624127908", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W9609649",
                    "transaction_type": "payment",
                    "amount": 120.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W9609649", "status": "processed"}
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W5765741",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 2}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W5765741",
                    "transaction_type": "payment",
                    "amount": 1500.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W5765741", "status": "delivered"}
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3561391", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W3561391", "status": "cancelled"}
            ),
        ],
        outputs=[
            {"order_id": "#W9609649", "added_count": 1, "items_len": 6},
            {"order_id": "#W9609649", "payment_history_len": 2},
            {"order_id": "#W9609649", "status": "processed"},
            {"order_id": "#W5765741", "added_count": 2, "items_len": 4},
            {"order_id": "#W5765741", "payment_history_len": 2},
            {"order_id": "#W5765741", "status": "delivered"},
            {"order_id": "#W3561391", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3561391", "status": "cancelled"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_071",
        instruction=(
            "Your assignment is to carry out a detailed account examination for 'Mia Martinez' (user_id 'mia_martinez_3271'). Your main objective is to handle an item exchange on her processed order '#W6310710'. Replace the item at index 0 with a 'Gaming Mouse' (product '5713490933', item '5796612084'). After completing the exchange, apply a new 'payment' of $150.00 using payment method 'pm-anya-card-2'. Additionally, restore her cancelled order '#W4140680' by reopening it and updating its status to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "5713490933",
                    "item_id": "5796612084",
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 150.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W6310710", "status": "processed"}
            ],
            {"status": "success", "message": "Order #W6310710 was successfully modified in memory."},
            {"order_id": "#W6310710", "payment_history_len": 2},
            [
                {"order_id": "#W4140680", "status": "cancelled"}
            ],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_072",
        instruction=(
            "Your task is to handle a multi-faceted logistics and account update. For the customer 'William Li' (user_id 'william_li_5688'), complete the shipment of his processed order '#W2611340'. You should update its tracking record ('357962501027') to designate the courier as 'RapidTransit Solutions', incorporate a 'delayed' event noting 'Weather disruption in transit', and move the tracking status forward to 'delivered'. For the customer 'Mia Martinez' (user_id 'mia_martinez_3271'), you need to revive her cancelled order '#W4140680' by reopening it. Finally, coordinate an ongoing supply chain operation by endorsing the pending supply order '#SO9359' for supplier '#SUP0001' with the justification 'Restock approved' and subsequently handle its receipt processing to refresh inventory."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "357962501027", "courier_name": "RapidTransit Solutions"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "delayed",
                    "note": "Weather disruption in transit",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AutoApproveSupplyOrder",
                kwargs={"supply_order_id": "#SO9359", "reason": "Restock approved"},
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO9359"},
            ),
        ],
        outputs=[
            {"tracking_id": "357962501027", "courier_name": "RapidTransit Solutions"},
            {"tracking_id": "357962501027", "new_status": "delayed", "history_len": 2},
            {"tracking_id": "357962501027", "new_status": "delivered", "history_len": 3},
            [{"order_id": "#W4140680", "status": "cancelled"}],
            {"order_id": "#W4140680", "status": "pending"},
            {"supply_order_id": "#SO9359", "status": "approved", "events_len": 1},
            {"supply_order_id": "#SO9359", "status": "closed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_073",
        instruction=(
            "Your task involves coordinating several required changes on 'Mia Martinez’s' account (user_id 'mia_martinez_3271'). The initial goal is to update her pending order '#W6436609'. You should substitute the item at index 0 with an 'Electric Kettle' (product '1075968781', item '9624127908') and then document the updated financial state of the order. The second goal is to bring back her cancelled order '#W4140680'. You are to reopen it, clear the contents by removing the three items at indices 0, 1, and 2, introduce a new 'Smart Watch' (product '6945232052', item '2681513500'), and then update its status to 'processed'. Finally, ensure that the initially modified order, '#W6436609', is also given a 'processed' status."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W6436609",
                    "index": 0,
                    "product_id": "1075968781",
                    "item_id": "9624127908",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W6436609"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "6945232052", "item_id": "2681513500", "quantity": 1}],
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6436609", "status": "processed"},
            ),
        ],
        outputs=[
            [{"order_id": "#W6436609", "status": "pending"}],
            [{"order_id": "#W4140680", "status": "cancelled"}],
            {"status": "success", "message": "Order #W6436609 was successfully modified in memory."},
            {"order_id": "#W6436609", "items_total": 3063.4},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "removed_count": 3, "items_len": 0},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 1},
            {"order_id": "#W4140680", "status": "processed"},
            {"order_id": "#W6436609", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_074",
        instruction=(
            "Your objective involves coordinating a multi-part administrative task concerning logistics, account auditing, and pricing. For customer 'Juan Johnson' (user_id 'juan_johnson_5229'), you need to complete the logistics for his order '#W7546247'. Update its tracking record ('326515289837') to utilize 'Priority Shipping Co.', log an 'info' event with the specific note 'Carrier change requested by logistics', and advance the status to 'in_transit'. For customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'), your responsibility is to conduct a financial audit on all of her delivered orders ('#W3113816' and '#W1539823'). The audit policy requires voiding the primary payment at index 0 from each order and resetting their statuses to 'pending' for review. As a concluding administrative task, you will coordinate a company-wide price update for the 'Smart Watch' (product '6945232052', item '9408160950'), establishing its new price at 299.99 USD."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "Priority Shipping Co.",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Carrier change requested by logistics",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "326515289837", "status": "in_transit"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "delivered"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "6945232052", "item_id": "9408160950", "new_price": 299.99},
            ),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "Priority Shipping Co."},
            {"tracking_id": "326515289837", "new_status": "info", "history_len": 2},
            {"tracking_id": "326515289837", "new_status": "in_transit", "history_len": 3},
            [{"order_id": "#W3113816"}, {"order_id": "#W1539823"}],
            {"order_id": "#W3113816", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3113816", "status": "pending"},
            {"order_id": "#W1539823", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1539823", "status": "pending"},
            {"product_id": "6945232052", "item_id": "9408160950", "old_price": 381.26, "new_price": 299.99},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_075",
        instruction=(
            "Your objective requires overseeing a post-shipment return and financial adjustment for 'William Li' (user_id 'william_li_5688') on his order '#W2611340'. Your primary task is to intercept the shipment with tracking ID '357962501027'. Update its courier to 'RapidTransit Solutions'. You are to log this action in the tracking history as a 'checkpoint' event with the note 'Shipment rerouted back to sender at customer request.' and then change the shipment's final status to 'returning'. After handling logistics, your next task is to financially reconcile the order: remove the returned 'Office Chair' at index 1, void the original payment at index 0, and apply a new 'payment' of $850.25 from payment method 'gift_card_1725971'."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={
                    "tracking_id": "357962501027",
                    "courier_name": "RapidTransit Solutions",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "checkpoint",
                    "note": "Shipment rerouted back to sender at customer request.",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "357962501027", "status": "returning"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W2611340", "indices": [1]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 850.25,
                    "payment_method_id": "gift_card_1725971",
                },
            ),
        ],
        outputs=[
            {"tracking_id": "357962501027", "courier_name": "RapidTransit Solutions"},
            {"tracking_id": "357962501027", "new_status": "checkpoint", "history_len": 2},
            {"tracking_id": "357962501027", "new_status": "returning", "history_len": 3},
            {"order_id": "#W2611340", "removed_count": 1, "items_len": 1},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "payment_history_len": 1},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_076",
        instruction=(
            "Handle a crucial update for customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). The main task is to manage an item exchange on her processed order '#W8160318' by substituting the item at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'). Subsequent to the exchange, it is necessary to reconcile the order's financials by voiding the payment at index 0 and applying a new 'payment' of 550.00 USD using payment method 'paypal_emma_santos_1'. To finalize the task, you will consolidate its shipment with her order '#W3113816' by connecting the existing tracking ID '443521489581' and logging an 'info' event with the note 'Package prepared for dispatch'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "processed"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W8160318",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W8160318", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W8160318",
                    "transaction_type": "payment",
                    "amount": 550.0,
                    "payment_method_id": "paypal_emma_santos_1",
                },
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={
                    "order_id": "#W3113816",
                    "tracking_id": "443521489581",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Package prepared for dispatch",
                },
            ),
        ],
        outputs=[
            [{"order_id": "#W8160318", "status": "processed", "items_len": 2}],
            {
                "status": "success",
                "message": "Order #W8160318 was successfully modified in memory.",
            },
            {"order_id": "#W8160318", "removed": True, "payment_history_len": 0},
            {"order_id": "#W8160318", "payment_history_len": 1},
            {"order_id": "#W3113816", "tracking_id": "443521489581", "fulfillments_len": 2},
            {"tracking_id": "443521489581", "new_status": "info", "history_len": 1},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_077",
        instruction=(
            "Coordinate a thorough financial audit and status realignment for all of 'Olivia Rodriguez''s (user_id 'olivia_rodriguez_9753') active orders. It is necessary to implement the company's end-of-quarter policy, which involves voiding the primary payment from all 'pending', 'processed', and 'delivered' orders. Following the payment reset, each order's status must be adjusted according to its original condition: delivered orders ('#W3113816', '#W1539823') are moved to pending; pending orders '#W9903153' and '#W2918688' are cancelled while others ('#W1620235', '#W9655299') are processed; and processed orders ('#W8160318') remain unchanged. Conclusively, as an additional administrative task, you will execute company-wide price updates to the 'Patio Umbrella' (product '9743693396', item '8170914468') and the 'Water Bottle' (product '8310926033', item '6469567736'), setting their new prices to 799.00 USD and 28.00 USD respectively."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "delivered"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "cancelled"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2918688", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2918688", "status": "cancelled"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W1620235", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1620235", "status": "processed"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W9655299", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9655299", "status": "processed"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W8160318", "index": 0},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9743693396", "item_id": "8170914468", "new_price": 799.00},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "8310926033", "item_id": "6469567736", "new_price": 28.00},
            ),
        ],
        outputs=[
            [{"order_id": "#W9903153"}, {"order_id": "#W1620235"}, {"order_id": "#W2918688"}, {"order_id": "#W9655299"}],
            [{"order_id": "#W8160318"}],
            [{"order_id": "#W3113816"}, {"order_id": "#W1539823"}],
            {"order_id": "#W3113816", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3113816", "status": "pending"},
            {"order_id": "#W1539823", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1539823", "status": "pending"},
            {"order_id": "#W9903153", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9903153", "status": "cancelled"},
            {"order_id": "#W2918688", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2918688", "status": "cancelled"},
            {"order_id": "#W1620235", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1620235", "status": "processed"},
            {"order_id": "#W9655299", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9655299", "status": "processed"},
            {"order_id": "#W8160318", "removed": True, "payment_history_len": 0},
            {"product_id": "9743693396", "item_id": "8170914468", "old_price": 316.29, "new_price": 799.00},
            {"product_id": "8310926033", "item_id": "6469567736", "old_price": 47.84, "new_price": 28.00},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_078",
        instruction=(
            "Handle a multi-faceted administrative operation. Initially, you are to manage the logistics for customer 'Juan Johnson' (user_id 'juan_johnson_5229') regarding his order '#W7546247'. You must update its tracking record ('326515289837') to 'Priority Shipping Co.', log an 'info' event with the note 'Carrier change requested by logistics', exactly as stated, and change the status to 'in_transit'. Next, coordinate a financial audit for 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). In accordance with audit policy, process all of her delivered orders ('#W3113816' and '#W1539823') by voiding the primary payment at index 0 from each and reverting their statuses to 'pending' for review. Lastly, oversee a company-wide price update for the 'Smart Watch' (product '6945232052', item '9408160950'), establishing its new price at 299.99 USD."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "Priority Shipping Co.",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Carrier change requested by logistics",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "326515289837", "status": "in_transit"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "delivered"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "6945232052", "item_id": "9408160950", "new_price": 299.99},
            ),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "Priority Shipping Co."},
            {"tracking_id": "326515289837", "new_status": "info", "history_len": 2},
            {"tracking_id": "326515289837", "new_status": "in_transit", "history_len": 3},
            [{"order_id": "#W3113816"}, {"order_id": "#W1539823"}],
            {"order_id": "#W3113816", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3113816", "status": "pending"},
            {"order_id": "#W1539823", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1539823", "status": "pending"},
            {"product_id": "6945232052", "item_id": "9408160950", "old_price": 150.58, "new_price": 299.99},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_079",
        instruction=(
            "Handle a financial re-audit for customer 'William Li' (user_id 'william_li_5688') and apply a pricing update. During the audit, locate his 'delivered' orders, particularly '#W4435622' and '#W3638028'. For each order, you are required to remove the primary payment records (at index 0) and change their status to 'pending'. Additionally, you will need to update the company-wide pricing for two 'T-Shirt' (product_id '9523456873') variants: set item '8124970213' to 45.50 USD and item '9612497925' to 50.00 USD."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "8124970213", "new_price": 45.50},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 50.00},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W4435622", "status": "delivered"},
                {"order_id": "#W3638028", "status": "delivered"},
            ],
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "status": "pending"},
            {
                "product_id": "9523456873",
                "item_id": "8124970213",
                "old_price": 39.99,
                "new_price": 45.50,
            }
        ],
    ),
    Task(
        annotator="1",
        user_id="user_080",
        instruction=(
            "Handle a comprehensive audit of the account for 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). Your aim is to alter her orders in accordance with the audit policy. For the pending order '#W9903153', eliminate the item situated at index 1. Regarding her other pending order '#W1620235', introduce one 'Pet Bed' (product '2747247837', item '6942241102'). For the delivered order '#W3113816', amend its tracking record ('443521489581') by altering the courier to 'RapidTransit Solutions' and adding an 'info' event stating 'Shipment audit complete'. To conclude the audit, ensure that both modified pending orders ('#W9903153' and '#W1620235') are marked as 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "pending"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W9903153", "indices": [1]},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W1620235",
                    "items": [{"product_id": "2747247837", "item_id": "6942241102", "quantity": 1}],
                },
            ),
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "443521489581", "courier_name": "RapidTransit Solutions"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Shipment audit complete",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1620235", "status": "processed"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W9903153", "status": "pending"},
                {"order_id": "#W1620235", "status": "pending"},
                {"order_id": "#W2918688", "status": "pending"},
                {"order_id": "#W9655299", "status": "pending"},
            ],
            {"order_id": "#W9903153", "removed_count": 1, "items_len": 4},
            {"order_id": "#W1620235", "added_count": 1, "items_len": 4},
            {"tracking_id": "443521489581", "courier_name": "RapidTransit Solutions"},
            {"tracking_id": "443521489581", "new_status": "info", "history_len": 2},
            {"order_id": "#W9903153", "status": "processed"},
            {"order_id": "#W1620235", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_081",
        instruction=(
            "Coordinate the updates for customer 'Mia Martinez' (user_id 'mia_martinez_3271'). Her order '#W2611340' has been received and dispatched. Proceed by completing the tracking updates by logging an `info` event to tracking ID '357962501027' with the note 'Shipment verified by logistics team', and then updating its status to 'delivered'. Once delivery confirmation is received, change the order status to 'delivered'. Additionally, reactivate her cancelled order '#W4140680', replenish it with one 'Gaming Mouse' (5713490933, 5796612084) and one 'T-Shirt' (9523456873, 9612497925), process a new payment of $850.00 using 'credit_card_8955149', and finalize the order as 'processed'."
        ),
        actions=[
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "info",
                    "note": "Shipment verified by logistics team",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "delivered"},
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [
                        {"product_id": "5713490933", "item_id": "5796612084", "quantity": 1},
                        {"product_id": "9523456873", "item_id": "9612497925", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 850.00,
                    "payment_method_id": "credit_card_8955149",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
        ],
        outputs=[
            {"tracking_id": "357962501027", "new_status": "info", "history_len": 1},
            {"tracking_id": "357962501027", "new_status": "delivered", "history_len": 3},
            {"order_id": "#W2611340", "status": "delivered"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 2, "items_len": 5},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_082",
        instruction=(
            "Handle the task of cross-customer reconciliation. For customer 'William Li' (user_id 'william_li_5688'), the aim is to consolidate his processed orders for review. Integrate his order '#W3632959' into '#W2611340' (excluding payments), then mark the consolidated order's status as 'pending'. Simultaneously, for customer 'Mia Martinez' (user_id 'mia_martinez_3271'), reopen her cancelled order '#W4140680', incorporate one 'Smartphone' (product '1801728040', item '5339029584'), apply a new 'payment' of $200.00 using 'pm-anya-card-2', and change its status to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="MergeOrdersForSameUser",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": False,
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "pending"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 200.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W2611340", "status": "processed"},
                {"order_id": "#W3632959", "status": "processed"},
            ],
            {"target_order_id": "#W2611340", "moved_items": 1, "target_items_len": 3},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_083",
        instruction=(
            "Coordinate a two-part administrative process. Initially, manage a post-shipment interception and financial adjustment for 'Aarav Lopez' (user_id 'aarav_lopez_9729') concerning his order '#W5455653'. Update the tracking record ('632894717617') to designate 'RapidTransit Solutions', document an 'info' event with the note 'Return to sender initiated', and adjust the shipment status to 'returning'. After the logistics update, reconcile the order's finances by voiding the payment at index 0 and providing a 'refund' of $50.00 using the payment method 'credit_card_2690859'. Subsequently, proceed to cancel the pending order '#W1429524' for customer 'Juan Johnson' (user_id 'juan_johnson_5229')."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "632894717617", "courier_name": "RapidTransit Solutions"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "632894717617",
                    "event_status": "info",
                    "note": "Return to sender initiated",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "632894717617", "status": "returning"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W5455653", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W5455653",
                    "transaction_type": "refund",
                    "amount": 50.00,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1429524", "status": "cancelled"},
            ),
        ],
        outputs=[
            {"tracking_id": "632894717617", "courier_name": "RapidTransit Solutions"},
            {"tracking_id": "632894717617", "new_status": "info", "history_len": 2},
            {"tracking_id": "632894717617", "new_status": "returning", "history_len": 7},
            {"order_id": "#W5455653", "removed": True, "payment_history_len": 0},
            {"order_id": "#W5455653", "payment_history_len": 1},
            {"order_id": "#W1429524", "status": "cancelled"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_084",
        instruction=(
            "Your task is to handle a multi-step update across two significant customer accounts. For 'Sofia Hernandez' (user_id 'sofia_hernandez_5364'), you should void the primary payment at index 0 from her order '#W5765741', add two 'Patio Umbrella' items (product '9743693396', item '8170914468'), process a new payment of $1500.00 using 'pm-sofia-card-3', and update the order status to 'delivered'. For 'Mia Martinez' (user_id 'mia_martinez_3271'), you need to accomplish two goals: first, reopen her cancelled order '#W4140680'. Then, complete the shipment for her order '#W6310710' by inserting an 'info' tracking event to '951786982868' with the note 'Shipment verified by logistics team', changing the tracking status to 'delivered', and updating the order status to 'delivered'."
        ),
        actions=[
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W5765741", "index": 0},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W5765741",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 2}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W5765741",
                    "transaction_type": "payment",
                    "amount": 1500.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W5765741", "status": "delivered"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Shipment verified by logistics team",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6310710", "status": "delivered"},
            ),
        ],
        outputs=[
            {"order_id": "#W5765741", "removed": True, "payment_history_len": 0},
            {"order_id": "#W5765741", "added_count": 2, "items_len": 4},
            {"order_id": "#W5765741", "payment_history_len": 1},
            {"order_id": "#W5765741", "status": "delivered"},
            {"order_id": "#W4140680", "status": "pending"},
            {"tracking_id": "951786982868", "new_status": "info"},
            {"tracking_id": "951786982868", "new_status": "delivered"},
            {"order_id": "#W6310710", "status": "delivered"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_085",
        instruction=(
            "Your duty is to coordinate an end-of-quarter financial audit for customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). You need to apply a specific realignment policy to several of her orders. This policy requires you to initially void the primary payment at index 0 for each of the following orders: '#W3113816', '#W9903153', '#W1620235', and '#W2918688'. Once the payments are voided, the orders must be assigned new statuses: '#W3113816' becomes 'pending', '#W9903153' changes to 'cancelled', and '#W1620235' updates to 'processed'. The order '#W2918688' requires no status change."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "cancelled"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W1620235", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1620235", "status": "processed"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2918688", "index": 0},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W3113816", "status": "delivered"},
                {"order_id": "#W9903153", "status": "pending"},
                {"order_id": "#W1620235", "status": "pending"},
                {"order_id": "#W2918688", "status": "pending"},
                {"order_id": "#W8160318", "status": "processed"},
                {"order_id": "#W1539823", "status": "delivered"},
                {"order_id": "#W9655299", "status": "pending"},
            ],
            {"order_id": "#W3113816", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3113816", "status": "pending"},
            {"order_id": "#W9903153", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9903153", "status": "cancelled"},
            {"order_id": "#W1620235", "removed": True, "payment_history_len": 0},
            {"order_id": "#W1620235", "status": "processed"},
            {"order_id": "#W2918688", "removed": True, "payment_history_len": 0},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_086",
        instruction=(
            "Your task is to perform a cross-customer account audit and reconciliation for 'Mia Martinez' (user_id 'mia_martinez_3271') and 'William Li' (user_id 'william_li_5688'). Initially, focus on managing Anya's account. As per audit policy, address her 'processed' order '#W6310710' by voiding the payment at index 0 and changing its status to 'pending'. Additionally, reactivate her 'cancelled' order '#W4140680' by reopening it, inserting one 'Gaming Mouse' (product '5713490933', item '5796612084'), and applying a new 'payment' of $75.00 using the method 'pm-anya-card-2'. Next, audit all of William Li's 'processed' and 'delivered' orders. For these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), the policy mandates voiding the payment at index 0 and setting the order's status to 'pending' for review."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "delivered"},
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="SetOrderStatus", kwargs={"order_id": "#W6310710", "status": "pending"}
            ),
            Action(name="ReopenCancelledOrder", kwargs={"order_id": "#W4140680"}),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="RemovePaymentByIndex", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="SetOrderStatus", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            [{"order_id": "#W6310710"}],
            [{"order_id": "#W4140680"}],
            [{"order_id": "#W2611340"}, {"order_id": "#W3632959"}],
            [{"order_id": "#W4435622"}, {"order_id": "#W3638028"}],
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "pending"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "pending"},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "pending"},
            {"order_id": "#W4435622", "removed": True, "payment_history_len": 0},
            {"order_id": "#W4435622", "status": "pending"},
            {"order_id": "#W3638028", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3638028", "status": "pending"},
        ]
    ),
    Task(
        annotator="1",
        user_id="user_087",
        instruction=(
            "Your task is to coordinate a multi-part operation involving logistics, supply chain, and pricing. For Mia Martinez's order '#W6310710', complete its shipment by updating its tracking record ('951786982868') to reflect the courier 'Priority Shipping Co.', record an 'info' event with the exact note 'Recipient requested change of courier.', and set both the order and tracking statuses to 'delivered'. Regarding supplier '#SUP0002', oversee their pending 'Gaming Mouse' inventory by approving supply order '#SO6035' with an 'info' event note 'Approved per inventory flag', and process its receipt, while canceling supply order '#SO7848'. Post restocking, implement a price adjustment to the 'Gaming Mouse' (product '5713490933', item '8214883393') to $82.50."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "951786982868", "courier_name": "Priority Shipping Co."},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Recipient requested change of courier.",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6310710", "status": "delivered"},
            ),
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Approved per inventory flag",
                },
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO7848", "status": "cancelled"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 82.50},
            ),
        ],
        outputs=[
            {"tracking_id": "951786982868", "courier_name": "Priority Shipping Co."},
            {"tracking_id": "951786982868", "new_status": "info", "history_len": 2},
            {"tracking_id": "951786982868", "new_status": "delivered", "history_len": 3},
            {"order_id": "#W6310710", "status": "delivered"},
            [{"supply_order_id": "#SO6035", "status": "pending"}, {"supply_order_id": "#SO7848", "status": "pending"}],
            {"supply_order_id": "#SO6035", "status": "approved"},
            {"supply_order_id": "#SO6035", "events_len": 1},
            {"supply_order_id": "#SO6035", "status": "closed"},
            {"supply_order_id": "#SO7848", "status": "cancelled"},
            {"product_id": "5713490933", "item_id": "8214883393", "old_price": 150.58, "new_price": 82.50},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_088",
        instruction=(
            "The task is to handle the downstream consequences of a supply chain disruption for customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). Begin by managing the cancellation of supply order '#SO6035' by changing its status to 'cancelled' and recording an 'info' type event noting 'Cancelled due to supplier quality control failure.'. To address the resulting stock dilemma for her order '#W3113816', substitute the out-of-stock item at index 2 with a 'Smart Watch' (product '6945232052', variant '2681513500') and update the order's status to 'pending' for further review. Conclude by amending the order's tracking record ('443521489581') by adding an 'info' type event with the note 'Order contents updated due to stock issue. Shipment will proceed as scheduled.' and adjust the price for the newly added 'Smart Watch' variant to $255.00."
        ),
        actions=[
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO6035", "status": "cancelled"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Cancelled due to supplier quality control failure.",
                },
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "delivered"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3113816",
                    "index": 2,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Order contents updated due to stock issue. Shipment will proceed as scheduled.",
                },
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "6945232052", "item_id": "2681513500", "new_price": 255.00},
            ),
        ],
        outputs=[
            {"supply_order_id": "#SO6035", "status": "cancelled"},
            {"supply_order_id": "#SO6035", "events_len": 1},
            [{"order_id": "#W3113816"}, {"order_id": "#W1539823"}],
            {"status": "success", "message": "Order #W3113816 was successfully modified in memory."},
            {"order_id": "#W3113816", "status": "pending"},
            {"tracking_id": "443521489581", "new_status": "info"},
            {"product_id": "6945232052", "item_id": "2681513500", "old_price": 356.23, "new_price": 255.00},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_089",
        instruction=(
            "Responsible for organizing the account of 'William Li' (user_id 'william_li_5688') for archival is your task. Start by identifying all his 'processed' orders. For order '#W2611340', you need to eliminate all items (at indices 0 and 1) and remove its primary payment. After these items are cleared, change its status to 'cancelled'. Next, for the other order '#W3632959', similarly remove its sole item (at index 0) and its primary payment. Subsequently, update its status to 'cancelled' to finalize the archival procedure."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W2611340", "indices": [0, 1]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "cancelled"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W3632959", "indices": [0]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3632959", "status": "cancelled"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W2611340", "status": "processed"},
                {"order_id": "#W3632959", "status": "processed"},
            ],
            {"order_id": "#W2611340", "removed_count": 2, "items_len": 0},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "status": "cancelled"},
            {"order_id": "#W3632959", "removed_count": 1, "items_len": 0},
            {"order_id": "#W3632959", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3632959", "status": "cancelled"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_090",
        instruction=(
            "Your task is to manage a comprehensive update for customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). You have two primary objectives. First, you need to finalize her pending order '#W9903153'. This involves substituting the item at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'), removing the item at index 2, reconciling the finances with a new 'payment' of $3321.66 using payment method 'credit_card_5869505', and updating the order's status to 'processed'. Second, you are to revise logistics for her delivered orders by changing the courier to 'SpeedWay Delivery' for tracking record '443521489581' and adding an 'info' event containing the note 'Delivery confirmation requested by user.' to tracking record '749747277477'."
        ),
        actions=[
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W9903153", "indices": [2]},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W9903153",
                    "transaction_type": "payment",
                    "amount": 3321.66,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "443521489581", "courier_name": "SpeedWay Delivery"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Delivery confirmation requested by user.",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
        ],
        outputs=[
            {"status": "success", "message": "Order #W9903153 was successfully modified in memory."},
            {"order_id": "#W9903153", "removed_count": 1, "items_len": 4},
            {"order_id": "#W9903153", "payment_history_len": 2},
            {"tracking_id": "443521489581", "courier_name": "SpeedWay Delivery"},
            {"tracking_id": "749747277477", "new_status": "info", "history_len": 1},
            {"order_id": "#W9903153", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_091",
        instruction=(
            "Your task is to coordinate a thorough account realignment for customer 'Mia Martinez' (user_id 'mia_martinez_3271') following the quarterly audit policy. As per the policy, you must handle her orders according to their current statuses. For her processed order '#W6310710', you must cancel the payment at index 0 and change its status back to 'pending'. For her pending order '#W6436609', you will also cancel the payment at index 0 but update its status to 'processed'. For her cancelled order '#W4140680', your responsibility is to reactivate it by reopening it, adding one 'Gaming Mouse' (product '5713490933', item '5796612084'), and applying a new 'payment' of $75.00 using method 'pm-anya-card-2'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "processed"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W6436609", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6436609", "status": "processed"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
        ],
        outputs=[
            [{"order_id": "#W6310710", "status": "processed"}],
            [{"order_id": "#W6436609", "status": "pending"}],
            [{"order_id": "#W4140680", "status": "cancelled"}],
            {"order_id": "#W6310710", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6310710", "status": "pending"},
            {"order_id": "#W6436609", "removed": True, "payment_history_len": 0},
            {"order_id": "#W6436609", "status": "processed"},
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "added_count": 1, "items_len": 4},
            {"order_id": "#W4140680", "payment_history_len": 3},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_092",
        instruction=(
            "Handle a comprehensive administrative assignment encompassing logistics and pricing. Start by arranging logistics for 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753') by updating two tracking entries: for '443521489581', modify the courier to 'RapidTransit Solutions' and append an 'info' event with the note 'First update complete'; for '749747277477', include an 'info' event with the note 'Second update started' and set its status to 'delivered'. Proceed to implement company-wide price adjustments for the 'Smartphone' (product '1801728040', item '5339029584') to 210.00 USD and the 'T-Shirt' (product '9523456873', item '9612497925') to 52.00 USD. Conclude by auditing the account of 'William Li' (user_id 'william_li_5688') by identifying all his processed orders and logging the financial details of each one located ('#W2611340' and '#W3632959')."
        ),
        actions=[
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "443521489581", "courier_name": "RapidTransit Solutions"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "First update complete",
                },
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Second update started",
                },
            ),
            Action(
                name="AdvanceTrackingStatus",
                kwargs={"tracking_id": "749747277477", "status": "delivered"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 210.00},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 52.00},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W2611340"},
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W3632959"},
            ),
        ],
        outputs=[
            {"tracking_id": "443521489581", "courier_name": "RapidTransit Solutions"},
            {"tracking_id": "443521489581", "new_status": "info", "history_len": 2},
            {"tracking_id": "749747277477", "new_status": "info", "history_len": 1},
            {"tracking_id": "749747277477", "new_status": "delivered", "history_len": 6},
            {"product_id": "1801728040", "item_id": "5339029584", "old_price": 1128.99, "new_price": 210.00},
            {"product_id": "9523456873", "item_id": "9612497925", "old_price": 50.88, "new_price": 52.00},
            [
                {"order_id": "#W2611340", "status": "processed"},
                {"order_id": "#W3632959", "status": "processed"},
            ],
            {"order_id": "#W2611340", "items_total": 0},
            {"order_id": "#W3632959", "items_total": 0},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_093",
        instruction=(
            "Coordinate the entire lifecycle management of the supply order '#SO9359', and then revise a related customer order in light of the new inventory. Begin by identifying the pending supply orders for supplier '#SUP0001' to understand the context. For order '#SO9359', progress it through the 'approved' and 'in_transit' stages, documenting each step with an 'info' type event using the messages 'Approved by management.' and 'Shipment departed from supplier facility.' respectively. Next, process the receipt of the order and close it. Once the 'Smartphone' stock is confirmed from this shipment, update the pending order '#W6436609' for customer 'Mia Martinez' (user_id 'mia_martinez_3271') by adding another 'Smartphone' (product '1801728040', item '5339029584'), applying a new 'payment' of $210.00 with method 'pm-anya-card-2', and finally marking the order as 'processed'."
        ),
        actions=[
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0001", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Approved by management.",
                },
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO9359", "status": "in_transit"},
            ),
            Action(
                name="AppendSupplyOrderEvent",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Shipment departed from supplier facility.",
                },
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO9359"},
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "pending"},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W6436609",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W6436609",
                    "transaction_type": "payment",
                    "amount": 210.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W6436609", "status": "processed"},
            ),
        ],
        outputs=[
            [{"supply_order_id": "#SO9359", "status": "pending"}],
            {"supply_order_id": "#SO9359", "status": "approved"},
            {"supply_order_id": "#SO9359", "events_len": 1},
            {"supply_order_id": "#SO9359", "status": "in_transit"},
            {"supply_order_id": "#SO9359", "events_len": 2},
            {"supply_order_id": "#SO9359", "status": "closed"},
            [{"order_id": "#W6436609", "status": "pending"}],
            {"order_id": "#W6436609", "added_count": 1, "items_len": 5},
            {"order_id": "#W6436609", "payment_history_len": 2},
            {"order_id": "#W6436609", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_094",
        instruction=(
            "Handle the task of consolidating and reconciling processed orders for customer 'William Li' (user_id 'william_li_5688'). Combine his order '#W3632959' into '#W2611340', ensuring all items and payments are transferred. In line with company policy, modify the consolidated order by substituting the item at index 2 with a 'Gaming Mouse' (product '5713490933', variant '5796612084'). Conclude with a comprehensive financial reconciliation: void the two merged payments at index 0 twice, then add a single new 'payment' reflecting the correct, final order total using payment method 'pm-james-card-1'. Make sure the order concludes in a 'processed' state."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "william_li_5688", "status": "processed"},
            ),
            Action(
                name="MergeOrdersForSameUser",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": True,
                },
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 2,
                    "product_id": "5713490933",
                    "item_id": "5796612084",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W2611340"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 695.54,
                    "payment_method_id": "pm-james-card-1",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2611340", "status": "processed"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W2611340", "status": "processed"},
                {"order_id": "#W3632959", "status": "processed"},
            ],
            {"target_order_id": "#W2611340", "source_order_id": "#W3632959", "target_items_len": 3, "source_status": "cancelled"},
            {"status": "success", "message": "Order #W2611340 was successfully modified in memory."},
            {"order_id": "#W2611340", "items_total": 695.54},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 1},
            {"order_id": "#W2611340", "removed": True, "payment_history_len": 0},
            {"order_id": "#W2611340", "payment_history_len": 1},
            {"order_id": "#W2611340", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_095",
        instruction=(
            "Oversee the multi-order update for customer 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753'). Begin by managing a product exchange in her order '#W9903153' by replacing the item at index 1 with a 'T-Shirt' (product '9523456873', item '8124970213'). Following this adjustment, orchestrate a batch status realignment on all appropriate pending orders as per the end-of-day policy: the updated order '#W9903153' should be 'processed', order '#W1620235' must be marked as 'delivered', order '#W2918688' is to be 'cancelled', and order '#W9655299' should stay 'pending'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "pending"},
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 1,
                    "product_id": "9523456873",
                    "item_id": "8124970213",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W9903153"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W1620235", "status": "delivered"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W2918688", "status": "cancelled"},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9655299", "status": "pending"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W9903153", "status": "pending"},
                {"order_id": "#W1620235", "status": "pending"},
                {"order_id": "#W2918688", "status": "pending"},
                {"order_id": "#W9655299", "status": "pending"},
            ],
            {"status": "success", "message": "Order #W9903153 was successfully modified in memory."},
            {"order_id": "#W9903153", "items_total": 3292.95},
            {"order_id": "#W9903153", "status": "processed"},
            {"order_id": "#W1620235", "status": "delivered"},
            {"order_id": "#W2918688", "status": "cancelled"},
            {"order_id": "#W9655299", "status": "pending"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_096",
        instruction=(
            "Your task is to handle a complex customer return and subsequent resale. Start by addressing a return from 'Aarav Lopez' (user_id 'aarav_lopez_9729') for his delivered order '#W5455653'. According to return policy, you must remove the 'DSLR Camera' at index 0, void the original payment at index 0, and apply an adjusted 'payment' of $371.27 using 'credit_card_2690859'. Next, coordinate the fulfillment of the pending order '#W7007896' for 'Ahmad Ahmed' (user_id 'ahmad_ahmed_6232'). To streamline this process, connect Aarav's tracking record ('632894717617') with Yusuf's order, log an 'info' event noting 'Shipment consolidated to include items for order #W7007896.', process Yusuf's 'payment' of $850.25 via 'credit_card_yusuf_ahmed_7745', and set the order status as 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "aarav_lopez_9729", "status": "delivered"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W5455653", "indices": [0]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W5455653", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W5455653",
                    "transaction_type": "payment",
                    "amount": 371.27,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "ahmad_ahmed_6232", "status": "pending"},
            ),
            Action(
                name="FindTrackingByOrder",
                kwargs={"order_id": "#W5455653"},
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W7007896", "tracking_id": "632894717617"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "632894717617",
                    "event_status": "info",
                    "note": "Shipment consolidated to include items for order #W7007896.",
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W7007896",
                    "transaction_type": "payment",
                    "amount": 850.25,
                    "payment_method_id": "credit_card_yusuf_ahmed_7745",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W7007896", "status": "processed"},
            ),
        ],
        outputs=[
            [{"order_id": "#W5455653", "status": "delivered"}],
            {"order_id": "#W5455653", "removed_count": 1, "items_len": 4},
            {"order_id": "#W5455653", "removed": True, "payment_history_len": 0},
            {"order_id": "#W5455653", "payment_history_len": 1},
            [{"order_id": "#W7007896", "status": "pending"}],
            {"tracking_id": ["632894717617"], "order_id": "#W5455653"},
            {"order_id": "#W7007896", "tracking_id": "632894717617", "fulfillments_len": 1},
            {"tracking_id": "632894717617", "new_status": "info", "history_len": 1},
            {"order_id": "#W7007896", "payment_history_len": 2},
            {"order_id": "#W7007896", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_097",
        instruction=(
            "Your goal is to manage a complex post-delivery exchange and its downstream effects for 'Olivia Rodriguez' (user_id 'olivia_rodriguez_9753') regarding her delivered order '#W3113816'. Begin by updating the order's logistics to show a return in progress. Modify the tracking record ('443521489581') by changing the courier to 'Returns Department' and adding a 'checkpoint' note with 'Return initiated by customer'. Proceed to handle the exchange by replacing the 'Dumbbell Set' at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'). Subsequently, conduct a full financial reconciliation by voiding the payment at index 0 and applying a new 'payment' totaling $1885.83 using 'credit_card_5869505'. To finalize the fulfillment of the replacement item, link the tracking ID '749747277477' from her other delivered order '#W1539823', add an 'info' note saying 'Replacement item dispatched under new tracking', and change the order status to 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "olivia_rodriguez_9753", "status": "delivered"},
            ),
            Action(
                name="UpdateTrackingCourier",
                kwargs={"tracking_id": "443521489581", "courier_name": "Returns Department"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "checkpoint",
                    "note": "Return initiated by customer",
                },
            ),
            Action(
                name="ReplaceItemVariantInOrder",
                kwargs={
                    "order_id": "#W3113816",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W3113816"},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W3113816",
                    "transaction_type": "payment",
                    "amount": 1885.83,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="FindTrackingByOrder",
                kwargs={"order_id": "#W1539823"},
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W3113816", "tracking_id": "749747277477"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Replacement item dispatched under new tracking",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3113816", "status": "processed"},
            ),
        ],
        outputs=[
            [{"order_id": "#W3113816"}, {"order_id": "#W1539823"}],
            {"tracking_id": "443521489581", "courier_name": "Returns Department"},
            {"tracking_id": "443521489581", "new_status": "checkpoint"},
            {"status": "success", "message": "Order #W3113816 was successfully modified in memory."},
            {"order_id": "#W3113816", "items_total": 1885.83},
            {"order_id": "#W3113816", "removed": True},
            {"order_id": "#W3113816", "payment_history_len": 1},
            {"tracking_id": ["749747277477"], "order_id": "#W1539823"},
            {"order_id": "#W3113816", "tracking_id": "749747277477", "fulfillments_len": 2},
            {"tracking_id": "749747277477", "new_status": "info"},
            {"order_id": "#W3113816", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_098",
        instruction=(
            "Handle the supply chain control for the 'Gaming Mouse' (product '5713490933', variant '8214883393') from supplier '#SUP0002' and apply flexible pricing strategies. Approve the priority supply order '#SO6035' while you cancel the non-essential one ('#SO7848'). Following your approval, adjust the product's price to respond to market fluctuations, initially raising it to 85.00 USD. Once the receipt of the approved supply order is processed, implement a sales strategy by reducing the price to 78.00 USD. Finally, log the details of a customer order ('#W3113816') that includes this item by obtaining its financial specifics."
        ),
        actions=[
            Action(
                name="FindSupplyOrders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="SetSupplyOrderStatus",
                kwargs={"supply_order_id": "#SO7848", "status": "cancelled"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 85.00},
            ),
            Action(
                name="ReceiveSupplyOrderAndClose",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="UpdateProductVariantPrice",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 78.00},
            ),
            Action(
                name="GetOrderFinancials",
                kwargs={"order_id": "#W3113816"},
            ),
        ],
        outputs=[
            [
                {"supply_order_id": "#SO6035", "status": "pending"},
                {"supply_order_id": "#SO7848", "status": "pending"},
            ],
            {"supply_order_id": "#SO6035", "status": "approved"},
            {"supply_order_id": "#SO7848", "status": "cancelled"},
            {"product_id": "5713490933", "item_id": "8214883393", "old_price": 150.58, "new_price": 85.00},
            {"supply_order_id": "#SO6035", "status": "closed"},
            {"product_id": "5713490933", "item_id": "8214883393", "old_price": 85.00, "new_price": 78.00},
            {"order_id": "#W3113816", "items_total": 0},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_099",
        instruction=(
            "Coordinate a thorough account archival for customer 'Sofia Hernandez' (user_id 'sofia_hernandez_5364'). The archival guidelines mandate archiving all non-essential orders. Handle her pending order '#W9609649' by removing its 5 items (indices 0-4) and its payment at index 0, then change the status to 'cancelled'. Apply the same archival methodology to her other pending order '#W3561391' by removing its 1 item (index 0) and its payment at index 0 before marking it as cancelled. Conclude by archiving her processed order '#W5765741' by eliminating its 2 items (indices 0-1) and its payment at index 0, setting it to 'cancelled'."
        ),
        actions=[
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W9609649", "indices": [0, 1, 2, 3, 4]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W9609649", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W9609649", "status": "cancelled"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W3561391", "indices": [0]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W3561391", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W3561391", "status": "cancelled"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W5765741", "indices": [0, 1]},
            ),
            Action(
                name="RemovePaymentByIndex",
                kwargs={"order_id": "#W5765741", "index": 0},
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W5765741", "status": "cancelled"},
            ),
        ],
        outputs=[
            {"order_id": "#W9609649", "removed_count": 5, "items_len": 0},
            {"order_id": "#W9609649", "removed": True, "payment_history_len": 0},
            {"order_id": "#W9609649", "status": "cancelled"},
            {"order_id": "#W3561391", "removed_count": 1, "items_len": 0},
            {"order_id": "#W3561391", "removed": True, "payment_history_len": 0},
            {"order_id": "#W3561391", "status": "cancelled"},
            {"order_id": "#W5765741", "removed_count": 2, "items_len": 0},
            {"order_id": "#W5765741", "removed": True, "payment_history_len": 0},
            {"order_id": "#W5765741", "status": "cancelled"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_100",
        instruction=(
            "Your aim is to reinstate and complete a cancelled order for 'Mia Martinez' (user_id 'mia_martinez_3271'). Reopen order '#W4140680' and fully replace its contents. Remove all three original items and proceed to add two new items: a 'Smart Watch' (product '6945232052', variant '9408160950') and a 'T-Shirt' (product '9523456873', variant '8124970213'). Once the items are updated, reconcile the payment by implementing a 'payment' transaction of $289.98 using her payment method 'pm-anya-card-1'. For fulfillment, associate the tracking ID '951786982868' from her order '#W6310710' and insert an 'info' type event with the precise note 'New items added to shipment'. Lastly, confirm that the order is marked as 'processed'."
        ),
        actions=[
            Action(
                name="FindOrdersByUserAndStatus",
                kwargs={"user_id": "mia_martinez_3271", "status": "cancelled"},
            ),
            Action(
                name="ReopenCancelledOrder",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="RemoveItemsByIndex",
                kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]},
            ),
            Action(
                name="AddItemsToOrder",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [
                        {"product_id": "6945232052", "item_id": "9408160950", "quantity": 1},
                        {"product_id": "9523456873", "item_id": "8124970213", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="AppendPayment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 289.98,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="LinkExistingTrackingToOrder",
                kwargs={"order_id": "#W4140680", "tracking_id": "951786982868"},
            ),
            Action(
                name="AddTrackingCustomEvent",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "New items added to shipment",
                },
            ),
            Action(
                name="SetOrderStatus",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
        ],
        outputs=[
            [
                {"order_id": "#W4140680", "status": "cancelled"}
            ],
            {"order_id": "#W4140680", "status": "pending"},
            {"order_id": "#W4140680", "removed_count": 3, "items_len": 0},
            {"order_id": "#W4140680", "added_count": 2, "items_len": 2},
            {"order_id": "#W4140680", "payment_history_len": 3},
            {"order_id": "#W4140680", "tracking_id": "951786982868", "fulfillments_len": 2},
            {"tracking_id": "951786982868", "new_status": "info", "history_len": 1},
            {"order_id": "#W4140680", "status": "processed"},
        ],
    ),
]
