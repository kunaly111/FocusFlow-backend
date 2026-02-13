from rest_framework.serializers import ModelSerializer, CharField
from .models import Tasks

class TaskSerializer(ModelSerializer):
    Project_name = CharField(source="Project.name", read_only=True)
    Workspace_name =CharField(source="Project.Workspace.name", read_only=True) 

    class Meta:
        model = Tasks
        fields = "__all__"