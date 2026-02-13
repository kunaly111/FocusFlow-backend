from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from workspaces.models import Workspace
from projects.models import Project
from tasks.models import Tasks


class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        total_workspaces = Workspace.objects.filter(
            owner=user
        ).count()

        total_projects = Project.objects.filter(
            Workspace__owner=user
        ).count()

        total_tasks = Tasks.objects.filter(
            Project__Workspace__owner=user
        ).count()

        completed_tasks = Tasks.objects.filter(
            Project__Workspace__owner=user,
            is_completed=True
        ).count()

        return Response({
            "total_workspaces": total_workspaces,
            "total_projects": total_projects,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks
        })
