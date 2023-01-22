from django.urls import path
from .views import Reserve

app_name="apps.appointment"

urlpatterns = [
    path('reserve/', Reserve.as_view())
]
