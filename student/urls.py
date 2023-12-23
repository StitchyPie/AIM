from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

app_name = 'student'

router = DefaultRouter()

router.register('student', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
