from enumfields import Enum


class OrderStatus(Enum):
    delivered = "delivered",
    shipped = "shipped",
    preparing = "preparing"