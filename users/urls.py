from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from users.views import (
    SignupView,
    SigninView,
    UserListView,
    SynthesistListView,
    ObserverListView,
    UserDetailView,
    UserUpdateView,
    PasswordUpdateView,
)


urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<uuid:uuid>/', UserDetailView.as_view(), name='user-detail'),
    path('<uuid:uuid>/update/', UserUpdateView.as_view(), name='user-update'),
    path('change-password/', PasswordUpdateView.as_view(), name='password-change'),
    # Auth
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    # Roles
    path('synthesists/', SynthesistListView.as_view(), name='synthesists'),
    path('observers/', ObserverListView.as_view(), name='observers'),
    
    # Token
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-refresh'),
]


# {
#   "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0Mjk4MjUyNywiaWF0IjoxNzI3NDMwNTI3LCJqdGkiOiI1NzZiNGI4MzgxMzM0Njk1YWI3NzYyM2QzMTljMjExYiIsInVzZXJfaWQiOjJ9.N1_f2qBxDtLWuvR1f_Xkbd5PIdsMKFNTiz8DwMmyjaU",
#   "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDM3NzI3LCJpYXQiOjE3Mjc0MzA1MjcsImp0aSI6ImU1OWM0MDZjMWIyZTQxMDM4MzRiMzJkZGUyMGY0ZTExIiwidXNlcl9pZCI6Mn0.uinixd3xMlh2wdCRAtQ95PpnWcWdyzrAmR_KisJibVc",
#   "uuid": "2f757e48-902c-46af-9b93-7aae4d8256ac",
#   "name": "James Doe",
#   "email": "johndoe@gmail.com",
#   "role": "Observer",
#   "isAdmin": false,
#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NDM3NzI3LCJpYXQiOjE3Mjc0MzA1MjcsImp0aSI6IjQzYzhiODM4ZTA0NDQ4Y2U5ODQ0MTIyNDg4ZTJlY2JiIiwidXNlcl9pZCI6Mn0.gYPhW7RXJfPGiWpBii8gZMHBt-sjMsXuWq3SW2xkC6U"
# }