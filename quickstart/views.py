from django.contrib.auth.models import User, Group
from quickstart.models import Candidate
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, CandidateSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer