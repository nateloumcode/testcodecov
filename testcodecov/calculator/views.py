from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView


class AddSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()


class AddView(APIView):
    serializer_class = AddSerializer

    def get(self, request):
        a = request.query_params['a']
        b = request.query_params['b']
        result = int(a) + int(b)
        return Response(status=status.HTTP_200_OK, data={ "result": result })


class DivideView(APIView):
    serializer_class = AddSerializer

    def get(self, request):
        a = request.query_params['a']
        b = request.query_params['b']
        result = int(a) / int(b)
        return Response(status=status.HTTP_200_OK, data={ "result": result })


class ExponentView(APIView):
    serializer_class = AddSerializer  # Consider renaming the serializer to a more appropriate name, e.g. ExponentSerializer

    def get(self, request):
        base = request.query_params['base']
        exponent = request.query_params['exponent']
        result = int(base) ** int(exponent)
        return Response(status=status.HTTP_200_OK, data={ "result": result })