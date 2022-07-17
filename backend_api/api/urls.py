from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView

from backend_api.api.views import RegisterView, ApiTokenObtainPairView

urlpatterns = [
    path('token/', ApiTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)



