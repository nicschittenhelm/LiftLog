from rest_framework import serializers
from data.models import Item, UserData, WorkoutTemplate, ExerciseTemplate

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
class ExerciseTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseTemplate
        fields = ['exercise']

class WorkoutTemplateSerializer(serializers.ModelSerializer):    
    
    exercises = ExerciseTemplateSerializer(many=True)
        
    class Meta:
        model = WorkoutTemplate
        fields = ['id', 'workoutTitle', 'exercises']
    
    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises')
        workout_template = WorkoutTemplate.objects.create(**validated_data)
        
        for exercise_data in exercises_data:
            exercise_serializer = ExerciseTemplateSerializer(data=exercise_data)
            exercise_serializer.is_valid(raise_exception=True)
            ExerciseTemplate.objects.create(workoutTemplate=workout_template, **exercise_serializer.validated_data)
        
        return workout_template