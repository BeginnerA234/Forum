from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from custom_user.api.views import (
    UserProfileRetrieveView,
    IgnoreUserViewSet,
    CountryCreateView,
    UserRegisterAPIView
)

router = DefaultRouter()

router.register(r'profile', UserProfileRetrieveView, basename='profile')
router.register(r'ignore-user', IgnoreUserViewSet, basename='ignore-user')
router.register(r'country', CountryCreateView, basename='country')

urlpatterns = router.urls

urlpatterns += [
    # JSON Web Token
    path('register/', UserRegisterAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
