
from .serializers import User, UserSerializer
from rest_framework import viewsets, generics, views
from rest_framework.permissions import AllowAny

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class RegisterView(viewsets.GenericViewSet, generics.CreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny,]
