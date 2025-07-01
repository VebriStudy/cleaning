from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CleaningServiceViewSet, BookingViewSet

# Buat router dan daftarkan viewset
router = DefaultRouter()
router.register(r'services', CleaningServiceViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # semua endpoint API akan diakses lewat /api/
]
