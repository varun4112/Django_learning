from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer


@api_view(["POST"])
def create_todos(request):
    serializers = TodoSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.error, status=status.HTTP_400_BAD_REQUEST)
