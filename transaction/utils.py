from django.shortcuts import render

from account.models import Account
from transaction.models import Transaction


def transfer(from_card_number, to_card_number, amount, transaction_type):
    from_account = Account.objects.get(card_number=from_card_number)
    if not from_account:
        raise Exception('no account is found with the specified card number')
    if from_account.balance < amount:
        raise Exception(
            'the to be transferred amount is greater than the amount the account currently owns')
    from_account.balance -= amount
    from_account.save()
    # withdrawal can be interpreted as user buying money from the bank
    to_account = Account.objects.get(card_number=to_card_number)
    to_account.balance += amount
    to_account.save()
    tnx = Transaction(
        sender=from_card_number,
        receiver=to_card_number,
        transaction_type=transaction_type,
        amount=amount
    )
    tnx.save()


def transfer_request(request, from_card_number, to_card_number, amount, transaction_type):
    try:
        transfer(from_card_number, to_card_number, amount, transaction_type)
        return render(request, "transaction/success.html")
    except Exception as e:
        return render(request, "transaction/fail.html", {'reason': e})
