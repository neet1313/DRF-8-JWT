from rest_framework import viewsets
from API import serializers, models


# ------- Model Serializer ------


class StudentViewset(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


# To install httpie command line tool-> pip install httpie
# Generating/Viewing Token for a user-> http POST http://127.0.0.1:8000/gettoken/ username='' pasword=''

# HTTPie GET request Token Authentication-> http http://127.0.0.1:8000/api/ 'Authorization:Token <Token>'
# HTTPie POST request Token Authentication-> http -f POST http://127.0.0.1:8000/api/ name=<name> roll=<roll> city=<city> 'Authorization:Token <Token>'
# HTTPie PUT request Token Authentication-> http PUT http://127.0.0.1:8000/api/<id>/ name=<name> roll=<roll> city=<city> 'Authorization:Token <Token>'
# HTTPie DELETE request Token Authentication-> http DELETE http://127.0.0.1:8000/api/<id>/ 'Authorization:Token <Token>'
