from __future__ import annotations

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets

from app.core.serializers import GroupSerialier
from app.core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows user to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = permissions


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows group to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerialier
    permission_classes = permissions
