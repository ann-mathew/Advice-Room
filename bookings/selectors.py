from .models import Advisor
from bookings.models import Booking

def getBookingDetails(user_id: str):

    booking_data = []
    queryset = Booking.objects.filter(user_id=user_id).values('advisor_id', 'booking_time', 'booking_id')

    for dict_item in queryset:
        advisor = Advisor.objects.get(advisor_id=dict_item['advisor_id'])
        booking_data.append({
                        "advisor_id": dict_item["advisor_id"],
                        "photo_url": advisor.photo_url,
                        "name": advisor.name,
                        "booking_id" : dict_item["booking_id"],
                        "booking_time": dict_item["booking_time"]
                            })

    if not bool(booking_data):  
        return None
    else:
        return booking_data

