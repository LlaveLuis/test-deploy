from django.contrib.auth import get_user_model
from django.views.generic import ListView

User = get_user_model()


class AccountList(ListView):
    template_name = 'accounts/account_list.html'
    model = User
