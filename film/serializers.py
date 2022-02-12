from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Actor, Movie, Comment


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    # def validate_gender(self, attrs):
    #     if attrs != 'erkak' or attrs != 'ayol':
    #         raise ValidationError(detail="Erkak yoki ayol so'zi kiritilishi shart")
    #     return attrs

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'