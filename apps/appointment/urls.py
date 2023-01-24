from django.urls import path
from .views import Reserve_Save, Get_Reserve

app_name="apps.appointment"

urlpatterns = [
    path('get-reserve/', Get_Reserve.as_view()),
    path('reserve/', Reserve_Save.as_view())
]
