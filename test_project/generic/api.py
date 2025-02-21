from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from django_ufilter.integrations.drf import DRFFilterBackend

from .models import ModelA, ModelB


class ModelASerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelA
        fields = ["name", "rel_b"]


class ModelBSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelB
        fields = ["name", "a", "content_type", "object_id"]


class ModelAViewSet(ModelViewSet):
    serializer_class = ModelASerializer
    queryset = ModelA.objects.all()
    filter_backends = [DRFFilterBackend]
    filter_fields = ["name", "rel_b"]


class ModelBViewSet(ModelViewSet):
    serializer_class = ModelBSerializer
    queryset = ModelB.objects.all()
    filter_backends = [DRFFilterBackend]
    filter_fields = []
