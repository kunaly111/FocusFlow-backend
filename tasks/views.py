from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializer
from .models import Tasks
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsTaskOwner

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsTaskOwner]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title']
    ordering_fields = ['created_at', 'title', 'is_completed']





    def get_queryset(self):
        return Tasks.objects.select_related("project", "project__workspace").filter(Project__Workspace__owner=self.request.user)


    @action(detail=True, methods=['post'])
    def mark_complete(self, request, pk=None):
        task =self.get_object()
        task.is_completed = True
        task.save()

        return Response({"status": "Task marked as completed"})
