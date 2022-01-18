from rest_framework import serializers 
from .models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    alias = serializers.SlugRelatedField(slug_field='username', required=True, queryset=User.objects.all())
    class Meta: 
        fields = ('id', 'alias', 'firstname', 'lastname', 'age', 'state', 'area', 'email', 'gender', 'agegroup', 'religion', 'discipline', 'gender1', 'smoking', 'alcohol', 'uncleanliness', 'lateness', 'homepartying',) 
        model = Post


