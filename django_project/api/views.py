from rest_framework import viewsets, generics
from .serializers import ProjectSerializer, ThumbnailSerializer
from projects.models import Project, Thumbnail
from rest_framework import filters


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    search_fields = ["title", "details"]
    filter_backends = (filters.SearchFilter,)


class ThumbnailViewSets(viewsets.ModelViewSet):
    queryset = Thumbnail.objects.all()
    serializer_class = ThumbnailSerializer


class ProjectByCategoryAPI(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        try:
            category = self.kwargs.get("category")
            project = Project.objects.filter(category=category)
            return project
        except Project.DoesNotExist:
            return Project.objects.none()
