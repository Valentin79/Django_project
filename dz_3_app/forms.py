from django import forms
from django.forms import RadioSelect
from .models import Goods


class GoodsChoice(forms.Form):
    CHOICES = (('1', 'Редактировать товар'), ('2', 'Загрузить изображение'))
    goods = forms.ModelChoiceField(queryset=Goods.objects.all())
    option = forms.ChoiceField(choices=CHOICES, widget=RadioSelect)


class OnlyGoodsChoice(forms.Form):
    goods = forms.ModelChoiceField(queryset=Goods.objects.all())



class EditGoods(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'placeholder': 'Title'}))
    description = forms.CharField(max_length=100, widget=forms.Textarea(
        attrs={'placeholder': 'Description'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(
        attrs={'placeholder': 'Price'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': 'Quantity'}))
    # image = forms.ImageField(required=False)


class ImageForm(forms.Form):
    image = forms.ImageField()

