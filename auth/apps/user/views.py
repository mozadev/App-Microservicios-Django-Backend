from rest_framework_api.views import StandardAPIView
import json, uuid

from rest_framework import permissions
from .serializers import UserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            #if obj is uuid, we simply return the value of obj
            return str(obj)
        return json.JSONEncoder.default(self, obj)
    
class ListAllUsersView(StandardAPIView):
    permission_classes = [permissions.AlloAny,]
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        user_data = UserListSerializer(user, many=True).data
        return self.send_response(json.dumps(user_data, cls=UUIDEncoder), status=status.HTTP_200_OK)