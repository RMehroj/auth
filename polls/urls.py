from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SignUpView, GoogleLoginView, EmailLoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('login/email/', EmailLoginView.as_view(), name='email_login'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
]
