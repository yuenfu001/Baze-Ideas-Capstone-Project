from django.shortcuts import render
from .serializers import ClientFormDataSerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    methods=['POST'],
    request_body=ClientFormDataSerializer,
    operation_description='Create Client Form Data'
)

@api_view(['POST'])
def create_client_form(request):
    if request.method == "POST":
        potential_client = ClientFormDataSerializer(data=request.data)
        if potential_client.is_valid():
            potential_client.save()
            return Response(potential_client.data, status=status.HTTP_201_CREATED)
        return Response(potential_client.errors, status=status.HTTP_400_BAD_REQUEST)
