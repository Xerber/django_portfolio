from dataclasses import field
from socket import fromshare
from django import forms

from .models import Offer


class OfferForm(forms.ModelForm):
  '''Форма заявок'''
  class Meta:
    model = Offer
    fields = ("name", "subject", "email", "message")