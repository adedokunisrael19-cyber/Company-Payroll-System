from enum import Enum

class PayrollStatus(str, Enum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    CANCELED = 'CANCELED'