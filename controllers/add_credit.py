from uuid import uuid4
from fastapi import HTTPException, status
from params import PostCreditParam

from db.db import data

def add_credit(credit_data: PostCreditParam):
    """Add credit API controller"""
    
    global data

    credit = {
        "id": uuid4()
    }
    credit.update(credit_data.__dict__)
    data.append(credit)
    
    return {"Success": True, "id": credit["id"]}