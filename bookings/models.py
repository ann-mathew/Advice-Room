from django.db import models
from users.models import User
from advisors.models import Advisor
import secrets

def get_code():
	return secrets.token_hex(3).upper()

class Booking(models.Model):
    user_id = models.ForeignKey(User, to_field="user_id", db_column="user", on_delete=models.CASCADE)
    advisor_id = models.ForeignKey(Advisor, to_field="advisor_id", db_column="advisor", on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=6, primary_key=True, default=get_code, editable=False)
    booking_time = models.DateTimeField()

    def __str__(self):
        return self.booking_id
