from django.core.validators import RegexValidator

from account.models import Account
from .enums import *


class Transaction(models.Model):
    sender = models.CharField(
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )
    receiver = models.CharField(
        max_length=16,
        validators=[RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')]
    )

    transaction_id = models.AutoField(primary_key=True)
    transaction_type = models.CharField(max_length=20, choices=TransactionType.choices)
    amount = models.DecimalField(max_digits=14, decimal_places=2)  # max 1 trillion
    started = models.DateTimeField(auto_now=True)


class ExchangeRate(models.Model):
    BASE = Currency.USD

    _exchange_rate_table = {
        Currency.CNY: 0.16,
        Currency.SGD: 0.8,
        Currency.EURO: 1.3,
    }

    @classmethod
    def get_exchange_rate(self, source, target):
        if source != self.BASE:
            return self._exchange_rate_table[source] / self._exchange_rate_table[target]
        return self._exchange_rate_table[target]
