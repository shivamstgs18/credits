from controllers.get_credit import get_credit
from db.db import data

def delete_credit(id: str):
    global data

    credit_data = get_credit(id)
    data.remove(credit_data)

    return {"Success": True}