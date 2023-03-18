from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class ListCreateDestroyViewSet(GenericViewSet,
                               mixins.ListModelMixin,
                               mixins.CreateModelMixin,
                               mixins.DestroyModelMixin):
    pass
