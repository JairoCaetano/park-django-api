from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('customer.urls')),
    path('api/v1/', include('operational.urls')),
]
