from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from basic import views

router = DefaultRouter()
router.register(r'stdapi', views.StudentModelViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Include the router URLs first
]