from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Booking
from users.models import User
from advisors.models import Advisor                
from .serializers import CreateBookingSerializer    
from rest_framework.decorators import api_view
import json
from .selectors import getBookingDetails

"""
    API Response Table:

    400: Invalid POST
    200: Success

"""

@api_view(['POST'])
def create_booking(request, user_id, advisor_id):
    if request.method == 'POST':                                      
        booking_serializer = CreateBookingSerializer(data=request.data)
        print (booking_serializer)
        if booking_serializer.is_valid():
                user = get_object_or_404(User, user_id=user_id) 
                advisor = get_object_or_404(Advisor, advisor_id=advisor_id)
                booking = booking_serializer.save(user_id=user,
                                                advisor_id=advisor) 
                                               
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(booking_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_booking(request, user_id):
    if request.method == 'GET':  
            details = getBookingDetails(user_id)
            return Response(details, status=status.HTTP_200_OK)



