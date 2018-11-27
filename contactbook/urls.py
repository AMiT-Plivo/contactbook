from django.urls import path, include

from contactbook import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('contact', views.ContactView)

urlpatterns = [
    path('', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
]