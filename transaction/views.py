from django.shortcuts import render, redirect
from .models import Transaction
from django.db.models import Q
from .forms import TransactionForm, SendForm, WithdrawForm, GetHistoryForm
from .enums import TransactionType
from .utils import transfer_request
from django.utils.html import format_html

ADMIN_CARD_NUMBER = '5410123456780810'


def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['transaction_type'] == TransactionType.SEND:
                return redirect('/transaction/send/')
            elif form.cleaned_data['transaction_type'] == TransactionType.WITHDRAWAL:
                return redirect('/transaction/withdraw/')
            return redirect('/transaction/getHistory/')
    form = TransactionForm()
    input_tag = format_html('<input type="submit" value=%s>' % 'Confirm')
    return render(request, "base_form.html", {'form': form, 'input': input_tag})


def send(request):
    if request.POST:
        form = SendForm(request.POST)
        if form.is_valid():
            from_card_number = form.cleaned_data['sender']
            to_card_number = form.cleaned_data['recipient']
            amount = form.cleaned_data['amount']
            return transfer_request(request, from_card_number, to_card_number, amount, TransactionType.SEND)
    form = SendForm()
    input_tag = format_html('<input type="submit" value=%s>' % 'Send')
    return render(request, "base_form.html", {'form': form, 'input': input_tag})


def withdraw(request):
    if request.POST:
        form = WithdrawForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            amount = form.cleaned_data['amount']
            return transfer_request(request, card_number, ADMIN_CARD_NUMBER, amount, TransactionType.WITHDRAWAL)
    form = WithdrawForm()
    input_tag = format_html('<input type="submit" value=%s>' % 'Withdraw')
    return render(request, "base_form.html", {'form': form, 'input': input_tag})


def history(request, card_number):
    # account = Account.objects.get(card_number=card_number)
    transactions = Transaction.objects.filter(Q(sender=card_number) | Q(receiver=card_number)).order_by('started')
    return render(request, "transaction/history.html", context={"transactions": transactions})


def get_history(request):
    if request.POST:
        form = GetHistoryForm(request.POST)
        if form.is_valid():
            card_number = form.cleaned_data['card_number']
            return redirect('/transaction/%s/history' % card_number)
    form = GetHistoryForm()
    input_tag = format_html('<input type="submit" value=%s>' % 'Go')
    return render(request, "base_form.html", {'form': form, 'input': input_tag})
