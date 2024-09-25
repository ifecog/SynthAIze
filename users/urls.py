from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.views import (
    SignupView,
    SigninView,
    UserListView,
    SynthesistListView,
    ObserverListView,
)


urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('synthesists/', SynthesistListView.as_view(), name='synthesists'),
    path('observers/', ObserverListView.as_view(), name='observers'),
    
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-refresh'),
]