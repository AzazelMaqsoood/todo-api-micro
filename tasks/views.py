from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all().order_by("priority")
    serializer_class = TaskSerializer
    filterset_fields = ["is_completed", "priority"]
    search_fields = ["title", "description"]
