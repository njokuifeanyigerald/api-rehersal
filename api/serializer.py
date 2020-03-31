from rest_framework import serializers
from .models import Post,ViewModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'descriptions',
            'owner'
        ]

class ViewModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ViewModel
        fields = [
            'id',
            # 'url',
            'title',
            'descriptions',
            'owner'
        ]
            
        