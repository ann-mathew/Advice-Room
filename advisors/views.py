from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status 
from bookings.models import Booking             
from .serializers import AddAdvisorSerializer     
from rest_framework.decorators import api_view
import json
from .selectors import getAdvisors

"""
    API Response Table:

    400: Invalid POST
    200: Advisor Added

"""

@api_view(['POST'])
def add_advisor(request):
    if request.method == 'POST':                                      
        advisor_serializer = AddAdvisorSerializer(data=request.data)
        if advisor_serializer.is_valid():
            advisor = advisor_serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(advisor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_advisor(request, user_id):
    if request.method == 'GET':  
            advisor = getAdvisors(user_id)
            return Response(advisor, status=status.HTTP_200_OK)


