from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('user_orders/<int:user_id>/<int:days>', views.user_orders, name='User_orders'),
    # path('chose_goods/', views.choose_goods, name='edit_goods'),
    # path('edit_goods/<int:goods_id>', views.edit_goods, name='edit_goods'),
    # path('upload_image/<int:goods_id>', views.add_image, name='upload_image'),
    path('view_goods/', views.view_goods, name='view_goods')
]