from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('/bodega',views.login_view,name='login_view'),
]