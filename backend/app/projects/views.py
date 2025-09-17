from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Project
from .serializers import ProjectSerializer


class CustomPagination(PageNumberPagination):
    page_size = 5


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
