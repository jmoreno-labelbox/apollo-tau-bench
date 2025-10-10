# Copyright owned by Sierra.

from .get_product_sku_by_name import GetProductSkuByName
from .get_inventory_item_by_sku_and_store import GetInventoryItemBySkuAndStore
from .get_promotion_by_name_and_date import GetPromotionByNameAndDate
from .get_customer_id_by_name import GetCustomerIdByName
from .create_customer import CreateCustomer
from .update_inventory_sale import UpdateInventorySale
from .create_transaction import CreateTransaction
from .get_employee_id_by_name import GetEmployeeIdByName
from .activate_promotion import ActivatePromotion
from .deactivate_promotion import DeactivatePromotion
from .update_promotion_details import UpdatePromotionDetails
from .get_promotions_by_status import GetPromotionsByStatus
from .get_product_details_by_sku import GetProductDetailsBySKU
from .update_product_details import UpdateProductDetails
from .update_customer_loyalty_points import UpdateCustomerLoyaltyPoints
from .update_inventory_reserved_quantity import UpdateInventoryReservedQuantity
from .get_promotion_by_id import GetPromotionById
from .create_promotion import CreatePromotion
from .get_product_by_status import GetProductByStatus
from .update_customer_details import UpdateCustomerDetails
from .update_inventory_status import UpdateInventoryStatus
from .get_customer_details_by_id import GetCustomerDetailsById
from .find_transaction_by_customer_and_sku import FindTransactionByCustomerAndSku
from .process_item_return import ProcessItemReturn
from .get_products_by_category import GetProductsByCategory
from .execute_inventory_transfer import ExecuteInventoryTransfer
from .create_inventory_record import CreateInventoryRecord
from .calculate_transaction_totals import CalculateTransactionTotals
from .update_stock_level import UpdateStockLevel
from .find_customers_by_criteria import FindCustomersByCriteria
from .generate_and_assign_promo_codes import GenerateAndAssignPromoCodes

ALL_TOOLS = [
    GetProductSkuByName,
    GetInventoryItemBySkuAndStore,
    GetPromotionByNameAndDate,
    GetCustomerIdByName,
    CreateCustomer,
    UpdateInventorySale,
    CreateTransaction,
    GetEmployeeIdByName,
    ActivatePromotion,
    DeactivatePromotion,
    UpdatePromotionDetails,
    GetPromotionsByStatus,
    GetProductDetailsBySKU,
    UpdateProductDetails,
    UpdateCustomerLoyaltyPoints,
    UpdateInventoryReservedQuantity,
    GetPromotionById,
    CreatePromotion,
    GetProductByStatus,
    UpdateCustomerDetails,
    UpdateInventoryStatus,
    GetCustomerDetailsById,
    FindTransactionByCustomerAndSku,
    ProcessItemReturn,
    GetProductsByCategory,
    ExecuteInventoryTransfer,
    CreateInventoryRecord,
    CalculateTransactionTotals,
    UpdateStockLevel,
    FindCustomersByCriteria,
    GenerateAndAssignPromoCodes,
]
