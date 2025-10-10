import json
from typing import Dict, Any, List
from domains.dto import Tool


def _find_order(data, order_id):
    return next((o for o in data.get('orders', []) if o.get('order_id') == order_id), None)

def _find_user(data, user_id):
    return next((u for u in data.get('users', []) if u.get('user_id') == user_id), None)

def _find_tracking(data, tracking_id):
    return next((t for t in data.get('tracking', []) if tracking_id in t.get('tracking_id', [])), None)

def _find_courier(data, courier_id):
    return next((c for c in data.get('couriers', []) if c.get('courier_id') == courier_id), None)

def _find_product_by_item(data, item_id):
    for p in data.get('products', []):
        variants = p.get('variants', {})
        if item_id in variants:
            return p, variants[item_id]
    return None, None

def _ensure_list(dct, key):
    if key not in dct or not isinstance(dct[key], list):
        dct[key] = []
    return dct[key]

class GetUserById(Tool):
    """Get a user by user_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error": "user_id is required"}, indent=2)
        user = _find_user(data, user_id)
        return json.dumps(user or {"error": f"user_id {user_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_user_by_id","description":"Return the user object by user_id.","parameters":{"type":"object","properties":{"user_id":{"type":"string"}},"required":["user_id"]}}}

class FindUsersByCity(Tool):
    """List users in a given city (exact match)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        city = kwargs.get('city')
        if not city:
            return json.dumps({"error":"city is required"}, indent=2)
        users = data.get('users', [])
        out = [u for u in users if u.get('address',{}).get('city') == city]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"find_users_by_city","description":"Find all users whose address.city equals the given city.","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}

class UpdateUserAddress(Tool):
    """Update a user's address to the provided fields."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        user_id = kwargs.get('user_id')
        address = kwargs.get('address')
        if not user_id or not isinstance(address, dict):
            return json.dumps({"error":"user_id and address (object) are required"}, indent=2)
        user = _find_user(data, user_id)
        if not user:
            return json.dumps({"error":f"user_id {user_id} not found"}, indent=2)
        user['address'] = address
        return json.dumps({"success": True, "user_id": user_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_user_address","description":"Replace a user's address with the provided object.","parameters":{"type":"object","properties":{"user_id":{"type":"string"},"address":{"type":"object"}},"required":["user_id","address"]}}}

class AddPaymentMethod(Tool):
    """Attach a payment method record to a user. Must include a stable id in payload."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        user_id = kwargs.get('user_id')
        payment = kwargs.get('payment_method')
        if not user_id or not isinstance(payment, dict) or 'id' not in payment:
            return json.dumps({"error":"user_id and payment_method object with 'id' are required"}, indent=2)
        user = _find_user(data, user_id)
        if not user:
            return json.dumps({"error":f"user_id {user_id} not found"}, indent=2)
        pm = user.setdefault('payment_methods', {})
        pm[payment['id']] = payment
        return json.dumps({"success": True, "user_id": user_id, "payment_method_id": payment['id']}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_payment_method","description":"Add/update a payment method on a user. The payload must include a 'id'.","parameters":{"type":"object","properties":{"user_id":{"type":"string"},"payment_method":{"type":"object"}},"required":["user_id","payment_method"]}}}

class GetProductById(Tool):
    """Return a product by product_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        product_id = kwargs.get('product_id')
        if not product_id:
            return json.dumps({"error":"product_id is required"}, indent=2)
        prod = next((p for p in data.get('products', []) if p.get('product_id') == product_id), None)
        return json.dumps(prod or {"error": f"product_id {product_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_product_by_id","description":"Get a product by product_id.","parameters":{"type":"object","properties":{"product_id":{"type":"string"}},"required":["product_id"]}}}

class GetItemVariant(Tool):
    """Return product and variant by item_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        item_id = kwargs.get('item_id')
        if not item_id:
            return json.dumps({"error":"item_id is required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        return json.dumps({"product_id": prod['product_id'], "variant": variant}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_item_variant","description":"Return the variant record and product_id for a given item_id.","parameters":{"type":"object","properties":{"item_id":{"type":"string"}},"required":["item_id"]}}}

class SetVariantAvailability(Tool):
    """Set a variant's 'available' flag."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        item_id = kwargs.get('item_id')
        available = kwargs.get('available')
        if item_id is None or available is None:
            return json.dumps({"error":"item_id and available are required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        prod['variants'][item_id]['available'] = bool(available)
        return json.dumps({"success": True, "item_id": item_id, "available": bool(available)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"set_variant_availability","description":"Set the boolean 'available' flag for a variant.","parameters":{"type":"object","properties":{"item_id":{"type":"string"},"available":{"type":"boolean"}},"required":["item_id","available"]}}}

class SetVariantPrice(Tool):
    """Set a variant's price to a specified numeric value."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        item_id = kwargs.get('item_id')
        price = kwargs.get('price')
        if item_id is None or price is None:
            return json.dumps({"error":"item_id and price are required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        prod['variants'][item_id]['price'] = float(price)
        return json.dumps({"success": True, "item_id": item_id, "price": float(price)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"set_variant_price","description":"Set a specific variant price.","parameters":{"type":"object","properties":{"item_id":{"type":"string"},"price":{"type":"number"}},"required":["item_id","price"]}}}

class SearchProductsByName(Tool):
    """Case-insensitive substring name search (read-only)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        q = kwargs.get('query','').lower()
        out = [p for p in data.get('products', []) if q in p.get('name','').lower()]
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"search_products_by_name","description":"Search products by name (case-insensitive contains).","parameters":{"type":"object","properties":{"query":{"type":"string"}}}}}

class GetOrderDetails(Tool):
    """Return an order by ID."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        if not order_id:
            return json.dumps({"error":"order_id is required"}, indent=2)
        order = _find_order(data, order_id)
        return json.dumps(order or {"error": f"order_id {order_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_order_details","description":"Fetch an order by ID.","parameters":{"type":"object","properties":{"order_id":{"type":"string"}},"required":["order_id"]}}}

class UpdateOrderStatus(Tool):
    """Set order status to provided value."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        status = kwargs.get('status')
        if not order_id or status is None:
            return json.dumps({"error":"order_id and status are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        o['status'] = status
        return json.dumps({"success": True, "order_id": order_id, "status": status}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_order_status","description":"Update the status field on an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"status":{"type":"string"}},"required":["order_id","status"]}}}

class AddOrderPayment(Tool):
    """Append a payment record."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        amount = kwargs.get('amount')
        payment_method_id = kwargs.get('payment_method_id')
        txn_id = kwargs.get('transaction_id')
        if not order_id or amount is None or not payment_method_id or not txn_id:
            return json.dumps({"error":"order_id, amount, payment_method_id, transaction_id are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        hist = _ensure_list(o, 'payment_history')
        # idempotent: replace existing by same txn_id
        existing = next((h for h in hist if h.get('transaction_id') == txn_id), None)
        record = {"transaction_type":"payment","amount": float(amount),"payment_method_id": payment_method_id,"transaction_id": txn_id}
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        return json.dumps({"success": True, "order_id": order_id, "transaction_id": txn_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_order_payment","description":"Add or upsert a payment record for an order (by transaction_id).","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"amount":{"type":"number"},"payment_method_id":{"type":"string"},"transaction_id":{"type":"string"}},"required":["order_id","amount","payment_method_id","transaction_id"]}}}

class RefundOrderPayment(Tool):
    """Append a refund record with provided refund_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        amount = kwargs.get('amount')
        reason_code = kwargs.get('reason_code')
        refund_id = kwargs.get('refund_id')
        if not order_id or amount is None or not reason_code or not refund_id:
            return json.dumps({"error":"order_id, amount, reason_code, refund_id are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        hist = _ensure_list(o, 'payment_history')
        existing = next((h for h in hist if h.get('refund_id') == refund_id), None)
        record = {"transaction_type":"refund","amount": float(amount),"reason_code": reason_code,"refund_id": refund_id}
        if existing:
            existing.update(record)
        else:
            hist.append(record)
        return json.dumps({"success": True, "order_id": order_id, "refund_id": refund_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"refund_order_payment","description":"Add or upsert a refund record for an order (by refund_id).","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"amount":{"type":"number"},"reason_code":{"type":"string"},"refund_id":{"type":"string"}},"required":["order_id","amount","reason_code","refund_id"]}}}

class CancelOrderItems(Tool):
    """Mark specific items in an order as cancelled with a reason_code (adds 'cancelled': True)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        item_ids = kwargs.get('item_ids', [])
        reason_code = kwargs.get('reason_code')
        if not order_id or not item_ids or not reason_code:
            return json.dumps({"error":"order_id, item_ids, reason_code are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        updated = []
        for item in o.get('items', []):
            if item.get('item_id') in item_ids:
                item['cancelled'] = True
                item['cancellation_reason'] = reason_code
                updated.append(item['item_id'])
        return json.dumps({"success": True, "order_id": order_id, "cancelled_item_ids": updated, "reason_code": reason_code}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"cancel_order_items","description":"Mark given item_ids in an order as cancelled with a reason_code.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}},"reason_code":{"type":"string"}},"required":["order_id","item_ids","reason_code"]}}}

class UpdateItemOption(Tool):
    """Update a specific option key for a given item in an order."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        item_id = kwargs.get('item_id')
        option_key = kwargs.get('option_key')
        option_value = kwargs.get('option_value')
        if not order_id or not item_id or option_key is None or option_value is None:
            return json.dumps({"error":"order_id, item_id, option_key, option_value are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        it = next((i for i in o.get('items', []) if i.get('item_id') == item_id), None)
        if not it:
            return json.dumps({"error":f"item_id {item_id} not in order {order_id}"}, indent=2)
        opts = it.setdefault('options', {})
        opts[option_key] = option_value
        return json.dumps({"success": True, "order_id": order_id, "item_id": item_id, "option_key": option_key, "option_value": option_value}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_item_option","description":"Update a single option on an order item.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_id":{"type":"string"},"option_key":{"type":"string"},"option_value":{}},"required":["order_id","item_id","option_key","option_value"]}}}

class AddOrderTag(Tool):
    """Add a tag string to an order (idempotent)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        tag = kwargs.get('tag')
        if not order_id or tag is None:
            return json.dumps({"error":"order_id and tag are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        tags = o.setdefault('order_tags', [])
        if tag not in tags:
            tags.append(tag)
        return json.dumps({"success": True, "order_id": order_id, "tag": tag}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"add_order_tag","description":"Append a tag to order.order_tags if not present.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"tag":{"type":"string"}},"required":["order_id","tag"]}}}

class ComputeOrderTotal(Tool):
    """Compute the sum of item prices for an order (ignores refunds/payments)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        if not order_id:
            return json.dumps({"error":"order_id is required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        total = sum(i.get('price', 0) for i in o.get('items', []))
        return json.dumps({"order_id": order_id, "computed_total": round(float(total),2)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_order_total","description":"Return computed sum of item prices for an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"}},"required":["order_id"]}}}

class GetTrackingInfo(Tool):
    """Return tracking record by tracking_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        if not tracking_id:
            return json.dumps({"error":"tracking_id is required"}, indent=2)
        t = _find_tracking(data, tracking_id)
        return json.dumps(t or {"error": f"tracking_id {tracking_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_tracking_info","description":"Get tracking record by tracking_id.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"}},"required":["tracking_id"]}}}

class AppendTrackingEvent(Tool):
    """Insert/overwrite an event timestamp in tracking_history for a tracking id (key -> timestamp)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        event = kwargs.get('event')
        timestamp = kwargs.get('timestamp')
        if not tracking_id or not event or not timestamp:
            return json.dumps({"error":"tracking_id, event, timestamp are required"}, indent=2)
        t = _find_tracking(data, tracking_id)
        if not t:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        history = t.setdefault('tracking_history', {})
        history[event] = timestamp
        return json.dumps({"success": True, "tracking_id": tracking_id, "event": event, "timestamp": timestamp}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"append_tracking_event","description":"Set an event timestamp in tracking.tracking_history for a given tracking_id.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"event":{"type":"string"},"timestamp":{"type":"string"}},"required":["tracking_id","event","timestamp"]}}}

class LinkTrackingToOrder(Tool):
    """Add a fulfillment record linking tracking_id and item_ids to an order (idempotent by exact tuple)."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        tracking_id = kwargs.get('tracking_id')
        item_ids = kwargs.get('item_ids', [])
        if not order_id or not tracking_id or not item_ids:
            return json.dumps({"error":"order_id, tracking_id, item_ids are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)
        fl = _ensure_list(o, 'fulfillments')
        payload = {"tracking_id":[tracking_id],"item_ids":item_ids}
        if payload not in fl:
            fl.append(payload)
        return json.dumps({"success": True, "order_id": order_id, "tracking_id": tracking_id, "item_ids": item_ids}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"link_tracking_to_order","description":"Append a fulfillment mapping (tracking_id, item_ids) to an order.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"tracking_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}}},"required":["order_id","tracking_id","item_ids"]}}}

class SplitOrderFulfillment(Tool):
    """Create a new tracking record and fulfillment for a subset of items, based on provided tracking_id and courier_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        item_ids = kwargs.get('item_ids', [])
        tracking_id = kwargs.get('tracking_id')
        courier_id = kwargs.get('courier_id')
        delivery_options = kwargs.get('delivery_options', 'Standard')
        address = kwargs.get('address')
        if not order_id or not item_ids or not tracking_id or not courier_id:
            return json.dumps({"error":"order_id, item_ids, tracking_id, courier_id are required"}, indent=2)
        order = _find_order(data, order_id)
        if not order:
            return json.dumps({"error":f"order_id {order_id} not found"}, indent=2)
        # Create or overwrite tracking record
        tr_list = data.setdefault('tracking', [])
        tr = _find_tracking(data, tracking_id)
        if not tr:
            tr = {"tracking_id":[tracking_id], "item_ids": item_ids, "address": address or order.get('address'), "delivery_carrier": courier_id, "delivery_options": delivery_options, "order_id": order_id, "tracking_history": {}}
            tr_list.append(tr)
        else:
            tr['item_ids'] = item_ids
            tr['delivery_carrier'] = courier_id
            tr['delivery_options'] = delivery_options
            tr['order_id'] = order_id
            tr['address'] = address or order.get('address')
        # Link to order fulfillments
        fl = _ensure_list(order, 'fulfillments')
        payload = {"tracking_id":[tracking_id], "item_ids": item_ids}
        if payload not in fl:
            fl.append(payload)
        return json.dumps({"success": True, "order_id": order_id, "tracking_id": tracking_id, "courier_id": courier_id, "item_ids": item_ids}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"split_order_fulfillment","description":"Create a tracking record and link a subset of items to it.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"item_ids":{"type":"array","items":{"type":"string"}},"tracking_id":{"type":"string"},"courier_id":{"type":"string"},"delivery_options":{"type":"string"},"address":{"type":"object"}},"required":["order_id","item_ids","tracking_id","courier_id"]}}}

class GetSupplierDetails(Tool):
    """Read supplier record by supplier_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        supplier_id = kwargs.get('supplier_id')
        if not supplier_id:
            return json.dumps({"error":"supplier_id is required"}, indent=2)
        sup = next((s for s in data.get('suppliers', []) if s.get('supplier_id') == supplier_id), None)
        return json.dumps(sup or {"error": f"supplier_id {supplier_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_supplier_details","description":"Fetch supplier by ID.","parameters":{"type":"object","properties":{"supplier_id":{"type":"string"}},"required":["supplier_id"]}}}

class PlaceSupplyOrder(Tool):
    """Create or update a supply order by provided supply_order_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        supply_order_id = kwargs.get('supply_order_id')
        supplier_id = kwargs.get('supplier_id')
        product_id = kwargs.get('product_id')
        item_id = kwargs.get('item_id')
        quantity = kwargs.get('quantity')
        unit_cost = kwargs.get('unit_cost')
        status = kwargs.get('status', 'pending')
        if not all([supply_order_id, supplier_id, product_id, item_id]) or quantity is None or unit_cost is None:
            return json.dumps({"error":"supply_order_id, supplier_id, product_id, item_id, quantity, unit_cost are required"}, indent=2)
        so_list = data.setdefault('supply_orders', [])
        existing = next((s for s in so_list if s.get('supply_order_id') == supply_order_id), None)
        record = {"supply_order_id": supply_order_id, "supplier_id": supplier_id, "product_id": product_id, "item_id": item_id, "quantity": int(quantity), "status": status, "order_date": "2025-01-01T00:00:00", "unit_cost": float(unit_cost), "total_cost": round(float(unit_cost)*int(quantity),2)}
        if existing:
            existing.update(record)
        else:
            so_list.append(record)
        return json.dumps({"success": True, "supply_order_id": supply_order_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"place_supply_order","description":"Create or overwrite a supply order by supply_order_id.","parameters":{"type":"object","properties":{"supply_order_id":{"type":"string"},"supplier_id":{"type":"string"},"product_id":{"type":"string"},"item_id":{"type":"string"},"quantity":{"type":"integer"},"unit_cost":{"type":"number"},"status":{"type":"string"}},"required":["supply_order_id","supplier_id","product_id","item_id","quantity","unit_cost"]}}}

class UpdateSupplyOrderStatus(Tool):
    """Set status on a supply order."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        supply_order_id = kwargs.get('supply_order_id')
        status = kwargs.get('status')
        if not supply_order_id or not status:
            return json.dumps({"error":"supply_order_id and status are required"}, indent=2)
        so = next((s for s in data.get('supply_orders', []) if s.get('supply_order_id') == supply_order_id), None)
        if not so:
            return json.dumps({"error": f"supply_order_id {supply_order_id} not found"}, indent=2)
        so['status'] = status
        return json.dumps({"success": True, "supply_order_id": supply_order_id, "status": status}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"update_supply_order_status","description":"Update a supply order's status.","parameters":{"type":"object","properties":{"supply_order_id":{"type":"string"},"status":{"type":"string"}},"required":["supply_order_id","status"]}}}

class GetCourierDetails(Tool):
    """Read courier record."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        courier_id = kwargs.get('courier_id')
        if not courier_id:
            return json.dumps({"error":"courier_id is required"}, indent=2)
        c = _find_courier(data, courier_id)
        return json.dumps(c or {"error": f"courier_id {courier_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_courier_details","description":"Fetch courier record by ID.","parameters":{"type":"object","properties":{"courier_id":{"type":"string"}},"required":["courier_id"]}}}

class ReassignCourierForTracking(Tool):
    """Change the delivery_carrier for an existing tracking record."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        courier_id = kwargs.get('courier_id')
        if not tracking_id or not courier_id:
            return json.dumps({"error":"tracking_id and courier_id are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        tr['delivery_carrier'] = courier_id
        return json.dumps({"success": True, "tracking_id": tracking_id, "courier_id": courier_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"reassign_courier_for_tracking","description":"Update delivery_carrier for a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"courier_id":{"type":"string"}},"required":["tracking_id","courier_id"]}}}

class AllocateTrackingId(Tool):
    """Allocate a new tracking_id string based on courier_id and a caller-provided seed."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        courier_id = kwargs.get('courier_id')
        seed = kwargs.get('seed')
        if not courier_id or seed is None:
            return json.dumps({"error":"courier_id and seed are required"}, indent=2)
        new_id = f"TRK-{courier_id.strip('#')}-{str(seed)}"
        return json.dumps({"tracking_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"allocate_tracking_id","description":"Return a tracking id for a courier based on a numeric/string seed.","parameters":{"type":"object","properties":{"courier_id":{"type":"string"},"seed":{}},"required":["courier_id","seed"]}}}

class ScheduleDelivery(Tool):
    """Set a 'scheduled' timestamp in tracking_history."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        scheduled = kwargs.get('scheduled')
        if not tracking_id or not scheduled:
            return json.dumps({"error":"tracking_id and scheduled (ISO string) are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        hist = tr.setdefault('tracking_history', {})
        hist['scheduled'] = scheduled
        return json.dumps({"success": True, "tracking_id": tracking_id, "scheduled": scheduled}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"schedule_delivery","description":"Set scheduled timestamp for a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"scheduled":{"type":"string"}},"required":["tracking_id","scheduled"]}}}

class FraudMarkOrder(Tool):
    """Attach a fraud_check dict to an order."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        order_id = kwargs.get('order_id')
        risk_level = kwargs.get('risk_level')
        reason_code = kwargs.get('reason_code')
        if not order_id or not risk_level or not reason_code:
            return json.dumps({"error":"order_id, risk_level, reason_code are required"}, indent=2)
        o = _find_order(data, order_id)
        if not o:
            return json.dumps({"error": f"order_id {order_id} not found"}, indent=2)
        o['fraud_check'] = {"risk_level": risk_level, "reason_code": reason_code}
        return json.dumps({"success": True, "order_id": order_id, "risk_level": risk_level}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"fraud_mark_order","description":"Mark an order with fraud_check metadata.","parameters":{"type":"object","properties":{"order_id":{"type":"string"},"risk_level":{"type":"string"},"reason_code":{"type":"string"}},"required":["order_id","risk_level","reason_code"]}}}

class ComputeUserFillRate(Tool):
    """Compute a naive fill rate for a user's orders: delivered_items / total_items across all orders."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error":"user_id is required"}, indent=2)
        user_orders = [o for o in data.get('orders', []) if o.get('user_id') == user_id]
        total = sum(len(o.get('items', [])) for o in user_orders)
        delivered = 0
        for o in user_orders:
            # count items in fulfillments for which tracking shows delivered
            for f in o.get('fulfillments', []):
                for tid in f.get('tracking_id', []):
                    tr = _find_tracking(data, tid)
                    if tr and tr.get('tracking_history', {}).get('delivered'):
                        delivered += len(f.get('item_ids', []))
        rate = (delivered/total) if total else 0.0
        return json.dumps({"user_id": user_id, "fill_rate": round(rate,4)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"compute_user_fill_rate","description":"Compute delivered item share across a user's orders.","parameters":{"type":"object","properties":{"user_id":{"type":"string"}},"required":["user_id"]}}}

class UpsertTrackingAddress(Tool):
    """Update the address on a tracking record."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        tracking_id = kwargs.get('tracking_id')
        address = kwargs.get('address')
        if not tracking_id or not isinstance(address, dict):
            return json.dumps({"error":"tracking_id and address (object) are required"}, indent=2)
        tr = _find_tracking(data, tracking_id)
        if not tr:
            return json.dumps({"error": f"tracking_id {tracking_id} not found"}, indent=2)
        tr['address'] = address
        return json.dumps({"success": True, "tracking_id": tracking_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"upsert_tracking_address","description":"Replace address on a tracking record.","parameters":{"type":"object","properties":{"tracking_id":{"type":"string"},"address":{"type":"object"}},"required":["tracking_id","address"]}}}

# Export tool instances
TOOLS = [
    GetUserById(),
    FindUsersByCity(),
    UpdateUserAddress(),
    AddPaymentMethod(),
    GetProductById(),
    GetItemVariant(),
    SetVariantAvailability(),
    SetVariantPrice(),
    SearchProductsByName(),
    GetOrderDetails(),
    UpdateOrderStatus(),
    AddOrderPayment(),
    RefundOrderPayment(),
    CancelOrderItems(),
    UpdateItemOption(),
    AddOrderTag(),
    ComputeOrderTotal(),
    GetTrackingInfo(),
    AppendTrackingEvent(),
    LinkTrackingToOrder(),
    SplitOrderFulfillment(),
    GetSupplierDetails(),
    PlaceSupplyOrder(),
    UpdateSupplyOrderStatus(),
    GetCourierDetails(),
    ReassignCourierForTracking(),
    AllocateTrackingId(),
    ScheduleDelivery(),
    FraudMarkOrder(),
    ComputeUserFillRate(),
    UpsertTrackingAddress()
]
