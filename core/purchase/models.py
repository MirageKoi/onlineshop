from django.db import models
from store.models import Product
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)

    def time_difference(self):
        current_time = timezone.now()
        time_diff = (current_time - self.ordered_date).total_seconds()
        if time_diff < 180:
            return True
        return False
       

class ReturnModel(models.Model):
    product_return = models.ForeignKey(PurchaseModel, on_delete=models.CASCADE)
    pending = models.BooleanField(default=False)

    