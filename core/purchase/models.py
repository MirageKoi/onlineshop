from django.db import models
from store.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class PurchaseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
