from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('account-list/', views.AccountList.as_view(), name='acc-list'),
]
