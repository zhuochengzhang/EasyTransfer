from account.models import Account
from transaction.enums import TransactionType
from transaction.utils import transfer
from random import seed
from random import randrange, randint

accounts = [
    {
        'cn': '5410123456780810',
        'balance': 1000000000000,
        'currency': 'USD',
    },  # the admin account
    {
        'cn': '5410123456780811',
        'balance': 1000000,
        'currency': 'USD',
    },
    {
        'cn': '5410123456780812',
        'balance': 1000000,
        'currency': 'USD',
    },
    {
        'cn': '5410123456780813',
        'balance': 1000000,
        'currency': 'USD',
    },
    {
        'cn': '5410123456780814',
        'balance': 1000000,
        'currency': 'USD',
    },
    {
        'cn': '5410123456780815',
        'balance': 1000000,
        'currency': 'USD',
    },
    # add more here with different currencies here
]

for account in accounts:
    a = Account(
        card_number=account['cn'],
        balance=account['balance'],
        currency=account['currency']
    )
    a.save()

seed(1)
for _ in range(100):
    index_from = randrange(1, len(accounts))
    amount = randint(50, 100)
    is_send = randint(0, 1)
    if is_send == 1:
        index_to = index_from
        while index_to == index_from:
            index_to = randrange(1, len(accounts))
        transfer(
            accounts[index_from]['cn'],
            accounts[index_to]['cn'],
            amount,
            TransactionType.SEND
        )
    else:
        transfer(
            accounts[index_from]['cn'],
            accounts[0]['cn'],
            amount,
            TransactionType.WITHDRAWAL
        )
