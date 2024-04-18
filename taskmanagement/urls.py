from django.contrib import admin
from django.urls import path, include
from tasks.views import index
from rest_framework.routers import DefaultRouter
from tasks.views import dataTaskViewset, stepsTaskViewset

router = DefaultRouter()
router.register('datatasks', dataTaskViewset, basename='Base')
router.register('steps', stepsTaskViewset, basename='Steps')

urlpatterns = [
    path('', index, name='Index'),
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
]
