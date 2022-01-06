from db.fake_db import users
from typing import Tuple


def get_amount(id: int) -> Tuple:
    """
    Functionality to export the amount of a specific user.
    :param id: Takes as parameter the id of the user
    :return: The total amount of the user.
    """
    for user in users:
        if user["id"] == id:
            return user["amount"], user["name"]
