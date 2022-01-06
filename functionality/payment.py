from db.fake_db import users, transactions
from typing import Dict, Any, Tuple
import uuid
import datetime


def make_payment(payer_iban: str, payee_iban: str, payment_amount: float, sort_code: str) -> Tuple:
    """
    Implementation of payment main functionality. Amount computation after payment.
    Assign tokens regarding the payment amount and the payer. The transaction is executed through the
    number of personal banking accounts. Also the sort_code is extracted from the recognizer each banking account.
    :param payer_iban:
    :param payee_iban:
    :param payment_amount:
    :param sort_code:
    :return:
    """
    for index, user in enumerate(users):
        if user["iban"].__eq__(payer_iban):
            payer_index = index
        elif user["iban"].__eq__(payee_iban):
            payee_index = index
        else:
            raise Exception("Invalid IBAN")

    # computation of amounts regarding current transaction
    # assign tokens to the payer
    users[payer_index]["amount"] -= payment_amount
    users[payer_index]["token"] += cashback_tokens(payment_amount)
    users[payee_index]["amount"] += payment_amount

    payload_payment = {
        "UUID": str(uuid.uuid1()),
        "creation_date": str(datetime.datetime.now().astimezone().isoformat()),
        "booking_date": str(datetime.datetime.now().astimezone().isoformat()),
        "payee": users[payee_index]["name"],
        "payee_primary_account": users[payee_index]["iban"],
        "payer": users[payer_index]["name"],
        "payer_primary_account": users[payer_index]["iban"],
        "movement_type": "IBAN",
        "amount": payment_amount,
        "currency": "GB" if users[payee_index]["iban"][:2] == sort_code else "Other",
    }
    # save data in db, in current situation is a list
    transactions.append(payload_payment)

    return payload_payment, users[payer_index]["token"]


def cashback_tokens(payment_amount: float) -> float:
    """
    Computation of cashback regarding ratio
    :param payment_amount:
    :return: discounted value
    """
    return round(payment_amount * 0.05)
