from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('bodega',views.bodega,name='bodega'),
    path('mermas',views.mermas,name='mermas'),
    path('strikes',views.strikes,name='strikes'),
    path('add_strike',views.add_strike,name='add_strike'),
    path('update_strike',views.update_strike,name='update_strike'),
    path('delete_strike/<int:id>', views.delete_strike, name='delete_strike'),
]