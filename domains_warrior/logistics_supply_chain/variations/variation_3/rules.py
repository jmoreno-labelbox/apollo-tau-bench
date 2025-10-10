RULES = [
    "Always use 'finder' tools (e.g., `find_warehouse_by_name`, `find_product_by_name`, `find_supplier_by_name`) to resolve human-readable names from the user's prompt into the IDs required by other tools.",
    "Before creating any outbound order, you must first verify that there is sufficient 'quantity_available' of the product at the designated fulfillment warehouse.",
    "Immediately after creating an outbound order, you must update the allocated quantity for each SKU in that order using the `update_inventory_allocated_quantity` tool to ensure real-time stock accuracy.",
    "Immediately after creating an inbound shipment (purchase order), you must update the inbound quantity for the relevant SKU using the `update_inventory_inbound_quantity` tool to reflect the incoming pipeline.",
    "When selecting a carrier and no specific cost constraint (e.g., 'cheapest', 'economical') is given, you must prioritize the carrier with the highest `average_rating` using the appropriate finder tool.",
    "To avoid data duplication, never create a new inventory record for a SKU in a warehouse where one already exists. Use `find_inventory_by_sku` to check first.",
    "If multiple warehouses have sufficient stock to fulfill an order, prioritize the one with the highest `quantity_available` to minimize the risk of stock-outs for other orders, unless warehouse capabilities dictate otherwise.",
    "When a user requests an inventory adjustment, you must use the `perform_inventory_adjustment` tool, which requires first finding the `current_allocated_quantity` to ensure the new `quantity_available` is calculated correctly.",
    "A complete purchase order process involves: 1. Identifying the product, supplier, and destination warehouse. 2. Calculating the expected arrival date. 3. Creating the inbound shipment record. 4. Updating the inventory's inbound quantity.",
    "When adding notes to an existing record, use the appropriate 'update' tool (e.g., `update_shipment_notes`, `update_outbound_order_details`) to append information, preserving the audit trail.",
    "If a stock-out prevents order fulfillment from the primary warehouse, the standard procedure is to check for alternate warehouse locations. If no alternate is available, you must calculate the earliest possible delivery date from the primary supplier to inform the next steps.",
]
