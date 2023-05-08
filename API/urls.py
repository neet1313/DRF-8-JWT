from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views
# from rest_framework.authtoken.views import obtain_auth_token
# from API.customauthtoken import CustomAuthToken

router = DefaultRouter()
router.register('api', views.StudentViewset)

urlpatterns = [
    path('', include(router.urls)),

    # Add path to for Token Authentication
    # path('gettoken/', obtain_auth_token)
    
    # Path for Custom Token respose
    # path('gettoken/', CustomAuthToken.as_view())
]
