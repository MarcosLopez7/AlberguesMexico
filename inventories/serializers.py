from rest_framework.serializers import ModelSerializer

from .models import Refuge, Post, Need


class NeedCreateSerializer(ModelSerializer):
    class Meta:
        model = Need
        fields = ['product', 'quantity']


class PostCreateSerializer(ModelSerializer):
    needs = NeedCreateSerializer(many=True)

    class Meta:
        model = Post
        fields = ('description', 'enable_beds', 'needs')

    def create(self, validated_data):
        need_data = validated_data.pop('needs')
        post = Post.objects.create(**validated_data)

        for data in need_data:
            Need.objects.create(post=post, **data)

        return post


class RefugeCreateSerializer(ModelSerializer):
    post = PostCreateSerializer()

    class Meta:
        model = Refuge
        fields = ('name', 'phone', 'location', 'city', 'state', 'post', 'user')

    def create(self, validated_data):
        post_data = validated_data.pop('post')
        refuge = Refuge.objects.create(**validated_data)

        need_data = post_data.pop('needs')
        post = Post.objects.create(refuge=refuge, **post_data)

        for data in need_data:
            Need.objects.create(post=post, **data)

        return refuge
