from rest_framework.serializers import ModelSerializer, CharField
from projects.models import Project

class ProjectSerializer(ModelSerializer):
    workspace_name = CharField(source="workspace.name", read_only=True)
    class Meta:
        model = Project
        fields = "__all__"