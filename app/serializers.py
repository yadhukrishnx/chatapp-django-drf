from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','tokens']
        
        extra_kwargs = {
            'password' : {'write_only':True},
            'tokens' : {'read_only':True},
        }
        
    def validate_username(self,value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists ! Try another one")
        return value
    
    def create(self,validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        