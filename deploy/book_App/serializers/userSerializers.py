from rest_framework import serializers
from book_App.models.user import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'firstname', 'lastname', 'address', 'email','phone','cantlib']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    def update(self, Instance, validated_data):
        Instance.firstname = validated_data.get('firstname', Instance.firstname)
        Instance.lasttname = validated_data.get('lastname', Instance.lastname)
        Instance.address = validated_data.get('address', Instance.address)
        Instance.email = validated_data.get('email', Instance.email)
        Instance.phone = validated_data.get('phone', Instance.phone)
        Instance.cantlib = validated_data.get('cantlib', Instance.cantlib)
        Instance.save()

        return Instance


    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'address': user.address,
            'email': user.email,
            'phone': user.phone,
            'cantlib': user.cantlib,
            
        }
