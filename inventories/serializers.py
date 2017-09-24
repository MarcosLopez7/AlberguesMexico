from rest_framework.serializers import ModelSerializer

from .models import Refuge, Post, Need


class NeedCreateSerializer(ModelSerializer):
    class Meta:
        model = Need
        fields = ['product', 'quantity']


class PostCreateSerializer(ModelSerializer):
    needs = NeedCreateSerializer()

    class Meta:
        model = Post
        fields = ['description', 'enable_beds', 'needs']


class RefugeCreateSerializer(ModelSerializer):
    post = PostCreateSerializer()

    class Meta:
        model = Refuge
        fields = ['name', 'phone', 'location', 'city', 'state', 'post']
