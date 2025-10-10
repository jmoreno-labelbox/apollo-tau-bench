from domains.dto import Action, Task

TASKS = [
    Task(
        annotator="1",
        user_id="user_119",
        instruction=(
            "Your objective is to manage a multi-stage supply chain process and apply its results to a customer order. "
            "You must first process the pending supply order '#SO9359' for supplier '#SUP0001'. You will advance it to 'approved', then 'in_transit', and finally process its receipt and closure, logging an 'info' event with the message 'Shipment received and verified' upon approval. "
            "After this 'T-Shirt' stock is confirmed, you must apply two sequential price updates to the variant ('product '9523456873', item '9612497925'): first an increase to $55.00, and then a promotional decrease to $49.99. "
            "Finally, you will modify the pending order '#W7007896' for customer 'Yusuf Ahmed' (user_id 'yusuf_ahmed_6232') by replacing the item at index 0 with this newly priced T-Shirt and voiding the payment at index 0."
        ),
        actions=[
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0001", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Shipment received and verified",
                },
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "in_transit"},
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO9359"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 49.99},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W7007896",
                    "index": 0,
                    "product_id": "9523456873",
                    "item_id": "9612497925",
                },
            ),
            Action(
                name="remove_payment_by_index",
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
            "Your objective is to manage a multi-faceted account update for customers 'Sofia Hernandez' (user_id 'sofia_hernandez_5364') and 'Anya Garcia' (user_id 'anya_garcia_3271'). "
            "For Sofia Hernandez, your goal is to process an update on her 'processed' order '#W9609649'. You must void the payment at index 0, add one 'Patio Umbrella' (product '9743693396', item '8170914468'), apply a new 'payment' of $750.00 using 'pm-sofia-card-3', and set its final status to 'delivered'. "
            "For Anya Garcia, your goal is to reactivate her 'cancelled' order '#W4140680' and prepare it for a consolidated shipment. You will reopen the order, and then link the existing tracking ID from her 'processed' order '#W6310710' to it. Finally, you will log an 'info' event with the note 'Order consolidated for shipment' on the shared tracking record and set the reopened order's status to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "sofia_hernandez_5364", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W9609649", "index": 0}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W9609649",
                    "transaction_type": "payment",
                    "amount": 750.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W9609649", "status": "delivered"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="find_tracking_by_order",
                kwargs={"order_id": "#W6310710"},
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W4140680", "tracking_id": "951786982868"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Order consolidated for shipment",
                },
            ),
             Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your task is to manage a full product lifecycle, from supply chain to pricing and final sale. "
            "First, you must oversee the replenishment of 'T-Shirt' stock by managing supply order '#SO7848' for supplier '#SUP0002': you will approve it, log an 'info' event 'Stock replenished for campaign', and process its receipt. "
            "Following this, your goal is a company-wide price update: set the 'T-Shirt' (product '9523456873', item '9612497925') to 49.99 USD and the 'Portable Charger' (product '6942297802', item '7903094618') to 89.99 USD. "
            "Finally, you must apply these changes to a customer order. For 'Mei Kovacs' (user_id 'mei_kovacs_5767') on her pending order '#W8193638', you will first apply a service 'payment' of 15.00 USD using method 'pm_mei_kovacs_card_1'. "
            "Then, you must replace the original item at index 0 with the newly priced 'T-Shirt' and 'Portable Charger'. "
            "To complete the fulfillment, you will link tracking ID '951786982868', add an 'info' event with note 'Order updated with new products and pricing', and set the order status to 'processed'."
        ),
        actions=[
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO7848", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO7848",
                    "event_type": "info",
                    "message": "Stock replenished for campaign",
                },
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO7848"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 49.99},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "6942297802", "item_id": "7903094618", "new_price": 89.99},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W8193638",
                    "transaction_type": "payment",
                    "amount": 15.00,
                    "payment_method_id": "pm_mei_kovacs_card_1",
                },
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W8193638", "indices": [0]},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [
                        {"product_id": "9523456873", "item_id": "9612497925", "quantity": 1},
                        {"product_id": "6942297802", "item_id": "7903094618", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W8193638", "tracking_id": "951786982868"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Order updated with new products and pricing",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to manage the downstream effects of a customer return. "
            "You must first process a return for 'Aarav Sanchez' (user_id 'aarav_sanchez_9729') on his delivered order '#W5455653' by cancelling it and issuing a full 'refund' of $1221.52 to payment method 'credit_card_2690859'. "
            "This return affects inventory levels, so you must then manage the supply chain. You will find the pending supply order '#SO6035' for the returned item's supplier ('#SUP0002') and approve it with an 'info' event note 'Approved to restock after customer return'. "
            "After processing the receipt of this supply order, you must apply a price update to the restocked 'Gaming Mouse' (product '5713490933', item '8214883393'), setting its new price to $82.50. "
            "Finally, you must reconcile the finances on a different customer's ('Emma Santos', user_id 'emma_santos_9753') delivered order '#W3113816', which was affected by the price change, by voiding the payment at index 0 and applying a new 'payment' of $1450.00 using method 'credit_card_5869505'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "aarav_sanchez_9729", "status": "delivered"},
            ),
            Action(
                name="cancel_order_and_refund",
                kwargs={
                    "order_id": "#W5455653",
                    "refund_amount": 1221.52,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Approved to restock after customer return",
                },
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 82.50},
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W3113816"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="append_payment",
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
            "Your objective is to perform a full account archival for 'James Li' (user_id 'james_li_5688') and manage the downstream impact. "
            "The archival policy requires that all of his 'processed' orders ('#W2611340', '#W3632959') be cleared by removing all items and the primary payment at index 0, and then setting their status to 'cancelled'. "
            "Because this archival action returns a 'Smartphone' to stock, you must then cancel the now-redundant pending supply order '#SO9359' for that item and log an 'info' event with the message 'Cancelled: stock returned from customer order #W2611340'. "
            "Finally, you are to resolve a separate pending order '#W9609649' for 'Sofia Hernandez' by cancelling it as well."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W2611340", "indices": [0, 1]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "cancelled"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W3632959", "indices": [0]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3632959", "status": "cancelled"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "cancelled"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Cancelled: stock returned from customer order #W2611340",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your task is to prepare James Li's account for a new audit. "
            "You need to reset both of his orders, '#W2611340' and '#W3632959', by stripping their initial payment data and moving them to a 'pending' state for review."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Both of James Li's orders, #W2611340 and #W3632959, had their initial payments removed and their statuses set to pending as part of the audit preparation."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_002",
        instruction=(
            "Your objective is to conduct a full account audit for customers 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "Your task is to implement the audit policy across all of their orders. The policy requires you to first perform a financial reset by voiding the primary payment at index 0 from every single order associated with both users. "
            "For any order that is 'cancelled', you must reactivate it before voiding the payment. "
            "Following the financial reset, you must realign the order statuses: all of Anya Garcia's orders ('#W6310710', '#W6436609', '#W4140680') must be set to 'processed', while James Li's order '#W2611340' must be set to 'pending'. No other status changes are required for James Li's other orders."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "cancelled"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
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
            "Your goal is to perform a targeted account cleanup. "
            "For Anya Garcia, you need to bring her inactive order '#W4140680' fully online with a 'processed' status, "
            "and simultaneously perform a financial reset on order '#W6310710' by removing its payment record at index 0. "
            "For James Li, your task is to move order '#W3632959' into a 'pending' state for further review."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
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
            "You are assigned to conduct a high-level status reconciliation. "
            "Your objective for James Li is to prepare his account for audit: move order '#W3632959' to a 'pending' state "
            "and strip the payment data at index 0 from order '#W2611340'. "
            "For Anya Garcia, your goal is to resolve the status of her inactive order '#W4140680' by reopening it "
            "and marking it as 'processed'."
        ),
        actions=[
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "You are to execute a system-wide audit for a new fiscal period for customers Anya Garcia and James Li. "
            "The audit policy states that all active orders ('#W6310710', '#W2611340', '#W3632959') must be financially reset and moved to a reviewable 'pending' state. "
            "As a separate case, Anya Garcia's inactive order '#W4140680' needs to be fully reactivated and finalized as 'processed'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your final task for this quarter is to perform a comprehensive account closure and reset process for customers Anya Garcia and James Li. "
            "For all of their currently active orders ('#W6310710', '#W2611340', '#W3632959'), your objective is to strip the initial payment data and reset their status to 'pending' to prepare them for the new fiscal period. "
            "Conversely, for Anya Garcia's cancelled order '#W4140680', your goal is to fully reactivate it, leaving it in a 'processed' state."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your task is to finalize the monthly order records for our key customers, James Li and Anya Garcia, by performing a series of status updates and financial adjustments. "
            "For James Li, you need to prepare his orders for archival: address order '#W2611340' by removing its initial payment and setting it to a 'pending' state. You must also adjust order '#W3632959' by removing its payment. "
            "For Anya Garcia, your goal is to resolve her account's only inactive order, '#W4140680', by bringing it back online and ensuring it is left in a 'processed' state."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "For James Li, order #W2611340 had its payment removed and was set to pending, while order #W3632959 also had its payment removed. For Anya Garcia, order #W4140680 was reopened and set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_008",
        instruction=(
            "You are in charge of a system-wide payment reconciliation. "
            "Your objective is to perform a financial reset on all active orders ('#W6310710', '#W2611340', '#W3632959') "
            "by removing the first payment in each order (index 0). "
            "Following this reset, the account policy requires that order '#W6310710' be moved to a 'pending' state. "
            "Separately, you must resolve the status of Anya Garcia's inactive order '#W4140680' by reopening it and "
            "setting it to 'processed'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
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
            "You are conducting a pre-audit cleanup for customers Anya Garcia and James Li. "
            "The audit policy requires that their active orders ('#W2611340' and '#W6310710') are financially reset and placed in a 'pending' state for review. "
            "For Anya Garcia's dormant order '#W4140680', your objective is different: it needs to be fully restored to a 'processed' state."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your final task is a quarterly account reconciliation for our primary customers. "
            "For Anya Garcia, you need to fully reactivate her cancelled order '#W4140680' and ensure it ends in a 'processed' state. "
            "You must also prepare her active order '#W6310710' for auditing by removing its payment record at index 0 and moving it to 'pending'. "
            "For James Li, your objective is to close out his active order '#W2611340' for the quarter by performing a financial reset on this order by removing its payment record at index 0 and then setting its status to 'processed'."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
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
            "You are preparing all customer orders for a system-wide data migration. "
            "The migration policy requires you to financially cleanse and then reset the status for all active orders. "
            "Specifically, standard active orders ('#W6310710', '#W2611340') should have their payment record at index 0 removed "
            "and end in a 'pending' state, while order '#W3632959' must have its payment record at index 0 removed and be fully archived with a 'cancelled' status. "
            "You must also handle the special case of Anya Garcia's inactive order '#W4140680' by ensuring it is reactivated and finalized as 'processed' for the migration."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "cancelled"}
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
            "You are an operations assistant performing a full financial reconciliation for key customers. "
            "Your objective is to reset the financial records for all active orders for James Li ('#W2611340', '#W3632959') and Anya Garcia ('#W6310710') by removing their initial payment data. "
            "Following the financial reset, you must ensure that both of James Li's orders are updated to a 'pending' status."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "A full financial reconciliation was completed. The initial payments for orders #W2611340, #W3632959, and #W6310710 were removed. Both of James Li's orders were then set to a 'pending' status."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_013",
        instruction=(
            "You need to perform a critical account cleanup for James Li and Anya Garcia. "
            "For James Li, your task is to reset his two orders, '#W2611340' and '#W3632959', by removing their initial payment records and then setting their statuses to 'processed'. "
            "For Anya Garcia, you must reactivate her cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[
            "Critical account cleanup completed. James Li's orders #W2611340 and #W3632959 had their payments removed and were set to processed. Anya Garcia's order #W4140680 was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_014",
        instruction=(
            "Your task is to handle two urgent customer requests. "
            "For customer Anya Garcia, you must reactivate her cancelled order '#W4140680' and ensure its status is 'processed'. "
            "For James Li, you need to prepare his orders '#W2611340' and '#W3632959' for a new audit by removing the initial payment from both orders and resetting their status to 'pending'."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Anya Garcia's order #W4140680 was reopened and processed. James Li's orders #W2611340 and #W3632959 were prepared for audit by removing payments and setting their statuses to pending."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_015",
        instruction=(
            "You are tasked with a full account cleanup for James Li and Anya Garcia. "
            "The objective for James Li is to reset his orders '#W2611340' and '#W3632959' by removing their payment record at index 0 "
            "and setting them to a 'processed' state. "
            "For Anya Garcia, you must resolve a billing issue on her active order '#W6310710' by removing its payment record at index 0 "
            "and also reactivate her cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
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
            "You are tasked with preparing customer accounts for a new audit. "
            "For Anya Garcia, your goal is to reactivate her cancelled order '#W4140680' and ensure it is in a 'processed' state, while also adding a new standard item (product '1801728040', variant '5339029584') to it. "
            "For James Li, you need to financially reset his orders '#W2611340' and '#W3632959' by removing their initial payment records and then moving them to a 'pending' state for review."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Anya Garcia's order #W4140680 was reopened, processed, and had a new item added. James Li's orders #W2611340 and #W3632959 were prepared for audit by removing payments and setting their statuses to pending."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_017",
        instruction=(
            "Your assignment is to prepare all orders for a new sales campaign launch. "
            "The preparation protocol requires a financial reset and status alignment. "
            "For every active order associated with Anya Garcia ('#W6310710') and James Li ('#W2611340', '#W3632959'), "
            "you must clear the first payment record (index 0) and then set their status to 'processed'. "
            "You also need to address Anya Garcia's dormant order '#W4140680', which must be reactivated and marked as 'processed'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "You are executing a data integrity and segmentation task. Your objective is to audit and reset all orders for our primary customers. "
            "The audit policy requires a financial reset for all active orders ('#W6310710', '#W2611340', '#W3632959') by removing the payment record at index 0 from each. "
            "After the reset, you need to segment them by status: high-priority orders '#W2611340' and '#W3632959' should be moved to 'processed', while order '#W6310710' is to be marked as 'pending' for review. "
            "As always, Anya Garcia's inactive order '#W4140680' must be reactivated and finalized in a 'processed' state."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your task is to perform a major account consolidation. You need to process every order for Anya Garcia and James Li. "
            "The consolidation rule requires that all payment records be stripped from their active orders ('#W6310710', '#W2611340', '#W3632959') by removing the payment record at index 0 from each. "
            "Following this, you are to unify the status of all these active orders to 'pending'. "
            "Your final step is to ensure Anya Garcia's cancelled order '#W4140680' is brought back to an active, 'processed' state."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "You are conducting the final cleanup for the quarter. Your goal is to standardize all customer orders. "
            "You must clear the payment record from every active order for Anya Garcia ('#W6310710') and James Li ('#W2611340', '#W3632959'). "
            "The cleanup policy then requires that you update the status for all of James Li's orders to 'processed', while setting Anya Garcia's active order to 'pending'. "
            "You also need to ensure her inactive order '#W4140680' is reopened and left as 'processed'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "Quarterly cleanup finished. All active orders were financially reset. James Li's orders were set to processed, and Anya Garcia's active order was set to pending. Her inactive order was reopened and processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_021",
        instruction=(
            "Your responsibility is to execute a multi-part audit for customers 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "For Anya, your goal is twofold: you must first restore her cancelled order '#W4140680' by reopening it and adding two units of the standard Smartphone (product '1801728040', item '5339029584'). Second, you will process her processed order '#W6310710' by voiding its payment at index 0. "
            "For James Li, the audit policy requires you to process all of his 'processed' and 'delivered' orders. For each of these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), you must replace the item at index 0 with the standard Smartphone and void the payment at index 0. "
            "After the audit, you are to set the status of all four of his orders to 'pending' for review."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 2}],
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W4435622",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
             Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3638028",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
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
            "You are to perform a complete audit and status reset for all orders associated with customers Anya Garcia and James Li. "
            "Your objective is to reactivate Anya Garcia's inactive order '#W4140680' and finalize it as 'processed'. "
            "For all other active orders ('#W6310710', '#W2611340', '#W3632959'), the audit policy requires that you clear their initial payment records and then update their statuses: orders '#W6310710' and '#W3632959' should be moved to a 'pending' state, while order '#W2611340' must be set to 'processed'."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "A full audit and status reset was completed. Inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) had their payments cleared and statuses updated according to the audit policy."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_023",
        instruction=(
            "Your objective is to conduct an account audit for James Li (user_id 'james_li_5688') and Anya Garcia (user_id 'anya_garcia_3271'). "
            "For James Li, the audit policy requires you to process all of his 'processed' and 'delivered' orders. For each of these orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), you must clear the financial record at index 0 and then set the order's status to 'pending'. "
            "For Anya Garcia, the policy requires you to reactivate her 'cancelled' order '#W4140680' and ensure it is marked as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "You are tasked with a system-wide reconciliation. "
            "The company policy requires you to perform a financial reset on all active orders for James Li ('#W2611340', '#W3632959') and Anya Garcia ('#W6310710') by clearing their primary payment records. "
            "Additionally, you must reactivate Anya Garcia's dormant order '#W4140680' and then finalize its status as 'processed'."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[
            "A system-wide reconciliation was performed. The payment records for all active orders (#W2611340, #W3632959, #W6310710) were cleared. Anya Garcia's dormant order #W4140680 was reactivated and processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_025",
        instruction=(
            "You are to perform a complete financial reset for the new quarter. "
            "Your primary objective is to clear the payment records at index 0 from all active orders "
            "(#W6310710, #W2611340, #W3632959) for customers Anya Garcia and James Li, "
            "and then move each of these orders into a 'pending' state for re-evaluation. "
            "Your final task is to reactivate Anya Garcia's dormant order #W4140680."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
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
            "Your task is a large-scale account cleanup and order enhancement project for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "For Anya Garcia, you must prepare her active order '#W6310710' for archival by clearing its "
            "financial and item data and placing it in a 'pending' state. You also need to reactivate her "
            "dormant order '#W4140680' and process a new payment for it for 75.00 USD via 'pm-anya-card-6'. "
            "For James Li, your objective is to enhance his active order '#W2611340' by replacing its first "
            "item with the standard Smartphone variant (product '1801728040', item_id '5339029584'), adding "
            "a second unit of the same, appending a new payment of 300.00 USD via 'pm-james-card-5', and "
            "finalizing the order as 'processed'."
        ),
        actions=[
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W6310710", "indices": [0]},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [
                        {"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}
                    ],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 300.00,
                    "payment_method_id": "pm-james-card-5",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "processed"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-6",
                },
            ),
        ],
        outputs=[
            "For Anya Garcia, order #W6310710 was prepared for archival and order #W4140680 was reactivated with a new payment. "
            "For James Li, order #W2611340 was enhanced with item and payment updates and then processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_027",
        instruction=(
            "You must perform the end-of-quarter account review for customers Anya Garcia (user_id 'anya_garcia_3271') "
            "and James Li (user_id 'james_li_5688'). According to the review policy, you are required to financially "
            "reset all active orders (#W6310710, #W2611340, #W3632959) by clearing their primary payment records. "
            "After the reset, update their statuses as specified in the EOD plan: mark orders #W6310710 and #W3632959 "
            "as 'pending', and for order #W2611340, mark it as 'processed' before finalizing it as 'pending'. "
            "Additionally, resolve the status of Anya Garcia's inactive order #W4140680 by reactivating it and ensuring "
            "it remains in a 'processed' state."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_028",
        instruction=(
            "Your task is to perform a system-wide financial reset for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The company policy requires that you clear the primary payment record from all of their orders that are currently in a 'pending', 'processed', or 'delivered' state. "
            "For any order that is inactive (i.e., 'cancelled'), you must first reactivate it, at which point it also becomes subject to this financial reset policy. "
            "After all financial records are cleared, you are to finalize the statuses: all of James Li's orders must be moved to 'pending', and Anya Garcia's previously inactive order should be marked 'processed'."
        ),
        actions=[
            Action(name="find_orders_by_user_and_status", kwargs={"user_id": "anya_garcia_3271"}),
            Action(name="find_orders_by_user_and_status", kwargs={"user_id": "james_li_5688"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[
            "A system-wide financial reset was performed. All active and reactivated orders for both customers had their primary payment records cleared. The final statuses were set according to policy: James Li's orders were set to pending, and Anya Garcia's reactivated order was set to processed."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_029",
        instruction=(
            "Your task is the end-of-quarter account review for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The review policy requires that you financially reset all active orders ('#W6310710', '#W2611340', '#W3632959') by clearing their primary payment records. "
            "After the reset, you must update their statuses per the EOD plan: '#W6310710' and '#W3632959' are to be marked 'pending', while '#W2611340' must first be marked 'processed' before being finalized as 'pending'. "
            "Finally, you are to resolve the status of Anya Garcia's inactive order '#W4140680' by ensuring it is reactivated and left in a 'processed' state."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
        ],
        outputs=[
            "End-of-quarter review is complete. Anya Garcia's inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) were financially reset and their statuses updated according to the EOD plan."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_030",
        instruction=(
            "You are tasked with a complete audit and status reset for all orders associated with customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The audit policy requires that you clear the initial payment records from all active orders ('#W6310710', '#W2611340', '#W3632959'). "
            "Following this, you must update their statuses: orders '#W6310710' and '#W3632959' should be moved to a 'pending' state, while order '#W2611340' must be set to 'processed'. "
            "As a separate case, you must reactivate Anya Garcia's dormant order '#W4140680' and finalize its status as 'processed'."
        ),
        actions=[
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "Full audit and status reset is complete. Inactive order #W4140680 was reactivated and processed. All active orders (#W6310710, #W2611340, #W3632959) had their payments cleared and statuses updated according to the audit policy."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_031",
        instruction=(
            "You must execute the new financial year-end policy for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The policy mandates a financial reset for all orders currently in a 'pending', 'processed', or 'delivered' state. "
            "This reset requires you to clear the primary payment record (index 0) from each of these orders: "
            "#W6310710, #W6436609, #W2611340, #W3632959, #W4435622, and #W3638028. "
            "After the reset, set orders '#W6310710', '#W6436609', and '#W2611340' to a 'pending' state for final review, "
            "while ensuring order '#W3632959' is marked as 'processed'. "
            "Do not modify any other orders."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W6436609", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
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
            "You are tasked with a system-wide data integrity audit for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The audit policy requires you to perform a full financial reset on every order that has a status of "
            "'pending', 'processed', or 'delivered' by clearing its primary payment record. "
            "After this financial reset is complete, you must standardize the status of all of James Li's orders to 'processed' "
            "and all of Anya Garcia's applicable orders to 'pending'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4435622", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3638028", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W6436609", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_033",
        instruction=(
            "You are to execute a price update directive and a corresponding account audit for customers "
            "'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "First, the company has mandated a price change: you must update the price for the standard Smartphone variant "
            "(product_id '1801728040', item_id '5339029584') to 105.50 USD. "
            "Following the price update, you must conduct an audit. Find all of James Li's orders with status 'pending', 'processed', or 'delivered'. For each of these orders, you are to clear the primary payment record (index 0) and place them in a 'pending' state. "
            "For Anya Garcia, find her cancelled order and reactivate it, finalizing its status as 'processed'."
        ),
        actions=[
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 105.50},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "You are to perform a complete overhaul of all four customer orders. "
            "For customer Anya Garcia (user_id 'anya_garcia_3271'), her active order '#W6310710' must have its primary item updated to the standard Smartphone variant (product '1801728040', item_id '5339029584') and its payment record cleared. Her cancelled order '#W4140680' must be reactivated. "
            "For customer James Li (user_id 'james_li_5688'), both of his active orders ('#W2611340', '#W3632959') must also have their primary items updated to the standard variant and their payment records cleared. "
            "Following these changes, you must set the status of all three active orders ('#W6310710', '#W2611340', '#W3632959') to 'pending'."
        ),
        actions=[
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "All four orders were overhauled. All three active orders had their primary item replaced and payment record cleared before being set to 'pending'. The cancelled order was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_035",
        instruction=(
            "You are to perform a complete overhaul of all four customer orders. "
            "For customer Anya Garcia (user_id 'anya_garcia_3271'), her active order '#W6310710' must have its primary item updated to the standard Smartphone variant (product '1801728040', item_id '5339029584') and its payment record cleared. Her cancelled order '#W4140680' must be reactivated. "
            "For customer James Li (user_id 'james_li_5688'), both of his active orders ('#W2611340', '#W3632959') must also have their primary items updated to the standard variant and their payment records cleared. "
            "Following these changes, you must set the status of all three active orders ('#W6310710', '#W2611340', '#W3632959') to 'pending'."
        ),
        actions=[
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[
            "All four orders were overhauled. All three active orders had their primary item replaced and payment record cleared before being set to 'pending'. The cancelled order was reactivated."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_036",
        instruction=(
            "You are to execute a system-wide data standardization project for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The company policy requires that for every order currently in a 'processed' state for these customers, you must standardize its primary item to the Smartphone variant (product '1801728040', item_id '5339029584') and also clear its initial payment record."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
        ],
        outputs=[
            "System-wide data standardization is complete. For all 'processed' orders belonging to the specified customers, the primary item was updated to the standard variant and the initial payment record was cleared."
        ],
    ),
    Task(
        annotator="1",
        user_id="user_037",
        instruction=(
            "You are tasked with a large-scale order enhancement project for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The project requires you to add a new standard Smartphone item (product '1801728040', item_id '5339029584') with quantity 1 to all of their active orders ('#W6310710', '#W2611340', '#W3632959'). "
            "Concurrently, you must process a new payment of 100.00 USD for each of these three orders, using payment methods 'pm-anya-card-1', 'pm-james-card-1', and 'pm-james-card-2' respectively. "
            "Finally, you must reactivate Anya's dormant order '#W4140680' and also add a standard Smartphone to it."
        ),
        actions=[
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W6310710",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-james-card-1",
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W3632959",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W3632959",
                    "transaction_type": "payment",
                    "amount": 100.00,
                    "payment_method_id": "pm-james-card-2",
                },
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
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
            "Your objective is to perform a full archival preparation for active orders for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The archival policy requires that you clear all items and the primary payment at index 0 from each specified active order. For order '#W6310710', you will remove one item (index 0). For order '#W2611340', you will remove two items (indices 0, 1). For order '#W3632959', you will remove one item (index 0). "
            "After clearing them, you must set all three orders to a 'pending' state. As a final step, your task is to reactivate Anya Garcia's cancelled order '#W4140680'."
        ),
        actions=[
            Action(name="remove_items_by_index", kwargs={"order_id": "#W6310710", "indices": [0]}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(
                name="remove_items_by_index", kwargs={"order_id": "#W2611340", "indices": [0, 1]}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_items_by_index", kwargs={"order_id": "#W3632959", "indices": [0]}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
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
            "You are executing a customer retention project for Anya Garcia (user_id 'anya_garcia_3271') "
            "and James Li (user_id 'james_li_5688'). "
            "Add a complimentary standard Smartphone (product_id '1801728040', item_id '5339029584', quantity 1) "
            "to each of their orders with status 'processed' or 'pending'. "
            "For all of James Li's applicable orders, remove the payment record at index 0 as a goodwill gesture. "
            "For each of Anya Garcia's 'processed' orders, append a service payment of exactly 10.00 USD using payment_method_id 'pm-anya-card-1'. "
            "If Anya Garcia has any orders with status 'cancelled', reopen them, add the complimentary smartphone, "
            "and set them to 'processed'. Use exactly the provided user_ids, product_ids, item_ids, order_ids, statuses, "
            "and index values without modification."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W6310710",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W6436609",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 10.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W2611340",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W3632959",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_040",
        instruction=(
            "Your task is a system-wide price update and corresponding financial audit for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "Execute a mandated price change for the standard Smartphone variant "
            "(product_id '1801728040', item_id '5339029584'), setting its new price to 115.00 USD. "
            "For orders '#W2611340' and '#W6310710', remove the payment record at index 0 "
            "and set their statuses to 'processed'. "
            "For order '#W3632959', remove the payment record at index 0. "
            "Finally, reactivate Anya Garcia's cancelled order '#W4140680'. "
            "Use exactly the provided order_ids, product_ids, item_ids, statuses, and index values without modification."
        ),
        actions=[
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 115.00},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_041",
        instruction=(
            "Your objective is to execute a system-wide data standardization project for customers 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "Your first goal is to apply a data policy to all of their 'processed' orders. For each of these orders ('#W6310710', '#W2611340', '#W3632959'), you must update the item at index 0 to be the standard Smartphone variant (product '1801728040', item '5339029584'). "
            "Your second goal is to conduct an audit by clearing the payment record at index 0 from all three of these processed orders. "
            "As a final administrative action, you are required to reactivate Anya Garcia's 'cancelled' order '#W4140680' and ensure its status is finalized as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3632959",
                    "index": 0,
                    "product_id": "1801728040",
                    "item_id": "5339029584",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
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
            "Your objective is to conduct a full account audit for customers 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "Your task is to implement the audit policy across all of their orders. The policy requires you to first perform a financial reset by voiding the primary payment at index 0 from every single order associated with both users. "
            "For any order that is 'cancelled', you must reactivate it before voiding the payment. "
            "Following the financial reset, you must realign the order statuses: all of Anya Garcia's orders ('#W6310710', '#W6436609', '#W4140680') must be set to 'processed', while James Li's order '#W2611340' must be set to 'pending'. No other status changes are required for James Li's other orders."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "cancelled"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
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
            "You must conduct a full-scope audit and status alignment for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "For every order with status 'pending', 'processed', or 'delivered', remove the payment record at index 0 (the primary payment). "
            "Any order with status 'cancelled' must be reopened, after which its payment record at index 0 must also be removed. "
            "After clearing the payments, set the status of all James Li's orders to 'pending' and set the status of all Anya Garcia's orders to 'processed'. "
            "Use exactly the provided user_ids, order_ids, statuses, and index values without modification."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "cancelled"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_044",
        instruction=(
            "You must apply the new company-wide pricing policy and perform an account audit for "
            "customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "Update the price of the standard Smartphone variant (product '1801728040', "
            "item_id '5339029584') to 105.50 USD. In the audit, clear the payment records at index 0 from all of "
            "James Li's active orders with 'processed' or 'delivered' status and place them in a 'pending' "
            "state. Additionally, reinstate Anya Garcia's single cancelled order so that it is ready for processing."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 105.50},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3632959", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="reopen_cancelled_order",
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
            "You must carry out an end-of-life order processing and pricing audit for "
            "customers James Li (user_id 'james_li_5688') and Anya Garcia (user_id 'anya_garcia_3271'). "
            "First, implement the updated price of 140.00 USD for the standard Smartphone variant "
            "(product '1801728040', item_id '5339029584'). Then, following the EOL audit policy, "
            "clear the financial records from all of James Li's orders with a 'delivered' status and place "
            "them in a 'pending' state for review. For Anya Garcia, ensure her cancelled order has its "
            "primary payment removed before reinstatement, and prepare her processed order for review by "
            "clearing its payment and setting it to 'pending'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 140.00},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W4140680", "index": 0},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_046",
        instruction=(
            "For customer Anya Garcia (user_id 'anya_garcia_3271'), you must find all her 'pending' orders and update their status to 'processed'. "
            "Simultaneously, locate her cancelled order '#W4140680', reopen it, and perform a financial reset by clearing its primary payment record. "
            "Finally, update the status of this reopened order to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_047",
        instruction=(
            "You need to perform a series of urgent updates for customer Harper Brown (user_id 'harper_brown_7363'). "
            "First, increase the price of the 'T-Shirt' (product_id '9523456873', item_id '9612497925') to 55.00 USD. "
            "Then, for her order '#W2693718', add a new item: one 'Water Bottle' (product_id '8310926033', item_id '6469567736'). "
            "For the cancelled order '#W3220387' of customer Amelia Silva, you must reopen it and add one unit of the same 'Water Bottle' item."
        ),
        actions=[
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W2693718",
                    "items": [{"product_id": "8310926033", "item_id": "6469567736", "quantity": 1}],
                },
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W3220387"}),
            Action(
                name="add_items_to_order",
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
            "You must manage a complex update for customer Sofia Hernandez (user_id 'sofia_hernandez_5364') while meeting all of the following objectives:\n"
            "Update the price of the product 'T-Shirt' (product_id '9523456873', item_id '9612497925') to exactly 55.00 USD.\n"
            "Add one unit of the additional item 'Patio Umbrella' (product_id '9743693396', item_id '8170914468') to her pending order '#W9609649'.\n"
            "For order '#W3561391', remove its primary payment record at index 0 and set its status to 'processed'.\n"
            "For order '#W6876713', retrieve its financial details, remove its primary payment record at index 0, and add one unit of the item 'Water Bottle' (product_id '8310926033', item_id '6469567736').\n"
            "Use exactly the user_id, product_ids, item_ids, order_ids, and values provided above without modification."
        ),
        actions=[
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 1}],
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3561391", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3561391", "status": "processed"}
            ),
            Action(name="get_order_financials", kwargs={"order_id": "#W6876713"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6876713", "index": 0}),
            Action(
                name="add_items_to_order",
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
            "You are tasked with a full account cleanup for James Li (user_id 'james_li_5688') and a specific price update. "
            "For James Li, remove the single existing payment record (located at index 0) from each of his orders "
            "('#W2611340', '#W3632959', '#W4435622', '#W3638028') and set all their statuses to 'pending'. "
            "Separately, implement a company-wide price correction by updating the price of the standard Smartphone variant "
            "(product '1801728040', item_id '5339029584') to 199.99 USD."
        ),
        actions=[
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 199.99},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_050",
        instruction=(
            "You must manage a complex update for customer Mei Kovacs (user_id 'mei_kovacs_5767'). "
            "For her order '#W8193638', remove the item at index 0, then add two new 'T-Shirt' variants: "
            "variant '8124970213' and variant '9612497925' (both product_id '9523456873') to that same order. "
            "Concurrently, reopen the cancelled order '#W3220387' of customer Amelia Silva, remove the payment at index 0, "
            "and update its status to 'delivered'. "
            "Finally, update the price of the 'T-Shirt' (product_id '9523456873', item_id '9612497925') to exactly 55.00 USD "
            "and the price of 'Portable Charger' (product_id '6942297802', item_id '7903094618') to exactly 95.00 USD."
        ),
        actions=[
            Action(name="remove_items_by_index", kwargs={"order_id": "#W8193638", "indices": [0]}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [{"product_id": "9523456873", "item_id": "8124970213", "quantity": 1}],
                },
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W8193638",
                    "items": [{"product_id": "9523456873", "item_id": "9612497925", "quantity": 1}],
                },
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W3220387"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3220387", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3220387", "status": "delivered"}
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 55.00},
            ),
            Action(
                name="update_product_variant_price",
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
            "You are to perform a quarterly audit for customer James Li (user_id 'james_li_5688'). "
            "The audit policy requires that all of his orders currently in a 'processed' state must be financially reset by clearing their primary payment record. "
            "After the financial reset, these orders must be moved to a 'pending' state for final review."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_052",
        instruction=(
            "You are tasked with a system-wide data integrity audit for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "The audit policy requires a full financial reset on every order belonging to either customer "
            "that has a status of 'pending', 'processed', or 'delivered', by clearing its primary payment record (index 0). "
            "After the financial reset is complete, set the status of all such orders for James Li to 'processed' "
            "and set the status of all such orders for Anya Garcia to 'pending'. "
            "Use exactly the provided user_ids, statuses, and order_ids; do not modify unrelated records."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3632959", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4435622", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3638028", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W6436609", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_053",
        instruction=(
            "You must conduct a full-scope audit and status alignment for customers Anya Garcia (user_id 'anya_garcia_3271') "
            "and James Li (user_id 'james_li_5688'). Apply the audit policy as follows: "
            "for every order with a status of 'pending', 'processed', or 'delivered', clear the primary payment record. "
            "For any order with a 'cancelled' status, reactivate it, and also clear its primary payment record. "
            "After all financial resets are complete, align the statuses so that all of James Li's orders are set to 'pending' "
            "and all of Anya Garcia's orders are set to 'processed'. Use only the provided order IDs and parameters explicitly."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "cancelled"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_054",
        instruction=(
            "You are conducting an end-of-quarter account finalization for customers Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "For Anya Garcia, your objective is to resolve her single inactive order (status 'cancelled') by ensuring it is reactivated and its status is finalized as 'processed'. "
            "For James Li, the policy requires you to prepare his 'delivered' orders for archival by clearing their single existing payment record at index 0."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_055",
        instruction=(
            "You must conduct a full-scope audit and status alignment for customers "
            "Anya Garcia (user_id 'anya_garcia_3271') and James Li (user_id 'james_li_5688'). "
            "For every order belonging to either customer with status 'pending', 'processed', or 'delivered', "
            "remove its payment record at index 0. "
            "For any order with status 'cancelled', remove its payment record at index 0 and then reopen it. "
            "After all payments are cleared, set the status of every order for James Li to 'pending' and "
            "set the status of every order for Anya Garcia to 'processed'. "
            "Use exactly the provided user_ids, statuses, order_ids, and indices; do not remove payments more than once per order."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "cancelled"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4140680", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W4140680", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "processed"}
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6436609", "status": "processed"}
            ),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
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
            "You are to manage the processing of the single pending supply order, '#SO9359', for the supplier identified by '#SUP0001'. "
            "The company policy requires that you first approve the order. Following approval, you must log an 'info' event with the verbatim message 'Approved for immediate shipment.'. "
            "Finally, you are to formally receive all items for this order and then ensure its status is finalized as 'completed'."
        ),
        actions=[
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Approved for immediate shipment.",
                },
            ),
            Action(name="receive_supply_order_and_close", kwargs={"supply_order_id": "#SO9359"}),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "completed"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_057",
        instruction=(
            "You must update the system to reflect the correct logistics state for shipment tracking ID '357962501027' "
            "associated with order '#W2611340'. "
            "Ensure that the tracking record shows courier_name = 'Express Delivery Services', includes a custom event "
            "with status 'rerouted' and the exact note 'Forwarded to partner carrier for final delivery', and that the "
            "shipment's tracking status is set to 'in_transit'. "
            "Use exactly the provided identifiers and texts (tracking_id '357962501027', order '#W2611340'); do not "
            "generate new tracking IDs or modify unrelated entities."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "357962501027", "courier_name": "Express Delivery Services"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "rerouted",
                    "note": "Forwarded to partner carrier for final delivery",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "357962501027", "status": "in_transit"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_058",
        instruction=(
            "You are handling a full return and replacement process for customer Anya Garcia (user_id 'anya_garcia_3271'). "
            "The first part of the process is the return: you must archive her order '#W6310710' by clearing its item at index 0 and payment data at index 0 and setting its status to 'cancelled'. "
            "The second part is the replacement: you are to repurpose her other cancelled order, '#W4140680', by reactivating it, clearing all of its previous three items, adding two new units of the standard Smartphone variant (product '1801728040', item_id '5339029584'), and appending a new payment of 240.00 USD via 'pm-anya-card-2'. "
            "To conclude, retrieve all orders for this customer that are now in a 'pending' state."
        ),
        actions=[
            Action(name="remove_items_by_index", kwargs={"order_id": "#W6310710", "indices": [0]}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "cancelled"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="remove_items_by_index", kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]}
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 2}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 240.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
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
            "You are to perform a data consolidation and pricing update for customers James Li (user_id 'james_li_5688') and Anya Garcia (user_id 'anya_garcia_3271'). "
            "For James Li, your objective is to consolidate the items and payments from his order '#W3632959' into the target order '#W2611340', ensuring the consolidated order's final status is 'processed'. "
            "For Anya Garcia, you must clear the primary payment record from her 'processed' order '#W6310710'. "
            "Finally, you must execute a company-wide price change for the standard Smartphone variant (product '1801728040', item_id '5339029584'), setting its new price to 160.00 USD. "
            "To conclude, retrieve all 'processed' orders for James Li."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="merge_orders_for_same_user",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": True,
                },
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "processed"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 160.00},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
        ],
        outputs=[[{"order_id": "#W2611340", "status": "processed"}]],
    ),
    Task(
        annotator="1",
        user_id="user_060",
        instruction=(
            "You must handle a customer request for 'Emma Santos' (user_id 'emma_santos_9753') who wants to modify her pending order '#W9903153'. "
            "Your goal is to replace the item at index 3 with a 'Water Bottle' (product '8310926033', item '6469567736'). "
            "After the replacement, you must fully reconcile the order's finances. This involves voiding the original payment and applying a new payment for the corrected total using her payment method 'credit_card_5869505'. "
            "For logistics, you need to consolidate this shipment with her previous order by linking the existing tracking ID '443521489581'. "
            "Finally, you will add an 'info' type event with the note 'Order #W9903153 added to this shipment. Contents verified.' to the tracking record and ensure the modified order is processed."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "pending"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 3,
                    "product_id": "8310926033",
                    "item_id": "6469567736",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W9903153"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W9903153",
                    "transaction_type": "payment",
                    "amount": 3437.33,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W9903153", "tracking_id": "443521489581"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Order #W9903153 added to this shipment. Contents verified.",
                },
            ),
            Action(
                name="set_order_status",
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
            "You are to resolve a logistics incident involving the shipment with tracking ID '357962501027'. "
            "The resolution policy requires you to log a 'delayed' event with the note 'Weather disruption in transit' and then see the delivery through to completion by advancing its status directly to 'delivered'. Upon delivery, you must ensure the associated order, '#W2611340', is also marked as 'delivered'. "
            "As a separate cleanup task, you must prepare all of Anya Garcia's (user_id 'anya_garcia_3271') orders with 'pending' status for review by clearing their primary payment records at index 0."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "delayed",
                    "note": "Weather disruption in transit",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2611340", "status": "delivered"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6436609", "index": 0}),
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
            "Your objective is to conduct a cross-customer account audit and reconciliation for 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "Your first goal is to handle Anya's account. Per audit policy, you must process her 'processed' order '#W6310710' by voiding the payment at index 0 and setting its status to 'pending'. You must also reactivate her 'cancelled' order '#W4140680' by reopening it, adding one 'Gaming Mouse' (product '5713490933', item '5796612084'), and applying a new 'payment' of $75.00 with method 'pm-anya-card-2'. "
            "Your second goal is to audit all of James Li's 'processed' and 'delivered' orders. For each of these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), the policy requires you to void the payment at index 0 and set the order's status to 'pending' for review."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
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
            "Your objective is to manage the complete lifecycle of a customer-modified order for 'Anya Garcia' (user_id 'anya_garcia_3271'). "
            "You must process her pending order '#W6436609' by first replacing the item at index 0 with a 'Smart Watch' (product '6945232052', variant '9408160950'). "
            "The next goal is a full financial reconciliation: you will void the original payment at index 0 and apply a new 'payment' for the updated total of $3285.76 using payment method 'pm-anya-card-2'. "
            "To complete the fulfillment process, you must link the existing tracking ID '951786982868' and advance its status sequentially to 'in_transit' and then 'delivered'. "
            "Once delivered, update the order status to match. "
            "Finally, you will complete the customer service cycle by issuing a partial 'refund' of 20.00 USD to the same payment method, 'pm-anya-card-2'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6436609",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "9408160950",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W6436609"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W6436609", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W6436609",
                    "transaction_type": "payment",
                    "amount": 3285.76,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W6436609", "tracking_id": "951786982868"},
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "951786982868", "status": "in_transit"},
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6436609", "status": "delivered"},
            ),
            Action(
                name="append_payment",
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
            "Your objective is to resolve a fulfillment crisis for customer 'luca_rossi_2745' regarding order '#W3631991'. "
            "This requires managing supply order '#SO9359' by logging a 'note' ('Emergency restock for promotion'), processing its receipt ('Urgent shipment received'), and logging a final 'note' ('Delivery completed successfully'). "
            "Concurrently, you must update the customer order by adding one unit (quantity 1) of the new stock (product '9523456873', item '9612497925'). "
            "The financial policy requires a reconciliation: apply a 'payment' of $39.99 with method 'pm_002' and void the payment at index 1. "
            "To complete the fulfillment, you must advance the order status first to 'shipped' and finally to 'delivered'."
        ),
        actions=[
            Action(name="append_supply_order_event", kwargs={
                "supply_order_id": "#SO9359",
                "event_type": "note",
                "message": "Emergency restock for promotion"
            }),
            Action(name="receive_supply_order_and_close", kwargs={
                "supply_order_id": "#SO9359",
                "note": "Urgent shipment received"
            }),
            Action(name="add_items_to_order", kwargs={
                "order_id": "#W3631991",
                "items": [{"product_id": "9523456873", "item_id": "9612497925", "quantity": 1}]
            }),
            Action(name="append_payment", kwargs={
                "order_id": "#W3631991",
                "transaction_type": "payment",
                "amount": 39.99,
                "payment_method_id": "pm_002"
            }),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3631991", "index": 1}),
            Action(name="set_order_status", kwargs={"order_id": "#W3631991", "status": "shipped"}),
            Action(name="set_order_status", kwargs={"order_id": "#W3631991", "status": "delivered"}),
            Action(name="append_supply_order_event", kwargs={
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
            "Your task is to resolve an account issue for 'Anya Garcia' (user_id 'anya_garcia_3271') by reactivating her cancelled order '#W4140680'. "
            "Your goal is to prepare this order for shipment by adding a 'Smart Watch' (product '6945232052', variant '9408160950') and applying a 'payment' transaction of 250.00 USD using her payment method 'pm-anya-card-1'. "
            "To meet the fulfillment requirements, you must consolidate this order's shipment by linking the tracking ID from James Li's order '#W3632959' and then ensure the order is marked as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "6945232052", "item_id": "9408160950", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 250.00,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="find_tracking_by_order",
                kwargs={"order_id": "#W3632959"},
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W4140680", "tracking_id": "474654093386"},
            ),
            Action(
                name="set_order_status",
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
            "Your task is to execute a multi-part operational workflow for customer 'Juan Smith' (user_id 'juan_smith_5229'). "
            "Your first goal is to update the shipment with tracking ID '326515289837'. The policy requires you to change the courier to 'FastTrack Couriers', log an 'info' status event with the note 'Rerouted to new courier', and advance the tracking status to 'delivered'. "
            "Your second goal is to perform a financial reset on his active orders '#W1429524' and '#W7546247' by removing the payment at index 0 from each and setting their final statuses to 'pending'."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "FastTrack Couriers",
                },
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Rerouted to new courier",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "326515289837", "status": "delivered"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W1429524", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W1429524", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W7546247", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W7546247", "status": "pending"}),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "FastTrack Couriers"},
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
            "You are performing a comprehensive account cleanup for customer Emma Santos (user_id 'emma_santos_9753'). "
            "The policy requires that you find all of her orders and apply a financial reset and status update. "
            "Specifically, for orders '#W3113816' and '#W9903153', you must clear the primary payment and set their status to 'pending'. "
            "For order '#W1620235', you must clear the payment and set the status to 'delivered'. "
            "Finally, for order '#W2918688', clear the payment and set the status to 'cancelled'."
        ),
        actions=[
            Action(name="find_orders_by_user_and_status", kwargs={"user_id": "emma_santos_9753"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3113816", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3113816", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W9903153", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W9903153", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W1620235", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W1620235", "status": "delivered"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2918688", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W2918688", "status": "cancelled"}
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="1",
        user_id="user_068",
        instruction=(
            "Your objective is to execute a comprehensive account management workflow for 'Sofia Hernandez' (user_id 'sofia_hernandez_5364') as part of a full order audit. Your task is to process three specific orders according to policy. "
            "For her pending order '#W9609649', you will add one 'Electric Kettle' (product '1075968781', item '9624127908'), apply a 'payment' of $120.00 using 'pm-sofia-card-3', and set its status to 'processed'. "
            "For her processed order '#W5765741', you will add two 'Patio Umbrella' items (product '9743693396', item '8170914468'), apply a 'payment' of $1500.00 using 'pm-sofia-card-3', and set its status to 'delivered'. "
            "Finally, for her pending order '#W3561391', you must remove the payment at index 0 and set its status to 'cancelled'."
        ),
        actions=[
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W9609649",
                    "items": [{"product_id": "1075968781", "item_id": "9624127908", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W9609649",
                    "transaction_type": "payment",
                    "amount": 120.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W9609649", "status": "processed"}
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W5765741",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 2}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W5765741",
                    "transaction_type": "payment",
                    "amount": 1500.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="set_order_status", kwargs={"order_id": "#W5765741", "status": "delivered"}
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3561391", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W3561391", "status": "cancelled"}
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
            "Your objective is to conduct a comprehensive account review for 'Anya Garcia' (user_id 'anya_garcia_3271'). "
            "Your primary goal is to process an item exchange on her processed order '#W6310710'. You must replace the item at index 0 with a 'Gaming Mouse' (product '5713490933', item '5796612084'). "
            "After the exchange, you will apply a new 'payment' of $150.00 using payment method 'pm-anya-card-2'. "
            "As a separate goal, you must restore her cancelled order '#W4140680' by reopening it and setting its status to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6310710",
                    "index": 0,
                    "product_id": "5713490933",
                    "item_id": "5796612084",
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W6310710",
                    "transaction_type": "payment",
                    "amount": 150.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to perform a multi-part logistics and account update. "
            "For customer 'James Li' (user_id 'james_li_5688'), finalize the shipment of his processed order '#W2611340'. You must update its tracking record ('357962501027') to assign the courier 'QuickShip Logistics', add a 'delayed' event with the note 'Weather disruption in transit', and advance the tracking status to 'delivered'. "
            "For customer 'Anya Garcia' (user_id 'anya_garcia_3271'), restore her cancelled order '#W4140680' by reopening it. "
            "Finally, manage an existing supply chain process by approving the pending supply order '#SO9359' for supplier '#SUP0001' with the reason 'Restock approved' and then processing its receipt to update inventory."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "357962501027", "courier_name": "QuickShip Logistics"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "delayed",
                    "note": "Weather disruption in transit",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="auto_approve_supply_order",
                kwargs={"supply_order_id": "#SO9359", "reason": "Restock approved"},
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO9359"},
            ),
        ],
        outputs=[
            {"tracking_id": "357962501027", "courier_name": "QuickShip Logistics"},
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
            "Your objective is to perform a series of required modifications on the account of 'Anya Garcia' (user_id 'anya_garcia_3271'). "
            "Your first goal is to update her pending order '#W6436609'. You must replace the item at index 0 with an 'Electric Kettle' (product '1075968781', item '9624127908') and then log the updated financial state of the order. "
            "Your second goal is to restore her cancelled order '#W4140680'. You must reopen it, clear its contents by removing the three items at indices 0, 1, and 2, add one new 'Smart Watch' (product '6945232052', item '2681513500'), and then set its status to 'processed'. "
            "Finally, ensure the first modified order, '#W6436609', is also marked as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W6436609",
                    "index": 0,
                    "product_id": "1075968781",
                    "item_id": "9624127908",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W6436609"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "6945232052", "item_id": "2681513500", "quantity": 1}],
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W4140680", "status": "processed"},
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to execute a multi-part administrative task involving logistics, account auditing, and pricing. "
            "For customer 'Juan Smith' (user_id 'juan_smith_5229'), your goal is to finalize the logistics for his order '#W7546247'. You must update its tracking record ('326515289837') to use 'Express Delivery Services', log an 'info' event with the verbatim note 'Carrier change requested by logistics', and advance the status to 'in_transit'. "
            "For customer 'Emma Santos' (user_id 'emma_santos_9753'), your goal is to perform a financial audit on all of her delivered orders ('#W3113816' and '#W1539823'). The audit policy requires you to void the primary payment at index 0 from each order and reset their statuses to 'pending' for review. "
            "As a final administrative task, you will perform a company-wide price update for the 'Smart Watch' (product '6945232052', item '9408160950'), setting its new price to 299.99 USD."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "Express Delivery Services",
                },
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Carrier change requested by logistics",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "326515289837", "status": "in_transit"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "delivered"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "6945232052", "item_id": "9408160950", "new_price": 299.99},
            ),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "Express Delivery Services"},
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
            "Your objective is to manage a post-shipment return and financial adjustment for 'James Li' (user_id 'james_li_5688') on his order '#W2611340'. "
            "Your primary goal is to intercept the shipment with tracking ID '357962501027'. You must update its courier to 'QuickShip Logistics'. "
            "You are to log this action in the tracking history as a 'checkpoint' event with the note 'Shipment rerouted back to sender at customer request.' and then update the shipment's final status to 'returning'. "
            "Once logistics are handled, your second goal is to financially reconcile the order: you must remove the returned 'Office Chair' at index 1, void the original payment at index 0, and apply a new 'payment' of $850.25 from payment method 'gift_card_1725971'."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={
                    "tracking_id": "357962501027",
                    "courier_name": "QuickShip Logistics",
                },
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "checkpoint",
                    "note": "Shipment rerouted back to sender at customer request.",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "357962501027", "status": "returning"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W2611340", "indices": [1]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 850.25,
                    "payment_method_id": "gift_card_1725971",
                },
            ),
        ],
        outputs=[
            {"tracking_id": "357962501027", "courier_name": "QuickShip Logistics"},
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
            "Your objective is to manage a significant update for customer 'Emma Santos' (user_id 'emma_santos_9753'). "
            "Your primary goal is to process an item exchange on her processed order '#W8160318' by replacing the item at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'). "
            "Following the exchange, you must reconcile the order's finances by voiding the payment at index 0 and applying a new 'payment' of 550.00 USD using payment method 'paypal_emma_santos_1'. "
            "To complete the task, you will consolidate its shipment with her order '#W3113816' by linking the existing tracking ID '443521489581' and logging an 'info' event with the note 'Package prepared for dispatch'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "processed"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W8160318",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W8160318", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W8160318",
                    "transaction_type": "payment",
                    "amount": 550.0,
                    "payment_method_id": "paypal_emma_santos_1",
                },
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={
                    "order_id": "#W3113816",
                    "tracking_id": "443521489581",
                },
            ),
            Action(
                name="add_tracking_custom_event",
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
            "Your objective is to execute a comprehensive financial audit and status realignment for all of 'Emma Santos''s (user_id 'emma_santos_9753') active orders. "
            "You are required to implement the company's end-of-quarter policy, which mandates voiding the primary payment from all 'pending', 'processed', and 'delivered' orders. "
            "Following the payment reset, you must realign each order's status based on its original state: delivered orders ('#W3113816', '#W1539823') are moved to pending; pending orders '#W9903153' and '#W2918688' are cancelled while others ('#W1620235', '#W9655299') are processed; and processed orders ('#W8160318') remain as such. "
            "Finally, as a separate administrative task, you will apply company-wide price updates to the 'Patio Umbrella' (product '9743693396', item '8170914468') and the 'Water Bottle' (product '8310926033', item '6469567736'), setting their new prices to 799.00 USD and 28.00 USD respectively."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "delivered"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9903153", "status": "cancelled"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2918688", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2918688", "status": "cancelled"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W1620235", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1620235", "status": "processed"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W9655299", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9655299", "status": "processed"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W8160318", "index": 0},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9743693396", "item_id": "8170914468", "new_price": 799.00},
            ),
            Action(
                name="update_product_variant_price",
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
            "Your responsibility is to execute a multi-faceted administrative operation. "
            "Your first goal is to manage the logistics for customer 'Juan Smith' (user_id 'juan_smith_5229') on his order '#W7546247'. You must update its tracking record ('326515289837') to use 'Express Delivery Services', log an 'info' event with the verbatim note 'Carrier change requested by logistics', and advance the status to 'in_transit'. "
            "Your second goal is to perform a financial audit for 'Emma Santos' (user_id 'emma_santos_9753'). Per audit policy, you will process all of her delivered orders ('#W3113816' and '#W1539823') by voiding the primary payment at index 0 from each and resetting their statuses to 'pending' for review. "
            "Finally, you will execute a company-wide price update for the 'Smart Watch' (product '6945232052', item '9408160950'), setting its new price to 299.99 USD."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={
                    "tracking_id": "326515289837",
                    "courier_name": "Express Delivery Services",
                },
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "326515289837",
                    "event_status": "info",
                    "note": "Carrier change requested by logistics",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "326515289837", "status": "in_transit"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "delivered"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W1539823", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1539823", "status": "pending"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "6945232052", "item_id": "9408160950", "new_price": 299.99},
            ),
        ],
        outputs=[
            {"tracking_id": "326515289837", "courier_name": "Express Delivery Services"},
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
            "Your task is to perform a financial re-audit for customer 'James Li' (user_id 'james_li_5688') and apply a pricing update. "
            "For the audit, you need to find his 'delivered' orders, specifically '#W4435622' and '#W3638028'. For both of these orders, you must remove their primary payment records (at index 0) and reset their status to 'pending'. "
            "Separately, you are required to update the company-wide pricing for two 'T-Shirt' (product_id '9523456873') variants: set item '8124970213' to 45.50 USD and item '9612497925' to 50.00 USD."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W4435622", "index": 0},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3638028", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W4435622", "status": "pending"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3638028", "status": "pending"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "8124970213", "new_price": 45.50},
            ),
            Action(
                name="update_product_variant_price",
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
            "Your task is to conduct a full account audit for 'Emma Santos' (user_id 'emma_santos_9753'). Your objective is to modify her orders according to the audit policy. "
            "For her pending order '#W9903153', you must remove the item at index 1. "
            "For her other pending order '#W1620235', you will add one 'Pet Bed' (product '2747247837', item '6942241102'). "
            "For her delivered order '#W3113816', you must update its tracking record ('443521489581') by changing the courier to 'QuickShip Logistics' and adding an 'info' event with the note 'Shipment audit complete'. "
            "To finalize the audit, you will ensure both modified pending orders ('#W9903153' and '#W1620235') are set to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "pending"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W9903153", "indices": [1]},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W1620235",
                    "items": [{"product_id": "2747247837", "item_id": "6942241102", "quantity": 1}],
                },
            ),
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "443521489581", "courier_name": "QuickShip Logistics"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Shipment audit complete",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
            Action(
                name="set_order_status",
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
            {"tracking_id": "443521489581", "courier_name": "QuickShip Logistics"},
            {"tracking_id": "443521489581", "new_status": "info", "history_len": 2},
            {"order_id": "#W9903153", "status": "processed"},
            {"order_id": "#W1620235", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_081",
        instruction=(
            "You are responsible for handling updates for customer 'Anya Garcia' (user_id 'anya_garcia_3271'). "
            "Her order '#W2611340' has already been received and dispatched. "
            "You must now complete the tracking updates by logging an `info` event to tracking ID '357962501027' with the note 'Shipment verified by logistics team', and then advancing its status to 'delivered'. "
            "Once the delivery is confirmed, update the order status to 'delivered'. "
            "In addition, reactivate her cancelled order '#W4140680', restock it with one 'Gaming Mouse' (5713490933, 5796612084) and one 'T-Shirt' (9523456873, 9612497925), process a new payment of $850.00 using 'credit_card_8955149', and finalize the order as 'processed'."
        ),
        actions=[
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "357962501027",
                    "event_status": "info",
                    "note": "Shipment verified by logistics team",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "357962501027", "status": "delivered"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "delivered"},
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [
                        {"product_id": "5713490933", "item_id": "5796612084", "quantity": 1},
                        {"product_id": "9523456873", "item_id": "9612497925", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 850.00,
                    "payment_method_id": "credit_card_8955149",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to execute a cross-customer reconciliation. For customer 'James Li' (user_id 'james_li_5688'), your goal is to consolidate his processed orders and prepare them for review. "
            "Merge his order '#W3632959' into '#W2611340' (without payments), then set the consolidated order's status to 'pending'. "
            "Concurrently, for customer 'Anya Garcia' (user_id 'anya_garcia_3271'), restore her cancelled order '#W4140680' by reopening it, adding one 'Smartphone' (product '1801728040', item '5339029584'), applying a new 'payment' of $200.00 using 'pm-anya-card-2', and setting its status to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="merge_orders_for_same_user",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": False,
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "pending"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 200.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to execute a two-part administrative task. First, you must manage a post-shipment interception and financial adjustment for 'Aarav Sanchez' (user_id 'aarav_sanchez_9729') on his order '#W5455653'. "
            "Your goal is to update the tracking record ('632894717617') to assign 'QuickShip Logistics', log an 'info' event with the note 'Return to sender initiated', and set the shipment status to 'returning'. "
            "Following the logistics update, you must reconcile the order's finances by voiding the payment at index 0 and issuing a 'refund' of $50.00 using payment method 'credit_card_2690859'. "
            "Second, your goal is to cancel the pending order '#W1429524' for customer 'Juan Smith' (user_id 'juan_smith_5229')."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "632894717617", "courier_name": "QuickShip Logistics"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "632894717617",
                    "event_status": "info",
                    "note": "Return to sender initiated",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "632894717617", "status": "returning"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W5455653", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W5455653",
                    "transaction_type": "refund",
                    "amount": 50.00,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1429524", "status": "cancelled"},
            ),
        ],
        outputs=[
            {"tracking_id": "632894717617", "courier_name": "QuickShip Logistics"},
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
            "Your objective is to execute a multi-part update across two key customer accounts. "
            "For 'Sofia Hernandez' (user_id 'sofia_hernandez_5364'), your goal is to void the primary payment at index 0 from her order '#W5765741', add two 'Patio Umbrella' items (product '9743693396', item '8170914468'), apply a new payment of $1500.00 using 'pm-sofia-card-3', and set the order's status to 'delivered'. "
            "For 'Anya Garcia' (user_id 'anya_garcia_3271'), your goal is twofold: first, reopen her cancelled order '#W4140680'. Then, finalize the shipment for her order '#W6310710' by adding an 'info' tracking event to '951786982868' with note 'Shipment verified by logistics team', advancing the tracking status to 'delivered', and updating the order status to 'delivered'."
        ),
        actions=[
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W5765741", "index": 0},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W5765741",
                    "items": [{"product_id": "9743693396", "item_id": "8170914468", "quantity": 2}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W5765741",
                    "transaction_type": "payment",
                    "amount": 1500.00,
                    "payment_method_id": "pm-sofia-card-3",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W5765741", "status": "delivered"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Shipment verified by logistics team",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="set_order_status",
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
            "Your responsibility is to execute an end-of-quarter financial audit for customer 'Emma Santos' (user_id 'emma_santos_9753'). "
            "Your goal is to apply a specific realignment policy to several of her orders. The policy requires that you first void the primary payment at index 0 for each of the following orders: '#W3113816', '#W9903153', '#W1620235', and '#W2918688'. "
            "After voiding the payments, you must set their new statuses: '#W3113816' becomes 'pending', '#W9903153' becomes 'cancelled', and '#W1620235' becomes 'processed'. The order '#W2918688' does not require a status change."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W9903153", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9903153", "status": "cancelled"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W1620235", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1620235", "status": "processed"},
            ),
            Action(
                name="remove_payment_by_index",
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
            "Your objective is to conduct a cross-customer account audit and reconciliation for 'Anya Garcia' (user_id 'anya_garcia_3271') and 'James Li' (user_id 'james_li_5688'). "
            "Your first goal is to handle Anya's account. Per audit policy, you must process her 'processed' order '#W6310710' by voiding the payment at index 0 and setting its status to 'pending'. You must also reactivate her 'cancelled' order '#W4140680' by reopening it, adding one 'Gaming Mouse' (product '5713490933', item '5796612084'), and applying a new 'payment' of $75.00 with method 'pm-anya-card-2'. "
            "Your second goal is to audit all of James Li's 'processed' and 'delivered' orders. For each of these four orders ('#W2611340', '#W3632959', '#W4435622', '#W3638028'), the policy requires you to void the payment at index 0 and set the order's status to 'pending' for review."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "delivered"},
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W6310710", "index": 0}),
            Action(
                name="set_order_status", kwargs={"order_id": "#W6310710", "status": "pending"}
            ),
            Action(name="reopen_cancelled_order", kwargs={"order_id": "#W4140680"}),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 75.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W2611340", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W2611340", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3632959", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3632959", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W4435622", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W4435622", "status": "pending"}),
            Action(name="remove_payment_by_index", kwargs={"order_id": "#W3638028", "index": 0}),
            Action(name="set_order_status", kwargs={"order_id": "#W3638028", "status": "pending"}),
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
            "Your objective is to execute a multi-part operation involving logistics, supply chain, and pricing. "
            "For Anya Garcia's order '#W6310710', you must finalize its shipment by updating its tracking record ('951786982868') with the courier 'Express Delivery Services', logging an 'info' event with the verbatim note 'Recipient requested change of courier.', and setting the order and tracking statuses to 'delivered'. "
            "For supplier '#SUP0002', manage their pending 'Gaming Mouse' inventory by approving supply order '#SO6035' with an 'info' event note of 'Approved per inventory flag' and processing its receipt, while canceling supply order '#SO7848'. "
            "After restocking, apply a price update to the 'Gaming Mouse' (product '5713490933', item '8214883393') to $82.50."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "951786982868", "courier_name": "Express Delivery Services"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "Recipient requested change of courier.",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "951786982868", "status": "delivered"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6310710", "status": "delivered"},
            ),
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Approved per inventory flag",
                },
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO7848", "status": "cancelled"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 82.50},
            ),
        ],
        outputs=[
            {"tracking_id": "951786982868", "courier_name": "Express Delivery Services"},
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
            "Your objective is to manage the downstream impact of a supply chain failure for customer 'Emma Santos' (user_id 'emma_santos_9753'). "
            "Your first goal is to process the cancellation of supply order '#SO6035' by setting its status to 'cancelled' and logging an 'info' type event with the note 'Cancelled due to supplier quality control failure.'. "
            "To resolve the resulting stock issue for her delivered order '#W3113816', you must replace the out-of-stock item at index 2 with a 'Smart Watch' (product '6945232052', variant '2681513500') and reset the order's status to 'pending' for review. "
            "As a final step, you need to update the order's tracking record ('443521489581') by adding an 'info' type event with the note 'Order contents updated due to stock issue. Shipment will proceed as scheduled.' and apply a price correction to the newly added 'Smart Watch' variant, setting its price to $255.00."
        ),
        actions=[
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO6035", "status": "cancelled"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO6035",
                    "event_type": "info",
                    "message": "Cancelled due to supplier quality control failure.",
                },
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "delivered"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3113816",
                    "index": 2,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3113816", "status": "pending"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "Order contents updated due to stock issue. Shipment will proceed as scheduled.",
                },
            ),
            Action(
                name="update_product_variant_price",
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
            "You are tasked with preparing the account of 'James Li' (user_id 'james_li_5688') for archival. "
            "First, find all his 'processed' orders. "
            "For his order '#W2611340', you must remove all items (at indices 0 and 1) and its primary payment. After clearing it, set its status to 'cancelled'. "
            "Next, for his other order '#W3632959', you must also remove its only item (at index 0) and its primary payment. Then, set its status to 'cancelled' as well to complete the archival process."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W2611340", "indices": [0, 1]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2611340", "status": "cancelled"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W3632959", "indices": [0]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3632959", "index": 0},
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to execute a multi-faceted update for customer 'Emma Santos' (user_id 'emma_santos_9753'). You have two primary goals. "
            "First, you must modify and finalize her pending order '#W9903153'. This requires you to replace the item at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'), remove the item at index 2, reconcile the finances with a new 'payment' of $3321.66 using payment method 'credit_card_5869505', and set the order's status to 'processed'. "
            "Second, you must update logistics for her delivered orders by updating the courier to 'FastTrack Couriers' for tracking record '443521489581' and adding an 'info' event with the note 'Delivery confirmation requested by user.' to tracking record '749747277477'."
        ),
        actions=[
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W9903153", "indices": [2]},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W9903153",
                    "transaction_type": "payment",
                    "amount": 3321.66,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "443521489581", "courier_name": "FastTrack Couriers"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Delivery confirmation requested by user.",
                },
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
        ],
        outputs=[
            {"status": "success", "message": "Order #W9903153 was successfully modified in memory."},
            {"order_id": "#W9903153", "removed_count": 1, "items_len": 4},
            {"order_id": "#W9903153", "payment_history_len": 2},
            {"tracking_id": "443521489581", "courier_name": "FastTrack Couriers"},
            {"tracking_id": "749747277477", "new_status": "info", "history_len": 1},
            {"order_id": "#W9903153", "status": "processed"},
        ],
    ),
    Task(
        annotator="1",
        user_id="user_091",
        instruction=(
            "Your objective is to execute a full account realignment for customer 'Anya Garcia' (user_id 'anya_garcia_3271') based on the quarterly audit policy. "
            "The policy requires you to process her orders based on their current status. For her processed order '#W6310710', you must void the payment at index 0 and reset its status to 'pending'. "
            "For her pending order '#W6436609', you will also void the payment at index 0 but change its status to 'processed'. "
            "For her cancelled order '#W4140680', your task is to restore it by reopening it, adding one 'Gaming Mouse' (product '5713490933', item '5796612084'), and applying a new 'payment' of $75.00 with method 'pm-anya-card-2'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "processed"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W6310710", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6310710", "status": "pending"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W6436609", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W6436609", "status": "processed"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [{"product_id": "5713490933", "item_id": "5796612084", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
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
            "Your objective is to execute a multi-part administrative task involving logistics and pricing. "
            "Your first goal is to finalize logistics for 'Emma Santos' (user_id 'emma_santos_9753') by updating two tracking records: for '443521489581', change the courier to 'QuickShip Logistics' and add an 'info' event with the note 'First update complete'; for '749747277477', add an 'info' event with the note 'Second update started' and set its status to 'delivered'. "
            "Your second goal is to execute company-wide price changes for the 'Smartphone' (product '1801728040', item '5339029584') to 210.00 USD and the 'T-Shirt' (product '9523456873', item '9612497925') to 52.00 USD. "
            "Your final goal is to audit the account of 'James Li' (user_id 'james_li_5688') by finding all his processed orders and logging the financial state of each one found ('#W2611340' and '#W3632959')."
        ),
        actions=[
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "443521489581", "courier_name": "QuickShip Logistics"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "info",
                    "note": "First update complete",
                },
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Second update started",
                },
            ),
            Action(
                name="advance_tracking_status",
                kwargs={"tracking_id": "749747277477", "status": "delivered"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "1801728040", "item_id": "5339029584", "new_price": 210.00},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "9523456873", "item_id": "9612497925", "new_price": 52.00},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W2611340"},
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W3632959"},
            ),
        ],
        outputs=[
            {"tracking_id": "443521489581", "courier_name": "QuickShip Logistics"},
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
            "Your task is to manage the full lifecycle of supply order '#SO9359' and then update a related customer order based on the new inventory. "
            "You will first find the pending supply orders for supplier '#SUP0001' to get context. Then, for order '#SO9359', you must advance it through 'approved' and 'in_transit' statuses, logging each step with an 'info' type event using the messages 'Approved by management.' and 'Shipment departed from supplier facility.' respectively. "
            "Your next goal is to process the order's receipt and close it. "
            "Once the 'Smartphone' stock is confirmed from this delivery, you will update the pending order '#W6436609' for customer 'Anya Garcia' (user_id 'anya_garcia_3271') by adding another 'Smartphone' (product '1801728040', item '5339029584'), applying a new 'payment' of $210.00 with method 'pm-anya-card-2', and finally marking the order as 'processed'."
        ),
        actions=[
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0001", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "approved"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Approved by management.",
                },
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO9359", "status": "in_transit"},
            ),
            Action(
                name="append_supply_order_event",
                kwargs={
                    "supply_order_id": "#SO9359",
                    "event_type": "info",
                    "message": "Shipment departed from supplier facility.",
                },
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO9359"},
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "pending"},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W6436609",
                    "items": [{"product_id": "1801728040", "item_id": "5339029584", "quantity": 1}],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W6436609",
                    "transaction_type": "payment",
                    "amount": 210.00,
                    "payment_method_id": "pm-anya-card-2",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your primary objective is to consolidate and reconcile processed orders for customer 'James Li' (user_id 'james_li_5688'). "
            "You must merge his order '#W3632959' into '#W2611340', carrying over all items and payments. "
            "Per company policy, you will then adjust the consolidated order by replacing the item at index 2 with a 'Gaming Mouse' (product '5713490933', variant '5796612084'). "
            "Your final goal is to complete a full financial reconciliation: you are to void the two merged payments at index 0 twice, and then apply a single new 'payment' for the correct, final order total using payment method 'pm-james-card-1'. "
            "The order should end in a 'processed' state."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "james_li_5688", "status": "processed"},
            ),
            Action(
                name="merge_orders_for_same_user",
                kwargs={
                    "target_order_id": "#W2611340",
                    "source_order_id": "#W3632959",
                    "include_payments": True,
                },
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W2611340",
                    "index": 2,
                    "product_id": "5713490933",
                    "item_id": "5796612084",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W2611340"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W2611340", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W2611340",
                    "transaction_type": "payment",
                    "amount": 695.54,
                    "payment_method_id": "pm-james-card-1",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your responsibility is to manage a multi-order update for customer 'Emma Santos' (user_id 'emma_santos_9753'). "
            "Your first goal is to handle a product exchange in her order '#W9903153' by replacing the item at index 1 with a 'T-Shirt' (product '9523456873', item '8124970213'). "
            "After this modification, your second goal is to perform a batch status realignment on all relevant pending orders according to the end-of-day policy: the modified order '#W9903153' should be 'processed', order '#W1620235' must be marked as 'delivered', order '#W2918688' is to be 'cancelled', and order '#W9655299' should remain 'pending'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "pending"},
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W9903153",
                    "index": 1,
                    "product_id": "9523456873",
                    "item_id": "8124970213",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W9903153"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9903153", "status": "processed"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W1620235", "status": "delivered"},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W2918688", "status": "cancelled"},
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to manage a complex customer return and subsequent resale. "
            "The first part of your task is to process a return from 'Aarav Sanchez' (user_id 'aarav_sanchez_9729') on his delivered order '#W5455653'. "
            "The return policy requires you to remove the 'DSLR Camera' at index 0, void the original payment at index 0, and apply an adjusted 'payment' of $371.27 via 'credit_card_2690859'. "
            "The second part of your task is to fulfill the pending order '#W7007896' for 'Yusuf Ahmed' (user_id 'yusuf_ahmed_6232'). "
            "To do this efficiently, you will consolidate logistics by linking Aarav's tracking record ('632894717617') to Yusuf's order, log an 'info' event with the note 'Shipment consolidated to include items for order #W7007896.', apply Yusuf's 'payment' of $850.25 via 'credit_card_yusuf_ahmed_7745', and mark the order as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "aarav_sanchez_9729", "status": "delivered"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W5455653", "indices": [0]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W5455653", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W5455653",
                    "transaction_type": "payment",
                    "amount": 371.27,
                    "payment_method_id": "credit_card_2690859",
                },
            ),
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "yusuf_ahmed_6232", "status": "pending"},
            ),
            Action(
                name="find_tracking_by_order",
                kwargs={"order_id": "#W5455653"},
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W7007896", "tracking_id": "632894717617"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "632894717617",
                    "event_status": "info",
                    "note": "Shipment consolidated to include items for order #W7007896.",
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W7007896",
                    "transaction_type": "payment",
                    "amount": 850.25,
                    "payment_method_id": "credit_card_yusuf_ahmed_7745",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to manage a complex post-delivery exchange and its downstream consequences for 'Emma Santos' (user_id 'emma_santos_9753') on her delivered order '#W3113816'. "
            "Your first goal is to update the order's logistics to reflect a return in progress. You will update the tracking record ('443521489581') by changing the courier to 'Returns Department' and adding a 'checkpoint' event with the note 'Return initiated by customer'. "
            "Next, your goal is to process the exchange itself by replacing the 'Dumbbell Set' at index 0 with a 'Smart Watch' (product '6945232052', variant '2681513500'). "
            "Following this, you must perform a full financial reconciliation by voiding the payment at index 0 and applying a new 'payment' for the correct total of $1885.83 using payment method 'credit_card_5869505'. "
            "To complete the fulfillment of the new item, you will link the tracking ID '749747277477' from her other delivered order '#W1539823', add an 'info' event with the note 'Replacement item dispatched under new tracking', and finally set the order's status to 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "emma_santos_9753", "status": "delivered"},
            ),
            Action(
                name="update_tracking_courier",
                kwargs={"tracking_id": "443521489581", "courier_name": "Returns Department"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "443521489581",
                    "event_status": "checkpoint",
                    "note": "Return initiated by customer",
                },
            ),
            Action(
                name="replace_item_variant_in_order",
                kwargs={
                    "order_id": "#W3113816",
                    "index": 0,
                    "product_id": "6945232052",
                    "item_id": "2681513500",
                },
            ),
            Action(
                name="get_order_financials",
                kwargs={"order_id": "#W3113816"},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3113816", "index": 0},
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W3113816",
                    "transaction_type": "payment",
                    "amount": 1885.83,
                    "payment_method_id": "credit_card_5869505",
                },
            ),
            Action(
                name="find_tracking_by_order",
                kwargs={"order_id": "#W1539823"},
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W3113816", "tracking_id": "749747277477"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "749747277477",
                    "event_status": "info",
                    "note": "Replacement item dispatched under new tracking",
                },
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to manage the supply chain for the 'Gaming Mouse' (product '5713490933', variant '8214883393') from supplier '#SUP0002' and apply dynamic pricing. "
            "You are to approve the priority supply order '#SO6035' while cancelling the non-essential one ('#SO7848'). "
            "Following the approval, you must adjust the product's price to reflect market changes, first increasing it to 85.00 USD. "
            "After you process the receipt of the approved supply order, your task is to implement a sales promotion by reducing the price to 78.00 USD. "
            "To conclude, you must log the value of a customer order ('#W3113816') that contains this item by getting its financial details."
        ),
        actions=[
            Action(
                name="find_supply_orders",
                kwargs={"supplier_id": "#SUP0002", "status": "pending"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO6035", "status": "approved"},
            ),
            Action(
                name="set_supply_order_status",
                kwargs={"supply_order_id": "#SO7848", "status": "cancelled"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 85.00},
            ),
            Action(
                name="receive_supply_order_and_close",
                kwargs={"supply_order_id": "#SO6035"},
            ),
            Action(
                name="update_product_variant_price",
                kwargs={"product_id": "5713490933", "item_id": "8214883393", "new_price": 78.00},
            ),
            Action(
                name="get_order_financials",
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
            "Your task is to perform a complete account archival for customer 'Sofia Hernandez' (user_id 'sofia_hernandez_5364'). "
            "The archival policy requires archiving all non-essential orders. "
            "You will process her pending order '#W9609649' by removing its 5 items (indices 0-4) and its payment at index 0, then setting the status to 'cancelled'. "
            "You will apply the same archival process to her other pending order '#W3561391' by removing its 1 item (index 0) and its payment at index 0 before cancelling. "
            "Finally, you will archive her processed order '#W5765741' by removing its 2 items (indices 0-1) and its payment at index 0 and marking it 'cancelled'."
        ),
        actions=[
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W9609649", "indices": [0, 1, 2, 3, 4]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W9609649", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W9609649", "status": "cancelled"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W3561391", "indices": [0]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W3561391", "index": 0},
            ),
            Action(
                name="set_order_status",
                kwargs={"order_id": "#W3561391", "status": "cancelled"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W5765741", "indices": [0, 1]},
            ),
            Action(
                name="remove_payment_by_index",
                kwargs={"order_id": "#W5765741", "index": 0},
            ),
            Action(
                name="set_order_status",
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
            "Your objective is to reactivate and fulfill a cancelled order for 'Anya Garcia' (user_id 'anya_garcia_3271'). The order, '#W4140680', needs to be reopened and its contents completely replaced. "
            "You are to clear all of its three original items and then add two new ones: a 'Smart Watch' (product '6945232052', variant '9408160950') and a 'T-Shirt' (product '9523456873', variant '8124970213'). "
            "After updating the items, you must reconcile the finances by applying a 'payment' transaction for $289.98 using her payment method 'pm-anya-card-1'. "
            "For fulfillment, you will link the tracking ID '951786982868' from her order '#W6310710' and add an 'info' type event with the exact note 'New items added to shipment'. "
            "Finally, you must ensure the order is marked as 'processed'."
        ),
        actions=[
            Action(
                name="find_orders_by_user_and_status",
                kwargs={"user_id": "anya_garcia_3271", "status": "cancelled"},
            ),
            Action(
                name="reopen_cancelled_order",
                kwargs={"order_id": "#W4140680"},
            ),
            Action(
                name="remove_items_by_index",
                kwargs={"order_id": "#W4140680", "indices": [0, 1, 2]},
            ),
            Action(
                name="add_items_to_order",
                kwargs={
                    "order_id": "#W4140680",
                    "items": [
                        {"product_id": "6945232052", "item_id": "9408160950", "quantity": 1},
                        {"product_id": "9523456873", "item_id": "8124970213", "quantity": 1},
                    ],
                },
            ),
            Action(
                name="append_payment",
                kwargs={
                    "order_id": "#W4140680",
                    "transaction_type": "payment",
                    "amount": 289.98,
                    "payment_method_id": "pm-anya-card-1",
                },
            ),
            Action(
                name="link_existing_tracking_to_order",
                kwargs={"order_id": "#W4140680", "tracking_id": "951786982868"},
            ),
            Action(
                name="add_tracking_custom_event",
                kwargs={
                    "tracking_id": "951786982868",
                    "event_status": "info",
                    "note": "New items added to shipment",
                },
            ),
            Action(
                name="set_order_status",
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
