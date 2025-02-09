from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Настройка Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Django REST API",
        default_version='v1',
        description="Документация для API вашего проекта",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# URL-конфигурация
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ваши API эндпоинты
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),  # Swagger UI
]
