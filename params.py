from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class AccountStatusEnum(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class PostCreditParam(BaseModel):
    company_name: str
    address: str
    registration_date: datetime
    number_of_employees: int
    turnover: int
    raised_capital: int
    net_profit: int
    contact_number: str
    contact_email: str
    company_website: str
    loan_amount: int
    loan_interest_percent: int
    account_status: AccountStatusEnum = AccountStatusEnum.ACTIVE.value

class UpdateCreditparam(BaseModel):
    id: str
    company_name: Optional[str] = None
    address: Optional[str] = None
    registration_date: Optional[datetime] = None
    number_of_employees: Optional[int] = None
    turnover: Optional[int] = None
    raised_capital: Optional[int] = None
    net_profit: Optional[int] = None
    contact_number: Optional[str] = None
    contact_email: Optional[str] = None
    company_website: Optional[str] = None
    loan_amount: Optional[int] = None
    loan_interest_percent: Optional[int] = None
    account_status: Optional[AccountStatusEnum] = None

class UserBase(BaseModel):
    username: str
    password: str