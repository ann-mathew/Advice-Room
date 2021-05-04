from .models import Advisor
from bookings.models import Booking

def getAdvisors(user_id: str):

    advisor_data = []
    queryset = Booking.objects.filter(user_id=user_id).values('advisor_id')

    for dict_item in queryset:
        advisor = Advisor.objects.get(advisor_id=dict_item['advisor_id'])
        advisor_data.append({
                        "advisor_id": advisor.advisor_id,
                        "photo_url": advisor.photo_url,
                        "name": advisor.name
                            })

    if not bool(advisor_data):  
        return None
    else:
        return advisor_data

