from project.models import Signup
from rest_framework import serializers
from .models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = '__all__'