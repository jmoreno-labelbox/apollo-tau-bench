from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ValidateSupplierCapacity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str) -> str:
        """
        Validate supplier capacity and order status for procurement planning

        Data Sources: supply_orders.json (supplier_id, status, quantity, total_cost, order_date)
        """
        supply_orders = data.get("supply_orders", [])
        supplier_orders = [
            order for order in supply_orders if order.get("supplier_id") == supplier_id
        ]

        if not supplier_orders:
            payload = {
                "error": f"No supply orders found for supplier {supplier_id}",
                "status": "not_found",
            }
            out = json.dumps(payload)
            return out

        # Rule: Supply orders must reference valid supplier_id and existing product_id
        # Rule: Supply orders with status 'cancelled' require alternative sourcing and cannot be fulfilled
        pending_orders = []
        fulfilled_orders = []
        cancelled_orders = []

        for order in supplier_orders:
            status = order.get("status")
            if status == "pending":
                pending_orders.append(order)
            elif status == "fulfilled":
                fulfilled_orders.append(order)
            elif status == "cancelled":
                cancelled_orders.append(order)

        # Calculate capacity metrics
        total_pending_quantity = sum(order.get("quantity", 0) for order in pending_orders)
        total_fulfilled_quantity = sum(order.get("quantity", 0) for order in fulfilled_orders)
        total_cancelled_quantity = sum(order.get("quantity", 0) for order in cancelled_orders)

        total_pending_cost = sum(order.get("total_cost", 0) for order in pending_orders)
        total_fulfilled_cost = sum(order.get("total_cost", 0) for order in fulfilled_orders)

        # Calculate reliability metrics
        total_completed_orders = len(fulfilled_orders) + len(cancelled_orders)
        fulfillment_rate = (
            (len(fulfilled_orders) / total_completed_orders * 100)
            if total_completed_orders > 0
            else 0
        )

        # Generate rating and feedback based on fulfillment rate
        def get_supplier_rating_and_feedback(fulfillment_rate_percent):
            if fulfillment_rate_percent >= 90:
                return {
                    "rating": "Excellent",
                    "numeric_score": 5.0,
                    "feedback": "Outstanding performance with exceptional reliability. This supplier consistently delivers on commitments and is highly recommended for critical orders.",
                    "recommendation": "Preferred supplier - suitable for all order types including high-priority items.",
                }
            elif fulfillment_rate_percent >= 80:
                return {
                    "rating": "Good",
                    "numeric_score": 4.0,
                    "feedback": "Strong performance with good reliability. Minor fulfillment issues but generally dependable for most orders.",
                    "recommendation": "Reliable supplier - good choice for standard orders with some monitoring recommended.",
                }
            elif fulfillment_rate_percent >= 70:
                return {
                    "rating": "Fair",
                    "numeric_score": 3.0,
                    "feedback": "Moderate performance with some reliability concerns. Fulfillment rate indicates room for improvement in delivery consistency.",
                    "recommendation": "Caution advised - suitable for non-critical orders with backup sourcing options.",
                }
            elif fulfillment_rate_percent >= 50:
                return {
                    "rating": "Poor",
                    "numeric_score": 2.0,
                    "feedback": "Below-average performance with significant reliability issues. High cancellation rate may impact supply chain stability.",
                    "recommendation": "High risk supplier - avoid for critical orders and consider alternative sourcing.",
                }
            else:
                return {
                    "rating": "Unacceptable",
                    "numeric_score": 1.0,
                    "feedback": "Unacceptable performance with very poor reliability. Frequent order cancellations pose serious supply chain risks.",
                    "recommendation": "Not recommended - seek immediate alternative suppliers for all future orders.",
                }

        # Get supplier rating and feedback
        rating_info = get_supplier_rating_and_feedback(fulfillment_rate)

        # Calculate additional performance insights
        def get_performance_insights(
            fulfillment_rate_percent, total_orders, cancelled_count
        ):
            insights = []

            if total_orders < 5:
                insights.append(
                    "Limited order history - rating based on small sample size"
                )

            if cancelled_count > 0:
                cancellation_rate = (
                    cancelled_count / (total_orders if total_orders > 0 else 1)
                ) * 100
                if cancellation_rate > 20:
                    insights.append(
                        f"High cancellation rate ({cancellation_rate:.1f}%) indicates potential capacity or reliability issues"
                    )
                elif cancellation_rate > 10:
                    insights.append(
                        f"Moderate cancellation rate ({cancellation_rate:.1f}%) requires monitoring"
                    )

            if fulfillment_rate_percent == 100 and total_orders >= 10:
                insights.append(
                    "Perfect fulfillment record demonstrates exceptional reliability"
                )

            if fulfillment_rate_percent > 0 and len(pending_orders) > 0:
                insights.append(
                    f"Currently has {len(pending_orders)} pending orders requiring attention"
                )

            return insights

        performance_insights = get_performance_insights(
            fulfillment_rate, len(supplier_orders), len(cancelled_orders)
        )

        result = {
            "status": "success",
            "supplier_id": supplier_id,
            "order_summary": {
                "total_orders": len(supplier_orders),
                "pending_orders": len(pending_orders),
                "fulfilled_orders": len(fulfilled_orders),
                "cancelled_orders": len(cancelled_orders),
            },
            "quantity_metrics": {
                "pending_quantity": total_pending_quantity,
                "fulfilled_quantity": total_fulfilled_quantity,
                "cancelled_quantity": total_cancelled_quantity,
            },
            "cost_metrics": {
                "pending_value": round(total_pending_cost, 2),
                "fulfilled_value": round(total_fulfilled_cost, 2),
            },
            "reliability": {
                "fulfillment_rate_percent": round(fulfillment_rate, 1),
                "requires_alternative_sourcing": len(cancelled_orders) > 0,
            },
            "performance_rating": {
                "overall_rating": rating_info["rating"],
                "numeric_score": rating_info["numeric_score"],
                "performance_feedback": rating_info["feedback"],
                "sourcing_recommendation": rating_info["recommendation"],
                "performance_insights": performance_insights,
            },
            "recent_orders": (
                supplier_orders[-5:] if len(supplier_orders) >= 5 else supplier_orders
            ),
        }
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateSupplierCapacity",
                "description": "Validate supplier capacity and reliability for procurement planning with performance rating based on fulfillment rate",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "Supplier identifier (e.g., '#SUP0001')",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
