from rest_framework.viewsets import ModelViewSet

from main.serializers import TestModelSerializer
from main.models import TestModel


class TestModelView(ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer



