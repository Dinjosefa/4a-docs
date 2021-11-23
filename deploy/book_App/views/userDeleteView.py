from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from book_App.serializers.userSerializers import UserSerializer
from django.forms.models import model_to_dict 
from book_App.models.user import User 

class UserDeleteView(generics.RetrieveUpdateDestroyAPIView): 
    def destroy(self, request, *args, **kwargs): 
        serializer = UserSerializer(data=request.data) 
        pk = kwargs["pk"] 
        if User.objects.filter(id=pk).exists(): 
            instance = User.objects.get(pk=pk) 
            self.perform_destroy(instance) 
        else: 
            return Response({'message':'Usuario no existe en la base de datos'},status=status.HTTP_404_NOT_FOUND) 
        return Response({"message":"Se eliminó el usuario correctamente"}, status=status.HTTP_200_OK)