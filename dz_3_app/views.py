from datetime import datetime, timedelta

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from dz_3_app.models import Order, User, Goods
from .forms import EditGoods, GoodsChoice, ImageForm, OnlyGoodsChoice


# goods_id = None


def index(request):
    return render(request, 'base.html')


def user_orders(request, user_id, days):
    point = datetime.today() - timedelta(days=days)
    user = User.objects.filter(pk=user_id).first()
    if user:
        orders = Order.objects.filter(user_ID=user, creation_date__gte=point)
        orders_list = {}
        for order in orders:
            item = order.goods_ID
            order_dict = {'Creation_date': order.creation_date,
                          'Goods': item.title,
                          'Quantity': order.quantity,
                          'Amount': order.amount}
            orders_list[f'Order_{order.id}'] = order_dict

            # orders_list += [f'Товар: {item.title}, Дата заказа: {order.creation_date}, '
            #                 f'Количество:{order.quantity}, Сумма: {order.amount}']

        context = {'User': user.name,
                   'Orders': orders_list}

        return render(request, 'user_orders.html', context)
    context = {'Error': 'Заказчик не найден'}
    return render(request, 'error.html', context)


def choose_goods(request):
    if request.method == 'POST':
        form = GoodsChoice(request.POST)
        # global goods_id
        goods_id = form.data['goods']
        option = form.data['option']
        if option == '1':
            return redirect('edit_goods', goods_id)
        elif option == '2':
            return redirect('upload_image', goods_id)

    else:
        form = GoodsChoice()
        return render(request, 'choose_goods.html',
                      context={'form': form, 'title': 'Выбрать товар'})


def edit_goods(request, goods_id=None):
    goods = Goods.objects.filter(pk=goods_id).first()
    if request.method == 'POST':  # and request.FILES

        form = EditGoods(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            Goods(
                id=goods_id,
                title=title,
                description=description,
                price=price,
                quantity=quantity,
                image=goods.image,
            ).save()
            return render(request, 'edit_goods.html', context={'title': 'успешно'})

    else:
        form = EditGoods()
        return render(request, 'edit_goods.html',
                      context={'form': form, 'goods_dict': {
                          'title': goods.title,
                          'description': goods.description,
                          'price': goods.price,
                          'quantity': goods.quantity,
                      }})


def add_image(request, goods_id=None):
    goods = Goods.objects.filter(pk=goods_id).first()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            if goods:
                Goods(id=goods_id,
                      title=goods.title,
                      description=goods.description,
                      price=goods.price,
                      quantity=goods.quantity,
                      image=image
                      ).save()
            return render(request, 'upload_image.html', context={'title': 'успешно'})
    else:
        form = ImageForm()
        return render(request, 'upload_image.html', {'form': form})


def view_goods(request):
    if request.method == 'POST':
        form = OnlyGoodsChoice(request.POST)
        goods_id = form.data['goods']
        goods = Goods.objects.filter(pk=goods_id).first()
        if goods:
            goods_dict = {'Goods': goods.title,
                       'Description': goods.description,
                       'Price': goods.price,
                       'Quantity': goods.quantity,
                       'Image': goods.image,
                       }

            return render(request, 'view_goods.html', context={'Dict': goods_dict})
    else:
        form = OnlyGoodsChoice()
        return render(request, 'choose_goods.html',
                      context={'form': form, 'title': 'Выбрать товар'})
