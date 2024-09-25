from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.views import (
    SignupView,
    SigninView,
)


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-refresh'),
]