from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Alert
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Alert
from .serializers import AlertSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

def test_email(request):
    try:
        send_mail(
            'Test Email',
            'This is a test email from Brevo.',
            settings.DEFAULT_FROM_EMAIL,
            ['komal.suryanarayana@gmail.com'],
            fail_silently=False,
        )
        return JsonResponse({'status': 'Email sent successfully'})
    except Exception as e:
        return JsonResponse({'status': 'Email failed', 'error': str(e)})

def home(request):
    return render(request, 'alerts/home.html')

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse



@csrf_exempt
def create_alert(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        target_price = data.get('target_price')

        alert = Alert.objects.create(email=email, target_price=target_price)
        return JsonResponse({'status': 'Alert created', 'alert_id': alert.id})

    return JsonResponse({'error': 'Invalid request'}, status=400)


from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Alert
from .serializers import AlertSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['DELETE'])
def delete_alert(request, pk):
    alert = get_object_or_404(Alert, pk=pk)
    alert.status = 'deleted'
    alert.save()
    return Response({'status': 'Alert deleted'}, status=status.HTTP_204_NO_CONTENT)


class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['get'])
    def filter_by_status(self, request):
        status = request.query_params.get('status')
        alerts = self.queryset.filter(status=status)
        page = self.paginate_queryset(alerts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(alerts, many=True)
        return Response(serializer.data)

