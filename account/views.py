from django.core.validators import RegexValidator
from django import forms
from django.shortcuts import render, redirect
from .models import Account


class EntryForm(forms.Form):
    card_number = forms.CharField(label='Enter your card number:',
                                  max_length=16,
                                  validators=[
                                      RegexValidator(regex='^\d{16}$', message='card number must be 16 digits',
                                                     code='nomatch')
                                  ])


def entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            return redirect('/accounts/%s/summary' % form.cleaned_data['card_number'])
    form = EntryForm()
    return render(request, "account/entry.html", context={'form': form})


def summary(request, card_number):
    try:
        account = Account.objects.get(card_number=card_number)
    except Exception as e:
        print(e)
        return render(request, "account/summary.html", context={"account": None})
    return render(request, "account/summary.html", context={"account": account})
