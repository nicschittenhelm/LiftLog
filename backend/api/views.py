from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from data.models import UserData, Item, WorkoutTemplate
from .serializers import ItemSerializer, UserDataSerializer, WorkoutTemplateSerializer
from django.contrib.auth.decorators import login_required

@api_view(["GET"])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def addData(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# To test if users are only able to view there own data
@login_required
@api_view(['POST'])
def create_user_data(request):
    serializer = UserDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def user_data_list(request):
    user_data = UserData.objects.filter(user=request.user)
    serializer = UserDataSerializer(user_data, many=True)
    return Response(serializer.data)


# Creating a template for a workout
@login_required
@api_view(['POST'])
def create_workouttemplate(request):
    serializer = WorkoutTemplateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required
@api_view(['GET'])
def get_workouttemplate(request):
    user_data = WorkoutTemplate.objects.filter(user=request.user)
    serializer = WorkoutTemplateSerializer(user_data, many=True)
    return Response(serializer.data)