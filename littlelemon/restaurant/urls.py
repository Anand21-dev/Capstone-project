from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.menuItemView.as_view(), name='menu-list'),
    path('menu/<int:pk>',views.singleItemView.as_view(), name ='single-menu-list'),
    path('api-token-auth/', obtain_auth_token)
]