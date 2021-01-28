from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View """

    def get(self, request, format=None):
        """Returns a list of APIView features """
        an_apiview = [
            'Uses HTTP methods as function(get,post,delete,update,patch)',
            'Is similar to tradiationl Django view',
            'is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
