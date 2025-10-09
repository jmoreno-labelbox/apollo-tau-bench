WIKI = """
"Consistently utilize 'finder' tools (such as `find_warehouse_by_name`, `find_product_by_name`, `find_supplier_by_name`) to convert user-provided, human-readable names into the corresponding IDs needed by other tools.",
    "Prior to initiating any outbound order, confirm that the designated fulfillment warehouse holds enough 'quantity_available' of the product.",
    "Directly following the creation of an outbound order, utilize the `update_inventory_allocated_quantity` tool to adjust the allocated quantity for each SKU in that order, thereby maintaining real-time stock accuracy.",
    "Directly after generating an inbound shipment (purchase order), employ the `update_inventory_inbound_quantity` tool to update the inbound quantity for the corresponding SKU, ensuring the incoming pipeline is accurately reflected.",
    "If no explicit cost constraint (such as 'cheapest' or 'economical') is specified when choosing a carrier, you must use the relevant finder tool to select the carrier with the highest `average_rating`.",
    "To prevent duplicate data, do not create a new inventory record for a SKU in a warehouse if one already exists there; always use `find_inventory_by_sku` to verify beforehand.",
    "When several warehouses can fulfill an order with adequate stock, select the warehouse with the greatest `quantity_available` to reduce the likelihood of stock-outs for other orders, except when warehouse capabilities require a different choice.",
    "To process a user's inventory adjustment request, utilize the `perform_inventory_adjustment` tool, ensuring that you first determine the `current_allocated_quantity` so the updated `quantity_available` is computed accurately.",
    "The full purchase order workflow consists of: 1. Selecting the product, supplier, and destination warehouse. 2. Determining the expected arrival date. 3. Generating the inbound shipment record. 4. Modifying the inventory's inbound quantity.",
    "For appending notes to an existing record, apply the relevant 'update' tool (such as `update_shipment_notes` or `update_outbound_order_details`) to add the information while maintaining the audit trail.",
    "When a stock-out hinders order fulfillment from the primary warehouse, the normal process involves checking for alternative warehouse locations. If no alternatives exist, it is necessary to determine the earliest delivery date from the primary supplier to guide subsequent actions.",
"""
