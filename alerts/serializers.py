# from rest_framework import serializers
# from .models import Alert

# class AlertSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Alert
#         fields = '__all__'


from rest_framework import serializers
from .models import Alert

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'email', 'target_price', 'status', 'created_at']  # Remove 'user' if not needed
