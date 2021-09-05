from django.utils.translation import gettext_lazy as _
from django.db import models


class TransactionType(models.TextChoices):
    SEND = 'SEND', _('SEND')
    WITHDRAWAL = 'WITHDRAWAL', _('WITHDRAWAL')


class Currency(models.TextChoices):
    USD = 'USD', _('US Dollars')
    EURO = 'EUR', _('European Union')
    CNY = 'CNY', _('Chinese Yuan')
    SGD = 'SGD', _('Singapore Dollars')
