from django.urls import path
from basic_app import views

#TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns=[
    path('registration/',views.register , name="register"),
    path('user_login/', views.user_login, name="user_login")
]
