from rest_framework import serializers
from .models import Score

class RunScoreSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(required=True)
    username = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = ['id', 'user', 'score', 'username']
    
    def update(self, instance, validated_data):
        if instance.score < validated_data.get('score', instance.score):
            instance.score = validated_data.get('score', instance.score)
            instance.user = validated_data.get('user', instance.user)
            instance.save()
        return instance
    
    def get_username(self, obj):
        return obj.user.username