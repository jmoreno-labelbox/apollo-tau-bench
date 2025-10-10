# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTransactionTotals(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        line_items = kwargs.get('line_items', [])
        promotion_ids = kwargs.get('promotion_ids', [])
        credit_amount = kwargs.get('credit_amount', 0.0)

        products = list(data.get("products", {}).values())  # Corrigido para lista
        promotions = data.get("promotions", [])  # Corrigido para lista

        subtotal = 0.0
        total_discount = 0.0
        final_line_items = []

        for item in line_items:
            sku = item.get('sku')
            quantity = item.get('quantity')
            product_details = next((p for p in products if p['sku'] == sku), None)

            if not product_details:
                continue

            price = product_details.get('price', 0.0)
            item_subtotal = price * quantity
            subtotal += item_subtotal

            item_discount_value = 0.0

            for promo_id in promotion_ids:
                promo = next((p for p in promotions if p['promotion_id'] == promo_id), None)
                if promo and sku in promo.get('applicable_skus', []):
                    if promo.get('type') == 'percentage':
                        item_discount_value = item_subtotal * (promo.get('discount_value', 0.0) / 100.0)

            total_discount += item_discount_value
            final_line_items.append({
                "sku": sku,
                "quantity": quantity,
                "unit_price": price,
                "discount": round(item_discount_value / quantity, 2) if quantity > 0 else 0.0
            })

        subtotal_after_discount = subtotal - total_discount
        final_subtotal = subtotal_after_discount - credit_amount

        tax_rate = 0.0825
        total_tax = final_subtotal * tax_rate
        final_total = final_subtotal + total_tax

        return json.dumps({
            "calculated_total_amount": round(final_total, 2),
            "calculated_tax_amount": round(total_tax, 2),
            "calculated_discount_total": round(total_discount, 2),
            "calculated_line_items": final_line_items
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_transaction_totals",
                "description": "Calculates the final total, tax, and discount for a transaction based on items, promotions, and credits.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "line_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string"},
                                    "quantity": {"type": "integer"}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "promotion_ids": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "credit_amount": {"type": "number"}
                    },
                    "required": ["line_items"],
                },
            },
        }
