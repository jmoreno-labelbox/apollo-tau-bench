RULES = [
    "Resolve the customer first. If email is provided, use get_contact_by_email; otherwise use get_contact_by_name (exact first/last).",
    "Reuse returned IDs exactly (contact_id, account_id, cart_id, order_id). Never invent IDs.",
    "Quantities passed to tools must be positive whole numbers.",
    "Use tool-computed money values as authoritative (Python round(x, 2)); never recompute externally.",
    "When a product is named in instructions, find it deterministically with get_product_by_name.",
    "When a category is given, list products for that category and apply the same deterministic ordering.",
    "Do not proceed with items lacking sufficient stock; follow Case SOP (Pending) for stock issues.",
    "Create a cart with create_cart(contact_id). The system assigns cart_id.",
    "Add items with add_item_to_cart(cart_id, product_id, qty). The tool merges duplicates.",
    "When you need a cart_item_id (for edits), call list_cart_items(cart_id) and then set_item_quantity.",
    "Remove items with remove_item_from_cart(cart_id, product_id).",
    "Pricing context resolves in this order: cart.override_pricebook_id if set; else the account default from get_default_pricebook_for_account(account_id); else pricebook '1' if present.",
    "Switch pricebook via set_cart_pricebook(cart_id, pricebook_id) when required before applying offers.",
    "If the instruction names a specific offer code, you may fetch it with get_offer_by_code(code) and apply if is_active.",
    "If instruction vaguely mentions some promo, list_active_offers() and deterministically pick the single offer producing the largest discount on the current subtotal (break ties by lexicographically smallest offer_code).",
    "You apply offers with apply_offer_to_cart(cart_id, offer_code) only when is_active is true.",
    "Never auto-apply 'WINTER20' unless explicitly requested.",
    "If offer application fails or yields no improvement, follow Case SOP (Pending) with the Offer Failure subject.",
    "Never create an order from an empty cart; this is an error path handled by Case SOP (Pending, Empty-Cart subject).",
    "Call create_order(cart_id[, order_id]) to place; if order_id omitted, the system assigns next numeric order_id.",
    "If create_order reports 'Missing pricebook entry.' or stock errors, treat as failed placement and follow Case SOP (Pending with specific subject).",
    "Verify placed lines with list_order_items(order_id).",
    "Set or correct shipping with set_order_shipping_address(order_id, full_address) when the instruction implies shipping to be used by using the shipping_address in the account information using get_account_by_id.",
    "To cancel: cancel_order(order_id). If cancellation is blocked by status, follow Case SOP Pending (Not Cancelable).",
    "Return flows require an order_id and the exact product_id(s)/qty to return.",
    "Map product names to product_id via get_product_by_name/search; find the most recent delivered order containing that product (prefer newest order_date).",
    "Validate eligibility with validate_return_eligibility(order_id). If ineligible, do not call return_order; follow Case SOP (Pending, Ineligible Return subject).",
    "If eligible, call return_order(order_id, lines=[{product_id, qty}, ...]). The tool restocks and reduces order.total_amount by the computed refund.",
    "Full refund: refund_order_full(order_id) which zeroes order.total_amount and returns refunded_amount.",
    "Partial refund: refund_order_partial(order_id, amount) with amount ∈ [0, current_total].",
    "After any refund, you may read the order to confirm the new total and record that value per Case SOP notes.",
    "Before opening any case, ensure all IDs required by the subject exist. If the scenario logically requires an order_id (returns, refunds, cancellations, shipping correction), locate the correct order first. If the task is about creating an order, place it before opening any resulting case that needs that order_id.",
    "Open a case at the start of user-impacting service flows that require tracking or may fail: returns, cancellations, refunds, address corrections, delivery issues, billing issues, offer application failures, order placement failures (empty cart, missing pricebook entries, stock), quotes prepared, and replacements/corrections.",
    "Subjects for common flows: "
    "Return start: 'Return request for Order #{order_id}'; "
    "Return success: 'Return processed for Order #{order_id}'; "
    "Return ineligible: 'Return Request Failed: Order #{order_id} not eligible'; "
    "Order placed: 'Order Placed: Order #{order_id}'; "
    "Order fail (missing pricebook): 'Order Placement Failed: Order #{order_id} missing pricebook entry'; "
    "Order fail (stock): 'Order Placement Failed: Insufficient stock for Order #{order_id}'; "
    "Order fail (empty cart): 'Order Placement Failed: Cart #{cart_id} has no items'; "
    "Address correction: 'Address Correction: Order #{order_id}'; "
    "Cancellation done: 'Cancellation completed for Order #{order_id}'; "
    "Cancellation fail: 'Cancellation Failed: Order #{order_id} not cancelable'; "
    "Offer success: 'Offer Applied: {offer_code} on Cart #{cart_id}'; "
    "Offer fail: 'Offer Application Failed: {offer_code}'; "
    "Quote: 'Quote Prepared: Cart #{cart_id} Total ${total_amount}'; "
    "Cart pruned: 'Cart Pruned to Requested Item: Cart #{cart_id}'; "
    "Cart emptied: 'Cart Emptied: Cart #{cart_id}'; "
    "Billing: 'Billing Inquiry: Order #{order_id}'; "
    "Delivery issue: 'Delivery Issue: Order #{order_id} (Package not received)'; "
    "Replacement: 'Replacement/Correction: Order #{order_id} ({short_reason})'; "
    "Full refund: 'Full Refund Issued: Order #{order_id} ${refunded_amount}'; "
    "Partial refund: 'Partial Refund Issued: Order #{order_id} ${refunded_amount}'.",
    "Every new case starts 'New'. Use 'Pending' when business rules block the requested action. Move to 'Resolved' only when the user’s stated concern is fully addressed.",
    "When multiple candidate orders exist, pick the most recent by order_date (ISO descending).",
    "When multiple contacts match a name, pick the lowest numeric contact_id.",
    "List current clusters with list_elasticache_clusters to understand state.",
    "Provision a cluster with provision_elasticache_cluster(cluster_id, cluster_name, endpoint_url|'NULL', status, instance_type, security_group_id).",
    "Resize capacity with update_elasticache_cluster_config(cluster_id, node_type, num_nodes).",
    "Change instance class with update_elasticache_instance_type(cluster_id, instance_type).",
    "Delete/decommission by delete_elasticache_cluster(cluster_id) (status becomes Deleted).",
    "Manage subnet groups with list_subnet_groups, create_subnet_group, get_subnet_group, update_subnet_group_description.",
    "Manage network access with list_security_group_rules and add_security_group_rule(security_group_id, protocol, port, source_ip, description).",
    "Always use the exact sgr-* ID returned when referencing a security group rule.",
    "If a required tool fails or returns a blocking message, do not improvise alternate flows; follow Case SOP Pending with the specific failure subject.",
]
