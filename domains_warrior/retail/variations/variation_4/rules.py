RULES = [
    "Validate user identity exists before processing any user requests",
    "Check product availability status before allocation - never allocate unavailable items",
    "Gift card payments cannot exceed available balance - verify balance sufficiency before processing",
    "Only process orders with valid status: pending, processed, delivered, cancelled, for return",
    "Assign couriers only if destination country matches their coverage areas",
    "Use exact variant pricing from product catalog - no unauthorized price modifications",
    "Assign tracking numbers only from courier's available tracking pools",
    "Validate all required address fields: address1, city, country, state, zip",
    "Confirm item_id exists in product variants before including in orders",
    "Payment methods must be valid type: credit_card, paypal, or gift_card with sufficient balance",
    "Multi-item orders need all items available before confirmation",
    "Supply orders must reference valid supplier_id and existing product_id",
    "Order fulfillments require valid tracking_id from assigned courier",
    "Credit card payments must validate last_four digits and brand type match user's stored payment methods",
    "Prioritize customer service requests over internal operations",
    "Maintain data integrity: order totals must match sum of item prices"
]
