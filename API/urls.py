from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

# Importing predefined classes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('api', views.StudentViewset, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken', TokenVerifyView.as_view(), name='token_verify')
]


# Install JWT -> pip install djangorestframework-simplejwt
