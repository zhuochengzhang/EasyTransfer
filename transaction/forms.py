from django import forms
from django.core.validators import RegexValidator
from .enums import TransactionType


class SendForm(forms.Form):
    sender = forms.CharField(
        label='Enter the card number of the recipient:',
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )
    recipient = forms.CharField(
        label='Enter the card number of the recipient:',
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )
    amount = forms.DecimalField(decimal_places=2, max_digits=16)
    # TODO: add currency


class WithdrawForm(forms.Form):
    card_number = forms.CharField(
        label='Enter the card number:',
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )
    amount = forms.DecimalField(decimal_places=2, max_digits=16)
    # TODO: add currency


class GetHistoryForm(forms.Form):
    card_number = forms.CharField(
        label='Enter the card number:',
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )


class TransactionForm(forms.Form):
    transaction_type = forms.ChoiceField(choices=TransactionType.choices + [('View History', 'View History')])
