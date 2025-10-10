# Copyright Sierra

from .search_products import SearchProducts
from .get_customer_details import GetCustomerDetails
from .get_product_details_by_sku import GetProductDetailsBySKU
from .list_all_products import ListAllProducts
from .list_products_by_category import ListProductsByCategory
from .get_transaction_details import GetTransactionDetails
from .list_transactions_by_customer import ListTransactionsByCustomer
from .get_inventory_level import GetInventoryLevel
from .list_low_stock_products import ListLowStockProducts
from .get_total_sales_by_date import GetTotalSalesByDate
from .get_customer_loyalty_points import GetCustomerLoyaltyPoints
from .get_employee_details import GetEmployeeDetails
from .list_all_employees import ListAllEmployees
from .record_sale import RecordSale
from .add_new_product import AddNewProduct
from .update_product_price import UpdateProductPrice
from .add_new_customer import AddNewCustomer
from .update_customer_loyalty_points import UpdateCustomerLoyaltyPoints
from .update_customer_membership_level import UpdateCustomerMembershipLevel
from .process_return import ProcessReturn
from .update_transaction_status import UpdateTransactionStatus
from .update_customer_email import UpdateCustomerEmail
from .add_employee import AddEmployee
from .remove_employee import RemoveEmployee
from .update_employee_status import UpdateEmployeeStatus
from .update_product_stock import UpdateProductStock
from .update_customer_address import UpdateCustomerAddress
from .update_customer_phone_number import UpdateCustomerPhoneNumber
from .add_promotion import AddPromotion
from .update_inventory_quantity import UpdateInventoryQuantity
from .get_inventory_analytics import GetInventoryAnalytics
from .add_inventory_record import AddInventoryRecord
from .remove_promotion import RemovePromotion

ALL_TOOLS = [
    SearchProducts,
    GetCustomerDetails,
    GetProductDetailsBySKU,
    ListAllProducts,
    ListProductsByCategory,
    GetTransactionDetails,
    ListTransactionsByCustomer,
    GetInventoryLevel,
    ListLowStockProducts,
    GetTotalSalesByDate,
    GetCustomerLoyaltyPoints,
    GetEmployeeDetails,
    ListAllEmployees,
    RecordSale,
    AddNewProduct,
    UpdateProductPrice,
    AddNewCustomer,
    UpdateCustomerLoyaltyPoints,
    UpdateCustomerMembershipLevel,
    ProcessReturn,
    UpdateTransactionStatus,
    UpdateCustomerEmail,
    AddEmployee,
    RemoveEmployee,
    UpdateEmployeeStatus,
    UpdateProductStock,
    UpdateCustomerAddress,
    UpdateCustomerPhoneNumber,
    AddPromotion,
    UpdateInventoryQuantity,
    GetInventoryAnalytics,
    AddInventoryRecord,
    RemovePromotion,
]
