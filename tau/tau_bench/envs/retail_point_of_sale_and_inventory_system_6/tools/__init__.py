# Copyright Sierra

from .find_discountable_products import find_discountable_products
from .update_stock_quantity import update_stock_quantity
from .check_low_stock_items import check_low_stock_items
from .get_detailed_item_price import get_detailed_item_price
from .find_check_out_employee import find_check_out_employee
from .transaction_price_info import transaction_price_info
from .make_transaction import make_transaction
from .find_transaction import find_transaction
from .cancel_promotion import cancel_promotion
from .create_promotion import create_promotion
from .find_promotions import find_promotions
from .create_customer import create_customer
from .remove_customer import remove_customer
from .find_customers import find_customers
from .update_customer import update_customer
from .create_employee import create_employee
from .remove_employee import remove_employee
from .find_employees import find_employees
from .update_employee import update_employee
from .create_inventory import create_inventory
from .remove_inventory import remove_inventory
from .find_items import find_items
from .create_product import create_product
from .remove_product import remove_product
from .find_products import find_products
from .get_profit_margins import get_profit_margins
from .get_top_selling_items import get_top_selling_items

ALL_TOOLS = [
    find_discountable_products,
    update_stock_quantity,
    check_low_stock_items,
    get_detailed_item_price,
    find_check_out_employee,
    transaction_price_info,
    make_transaction,
    find_transaction,
    cancel_promotion,
    create_promotion,
    find_promotions,
    create_customer,
    remove_customer,
    find_customers,
    update_customer,
    create_employee,
    remove_employee,
    find_employees,
    update_employee,
    create_inventory,
    remove_inventory,
    find_items,
    create_product,
    remove_product,
    find_products,
    get_profit_margins,
    get_top_selling_items,
]
