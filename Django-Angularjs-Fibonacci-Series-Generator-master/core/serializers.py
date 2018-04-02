from rest_framework import serializers

from .models import Fibonacci


class FibSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fibonacci
        fields = '__all__'








