from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:catalog_list'), name='logout'),
]