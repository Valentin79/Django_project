from django import forms
from .models import Goods


class GoodsChoice(forms.Form):
    goods = forms.ModelChoiceField(queryset=Goods.objects.all())
