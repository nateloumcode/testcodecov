from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from testcodecov.calculator.services import add, subtract, divide, exponentiate


class OperationSerializer(serializers.Serializer):
    a = serializers.IntegerField()
    b = serializers.IntegerField()


class AddView(APIView):
    serializer_class = OperationSerializer

    def get(self, request):
        a = request.query_params['a']
        b = request.query_params['b']
        result = add(a, b)
        return Response(status=status.HTTP_200_OK, data={ "result": result })


class SubtractView(APIView):
    serializer_class = OperationSerializer

    def get(self, request):
        a = request.query_params['a']
        b = request.query_params['b']
        result = subtract(a, b)
        return Response(status=status.HTTP_200_OK, data={ "result": result })


class DivideView(APIView):
    serializer_class = OperationSerializer

    def get(self, request):
        a = request.query_params['a']
        b = request.query_params['b']
        result = divide(a, b)
        return Response(status=status.HTTP_200_OK, data={ "result": result })


class RaiseView(APIView):
    serializer_class = OperationSerializer  # Consider renaming the serializer to a more appropriate name, e.g. ExponentSerializer

    def get(self, request):
        base = request.query_params['a']
        exponent = request.query_params['b']
        result = exponentiate(exponent, base)
        return Response(status=status.HTTP_200_OK, data={ "result": result })
