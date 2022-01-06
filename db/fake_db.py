from typing import List

# Mock Data as document database
# Users have collection behaviour
users: List = [{"id": 1,
                "name": "John Smith",
                "iban": "GB26 1111 2222 2255 5555 01",
                "amount": 10000.00,
                "token": 0},
               {"id": 2,
                "name": "Jane Smith",
                "iban": "GB26 1111 2222 2255 6666 01",
                "amount": 15000.00,
                "token": 0}
               ]


# transactions have collection behaviour
# payments saved as documents
transactions: List = []

# list of choices
impact_choices: List =[
    {"pizza": 5},
    {"coffee": 2}
]


