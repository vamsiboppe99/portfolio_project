from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('resume.urls')),  # Replace 'your_app_name' with your actual app name
]