from rest_framework.viewsets import ModelViewSet

from backend.serializers import TestModelSerializer
from backend.models import TestModel


class TestModelView(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer



