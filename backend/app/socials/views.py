from rest_framework import viewsets

from .models import Social
from .serializers import SocialSerializer


class SocialViewSet(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
