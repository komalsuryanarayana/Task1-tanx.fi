# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User

# class Alert(models.Model):
#     email = models.EmailField()
#     target_price = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, default='created')  # created, triggered, deleted
#     created_at = models.DateTimeField(auto_now_add=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.email} - {self.target_price}'
from django.db import models

class Alert(models.Model):
    email = models.EmailField()
    target_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='created')  # created, triggered, deleted
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)  # Make user optional

    def __str__(self):
        return f'{self.email} - {self.target_price}'