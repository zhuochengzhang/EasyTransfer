from django.db import models
from django.core.validators import RegexValidator
from transaction.enums import Currency


class Account(models.Model):
    card_number = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(regex='^\d{16}$', message='card number must be 16 digits', code='nomatch')
        ],
        primary_key=True,
        unique=True
    )  # card number must be 16 digits
    balance = models.DecimalField(decimal_places=2, max_digits=20)
    currency = models.CharField(max_length=3, choices=Currency.choices)


