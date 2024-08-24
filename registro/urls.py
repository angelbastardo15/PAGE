from django.urls import path,include
from .views import SignupPageView


urlpatterns=[
    # Compañero la ruta accounts/ es obligatorio ese nombre
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup",SignupPageView.as_view(), name="signup"),
    
]