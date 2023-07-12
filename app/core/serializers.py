from __future__ import annotations

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for user models."""

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'group']


class GroupSerialier(serializers.HyperlinkedModelSerializer):
    """Serizalier for group models."""

    class Meta:
        model = Group
        fields = ['url', 'name']
