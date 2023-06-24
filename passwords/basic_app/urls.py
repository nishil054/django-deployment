from django.urls import path,include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register,name="register"),
    path('user_login/',views.user_login,name='user_login'),
]

                # <!-- <li><a href="{% url 'index' %}"></a>Admin</li>
                # <li><a href="{% url 'basic_app:register' %}"></a>Register</li> -->