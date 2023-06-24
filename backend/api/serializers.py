from rest_framework import serializers
from data.models import Item, UserData, WorkoutTemplate

# only testing
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ['id', 'message', 'created']
      
      
# Workout serializers
# ONLY FOR TESTING, needs to be changes to proper serializer
class WorkoutTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutTemplate
        fields = "__all__"