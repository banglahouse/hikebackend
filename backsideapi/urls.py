from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('menu/', views.getMenu),
    path('order/', views.postOrderDetails),
    path('getorder/', views.getOrderDetails),
    # path('order/', views.order),
    # path('menuwithcateg/', views.getMenuWithCateg),



 

]