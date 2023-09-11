from rest_framework import serializers

from toys.models import Toy, Brend


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = '__all__'


class BrendSerializer(serializers.ModelSerializer):
    toys_by_brend = serializers.StringRelatedField(many=True)

    class Meta:
        model = Brend
        fields = ['brend', 'toys_by_brend']
