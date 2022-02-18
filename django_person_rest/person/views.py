from rest_framework import viewsets

from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer  # serializers.py 내에 있는 함수
