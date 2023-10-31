from django.urls import path
from menu_app.views import index

urlpatterns = [
    path('<str:menu_name>/', index, name='index'),
]
