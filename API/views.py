from rest_framework import viewsets
from API import serializers, models
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )


# Accessing API through JWT: http http://127.0.0.1:8000/gettoken/ 'Authorization:Bearer <Token>'
# POSTing data to API through JWT:  http -f POST http://127.0.0.1:8000/gettoken/ name=Karan roll=2 city=Ludhiana "Authorization:Bearer <Token>"
# PUT data to API through JWT:  http PUT http://127.0.0.1:8000/gettoken/<id>/ name=Karan roll=3 city=Ludhiana "Authorization:Bearer <Token>"
# DELETE object of API through JWT: http DELETE http://127.0.0.1:8000/gettoken/<id>/ "Authorization:Bearer <Token>"
