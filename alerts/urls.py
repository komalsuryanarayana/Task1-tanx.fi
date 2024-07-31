# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AlertViewSet, home, create_alert

# router = DefaultRouter()
# router.register(r'alerts', AlertViewSet)

# urlpatterns = [
#     path('', home, name='home'),
#     path('create_alert/', create_alert, name='create_alert'),
#     path('api/', include(router.urls)),
# ]
# 
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet, home, create_alert, delete_alert, test_email

router = DefaultRouter()
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('create_alert/', create_alert, name='create_alert'),
    path('api/', include(router.urls)),
    path('api/alerts/delete/<int:pk>/', delete_alert, name='delete_alert'),
    path('test_email/', test_email, name='test_email'),  # Add this line
]
