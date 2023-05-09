from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

# Importing predefined classes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('gettoken', views.StudentViewset, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]


# Install JWT -> pip install djangorestframework-simplejwt
# GET Token ->  http POST http://127.0.0.1:8000/api/token/ username="Henal" password="yoloyolo@123"
#  Active Token Validity -> 5 min.
#  Active Token Validity -> 1day
# Verify Token -> http POST http://127.0.0.1:8000/api/token/verify/ token="<token>"
# Refresh Token -> http POST http://127.0.0.1:8000/api/token/refresh/ token="<refresh token>"


#  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzNTk5Mzg1LCJpYXQiOjE2ODM1OTkwODUsImp0aSI6Ijg2Y2YzZGEzNWI1ODQ5MTU5NzIwMTBjYTI3Y2Q5ODlmIiwidXNlcl9pZCI6Mn0.EHyuIxmTTLZEDD27I6iZMfFa8Okh-KrC-RfDWfXEKig",       
    # "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4MzY4NTQ4NSwiaWF0IjoxNjgzNTk5MDg1LCJqdGkiOiIxNTNmMGUyNDZiMDQ0OGJmYjk5NTc3ZGQxNTliZDFhYSIsInVzZXJfaWQiOjJ9.v2iWuyfFpXiPyIJmoMJ1fnrI7CTri6V0m2XymmvVS7I"   
