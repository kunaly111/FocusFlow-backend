from rest_framework.serializers import ModelSerializer, CharField
from .models import Workspace

class WorkspaceSerializer(ModelSerializer):
    owner_username = CharField(source="owner.username", read_only=True), 
    class Meta:
        model = Workspace
        fields = "__all__"
        read_only_fields = ["owner"]