from django.urls import path
from . import views

urlpatterns=[
    path("",views.Login.as_view()),
    path("<int:pk>",views.Login.as_view()),
    path("verify_email/<int:pk>/", views.EmailVerify.as_view()),

    
]