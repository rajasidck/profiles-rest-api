from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
import sys

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function(get,post,delete,update,patch)',
            'Is similar to tradiationl Django view',
            'Gives you the most control over you application logic',
            'is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self , request):
        """create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            # message = f'Hello {name}!'
            message = 'Hello :' + name
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status =status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self ,request, pk=None):
        """Delete an object """
        return Response({'method': 'DELETE'})
