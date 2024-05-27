from django.urls import path, include
from rest_framework import routers
from test_api import views

router = routers.DefaultRouter()
router.register(r'alumnos', views.AlumnoViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', include(router.urls))
]